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
            'identifier': 1139372,
            'width': 5841093612863723647,
            'height': 8523407647623939264,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': -976731,

            'width': 1416218402434409747,

            'height': 5014974573898878293,

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
            'source_monitor': 7524420,
            'source_nw_x_pixel': -4040645713651253249,
            'source_nw_y_pixel': -5640901713713938466,
            'source_pixel_width': -1847722558898297567,
            'source_pixel_height': -1276916556651080798,
            'rotation': -4161793164640357283,
            'virtual_nw_x_pixel': 788318289,
            'virtual_nw_y_pixel': 1004987174,
            'virtual_width': -177584691,
            'virtual_height': -444720766,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -8343689627971511715,

            'source_nw_y_pixel': -6783506028318965735,

            'source_pixel_width': -4040511346719138302,

            'source_pixel_height': -4335918455479486219,

            'rotation': -4802316936355520670,

            'virtual_nw_x_pixel': 132316216,

            'virtual_nw_y_pixel': -1482567478,

            'virtual_width': -500844595,

            'virtual_height': 1638214170,

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
            'description': 'ɒɹ&œҮѕˤŬЀnˎȰðʂƩŹƊɈĹǠˏ˼äЙӓ\x7fʉϛ˧Ϫ',
            'monitors': [
                {
                    'identifier': -780452,
                    'width': 6797502789045277696,
                    'height': -7775370136000137165,
                },
                {
                    'identifier': 3294707,
                    'width': -6499547948999350695,
                    'height': -5485979500445694589,
                },
                {
                    'identifier': -314435,
                    'width': -8448838863114467091,
                    'height': -1246548279375581830,
                },
                {
                    'identifier': -981766,
                    'width': 6909098190503080404,
                    'height': 5971442302888082785,
                },
                {
                    'identifier': -3929,
                    'width': 8026835556608775363,
                    'height': -1316637142593029866,
                },
                {
                    'identifier': 8592619,
                    'width': -5223585600102744769,
                    'height': 1185309373730612454,
                },
                {
                    'identifier': 697071,
                    'width': 8424185278704349039,
                    'height': 5088158384510397752,
                },
                {
                    'identifier': 2982829,
                    'width': -1155216553911132312,
                    'height': -2985545925717251843,
                },
                {
                    'identifier': 2705379,
                    'width': 6364840658506980148,
                    'height': 5260730805597843932,
                },
                {
                    'identifier': 1519178,
                    'width': 7046946610728700918,
                    'height': 2390447658738938889,
                },
            ],
            'screen': [
                {
                    'source_monitor': 8087032,
                    'source_nw_x_pixel': -552281503526715644,
                    'source_nw_y_pixel': -6778585408866957800,
                    'source_pixel_width': -1215247876588397273,
                    'source_pixel_height': -4716123423376630311,
                    'rotation': -1225493208259340471,
                    'virtual_nw_x_pixel': -765480114,
                    'virtual_nw_y_pixel': -749450148,
                    'virtual_width': 149441214,
                    'virtual_height': 27935877,
                },
                {
                    'source_monitor': 9083887,
                    'source_nw_x_pixel': -2939602976646556660,
                    'source_nw_y_pixel': -4609043660827073225,
                    'source_pixel_width': -3193403246988868599,
                    'source_pixel_height': -4622804779400971365,
                    'rotation': -4122345245652906300,
                    'virtual_nw_x_pixel': 102292426,
                    'virtual_nw_y_pixel': 1622222798,
                    'virtual_width': -85741945,
                    'virtual_height': -1536299231,
                },
                {
                    'source_monitor': 4629512,
                    'source_nw_x_pixel': -1326245717783796008,
                    'source_nw_y_pixel': -771714743728745286,
                    'source_pixel_width': -7028718357012791252,
                    'source_pixel_height': -8590256668740606565,
                    'rotation': -2374035857278607462,
                    'virtual_nw_x_pixel': 315776718,
                    'virtual_nw_y_pixel': -671537088,
                    'virtual_width': -1825848194,
                    'virtual_height': 1884984095,
                },
                {
                    'source_monitor': 8538138,
                    'source_nw_x_pixel': -6185538450643056324,
                    'source_nw_y_pixel': -3429936089630173804,
                    'source_pixel_width': -7445809437540466339,
                    'source_pixel_height': -7091420619409187449,
                    'rotation': -2566904490673834135,
                    'virtual_nw_x_pixel': 626480359,
                    'virtual_nw_y_pixel': -1822634771,
                    'virtual_width': -688396577,
                    'virtual_height': 1861704518,
                },
                {
                    'source_monitor': 743930,
                    'source_nw_x_pixel': -4121708708453869361,
                    'source_nw_y_pixel': -138206152231960530,
                    'source_pixel_width': -4095170596039243791,
                    'source_pixel_height': -3967981712985056898,
                    'rotation': -2206342840159756458,
                    'virtual_nw_x_pixel': 1743450149,
                    'virtual_nw_y_pixel': 1925558326,
                    'virtual_width': -1236085601,
                    'virtual_height': -1734874839,
                },
                {
                    'source_monitor': -364722,
                    'source_nw_x_pixel': -287518073484048226,
                    'source_nw_y_pixel': -1989195749597554301,
                    'source_pixel_width': -8389307262244040887,
                    'source_pixel_height': -4397986922530302068,
                    'rotation': -2566163536147158961,
                    'virtual_nw_x_pixel': 1074443897,
                    'virtual_nw_y_pixel': -634544290,
                    'virtual_width': -648391215,
                    'virtual_height': 287785326,
                },
                {
                    'source_monitor': 8681231,
                    'source_nw_x_pixel': -4046382545677478624,
                    'source_nw_y_pixel': -5651757583396902140,
                    'source_pixel_width': -1408848683364951446,
                    'source_pixel_height': -7848514057794483695,
                    'rotation': -8349589377318215225,
                    'virtual_nw_x_pixel': -1807998099,
                    'virtual_nw_y_pixel': 643181714,
                    'virtual_width': -342243151,
                    'virtual_height': 1008410133,
                },
                {
                    'source_monitor': -700862,
                    'source_nw_x_pixel': -6628350275563200164,
                    'source_nw_y_pixel': -3921534303598099203,
                    'source_pixel_width': -3164782941797298972,
                    'source_pixel_height': -4549608376645768080,
                    'rotation': -4174399808260898889,
                    'virtual_nw_x_pixel': -19397481,
                    'virtual_nw_y_pixel': 1459703872,
                    'virtual_width': -1443202035,
                    'virtual_height': 246784035,
                },
                {
                    'source_monitor': 7113705,
                    'source_nw_x_pixel': -8469969894679389898,
                    'source_nw_y_pixel': -9170114616078707597,
                    'source_pixel_width': -4217661550961427477,
                    'source_pixel_height': -1671287171579946182,
                    'rotation': -7470783741057884652,
                    'virtual_nw_x_pixel': 1663580107,
                    'virtual_nw_y_pixel': -1725933084,
                    'virtual_width': 1519096617,
                    'virtual_height': -1590979020,
                },
                {
                    'source_monitor': -870887,
                    'source_nw_x_pixel': -4363881767485674785,
                    'source_nw_y_pixel': -980332463957116161,
                    'source_pixel_width': -834108708496528192,
                    'source_pixel_height': -6973108037630417917,
                    'rotation': -5601682984996338898,
                    'virtual_nw_x_pixel': -998067047,
                    'virtual_nw_y_pixel': 582361409,
                    'virtual_width': -1633335839,
                    'virtual_height': -320166000,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 2453522,
                    'width': -657235133210036782,
                    'height': -2813136302073413882,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -844216649350122470,
                    'source_nw_y_pixel': -6329782340488493525,
                    'source_pixel_width': -6157342599619287976,
                    'source_pixel_height': -1026315019675965632,
                    'rotation': -2690353703897156239,
                    'virtual_nw_x_pixel': 1087839478,
                    'virtual_nw_y_pixel': -816510416,
                    'virtual_width': -1011420267,
                    'virtual_height': 188116228,
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
            'request_id': 2530842,
            'mapped_screens_by_monitors': [
                {
                    'description': '\x9fԪľʙірѴƾȜ\x86ϋ҄ˈςłӳη¼ĆƜƱτÐщϙǒOНτ)',
                    'monitors': [
                            {
                                        'identifier': 7227966,
                                        'width': -8401410425978646467,
                                        'height': -6081021492976032075,
                                    },
                            {
                                        'identifier': 7298061,
                                        'width': -3498448863915527828,
                                        'height': -1010321709299929672,
                                    },
                            {
                                        'identifier': 7145655,
                                        'width': 2507302247371960383,
                                        'height': -8538800436682854195,
                                    },
                            {
                                        'identifier': 115813,
                                        'width': 6217874756168825973,
                                        'height': -2176088751258445142,
                                    },
                            {
                                        'identifier': 6250117,
                                        'width': 2142774243668092309,
                                        'height': -1529250780612720356,
                                    },
                            {
                                        'identifier': 6963130,
                                        'width': -6530807646767675603,
                                        'height': -5046194757991698416,
                                    },
                            {
                                        'identifier': 8334851,
                                        'width': 7921163873049274977,
                                        'height': 2107010921276080528,
                                    },
                            {
                                        'identifier': 7550287,
                                        'width': 2036712112200632630,
                                        'height': 3648947540298936223,
                                    },
                            {
                                        'identifier': 2114983,
                                        'width': -3647658515818235279,
                                        'height': 8859686605857254228,
                                    },
                            {
                                        'identifier': 2805107,
                                        'width': 7889659976054086689,
                                        'height': -7552775273202523758,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5221839,
                                        'source_nw_x_pixel': -7336913643763801464,
                                        'source_nw_y_pixel': -4088461852571216380,
                                        'source_pixel_width': -7000759489335739863,
                                        'source_pixel_height': -3846827013727017993,
                                        'rotation': -5214427787361890983,
                                        'virtual_nw_x_pixel': 1112953056,
                                        'virtual_nw_y_pixel': 1955690498,
                                        'virtual_width': 73309507,
                                        'virtual_height': -100699696,
                                    },
                            {
                                        'source_monitor': 4524024,
                                        'source_nw_x_pixel': -1286803647252547317,
                                        'source_nw_y_pixel': -3174614949717883084,
                                        'source_pixel_width': -7781698905372419707,
                                        'source_pixel_height': -3545269641239426208,
                                        'rotation': -1236621501023730617,
                                        'virtual_nw_x_pixel': 45457481,
                                        'virtual_nw_y_pixel': -1779700134,
                                        'virtual_width': 1619934710,
                                        'virtual_height': 1606750868,
                                    },
                            {
                                        'source_monitor': 7832759,
                                        'source_nw_x_pixel': -5758643458049048613,
                                        'source_nw_y_pixel': -3499146733480003127,
                                        'source_pixel_width': -675423303521996196,
                                        'source_pixel_height': -4015039034031325539,
                                        'rotation': -5515011897915568019,
                                        'virtual_nw_x_pixel': 1831576469,
                                        'virtual_nw_y_pixel': 935944862,
                                        'virtual_width': -836053554,
                                        'virtual_height': 1368479989,
                                    },
                            {
                                        'source_monitor': 8226805,
                                        'source_nw_x_pixel': -3278424444785432128,
                                        'source_nw_y_pixel': -3474821769921813410,
                                        'source_pixel_width': -6926247942745749597,
                                        'source_pixel_height': -1643078021486913786,
                                        'rotation': -8940423960675797441,
                                        'virtual_nw_x_pixel': 1518011735,
                                        'virtual_nw_y_pixel': 944012484,
                                        'virtual_width': 387868224,
                                        'virtual_height': -221749056,
                                    },
                            {
                                        'source_monitor': -568937,
                                        'source_nw_x_pixel': -2303091983125419492,
                                        'source_nw_y_pixel': -3748204417089809760,
                                        'source_pixel_width': -2398627665652421299,
                                        'source_pixel_height': -860617198460549139,
                                        'rotation': -9041010801957437597,
                                        'virtual_nw_x_pixel': 1247775796,
                                        'virtual_nw_y_pixel': -982219858,
                                        'virtual_width': 1481749952,
                                        'virtual_height': -78390092,
                                    },
                            {
                                        'source_monitor': 6587025,
                                        'source_nw_x_pixel': -8113650505690003204,
                                        'source_nw_y_pixel': -3886975982538570986,
                                        'source_pixel_width': -5025731092775905627,
                                        'source_pixel_height': -7736643438137608625,
                                        'rotation': -8617646606299976413,
                                        'virtual_nw_x_pixel': 1552664149,
                                        'virtual_nw_y_pixel': -1900602151,
                                        'virtual_width': -1978657412,
                                        'virtual_height': 1631743947,
                                    },
                            {
                                        'source_monitor': 7763829,
                                        'source_nw_x_pixel': -709132282894844647,
                                        'source_nw_y_pixel': -4176243276079240763,
                                        'source_pixel_width': -6642788092765172272,
                                        'source_pixel_height': -7835928006503704361,
                                        'rotation': -489967819365862353,
                                        'virtual_nw_x_pixel': 1300999591,
                                        'virtual_nw_y_pixel': 1065908640,
                                        'virtual_width': -318278920,
                                        'virtual_height': 1092497191,
                                    },
                            {
                                        'source_monitor': 2051345,
                                        'source_nw_x_pixel': -4475550485061557627,
                                        'source_nw_y_pixel': -3989977712707765481,
                                        'source_pixel_width': -2016080915213284960,
                                        'source_pixel_height': -8393300789771771531,
                                        'rotation': -4681482296322551840,
                                        'virtual_nw_x_pixel': 162840082,
                                        'virtual_nw_y_pixel': 142359069,
                                        'virtual_width': 73336025,
                                        'virtual_height': 1110418729,
                                    },
                            {
                                        'source_monitor': 9639067,
                                        'source_nw_x_pixel': -2539469844875046187,
                                        'source_nw_y_pixel': -2613344604795974385,
                                        'source_pixel_width': -4001891062986108083,
                                        'source_pixel_height': -4783139099067895113,
                                        'rotation': -6796574744808517487,
                                        'virtual_nw_x_pixel': -550458326,
                                        'virtual_nw_y_pixel': -1780636599,
                                        'virtual_width': 838280746,
                                        'virtual_height': 1010143972,
                                    },
                            {
                                        'source_monitor': 3174182,
                                        'source_nw_x_pixel': -985085657013600318,
                                        'source_nw_y_pixel': -153224786100101690,
                                        'source_pixel_width': -2289399251824321393,
                                        'source_pixel_height': -218135584540887435,
                                        'rotation': -2253081308192248638,
                                        'virtual_nw_x_pixel': -655384552,
                                        'virtual_nw_y_pixel': 124092112,
                                        'virtual_width': 639496540,
                                        'virtual_height': 1411434045,
                                    },
                        ],
                },
                {
                    'description': 'άƀ˧ɏҳȯ˲ƁӲʽǟͷΆ8ƒ˷˄ȵŸfķҴіȦŃɲřûƯ®',
                    'monitors': [
                            {
                                        'identifier': 3439712,
                                        'width': -6997820083669965917,
                                        'height': -2597405424221224668,
                                    },
                            {
                                        'identifier': 2654279,
                                        'width': 3604300507055636377,
                                        'height': -7038115392545277806,
                                    },
                            {
                                        'identifier': 4103646,
                                        'width': -8152718573037053606,
                                        'height': 2616712436591781144,
                                    },
                            {
                                        'identifier': 7083266,
                                        'width': -4902894006549097278,
                                        'height': 9083461698036027327,
                                    },
                            {
                                        'identifier': 3701828,
                                        'width': 5333615169481150135,
                                        'height': 4862705149609363385,
                                    },
                            {
                                        'identifier': 4574122,
                                        'width': -5130367626432339062,
                                        'height': 6343629691932693038,
                                    },
                            {
                                        'identifier': 9286393,
                                        'width': 8930280103197617326,
                                        'height': 6188390371287242122,
                                    },
                            {
                                        'identifier': 5276429,
                                        'width': 484664855185419691,
                                        'height': 710729550283670396,
                                    },
                            {
                                        'identifier': 5513728,
                                        'width': 9219041461023719648,
                                        'height': 127791647202439786,
                                    },
                            {
                                        'identifier': 7535782,
                                        'width': 9141461683448367358,
                                        'height': -3543032917249710826,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4355806,
                                        'source_nw_x_pixel': -2344924951680586203,
                                        'source_nw_y_pixel': -8999691243315377947,
                                        'source_pixel_width': -5979427795824042130,
                                        'source_pixel_height': -7791947749235424085,
                                        'rotation': -7305728812195681304,
                                        'virtual_nw_x_pixel': 1229578823,
                                        'virtual_nw_y_pixel': 1855759639,
                                        'virtual_width': 536889679,
                                        'virtual_height': -536470914,
                                    },
                            {
                                        'source_monitor': -44871,
                                        'source_nw_x_pixel': -7258908301424205847,
                                        'source_nw_y_pixel': -2238282593871005688,
                                        'source_pixel_width': -4779597467446427037,
                                        'source_pixel_height': -7397214399285805435,
                                        'rotation': -6931200010480609274,
                                        'virtual_nw_x_pixel': -1698566274,
                                        'virtual_nw_y_pixel': 1923209576,
                                        'virtual_width': -262883874,
                                        'virtual_height': 388092515,
                                    },
                            {
                                        'source_monitor': 3640680,
                                        'source_nw_x_pixel': -6519981801016848024,
                                        'source_nw_y_pixel': -6093565161782744718,
                                        'source_pixel_width': -6642924795083184548,
                                        'source_pixel_height': -8612695656294704334,
                                        'rotation': -3840578951155184281,
                                        'virtual_nw_x_pixel': 1675878921,
                                        'virtual_nw_y_pixel': -1568397815,
                                        'virtual_width': 226557518,
                                        'virtual_height': -998305481,
                                    },
                            {
                                        'source_monitor': 945428,
                                        'source_nw_x_pixel': -6299437123135774501,
                                        'source_nw_y_pixel': -6396110521033205584,
                                        'source_pixel_width': -4930158559109419556,
                                        'source_pixel_height': -3139833675501040619,
                                        'rotation': -354641103077149315,
                                        'virtual_nw_x_pixel': -891611283,
                                        'virtual_nw_y_pixel': 52430460,
                                        'virtual_width': -1439978456,
                                        'virtual_height': 1611849059,
                                    },
                            {
                                        'source_monitor': 5636480,
                                        'source_nw_x_pixel': -6611554668297354653,
                                        'source_nw_y_pixel': -1532197941492528958,
                                        'source_pixel_width': -2479268329319725277,
                                        'source_pixel_height': -7425628895586405193,
                                        'rotation': -3740205551517334849,
                                        'virtual_nw_x_pixel': 1854935836,
                                        'virtual_nw_y_pixel': -212583902,
                                        'virtual_width': 325111350,
                                        'virtual_height': 1016548098,
                                    },
                            {
                                        'source_monitor': 4417155,
                                        'source_nw_x_pixel': -8409022011940826727,
                                        'source_nw_y_pixel': -5049220669129794423,
                                        'source_pixel_width': -5486576034696173728,
                                        'source_pixel_height': -8892814844488276515,
                                        'rotation': -155498684901261595,
                                        'virtual_nw_x_pixel': 1131476465,
                                        'virtual_nw_y_pixel': -1580720359,
                                        'virtual_width': -285436886,
                                        'virtual_height': 1605251149,
                                    },
                            {
                                        'source_monitor': 7584341,
                                        'source_nw_x_pixel': -8160938197202341269,
                                        'source_nw_y_pixel': -7483602580747715208,
                                        'source_pixel_width': -3916138049640544996,
                                        'source_pixel_height': -6122939002892687238,
                                        'rotation': -5875541640168909151,
                                        'virtual_nw_x_pixel': 1910681294,
                                        'virtual_nw_y_pixel': -404157665,
                                        'virtual_width': 487900344,
                                        'virtual_height': 817205521,
                                    },
                            {
                                        'source_monitor': 6516923,
                                        'source_nw_x_pixel': -6670147087479509035,
                                        'source_nw_y_pixel': -4812936420565669321,
                                        'source_pixel_width': -2346798478748643569,
                                        'source_pixel_height': -3595619186218853492,
                                        'rotation': -2014897636768302081,
                                        'virtual_nw_x_pixel': -1724661213,
                                        'virtual_nw_y_pixel': 257894115,
                                        'virtual_width': 574832162,
                                        'virtual_height': 621409919,
                                    },
                            {
                                        'source_monitor': 5830339,
                                        'source_nw_x_pixel': -3689333950899223516,
                                        'source_nw_y_pixel': -7896841040691572502,
                                        'source_pixel_width': -4748582854860086110,
                                        'source_pixel_height': -7662640987867867785,
                                        'rotation': -3583796005026664511,
                                        'virtual_nw_x_pixel': -1506900663,
                                        'virtual_nw_y_pixel': 1497286148,
                                        'virtual_width': -1467624313,
                                        'virtual_height': -1064574244,
                                    },
                            {
                                        'source_monitor': 31891,
                                        'source_nw_x_pixel': -7475692290070020516,
                                        'source_nw_y_pixel': -7153974447433006154,
                                        'source_pixel_width': -3546681678938776544,
                                        'source_pixel_height': -201896732968573356,
                                        'rotation': -4088475727199940040,
                                        'virtual_nw_x_pixel': 1548376824,
                                        'virtual_nw_y_pixel': 361526882,
                                        'virtual_width': 403139627,
                                        'virtual_height': 86377770,
                                    },
                        ],
                },
                {
                    'description': 'ƮˢѡɌ\u038bԔʖˬŢтμΫ£ʩӯͳǉԈêԮʠĮɆϚ¼ΘǸԉɡ\u0379',
                    'monitors': [
                            {
                                        'identifier': 4121472,
                                        'width': -7260515434432299375,
                                        'height': -8673139626631036208,
                                    },
                            {
                                        'identifier': 3579999,
                                        'width': -5855782469343363579,
                                        'height': 21949030052501847,
                                    },
                            {
                                        'identifier': 5972983,
                                        'width': -324743649625157050,
                                        'height': -7385213523044881720,
                                    },
                            {
                                        'identifier': 7075590,
                                        'width': -6186487917584109903,
                                        'height': 7517987972740976585,
                                    },
                            {
                                        'identifier': -667183,
                                        'width': -8867927975947587509,
                                        'height': 3923846235966165002,
                                    },
                            {
                                        'identifier': 9119183,
                                        'width': -1667053729238194932,
                                        'height': -8855685204285906170,
                                    },
                            {
                                        'identifier': 3230317,
                                        'width': 4908869786742765585,
                                        'height': -3482789689944140875,
                                    },
                            {
                                        'identifier': 9135275,
                                        'width': -536037112778102209,
                                        'height': 7042340860371245163,
                                    },
                            {
                                        'identifier': 9329795,
                                        'width': -1421628535757838808,
                                        'height': -6675848660063887877,
                                    },
                            {
                                        'identifier': 6880947,
                                        'width': 3612396306277756240,
                                        'height': 4614561785062527800,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2655540,
                                        'source_nw_x_pixel': -193548641681786799,
                                        'source_nw_y_pixel': -8407571156628275254,
                                        'source_pixel_width': -2324875864049917711,
                                        'source_pixel_height': -6110424241414730982,
                                        'rotation': -5796498863011335308,
                                        'virtual_nw_x_pixel': 485628959,
                                        'virtual_nw_y_pixel': -1518828594,
                                        'virtual_width': -1793435696,
                                        'virtual_height': -908730163,
                                    },
                            {
                                        'source_monitor': 3635895,
                                        'source_nw_x_pixel': -6462755233252203487,
                                        'source_nw_y_pixel': -989455982836940545,
                                        'source_pixel_width': -4648562883558284332,
                                        'source_pixel_height': -5184881385797791857,
                                        'rotation': -1032476670585460357,
                                        'virtual_nw_x_pixel': -54859176,
                                        'virtual_nw_y_pixel': 868870719,
                                        'virtual_width': -1034002890,
                                        'virtual_height': -1420588175,
                                    },
                            {
                                        'source_monitor': 12572,
                                        'source_nw_x_pixel': -3213447460535987848,
                                        'source_nw_y_pixel': -8022323279672867871,
                                        'source_pixel_width': -2678707340130185161,
                                        'source_pixel_height': -3971827949780228115,
                                        'rotation': -3410147583581468106,
                                        'virtual_nw_x_pixel': -1068942118,
                                        'virtual_nw_y_pixel': 1724151266,
                                        'virtual_width': -327129034,
                                        'virtual_height': 1690015095,
                                    },
                            {
                                        'source_monitor': 1759131,
                                        'source_nw_x_pixel': -3616479967774166977,
                                        'source_nw_y_pixel': -7587668223212324759,
                                        'source_pixel_width': -8051009876037623913,
                                        'source_pixel_height': -608438194413976040,
                                        'rotation': -4345678202875792369,
                                        'virtual_nw_x_pixel': -778455336,
                                        'virtual_nw_y_pixel': -374625444,
                                        'virtual_width': -70824419,
                                        'virtual_height': 732106997,
                                    },
                            {
                                        'source_monitor': 3099778,
                                        'source_nw_x_pixel': -8379202719763964550,
                                        'source_nw_y_pixel': -3737231026728040345,
                                        'source_pixel_width': -2302187458956612658,
                                        'source_pixel_height': -453206550651800531,
                                        'rotation': -3271791604913193943,
                                        'virtual_nw_x_pixel': -1846324904,
                                        'virtual_nw_y_pixel': -666818868,
                                        'virtual_width': -1651025352,
                                        'virtual_height': -886208804,
                                    },
                            {
                                        'source_monitor': 804930,
                                        'source_nw_x_pixel': -4873236668196700069,
                                        'source_nw_y_pixel': -9010078787911723223,
                                        'source_pixel_width': -4611051709648739094,
                                        'source_pixel_height': -9214486857741180093,
                                        'rotation': -4846738980078755489,
                                        'virtual_nw_x_pixel': -913595397,
                                        'virtual_nw_y_pixel': -1857369958,
                                        'virtual_width': 1789469974,
                                        'virtual_height': 1582723413,
                                    },
                            {
                                        'source_monitor': 6660453,
                                        'source_nw_x_pixel': -9163479640027307355,
                                        'source_nw_y_pixel': -525949234814442530,
                                        'source_pixel_width': -9143049577691673332,
                                        'source_pixel_height': -2791350743615379287,
                                        'rotation': -5126081341447048133,
                                        'virtual_nw_x_pixel': -1399334826,
                                        'virtual_nw_y_pixel': 1409910509,
                                        'virtual_width': -447621418,
                                        'virtual_height': 434623628,
                                    },
                            {
                                        'source_monitor': 3240177,
                                        'source_nw_x_pixel': -4459985803529465586,
                                        'source_nw_y_pixel': -540952065934812792,
                                        'source_pixel_width': -597831967309022223,
                                        'source_pixel_height': -6521392505198333247,
                                        'rotation': -8603634096797327313,
                                        'virtual_nw_x_pixel': 1781560627,
                                        'virtual_nw_y_pixel': -1809468256,
                                        'virtual_width': -750381312,
                                        'virtual_height': 171188653,
                                    },
                            {
                                        'source_monitor': 2920182,
                                        'source_nw_x_pixel': -6142944717449127252,
                                        'source_nw_y_pixel': -1834271551195094376,
                                        'source_pixel_width': -2160736096225263789,
                                        'source_pixel_height': -4595783282959776775,
                                        'rotation': -8945039809930060440,
                                        'virtual_nw_x_pixel': -1778928726,
                                        'virtual_nw_y_pixel': -1858499616,
                                        'virtual_width': 1577044241,
                                        'virtual_height': 505678592,
                                    },
                            {
                                        'source_monitor': 5093659,
                                        'source_nw_x_pixel': -8021242424623851855,
                                        'source_nw_y_pixel': -8800532811481002124,
                                        'source_pixel_width': -3210075514391775670,
                                        'source_pixel_height': -674822165576338916,
                                        'rotation': -9032796252171759082,
                                        'virtual_nw_x_pixel': -722054099,
                                        'virtual_nw_y_pixel': -1166921815,
                                        'virtual_width': 564075206,
                                        'virtual_height': -1498667015,
                                    },
                        ],
                },
                {
                    'description': 'Oǆɋ\x7fҿқÀҭʸ\\ǈȑΌòcҵ҇ԒήəƔ.Č\x98ɠǵВ\x86Лӓ',
                    'monitors': [
                            {
                                        'identifier': 5314424,
                                        'width': -5176788208154633011,
                                        'height': -6893836004439792625,
                                    },
                            {
                                        'identifier': 161276,
                                        'width': 5209747998786763677,
                                        'height': 5779657147584657352,
                                    },
                            {
                                        'identifier': 9248849,
                                        'width': 3370655325028021391,
                                        'height': -4160140531928081518,
                                    },
                            {
                                        'identifier': 9423669,
                                        'width': 1582776101254147193,
                                        'height': 3040224466176539699,
                                    },
                            {
                                        'identifier': 6666819,
                                        'width': -7427200816878756209,
                                        'height': 7031177457138497609,
                                    },
                            {
                                        'identifier': 9103716,
                                        'width': 990221864039513343,
                                        'height': 8998756232153742391,
                                    },
                            {
                                        'identifier': 7853257,
                                        'width': 992741969501564702,
                                        'height': -1273699056641798722,
                                    },
                            {
                                        'identifier': 829638,
                                        'width': -2975636667276610998,
                                        'height': 7448293875892079502,
                                    },
                            {
                                        'identifier': -202012,
                                        'width': 4225547651901490284,
                                        'height': 9146940801790023500,
                                    },
                            {
                                        'identifier': 7507319,
                                        'width': -871961827845271978,
                                        'height': 5892457954884605765,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 279391,
                                        'source_nw_x_pixel': -2851388140405664551,
                                        'source_nw_y_pixel': -7714317294656477028,
                                        'source_pixel_width': -1912681045782886151,
                                        'source_pixel_height': -8201726684804233165,
                                        'rotation': -5126703944471259856,
                                        'virtual_nw_x_pixel': 121368825,
                                        'virtual_nw_y_pixel': 230715109,
                                        'virtual_width': -753013670,
                                        'virtual_height': -1936215032,
                                    },
                            {
                                        'source_monitor': 7552808,
                                        'source_nw_x_pixel': -2702638868518376054,
                                        'source_nw_y_pixel': -6366692831391837235,
                                        'source_pixel_width': -3004180504617212334,
                                        'source_pixel_height': -6206651767963191982,
                                        'rotation': -6395246127146891724,
                                        'virtual_nw_x_pixel': -880566379,
                                        'virtual_nw_y_pixel': 516334158,
                                        'virtual_width': -1904148128,
                                        'virtual_height': 668036462,
                                    },
                            {
                                        'source_monitor': 3452245,
                                        'source_nw_x_pixel': -9191827198745512205,
                                        'source_nw_y_pixel': -7283985395357866754,
                                        'source_pixel_width': -4229380637609893191,
                                        'source_pixel_height': -1661832734074084948,
                                        'rotation': -6999058672465849945,
                                        'virtual_nw_x_pixel': 139712003,
                                        'virtual_nw_y_pixel': 273547284,
                                        'virtual_width': -493212426,
                                        'virtual_height': 490127869,
                                    },
                            {
                                        'source_monitor': -956424,
                                        'source_nw_x_pixel': -3731062201169712311,
                                        'source_nw_y_pixel': -9169467932386986295,
                                        'source_pixel_width': -886412445547517843,
                                        'source_pixel_height': -5874496494206449385,
                                        'rotation': -1219181423225910295,
                                        'virtual_nw_x_pixel': -656266566,
                                        'virtual_nw_y_pixel': 1451738402,
                                        'virtual_width': 1642726673,
                                        'virtual_height': -727813458,
                                    },
                            {
                                        'source_monitor': 4908419,
                                        'source_nw_x_pixel': -685246819781903549,
                                        'source_nw_y_pixel': -1332069945082125134,
                                        'source_pixel_width': -1568792002193236515,
                                        'source_pixel_height': -1256002086028992949,
                                        'rotation': -6030117472928091454,
                                        'virtual_nw_x_pixel': 1665204006,
                                        'virtual_nw_y_pixel': 697657279,
                                        'virtual_width': 519027513,
                                        'virtual_height': 262305998,
                                    },
                            {
                                        'source_monitor': 3143053,
                                        'source_nw_x_pixel': -5496017647811461160,
                                        'source_nw_y_pixel': -8702081309587743807,
                                        'source_pixel_width': -8799364471463323734,
                                        'source_pixel_height': -2031975352993305159,
                                        'rotation': -3499220405324551884,
                                        'virtual_nw_x_pixel': -1329688383,
                                        'virtual_nw_y_pixel': 1438543663,
                                        'virtual_width': -1764820563,
                                        'virtual_height': 1535038593,
                                    },
                            {
                                        'source_monitor': 9487841,
                                        'source_nw_x_pixel': -6635370262569241750,
                                        'source_nw_y_pixel': -1416889682813375494,
                                        'source_pixel_width': -4926114665372374727,
                                        'source_pixel_height': -8612375250627204961,
                                        'rotation': -5822476875163339690,
                                        'virtual_nw_x_pixel': 1656369857,
                                        'virtual_nw_y_pixel': 302772245,
                                        'virtual_width': -1999660107,
                                        'virtual_height': 439379923,
                                    },
                            {
                                        'source_monitor': 8482661,
                                        'source_nw_x_pixel': -6092264452719096906,
                                        'source_nw_y_pixel': -7022249711510240978,
                                        'source_pixel_width': -6001163077094165785,
                                        'source_pixel_height': -5457477903282309830,
                                        'rotation': -7419217754381875213,
                                        'virtual_nw_x_pixel': 454528202,
                                        'virtual_nw_y_pixel': -88134059,
                                        'virtual_width': -482838720,
                                        'virtual_height': -1800459750,
                                    },
                            {
                                        'source_monitor': 2935194,
                                        'source_nw_x_pixel': -8392925043650286792,
                                        'source_nw_y_pixel': -1627055761385445569,
                                        'source_pixel_width': -8197095565973968359,
                                        'source_pixel_height': -2374573747958645580,
                                        'rotation': -982824004157580424,
                                        'virtual_nw_x_pixel': -1468124002,
                                        'virtual_nw_y_pixel': -208588519,
                                        'virtual_width': -1523101220,
                                        'virtual_height': 690596864,
                                    },
                            {
                                        'source_monitor': 1356630,
                                        'source_nw_x_pixel': -88545029239145861,
                                        'source_nw_y_pixel': -163295368490841124,
                                        'source_pixel_width': -2534553638674718232,
                                        'source_pixel_height': -6000328795404741258,
                                        'rotation': -5874368292264628233,
                                        'virtual_nw_x_pixel': -792330582,
                                        'virtual_nw_y_pixel': -1221170149,
                                        'virtual_width': 1167398608,
                                        'virtual_height': -578365174,
                                    },
                        ],
                },
                {
                    'description': 'ưȭћоƁĭ\x7fϏɺȠДɶЩžÏнÆщƇѯěЙʜŧ7ʬӍϤAυ',
                    'monitors': [
                            {
                                        'identifier': -353810,
                                        'width': 3192975822595436221,
                                        'height': -2674730817451193134,
                                    },
                            {
                                        'identifier': 220443,
                                        'width': -1259904496466128106,
                                        'height': 7602605443730236456,
                                    },
                            {
                                        'identifier': 495057,
                                        'width': 1042759201058582109,
                                        'height': -8340596265788115952,
                                    },
                            {
                                        'identifier': 4947803,
                                        'width': 4793825286899102006,
                                        'height': 5779175306018358776,
                                    },
                            {
                                        'identifier': 3695707,
                                        'width': -7850087520278293065,
                                        'height': 5760845875612528763,
                                    },
                            {
                                        'identifier': 1821907,
                                        'width': -6067845690154364659,
                                        'height': 8141494059802955916,
                                    },
                            {
                                        'identifier': 1525466,
                                        'width': -5509618948837827201,
                                        'height': -1621781116308135276,
                                    },
                            {
                                        'identifier': 3106866,
                                        'width': 654927567130211835,
                                        'height': -3110520242014704434,
                                    },
                            {
                                        'identifier': 2028059,
                                        'width': -1007430267121446542,
                                        'height': 1422137712546185371,
                                    },
                            {
                                        'identifier': 405598,
                                        'width': -6338966340599528504,
                                        'height': 7900924528178768835,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2502933,
                                        'source_nw_x_pixel': -9135259319599029090,
                                        'source_nw_y_pixel': -6083929279177022367,
                                        'source_pixel_width': -8267012651018518303,
                                        'source_pixel_height': -8558587464346377992,
                                        'rotation': -5519164374013670890,
                                        'virtual_nw_x_pixel': -486487551,
                                        'virtual_nw_y_pixel': -337140666,
                                        'virtual_width': -934680212,
                                        'virtual_height': -1317198688,
                                    },
                            {
                                        'source_monitor': 4343757,
                                        'source_nw_x_pixel': -446423423814889105,
                                        'source_nw_y_pixel': -222120183438774825,
                                        'source_pixel_width': -7936535477993355141,
                                        'source_pixel_height': -5763937233663940793,
                                        'rotation': -4926324250260300737,
                                        'virtual_nw_x_pixel': -772567837,
                                        'virtual_nw_y_pixel': -577809232,
                                        'virtual_width': -1260063763,
                                        'virtual_height': 1544559639,
                                    },
                            {
                                        'source_monitor': 8624115,
                                        'source_nw_x_pixel': -8233767995377886698,
                                        'source_nw_y_pixel': -1369104416335136048,
                                        'source_pixel_width': -1659815339848352772,
                                        'source_pixel_height': -5969497745258906040,
                                        'rotation': -2562809803718438166,
                                        'virtual_nw_x_pixel': -1868975323,
                                        'virtual_nw_y_pixel': -353644319,
                                        'virtual_width': -1788668015,
                                        'virtual_height': 385238446,
                                    },
                            {
                                        'source_monitor': 4650383,
                                        'source_nw_x_pixel': -7532720390157924562,
                                        'source_nw_y_pixel': -7482809356338993304,
                                        'source_pixel_width': -9216291019899566706,
                                        'source_pixel_height': -1626582907590721288,
                                        'rotation': -8006268656908282990,
                                        'virtual_nw_x_pixel': -648399450,
                                        'virtual_nw_y_pixel': -1745317062,
                                        'virtual_width': -802708672,
                                        'virtual_height': 804442854,
                                    },
                            {
                                        'source_monitor': 511256,
                                        'source_nw_x_pixel': -9188091980771662686,
                                        'source_nw_y_pixel': -2476832796595813159,
                                        'source_pixel_width': -6946235278374447600,
                                        'source_pixel_height': -2756935516330276220,
                                        'rotation': -5727669439242142284,
                                        'virtual_nw_x_pixel': 1935465761,
                                        'virtual_nw_y_pixel': 1859291691,
                                        'virtual_width': -784658246,
                                        'virtual_height': 1666280556,
                                    },
                            {
                                        'source_monitor': 1407032,
                                        'source_nw_x_pixel': -981227675015832855,
                                        'source_nw_y_pixel': -1699037124346310175,
                                        'source_pixel_width': -1686132322335901187,
                                        'source_pixel_height': -6717675251535351514,
                                        'rotation': -4039962283641324044,
                                        'virtual_nw_x_pixel': -355355691,
                                        'virtual_nw_y_pixel': 1160989637,
                                        'virtual_width': 1481692003,
                                        'virtual_height': 1498254301,
                                    },
                            {
                                        'source_monitor': 9854359,
                                        'source_nw_x_pixel': -4981672279565893063,
                                        'source_nw_y_pixel': -4864403075089282052,
                                        'source_pixel_width': -1993036582624328941,
                                        'source_pixel_height': -916202564456180410,
                                        'rotation': -8717564716347428320,
                                        'virtual_nw_x_pixel': -234713678,
                                        'virtual_nw_y_pixel': 1701407861,
                                        'virtual_width': 142885594,
                                        'virtual_height': 1854411461,
                                    },
                            {
                                        'source_monitor': 3936833,
                                        'source_nw_x_pixel': -3244271469639663801,
                                        'source_nw_y_pixel': -4402065934814428102,
                                        'source_pixel_width': -3472602407502350250,
                                        'source_pixel_height': -2444019980725541718,
                                        'rotation': -6716050930114584474,
                                        'virtual_nw_x_pixel': 91166292,
                                        'virtual_nw_y_pixel': -717897592,
                                        'virtual_width': 849856610,
                                        'virtual_height': 1902987827,
                                    },
                            {
                                        'source_monitor': 2937569,
                                        'source_nw_x_pixel': -2992053333210397164,
                                        'source_nw_y_pixel': -1465545416317625976,
                                        'source_pixel_width': -7386661648462635180,
                                        'source_pixel_height': -3147070571493102589,
                                        'rotation': -330598017554629992,
                                        'virtual_nw_x_pixel': -1434856529,
                                        'virtual_nw_y_pixel': 1161139238,
                                        'virtual_width': -1458599531,
                                        'virtual_height': -1094481059,
                                    },
                            {
                                        'source_monitor': 7772542,
                                        'source_nw_x_pixel': -3556572151267798622,
                                        'source_nw_y_pixel': -4307672226571233206,
                                        'source_pixel_width': -6584097246762033411,
                                        'source_pixel_height': -1726049404478478838,
                                        'rotation': -6888372718155104253,
                                        'virtual_nw_x_pixel': 811230929,
                                        'virtual_nw_y_pixel': -37147603,
                                        'virtual_width': 787920260,
                                        'virtual_height': 454817932,
                                    },
                        ],
                },
                {
                    'description': 'Ŗ˕ɫpˀыɩȉԦ˽ҠŽ£ҹʲ\x8eœҋΎϧѭӐƫďȝŴѮ\x93ҥʬ',
                    'monitors': [
                            {
                                        'identifier': 871141,
                                        'width': -2124222463548806059,
                                        'height': 571089081352764808,
                                    },
                            {
                                        'identifier': 8883380,
                                        'width': -3907760675831873439,
                                        'height': 5650039513896432560,
                                    },
                            {
                                        'identifier': 7935823,
                                        'width': -1761584314668998061,
                                        'height': 3636101235442889463,
                                    },
                            {
                                        'identifier': 3104680,
                                        'width': -8280258301994767783,
                                        'height': -5425929600743456920,
                                    },
                            {
                                        'identifier': -685366,
                                        'width': 2234324913175640195,
                                        'height': -631079027109780292,
                                    },
                            {
                                        'identifier': 4070622,
                                        'width': -5305651785052434706,
                                        'height': -6652581086190762579,
                                    },
                            {
                                        'identifier': 7797171,
                                        'width': -2213344330693430221,
                                        'height': -4120604534482601577,
                                    },
                            {
                                        'identifier': 7067935,
                                        'width': 287959046328841237,
                                        'height': -926255903916085718,
                                    },
                            {
                                        'identifier': 5653345,
                                        'width': 4693793104149038441,
                                        'height': 6165125569674064509,
                                    },
                            {
                                        'identifier': 8256223,
                                        'width': 8717238701067767226,
                                        'height': 6653660531868485389,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8297175,
                                        'source_nw_x_pixel': -2455213062023227089,
                                        'source_nw_y_pixel': -1464157747241696099,
                                        'source_pixel_width': -777388895080942692,
                                        'source_pixel_height': -5106300681602276433,
                                        'rotation': -4402282990270684723,
                                        'virtual_nw_x_pixel': 1445904846,
                                        'virtual_nw_y_pixel': 119702079,
                                        'virtual_width': -26339346,
                                        'virtual_height': -1432489234,
                                    },
                            {
                                        'source_monitor': 1482832,
                                        'source_nw_x_pixel': -923140241742872941,
                                        'source_nw_y_pixel': -3036208462846637975,
                                        'source_pixel_width': -8336275522898617755,
                                        'source_pixel_height': -913917933755609650,
                                        'rotation': -4242178905782651901,
                                        'virtual_nw_x_pixel': -1644826734,
                                        'virtual_nw_y_pixel': 1913246251,
                                        'virtual_width': 382783302,
                                        'virtual_height': 1997130114,
                                    },
                            {
                                        'source_monitor': 1432686,
                                        'source_nw_x_pixel': -7686774312431252913,
                                        'source_nw_y_pixel': -4067853287592765573,
                                        'source_pixel_width': -2402168661967196664,
                                        'source_pixel_height': -4933617963438738368,
                                        'rotation': -3034368345492914904,
                                        'virtual_nw_x_pixel': 1956794031,
                                        'virtual_nw_y_pixel': 987158547,
                                        'virtual_width': -940996850,
                                        'virtual_height': 985607380,
                                    },
                            {
                                        'source_monitor': 868551,
                                        'source_nw_x_pixel': -307258166845298052,
                                        'source_nw_y_pixel': -4735416012200981354,
                                        'source_pixel_width': -1526315405180186786,
                                        'source_pixel_height': -6899161456024018653,
                                        'rotation': -1629733533836278179,
                                        'virtual_nw_x_pixel': -657010254,
                                        'virtual_nw_y_pixel': 1801229974,
                                        'virtual_width': 717918123,
                                        'virtual_height': -1521855460,
                                    },
                            {
                                        'source_monitor': 4348457,
                                        'source_nw_x_pixel': -7008316287966844097,
                                        'source_nw_y_pixel': -1131847989459726849,
                                        'source_pixel_width': -5194030415438233973,
                                        'source_pixel_height': -4845743544465442977,
                                        'rotation': -5964860284095998105,
                                        'virtual_nw_x_pixel': -1505721463,
                                        'virtual_nw_y_pixel': 1561345528,
                                        'virtual_width': -545500223,
                                        'virtual_height': 202815857,
                                    },
                            {
                                        'source_monitor': 725569,
                                        'source_nw_x_pixel': -4035002249374920924,
                                        'source_nw_y_pixel': -5809046639849206565,
                                        'source_pixel_width': -6222248901804404674,
                                        'source_pixel_height': -2987226500720665577,
                                        'rotation': -4274401282383382255,
                                        'virtual_nw_x_pixel': -84147691,
                                        'virtual_nw_y_pixel': 1372694141,
                                        'virtual_width': -990905964,
                                        'virtual_height': -33545062,
                                    },
                            {
                                        'source_monitor': 7115249,
                                        'source_nw_x_pixel': -5284691985292283353,
                                        'source_nw_y_pixel': -8113050756935051693,
                                        'source_pixel_width': -7275382339383992679,
                                        'source_pixel_height': -5206672674554850203,
                                        'rotation': -7122984302380476346,
                                        'virtual_nw_x_pixel': -1755094619,
                                        'virtual_nw_y_pixel': -856951627,
                                        'virtual_width': 1941681050,
                                        'virtual_height': 249206961,
                                    },
                            {
                                        'source_monitor': 3865796,
                                        'source_nw_x_pixel': -178796333370576121,
                                        'source_nw_y_pixel': -2886854193685626052,
                                        'source_pixel_width': -6076518417339342191,
                                        'source_pixel_height': -5165061400713551168,
                                        'rotation': -803835276162503028,
                                        'virtual_nw_x_pixel': -272280701,
                                        'virtual_nw_y_pixel': 785105542,
                                        'virtual_width': -1914163518,
                                        'virtual_height': -1423334979,
                                    },
                            {
                                        'source_monitor': 2250041,
                                        'source_nw_x_pixel': -2128528980754648136,
                                        'source_nw_y_pixel': -8111127883915037408,
                                        'source_pixel_width': -2002882021036518559,
                                        'source_pixel_height': -2827832247387999338,
                                        'rotation': -622077562218246518,
                                        'virtual_nw_x_pixel': 113403920,
                                        'virtual_nw_y_pixel': 289776952,
                                        'virtual_width': 560987499,
                                        'virtual_height': 1276203191,
                                    },
                            {
                                        'source_monitor': 4528777,
                                        'source_nw_x_pixel': -3290811498629708349,
                                        'source_nw_y_pixel': -2422972161205849245,
                                        'source_pixel_width': -25150791744130294,
                                        'source_pixel_height': -6805083603312266710,
                                        'rotation': -2041837529945875704,
                                        'virtual_nw_x_pixel': -1723491976,
                                        'virtual_nw_y_pixel': 1605389775,
                                        'virtual_width': 1811196153,
                                        'virtual_height': 467674347,
                                    },
                        ],
                },
                {
                    'description': 'ʂxΟӝǈõʿȂ˙˻ЎF3ЩűȓіӶ˦(ŕ´kҴҚьŬǰƪǏ',
                    'monitors': [
                            {
                                        'identifier': 465934,
                                        'width': 2195510878537953602,
                                        'height': 4630977745976548620,
                                    },
                            {
                                        'identifier': 6870589,
                                        'width': -3119726613426788687,
                                        'height': 3795702621484057253,
                                    },
                            {
                                        'identifier': 7297069,
                                        'width': 5025261737347330058,
                                        'height': -3544450216635301136,
                                    },
                            {
                                        'identifier': 6717023,
                                        'width': -5816077917289450197,
                                        'height': 3485910619697751996,
                                    },
                            {
                                        'identifier': 8581564,
                                        'width': -7234412596621673392,
                                        'height': 474720289731006101,
                                    },
                            {
                                        'identifier': 3797483,
                                        'width': 6962244192646711739,
                                        'height': 2939912574225351830,
                                    },
                            {
                                        'identifier': 8282167,
                                        'width': -1269906632780456440,
                                        'height': 61526281973724586,
                                    },
                            {
                                        'identifier': 8000607,
                                        'width': 8114039697472711051,
                                        'height': -5463289558595820299,
                                    },
                            {
                                        'identifier': -680545,
                                        'width': 4456743278972161177,
                                        'height': -8044468725606118217,
                                    },
                            {
                                        'identifier': 8192906,
                                        'width': 413239713081188065,
                                        'height': 5778274459594468887,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2508551,
                                        'source_nw_x_pixel': -483851764776076153,
                                        'source_nw_y_pixel': -8283679691832623131,
                                        'source_pixel_width': -4104596463809645041,
                                        'source_pixel_height': -6254847356697657090,
                                        'rotation': -31345760493011471,
                                        'virtual_nw_x_pixel': 1929968701,
                                        'virtual_nw_y_pixel': 1528176569,
                                        'virtual_width': -1203461287,
                                        'virtual_height': 847725224,
                                    },
                            {
                                        'source_monitor': 929668,
                                        'source_nw_x_pixel': -717417497207400316,
                                        'source_nw_y_pixel': -3706888889077445703,
                                        'source_pixel_width': -4594240617231338771,
                                        'source_pixel_height': -2554628907935981731,
                                        'rotation': -8253412522717810140,
                                        'virtual_nw_x_pixel': 1836543720,
                                        'virtual_nw_y_pixel': 38997131,
                                        'virtual_width': 1345151875,
                                        'virtual_height': 1187471152,
                                    },
                            {
                                        'source_monitor': 2378156,
                                        'source_nw_x_pixel': -8317572265580039658,
                                        'source_nw_y_pixel': -7051704634949998592,
                                        'source_pixel_width': -6148551783800816200,
                                        'source_pixel_height': -1570255225848675815,
                                        'rotation': -2246287885165950497,
                                        'virtual_nw_x_pixel': -1800160691,
                                        'virtual_nw_y_pixel': 1915321075,
                                        'virtual_width': -1601206231,
                                        'virtual_height': 1413590653,
                                    },
                            {
                                        'source_monitor': 542281,
                                        'source_nw_x_pixel': -1664324187761785949,
                                        'source_nw_y_pixel': -7120861617816328686,
                                        'source_pixel_width': -2050882623501572877,
                                        'source_pixel_height': -4469508535384190307,
                                        'rotation': -2723641742827146582,
                                        'virtual_nw_x_pixel': -1671398010,
                                        'virtual_nw_y_pixel': -1214236110,
                                        'virtual_width': 230727069,
                                        'virtual_height': -31314945,
                                    },
                            {
                                        'source_monitor': 8290476,
                                        'source_nw_x_pixel': -1612417954831699917,
                                        'source_nw_y_pixel': -6989356157250223546,
                                        'source_pixel_width': -9126763400323643712,
                                        'source_pixel_height': -7928716071850176991,
                                        'rotation': -8939825194355334037,
                                        'virtual_nw_x_pixel': 416823679,
                                        'virtual_nw_y_pixel': 1453454085,
                                        'virtual_width': 833771954,
                                        'virtual_height': 12202212,
                                    },
                            {
                                        'source_monitor': -217595,
                                        'source_nw_x_pixel': -3703983102660460105,
                                        'source_nw_y_pixel': -5897331027761374690,
                                        'source_pixel_width': -3615512217931691919,
                                        'source_pixel_height': -6376047813104700394,
                                        'rotation': -6217399607893944712,
                                        'virtual_nw_x_pixel': 184516659,
                                        'virtual_nw_y_pixel': -931143647,
                                        'virtual_width': -408529941,
                                        'virtual_height': 1684624508,
                                    },
                            {
                                        'source_monitor': 3911532,
                                        'source_nw_x_pixel': -2386123285699782936,
                                        'source_nw_y_pixel': -8516059374739796720,
                                        'source_pixel_width': -5768639268373309303,
                                        'source_pixel_height': -8696515096757460104,
                                        'rotation': -1422528553145062026,
                                        'virtual_nw_x_pixel': 1694555071,
                                        'virtual_nw_y_pixel': 1828456523,
                                        'virtual_width': 341678211,
                                        'virtual_height': 1794178968,
                                    },
                            {
                                        'source_monitor': 9001844,
                                        'source_nw_x_pixel': -7656911793156842661,
                                        'source_nw_y_pixel': -5145007299506562989,
                                        'source_pixel_width': -2583323355862911715,
                                        'source_pixel_height': -6526719709066567431,
                                        'rotation': -9068339787590131984,
                                        'virtual_nw_x_pixel': 166937498,
                                        'virtual_nw_y_pixel': -495767342,
                                        'virtual_width': -58187719,
                                        'virtual_height': -1936227851,
                                    },
                            {
                                        'source_monitor': 3440950,
                                        'source_nw_x_pixel': -2579000915156815740,
                                        'source_nw_y_pixel': -4018550489176589138,
                                        'source_pixel_width': -8819847811348284050,
                                        'source_pixel_height': -1792241353901448189,
                                        'rotation': -438815526315117675,
                                        'virtual_nw_x_pixel': 1297222072,
                                        'virtual_nw_y_pixel': 826209679,
                                        'virtual_width': -106979856,
                                        'virtual_height': -1705237553,
                                    },
                            {
                                        'source_monitor': 4360083,
                                        'source_nw_x_pixel': -6901908564230496164,
                                        'source_nw_y_pixel': -4141010000108300382,
                                        'source_pixel_width': -8391812654471222101,
                                        'source_pixel_height': -6543162726612753100,
                                        'rotation': -7688117475742384880,
                                        'virtual_nw_x_pixel': -1027432592,
                                        'virtual_nw_y_pixel': 1636353400,
                                        'virtual_width': 207782477,
                                        'virtual_height': 760170140,
                                    },
                        ],
                },
                {
                    'description': 'ϮƜýϖjķηȮŃƉš¯\u038bƖȥˌʤͰŌˎȊɒɕɖũҖҋěɘ҈',
                    'monitors': [
                            {
                                        'identifier': 5460685,
                                        'width': -4057577836552977504,
                                        'height': -7357288395847895309,
                                    },
                            {
                                        'identifier': 8517926,
                                        'width': 4257020585786291820,
                                        'height': -3070490729482084048,
                                    },
                            {
                                        'identifier': 6352141,
                                        'width': -6523127175980548481,
                                        'height': -1722516253189165316,
                                    },
                            {
                                        'identifier': 1286774,
                                        'width': -9098311760265481094,
                                        'height': -7026734071984801571,
                                    },
                            {
                                        'identifier': 8714839,
                                        'width': -2143965282871864520,
                                        'height': -7477247256785042034,
                                    },
                            {
                                        'identifier': -977079,
                                        'width': 1938873634087816128,
                                        'height': -7216792193992088642,
                                    },
                            {
                                        'identifier': 7977967,
                                        'width': -3648042952952984687,
                                        'height': 6233838767728443489,
                                    },
                            {
                                        'identifier': 8789803,
                                        'width': 3598138196236424052,
                                        'height': 4207085281952792519,
                                    },
                            {
                                        'identifier': 1893915,
                                        'width': 7200286317169423985,
                                        'height': 2756907234651498059,
                                    },
                            {
                                        'identifier': 1903627,
                                        'width': -5859807253260477707,
                                        'height': 3523303924556871378,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2073681,
                                        'source_nw_x_pixel': -1337409021210790179,
                                        'source_nw_y_pixel': -1562248625746789614,
                                        'source_pixel_width': -5234112574527297051,
                                        'source_pixel_height': -3628150492487831398,
                                        'rotation': -4275968849044222504,
                                        'virtual_nw_x_pixel': 1745530860,
                                        'virtual_nw_y_pixel': -1574607929,
                                        'virtual_width': 1537518881,
                                        'virtual_height': 1346989571,
                                    },
                            {
                                        'source_monitor': 5212319,
                                        'source_nw_x_pixel': -7836748254158904977,
                                        'source_nw_y_pixel': -1685485011911407899,
                                        'source_pixel_width': -1682284490746053950,
                                        'source_pixel_height': -7787182444590818673,
                                        'rotation': -3308191824110753849,
                                        'virtual_nw_x_pixel': -1433349845,
                                        'virtual_nw_y_pixel': -408097439,
                                        'virtual_width': 156514506,
                                        'virtual_height': -1930290146,
                                    },
                            {
                                        'source_monitor': 4061823,
                                        'source_nw_x_pixel': -2588710131867112120,
                                        'source_nw_y_pixel': -105612447002932323,
                                        'source_pixel_width': -4685369939659922660,
                                        'source_pixel_height': -92530694005854834,
                                        'rotation': -2434116261123293190,
                                        'virtual_nw_x_pixel': -1634701410,
                                        'virtual_nw_y_pixel': -1065255735,
                                        'virtual_width': -1776715126,
                                        'virtual_height': 1278936565,
                                    },
                            {
                                        'source_monitor': 2766544,
                                        'source_nw_x_pixel': -5867758984935505818,
                                        'source_nw_y_pixel': -2555266458202652758,
                                        'source_pixel_width': -6309328637881640948,
                                        'source_pixel_height': -2487437409867664925,
                                        'rotation': -1762570982753613470,
                                        'virtual_nw_x_pixel': -1501637704,
                                        'virtual_nw_y_pixel': 301632837,
                                        'virtual_width': -1897325102,
                                        'virtual_height': -715626710,
                                    },
                            {
                                        'source_monitor': -443542,
                                        'source_nw_x_pixel': -2441395247055876640,
                                        'source_nw_y_pixel': -5736952255677553916,
                                        'source_pixel_width': -1445971059157140785,
                                        'source_pixel_height': -4902271936913639258,
                                        'rotation': -4115381940046063274,
                                        'virtual_nw_x_pixel': -465352771,
                                        'virtual_nw_y_pixel': -1243002967,
                                        'virtual_width': -1152718551,
                                        'virtual_height': 464753176,
                                    },
                            {
                                        'source_monitor': 4431406,
                                        'source_nw_x_pixel': -3471046041826640577,
                                        'source_nw_y_pixel': -6147346767695283548,
                                        'source_pixel_width': -2434557009491716216,
                                        'source_pixel_height': -5570649146462060273,
                                        'rotation': -1477243835982121155,
                                        'virtual_nw_x_pixel': -851519226,
                                        'virtual_nw_y_pixel': -1043078543,
                                        'virtual_width': -587357759,
                                        'virtual_height': -1616619399,
                                    },
                            {
                                        'source_monitor': 3284177,
                                        'source_nw_x_pixel': -5155786092463913416,
                                        'source_nw_y_pixel': -8591829687406898345,
                                        'source_pixel_width': -4935458408295416423,
                                        'source_pixel_height': -7209692818668805908,
                                        'rotation': -4892297445623824983,
                                        'virtual_nw_x_pixel': 190983716,
                                        'virtual_nw_y_pixel': -1216154837,
                                        'virtual_width': -1372096995,
                                        'virtual_height': 1677869088,
                                    },
                            {
                                        'source_monitor': -163860,
                                        'source_nw_x_pixel': -1871090094429406173,
                                        'source_nw_y_pixel': -5121046062162804969,
                                        'source_pixel_width': -5110662690129074199,
                                        'source_pixel_height': -1076967960874192384,
                                        'rotation': -1951074101559495307,
                                        'virtual_nw_x_pixel': -1553123709,
                                        'virtual_nw_y_pixel': 1161729919,
                                        'virtual_width': 197114496,
                                        'virtual_height': -1415554415,
                                    },
                            {
                                        'source_monitor': 624457,
                                        'source_nw_x_pixel': -8474281770019363850,
                                        'source_nw_y_pixel': -4403506176449337459,
                                        'source_pixel_width': -8606584650287357759,
                                        'source_pixel_height': -6612642205597918508,
                                        'rotation': -253120704371739680,
                                        'virtual_nw_x_pixel': 689404282,
                                        'virtual_nw_y_pixel': -29943794,
                                        'virtual_width': -1611859057,
                                        'virtual_height': 1415671840,
                                    },
                            {
                                        'source_monitor': -670567,
                                        'source_nw_x_pixel': -190630546155019331,
                                        'source_nw_y_pixel': -4061447274803602883,
                                        'source_pixel_width': -2992243197579597055,
                                        'source_pixel_height': -2815014508322441130,
                                        'rotation': -8011388460795182974,
                                        'virtual_nw_x_pixel': 1385249247,
                                        'virtual_nw_y_pixel': -1209414043,
                                        'virtual_width': 62824388,
                                        'virtual_height': -1320463601,
                                    },
                        ],
                },
                {
                    'description': 'ɼÏÏ&Ȩϯ˚ԍƽΓǞǉǭʙȝǭ·Ӗf;;ƩʢфʯÏEԒɌΰ',
                    'monitors': [
                            {
                                        'identifier': 8843409,
                                        'width': -6532994816872162459,
                                        'height': -7315984410224709390,
                                    },
                            {
                                        'identifier': 4096837,
                                        'width': 3945113279243031065,
                                        'height': 3865427586951498206,
                                    },
                            {
                                        'identifier': 2164873,
                                        'width': 3886864141449058326,
                                        'height': -3186997504614213502,
                                    },
                            {
                                        'identifier': 9929367,
                                        'width': -4523176409362177065,
                                        'height': -2994629612380947412,
                                    },
                            {
                                        'identifier': 3022461,
                                        'width': 2740589027431465217,
                                        'height': 912229063875400497,
                                    },
                            {
                                        'identifier': 3885612,
                                        'width': -8989482778504093353,
                                        'height': 5570304529677891304,
                                    },
                            {
                                        'identifier': -683327,
                                        'width': 1925756284714456764,
                                        'height': 1095832641668317207,
                                    },
                            {
                                        'identifier': 6076891,
                                        'width': -3181780853171451756,
                                        'height': 7141750447785826077,
                                    },
                            {
                                        'identifier': 7308938,
                                        'width': 281516546402946402,
                                        'height': -8243109382485455695,
                                    },
                            {
                                        'identifier': -642300,
                                        'width': -576970860216285234,
                                        'height': -7115186523276417607,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9122352,
                                        'source_nw_x_pixel': -5037948302732183510,
                                        'source_nw_y_pixel': -567799723000524755,
                                        'source_pixel_width': -5347228152122764644,
                                        'source_pixel_height': -7178865187891520745,
                                        'rotation': -2638204183336135903,
                                        'virtual_nw_x_pixel': 1041258162,
                                        'virtual_nw_y_pixel': 1413337979,
                                        'virtual_width': 1882854176,
                                        'virtual_height': 14710805,
                                    },
                            {
                                        'source_monitor': 9594854,
                                        'source_nw_x_pixel': -7432505848443251433,
                                        'source_nw_y_pixel': -1583578325068838099,
                                        'source_pixel_width': -5770446177323908717,
                                        'source_pixel_height': -5038700669622503098,
                                        'rotation': -3224538564849802945,
                                        'virtual_nw_x_pixel': -1566534509,
                                        'virtual_nw_y_pixel': -1068131302,
                                        'virtual_width': 1364227627,
                                        'virtual_height': -279201871,
                                    },
                            {
                                        'source_monitor': 974714,
                                        'source_nw_x_pixel': -4648593778014212571,
                                        'source_nw_y_pixel': -5720577635802485773,
                                        'source_pixel_width': -7652168095153564148,
                                        'source_pixel_height': -6220007870707845217,
                                        'rotation': -6088731677256356554,
                                        'virtual_nw_x_pixel': -1076930096,
                                        'virtual_nw_y_pixel': 414194525,
                                        'virtual_width': -634832371,
                                        'virtual_height': -1667090374,
                                    },
                            {
                                        'source_monitor': 7413925,
                                        'source_nw_x_pixel': -7713352421400921373,
                                        'source_nw_y_pixel': -3271597059718034401,
                                        'source_pixel_width': -6743597951813980457,
                                        'source_pixel_height': -5140588325454470684,
                                        'rotation': -539377371826270086,
                                        'virtual_nw_x_pixel': 1400243447,
                                        'virtual_nw_y_pixel': -1902546552,
                                        'virtual_width': -115974421,
                                        'virtual_height': -1063778657,
                                    },
                            {
                                        'source_monitor': 8902945,
                                        'source_nw_x_pixel': -1546662660494563614,
                                        'source_nw_y_pixel': -7296602048541409415,
                                        'source_pixel_width': -7142627096604271671,
                                        'source_pixel_height': -8807198362103387887,
                                        'rotation': -7518951697969336436,
                                        'virtual_nw_x_pixel': 1659833656,
                                        'virtual_nw_y_pixel': -297580742,
                                        'virtual_width': -109322172,
                                        'virtual_height': 1831503573,
                                    },
                            {
                                        'source_monitor': -222634,
                                        'source_nw_x_pixel': -1135955525452407515,
                                        'source_nw_y_pixel': -8936388531621983770,
                                        'source_pixel_width': -681095308602745975,
                                        'source_pixel_height': -4849480587681820869,
                                        'rotation': -3674260863134189120,
                                        'virtual_nw_x_pixel': -928276321,
                                        'virtual_nw_y_pixel': -536439993,
                                        'virtual_width': -102282546,
                                        'virtual_height': -798464491,
                                    },
                            {
                                        'source_monitor': 5216095,
                                        'source_nw_x_pixel': -9024740085668528107,
                                        'source_nw_y_pixel': -5589178613441119166,
                                        'source_pixel_width': -4185960790654863192,
                                        'source_pixel_height': -131007947113462041,
                                        'rotation': -4409287631693240125,
                                        'virtual_nw_x_pixel': 143232902,
                                        'virtual_nw_y_pixel': 1407848743,
                                        'virtual_width': -533572758,
                                        'virtual_height': 137700563,
                                    },
                            {
                                        'source_monitor': 5134372,
                                        'source_nw_x_pixel': -2380615135988954790,
                                        'source_nw_y_pixel': -7166490432843154927,
                                        'source_pixel_width': -7972804764385602837,
                                        'source_pixel_height': -3842975847282884491,
                                        'rotation': -4152119199150517985,
                                        'virtual_nw_x_pixel': -1410649944,
                                        'virtual_nw_y_pixel': 469399231,
                                        'virtual_width': 1216560139,
                                        'virtual_height': 704126182,
                                    },
                            {
                                        'source_monitor': 1915717,
                                        'source_nw_x_pixel': -6634860788755664385,
                                        'source_nw_y_pixel': -8511769482662615264,
                                        'source_pixel_width': -9009233571444818862,
                                        'source_pixel_height': -1599359086027872410,
                                        'rotation': -2793819465664028981,
                                        'virtual_nw_x_pixel': 1842000225,
                                        'virtual_nw_y_pixel': -1209224388,
                                        'virtual_width': -1996493542,
                                        'virtual_height': 1557906932,
                                    },
                            {
                                        'source_monitor': 3404801,
                                        'source_nw_x_pixel': -393798859332571984,
                                        'source_nw_y_pixel': -1321727125526643586,
                                        'source_pixel_width': -1110114829244293508,
                                        'source_pixel_height': -2190110823316216452,
                                        'rotation': -3762231469629123830,
                                        'virtual_nw_x_pixel': -1833754086,
                                        'virtual_nw_y_pixel': -15107692,
                                        'virtual_width': 1116237087,
                                        'virtual_height': -1958620781,
                                    },
                        ],
                },
                {
                    'description': 'ѳĕоʣгзˣӭ˵\x8cϴӧ\x96ұ϶ʈԋ\x97ǭóҭіҪ˜˽ǩǭƲɢЋ',
                    'monitors': [
                            {
                                        'identifier': 2552688,
                                        'width': 9010191207915269524,
                                        'height': -6848455594592115680,
                                    },
                            {
                                        'identifier': 4183069,
                                        'width': 4737188157577125859,
                                        'height': -1625015170179736320,
                                    },
                            {
                                        'identifier': -862973,
                                        'width': 5900549299991110148,
                                        'height': 2607988709131926207,
                                    },
                            {
                                        'identifier': 3898180,
                                        'width': 2180126705148988492,
                                        'height': -2531199439341147627,
                                    },
                            {
                                        'identifier': 7653544,
                                        'width': 8513285722239178787,
                                        'height': 7308104910579833821,
                                    },
                            {
                                        'identifier': 1744872,
                                        'width': 7857548125584529848,
                                        'height': -6097587494381713182,
                                    },
                            {
                                        'identifier': 8704613,
                                        'width': 4085283270228503650,
                                        'height': -2997477441860625599,
                                    },
                            {
                                        'identifier': 7236702,
                                        'width': -5898914986313537078,
                                        'height': -6303624061183628686,
                                    },
                            {
                                        'identifier': 1120354,
                                        'width': 4032080864206975333,
                                        'height': 7862959171503069164,
                                    },
                            {
                                        'identifier': 6089685,
                                        'width': 2996648698333206121,
                                        'height': -9148820670885386733,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9159625,
                                        'source_nw_x_pixel': -20527464430503930,
                                        'source_nw_y_pixel': -1350707164014932865,
                                        'source_pixel_width': -5893778327640218515,
                                        'source_pixel_height': -8121370351004424535,
                                        'rotation': -7958752713025774081,
                                        'virtual_nw_x_pixel': 621322915,
                                        'virtual_nw_y_pixel': -1033403580,
                                        'virtual_width': 1538652391,
                                        'virtual_height': 1677781097,
                                    },
                            {
                                        'source_monitor': 9528011,
                                        'source_nw_x_pixel': -3002767220742577577,
                                        'source_nw_y_pixel': -1869572753223100853,
                                        'source_pixel_width': -365431834110735369,
                                        'source_pixel_height': -8348939495808665749,
                                        'rotation': -1189873108326679601,
                                        'virtual_nw_x_pixel': -1347997858,
                                        'virtual_nw_y_pixel': -1285398829,
                                        'virtual_width': -195305835,
                                        'virtual_height': -911341721,
                                    },
                            {
                                        'source_monitor': 1545470,
                                        'source_nw_x_pixel': -637234191416590949,
                                        'source_nw_y_pixel': -7160540648610342022,
                                        'source_pixel_width': -3269570775210426720,
                                        'source_pixel_height': -8093758288792054574,
                                        'rotation': -944265407518245086,
                                        'virtual_nw_x_pixel': 1260803051,
                                        'virtual_nw_y_pixel': -1160341591,
                                        'virtual_width': 1192491612,
                                        'virtual_height': -1747936433,
                                    },
                            {
                                        'source_monitor': 3473069,
                                        'source_nw_x_pixel': -2607899052321930430,
                                        'source_nw_y_pixel': -8381527698386833894,
                                        'source_pixel_width': -2682733824966648848,
                                        'source_pixel_height': -5073647469475486599,
                                        'rotation': -7254969230326649517,
                                        'virtual_nw_x_pixel': -1876600593,
                                        'virtual_nw_y_pixel': 980623010,
                                        'virtual_width': 1931616372,
                                        'virtual_height': 1284653487,
                                    },
                            {
                                        'source_monitor': 8134901,
                                        'source_nw_x_pixel': -4800486686227255792,
                                        'source_nw_y_pixel': -3594698764904243677,
                                        'source_pixel_width': -4343131858713041750,
                                        'source_pixel_height': -7759905747777357129,
                                        'rotation': -5249990058383106138,
                                        'virtual_nw_x_pixel': -240769008,
                                        'virtual_nw_y_pixel': 1940748300,
                                        'virtual_width': -1789773434,
                                        'virtual_height': -1598718723,
                                    },
                            {
                                        'source_monitor': 1540984,
                                        'source_nw_x_pixel': -6830540730949780230,
                                        'source_nw_y_pixel': -2646979485737331775,
                                        'source_pixel_width': -3472901807537237605,
                                        'source_pixel_height': -583512677896378171,
                                        'rotation': -8769203241052707155,
                                        'virtual_nw_x_pixel': -1794900618,
                                        'virtual_nw_y_pixel': 676559373,
                                        'virtual_width': -881404072,
                                        'virtual_height': -1436579067,
                                    },
                            {
                                        'source_monitor': 2967230,
                                        'source_nw_x_pixel': -2681370593986717814,
                                        'source_nw_y_pixel': -6167174037293269403,
                                        'source_pixel_width': -5656057056749463401,
                                        'source_pixel_height': -6008123472102001205,
                                        'rotation': -8126155990904427527,
                                        'virtual_nw_x_pixel': 1614574421,
                                        'virtual_nw_y_pixel': -1972661012,
                                        'virtual_width': -723907192,
                                        'virtual_height': 276100636,
                                    },
                            {
                                        'source_monitor': 2651072,
                                        'source_nw_x_pixel': -3262259073939120159,
                                        'source_nw_y_pixel': -3430942752384261829,
                                        'source_pixel_width': -6079187494582614083,
                                        'source_pixel_height': -9191428882091267783,
                                        'rotation': -6711162737491572611,
                                        'virtual_nw_x_pixel': 339558182,
                                        'virtual_nw_y_pixel': -1603304296,
                                        'virtual_width': -1126331762,
                                        'virtual_height': -1567712155,
                                    },
                            {
                                        'source_monitor': 1738457,
                                        'source_nw_x_pixel': -6888170084552672571,
                                        'source_nw_y_pixel': -2020042872008557387,
                                        'source_pixel_width': -1297314140531962746,
                                        'source_pixel_height': -4617804169383834903,
                                        'rotation': -1758871661906286212,
                                        'virtual_nw_x_pixel': 1540222060,
                                        'virtual_nw_y_pixel': 1563209046,
                                        'virtual_width': 340598090,
                                        'virtual_height': -1236868162,
                                    },
                            {
                                        'source_monitor': -428827,
                                        'source_nw_x_pixel': -3467633877487561941,
                                        'source_nw_y_pixel': -4878883442637683500,
                                        'source_pixel_width': -2687820713870521775,
                                        'source_pixel_height': -7323464081085677943,
                                        'rotation': -2495694357840730442,
                                        'virtual_nw_x_pixel': 618161886,
                                        'virtual_nw_y_pixel': 1549378238,
                                        'virtual_width': 851038749,
                                        'virtual_height': -868583708,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 5526729,

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
            'request_id': 5741588,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 741282,

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
            '$': 'ʆɁΪʄMĈ˼Ԟϯªĥ$rϧQĸ΄ԓrǉȉͻԟвσˑ¬Ӫгˎ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3967466188352052847,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 412820.5719215249,
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
            '$': '20220526:211851.261244:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ǒЄʦҏiҎǅă˟ƽȶΫӄѺÁФΡʭéÁ-ǵλτ\u0382˃϶ӂʀϖ',
                'âҞōɳһΧǁп\x95ƀʜρ\x87ēҎǇ˘ԏ\x89ȕќыЌƔϜ4ӡЈӴә',
                'ƸхϹȎыó\u038dɔƘżǦƱ¾ʫȼɺ¦˪/²,OһЎҢӅŧъʼǀ',
                'йʍуҖϼŃЀϋԤmȡʊǑ\x8fʕѨƴåÐʑ\x98ӦхΟ˂ĀϤԏӆƕ',
                'Ȭ˸ŝƽαӺģŇʩӕѡR\x89Ɲʗ@ԊӕǖИҠŧnӽԄƆĖͶД4',
                'νƶӺƣJȵɍӌη҄ҞӇϐσñƄðƖҤҿĦ\x9bõĜѯÑӖ\u03a2N\x8b',
                'áʓϴƿϰԀ˹ғ²ƋҖƘϋ}ЧżĪĮҬȔΜɤ҃ͶӰôɫ˓l˃',
                'ρȮ˥Ʀ\u0378ƨǎ\\\\ǌӻѾÅJ\x8aЊ\x96\x83\x8fş˕˳ιʓƓƧƝȘԥΚ',
                'ǦÉɋѾɎԣ˫ҚаĆȿӼʡһʨ^΄Ė²îħʓéԑχόĜĿµĭ',
                'ԀɃȚȬСʙта@XʳũʹѺ\x97ʗʒёǑǲХԥЧwšȫЌʃ\x84Җ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1250749480371849805,
                2901941161145397430,
                693460781022746672,
                8338856798079257662,
                2061163377477096874,
                3297722320000200809,
                -3903483894920343537,
                5365684592706833188,
                -8677076282669155566,
                5299126046459198391,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -34925.078215385474,
                445093.95955925225,
                856938.6126885433,
                -98071.96243479114,
                783039.8439273153,
                872175.8256684787,
                -68216.06198892771,
                200146.87082367,
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
                True,
                True,
                False,
                False,
                True,
                True,
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
            'name': 'ʶˢԧͱƾĐ',
            'value': {
                '^': 'datetime',
                '$': '20220526:211851.017628:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ν',

            'value': {
                '^': 'string_list',
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
            'catalog': 'Μĕчß1ˤąЬȘϓȜСɐ˔Ĳƫͽ«ƭԘ@ӖωǢϑFШɶΣљ',
            'message': 'ǖоEȐʆÙԃӔЫӓȼϦǬȜȟжЬʶ˱ʔӞȑȖφËλ˳ΔÎŪ',
            'arguments': [
                {
                    'name': 'ΰŹүϥԔWǦӴˏЯʤчҋˋɹөӯĎɁ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:211849.905521:+0000',
                        },
                },
                {
                    'name': 'ʯИ´Ѣɭ\x83ќж',
                    'value': {
                            '^': 'float',
                            '$': 655184.2226872282,
                        },
                },
                {
                    'name': '˄ŠĬ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20220526:211850.061706:+0000',
                                        '20220526:211850.078250:+0000',
                                        '20220526:211850.099005:+0000',
                                        '20220526:211850.115871:+0000',
                                        '20220526:211850.132964:+0000',
                                        '20220526:211850.154660:+0000',
                                        '20220526:211850.171366:+0000',
                                        '20220526:211850.187851:+0000',
                                        '20220526:211850.206813:+0000',
                                        '20220526:211850.224448:+0000',
                                    ],
                        },
                },
                {
                    'name': '˹Nlɣ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220526:211850.306876:+0000',
                        },
                },
                {
                    'name': 'ϼϠцĢB·˙ΠʈʹрϘ;ɑ²,ϾÝҢ&ǉǣŦȯőЯΠҝKz',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        True,
                                        False,
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
                    'name': 'ŭЄҗώŏ\x83',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
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
                    'name': 'Ɵ#',
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

            'catalog': 'Ϩː',

            'message': 'ӥ',

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
            'identifier': "ԜǡűĉĈǝ;эӈдж'Ԩ\x82ϐӮǹØȶ$ӠȯƦШȌȊԖԖģÒ",
            'categories': [
                'access-restriction',
                'os',
                'file',
                'access-restriction',
                'network',
                'access-restriction',
                'file',
                'file',
                'os',
                'os',
            ],
            'source': ',ɱɹҝϸɪȥ˩ϫÙɤ҈ХĩƦԛʸƔ2Ͽʋ¥дsӴτ5ҙӉP',
            'messages': [
                {
                    'catalog': '\u0380ˀŋɉ\x80ËөҖʓ\x83ӬʒǉϞёз¯өļɁʉԠŹã^ϭаĝɛõ',
                    'message': '»ĬƍɖҐӌѮġȌwƿaϻЫȜѯͻĦǂʀґʳŽԡ;ʸǲǁƎҔ',
                    'arguments': [
                            {
                                        'name': 'ϲǨԝkȧ@ăҎ˅ДǌϣǋōĽѽFŊHǵȔʤ˥Ǘƙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '9ǙӌϳɱɶõpάŞӗ\x8cҩÌ¹ȮѓǴʵŎҒЫđǩԧԬƪʊƁҍ',
                                                    },
                                    },
                            {
                                        'name': '<ϱ˱˼ʿǱgyƨ¤nӢÝɉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            86364.47172214248,
                                                                            350432.7898868137,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƈ[ŝđũʉǸ×ϲȁǼ\x9fϹͼƂɠΪѹžƶ\x94ňBƳȋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 468610.9767986386,
                                                    },
                                    },
                            {
                                        'name': 'ăǥŧĬʿԓΎƹӑҰŌԙƉʒϊĉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211835.113576:+0000',
                                                                            '20220526:211835.130040:+0000',
                                                                            '20220526:211835.149293:+0000',
                                                                            '20220526:211835.166032:+0000',
                                                                            '20220526:211835.183759:+0000',
                                                                            '20220526:211835.200735:+0000',
                                                                            '20220526:211835.218576:+0000',
                                                                            '20220526:211835.234780:+0000',
                                                                            '20220526:211835.251410:+0000',
                                                                            '20220526:211835.268153:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŃƐҽҏ?ĶʏƑÜӷΓʆİǭǦϒƜ˪өȮɁëԡŅƬϾȃтɇԣ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ΧƪԡƇ[Îǖͺɻ¢ӎœΪжФͺΖʀŖ˪ѧ4¬',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ӺƩ˙',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҩĘőʖēε',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211835.899871:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȉђҲĵ¢Ѝҕ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211835.967664:+0000',
                                                                            '20220526:211835.984871:+0000',
                                                                            '20220526:211836.001848:+0000',
                                                                            '20220526:211836.018881:+0000',
                                                                            '20220526:211836.035908:+0000',
                                                                            '20220526:211836.052682:+0000',
                                                                            '20220526:211836.069838:+0000',
                                                                            '20220526:211836.086961:+0000',
                                                                            '20220526:211836.103936:+0000',
                                                                            '20220526:211836.120704:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԩɝÙƔɢԥŹ϶9ɡγīѹͽȆХ\x8fDů\u0381жϽ$ǯӅџ"˭Њǯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƹ\x98ȋΧԇɂ˝ԌŗʟȮӽϾŠɲŔԁAŅԢ˲ɢůʞѢĝԍӷ«ē',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ӝ&ЉɾËgǹƇɟңʌɳȋҎ\u0383øˉÉжΤƆзȴ@ǇŒɰӆƗӒ',
                    'message': 'ӃʻæӟʂŻѴϬԖΗ˹ҚÀoĉȌȭ\u03a2˅ϥϰÓө¶ėχŹß˻˂',
                    'arguments': [
                            {
                                        'name': 'ԅˉVѮ˾ЁȔЫϾɻ˩¤ӵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4187332116687239316,
                                                    },
                                    },
                            {
                                        'name': '{Ҷ˹н)\x9dǬ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211836.425959:+0000',
                                                                            '20220526:211836.443654:+0000',
                                                                            '20220526:211836.461081:+0000',
                                                                            '20220526:211836.479395:+0000',
                                                                            '20220526:211836.497223:+0000',
                                                                            '20220526:211836.518158:+0000',
                                                                            '20220526:211836.539920:+0000',
                                                                            '20220526:211836.560740:+0000',
                                                                            '20220526:211836.581506:+0000',
                                                                            '20220526:211836.602203:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Æ\u0382ÁҍȬѠϺǆƬҧäOɗɺȼƠ\u0378Ö¼ɒĆɾÒčʰǽίͳ\xadƢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ĊʔӚпŋǨԢєϷϷȈп\x9a·ïȂºȹʻƼÏlƇȦȨʗºӊĭ˸',
                                                                            'QӀJϯфђʐ˪˯Ş΄ъȎрƽĴǸѬŁӊҰѳKȹƼ<ԁϮȬò',
                                                                            'ϵѤƱȟӘӨφċҤѢɳ\x82БȘӇùǲљ҉˧ζS\x90ŊϾԢӋ˙¯3',
                                                                            'ųАσʩӻГмwcˀňѹу±ϯȲ˪ƞКȸ',
                                                                            '\u038bӅ\u038bÛĨȖāȚПļıҙʾTɼӉЃȳ\u038dƋс\x9cĵĄӶбįǟ˼°',
                                                                            'Ó)РʤєѢɩûƵфǧζԥˣѸΪǍǺìʺƧÆĢğӵϽϣќеҡ',
                                                                            'κϥӭϷŌϰĿʖΤ«ƋӎӏʦӽӀӍȣʪĐεɮ;ɤԌˌĞĖҟʉ',
                                                                            '¤úŠóѢƇΠѵӛŠˑϞɽȭɎϛѶҎзїȥхʄѹɺҳ8gĺό',
                                                                            'eǂӟҟХȰìг3ұЂɤɑϤWϵѷ\u03a2ȶӃϚʻZ˟ş˃ɰǻ˗Ԅ',
                                                                            'ǻɠɨѲЯԚǌɘƴϠɄҩαϡ\x9e·ΌǺΘĐˑ\x93·ԩĵ˶ϫʔɎe',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'α#ҸRƱҀыēǞǕΙΩԃęʾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211836.930054:+0000',
                                                                            '20220526:211836.946248:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɬȼӯЩǘѨCɞΎҕԁñîΠʛ#ĘӅĞѣӳ˨Ȋпγ©ǇȭѐϚ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211837.026279:+0000',
                                                    },
                                    },
                            {
                                        'name': 'fř҄ϛ˰ȭĞѡƙε\x9fѰřўûǁӗˆˊӦ΅<X-Йʶĺ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211837.096955:+0000',
                                                    },
                                    },
                            {
                                        'name': '˺ķɳƥҞєĬɕʓƲf\x88ɦǆʤ˵k(ʈϭɒΘłӹΤ¡˒δʟ\x81',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ӬŋЊ2ɳɋ·ӥ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            9061001864127210090,
                                                                            5209533325366445508,
                                                                            4040833180667997887,
                                                                            2786918180771456400,
                                                                            -3512060436463903227,
                                                                            4148272773930697196,
                                                                            5433869559021766975,
                                                                            -7858400879220490977,
                                                                            -1511597089639631422,
                                                                            -3420237433355417996,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƌƧЋГœϕĒćȝѵøԎӄȌӪ©Űρ˻уAĹԇjйлŹӄԣƮ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ѩ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -80946.25667921272,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɸƳӔйһϭ±ʃϢ\x7fўґɏťǕ÷øӳȄЩɤƬPVԏЃЭӵƂӆ',
                    'message': 'bǻԉӰGɜϴćƛφ±sǜԐɋɇðϾʑͻ\x83ҏɮ҈Пə¾ӌƼ\x9b',
                    'arguments': [
                            {
                                        'name': 'ʜȟòȓϽȽȇd˄юΨƥʆȇӖžԚɃńԩǠλџӞϲɕӟѩνY',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѲȜĄҡɖÑʷҖľиĩӍŠԉѝRņρñķ˼ӂҋ\x99ӎѪ΄ϋǮí',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211837.782731:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ςЄфʦћӝďΨʗºĘą',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'κɴƧƗͲҀüϻʡC¸Ӭƹьɽʋ\u0378ʽʊȠƗqȞҏɘ\x93ΐĄƮȢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 886567.5286764448,
                                                    },
                                    },
                            {
                                        'name': '\x99ǻÝҳĝŔƔǠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211838.036531:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϖƃʆƾaйyΏDƊy',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'σ¹ǹѹȌïӘĨԩ\x85ǁeǆѴŵσ˳ˍǭņӝώ\x93ҟ¡\u0382ӉĬϟɆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3023333073204180747,
                                                    },
                                    },
                            {
                                        'name': 'ΓԌȽã',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211838.451507:+0000',
                                                                            '20220526:211838.467612:+0000',
                                                                            '20220526:211838.485531:+0000',
                                                                            '20220526:211838.501425:+0000',
                                                                            '20220526:211838.519482:+0000',
                                                                            '20220526:211838.540360:+0000',
                                                                            '20220526:211838.560553:+0000',
                                                                            '20220526:211838.580510:+0000',
                                                                            '20220526:211838.603545:+0000',
                                                                            '20220526:211838.626893:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʗɐҪҦűĜӼŗȟčʃ\x81(˳6ºҕҦâǶԇϼŦI\x83Ѱ\u0378Їɟ^',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϥÄʖǧΌɋű',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ѽƐЂͿпŃЪ'ɩħԗĺˮʻȚӹ<Уȍњԑŭʕn˂ʵαԅғã",
                                                                            'ʛҀƄÀȝҰЖ[ӢÛ6ǝʥĭҨȰԐĲ\\!ˬ˳ĉωϕȁѶӃĮԇ',
                                                                            'ѨüȯҋѫȒȒλʹӭδȥДŇ\u0383ӛĥ҈˩ʗ\x9aόӡөҲƒҮŮҵѬ',
                                                                            '\x83cςìӏƹӌΐԐϱāƍΥȳˀщûìǹĞĐφ2ȋέʋҶθƅԂ',
                                                                            'ѡБμӘŇÒҦшЧĳɪЩǃѵǃʠŦͲЃ\x7fϟӃҸbҝӶǬΘǞώ',
                                                                            'ұŔǨƿЦӶǨ(ĀJȬÝȘЫqÔì΄Ƥ\x80ǜѡʛЬŏǌϥІ\x9cҷ',
                                                                            'ʾӣЫøʲǲǞɠˁØĠńәɞнmνˋϱҕөŵΨˈWǧѺҿɩÍ',
                                                                            'ѴӰɈԇ7ϩҀʁЗ++ˤлȯԐЫӾҒм˅ņɢR]ǾςȂϡEʅ',
                                                                            'жƒљůӘ$Ҏȷҟ¥ɏͻȗЬǾ,\x8f«ҤҰɔʌǭõ#ɓ˙щԍȱ',
                                                                            'ŝȄԤ¿ïҔɲƘӈɈ˧πȬВΐ{Е/ӤàθҸύ\x86ɶfţшȡè',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¿˴Цʒ<Γ³ΡâċѤϙȨɭŰӸŘʞӧϏŭˢЕұ¶%η\x8f½Ŏ',
                    'message': ';ҺSзƋſ~ı˝ÜƎνŕʛωŅцæҴŎԍ˱!ΟÎȳǋҐӇȣ',
                    'arguments': [
                            {
                                        'name': 'ɣɒȭĽϗЎȄЪ˝ƠĤιҎQ҆ӏӨÙϊċе<Ѯ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5884408947988867713,
                                                    },
                                    },
                            {
                                        'name': ']ԈãԃģɧǷɠ#ӖЊ¾˘ęԒӦԂТǓȿƃqѫҭĲҶεʻóЌ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '·Ӆ\xa0ɩjϏԨαȞ˙ϓ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            510622.2572903554,
                                                                            946599.1178439355,
                                                                            154337.25482369255,
                                                                            860721.9063430966,
                                                                            -16633.316736246066,
                                                                            661808.9889491465,
                                                                            535649.6166605134,
                                                                            50268.48787656429,
                                                                            272426.680124945,
                                                                            354299.2029887099,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x90ԠЎˎђ}ԖѭʛTӬâȧȼИфȺʏƖԣƙ±\x7fǛЋh˜dШŸ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0381ϣǏŠÞƪœǡԊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5514843102624069425,
                                                                            6503856616632659538,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȴȟЯɪťЀýÌÿ®ԛΞƞ9ԟĶɤʘҨ¥˩Ɲѿ\u0379ɗȑΚџ˩ȓ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2033848559818810492,
                                                    },
                                    },
                            {
                                        'name': 'ɦͰ˭ɉЪєʯǷуҴԇĿßɌ¹ȆԎӊķˊȤΖΏà\x96ɞӥϗԗ\x88',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƫӵьɼ˴ŪΫҙΚ´ӶѕʹǙԛΗҕəƵԡԊԦҚӖВԙħɎǄĳ',
                                                    },
                                    },
                            {
                                        'name': '҈¡ԬѺЫɏòʕы=ͶwÖӃŧӼɩɴΝ0сʠȪΎ\u038d',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ͼщ˭ѱʥŗÖȸɃǰ˦νίďôútϮÎϨчæʈÚѣȔȑʼҒ҅',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5591568404791752227,
                                                                            -3196301158626338049,
                                                                            -8493968768075895840,
                                                                            -554105412528373846,
                                                                            4335742011427413770,
                                                                            8480178576800720703,
                                                                            -3806213354559623531,
                                                                            6666588200374142119,
                                                                            -4389002425911554154,
                                                                            -7262610096227264005,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϿΣъп\\ͽƻxΞŔпęӓċŁǂˀΑɧǪҒ҉ϥϵǪҏɻԁơΩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŉΈ´Є˛ЌêѦɕӭżũǜ!Λȉȓҫȍɰ˄ΆǢÒȥʘǐңШϺ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '£ԝǫщϳ\x80ĭ±ρʵMǩѫ<ϫÉˤŰXҍȑԎӨюoɘѾӡvČ',
                    'message': 'ѯ\x92ӻӐЈЊҚ\x84ÉϮΕǶɷǚƴŨŋſиϟΣĝ?ĜȸȜɣÕԗү',
                    'arguments': [
                            {
                                        'name': 'ԂɐϟåσѶǂï\x9eϽҟǵ¢Λ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'İӺƕэԧЁϞѯv\x8bΌҮ\x87\x97ʙҖƪҎȌ.ώoȤӚˣʒбϣěɢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 274538.5591420337,
                                                    },
                                    },
                            {
                                        'name': '\x82ȹЭʹ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211841.128601:+0000',
                                                                            '20220526:211841.145538:+0000',
                                                                            '20220526:211841.162383:+0000',
                                                                            '20220526:211841.182506:+0000',
                                                                            '20220526:211841.201588:+0000',
                                                                            '20220526:211841.218055:+0000',
                                                                            '20220526:211841.234570:+0000',
                                                                            '20220526:211841.251491:+0000',
                                                                            '20220526:211841.268548:+0000',
                                                                            '20220526:211841.285380:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˵ɹΡ˹Ώԁĭ˚\x9eġÚұͼζǥѪǘħ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            259904.87957834883,
                                                                            361511.85360500054,
                                                                            776567.0647036248,
                                                                            902325.1441471498,
                                                                            -20188.999876959424,
                                                                            138495.64947258102,
                                                                            431231.54893123056,
                                                                            686443.0233613468,
                                                                            301886.6074167409,
                                                                            328335.6494136337,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҠĆϯҔʦҢŏȡəϜț\x9cǾď˄ОІ˪8´ʄĄӦ©ϳі4ʑӓƹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 778955.0887830766,
                                                    },
                                    },
                            {
                                        'name': 'ÛȳŧʞъӼˊĞϬÑԅǎʜ˙Ӓɯәúɰ˪ˮѝӉ˽ӗȟËӱǋƫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5234503334904951138,
                                                    },
                                    },
                            {
                                        'name': 'БƯжњђĩ\x97\x99ĹȝҋэƹϹήǴҢЋăɜȀϰé˃фΦZϨɾǜ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211841.748171:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȇʨ+\\ʽԖԁɍРƖȔȽÔÔДʘ˧ҥƭʒǯ҈óēԈǾѝͺԄ½',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӈ÷ӚĻȭƊҒȥѧWѯȻҨƚбɕȾċůïʃıԊɃǇҜŏҵɨý',
                                                                            'ɬʂơɮrȡɎ£ғȠlϺԐksǑϢƋ\x9eʢͽӊGɼɖЄȪœˣю',
                                                                            'ҘҒʋ˔ӨÌˎÿǑȡӬǘӃʥЌҲńԁМџÀùԣɍѕ҉ŁњȦɜ',
                                                                            '[бП\u03a2ӧԛǠ·ɥϞiǋɝɆÕȮϏөӤԂЌɻΗƠ˺ИΔ]É<',
                                                                            'ɯ\x90ΨΒ\u03a2ԎȟǹԂǍƃNϿò»ɿĬ\xa0ɲʗˡғÅȷʸ\x86ѧȊÛѣ',
                                                                            'тӳʍϭđ\u0380ӆɳ7ðӠʚĢМȚӻȾɼԌƭǢФЖêʌррĦЈɲ',
                                                                            'ӉĔԙ·ʂӂҮѦӊɮɰхɣŊmХƌȶҲĉ˓ɮȝɷ°ЛĉµÍ\x9c',
                                                                            'ƤПԣ¾Ѷϒӂӈ9ʓ˨ĝ$ϔǘʥϼѩEԉːԫőǵQ_ЍқNѾ',
                                                                            ')ʶǵøϑиɒӦԁÍȚԉăŜнϋϔȾьuɳӁˊǔûύЌɨԬҭ',
                                                                            'ȺbҲ˰¥=ҎíĆũԌʹԉɮîʣŭǻӥǁԍλԈϟδ\x9eˬG\x88%',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǇíǼƺԆġԂğѿĜΐɓ*ҟ%ӥʫ\u0378ӴɝԣƋθŃƥķŴ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x84Ȥǹ+ӽίѝɨ\x9e§\x7fȘҊ˒ЄYѰˠȎǴӏү҇ѵ)ʸŝPԟE',
                                                                            'ĠЮȭ7Ќĕ>ӛĉɔ\x9dƬˎȼˎʴԂˏ1Ø\x96ƳΦɨƟÀΖʈєǎ',
                                                                            'ƮӭǱò҄ſŞǣǨƔԔƳǹұũΛҫϫƴȻЖʌӹ˾ǊŅǳ҃кʗ',
                                                                            'ǌμΗәȸӠøχ(ΦϪϽ\x91Ǚ҂ҔҸǾǄƅТ˷ʄšľΕϽҙΘb',
                                                                            'χƑƁgҏͲΚ4ÓɱӮ˵ȗЯɪșϤ\x8elʵɑÖʸͽϒѐӶȳѰǃ',
                                                                            '¼=ӐǯΟRϐƂƒßGϗҎǱ/ҋǦˏǴnҾåįʉ΅ԁϖɅ§Ť',
                                                                            'ʛԔфɇǪ\x84Ĕîćįʁ\x89ʹǰƃʐψȊŽİǂέѰԤȒхǘϟ\x9f˓',
                                                                            'ӜԗϩԈʙΧʼϻϱѯǳҢęƋ˂ϫзŗϢ§ʡâӂxÎǶʀǍqԈ',
                                                                            'ȢԣҟȚɉñ)ԪɌĭк˸¡δҨʦǁԝˑȤԆŖ\x85\x94øҋǱ_ҟͷ',
                                                                            'ƨӞÿӭWώćȠǞӢˢӗɽʯŔӣӏɨѰȝɴИäЅǊΨ±ȯǊ\\',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Іә©ˉȒªѳǡԙψӼƽϙǳϩǣǪӴЛӶhШԩ҆ȂȽȫӨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211842.290159:+0000',
                                                                            '20220526:211842.306057:+0000',
                                                                            '20220526:211842.321866:+0000',
                                                                            '20220526:211842.339160:+0000',
                                                                            '20220526:211842.356455:+0000',
                                                                            '20220526:211842.372962:+0000',
                                                                            '20220526:211842.389581:+0000',
                                                                            '20220526:211842.406618:+0000',
                                                                            '20220526:211842.423116:+0000',
                                                                            '20220526:211842.439353:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'мÙǎёĜ҃Ї˂ɪԦўԩʫȏϴ\'ȞiƵ˪"ģMӧeԟɾǎ$ί',
                    'message': 'Ӑʉп\x8cǫΞųФгȥoŃͰɀåԣǞƅγԟԃɼƊɪǲʭк\x91ӝԝ',
                    'arguments': [
                            {
                                        'name': 'ȾПŨšԋӞϵʂϽώ°ґґԃHȘςѻZĔ®ŸǏ˴Āцɽσ2Ï',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 293962.1759662148,
                                                    },
                                    },
                            {
                                        'name': 'ȫ˴˔ο¶ӳϨǵϻĤ\x90ї®ϜӑͰ/ñǝϠÉěȎʦŋœ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΰŋ\x86ɣЯʴǠѩʘҗϒĸɁϰɹ˥˅Ҧǀʽԇ˗ǾjԭȜ˒ѳǙҁ',
                                                    },
                                    },
                            {
                                        'name': 'ԛѾÔΣʊӍķøϠҶɖϖўÞЋΛŁũƅҸȴĥӉɝǣʧρκɃŵ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            346284.32725557906,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '²ʏȭȄŜЍϡҊƊ\xadΓ\x94ҒƄϤϕѩ\xadҪɨʛūj҂õͼT-ʻԁ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2625541722308726976,
                                                    },
                                    },
                            {
                                        'name': 'ѸЃ˖',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211842.905837:+0000',
                                                                            '20220526:211842.921856:+0000',
                                                                            '20220526:211842.937717:+0000',
                                                                            '20220526:211842.959443:+0000',
                                                                            '20220526:211842.978997:+0000',
                                                                            '20220526:211842.995767:+0000',
                                                                            '20220526:211843.012789:+0000',
                                                                            '20220526:211843.029507:+0000',
                                                                            '20220526:211843.046695:+0000',
                                                                            '20220526:211843.063285:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'γӶ˳ԕƈÞԉįʸƎŭΙƳǟĵȞ\x85ΔȽΦӞŒȄȴĸȾį©ʄŅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211843.147292:+0000',
                                                    },
                                    },
                            {
                                        'name': 'щȦéΫϊĳĽbƖǤˋð\x8aӉҺӖ˝ʐЮ¯',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 84797.58324942322,
                                                    },
                                    },
                            {
                                        'name': 'Эőϐ[_ƲӪÞżƼˋɇ¸ԉƩȀψҊpбóЬ+\x96ÖɺҲқǂɅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÆΕŘŉƙΪʽę˲ҬɑàØƨԁǂќǽ҉ˬʹƴȥšѺʱÞГӌǇ',
                                                    },
                                    },
                            {
                                        'name': 'ɊŖjϤbƸhŉψЮҘ϶ίɂЎ˅ѴåƝǡ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ČƓϝҔҁϞЀʞĿǜĈâϡЛ҆Ϥϑ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -503156267045362033,
                                                                            -2043455271821344333,
                                                                            268699806697621396,
                                                                            3481931893110521077,
                                                                            -8404605656018302017,
                                                                            -7005261116305147022,
                                                                            5615747316191668488,
                                                                            2808439347079588042,
                                                                            -6026769343231419604,
                                                                            2980357714412815916,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҸʰǭÂ}ЉѝǕy¼ǚɥ#Ǐ҆±īӺ\\ɹ»ÈԘZ9Ēҝњŧ\u0382',
                    'message': 'Ҋϔ&ǶԆ\x92Ʀɾ΅ˏƀНƓÛǘŋƼ\u0381ǳҪͽȊȺƬ4öңз\x96/',
                    'arguments': [
                            {
                                        'name': 'ѷȞӆǅчώʤуŏɾЄȅ\x97ɮ£ιW',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            519416.1348297264,
                                                                            417399.8043402515,
                                                                            191236.1696340802,
                                                                            608825.1488019809,
                                                                            -56246.095572758335,
                                                                            301703.1479997427,
                                                                            465044.0607616288,
                                                                            -44035.69949371125,
                                                                            361080.5988680043,
                                                                            367291.92379009374,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '6ҙːɊʟǠŦʪԕŤӗѭÏȮϻɥʔϗÐԌöATԚүЦә',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211844.064643:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʼŹǦʵϱѣҤƥȇƓ)Ł\x88˛ԨƂѳLԙӐвѭϣԘSԤCFү҉',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211844.133133:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҘŘ.âǄϸқS5ΙʐԍĹ˳ɻ^ν',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8141070822862791708,
                                                    },
                                    },
                            {
                                        'name': 'Ɣ\x94ʰ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '҃РǢͱfҿ˲ѺȓÐӇ˽ɱҤŵɝΓΙ˛ĽȒĦǭЖ6WȢϻсȆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 326832.3998742281,
                                                    },
                                    },
                            {
                                        'name': 'bѤҭƵΚϻȬéīʖƾӵȸϗΫͲʩΗɟŃƂʡǣѝ5ӁӒ>ЬԘ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ňćʏ˧ʑԐŠ\x95ÑĪƷŴ1',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4153969440422173138,
                                                    },
                                    },
                            {
                                        'name': 'π\x98Ӓů¿öʧlǶ\x85ѩұĭȧλʜýҚ}ҫơ˨¾ǵϛӔTʹџğ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 874342.2214040682,
                                                    },
                                    },
                            {
                                        'name': 'ĬȓӕȮύȍ\x81',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԘķЅȐ΄YÛйǳУћşĘ',
                    'message': '˶ԅŨXȫťÞw˻Ŕ˄ʪҹɉ\x92ƌӡ˓Ѩ"ʗďȇˡtγȴĔҮɉ',
                    'arguments': [
                            {
                                        'name': 'ԨԦЈàАɢ9\u038bĬ\x91ыɒϐÖӭŉÑςҥԪΈŽђѱƽɜEƎԁĪ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4133482994126724852,
                                                    },
                                    },
                            {
                                        'name': 'ǃɖԇκԂҊQ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǅϭԫɍȆɰüʕίŽӠȂē;ɊӿПűòԪˈϨσ7ǔόzȐ\x8fѴ',
                                                                            'ΰɠӞ·Ԗ\u038bĲÚɈ^°ӳ1\x85żÅѮbЅȔɵѭѓɱƁɢϤбƴԈ',
                                                                            'ѺÓ»һΓ˓ĄɴӢ\x97ӀЍН//ǳδӪҁ˨\u0378ӎӝΞʒƤρĎˋr',
                                                                            "ƶìNŕCƐ˧\x8d'ҽϙŊʌeŖĀϯ4ήјZƻŊŀѭ_ӕ.Ǻy",
                                                                            'ï6\u0383°ͽƃÞFː<șΪΞÇσƏ«ȌǅӗǬŪ˪ԣǡQɀΗc¶',
                                                                            'Хĥ`ɩɹGǒԡĬǫ[%ðv˅½҈÷ʈμćȼÈĒȠ\x8bΟ˱ěѓ',
                                                                            '˽ɗϿz҄ҍѓöȦϠϸʏŊͻčСƼĦĲȅғҁĽiĽƍЙӢĸӘ',
                                                                            'ȶԬʐ\u0378ђԜǯËÄӢCˏћϜȠŏʔŀĥ"ƓƗȌɀǽƝǏɏðӺ',
                                                                            '\x98ȴǏžǃl¢уͰЩ˜ϹɅƼ\x86ŨϑϜȽţŵ\x8fóϐěʠ»@Ьŋ',
                                                                            'ʩĘ˅ɠ*˰ПʠҟΜӉЗˬBХüƣ\x9eȇdƭϰЄˑĿò˸Ӻаˁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԓλɮ҅ňԘʓϠХÜƌЩdŧɇĩͻR',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƜʪÁ4ҩĎͻ˧®ÃԠ˧ќɉŞūƻǀУϣ,зªӰSĐƖ˖Ĭԁ',
                                                                            'ȎӪɒƆͼǽНĿ$ǻȍ\x92`ѷˡĽì¸ɱԌГ#ӍƠɭɫ@ͲǉЃ',
                                                                            'ҮÉѡƯ\x9cϪĂϽԑѻԟɈȪȠҗʳӴͽҔÃѭӒSŷȃӻҫïӴÞ',
                                                                            '{ȷɼǡϖȓ\x9dԫƾӂɡΘȓƋоʵġǿɺѿ1\x8dМǃӲͳčÌ«Ȳ',
                                                                            'ϏöҏħϦМԡĿјɞϽѾΔқȀҙǥĎϙũЄşҋйԬIǄҎӆŝ',
                                                                            'ʈĜнEɍľ˜ԢұͶͶXͿĤЊʚ\x92ԙqǍňѕ«ϵɪϕċˇȹÐ',
                                                                            '\u0383σȎƥɟnƈΣ\x81ȐɆɤĵҽҧǖΎɲԛ¶ƙɻ˂ҦǝŠʘѬŀΔ',
                                                                            'ĹϽΰϢÉÁƁϡ϶˔ȋԪ˧ŭʬмžƸƞĖʥȧȂуϨˍÎȘΝƎ',
                                                                            'σ.ђҏøñҺƇÀőЖ",12ʹŅ}żŀ\x85ђчȲήȺǦɛчĭ',
                                                                            'ԡÖН*ҦӂрǩЇԪ҉Б˴зΓʦϯvѰȫǜǢΎƇҲǒӼɑͻã',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǊmΒ*ήϊɥčͷԂΨ϶tǛɃѪШƹʧ/ѲȾ?',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ĝ\x9eǣ҇RWУйϐϖǬ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 421850.6897256674,
                                                    },
                                    },
                            {
                                        'name': 'ђєЩ?&˽\x97Ďȩ϶Τїšҹ1ѤǆЏţȹůҚȄģǥлҲҪĮƵ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211845.426529:+0000',
                                                                            '20220526:211845.443117:+0000',
                                                                            '20220526:211845.460006:+0000',
                                                                            '20220526:211845.476992:+0000',
                                                                            '20220526:211845.493828:+0000',
                                                                            '20220526:211845.515437:+0000',
                                                                            '20220526:211845.535771:+0000',
                                                                            '20220526:211845.557804:+0000',
                                                                            '20220526:211845.577969:+0000',
                                                                            '20220526:211845.597787:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӊӭ϶ġCÝǕԆőʗƟǨĥʮâ+ϖЉȑǕȟǏʊԛͶz҉\x9cåϱ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3740554023571258795,
                                                                            -5518061682286707915,
                                                                            6435554624057746040,
                                                                            -7235151966453143501,
                                                                            9169987476886606948,
                                                                            -9044010534092928697,
                                                                            709660385272923688,
                                                                            8514724364072629919,
                                                                            7068879189988105442,
                                                                            -7323026411057895115,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϗʘҩł\x83ҵȆ\x96Ƭͱ҅ΡĳǒˋʿʜɘСͻӽΪʹӕʧǚѰ\x9eŀƿ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            180209.8592452107,
                                                                            76515.98751745585,
                                                                            -19355.114850450234,
                                                                            472185.04609730945,
                                                                            545165.6835504633,
                                                                            -34791.073839042416,
                                                                            113717.76832354232,
                                                                            209670.6669650704,
                                                                            219795.54508181388,
                                                                            615927.5763291381,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'șӮКɘǼɊƾЇԃPўȂəǯЏʛРϦǠ\x92ɯӽʔǲԭµĊŞȩ˼',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ѬǱҤӔěЬÛ˗ȌԚȒŏϐˁϩǮЩЄЄɭŀƁĮ˫0Ƶӄ;Ԧʷ',
                                                    },
                                    },
                            {
                                        'name': 'ǝǝ²ιϒΖéčUПȐэƪŜũ\x8cӳȋÿʑưfӦčˑƍŨɁßΨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '҆Ѝɾ%ȓӢʔưƝèʒПԀЁ\u03a2]ǲӮȂԗȏҌˇνĖ"ǘɜĶӼ',
                    'message': 'ł\x89ƠƣӍɑКêÚɉȚӲĤČ¾\u0382ƢǚθȒԂņέәɁТˉȭʢБ',
                    'arguments': [
                            {
                                        'name': 'ɝλЧ´ԧ\x86\u038dӈɴ\x98ʞҎĮûɻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ȭΰ?ɫɴʊЮ·ǠĮȊаҁƎϰҼчǽēʵŸ\x81Ίʇԟδ˙ζӑÍ',
                                                    },
                                    },
                            {
                                        'name': 'ĲĸʬοлìӸȻŻԮ\x8dõǤҪΒǛ5ȼŮƗҏМΩƼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211846.459808:+0000',
                                                                            '20220526:211846.476231:+0000',
                                                                            '20220526:211846.493572:+0000',
                                                                            '20220526:211846.510639:+0000',
                                                                            '20220526:211846.526352:+0000',
                                                                            '20220526:211846.542523:+0000',
                                                                            '20220526:211846.560005:+0000',
                                                                            '20220526:211846.576086:+0000',
                                                                            '20220526:211846.592384:+0000',
                                                                            '20220526:211846.608984:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩȕ˶\x8b#',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220526:211846.713399:+0000',
                                                                            '20220526:211846.736713:+0000',
                                                                            '20220526:211846.753076:+0000',
                                                                            '20220526:211846.770005:+0000',
                                                                            '20220526:211846.787066:+0000',
                                                                            '20220526:211846.803791:+0000',
                                                                            '20220526:211846.819798:+0000',
                                                                            '20220526:211846.836875:+0000',
                                                                            '20220526:211846.853734:+0000',
                                                                            '20220526:211846.870655:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʇɛЗʁôͳsΚ"ԗÿΒ҈Î҉\u0380\x9c˺IȎˤҘӓεгȟ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǜқ\x82ĉ˼ɅӇ\x97Ňυξв\x8e¯ʰ%ϔ҂Ьǎ³ɼtũ˴ǂӢԁΒƃ',
                                                    },
                                    },
                            {
                                        'name': 'ѱΐƗұͲΖҝ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 101945.13832403344,
                                                    },
                                    },
                            {
                                        'name': '9¢Ă҂[Ȯ\x86ɥƀ)ΑÇúдΣӦЋтp˒ӧ҈\x7fÊҧȑ?ƹϼӍ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɻÜĽǪņÑ΄Ν˺©\x98īĥʝϝХΨӭЯ×ӵ҉\u0382xǊłԇπǫм',
                                                    },
                                    },
                            {
                                        'name': 'ŅƁĕӥҳȭʥ\x9fѮԩĮύYĩАёӯèғɷÞƠȂАøϽúԑǆƞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǒМ˽»ӉȫÐНП˘ҚɸѹӦȮЫέĆԎɟɺʬȫӺʯǆ˯ΐӿũ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˦ōɽϢʼ\x9fķǃo\x86\u03a2ǒаÔвǴʈӮğţɲʴΫŵĕ|\x91ʻƍԌ',
                                                                            'јγΏȧΩ~ĉǒÐɞѕřԄѿįRΫΏӝîƻ*ț¼Ɍ\x9bŤХʛĄ',
                                                                            'hʁŬ±ȇ\x89Ҭyˎ.ЅϓοξɏȱІҀЎΠӁҚЪɡ\xa0xԮϠəʬ',
                                                                            'ÓĆȮɢΧǻԀ^μ,ΣŧΟžƶ˭üöʙӸЁÐӪķęˆȇIˎǋ',
                                                                            'з³ӔӖ±ʟԩZðʐňЄÀǩƃ\x7fƽ\u0378Ѭљԫaʬчмƺſ\u038bʗÞ',
                                                                            '>˦ɰÕЛǘл\x95әğӻľ\x88қʉԗĊϲ˴ӵжÈřu¾˳ÿɉΣƑ',
                                                                            'ΨîǠàЎǣ¨ΌǁЌĐĦҤĀԪȽ˵ԟðƷΆæέKѺǋ·őБ\\',
                                                                            'oʌА\x92ӘϏϋSƜɮƂȯď\x80ÔȸǵÓӿ=\x86\u0378ҩȜ9ŬǤ¿ßĘ',
                                                                            "ÏϹéŘšѡĐƧК'ėӱ\x7fĚ\x9eŰўñћӳ\x84ǆ«ơψŊÁѺȧ|",
                                                                            'ĄοȴҠ;ʁ{ɏʃŮǓĺ\x93\x98ʣC\\ϖʯƵѫѫͰĤϏþCɗΜŧ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xadʚЦƨҏц;ЌȁǅȊѝƏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5876369430785835067,
                                                    },
                                    },
                            {
                                        'name': 'Bˌы°Ǳ<ģƫ˵ĀWԩʜЀʺ ȻɪԤɷ}',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '£ĉ˞ͱЭMύ˱©#Ù\u0382Ñ6ªBȡɠЂАlӌҟͽʗ(ǴȫĊϳ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƆҚʡʾIѲȗˀɟѵ·ƛӠ`ǤͻԤńˈЗқͻĎѦѸȆΡϕǳĤ',
                    'message': 'ħԉʇȆBϞƳЪԥą˒ˣȨ!ɩŃԙʀ˾ѭµΙҐ˶ϭȌ´ƴĞϛ',
                    'arguments': [
                            {
                                        'name': '˞',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 846081.8198187037,
                                                    },
                                    },
                            {
                                        'name': 'Ǚƌ?ˋԀȊȨŜȋҔӍ\x95˳àѫɹVл',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'hɂˮϐȿΉыŇӀE˨ʤҡȕäÒäΊŬӚͳ\u03805ıÿ\u0380Ǡ°Ȕ\x84',
                                                                            'Cřͷv¹ŔªɺǟʻâȚӔǽԛԭ\x9fʰɀҖīн¥ɈǎҲʙӪӦ±',
                                                                            'ϯԄƁѻЧ§Χ Ȫʶ΄ӓŝԬЁ҅ϤȩːķѭÂһԑȭĭȢˈµ\x8b',
                                                                            '@мԣс˄ӊʤӛĜɲōŗųǮϐфƲԥˎʯʡжƪөū҂ӾԎȹ¥',
                                                                            'ɁˠX$ԅ>ͽϘŃǝԜ0˴ŵ˫ʫàĿ˖áѼ˪ȖΚόЛԊϒҢƟ',
                                                                            '\x7fԏӎԖДҸˋўřƆύʼ¿Κzǭˁ#Қǥ6cԔǇԄɺ²ÇǡȺ',
                                                                            'ƹɆɓ¢ČӾǼї˼ǖƓĽƄţƄęʁЧѨδӕҔŪǫπÇҹӅϏԈ',
                                                                            'пø4ǑʴȎˋӅVўϓ;ϥϿ)Ē\u03a2ɦŨÇɭΥǵŵӤȯҦɄŕӧ',
                                                                            'ʭЏȌˡʕϲďÕͳгʩæɾĀщDǒʏ˗ȣϴϙŒ˲õˌĄƭȆԐ',
                                                                            'Ɲӗí˖ԑѻ˒ԥǪ÷Ʋ˜ȝȐǛ˟УȠ½ЁɁʔԖϏϋʵԑº\u0380µ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ò˥ˈ\x96ɯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7596433810407448845,
                                                                            9103620745814522668,
                                                                            -2493669381142713404,
                                                                            -8871826444406440457,
                                                                            -8144736550039049420,
                                                                            8747686452825914863,
                                                                            -6742672724120229477,
                                                                            2595469100085584366,
                                                                            -8068735376169844252,
                                                                            -5360269622483175383,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑɏʓˣΎŒśɲʳͼΚĵӯԋ©NMbӒƽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 323184.04583235347,
                                                    },
                                    },
                            {
                                        'name': 'ͳϏ]ȉÿJΞƸτwιĝʎӷ˪*ŅͼТRȝͰ˔͵҅ϵӉԍȭÞ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            756653.6784432188,
                                                                            424802.5035043275,
                                                                            262404.1456087696,
                                                                            927748.0316810324,
                                                                            124715.19813803045,
                                                                            384660.15842443495,
                                                                            -72975.06595285311,
                                                                            -28945.712623985542,
                                                                            811108.851704343,
                                                                            430054.27058134717,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '/ǑǘʣˈѧдүӚƨ˝ͱMɉ©}~ gƯŮӹÚ¥',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            850187.5183030656,
                                                                            839617.0445869787,
                                                                            198315.4082527802,
                                                                            -78968.2134007362,
                                                                            115671.79296532011,
                                                                            101275.44453100371,
                                                                            -46369.18590087056,
                                                                            197169.19594132842,
                                                                            79152.36173391333,
                                                                            969293.2030514353,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'aΩȫƑ\x90ҽ\xadX˲¿ӍҁéȁϪԕƁӑ˷ӜΆʆɊҁɈŃƋØԙҴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 53607.76719786701,
                                                    },
                                    },
                            {
                                        'name': 'ÿщϫSå$ƙŭ(LϟԃPȐΜǥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            809615.1154031075,
                                                                            144069.39609622266,
                                                                            573963.5678070949,
                                                                            174233.3475685077,
                                                                            46038.854670825705,
                                                                            523007.67836509726,
                                                                            -45509.889804754355,
                                                                            274227.3356655283,
                                                                            912422.5002178672,
                                                                            960599.9004842145,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĞϦϕÜʁԇɳЎȶĒҖFӻ҂ȸƋʴƖǤΝ\u038dƋĘőzҵΣɹϼԠ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220526:211849.359011:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɲӓ;Ѹ',
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
                                                                            True,
                                                                            True,
                                                                            False,
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

            'identifier': 'ɿĦу\x8aɜ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ӌі',
                    'message': 'ʨ',
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
            'request_id': 2501058,
            'error': {
                'identifier': '»\u0381ПθûƮџʚƒѢ)ҙɂ˰ΫѲΦ˕Ƌ]ϬʬϠdŭĊБȩǡɭ',
                'categories': [
                    'internal',
                    'file',
                    'os',
                    'os',
                    'invalid-user-action',
                    'invalid-user-action',
                    'access-restriction',
                    'file',
                    'network',
                    'internal',
                ],
                'source': 'Ūο˩ɂѹ\x807áɬҞōÄέлńѮӋ¾Éǎҡ˕ʞƍΰԣ\x90į¢Ŧ',
                'messages': [
                    {
                            'catalog': 'ҪʵĺĪϪŬ\x9dĜǯԈһʢκȮϖƁМԊрɒξԨӍ³Ȉɬ%ΈҰ\x83',
                            'message': 'З¯%ǊÆ\u03a2ʎ.ɲ҇ʏϲӣӞѯĐqƓěυҍ˦ˀĘΒÄƮ¬ǣ§',
                            'arguments': [
                                        {
                                                        'name': 'ԖŋϟӂҷǝɐϨ;ԆĴπf\x88Ʈ<ԡʡµ\x89Ȱφ˶ċʺԏ³ɖп',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣ¼Цѱ҇ϺɊӿҸ¢ϓ˦ϘҦǰŞ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¦&ĉÜƷЛȏŁӞъ˷ӑԮČҮԮƒлĩ?ͶԉʚȤŹЍɘϕíў',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¶\u0383ŬЪΎɏЇǻǤ˞ɐƾɬȶʱ\xa0Ȩ%ҚkʠĠѦ¿˰ƅΜέДҼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211829.337301:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'χġĊԭź˗ϭʧͺ©ȫƊҫɫҢŔε9Ɨ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÊʆχЄԏƴӑs\x90ӽϻʻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '¿ɱѸыĝ\x8a!ѱʀϑƹ˶хciвǝÚŘţѵˬϙƎ.ƃϛǟʩ9',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7660635369131541721,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄǨ҆˵Μaóɫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'іӱΥȪӹӵȇ^ΰҙ²Ȣ¶҅®ÐЍēöαź\x91ĭʾϗÊƭəʃˣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8aBΆǮǵȐΥʔѝɶɲÀ9',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x82υDȎҵΟ´ȝҠҙёͽħπЙ',
                            'message': '´ςϢǷƩϞɖǃʪɶ˸ȰіϧӇȘÆ²ΎƐ0ӳҎơûƚ\x9eĆǂѱ',
                            'arguments': [
                                        {
                                                        'name': 'ҰʄФ\u0379³ŲνК',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¾ǣ¿Ԋł\x85ŧӾŝӠɮɎҘĔʨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -69486.91095962656,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɵ²\x98EáÇ%άĨМʍŀŐPìҥɛʩҜ¨ӱ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3373176541403075164,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӗʎȑǲƕс˜ωʺг˺\x9eˈ˻}ƸϘőŕҎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 746862.030012167,
                                                                        },
                                                    },
                                        {
                                                        'name': 'υʺʷӺӻҙU\x9aӗɏʅэƽίƫußŊΫоɰʍɥ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211830.180572:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӄѵ\u0380W\x81ˎћŀΒβ˽ƽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ł҂Ȝ÷ХʍĻȨЗčʊίʪ%ÁӟʆUϐěâĤӊɪˇ˼˯\x85',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʦ,ͿΤ\xa0қǋɠƣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211830.374988:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'бҠήӐ4ǀGǽìԉѦғ˪Ŧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211830.440209:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǡЌ˂ƄƚŁșÀԥϠ\\҃\x80¾ʅҊëЁɱǧX\x8aҐâ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÐǇXĖ3ČИǫԠӉȴΟ˩ɶʁɑȻƟΚЩԧƤʘ϶ǖǀˆҡϜƿ',
                            'message': 'ӕɕ\x93ԀǞƧƥѭÌӪŘɜ¾ЇҬœȆϊΕъ\x91ϲӋԘӳ;ӊŁΡe',
                            'arguments': [
                                        {
                                                        'name': 'ԈңƲΈɘˡβʩ˽ϜĢŅѢəʳƖϔ\x95_Ʀξ҅ǋΈР',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211830.640202:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ßĘ˟łρ˯!CÕѣ΄ę˒Ġэ˛ʓϒǳȫϦzǟʯđϽ҉тı\x92',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8312932505717358188,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0382ГҨҎ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 362262.09493735014,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҤȐӥЫʴkʇҗĨƆɦʰԬѦсǌ\x8cÞϛλѭȌʻӌҷНɗǥǟˮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 886640.8094718514,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɋԞͲǄjІºöȡϕхϪзƓ>ϕ\x96\u038dѾЌӤʴƣț\u038bѡƚǗqѩ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211830.923427:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨΦp˪ѽҲÉÔжɌϒħ«Ëȏ˰ЁŸϥŲâΔώͳáòºʫҜӞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211830.992321:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҰәÀɶȷԃĕǅǇ»ŚзɪҎϢŢҍԑɜǣԦ˾҆ưŅǝƬҖӷŸ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211831.060548:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'јԉÉħăx',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʷǏȁɵР,ԎΎϐˍmÖŴȲ\x82ŽƉ<˔їКʨӸԓ%ϱνˑ\x9eŶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝʋAҒˇ&ȈɃŴǶ˱ɌҔđţΉ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 711129.7106001537,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɠӴȉǐzǑϞǙψΆ˝ԪǾϝяÙɜԆϕѰʨɉ҅ӔũʙџΧπʏ',
                            'message': "ȑǰ'ҡƸϒſЯФԡӧЛ¿ʭ\xa0ԭ\x9d!γЁˏӇàƀϬˁÞLǘO",
                            'arguments': [
                                        {
                                                        'name': 'ΝćԪgήĐǽɦ~π˕ŧ?ƘĽϐƉˈӠІЈǧƅr\x88æҶȱçě',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5029768314361754299,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɧӑϥƔ"ѺɡΚ˼ԓκ=ӔȲҙ҇ĩʽ˓ĥ\x9c7ŊɛγˬƩφκ1',
                                                                        },
                                                    },
                                        {
                                                        'name': '¨МӾ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ə\x93ԏԚĉԩ҉ơZ¥ːgϒȶ\x9cҘŬƿǨǭȉĳȈԓϙçǳıəĉ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀѽɽЃŧҩǦҧƟԡɷԦˢöǝȂѲȽӹ~',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӗƗ˘Ǡ˵ыƐғѫ%įå\x90΄ӰΘʤŐӑˎćΰʾ˱ȑΫˮ¯Ɲԅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -71051.41028891454,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƢВʌd˽gĽȆ~(',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϞΝԂЧВa˘ŏұóҾρɉΨˌϼϺıѼѦҁÉƘȾ˝ŶЭƴǥZ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˞ȉ˝ЁņӶυӋ˻ӠǋǤ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211831.948012:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '.Äбс\\њˮŃȕ4҃k\x9eŤZĀ÷',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҌοԣȨĴĜ\u038dΤҾǬǼԢȓð\x80ӣɵŠ˻ń_ěʁϊŢeѠƀгˑ',
                            'message': '\u038bҺҘƤɴľˠԘȳƆþƿɣ\x87ͰÌҲłҎȞȃȔʈǒΠѺӳʕԟƱ',
                            'arguments': [
                                        {
                                                        'name': '<ϠɄѓԗ˚ϱ\x82ɷӉȻҼ)ЩҊϨƔ\x93ӬɛǏХȨϼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '&ȕ͵ɨԓǋƜυƿШӛŽñƼŤXǪЁȌɿŅҼξаŞǺ°áʱʸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĨÂѭѱιѱɞˮȓʛʭʔ²Ѐ_ϛ·ʳϤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1498761279715133898,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˑҳ04ΞαÙƃȥɿʡâʞ.4',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȹȈŊnċ\x95ўǹHӠʈʣ˂˹\x83šδrƉӞlǚЬɼʢ®űʶΏФ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɻȴΐo¡ƹ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͽң˨èìĜԪ\x92ʟԍ\x87ÖЪёȫʟǳӄĭǌ¤ɔƅӛ¶\x97ȡΚŰ½',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŉǋƘsʘǴρʒǠҡЃëpщԩɜώƵș',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɆrԠАǥκҸ\x94Ȉ˄ή;ˌˊѾўϦɞˏб',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎɤҮǡӠι°˰ùмѱϓǍӉчGȚЉ҇VӐΕΐ:ϭİűƯʄҹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7099242810252098390,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ũʛҥǔcŕˑ}ӒҏүҴυƾʮŨŀȍҾwǹĂǛŷϳƵȼ˼',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'öȲƍ˪˄Θ8\u03a2\x82җɖќ\x8bƬƙǲҔӷԛΠǰ\x81ӹȆӾԓƳϔŻɧ',
                            'message': 'ɖĜǵƅϼȊŎǇϔX\x84ǧοŌ\u038dgĥȤԏѵԏςғ,ȷVΤɓéÁ',
                            'arguments': [
                                        {
                                                        'name': 'ύ²',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϟгŃϟºŀυ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -85693.41683054013,
                                                                        },
                                                    },
                                        {
                                                        'name': '8>ɧǦƸԛ5ЃӏоĠԣɪ)ѭέΥɏŐρʷҕϡɺəɫҁƣ2ɩ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜ_ķ\x8cȄήӥȽǎЦ\x9clѝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 857554.8233539971,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȶ˯ԩʂɕįɹѪψȳÒΉ[ĝėɱШўΧӽΓЊЉŲµе҂Ӧѻu',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 251316030082318690,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭ;ÇǷȽ\x88Ԏѡ\u0383ϊȍ§ԜѪŘԞĒlżʈĨ˶ɩĶê˪Ӊɡϵг',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 407480.2387120662,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҌӘǪҟ¥ϗȨˉłӔɳ\x97ʊԂǩʙɪУ|ƆǸԧǟ\x8cˠӭɟ/\x83ѩ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƺΙʳҖŘ¥ҷÜŖɅ\x9fҞƇӑŖЬÓѕ·ĶҹͺӯѬБŀҀѕɷƯ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɥюϹ$ѨӟJЊӌɁфϓĉԟ½«eƐɑǴćȳЄ÷oʰӾˢȡ$',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƌȹϓԭҘѾ\x85ƨiƶёˤЌǵжԬʚĺ˷',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ͼɕӫɪʨʳʩëϢΫάɂøˠқǐɒԄЧӐЕˮͷьѢĂƉǗв¶',
                            'message': 'ӾŷȯĉɚŘҴyх¯Э"ȓʕԐӆĶӆŗĩΙ϶ɩČӮÆŠɦҸɶ',
                            'arguments': [
                                        {
                                                        'name': 'ԥΏӉє¸νѽΠʧWƤЮЧԀƴŲ»ǪɧšŖӜҢӗф\x9eҁŪȴӳ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ә9ɊĔ˒ŒŀϱϪÑӦ҈$ζ҄÷ƉЋ[ǝӈȃ\x92ºƮѨӗŭʚ˚',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѺӘÊIǁпɍԔƄЬў',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 207318.46620240342,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9cФŕȍˬӾӤοßª³Ϣ\u038bëŐǮӸ#Ԛɦ҃ăЭ\x9dΒƓӺhƫΜ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 97942.75174026995,
                                                                        },
                                                    },
                                        {
                                                        'name': '+ӜеɀϺŜӴǻďρʏԠȠѨΐȂȘηϡ]ȿȉą҆ЈӪɎϾ©Ӛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3914782833476027049,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӋН҄ӉӔ҅ҲʷO\u03a2ġȥȪǹчú¥ԎѲԁ\x93ȞԤȠǇЭˤ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'L˞қŸϒԦюͰʘĹĦɉéҢ²ΓΥԑǓŰšВʬηТҢ҄ξñĂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'D\u0382ʣПÿ\x96Ѷˌе',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '©ʐұãtШțӆt\x94ɳ\x94ƀL\x86·ΊÑѮ˩ȫˍQƼˏӞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220526:211834.157236:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȫIРІƤȋҪFȲŝţtʸˠƋɏi',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĉõ²Ь˷ʹéDъƨˡґŐĹьӭϖfҠƅ\x91ǙˤÈƨĿГLΊΆ',
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

            'request_id': 2455400,

            'error': {
                'identifier': 'ή¦ıAұ',
                'categories': [
                    'os',
                ],
                'messages': [
                    {
                            'catalog': 'ȡK',
                            'message': 'ƽ',
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
            'nw_x_pixel': -331123997,
            'nw_y_pixel': 708653505,
            'width': -7076101475461507116,
            'height': -5315650583997113793,
            'ratio_x': -6217555023255888917,
            'ratio_y': -2440874573464933891,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1694332697,

            'nw_y_pixel': 229227397,

            'width': -2710504872042781287,

            'height': -4805834488111969771,

            'ratio_x': -3536053175351900724,

            'ratio_y': -8896730384194741707,

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
                    'nw_x_pixel': -1522542678,
                    'nw_y_pixel': 33333215,
                    'width': -998244143898514152,
                    'height': -3826858618245811392,
                    'ratio_x': 4412492133222278291,
                    'ratio_y': -7432348573742451772,
                },
                {
                    'nw_x_pixel': -1432872709,
                    'nw_y_pixel': -945657565,
                    'width': -2941239461754411440,
                    'height': -8505816337745408955,
                    'ratio_x': 5901338817106657077,
                    'ratio_y': 2080952670285024900,
                },
                {
                    'nw_x_pixel': 1201989767,
                    'nw_y_pixel': 1051413477,
                    'width': -4142158891025501618,
                    'height': -2372312964350635339,
                    'ratio_x': -7550884289249983110,
                    'ratio_y': 1737247227828474932,
                },
                {
                    'nw_x_pixel': -1481014305,
                    'nw_y_pixel': 1296022392,
                    'width': -7084341352446320598,
                    'height': -3486183284337262872,
                    'ratio_x': 2027293359956847046,
                    'ratio_y': -8328546743980452850,
                },
                {
                    'nw_x_pixel': -1671681090,
                    'nw_y_pixel': 100256791,
                    'width': -4122255190488721039,
                    'height': -1954542121900189981,
                    'ratio_x': -7842430006734186396,
                    'ratio_y': 8426418052375136989,
                },
                {
                    'nw_x_pixel': 65318739,
                    'nw_y_pixel': -914236989,
                    'width': -1784864615624543538,
                    'height': -7132969565062367455,
                    'ratio_x': 4911461510075646317,
                    'ratio_y': -7097746042565017327,
                },
                {
                    'nw_x_pixel': 1500853515,
                    'nw_y_pixel': -293971236,
                    'width': -1515230733756689707,
                    'height': -7243745740897822155,
                    'ratio_x': 7947265713006137513,
                    'ratio_y': 4317765014509355604,
                },
                {
                    'nw_x_pixel': 423110307,
                    'nw_y_pixel': 1777264847,
                    'width': -64142749311761860,
                    'height': -3459504198248823969,
                    'ratio_x': 5149006493765530031,
                    'ratio_y': -3640742506202184252,
                },
                {
                    'nw_x_pixel': 913908636,
                    'nw_y_pixel': -1772426121,
                    'width': -5527773839148511844,
                    'height': -3872932023540722420,
                    'ratio_x': -8934854227487271264,
                    'ratio_y': 4424381480295557173,
                },
                {
                    'nw_x_pixel': -1245605340,
                    'nw_y_pixel': 1108507398,
                    'width': -3869307652175687284,
                    'height': -1196204591560520142,
                    'ratio_x': -2734339426794281586,
                    'ratio_y': -6512660175239333232,
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
                    'description': 'ǟĊȕȢѭҸăƊOɃ\x90ΎӗϼЩĩɡвƋľνgϬӊѫǋØϟ\u0382ƻ',
                    'monitors': [
                            {
                                        'identifier': 3686298,
                                        'width': 1839599266002816153,
                                        'height': 6764578607459499630,
                                    },
                            {
                                        'identifier': 8401687,
                                        'width': 7546765454162095632,
                                        'height': -2722588265403957090,
                                    },
                            {
                                        'identifier': 7950977,
                                        'width': -6094033168732637672,
                                        'height': 175746189719418879,
                                    },
                            {
                                        'identifier': 7363395,
                                        'width': -7501625618281083643,
                                        'height': 6414970834217018109,
                                    },
                            {
                                        'identifier': 2451403,
                                        'width': -3417707637237673169,
                                        'height': -1490135593308236008,
                                    },
                            {
                                        'identifier': 343686,
                                        'width': -4255919456657514549,
                                        'height': -6311004701903099211,
                                    },
                            {
                                        'identifier': 7726408,
                                        'width': -95315455742432924,
                                        'height': 5782506011766857972,
                                    },
                            {
                                        'identifier': 1395101,
                                        'width': 5658437245439083421,
                                        'height': -875519913846624746,
                                    },
                            {
                                        'identifier': 7176416,
                                        'width': -8938958190809770458,
                                        'height': -2988052136006003339,
                                    },
                            {
                                        'identifier': 9476975,
                                        'width': -8021233436545452339,
                                        'height': -6737365775507410128,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9305657,
                                        'source_nw_x_pixel': -8330139960062746069,
                                        'source_nw_y_pixel': -8080656991272865759,
                                        'source_pixel_width': -6420435780146071066,
                                        'source_pixel_height': -7375458741597444067,
                                        'rotation': -5620392197677288791,
                                        'virtual_nw_x_pixel': -1155217408,
                                        'virtual_nw_y_pixel': 131904189,
                                        'virtual_width': 145772399,
                                        'virtual_height': -248009816,
                                    },
                            {
                                        'source_monitor': -442719,
                                        'source_nw_x_pixel': -4229375102863260962,
                                        'source_nw_y_pixel': -4044254483891644025,
                                        'source_pixel_width': -332950570234113778,
                                        'source_pixel_height': -7612303005309915525,
                                        'rotation': -6623431859289840136,
                                        'virtual_nw_x_pixel': -1147443874,
                                        'virtual_nw_y_pixel': 337304385,
                                        'virtual_width': -1320355937,
                                        'virtual_height': -1642065707,
                                    },
                            {
                                        'source_monitor': 1279049,
                                        'source_nw_x_pixel': -6141154979616522890,
                                        'source_nw_y_pixel': -4890723720298841880,
                                        'source_pixel_width': -7223755762616548315,
                                        'source_pixel_height': -5294576950807796345,
                                        'rotation': -2006185569730649521,
                                        'virtual_nw_x_pixel': 316784820,
                                        'virtual_nw_y_pixel': -600050713,
                                        'virtual_width': 1501935305,
                                        'virtual_height': 914709261,
                                    },
                            {
                                        'source_monitor': 3817986,
                                        'source_nw_x_pixel': -8308242123038070499,
                                        'source_nw_y_pixel': -2212735029277470586,
                                        'source_pixel_width': -131751511209292796,
                                        'source_pixel_height': -6562430264914273227,
                                        'rotation': -5105384371300763327,
                                        'virtual_nw_x_pixel': 511861962,
                                        'virtual_nw_y_pixel': -398799273,
                                        'virtual_width': -1658637952,
                                        'virtual_height': 722532736,
                                    },
                            {
                                        'source_monitor': 4185377,
                                        'source_nw_x_pixel': -7430233979820097394,
                                        'source_nw_y_pixel': -4786081931528360921,
                                        'source_pixel_width': -4555505344367540693,
                                        'source_pixel_height': -2646949791764263856,
                                        'rotation': -5528497492818930439,
                                        'virtual_nw_x_pixel': -1502263894,
                                        'virtual_nw_y_pixel': -510856464,
                                        'virtual_width': -1970590925,
                                        'virtual_height': 522743693,
                                    },
                            {
                                        'source_monitor': -225922,
                                        'source_nw_x_pixel': -6476416062728911017,
                                        'source_nw_y_pixel': -8908951833918849091,
                                        'source_pixel_width': -8891323090719350235,
                                        'source_pixel_height': -7490966293301606178,
                                        'rotation': -2512828938617021042,
                                        'virtual_nw_x_pixel': 1529226379,
                                        'virtual_nw_y_pixel': 1992746885,
                                        'virtual_width': -974837187,
                                        'virtual_height': -1256537692,
                                    },
                            {
                                        'source_monitor': 1377253,
                                        'source_nw_x_pixel': -5284204716324118851,
                                        'source_nw_y_pixel': -3116756799767802625,
                                        'source_pixel_width': -4914937137958938359,
                                        'source_pixel_height': -6635548237992347250,
                                        'rotation': -4825680885657825664,
                                        'virtual_nw_x_pixel': 1040126362,
                                        'virtual_nw_y_pixel': 1189234878,
                                        'virtual_width': 1925438926,
                                        'virtual_height': 244508908,
                                    },
                            {
                                        'source_monitor': -644357,
                                        'source_nw_x_pixel': -1305773759616163699,
                                        'source_nw_y_pixel': -4092913972863968637,
                                        'source_pixel_width': -2957160531782627314,
                                        'source_pixel_height': -5680893605405197899,
                                        'rotation': -2875175643723650381,
                                        'virtual_nw_x_pixel': 1322053379,
                                        'virtual_nw_y_pixel': -1717785212,
                                        'virtual_width': 155258172,
                                        'virtual_height': -1094507180,
                                    },
                            {
                                        'source_monitor': 7300237,
                                        'source_nw_x_pixel': -5077041303895397249,
                                        'source_nw_y_pixel': -3600832999138964495,
                                        'source_pixel_width': -1945513605156873048,
                                        'source_pixel_height': -8989268375063467634,
                                        'rotation': -5267096763549406383,
                                        'virtual_nw_x_pixel': 191739031,
                                        'virtual_nw_y_pixel': 1268811055,
                                        'virtual_width': -122987801,
                                        'virtual_height': -970887193,
                                    },
                            {
                                        'source_monitor': 5625724,
                                        'source_nw_x_pixel': -7399737261081063125,
                                        'source_nw_y_pixel': -899748399445471376,
                                        'source_pixel_width': -2975556501184498775,
                                        'source_pixel_height': -1557193448179438282,
                                        'rotation': -5086799724112008336,
                                        'virtual_nw_x_pixel': 1323838073,
                                        'virtual_nw_y_pixel': 152971340,
                                        'virtual_width': 1780072456,
                                        'virtual_height': -1199076627,
                                    },
                        ],
                },
                {
                    'description': 'Ñ_UÄΰϵӵNŻÓӇʃҥ2àΧ|ȲΐӃÔ˞´ʝ\x93ŮɆŠ΅Δ',
                    'monitors': [
                            {
                                        'identifier': 8529081,
                                        'width': -2278427876893757416,
                                        'height': 5218600513102354283,
                                    },
                            {
                                        'identifier': 9633231,
                                        'width': -4660175618261760022,
                                        'height': 647964972556825251,
                                    },
                            {
                                        'identifier': 4144979,
                                        'width': -4032119769739064951,
                                        'height': 797587662355296219,
                                    },
                            {
                                        'identifier': 7606835,
                                        'width': -8104810697124384709,
                                        'height': 2818018817893468851,
                                    },
                            {
                                        'identifier': 1839036,
                                        'width': -2326399149571739447,
                                        'height': -7481804857475850150,
                                    },
                            {
                                        'identifier': 9592307,
                                        'width': 4687365871253010125,
                                        'height': 5731558553206503001,
                                    },
                            {
                                        'identifier': 9569238,
                                        'width': 4508524530271803726,
                                        'height': -257287048916033558,
                                    },
                            {
                                        'identifier': 2302676,
                                        'width': -3298685869292106925,
                                        'height': 4702463609225218524,
                                    },
                            {
                                        'identifier': 9036786,
                                        'width': 6866915121576671730,
                                        'height': -1122213003284608049,
                                    },
                            {
                                        'identifier': -721332,
                                        'width': -5461937158266481216,
                                        'height': 4938669609624292474,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2819856,
                                        'source_nw_x_pixel': -7030600709941085915,
                                        'source_nw_y_pixel': -8035439396963116739,
                                        'source_pixel_width': -3747291594926282527,
                                        'source_pixel_height': -2390204651184900701,
                                        'rotation': -684084422981196852,
                                        'virtual_nw_x_pixel': 1575470180,
                                        'virtual_nw_y_pixel': 772829892,
                                        'virtual_width': -499187375,
                                        'virtual_height': 196508654,
                                    },
                            {
                                        'source_monitor': 3173114,
                                        'source_nw_x_pixel': -2142031770365122093,
                                        'source_nw_y_pixel': -6616523882753827142,
                                        'source_pixel_width': -2178366667647906513,
                                        'source_pixel_height': -99782375147289500,
                                        'rotation': -6368044682649238512,
                                        'virtual_nw_x_pixel': -372658956,
                                        'virtual_nw_y_pixel': 464246629,
                                        'virtual_width': -1935785054,
                                        'virtual_height': -766358937,
                                    },
                            {
                                        'source_monitor': 801820,
                                        'source_nw_x_pixel': -5648682756350798862,
                                        'source_nw_y_pixel': -2191430518922730737,
                                        'source_pixel_width': -7969090139069716979,
                                        'source_pixel_height': -693595986897539470,
                                        'rotation': -2325830952088289657,
                                        'virtual_nw_x_pixel': 1199322114,
                                        'virtual_nw_y_pixel': -880012632,
                                        'virtual_width': -213801043,
                                        'virtual_height': 1980201687,
                                    },
                            {
                                        'source_monitor': 7674793,
                                        'source_nw_x_pixel': -4322790661230391013,
                                        'source_nw_y_pixel': -6076783154582340027,
                                        'source_pixel_width': -2614819145013221972,
                                        'source_pixel_height': -5306605757091039,
                                        'rotation': -8016547177025896216,
                                        'virtual_nw_x_pixel': -1974391456,
                                        'virtual_nw_y_pixel': 1605031779,
                                        'virtual_width': 1895020195,
                                        'virtual_height': -1168281348,
                                    },
                            {
                                        'source_monitor': 9677087,
                                        'source_nw_x_pixel': -6261257889155755014,
                                        'source_nw_y_pixel': -8096340828013712838,
                                        'source_pixel_width': -6419739249424121189,
                                        'source_pixel_height': -664339421992626211,
                                        'rotation': -1588415646509758117,
                                        'virtual_nw_x_pixel': 374840601,
                                        'virtual_nw_y_pixel': -862092707,
                                        'virtual_width': 332353263,
                                        'virtual_height': -828795053,
                                    },
                            {
                                        'source_monitor': 661217,
                                        'source_nw_x_pixel': -5298879627620704773,
                                        'source_nw_y_pixel': -3397794053600092237,
                                        'source_pixel_width': -8656568669131216177,
                                        'source_pixel_height': -6878549962367873055,
                                        'rotation': -7782745719606388707,
                                        'virtual_nw_x_pixel': 909787448,
                                        'virtual_nw_y_pixel': 1788791739,
                                        'virtual_width': -1239947979,
                                        'virtual_height': -229554027,
                                    },
                            {
                                        'source_monitor': 4685037,
                                        'source_nw_x_pixel': -5924243646309618744,
                                        'source_nw_y_pixel': -3737773154375694642,
                                        'source_pixel_width': -4862204832726073120,
                                        'source_pixel_height': -3780978559138212031,
                                        'rotation': -1317448544434495109,
                                        'virtual_nw_x_pixel': -1066994325,
                                        'virtual_nw_y_pixel': -391582495,
                                        'virtual_width': 834545781,
                                        'virtual_height': -707009170,
                                    },
                            {
                                        'source_monitor': 5393242,
                                        'source_nw_x_pixel': -4340929194292757692,
                                        'source_nw_y_pixel': -7339650820423698469,
                                        'source_pixel_width': -2255901084196270328,
                                        'source_pixel_height': -3354068952549110682,
                                        'rotation': -2433959501883554705,
                                        'virtual_nw_x_pixel': 1101469695,
                                        'virtual_nw_y_pixel': 555397962,
                                        'virtual_width': 1058250741,
                                        'virtual_height': -792190698,
                                    },
                            {
                                        'source_monitor': 878095,
                                        'source_nw_x_pixel': -6918981283935800054,
                                        'source_nw_y_pixel': -7117276328666668775,
                                        'source_pixel_width': -8662031430896426312,
                                        'source_pixel_height': -470152795153873630,
                                        'rotation': -7298141045465326554,
                                        'virtual_nw_x_pixel': -1903151585,
                                        'virtual_nw_y_pixel': 1886350474,
                                        'virtual_width': 1736831442,
                                        'virtual_height': -70360258,
                                    },
                            {
                                        'source_monitor': 3013631,
                                        'source_nw_x_pixel': -8261432856316071744,
                                        'source_nw_y_pixel': -4556819709879682801,
                                        'source_pixel_width': -495907752814004935,
                                        'source_pixel_height': -2455983220803484829,
                                        'rotation': -4007010179050488347,
                                        'virtual_nw_x_pixel': -983567668,
                                        'virtual_nw_y_pixel': -576628428,
                                        'virtual_width': -663467013,
                                        'virtual_height': 1931465737,
                                    },
                        ],
                },
                {
                    'description': 'Ƨȋsң°ˏҭkɑςӼʀΌуҽ(ʛѠτχгȻ&LĬΏţśԕȝ',
                    'monitors': [
                            {
                                        'identifier': 7973691,
                                        'width': -5505574261054665636,
                                        'height': -6644448151299128408,
                                    },
                            {
                                        'identifier': 7593157,
                                        'width': -6377518029789642442,
                                        'height': -3389738910076393290,
                                    },
                            {
                                        'identifier': 4095970,
                                        'width': -1170635358832618584,
                                        'height': 7183325516495509931,
                                    },
                            {
                                        'identifier': 2237266,
                                        'width': -7690514133398707647,
                                        'height': 201486066886142373,
                                    },
                            {
                                        'identifier': 8489549,
                                        'width': 5016692149771366116,
                                        'height': -4936389618581163831,
                                    },
                            {
                                        'identifier': 9416960,
                                        'width': -3336406107767606419,
                                        'height': 4525572440867776043,
                                    },
                            {
                                        'identifier': 7136648,
                                        'width': -7740552739963428500,
                                        'height': -8886947516565064919,
                                    },
                            {
                                        'identifier': 2918737,
                                        'width': 6006264196774276784,
                                        'height': -1449177513378999581,
                                    },
                            {
                                        'identifier': 7289084,
                                        'width': 8706141450913092185,
                                        'height': 5812992129340184920,
                                    },
                            {
                                        'identifier': 6363979,
                                        'width': 8992001704058529795,
                                        'height': 6926197768835634900,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3635418,
                                        'source_nw_x_pixel': -6548174934769519727,
                                        'source_nw_y_pixel': -3607499348450140270,
                                        'source_pixel_width': -6263118797134017470,
                                        'source_pixel_height': -4641009250611072309,
                                        'rotation': -6926979347517250671,
                                        'virtual_nw_x_pixel': 482543691,
                                        'virtual_nw_y_pixel': -158770714,
                                        'virtual_width': 754613407,
                                        'virtual_height': 377783978,
                                    },
                            {
                                        'source_monitor': -121422,
                                        'source_nw_x_pixel': -4230567630254747051,
                                        'source_nw_y_pixel': -4625408763321944505,
                                        'source_pixel_width': -6807276604939159061,
                                        'source_pixel_height': -6879548273611790130,
                                        'rotation': -7752709688645137600,
                                        'virtual_nw_x_pixel': -1589838446,
                                        'virtual_nw_y_pixel': -747139322,
                                        'virtual_width': -781790260,
                                        'virtual_height': 1593518664,
                                    },
                            {
                                        'source_monitor': 5702941,
                                        'source_nw_x_pixel': -6735659484522929561,
                                        'source_nw_y_pixel': -7934017806698685075,
                                        'source_pixel_width': -1638838384382094165,
                                        'source_pixel_height': -5257325738326154706,
                                        'rotation': -2786187980942703393,
                                        'virtual_nw_x_pixel': -1433852604,
                                        'virtual_nw_y_pixel': 1886662484,
                                        'virtual_width': -693499828,
                                        'virtual_height': 632444518,
                                    },
                            {
                                        'source_monitor': -473703,
                                        'source_nw_x_pixel': -7956990054239802960,
                                        'source_nw_y_pixel': -6444935834744523096,
                                        'source_pixel_width': -860599379419001352,
                                        'source_pixel_height': -149849226790094243,
                                        'rotation': -437124472928660231,
                                        'virtual_nw_x_pixel': 1227759112,
                                        'virtual_nw_y_pixel': 1168336587,
                                        'virtual_width': 1329799502,
                                        'virtual_height': -1381804016,
                                    },
                            {
                                        'source_monitor': 7131142,
                                        'source_nw_x_pixel': -8736873595467921480,
                                        'source_nw_y_pixel': -1932631817861984334,
                                        'source_pixel_width': -363196557306547311,
                                        'source_pixel_height': -1938612126112758201,
                                        'rotation': -555815354364594953,
                                        'virtual_nw_x_pixel': -1672773707,
                                        'virtual_nw_y_pixel': -710272293,
                                        'virtual_width': 585014014,
                                        'virtual_height': -1746788749,
                                    },
                            {
                                        'source_monitor': 83818,
                                        'source_nw_x_pixel': -2411587797414207286,
                                        'source_nw_y_pixel': -1472564608775508473,
                                        'source_pixel_width': -9183983558667720717,
                                        'source_pixel_height': -6531924938061501833,
                                        'rotation': -2069136497079260606,
                                        'virtual_nw_x_pixel': 1117831001,
                                        'virtual_nw_y_pixel': -43343423,
                                        'virtual_width': 468867200,
                                        'virtual_height': -1374480683,
                                    },
                            {
                                        'source_monitor': 7094789,
                                        'source_nw_x_pixel': -5684129710806686195,
                                        'source_nw_y_pixel': -4650500691380387041,
                                        'source_pixel_width': -3466203822215005592,
                                        'source_pixel_height': -505752969364762175,
                                        'rotation': -8246459392910642892,
                                        'virtual_nw_x_pixel': 375056843,
                                        'virtual_nw_y_pixel': 1190894583,
                                        'virtual_width': 1962384472,
                                        'virtual_height': -1040622715,
                                    },
                            {
                                        'source_monitor': 4380291,
                                        'source_nw_x_pixel': -3061987576678255859,
                                        'source_nw_y_pixel': -3147720376567778391,
                                        'source_pixel_width': -7521219476677736529,
                                        'source_pixel_height': -889184273123432352,
                                        'rotation': -2852044909029360329,
                                        'virtual_nw_x_pixel': 1382707842,
                                        'virtual_nw_y_pixel': 981707581,
                                        'virtual_width': 1981626876,
                                        'virtual_height': -806132225,
                                    },
                            {
                                        'source_monitor': 8154047,
                                        'source_nw_x_pixel': -915149206543293416,
                                        'source_nw_y_pixel': -5373235840335351069,
                                        'source_pixel_width': -816164896297386075,
                                        'source_pixel_height': -1519028624447482138,
                                        'rotation': -2042114489565699497,
                                        'virtual_nw_x_pixel': -1784277836,
                                        'virtual_nw_y_pixel': -818137461,
                                        'virtual_width': 879590049,
                                        'virtual_height': -1961281406,
                                    },
                            {
                                        'source_monitor': 4902660,
                                        'source_nw_x_pixel': -8409287965554480985,
                                        'source_nw_y_pixel': -5358136547623784018,
                                        'source_pixel_width': -7107104435553585150,
                                        'source_pixel_height': -6368520073538446458,
                                        'rotation': -6310459220729255263,
                                        'virtual_nw_x_pixel': 747996648,
                                        'virtual_nw_y_pixel': 310562941,
                                        'virtual_width': -48104895,
                                        'virtual_height': -148007312,
                                    },
                        ],
                },
                {
                    'description': "˹;ɧѤј˒ƺĥ§ßɰǵώʀ\x9f4Ǡ©ʪǝӊчÚ'®\u0382ơӎԭÝ",
                    'monitors': [
                            {
                                        'identifier': 1081750,
                                        'width': 4112710984962990842,
                                        'height': 3878670205283642868,
                                    },
                            {
                                        'identifier': 1999073,
                                        'width': 5701175166430573645,
                                        'height': -6655994908882501449,
                                    },
                            {
                                        'identifier': 6973103,
                                        'width': 946794099833491229,
                                        'height': 2220714599095291241,
                                    },
                            {
                                        'identifier': 6740574,
                                        'width': -2436958919701496174,
                                        'height': -7710873763364872789,
                                    },
                            {
                                        'identifier': 1993364,
                                        'width': 7821701605757367194,
                                        'height': -8927007212247005071,
                                    },
                            {
                                        'identifier': 5646657,
                                        'width': 322192090677784595,
                                        'height': 3986581392457556773,
                                    },
                            {
                                        'identifier': 2644555,
                                        'width': -7847359053950202046,
                                        'height': 2986235990562148677,
                                    },
                            {
                                        'identifier': 9662627,
                                        'width': 8124467681802641748,
                                        'height': -3276628308853058270,
                                    },
                            {
                                        'identifier': 2362501,
                                        'width': -3538924917651228732,
                                        'height': -5074757565208384813,
                                    },
                            {
                                        'identifier': 6285985,
                                        'width': 6766498379203469534,
                                        'height': 2693701562431172832,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8203444,
                                        'source_nw_x_pixel': -8330732090854571576,
                                        'source_nw_y_pixel': -4318653051646315429,
                                        'source_pixel_width': -5346589296203329730,
                                        'source_pixel_height': -2156697088667867196,
                                        'rotation': -2234856487444378198,
                                        'virtual_nw_x_pixel': -380885158,
                                        'virtual_nw_y_pixel': 1820419580,
                                        'virtual_width': -1498458110,
                                        'virtual_height': 151955448,
                                    },
                            {
                                        'source_monitor': 2764386,
                                        'source_nw_x_pixel': -7692080400964064613,
                                        'source_nw_y_pixel': -4319488273919951758,
                                        'source_pixel_width': -8123321687883795228,
                                        'source_pixel_height': -4025891688617152020,
                                        'rotation': -7495209721891217612,
                                        'virtual_nw_x_pixel': -1494852496,
                                        'virtual_nw_y_pixel': 156711047,
                                        'virtual_width': -69985956,
                                        'virtual_height': 217217709,
                                    },
                            {
                                        'source_monitor': -929316,
                                        'source_nw_x_pixel': -8611615364608573917,
                                        'source_nw_y_pixel': -2163659653622128993,
                                        'source_pixel_width': -469906013156802531,
                                        'source_pixel_height': -1347298929918777581,
                                        'rotation': -6581771520682506678,
                                        'virtual_nw_x_pixel': 376245300,
                                        'virtual_nw_y_pixel': 1375565593,
                                        'virtual_width': 135306520,
                                        'virtual_height': -1631851623,
                                    },
                            {
                                        'source_monitor': 4497543,
                                        'source_nw_x_pixel': -2660218389998520218,
                                        'source_nw_y_pixel': -2427935700026417605,
                                        'source_pixel_width': -2103511626702486078,
                                        'source_pixel_height': -39721551193957749,
                                        'rotation': -2602265703905565402,
                                        'virtual_nw_x_pixel': 1087042443,
                                        'virtual_nw_y_pixel': 1188433172,
                                        'virtual_width': 1560457708,
                                        'virtual_height': -1147714976,
                                    },
                            {
                                        'source_monitor': 4862448,
                                        'source_nw_x_pixel': -8143196776430564716,
                                        'source_nw_y_pixel': -679278374212166446,
                                        'source_pixel_width': -2122341741856309926,
                                        'source_pixel_height': -3198434446932804301,
                                        'rotation': -1324955578103400908,
                                        'virtual_nw_x_pixel': 1606833597,
                                        'virtual_nw_y_pixel': 1025535823,
                                        'virtual_width': -1693897666,
                                        'virtual_height': -935209867,
                                    },
                            {
                                        'source_monitor': 4340570,
                                        'source_nw_x_pixel': -2398066576374912487,
                                        'source_nw_y_pixel': -8161618459393735662,
                                        'source_pixel_width': -8266303028008523216,
                                        'source_pixel_height': -5275332856124757279,
                                        'rotation': -3426150698382852450,
                                        'virtual_nw_x_pixel': -164504764,
                                        'virtual_nw_y_pixel': -519777641,
                                        'virtual_width': 733505005,
                                        'virtual_height': 1316964912,
                                    },
                            {
                                        'source_monitor': 3182666,
                                        'source_nw_x_pixel': -8589315000358605952,
                                        'source_nw_y_pixel': -6459362415101285980,
                                        'source_pixel_width': -6821120253381882254,
                                        'source_pixel_height': -4614571747572146062,
                                        'rotation': -5979076183313109281,
                                        'virtual_nw_x_pixel': -986619518,
                                        'virtual_nw_y_pixel': -792368561,
                                        'virtual_width': 1353157854,
                                        'virtual_height': 282513462,
                                    },
                            {
                                        'source_monitor': 5030228,
                                        'source_nw_x_pixel': -3174707942357034801,
                                        'source_nw_y_pixel': -1746656368896739995,
                                        'source_pixel_width': -8642597260455131434,
                                        'source_pixel_height': -6355195193340308253,
                                        'rotation': -871546760674383804,
                                        'virtual_nw_x_pixel': -716775960,
                                        'virtual_nw_y_pixel': -999023446,
                                        'virtual_width': -254417625,
                                        'virtual_height': 916289557,
                                    },
                            {
                                        'source_monitor': 6233440,
                                        'source_nw_x_pixel': -7626335233180891177,
                                        'source_nw_y_pixel': -830316361041854844,
                                        'source_pixel_width': -5015897759302174104,
                                        'source_pixel_height': -8155725819097231319,
                                        'rotation': -3774670140773792514,
                                        'virtual_nw_x_pixel': 223960554,
                                        'virtual_nw_y_pixel': 32343524,
                                        'virtual_width': -1940343614,
                                        'virtual_height': 1508464410,
                                    },
                            {
                                        'source_monitor': 1976571,
                                        'source_nw_x_pixel': -4228638355414555879,
                                        'source_nw_y_pixel': -9147482936065831041,
                                        'source_pixel_width': -1843402837971901469,
                                        'source_pixel_height': -6582464683299504707,
                                        'rotation': -1333886640583946403,
                                        'virtual_nw_x_pixel': -1615957624,
                                        'virtual_nw_y_pixel': 1097026710,
                                        'virtual_width': 310708543,
                                        'virtual_height': 174974830,
                                    },
                        ],
                },
                {
                    'description': 'ӜȧKάK˒ϑȺБ`ǀęҁΛԟώҗeýʄvеŲΧΘчɧѸ\u0379ѣ',
                    'monitors': [
                            {
                                        'identifier': -358936,
                                        'width': 3897490772566925504,
                                        'height': -7205269880135444082,
                                    },
                            {
                                        'identifier': 6070580,
                                        'width': -7549520978785361690,
                                        'height': -2770638583937280047,
                                    },
                            {
                                        'identifier': -782576,
                                        'width': 6375587351587688949,
                                        'height': 4999987073928373585,
                                    },
                            {
                                        'identifier': 8202295,
                                        'width': 456828845352754659,
                                        'height': 5326920576301782172,
                                    },
                            {
                                        'identifier': 4000605,
                                        'width': 3536302540728596553,
                                        'height': 2721573126652378875,
                                    },
                            {
                                        'identifier': 2585114,
                                        'width': 2621222716412655642,
                                        'height': -6818006805545526970,
                                    },
                            {
                                        'identifier': 8259451,
                                        'width': 4616110451544354860,
                                        'height': 4446066415813320609,
                                    },
                            {
                                        'identifier': 8318268,
                                        'width': 6473052669669513828,
                                        'height': 4436630960642933102,
                                    },
                            {
                                        'identifier': 6884966,
                                        'width': 3945635066063202968,
                                        'height': 2509759293356818449,
                                    },
                            {
                                        'identifier': 3421647,
                                        'width': 2494060543846026729,
                                        'height': 7159660089864531745,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7814059,
                                        'source_nw_x_pixel': -490261811325837054,
                                        'source_nw_y_pixel': -6822709893311650493,
                                        'source_pixel_width': -8933640084909145348,
                                        'source_pixel_height': -2165978355622169715,
                                        'rotation': -839181248907182816,
                                        'virtual_nw_x_pixel': 624887498,
                                        'virtual_nw_y_pixel': -736179938,
                                        'virtual_width': -1322476389,
                                        'virtual_height': -513542004,
                                    },
                            {
                                        'source_monitor': 2499647,
                                        'source_nw_x_pixel': -5761522338008710044,
                                        'source_nw_y_pixel': -2845708752593454326,
                                        'source_pixel_width': -1625083374401245467,
                                        'source_pixel_height': -5839937162216742566,
                                        'rotation': -9062651046790278420,
                                        'virtual_nw_x_pixel': 567622737,
                                        'virtual_nw_y_pixel': 1443761891,
                                        'virtual_width': 1201381833,
                                        'virtual_height': -372434048,
                                    },
                            {
                                        'source_monitor': 9497003,
                                        'source_nw_x_pixel': -6712631392630019014,
                                        'source_nw_y_pixel': -6641477457682901001,
                                        'source_pixel_width': -1574370763828910707,
                                        'source_pixel_height': -8992903711461834131,
                                        'rotation': -8833390455418285599,
                                        'virtual_nw_x_pixel': 628829982,
                                        'virtual_nw_y_pixel': 1380422862,
                                        'virtual_width': -87217451,
                                        'virtual_height': -749657268,
                                    },
                            {
                                        'source_monitor': 6348443,
                                        'source_nw_x_pixel': -8170792848800429084,
                                        'source_nw_y_pixel': -8414649924260932763,
                                        'source_pixel_width': -8880304594521049393,
                                        'source_pixel_height': -669676896748332795,
                                        'rotation': -5604293083649041352,
                                        'virtual_nw_x_pixel': -1115549257,
                                        'virtual_nw_y_pixel': -491860210,
                                        'virtual_width': -1078948138,
                                        'virtual_height': 588906969,
                                    },
                            {
                                        'source_monitor': -931835,
                                        'source_nw_x_pixel': -3687864972295693523,
                                        'source_nw_y_pixel': -5245493132250668523,
                                        'source_pixel_width': -3171931250229338833,
                                        'source_pixel_height': -3266218509400097547,
                                        'rotation': -9068446758185851193,
                                        'virtual_nw_x_pixel': 408262671,
                                        'virtual_nw_y_pixel': -148043977,
                                        'virtual_width': 1985424443,
                                        'virtual_height': 654118386,
                                    },
                            {
                                        'source_monitor': 5827697,
                                        'source_nw_x_pixel': -7817967707928756267,
                                        'source_nw_y_pixel': -837621410720911479,
                                        'source_pixel_width': -4343154338938091562,
                                        'source_pixel_height': -4126038035429758901,
                                        'rotation': -2046334309777225827,
                                        'virtual_nw_x_pixel': -207487617,
                                        'virtual_nw_y_pixel': 345814458,
                                        'virtual_width': -1931009894,
                                        'virtual_height': -403048455,
                                    },
                            {
                                        'source_monitor': 4465471,
                                        'source_nw_x_pixel': -3524190098283340035,
                                        'source_nw_y_pixel': -7416732723714956406,
                                        'source_pixel_width': -6946342975360955841,
                                        'source_pixel_height': -5611967588461247712,
                                        'rotation': -7647323814184790203,
                                        'virtual_nw_x_pixel': -1771209739,
                                        'virtual_nw_y_pixel': 53683632,
                                        'virtual_width': -830342693,
                                        'virtual_height': -254358816,
                                    },
                            {
                                        'source_monitor': 8787693,
                                        'source_nw_x_pixel': -5939477063230223234,
                                        'source_nw_y_pixel': -3580098625458008293,
                                        'source_pixel_width': -3934996185537425811,
                                        'source_pixel_height': -4952222837908379631,
                                        'rotation': -6040711887140856093,
                                        'virtual_nw_x_pixel': -1212234736,
                                        'virtual_nw_y_pixel': -937619200,
                                        'virtual_width': 944622968,
                                        'virtual_height': -81908388,
                                    },
                            {
                                        'source_monitor': 1802781,
                                        'source_nw_x_pixel': -5124565499798310221,
                                        'source_nw_y_pixel': -8888819799957819412,
                                        'source_pixel_width': -1575848838840819882,
                                        'source_pixel_height': -3189904146400087830,
                                        'rotation': -8532307293963933403,
                                        'virtual_nw_x_pixel': -1486477033,
                                        'virtual_nw_y_pixel': -52468004,
                                        'virtual_width': 290437615,
                                        'virtual_height': 1980861818,
                                    },
                            {
                                        'source_monitor': 3877282,
                                        'source_nw_x_pixel': -8032948194623294294,
                                        'source_nw_y_pixel': -2832113877085820964,
                                        'source_pixel_width': -4007355230842189263,
                                        'source_pixel_height': -757771912349400691,
                                        'rotation': -2480525133577048880,
                                        'virtual_nw_x_pixel': -8343797,
                                        'virtual_nw_y_pixel': -198672241,
                                        'virtual_width': 482690567,
                                        'virtual_height': 52425725,
                                    },
                        ],
                },
                {
                    'description': 'БǒϧϢϔ\x98Лԑѵк\x90Ǽɿυ)ɛкнԢΏ,їҌʢǛ˱ʅѻȬĶ',
                    'monitors': [
                            {
                                        'identifier': 1985694,
                                        'width': -1222647569489979502,
                                        'height': 652196464604415365,
                                    },
                            {
                                        'identifier': 500686,
                                        'width': 8866084485696717731,
                                        'height': -1424304499758799078,
                                    },
                            {
                                        'identifier': 6369851,
                                        'width': -1203686577049556297,
                                        'height': -4180819655947410676,
                                    },
                            {
                                        'identifier': 6435117,
                                        'width': -2548190633268858047,
                                        'height': -3670749473323225663,
                                    },
                            {
                                        'identifier': -722848,
                                        'width': 623350268512855459,
                                        'height': 5917099730498913510,
                                    },
                            {
                                        'identifier': 8742858,
                                        'width': -2673873814265078326,
                                        'height': 7491964477975762169,
                                    },
                            {
                                        'identifier': 6231723,
                                        'width': 3516820577195824249,
                                        'height': 7448553290690993367,
                                    },
                            {
                                        'identifier': 1602082,
                                        'width': 7049426020782709308,
                                        'height': -5128996222597803962,
                                    },
                            {
                                        'identifier': 31575,
                                        'width': -5690622003245423672,
                                        'height': 7129979588375669415,
                                    },
                            {
                                        'identifier': 8503940,
                                        'width': -6664353253166198751,
                                        'height': 5071334973265180383,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2261505,
                                        'source_nw_x_pixel': -8687155484424152540,
                                        'source_nw_y_pixel': -8944516842711994397,
                                        'source_pixel_width': -8417218082269372173,
                                        'source_pixel_height': -5279218756033789102,
                                        'rotation': -4825817740598248169,
                                        'virtual_nw_x_pixel': 373858287,
                                        'virtual_nw_y_pixel': 312492671,
                                        'virtual_width': 240384512,
                                        'virtual_height': 1962742147,
                                    },
                            {
                                        'source_monitor': 2201026,
                                        'source_nw_x_pixel': -366743820976745871,
                                        'source_nw_y_pixel': -4322950899089872035,
                                        'source_pixel_width': -3021870586815057319,
                                        'source_pixel_height': -703126892327973713,
                                        'rotation': -7300164516233093163,
                                        'virtual_nw_x_pixel': -1080360554,
                                        'virtual_nw_y_pixel': 893809842,
                                        'virtual_width': 381300115,
                                        'virtual_height': -1785310268,
                                    },
                            {
                                        'source_monitor': 648664,
                                        'source_nw_x_pixel': -8297830262491875222,
                                        'source_nw_y_pixel': -6066894866196102826,
                                        'source_pixel_width': -3218283557206945153,
                                        'source_pixel_height': -6827204655901731443,
                                        'rotation': -7693174762008332850,
                                        'virtual_nw_x_pixel': 545869488,
                                        'virtual_nw_y_pixel': -991550690,
                                        'virtual_width': 273292432,
                                        'virtual_height': 13160023,
                                    },
                            {
                                        'source_monitor': 8218392,
                                        'source_nw_x_pixel': -1520007064487009381,
                                        'source_nw_y_pixel': -7549168391736215997,
                                        'source_pixel_width': -7628959607241960081,
                                        'source_pixel_height': -5322431797414913001,
                                        'rotation': -6095532551565618862,
                                        'virtual_nw_x_pixel': 227156307,
                                        'virtual_nw_y_pixel': -964758513,
                                        'virtual_width': -557604020,
                                        'virtual_height': 1736339815,
                                    },
                            {
                                        'source_monitor': -160952,
                                        'source_nw_x_pixel': -6964570015559858897,
                                        'source_nw_y_pixel': -7281358501767167482,
                                        'source_pixel_width': -3974095704888557012,
                                        'source_pixel_height': -5870600976015980266,
                                        'rotation': -3765441181874446093,
                                        'virtual_nw_x_pixel': -1289002394,
                                        'virtual_nw_y_pixel': -771447853,
                                        'virtual_width': 3842699,
                                        'virtual_height': -415097977,
                                    },
                            {
                                        'source_monitor': 1662009,
                                        'source_nw_x_pixel': -3136422081174160516,
                                        'source_nw_y_pixel': -4617859212165522439,
                                        'source_pixel_width': -3463734110780009135,
                                        'source_pixel_height': -691807065980442389,
                                        'rotation': -8503409757864112873,
                                        'virtual_nw_x_pixel': -411604278,
                                        'virtual_nw_y_pixel': 93432312,
                                        'virtual_width': -1470864630,
                                        'virtual_height': -168773031,
                                    },
                            {
                                        'source_monitor': 9000714,
                                        'source_nw_x_pixel': -4578854322134552274,
                                        'source_nw_y_pixel': -881603073119378860,
                                        'source_pixel_width': -8338537021704006318,
                                        'source_pixel_height': -7274372959714702872,
                                        'rotation': -888933951862774746,
                                        'virtual_nw_x_pixel': -787181510,
                                        'virtual_nw_y_pixel': -1130553857,
                                        'virtual_width': 55288321,
                                        'virtual_height': -1079670855,
                                    },
                            {
                                        'source_monitor': 7099239,
                                        'source_nw_x_pixel': -3176579442662856264,
                                        'source_nw_y_pixel': -4599546491133904387,
                                        'source_pixel_width': -3759051876052101269,
                                        'source_pixel_height': -8174635404137019733,
                                        'rotation': -5191500832310711800,
                                        'virtual_nw_x_pixel': 336407618,
                                        'virtual_nw_y_pixel': -22450925,
                                        'virtual_width': 1193080220,
                                        'virtual_height': -1689328812,
                                    },
                            {
                                        'source_monitor': 7537894,
                                        'source_nw_x_pixel': -3420184246480709880,
                                        'source_nw_y_pixel': -8116920392990602846,
                                        'source_pixel_width': -5884824398975924443,
                                        'source_pixel_height': -1539532836381848750,
                                        'rotation': -3012314684679732968,
                                        'virtual_nw_x_pixel': -1295545244,
                                        'virtual_nw_y_pixel': 767067342,
                                        'virtual_width': -1296336546,
                                        'virtual_height': -1265288261,
                                    },
                            {
                                        'source_monitor': 3563852,
                                        'source_nw_x_pixel': -5151347728543509126,
                                        'source_nw_y_pixel': -3590274051832409154,
                                        'source_pixel_width': -6207710642786572354,
                                        'source_pixel_height': -8656122714210442980,
                                        'rotation': -7521053235125208317,
                                        'virtual_nw_x_pixel': -1935590200,
                                        'virtual_nw_y_pixel': 1816492784,
                                        'virtual_width': -602192071,
                                        'virtual_height': 1738079804,
                                    },
                        ],
                },
                {
                    'description': 'щ˯ŬʔќѣȅƲļŭɊѯÈѶɴ˲τğҜЯʭъΔƃӌЏԈćʺǈ',
                    'monitors': [
                            {
                                        'identifier': 2407841,
                                        'width': -7336474438590911381,
                                        'height': 644689398426580036,
                                    },
                            {
                                        'identifier': 9814387,
                                        'width': -5145244404475902513,
                                        'height': -582687157030340939,
                                    },
                            {
                                        'identifier': 882127,
                                        'width': -3349562722429870963,
                                        'height': 7644711966962061013,
                                    },
                            {
                                        'identifier': 406220,
                                        'width': 7204690639218979787,
                                        'height': 3855600009141517020,
                                    },
                            {
                                        'identifier': 1885545,
                                        'width': -5600118881083789574,
                                        'height': 1380332604640911800,
                                    },
                            {
                                        'identifier': -497019,
                                        'width': 8837984603520774334,
                                        'height': 310086110178274998,
                                    },
                            {
                                        'identifier': 5179476,
                                        'width': -5063216058189516870,
                                        'height': -8308955517978264724,
                                    },
                            {
                                        'identifier': 6799933,
                                        'width': -3183776963981712624,
                                        'height': -629063752772904237,
                                    },
                            {
                                        'identifier': -896333,
                                        'width': 5105362485113112478,
                                        'height': -6187162425941355039,
                                    },
                            {
                                        'identifier': 3496710,
                                        'width': 2015792085074402418,
                                        'height': 5257066874497585406,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9769955,
                                        'source_nw_x_pixel': -138914115625977852,
                                        'source_nw_y_pixel': -3033056075740162942,
                                        'source_pixel_width': -1301328024480077190,
                                        'source_pixel_height': -1514045862802023522,
                                        'rotation': -3167535173564978902,
                                        'virtual_nw_x_pixel': -575697077,
                                        'virtual_nw_y_pixel': 1081852208,
                                        'virtual_width': 202316803,
                                        'virtual_height': 1639272726,
                                    },
                            {
                                        'source_monitor': 8944145,
                                        'source_nw_x_pixel': -245703902426131394,
                                        'source_nw_y_pixel': -6959289257425242017,
                                        'source_pixel_width': -7071469092631631863,
                                        'source_pixel_height': -406799245791619009,
                                        'rotation': -7517520600097639611,
                                        'virtual_nw_x_pixel': -886147573,
                                        'virtual_nw_y_pixel': -1420791063,
                                        'virtual_width': 1716371763,
                                        'virtual_height': -1923931219,
                                    },
                            {
                                        'source_monitor': -610259,
                                        'source_nw_x_pixel': -6626584142697086924,
                                        'source_nw_y_pixel': -3524051471987753164,
                                        'source_pixel_width': -1354875863961337225,
                                        'source_pixel_height': -3046062680510649112,
                                        'rotation': -479408098465702541,
                                        'virtual_nw_x_pixel': 108953571,
                                        'virtual_nw_y_pixel': -1550994494,
                                        'virtual_width': 944040741,
                                        'virtual_height': -1336829234,
                                    },
                            {
                                        'source_monitor': 4556583,
                                        'source_nw_x_pixel': -8693602787918418561,
                                        'source_nw_y_pixel': -461947715754732790,
                                        'source_pixel_width': -4529316175761049537,
                                        'source_pixel_height': -7107172689150648102,
                                        'rotation': -3140843525007609115,
                                        'virtual_nw_x_pixel': 1149278667,
                                        'virtual_nw_y_pixel': -564610321,
                                        'virtual_width': 1710451109,
                                        'virtual_height': -460640941,
                                    },
                            {
                                        'source_monitor': 80263,
                                        'source_nw_x_pixel': -8513728663202087832,
                                        'source_nw_y_pixel': -7331184512037480066,
                                        'source_pixel_width': -6760030527618333235,
                                        'source_pixel_height': -2109056768544381528,
                                        'rotation': -4811435669923409935,
                                        'virtual_nw_x_pixel': -354533026,
                                        'virtual_nw_y_pixel': -1806699255,
                                        'virtual_width': 54702471,
                                        'virtual_height': 1842884613,
                                    },
                            {
                                        'source_monitor': 7473723,
                                        'source_nw_x_pixel': -4254320377399803646,
                                        'source_nw_y_pixel': -3650829816268909793,
                                        'source_pixel_width': -5889338924270950214,
                                        'source_pixel_height': -7719226664479224895,
                                        'rotation': -1852462091929480599,
                                        'virtual_nw_x_pixel': 712933833,
                                        'virtual_nw_y_pixel': -982730184,
                                        'virtual_width': 1058665017,
                                        'virtual_height': 1981156249,
                                    },
                            {
                                        'source_monitor': 180809,
                                        'source_nw_x_pixel': -7363304618530768490,
                                        'source_nw_y_pixel': -4972634771960120664,
                                        'source_pixel_width': -209494043844034716,
                                        'source_pixel_height': -6253917291737206591,
                                        'rotation': -774791417934408534,
                                        'virtual_nw_x_pixel': 1909696426,
                                        'virtual_nw_y_pixel': -1375361456,
                                        'virtual_width': 1354229745,
                                        'virtual_height': -1912359480,
                                    },
                            {
                                        'source_monitor': 7057249,
                                        'source_nw_x_pixel': -580930227211679775,
                                        'source_nw_y_pixel': -8171093841689369222,
                                        'source_pixel_width': -8202858972289696054,
                                        'source_pixel_height': -2922675627925544313,
                                        'rotation': -3074071361752542361,
                                        'virtual_nw_x_pixel': 278605555,
                                        'virtual_nw_y_pixel': -1285665118,
                                        'virtual_width': 1094099940,
                                        'virtual_height': -795322416,
                                    },
                            {
                                        'source_monitor': 5472544,
                                        'source_nw_x_pixel': -6600027303411400656,
                                        'source_nw_y_pixel': -6674160414714221884,
                                        'source_pixel_width': -8275105581739253023,
                                        'source_pixel_height': -162613146107687044,
                                        'rotation': -7395226111583934525,
                                        'virtual_nw_x_pixel': 1885993102,
                                        'virtual_nw_y_pixel': 1428843212,
                                        'virtual_width': 897010032,
                                        'virtual_height': -1153587582,
                                    },
                            {
                                        'source_monitor': 9604270,
                                        'source_nw_x_pixel': -3701398280262088380,
                                        'source_nw_y_pixel': -2529424688319906411,
                                        'source_pixel_width': -7573188278543855220,
                                        'source_pixel_height': -4671880025376004766,
                                        'rotation': -107366175790897306,
                                        'virtual_nw_x_pixel': -1395142284,
                                        'virtual_nw_y_pixel': 723664902,
                                        'virtual_width': 418167101,
                                        'virtual_height': -790141699,
                                    },
                        ],
                },
                {
                    'description': 'NĮʔțӯÏΞKƫÑѸ\x98Ǣ«˕ªɈÓҐɸͲˍӒӛƲ%ѿѠǖԧ',
                    'monitors': [
                            {
                                        'identifier': -351656,
                                        'width': 826604346486307489,
                                        'height': -6231915105629718215,
                                    },
                            {
                                        'identifier': 3082254,
                                        'width': 6802063713564380587,
                                        'height': 4610718745150572814,
                                    },
                            {
                                        'identifier': 9565221,
                                        'width': -6614959032124610665,
                                        'height': -900221250769819901,
                                    },
                            {
                                        'identifier': -455085,
                                        'width': 4811592315078202713,
                                        'height': 6417245192484983093,
                                    },
                            {
                                        'identifier': 5221592,
                                        'width': -8327953093574591888,
                                        'height': 4283542775590326553,
                                    },
                            {
                                        'identifier': 7479825,
                                        'width': -7759540445471700998,
                                        'height': 6526162324035061262,
                                    },
                            {
                                        'identifier': 2618980,
                                        'width': -6840904780253091037,
                                        'height': -793643999142113189,
                                    },
                            {
                                        'identifier': 5762022,
                                        'width': 934650832610254884,
                                        'height': -3362073198254392836,
                                    },
                            {
                                        'identifier': 3519274,
                                        'width': 1521989681902648656,
                                        'height': -8826172819823936153,
                                    },
                            {
                                        'identifier': 4957252,
                                        'width': -2717376600575931624,
                                        'height': 8223499669702288370,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5759459,
                                        'source_nw_x_pixel': -5815748965744923384,
                                        'source_nw_y_pixel': -6865383674983425530,
                                        'source_pixel_width': -7564748013470395176,
                                        'source_pixel_height': -6574858625518622355,
                                        'rotation': -2128149996992856753,
                                        'virtual_nw_x_pixel': -1015696682,
                                        'virtual_nw_y_pixel': -234167439,
                                        'virtual_width': -317058348,
                                        'virtual_height': -530069150,
                                    },
                            {
                                        'source_monitor': 131332,
                                        'source_nw_x_pixel': -8201251766680130673,
                                        'source_nw_y_pixel': -1668855378632565572,
                                        'source_pixel_width': -2644734001472589767,
                                        'source_pixel_height': -8158299507909077951,
                                        'rotation': -1494816709637653746,
                                        'virtual_nw_x_pixel': 1483123595,
                                        'virtual_nw_y_pixel': -410049217,
                                        'virtual_width': -430138597,
                                        'virtual_height': -364309745,
                                    },
                            {
                                        'source_monitor': 5085730,
                                        'source_nw_x_pixel': -953225860583429210,
                                        'source_nw_y_pixel': -5148674220799652943,
                                        'source_pixel_width': -4422653519162939455,
                                        'source_pixel_height': -1893533867671224780,
                                        'rotation': -4967621409805794078,
                                        'virtual_nw_x_pixel': -596992569,
                                        'virtual_nw_y_pixel': -1529013191,
                                        'virtual_width': 219494219,
                                        'virtual_height': -706035437,
                                    },
                            {
                                        'source_monitor': 9978886,
                                        'source_nw_x_pixel': -4824003337480776470,
                                        'source_nw_y_pixel': -8841703738433466833,
                                        'source_pixel_width': -2644147123018002821,
                                        'source_pixel_height': -4183796367209983668,
                                        'rotation': -8685127777288877317,
                                        'virtual_nw_x_pixel': -228132322,
                                        'virtual_nw_y_pixel': 181198999,
                                        'virtual_width': -1863989440,
                                        'virtual_height': -646105817,
                                    },
                            {
                                        'source_monitor': 8420159,
                                        'source_nw_x_pixel': -6276690820994706918,
                                        'source_nw_y_pixel': -4503575311461616435,
                                        'source_pixel_width': -3416301169941673183,
                                        'source_pixel_height': -5923324384732263897,
                                        'rotation': -4426308630106235848,
                                        'virtual_nw_x_pixel': -616181197,
                                        'virtual_nw_y_pixel': -390284355,
                                        'virtual_width': 117874480,
                                        'virtual_height': 1690291630,
                                    },
                            {
                                        'source_monitor': -252220,
                                        'source_nw_x_pixel': -5078596853079775548,
                                        'source_nw_y_pixel': -6328829709854030342,
                                        'source_pixel_width': -6763375846727953154,
                                        'source_pixel_height': -5894762108812289652,
                                        'rotation': -2669489789440500095,
                                        'virtual_nw_x_pixel': 127557995,
                                        'virtual_nw_y_pixel': 967189901,
                                        'virtual_width': -462954375,
                                        'virtual_height': 1721918348,
                                    },
                            {
                                        'source_monitor': 9096208,
                                        'source_nw_x_pixel': -5936150674647872703,
                                        'source_nw_y_pixel': -1447408859866514573,
                                        'source_pixel_width': -7547101487298705147,
                                        'source_pixel_height': -4225779907983755847,
                                        'rotation': -7602300571266222357,
                                        'virtual_nw_x_pixel': 573247756,
                                        'virtual_nw_y_pixel': -1122236093,
                                        'virtual_width': 513271597,
                                        'virtual_height': -319658766,
                                    },
                            {
                                        'source_monitor': 3623964,
                                        'source_nw_x_pixel': -6203282413900289994,
                                        'source_nw_y_pixel': -7319632451267785354,
                                        'source_pixel_width': -8746093760277949927,
                                        'source_pixel_height': -4795762284738663349,
                                        'rotation': -383706573164968606,
                                        'virtual_nw_x_pixel': 1671516319,
                                        'virtual_nw_y_pixel': 1262466839,
                                        'virtual_width': 582451458,
                                        'virtual_height': 1238869913,
                                    },
                            {
                                        'source_monitor': 6103627,
                                        'source_nw_x_pixel': -6233854589956523633,
                                        'source_nw_y_pixel': -8547943007518494930,
                                        'source_pixel_width': -7668968495306827070,
                                        'source_pixel_height': -3586724826042982917,
                                        'rotation': -9128247544634268462,
                                        'virtual_nw_x_pixel': -280201581,
                                        'virtual_nw_y_pixel': -1147865449,
                                        'virtual_width': -1788565610,
                                        'virtual_height': 1986748136,
                                    },
                            {
                                        'source_monitor': 881301,
                                        'source_nw_x_pixel': -827446649356582146,
                                        'source_nw_y_pixel': -5961410368757123193,
                                        'source_pixel_width': -3334712118672908721,
                                        'source_pixel_height': -2996636564562902502,
                                        'rotation': -2350527576143628991,
                                        'virtual_nw_x_pixel': -605890604,
                                        'virtual_nw_y_pixel': 1460683488,
                                        'virtual_width': 1655986592,
                                        'virtual_height': 77717368,
                                    },
                        ],
                },
                {
                    'description': 'YѹӞӀǓʖͶmQłӵ˨ρȩʛ¹ӍыέΐtʇǳĔϕ\x9d˽ʿǞҧ',
                    'monitors': [
                            {
                                        'identifier': 5809146,
                                        'width': 6765279789094168575,
                                        'height': -250430411841745981,
                                    },
                            {
                                        'identifier': 382281,
                                        'width': 5561948495782930454,
                                        'height': -8721337465594626601,
                                    },
                            {
                                        'identifier': 8288261,
                                        'width': -7090651019553355279,
                                        'height': -8163322960436923360,
                                    },
                            {
                                        'identifier': 4024294,
                                        'width': 8299829173428050627,
                                        'height': 3173871928873910600,
                                    },
                            {
                                        'identifier': 6790103,
                                        'width': 7734486257386423983,
                                        'height': -1418701761796607384,
                                    },
                            {
                                        'identifier': 5547680,
                                        'width': 4067991285919158941,
                                        'height': -7167975180379918289,
                                    },
                            {
                                        'identifier': 1476356,
                                        'width': 1533915446461182599,
                                        'height': 5197327423718443851,
                                    },
                            {
                                        'identifier': 8161048,
                                        'width': -6477492665725521660,
                                        'height': -7576781470962204259,
                                    },
                            {
                                        'identifier': 4466628,
                                        'width': -385405115993105524,
                                        'height': 1634228556788480389,
                                    },
                            {
                                        'identifier': 8781093,
                                        'width': -5798552481459065990,
                                        'height': -6917625933415428964,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2690363,
                                        'source_nw_x_pixel': -6018666929449465056,
                                        'source_nw_y_pixel': -7400838652056175276,
                                        'source_pixel_width': -2147779018385056865,
                                        'source_pixel_height': -6961673931728221023,
                                        'rotation': -6178581534489131889,
                                        'virtual_nw_x_pixel': 1438288262,
                                        'virtual_nw_y_pixel': 1760053444,
                                        'virtual_width': -554746197,
                                        'virtual_height': 552534855,
                                    },
                            {
                                        'source_monitor': 9969416,
                                        'source_nw_x_pixel': -1913053022852571974,
                                        'source_nw_y_pixel': -5852831272406590287,
                                        'source_pixel_width': -3671241448353408819,
                                        'source_pixel_height': -4142819811855954203,
                                        'rotation': -5679310418307651603,
                                        'virtual_nw_x_pixel': -464104773,
                                        'virtual_nw_y_pixel': -1144940599,
                                        'virtual_width': -1517230700,
                                        'virtual_height': -358352082,
                                    },
                            {
                                        'source_monitor': -117922,
                                        'source_nw_x_pixel': -1305708405538984321,
                                        'source_nw_y_pixel': -6663264174631288254,
                                        'source_pixel_width': -2259986396769571779,
                                        'source_pixel_height': -6276733458636529756,
                                        'rotation': -3830323704852996721,
                                        'virtual_nw_x_pixel': -1096931270,
                                        'virtual_nw_y_pixel': -479478368,
                                        'virtual_width': -1239373086,
                                        'virtual_height': -1616569454,
                                    },
                            {
                                        'source_monitor': 153115,
                                        'source_nw_x_pixel': -5130459234137636779,
                                        'source_nw_y_pixel': -5167781406088605652,
                                        'source_pixel_width': -5941606267453778310,
                                        'source_pixel_height': -8979918255356617184,
                                        'rotation': -6757491231832385597,
                                        'virtual_nw_x_pixel': 484472204,
                                        'virtual_nw_y_pixel': 415603048,
                                        'virtual_width': -1941045346,
                                        'virtual_height': 545356484,
                                    },
                            {
                                        'source_monitor': 3869590,
                                        'source_nw_x_pixel': -6050810930526723189,
                                        'source_nw_y_pixel': -2217750973311528886,
                                        'source_pixel_width': -2410024051983972647,
                                        'source_pixel_height': -3577067075737054266,
                                        'rotation': -3177839228827963043,
                                        'virtual_nw_x_pixel': -440613202,
                                        'virtual_nw_y_pixel': -1962831116,
                                        'virtual_width': -455692328,
                                        'virtual_height': -542327266,
                                    },
                            {
                                        'source_monitor': 1066756,
                                        'source_nw_x_pixel': -1283871018436342101,
                                        'source_nw_y_pixel': -5103130878509528661,
                                        'source_pixel_width': -8947901194560815546,
                                        'source_pixel_height': -2687033563519883619,
                                        'rotation': -5867975774947700661,
                                        'virtual_nw_x_pixel': 427015999,
                                        'virtual_nw_y_pixel': 1148317584,
                                        'virtual_width': 401607832,
                                        'virtual_height': -1549670913,
                                    },
                            {
                                        'source_monitor': 4242044,
                                        'source_nw_x_pixel': -6103026203375650900,
                                        'source_nw_y_pixel': -3763826963576382743,
                                        'source_pixel_width': -6096685766400020234,
                                        'source_pixel_height': -3965199951656622865,
                                        'rotation': -4990562219714826385,
                                        'virtual_nw_x_pixel': -865149260,
                                        'virtual_nw_y_pixel': -247392317,
                                        'virtual_width': -54121418,
                                        'virtual_height': 1703006749,
                                    },
                            {
                                        'source_monitor': -130453,
                                        'source_nw_x_pixel': -6997728807765501981,
                                        'source_nw_y_pixel': -8812929396352376137,
                                        'source_pixel_width': -5497622999987049080,
                                        'source_pixel_height': -1394328516315115037,
                                        'rotation': -990715316628190196,
                                        'virtual_nw_x_pixel': -1204720367,
                                        'virtual_nw_y_pixel': -392623551,
                                        'virtual_width': -680849880,
                                        'virtual_height': 187551587,
                                    },
                            {
                                        'source_monitor': 5397726,
                                        'source_nw_x_pixel': -6505026718622721581,
                                        'source_nw_y_pixel': -1748453135597384782,
                                        'source_pixel_width': -1998583035799009445,
                                        'source_pixel_height': -1544153453991080627,
                                        'rotation': -2437268189638492224,
                                        'virtual_nw_x_pixel': -43408266,
                                        'virtual_nw_y_pixel': -1865885833,
                                        'virtual_width': -131582320,
                                        'virtual_height': 1688940044,
                                    },
                            {
                                        'source_monitor': 779453,
                                        'source_nw_x_pixel': -4631135280879006081,
                                        'source_nw_y_pixel': -4258661959306313526,
                                        'source_pixel_width': -6008627319833591903,
                                        'source_pixel_height': -7063193171843607069,
                                        'rotation': -3871612131694042249,
                                        'virtual_nw_x_pixel': -484301835,
                                        'virtual_nw_y_pixel': -729081880,
                                        'virtual_width': -1754824898,
                                        'virtual_height': 910394464,
                                    },
                        ],
                },
                {
                    'description': 'ʖȼʘƆíАЅЋˍʉѥαʶ>ɡȕΙӳʂȽɔҾ˛ԃœϑѝǦDΨ',
                    'monitors': [
                            {
                                        'identifier': -119991,
                                        'width': -6514366769158189148,
                                        'height': 8575483706067460439,
                                    },
                            {
                                        'identifier': 8008055,
                                        'width': 7277001875434105641,
                                        'height': -8260224472721510686,
                                    },
                            {
                                        'identifier': 1852337,
                                        'width': 6607808251105038373,
                                        'height': -8765861327138880481,
                                    },
                            {
                                        'identifier': 466280,
                                        'width': 5448793535036547650,
                                        'height': 4593186484254394150,
                                    },
                            {
                                        'identifier': 4819367,
                                        'width': 5562135741612199121,
                                        'height': -7146838006575052919,
                                    },
                            {
                                        'identifier': 8201896,
                                        'width': -4460714874502344647,
                                        'height': -8311691116592355154,
                                    },
                            {
                                        'identifier': 3991727,
                                        'width': -6747439183186625684,
                                        'height': 3562418735802626611,
                                    },
                            {
                                        'identifier': 6198817,
                                        'width': 4135333743745385981,
                                        'height': 124922416878447474,
                                    },
                            {
                                        'identifier': 266921,
                                        'width': 3844496551041305096,
                                        'height': 1077462165115426531,
                                    },
                            {
                                        'identifier': 4684191,
                                        'width': -5372333854294753057,
                                        'height': -6328855048867103002,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3437810,
                                        'source_nw_x_pixel': -4619640410974193422,
                                        'source_nw_y_pixel': -9014095444909331111,
                                        'source_pixel_width': -3636968026200964639,
                                        'source_pixel_height': -6256545678295078839,
                                        'rotation': -4742894917799937736,
                                        'virtual_nw_x_pixel': 232299566,
                                        'virtual_nw_y_pixel': 669590011,
                                        'virtual_width': -1174443433,
                                        'virtual_height': -672962251,
                                    },
                            {
                                        'source_monitor': 1370181,
                                        'source_nw_x_pixel': -8022867151885438544,
                                        'source_nw_y_pixel': -983036176770997302,
                                        'source_pixel_width': -21661999937848319,
                                        'source_pixel_height': -1133288707757092570,
                                        'rotation': -758015913938424973,
                                        'virtual_nw_x_pixel': -1344101936,
                                        'virtual_nw_y_pixel': 237568429,
                                        'virtual_width': -744506925,
                                        'virtual_height': -1644275187,
                                    },
                            {
                                        'source_monitor': 6014928,
                                        'source_nw_x_pixel': -3153309387066811994,
                                        'source_nw_y_pixel': -4307891537753290454,
                                        'source_pixel_width': -1082953210863054415,
                                        'source_pixel_height': -7143639144275850258,
                                        'rotation': -5180743180870453659,
                                        'virtual_nw_x_pixel': -1916795065,
                                        'virtual_nw_y_pixel': -178373399,
                                        'virtual_width': -676668242,
                                        'virtual_height': 554838319,
                                    },
                            {
                                        'source_monitor': 8081076,
                                        'source_nw_x_pixel': -4990608936568971152,
                                        'source_nw_y_pixel': -4414897742079842403,
                                        'source_pixel_width': -8739149208185053672,
                                        'source_pixel_height': -8563808076605608368,
                                        'rotation': -1094543601509572108,
                                        'virtual_nw_x_pixel': -1499099911,
                                        'virtual_nw_y_pixel': -1060519114,
                                        'virtual_width': -1654382921,
                                        'virtual_height': 1292367462,
                                    },
                            {
                                        'source_monitor': 8611368,
                                        'source_nw_x_pixel': -2888795716842785324,
                                        'source_nw_y_pixel': -6031094992378876777,
                                        'source_pixel_width': -4205717647122078841,
                                        'source_pixel_height': -5328434087110143930,
                                        'rotation': -2337109526307967946,
                                        'virtual_nw_x_pixel': 200839612,
                                        'virtual_nw_y_pixel': 1417794223,
                                        'virtual_width': -1174129671,
                                        'virtual_height': -1712507829,
                                    },
                            {
                                        'source_monitor': 8161476,
                                        'source_nw_x_pixel': -3794991556747281610,
                                        'source_nw_y_pixel': -1457653708676339363,
                                        'source_pixel_width': -4851167241635923342,
                                        'source_pixel_height': -2478655169781729154,
                                        'rotation': -1163653549671285855,
                                        'virtual_nw_x_pixel': 1961034514,
                                        'virtual_nw_y_pixel': -144508383,
                                        'virtual_width': 781353624,
                                        'virtual_height': 220636214,
                                    },
                            {
                                        'source_monitor': 8559274,
                                        'source_nw_x_pixel': -374336847152339095,
                                        'source_nw_y_pixel': -3666127871603506616,
                                        'source_pixel_width': -6787807596084501052,
                                        'source_pixel_height': -6327600898668244135,
                                        'rotation': -6920834106944741757,
                                        'virtual_nw_x_pixel': 1094872512,
                                        'virtual_nw_y_pixel': 1923404612,
                                        'virtual_width': -38890162,
                                        'virtual_height': -994961847,
                                    },
                            {
                                        'source_monitor': 9437940,
                                        'source_nw_x_pixel': -1393292537994663309,
                                        'source_nw_y_pixel': -4030864353350639967,
                                        'source_pixel_width': -5403427240802912454,
                                        'source_pixel_height': -682149336527362853,
                                        'rotation': -6429338412660871877,
                                        'virtual_nw_x_pixel': -1936617362,
                                        'virtual_nw_y_pixel': 825061328,
                                        'virtual_width': -1682611667,
                                        'virtual_height': -1174873236,
                                    },
                            {
                                        'source_monitor': 3034839,
                                        'source_nw_x_pixel': -7570039251992492118,
                                        'source_nw_y_pixel': -2544936809112811388,
                                        'source_pixel_width': -6028881661090382424,
                                        'source_pixel_height': -1486004565669407794,
                                        'rotation': -1714222249811026792,
                                        'virtual_nw_x_pixel': -1134617970,
                                        'virtual_nw_y_pixel': 1971285699,
                                        'virtual_width': 530715177,
                                        'virtual_height': -40580179,
                                    },
                            {
                                        'source_monitor': 5123133,
                                        'source_nw_x_pixel': -4839324552589393650,
                                        'source_nw_y_pixel': -6439180305048063559,
                                        'source_pixel_width': -3524881394805506393,
                                        'source_pixel_height': -7945602119658140821,
                                        'rotation': -6487884574227138264,
                                        'virtual_nw_x_pixel': 857517059,
                                        'virtual_nw_y_pixel': -241457425,
                                        'virtual_width': 1976747649,
                                        'virtual_height': 1261391544,
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
                                        'identifier': 9639463,
                                        'width': 6557800145441559918,
                                        'height': -5410802196199809276,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -599547502064361230,
                                        'source_nw_y_pixel': -481941851375865842,
                                        'source_pixel_width': -4121357659733337639,
                                        'source_pixel_height': -2732112486517146095,
                                        'rotation': -7547597186876727521,
                                        'virtual_nw_x_pixel': 1387819225,
                                        'virtual_nw_y_pixel': 627688393,
                                        'virtual_width': 720564880,
                                        'virtual_height': -1627367304,
                                    },
                        ],
                },
            ],

        },
    ),
]
