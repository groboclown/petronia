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
            'nw_x_pixel': -1470166298,
            'nw_y_pixel': 846572606,
            'width': -4740495063329432494,
            'height': -4095874251214759422,
            'ratio_x': -788539477809373212,
            'ratio_y': -6859780141004029958,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -938786941,

            'nw_y_pixel': 1091808303,

            'width': -3771944640349328652,

            'height': -1359076892756791160,

            'ratio_x': -7582897815682890422,

            'ratio_y': 715517630092271364,

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
                    'nw_x_pixel': -1748764861,
                    'nw_y_pixel': -918944477,
                    'width': -357703208382288459,
                    'height': -3447715106616211166,
                    'ratio_x': 5409965332439501870,
                    'ratio_y': 4060311424266721463,
                },
                {
                    'nw_x_pixel': 237168769,
                    'nw_y_pixel': 306501979,
                    'width': -5841731329504437992,
                    'height': -5602991076946453652,
                    'ratio_x': -75372675695256072,
                    'ratio_y': 2229439901600182679,
                },
                {
                    'nw_x_pixel': 1616032571,
                    'nw_y_pixel': -47071618,
                    'width': -8250439200650436139,
                    'height': -8065985790366673776,
                    'ratio_x': -7018862880078626967,
                    'ratio_y': 8729070633946042814,
                },
                {
                    'nw_x_pixel': -1124670446,
                    'nw_y_pixel': -70123756,
                    'width': -5991998789703709205,
                    'height': -7269881838043124198,
                    'ratio_x': -2086053881225795573,
                    'ratio_y': 6058462734684601783,
                },
                {
                    'nw_x_pixel': 117931661,
                    'nw_y_pixel': 404693021,
                    'width': -4016967957823536383,
                    'height': -619428106157169203,
                    'ratio_x': 6236713375660915523,
                    'ratio_y': -6122842779223649905,
                },
                {
                    'nw_x_pixel': -875982768,
                    'nw_y_pixel': -710438648,
                    'width': -5990501716187187196,
                    'height': -3405186025828782546,
                    'ratio_x': 3778392478545265160,
                    'ratio_y': -2441196200335854094,
                },
                {
                    'nw_x_pixel': 1839618033,
                    'nw_y_pixel': -1510967377,
                    'width': -3337495596592782211,
                    'height': -9172679674618825808,
                    'ratio_x': 3500933098677889156,
                    'ratio_y': 8743926518843974688,
                },
                {
                    'nw_x_pixel': 1430729515,
                    'nw_y_pixel': -641416515,
                    'width': -4264155961791745345,
                    'height': -1726726315610413106,
                    'ratio_x': -392006667580893612,
                    'ratio_y': -4596520213014068024,
                },
                {
                    'nw_x_pixel': -276283747,
                    'nw_y_pixel': -333819135,
                    'width': -6367066804811252267,
                    'height': -6556068162450862796,
                    'ratio_x': -3457374858946736265,
                    'ratio_y': 4188341767900465844,
                },
                {
                    'nw_x_pixel': -1558434836,
                    'nw_y_pixel': -107251862,
                    'width': -872112629033274302,
                    'height': -1713705751096417633,
                    'ratio_x': -4957560112301142742,
                    'ratio_y': -4786738895251933443,
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
            'identifier': 4267202,
            'width': 5553660433741653524,
            'height': -8323551817910997973,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 8021686,

            'width': 7424842730150383592,

            'height': 3877802319548660551,

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
            'source_monitor': 5829768,
            'source_nw_x_pixel': -3120798694033050895,
            'source_nw_y_pixel': -1769585714633087918,
            'source_pixel_width': -8950492720260528210,
            'source_pixel_height': -8383614151863647958,
            'rotation': -5623662867428945676,
            'virtual_nw_x_pixel': 1175126109,
            'virtual_nw_y_pixel': -651266263,
            'virtual_width': 173570982,
            'virtual_height': 1303199928,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -3128937947107823632,

            'source_nw_y_pixel': -3734366302568438110,

            'source_pixel_width': -5200707156425246855,

            'source_pixel_height': -8683368084712552035,

            'rotation': -8127431292726576450,

            'virtual_nw_x_pixel': -1899478965,

            'virtual_nw_y_pixel': -75375345,

            'virtual_width': -816199416,

            'virtual_height': 1621853225,

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
            'description': 'ϑ\x8bΧΡΟʽѴǿˢϷQ\x85ѰńʍͷĎũƷϪǧȈõѕѦͻ\u03a2ņυљ',
            'monitors': [
                {
                    'identifier': 9477410,
                    'width': 2380615472219600247,
                    'height': -2134640373500268376,
                },
                {
                    'identifier': 7309116,
                    'width': -2955239956736737494,
                    'height': -8356786814132632587,
                },
                {
                    'identifier': 7257553,
                    'width': -7270038891166739165,
                    'height': -455162461128613795,
                },
                {
                    'identifier': 6388316,
                    'width': -1585096907948754041,
                    'height': -4242223005108576148,
                },
                {
                    'identifier': 2023720,
                    'width': 6342728050508328184,
                    'height': -8277258812630237928,
                },
                {
                    'identifier': 62767,
                    'width': -8424993095785655106,
                    'height': -1118406037899811844,
                },
                {
                    'identifier': 4319520,
                    'width': 5798356402489396270,
                    'height': 5148928845711946986,
                },
                {
                    'identifier': 4826543,
                    'width': -4458934192106990839,
                    'height': -4281556153991518580,
                },
                {
                    'identifier': 6466817,
                    'width': 9183795578657118889,
                    'height': 5104143274796475246,
                },
                {
                    'identifier': 4142762,
                    'width': -1906555932314529869,
                    'height': 5165931688507225935,
                },
            ],
            'screen': [
                {
                    'source_monitor': 9071509,
                    'source_nw_x_pixel': -9042318810364873733,
                    'source_nw_y_pixel': -1730350939824222119,
                    'source_pixel_width': -3301829593558147801,
                    'source_pixel_height': -8684562597391423217,
                    'rotation': -3589109964771727344,
                    'virtual_nw_x_pixel': -1983962179,
                    'virtual_nw_y_pixel': 1945161293,
                    'virtual_width': 649642690,
                    'virtual_height': -132156425,
                },
                {
                    'source_monitor': -889710,
                    'source_nw_x_pixel': -4949016610348383544,
                    'source_nw_y_pixel': -345148420336122539,
                    'source_pixel_width': -4744378060986916041,
                    'source_pixel_height': -6376034976643067202,
                    'rotation': -1543243859297909455,
                    'virtual_nw_x_pixel': -1040716210,
                    'virtual_nw_y_pixel': 1287138166,
                    'virtual_width': -1871794580,
                    'virtual_height': -745922160,
                },
                {
                    'source_monitor': 4853452,
                    'source_nw_x_pixel': -9035396609544820635,
                    'source_nw_y_pixel': -3946849866380998658,
                    'source_pixel_width': -516692745624996793,
                    'source_pixel_height': -8891550262096265288,
                    'rotation': -2465641874254240879,
                    'virtual_nw_x_pixel': 378572334,
                    'virtual_nw_y_pixel': -754183659,
                    'virtual_width': -1346182693,
                    'virtual_height': 1851912317,
                },
                {
                    'source_monitor': 9670705,
                    'source_nw_x_pixel': -6800861577560307738,
                    'source_nw_y_pixel': -9209933559142318123,
                    'source_pixel_width': -974583291624915155,
                    'source_pixel_height': -6431594874472243685,
                    'rotation': -8453407130241037574,
                    'virtual_nw_x_pixel': 1626225093,
                    'virtual_nw_y_pixel': 35496617,
                    'virtual_width': -1358955710,
                    'virtual_height': 578197592,
                },
                {
                    'source_monitor': 273831,
                    'source_nw_x_pixel': -3607461186687473846,
                    'source_nw_y_pixel': -4236612975046035327,
                    'source_pixel_width': -4138781182479404064,
                    'source_pixel_height': -4742697884833516666,
                    'rotation': -6791944084394992579,
                    'virtual_nw_x_pixel': -48147960,
                    'virtual_nw_y_pixel': 110769569,
                    'virtual_width': -1781913366,
                    'virtual_height': 1579118243,
                },
                {
                    'source_monitor': 1455940,
                    'source_nw_x_pixel': -342254028143980753,
                    'source_nw_y_pixel': -7968033014706266002,
                    'source_pixel_width': -6157769158352506322,
                    'source_pixel_height': -3257577383739214941,
                    'rotation': -519658647363000892,
                    'virtual_nw_x_pixel': -1174085946,
                    'virtual_nw_y_pixel': -835733093,
                    'virtual_width': -1649533852,
                    'virtual_height': -160188367,
                },
                {
                    'source_monitor': 8116223,
                    'source_nw_x_pixel': -2134992829380830685,
                    'source_nw_y_pixel': -384806018881187226,
                    'source_pixel_width': -1490404971136064617,
                    'source_pixel_height': -4938136730016543529,
                    'rotation': -2163965763753759494,
                    'virtual_nw_x_pixel': -1620151748,
                    'virtual_nw_y_pixel': 1031368486,
                    'virtual_width': 1978935590,
                    'virtual_height': -213308482,
                },
                {
                    'source_monitor': 4555675,
                    'source_nw_x_pixel': -7143839536546707058,
                    'source_nw_y_pixel': -5668674683685477879,
                    'source_pixel_width': -3025625095567136292,
                    'source_pixel_height': -4008188682749436013,
                    'rotation': -763561390732103818,
                    'virtual_nw_x_pixel': 359733493,
                    'virtual_nw_y_pixel': -521874476,
                    'virtual_width': -1190087694,
                    'virtual_height': -1312321898,
                },
                {
                    'source_monitor': 7055194,
                    'source_nw_x_pixel': -7017078569885031582,
                    'source_nw_y_pixel': -8703815361463138283,
                    'source_pixel_width': -1073887068441728901,
                    'source_pixel_height': -6654529492000897639,
                    'rotation': -1573441120305462647,
                    'virtual_nw_x_pixel': -1392467574,
                    'virtual_nw_y_pixel': -981498658,
                    'virtual_width': -916639685,
                    'virtual_height': -980248148,
                },
                {
                    'source_monitor': 4651129,
                    'source_nw_x_pixel': -6896544244952207912,
                    'source_nw_y_pixel': -5550809486174664618,
                    'source_pixel_width': -6726710388186212776,
                    'source_pixel_height': -1567729237632945625,
                    'rotation': -6941748688702653542,
                    'virtual_nw_x_pixel': -1848616091,
                    'virtual_nw_y_pixel': -17247791,
                    'virtual_width': -1134297825,
                    'virtual_height': -23414400,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 4747144,
                    'width': 5579986027160974672,
                    'height': 8906000939610799292,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -6839591474082244850,
                    'source_nw_y_pixel': -4886058638232213324,
                    'source_pixel_width': -8373879511963447871,
                    'source_pixel_height': -366586593835387430,
                    'rotation': -8383447811503130931,
                    'virtual_nw_x_pixel': 1786486505,
                    'virtual_nw_y_pixel': 830770322,
                    'virtual_width': -1527527283,
                    'virtual_height': 776444203,
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
                    'description': 'ʢKJ˯ξ҉˹ʊҷ˞Ɔ҇¸ΆԩѰǬτɯ.ʤú΅ЗҼ˞Ă\xadЖҜ',
                    'monitors': [
                            {
                                        'identifier': -984747,
                                        'width': 3748885635848291601,
                                        'height': -5590050490123841562,
                                    },
                            {
                                        'identifier': 2744299,
                                        'width': -1011730265535463042,
                                        'height': -7199837087124051900,
                                    },
                            {
                                        'identifier': 314553,
                                        'width': 7643794147494743427,
                                        'height': -1193004992105018636,
                                    },
                            {
                                        'identifier': 6150188,
                                        'width': -7846103972345743627,
                                        'height': -5470150240398193727,
                                    },
                            {
                                        'identifier': 6058611,
                                        'width': -6459519681434261486,
                                        'height': -5651419411813350052,
                                    },
                            {
                                        'identifier': 2936535,
                                        'width': 6687049072903923183,
                                        'height': 6389095364422011383,
                                    },
                            {
                                        'identifier': 5627228,
                                        'width': 7299126965336408591,
                                        'height': 8342793589754059907,
                                    },
                            {
                                        'identifier': 5109853,
                                        'width': -1402885012395484471,
                                        'height': -7507658362589495115,
                                    },
                            {
                                        'identifier': 7247886,
                                        'width': 1194547642435801293,
                                        'height': -253437588754647570,
                                    },
                            {
                                        'identifier': 6328361,
                                        'width': -7802527125993489980,
                                        'height': -8675966358255522390,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4952887,
                                        'source_nw_x_pixel': -4442900913333622936,
                                        'source_nw_y_pixel': -6892106070018277187,
                                        'source_pixel_width': -4052802121583194589,
                                        'source_pixel_height': -8307331093927287938,
                                        'rotation': -7786918891477487672,
                                        'virtual_nw_x_pixel': 625726938,
                                        'virtual_nw_y_pixel': -277751911,
                                        'virtual_width': 895692356,
                                        'virtual_height': -391702739,
                                    },
                            {
                                        'source_monitor': 3490205,
                                        'source_nw_x_pixel': -7235082455840524198,
                                        'source_nw_y_pixel': -8074250998321337686,
                                        'source_pixel_width': -6265921679506676284,
                                        'source_pixel_height': -4959640839712799394,
                                        'rotation': -6699139577929464376,
                                        'virtual_nw_x_pixel': 812908309,
                                        'virtual_nw_y_pixel': -1032639493,
                                        'virtual_width': -1224036858,
                                        'virtual_height': 632084119,
                                    },
                            {
                                        'source_monitor': 6067621,
                                        'source_nw_x_pixel': -4221050162177185644,
                                        'source_nw_y_pixel': -3431699324957752810,
                                        'source_pixel_width': -5697315532444651320,
                                        'source_pixel_height': -1894474212513968388,
                                        'rotation': -8002094581656298491,
                                        'virtual_nw_x_pixel': 829479419,
                                        'virtual_nw_y_pixel': -478219568,
                                        'virtual_width': 1901108819,
                                        'virtual_height': 119111943,
                                    },
                            {
                                        'source_monitor': 8987053,
                                        'source_nw_x_pixel': -1977438307027246461,
                                        'source_nw_y_pixel': -4000367292215686704,
                                        'source_pixel_width': -5641786985660227568,
                                        'source_pixel_height': -3025875802527684048,
                                        'rotation': -6847571082745786073,
                                        'virtual_nw_x_pixel': -1563589974,
                                        'virtual_nw_y_pixel': 1246422626,
                                        'virtual_width': -852061329,
                                        'virtual_height': -588046651,
                                    },
                            {
                                        'source_monitor': 3590444,
                                        'source_nw_x_pixel': -6016363374808364910,
                                        'source_nw_y_pixel': -8044735118818954850,
                                        'source_pixel_width': -6412271307811961167,
                                        'source_pixel_height': -2379041599192242940,
                                        'rotation': -537452258197949993,
                                        'virtual_nw_x_pixel': 1776281404,
                                        'virtual_nw_y_pixel': -885380836,
                                        'virtual_width': -944655846,
                                        'virtual_height': 271966535,
                                    },
                            {
                                        'source_monitor': 4475868,
                                        'source_nw_x_pixel': -5074408063895817385,
                                        'source_nw_y_pixel': -1249205574667066138,
                                        'source_pixel_width': -3087646045897597494,
                                        'source_pixel_height': -8604999548318828610,
                                        'rotation': -9127713782986459977,
                                        'virtual_nw_x_pixel': -530705,
                                        'virtual_nw_y_pixel': -1932469709,
                                        'virtual_width': -1982866398,
                                        'virtual_height': -1859251962,
                                    },
                            {
                                        'source_monitor': 8139081,
                                        'source_nw_x_pixel': -2894862059823120284,
                                        'source_nw_y_pixel': -4089555513227548950,
                                        'source_pixel_width': -6065103350277062696,
                                        'source_pixel_height': -145667351003897375,
                                        'rotation': -2770215107792186610,
                                        'virtual_nw_x_pixel': -1020216473,
                                        'virtual_nw_y_pixel': -849082123,
                                        'virtual_width': 69251967,
                                        'virtual_height': 57654032,
                                    },
                            {
                                        'source_monitor': 1795297,
                                        'source_nw_x_pixel': -443632623032700677,
                                        'source_nw_y_pixel': -8327959660184721656,
                                        'source_pixel_width': -2499815715274596359,
                                        'source_pixel_height': -926048026231617282,
                                        'rotation': -8057622118362333711,
                                        'virtual_nw_x_pixel': -288792327,
                                        'virtual_nw_y_pixel': 31765435,
                                        'virtual_width': 992890496,
                                        'virtual_height': 1070504012,
                                    },
                            {
                                        'source_monitor': 4301302,
                                        'source_nw_x_pixel': -8413367209558361438,
                                        'source_nw_y_pixel': -8912373702407836081,
                                        'source_pixel_width': -2972457153904658454,
                                        'source_pixel_height': -8494264941311320935,
                                        'rotation': -5479985540484387866,
                                        'virtual_nw_x_pixel': 470331627,
                                        'virtual_nw_y_pixel': 831462427,
                                        'virtual_width': 792760144,
                                        'virtual_height': 121768370,
                                    },
                            {
                                        'source_monitor': 7332998,
                                        'source_nw_x_pixel': -409470326294751397,
                                        'source_nw_y_pixel': -8472821000511655491,
                                        'source_pixel_width': -3585069406060646168,
                                        'source_pixel_height': -8554794064925570576,
                                        'rotation': -4008962781381202904,
                                        'virtual_nw_x_pixel': 434029049,
                                        'virtual_nw_y_pixel': 1575931081,
                                        'virtual_width': 1877656258,
                                        'virtual_height': -440009152,
                                    },
                        ],
                },
                {
                    'description': 'ɯԞǵҸʶǓ˧˒\x9fi˅˅˞ϛǲʚʓГ÷WȎȗӻǘЬӗŹĕӗģ',
                    'monitors': [
                            {
                                        'identifier': 5020067,
                                        'width': 5485613035790100744,
                                        'height': 8113377160604436935,
                                    },
                            {
                                        'identifier': 13159,
                                        'width': -683303136878485398,
                                        'height': -5604008018114657098,
                                    },
                            {
                                        'identifier': 3557412,
                                        'width': -6746502438782921662,
                                        'height': 434149833503954250,
                                    },
                            {
                                        'identifier': 6281941,
                                        'width': -422162887935939397,
                                        'height': 2407325152050798769,
                                    },
                            {
                                        'identifier': 500540,
                                        'width': 7864935222285620231,
                                        'height': -7761925942291013006,
                                    },
                            {
                                        'identifier': 5452479,
                                        'width': -1514081105749996779,
                                        'height': 8671109454406234074,
                                    },
                            {
                                        'identifier': 3234073,
                                        'width': 188136511091146355,
                                        'height': -7033611980217362477,
                                    },
                            {
                                        'identifier': 6807222,
                                        'width': 6705983540280743299,
                                        'height': -7923251565117434234,
                                    },
                            {
                                        'identifier': 9972154,
                                        'width': 1691813190283158006,
                                        'height': -2695522821922792291,
                                    },
                            {
                                        'identifier': 8029408,
                                        'width': -6977531309433545070,
                                        'height': 6603327386790834723,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2103195,
                                        'source_nw_x_pixel': -1503007943569097511,
                                        'source_nw_y_pixel': -8039451646204574700,
                                        'source_pixel_width': -1752452838216405843,
                                        'source_pixel_height': -8105709584949509512,
                                        'rotation': -3617404941525980197,
                                        'virtual_nw_x_pixel': 205858155,
                                        'virtual_nw_y_pixel': 1927405491,
                                        'virtual_width': -581217351,
                                        'virtual_height': -293798966,
                                    },
                            {
                                        'source_monitor': 8319237,
                                        'source_nw_x_pixel': -4970117136963479251,
                                        'source_nw_y_pixel': -1125529956151610106,
                                        'source_pixel_width': -5986541888618002869,
                                        'source_pixel_height': -8352954120458671636,
                                        'rotation': -1779218751954272829,
                                        'virtual_nw_x_pixel': 173011339,
                                        'virtual_nw_y_pixel': -1462925539,
                                        'virtual_width': -665378349,
                                        'virtual_height': 648452396,
                                    },
                            {
                                        'source_monitor': 7636157,
                                        'source_nw_x_pixel': -8110007896748995180,
                                        'source_nw_y_pixel': -4464095615216163756,
                                        'source_pixel_width': -6373998645846958296,
                                        'source_pixel_height': -8130467477128705820,
                                        'rotation': -4882306141801112863,
                                        'virtual_nw_x_pixel': 137172291,
                                        'virtual_nw_y_pixel': 919973368,
                                        'virtual_width': 436332169,
                                        'virtual_height': 1969322238,
                                    },
                            {
                                        'source_monitor': 4759283,
                                        'source_nw_x_pixel': -2962307725249290792,
                                        'source_nw_y_pixel': -502236694734040980,
                                        'source_pixel_width': -6287081132483998721,
                                        'source_pixel_height': -4214299221016637507,
                                        'rotation': -489399549643495262,
                                        'virtual_nw_x_pixel': 17331748,
                                        'virtual_nw_y_pixel': 469479894,
                                        'virtual_width': -1273985634,
                                        'virtual_height': -1423112577,
                                    },
                            {
                                        'source_monitor': -439793,
                                        'source_nw_x_pixel': -5242799087583708971,
                                        'source_nw_y_pixel': -9022703282967565728,
                                        'source_pixel_width': -2220074335270966845,
                                        'source_pixel_height': -6308124551323080364,
                                        'rotation': -2746243016822990978,
                                        'virtual_nw_x_pixel': -981155559,
                                        'virtual_nw_y_pixel': 226395233,
                                        'virtual_width': 1111889029,
                                        'virtual_height': 1293517858,
                                    },
                            {
                                        'source_monitor': 3468259,
                                        'source_nw_x_pixel': -1338178661782125464,
                                        'source_nw_y_pixel': -6062335897599681169,
                                        'source_pixel_width': -9081672884651389336,
                                        'source_pixel_height': -6379234427838351748,
                                        'rotation': -454656074947063704,
                                        'virtual_nw_x_pixel': -1688953406,
                                        'virtual_nw_y_pixel': -1708265787,
                                        'virtual_width': -403194483,
                                        'virtual_height': -906563277,
                                    },
                            {
                                        'source_monitor': -312419,
                                        'source_nw_x_pixel': -8878241916397624527,
                                        'source_nw_y_pixel': -3764659091253917011,
                                        'source_pixel_width': -3009141002040012291,
                                        'source_pixel_height': -3440235696777847226,
                                        'rotation': -6524395068957920657,
                                        'virtual_nw_x_pixel': -1662455631,
                                        'virtual_nw_y_pixel': -469051074,
                                        'virtual_width': 1944450752,
                                        'virtual_height': -1726205902,
                                    },
                            {
                                        'source_monitor': 5015504,
                                        'source_nw_x_pixel': -2632971227499245008,
                                        'source_nw_y_pixel': -1712626658995091932,
                                        'source_pixel_width': -6957862130309181123,
                                        'source_pixel_height': -4488221202513844340,
                                        'rotation': -6649190966149188996,
                                        'virtual_nw_x_pixel': 1327208889,
                                        'virtual_nw_y_pixel': -251975038,
                                        'virtual_width': -1244520628,
                                        'virtual_height': 1005018929,
                                    },
                            {
                                        'source_monitor': 4139148,
                                        'source_nw_x_pixel': -6386549978800798981,
                                        'source_nw_y_pixel': -5630226522102018909,
                                        'source_pixel_width': -3059209774921895961,
                                        'source_pixel_height': -5957418405181830898,
                                        'rotation': -8959713795337287576,
                                        'virtual_nw_x_pixel': 1226406082,
                                        'virtual_nw_y_pixel': 1452161240,
                                        'virtual_width': 1886874498,
                                        'virtual_height': 1356046975,
                                    },
                            {
                                        'source_monitor': 601537,
                                        'source_nw_x_pixel': -957946688807693442,
                                        'source_nw_y_pixel': -6909452826046584260,
                                        'source_pixel_width': -1103568450347005341,
                                        'source_pixel_height': -1081831893116522013,
                                        'rotation': -2868791322652593076,
                                        'virtual_nw_x_pixel': 472527391,
                                        'virtual_nw_y_pixel': 368241236,
                                        'virtual_width': 1657331583,
                                        'virtual_height': 1026709042,
                                    },
                        ],
                },
                {
                    'description': 'ĈŠϕʇ¦˳Ô*ɣŒǕEŸѻsϔ\x95ĜӆĉʹȞȣť8ӊėԦŋϑ',
                    'monitors': [
                            {
                                        'identifier': 7123586,
                                        'width': 7465832912163325254,
                                        'height': -7253315252649842202,
                                    },
                            {
                                        'identifier': -917301,
                                        'width': 4980532526204828132,
                                        'height': -5120279569099089727,
                                    },
                            {
                                        'identifier': 9984297,
                                        'width': 2663603448962530055,
                                        'height': 4542175439845914458,
                                    },
                            {
                                        'identifier': 7291719,
                                        'width': -3545099436939171382,
                                        'height': -3521329136320218954,
                                    },
                            {
                                        'identifier': 5573101,
                                        'width': -7958643073658938353,
                                        'height': 1490671441032197892,
                                    },
                            {
                                        'identifier': 4184401,
                                        'width': -5702726284724636099,
                                        'height': 3714577086605822354,
                                    },
                            {
                                        'identifier': 6810818,
                                        'width': -1809852771570841568,
                                        'height': -2880707247736989286,
                                    },
                            {
                                        'identifier': 9083033,
                                        'width': 2110831839000651420,
                                        'height': 2226250863529181921,
                                    },
                            {
                                        'identifier': 2597903,
                                        'width': 2293198132299390476,
                                        'height': 8538926890171717914,
                                    },
                            {
                                        'identifier': 247996,
                                        'width': -1503638128389555539,
                                        'height': -328319422078400254,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2165758,
                                        'source_nw_x_pixel': -6254475233213305232,
                                        'source_nw_y_pixel': -372330807851103997,
                                        'source_pixel_width': -1195435656738046503,
                                        'source_pixel_height': -4479803110991683077,
                                        'rotation': -212067081023535858,
                                        'virtual_nw_x_pixel': 1398094600,
                                        'virtual_nw_y_pixel': -1200130775,
                                        'virtual_width': -1249979892,
                                        'virtual_height': -177217400,
                                    },
                            {
                                        'source_monitor': 862360,
                                        'source_nw_x_pixel': -2815501967464496187,
                                        'source_nw_y_pixel': -4018991947300564464,
                                        'source_pixel_width': -3820624706346307505,
                                        'source_pixel_height': -858598376079174657,
                                        'rotation': -6527994463576521176,
                                        'virtual_nw_x_pixel': -1110331926,
                                        'virtual_nw_y_pixel': -1888821445,
                                        'virtual_width': -1313635074,
                                        'virtual_height': 1276408508,
                                    },
                            {
                                        'source_monitor': 1466171,
                                        'source_nw_x_pixel': -6992985716766773502,
                                        'source_nw_y_pixel': -1900909340005961276,
                                        'source_pixel_width': -5834363296239011757,
                                        'source_pixel_height': -4302264538002791053,
                                        'rotation': -2529983409120227369,
                                        'virtual_nw_x_pixel': -789490213,
                                        'virtual_nw_y_pixel': -1522722194,
                                        'virtual_width': -1514253590,
                                        'virtual_height': 1295423480,
                                    },
                            {
                                        'source_monitor': 6833530,
                                        'source_nw_x_pixel': -8972038816816200018,
                                        'source_nw_y_pixel': -476485296114680723,
                                        'source_pixel_width': -2089992865209409779,
                                        'source_pixel_height': -8675255224259953804,
                                        'rotation': -160983923374317347,
                                        'virtual_nw_x_pixel': 38134771,
                                        'virtual_nw_y_pixel': 1008664582,
                                        'virtual_width': 737213810,
                                        'virtual_height': 483356644,
                                    },
                            {
                                        'source_monitor': 1235662,
                                        'source_nw_x_pixel': -7696359473778579058,
                                        'source_nw_y_pixel': -1144554300378826546,
                                        'source_pixel_width': -1011784425195632892,
                                        'source_pixel_height': -6708892181483376095,
                                        'rotation': -1090345148206128548,
                                        'virtual_nw_x_pixel': 890644022,
                                        'virtual_nw_y_pixel': 559381636,
                                        'virtual_width': 930882073,
                                        'virtual_height': 47991999,
                                    },
                            {
                                        'source_monitor': 5857037,
                                        'source_nw_x_pixel': -2385674778877510061,
                                        'source_nw_y_pixel': -964141713358616916,
                                        'source_pixel_width': -7833451214154932425,
                                        'source_pixel_height': -7797833548844357018,
                                        'rotation': -925684565728827593,
                                        'virtual_nw_x_pixel': -399504637,
                                        'virtual_nw_y_pixel': -1389112597,
                                        'virtual_width': 1339037973,
                                        'virtual_height': 27544260,
                                    },
                            {
                                        'source_monitor': 1435264,
                                        'source_nw_x_pixel': -7737164811540114505,
                                        'source_nw_y_pixel': -1064053492140689394,
                                        'source_pixel_width': -3850303906055319521,
                                        'source_pixel_height': -2906956231602861320,
                                        'rotation': -3887484068508892853,
                                        'virtual_nw_x_pixel': -241799564,
                                        'virtual_nw_y_pixel': 446223170,
                                        'virtual_width': 337023656,
                                        'virtual_height': -124398790,
                                    },
                            {
                                        'source_monitor': 8304358,
                                        'source_nw_x_pixel': -4251127770960184570,
                                        'source_nw_y_pixel': -7915056532043134650,
                                        'source_pixel_width': -7727942717036492283,
                                        'source_pixel_height': -7183980066007100495,
                                        'rotation': -1703624097575014827,
                                        'virtual_nw_x_pixel': -1174018027,
                                        'virtual_nw_y_pixel': 1603964515,
                                        'virtual_width': -1801536070,
                                        'virtual_height': -1813096294,
                                    },
                            {
                                        'source_monitor': 3381554,
                                        'source_nw_x_pixel': -6287574250472575098,
                                        'source_nw_y_pixel': -1939390401391714894,
                                        'source_pixel_width': -5266990441910616894,
                                        'source_pixel_height': -975307320367463855,
                                        'rotation': -351422598711565194,
                                        'virtual_nw_x_pixel': 943125900,
                                        'virtual_nw_y_pixel': -1746667845,
                                        'virtual_width': -1340812765,
                                        'virtual_height': -1346384470,
                                    },
                            {
                                        'source_monitor': 6828720,
                                        'source_nw_x_pixel': -7585933447599004034,
                                        'source_nw_y_pixel': -1310953093154954321,
                                        'source_pixel_width': -4299315771622534209,
                                        'source_pixel_height': -6057495181822327802,
                                        'rotation': -4763664581716371469,
                                        'virtual_nw_x_pixel': 867909378,
                                        'virtual_nw_y_pixel': -1649590810,
                                        'virtual_width': -1436009438,
                                        'virtual_height': 1691901778,
                                    },
                        ],
                },
                {
                    'description': 'лǽҮЗɲɴđΨӁʽ¥\u0383ʮhšȶŠӹёäǿʫњɃˆĎγə҃ſ',
                    'monitors': [
                            {
                                        'identifier': 9326276,
                                        'width': -7349333031564872771,
                                        'height': -7471185437680643324,
                                    },
                            {
                                        'identifier': 9325050,
                                        'width': 3593360938378602384,
                                        'height': 3216264798121228252,
                                    },
                            {
                                        'identifier': 8966632,
                                        'width': -8972282765567420603,
                                        'height': 7074718759503985159,
                                    },
                            {
                                        'identifier': 7527684,
                                        'width': 240388993727499405,
                                        'height': 6012486714755484613,
                                    },
                            {
                                        'identifier': 5288979,
                                        'width': 6006239589452958606,
                                        'height': -7776671148831065346,
                                    },
                            {
                                        'identifier': 8529392,
                                        'width': 7634133505406179112,
                                        'height': -1821152925215774905,
                                    },
                            {
                                        'identifier': -342861,
                                        'width': 3871129670035711531,
                                        'height': 1987976566226006326,
                                    },
                            {
                                        'identifier': 8294155,
                                        'width': 1426362202661835881,
                                        'height': 4869671077703939930,
                                    },
                            {
                                        'identifier': 8059148,
                                        'width': 4227241822106550487,
                                        'height': 367653684069832802,
                                    },
                            {
                                        'identifier': 1464753,
                                        'width': -4521023250414300636,
                                        'height': -7530290669300987516,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -656180,
                                        'source_nw_x_pixel': -4101996950671727353,
                                        'source_nw_y_pixel': -4590951097688181186,
                                        'source_pixel_width': -920456822022002588,
                                        'source_pixel_height': -8072639322939082697,
                                        'rotation': -5231640118431047770,
                                        'virtual_nw_x_pixel': 452878784,
                                        'virtual_nw_y_pixel': 17008542,
                                        'virtual_width': 927420616,
                                        'virtual_height': -894227086,
                                    },
                            {
                                        'source_monitor': 976758,
                                        'source_nw_x_pixel': -2643994357086195081,
                                        'source_nw_y_pixel': -7231893768874259321,
                                        'source_pixel_width': -5094945725943428342,
                                        'source_pixel_height': -1336675014815023047,
                                        'rotation': -9133332662317524187,
                                        'virtual_nw_x_pixel': 442686363,
                                        'virtual_nw_y_pixel': 1836444789,
                                        'virtual_width': 329154787,
                                        'virtual_height': 225718575,
                                    },
                            {
                                        'source_monitor': 8148885,
                                        'source_nw_x_pixel': -4444492939075527417,
                                        'source_nw_y_pixel': -6633546791757861281,
                                        'source_pixel_width': -362622165670911946,
                                        'source_pixel_height': -9079981583343112992,
                                        'rotation': -6768474441092434862,
                                        'virtual_nw_x_pixel': -66514961,
                                        'virtual_nw_y_pixel': -1790704159,
                                        'virtual_width': 610779304,
                                        'virtual_height': -825045027,
                                    },
                            {
                                        'source_monitor': 1020833,
                                        'source_nw_x_pixel': -3062290622969672270,
                                        'source_nw_y_pixel': -7187153595051421652,
                                        'source_pixel_width': -3126542229949263870,
                                        'source_pixel_height': -4238652439621470409,
                                        'rotation': -1152266336379093602,
                                        'virtual_nw_x_pixel': -1932781996,
                                        'virtual_nw_y_pixel': -698506984,
                                        'virtual_width': 1369543067,
                                        'virtual_height': 1582076151,
                                    },
                            {
                                        'source_monitor': 7528709,
                                        'source_nw_x_pixel': -7245536031998603647,
                                        'source_nw_y_pixel': -3808461483021919877,
                                        'source_pixel_width': -1391626012513396237,
                                        'source_pixel_height': -3158832208614998927,
                                        'rotation': -8613131604335990554,
                                        'virtual_nw_x_pixel': 1169514880,
                                        'virtual_nw_y_pixel': -1147667463,
                                        'virtual_width': -1014798046,
                                        'virtual_height': -979242555,
                                    },
                            {
                                        'source_monitor': -882282,
                                        'source_nw_x_pixel': -8118046245877303128,
                                        'source_nw_y_pixel': -3685174842806214653,
                                        'source_pixel_width': -2379730704648273585,
                                        'source_pixel_height': -6402074584956944581,
                                        'rotation': -4734350498676552643,
                                        'virtual_nw_x_pixel': -1476191712,
                                        'virtual_nw_y_pixel': -573887,
                                        'virtual_width': 198131463,
                                        'virtual_height': -1762780460,
                                    },
                            {
                                        'source_monitor': 5881389,
                                        'source_nw_x_pixel': -5860773400567029077,
                                        'source_nw_y_pixel': -2089007467283907484,
                                        'source_pixel_width': -1577140423840844804,
                                        'source_pixel_height': -108229973972277748,
                                        'rotation': -6444532582502682139,
                                        'virtual_nw_x_pixel': 1364393312,
                                        'virtual_nw_y_pixel': -861356368,
                                        'virtual_width': -466659093,
                                        'virtual_height': 1744424156,
                                    },
                            {
                                        'source_monitor': 2828545,
                                        'source_nw_x_pixel': -3052073941282716916,
                                        'source_nw_y_pixel': -8649596451550513053,
                                        'source_pixel_width': -2734055178616063150,
                                        'source_pixel_height': -6362878211828727013,
                                        'rotation': -874368626410993915,
                                        'virtual_nw_x_pixel': 1649366904,
                                        'virtual_nw_y_pixel': 210361589,
                                        'virtual_width': 441504214,
                                        'virtual_height': -1424383588,
                                    },
                            {
                                        'source_monitor': 3910179,
                                        'source_nw_x_pixel': -5724038323845038961,
                                        'source_nw_y_pixel': -5668300559722839725,
                                        'source_pixel_width': -2718639571761324151,
                                        'source_pixel_height': -9103475773122514619,
                                        'rotation': -7529461209822182598,
                                        'virtual_nw_x_pixel': 965220584,
                                        'virtual_nw_y_pixel': -1594273885,
                                        'virtual_width': 1410158016,
                                        'virtual_height': -627778706,
                                    },
                            {
                                        'source_monitor': -112721,
                                        'source_nw_x_pixel': -7927936187794574975,
                                        'source_nw_y_pixel': -4501143087447716098,
                                        'source_pixel_width': -4575980346189030118,
                                        'source_pixel_height': -6731200001481065492,
                                        'rotation': -4141828268508495229,
                                        'virtual_nw_x_pixel': -1730660943,
                                        'virtual_nw_y_pixel': -29058167,
                                        'virtual_width': -712684207,
                                        'virtual_height': -418104829,
                                    },
                        ],
                },
                {
                    'description': 'vȨĆÚœ\u0380Ќʢѓҩ{ÀіλþѕξǆËϡĬЫǱmǉùѻ\u0381ѷН',
                    'monitors': [
                            {
                                        'identifier': 1126003,
                                        'width': 7593844133012204569,
                                        'height': -640736833548802197,
                                    },
                            {
                                        'identifier': 1226155,
                                        'width': 9139527422332808486,
                                        'height': -1459515158475961389,
                                    },
                            {
                                        'identifier': 4817512,
                                        'width': -6931241095291368355,
                                        'height': 4657739704886577393,
                                    },
                            {
                                        'identifier': 721930,
                                        'width': 2153671208611801596,
                                        'height': 7321449539533872506,
                                    },
                            {
                                        'identifier': 5982634,
                                        'width': -8906361423164147718,
                                        'height': 3128951213028658410,
                                    },
                            {
                                        'identifier': 1034429,
                                        'width': 3398653282280490889,
                                        'height': 1344389567769659590,
                                    },
                            {
                                        'identifier': -811198,
                                        'width': -8995965231807184164,
                                        'height': 123743125980584518,
                                    },
                            {
                                        'identifier': -791269,
                                        'width': -1577812917706569278,
                                        'height': -3769019185136487413,
                                    },
                            {
                                        'identifier': 1734760,
                                        'width': -2857952067029691784,
                                        'height': 2566963027684781916,
                                    },
                            {
                                        'identifier': 907218,
                                        'width': -3778808618547123389,
                                        'height': 366568682559297817,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3650876,
                                        'source_nw_x_pixel': -4257231248509060033,
                                        'source_nw_y_pixel': -4288965500150634591,
                                        'source_pixel_width': -8168450844566379613,
                                        'source_pixel_height': -1351930998880066314,
                                        'rotation': -6309334059245369143,
                                        'virtual_nw_x_pixel': -865477203,
                                        'virtual_nw_y_pixel': -790601920,
                                        'virtual_width': 1573485661,
                                        'virtual_height': 1051553331,
                                    },
                            {
                                        'source_monitor': 5928217,
                                        'source_nw_x_pixel': -6206085708318640542,
                                        'source_nw_y_pixel': -3104161082612756418,
                                        'source_pixel_width': -8222332181951064680,
                                        'source_pixel_height': -729883473564742120,
                                        'rotation': -4258651414700714553,
                                        'virtual_nw_x_pixel': 1815968335,
                                        'virtual_nw_y_pixel': 984086906,
                                        'virtual_width': -1837245600,
                                        'virtual_height': -1111039283,
                                    },
                            {
                                        'source_monitor': 5709201,
                                        'source_nw_x_pixel': -5823136788287768546,
                                        'source_nw_y_pixel': -7452552825633045851,
                                        'source_pixel_width': -9171553423027876462,
                                        'source_pixel_height': -8692261391754540594,
                                        'rotation': -1113981822693510460,
                                        'virtual_nw_x_pixel': -11495857,
                                        'virtual_nw_y_pixel': -1429160449,
                                        'virtual_width': -710014387,
                                        'virtual_height': -1841533428,
                                    },
                            {
                                        'source_monitor': 3686856,
                                        'source_nw_x_pixel': -5809112811989312886,
                                        'source_nw_y_pixel': -1690753529116613164,
                                        'source_pixel_width': -6955861900814802541,
                                        'source_pixel_height': -1590661638845388601,
                                        'rotation': -4313262141182523597,
                                        'virtual_nw_x_pixel': 697481732,
                                        'virtual_nw_y_pixel': -1952023492,
                                        'virtual_width': -1561789816,
                                        'virtual_height': 20899106,
                                    },
                            {
                                        'source_monitor': 6010472,
                                        'source_nw_x_pixel': -3731570442570053963,
                                        'source_nw_y_pixel': -1959608252562712530,
                                        'source_pixel_width': -268201574791183601,
                                        'source_pixel_height': -3056946180851714416,
                                        'rotation': -7018813141014242245,
                                        'virtual_nw_x_pixel': 1357806977,
                                        'virtual_nw_y_pixel': 1680311524,
                                        'virtual_width': 1767586706,
                                        'virtual_height': 1163583425,
                                    },
                            {
                                        'source_monitor': 8088692,
                                        'source_nw_x_pixel': -4004846471489883998,
                                        'source_nw_y_pixel': -1480582258320837039,
                                        'source_pixel_width': -3548455146959884419,
                                        'source_pixel_height': -12390802921863704,
                                        'rotation': -3160019154020606722,
                                        'virtual_nw_x_pixel': -1422103071,
                                        'virtual_nw_y_pixel': -770388741,
                                        'virtual_width': -1033856331,
                                        'virtual_height': -28862488,
                                    },
                            {
                                        'source_monitor': 1053064,
                                        'source_nw_x_pixel': -3488805638777955033,
                                        'source_nw_y_pixel': -505418393314322533,
                                        'source_pixel_width': -1705403589676012200,
                                        'source_pixel_height': -3270705815182482800,
                                        'rotation': -1449077254706210993,
                                        'virtual_nw_x_pixel': -58693284,
                                        'virtual_nw_y_pixel': -1813917879,
                                        'virtual_width': 892060030,
                                        'virtual_height': 32440091,
                                    },
                            {
                                        'source_monitor': 4268713,
                                        'source_nw_x_pixel': -4645251238744157915,
                                        'source_nw_y_pixel': -8338244379630586015,
                                        'source_pixel_width': -1867051119073996769,
                                        'source_pixel_height': -8592254616483229369,
                                        'rotation': -1577454888748882595,
                                        'virtual_nw_x_pixel': -962024171,
                                        'virtual_nw_y_pixel': -1732141119,
                                        'virtual_width': -879331358,
                                        'virtual_height': -1050503559,
                                    },
                            {
                                        'source_monitor': 4391008,
                                        'source_nw_x_pixel': -2669243237760782821,
                                        'source_nw_y_pixel': -8655134790362173382,
                                        'source_pixel_width': -741651467223297207,
                                        'source_pixel_height': -3899998469656992182,
                                        'rotation': -3591403890171649874,
                                        'virtual_nw_x_pixel': 1318080346,
                                        'virtual_nw_y_pixel': -385637230,
                                        'virtual_width': -1336069968,
                                        'virtual_height': 339701490,
                                    },
                            {
                                        'source_monitor': 6404524,
                                        'source_nw_x_pixel': -5165444626541094386,
                                        'source_nw_y_pixel': -1960439236135794787,
                                        'source_pixel_width': -7843103119790893712,
                                        'source_pixel_height': -482852719334112991,
                                        'rotation': -7454695124999189549,
                                        'virtual_nw_x_pixel': -478860141,
                                        'virtual_nw_y_pixel': 1901345940,
                                        'virtual_width': 731066466,
                                        'virtual_height': 1298687183,
                                    },
                        ],
                },
                {
                    'description': 'ЦϊЭȟĻ˵ѼÔǌҟżȦχ\u038dưԞȭʒǃШόʿƁѳƹΰóúɆӟ',
                    'monitors': [
                            {
                                        'identifier': 8083984,
                                        'width': 3383406287833763360,
                                        'height': 3589566969130569443,
                                    },
                            {
                                        'identifier': 9254193,
                                        'width': 6762703460601825336,
                                        'height': 6707866185478939666,
                                    },
                            {
                                        'identifier': 4564878,
                                        'width': 8486415407215511968,
                                        'height': 4922855769584192865,
                                    },
                            {
                                        'identifier': 1875808,
                                        'width': 5516765739871591181,
                                        'height': -3193437443178299076,
                                    },
                            {
                                        'identifier': -558798,
                                        'width': -8257178401918457296,
                                        'height': -3585503340099100917,
                                    },
                            {
                                        'identifier': 3235507,
                                        'width': -1835524084350304966,
                                        'height': -5896981826147895110,
                                    },
                            {
                                        'identifier': 2844726,
                                        'width': -5768712493768368246,
                                        'height': 4124125609966845204,
                                    },
                            {
                                        'identifier': 506293,
                                        'width': -1988667832356372079,
                                        'height': 5097327258433593356,
                                    },
                            {
                                        'identifier': 6603815,
                                        'width': -3762638952464231687,
                                        'height': -2724411570697882125,
                                    },
                            {
                                        'identifier': 1364274,
                                        'width': -2461397823331061292,
                                        'height': -3643894408107014291,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5449300,
                                        'source_nw_x_pixel': -4178582901723857559,
                                        'source_nw_y_pixel': -7006539949334698912,
                                        'source_pixel_width': -799343522369926841,
                                        'source_pixel_height': -5500972828903240481,
                                        'rotation': -349111366240320315,
                                        'virtual_nw_x_pixel': -1984111544,
                                        'virtual_nw_y_pixel': 1823625924,
                                        'virtual_width': -1877276117,
                                        'virtual_height': -566064069,
                                    },
                            {
                                        'source_monitor': 3102050,
                                        'source_nw_x_pixel': -4005260661166422122,
                                        'source_nw_y_pixel': -5820630323483885071,
                                        'source_pixel_width': -3975750079511179003,
                                        'source_pixel_height': -3212520003770278678,
                                        'rotation': -8867160336654117775,
                                        'virtual_nw_x_pixel': 679817890,
                                        'virtual_nw_y_pixel': 947554262,
                                        'virtual_width': 839231398,
                                        'virtual_height': 1544211981,
                                    },
                            {
                                        'source_monitor': 6099398,
                                        'source_nw_x_pixel': -8288629590310651643,
                                        'source_nw_y_pixel': -2054589962294108046,
                                        'source_pixel_width': -7536319135090353971,
                                        'source_pixel_height': -3938875162078125752,
                                        'rotation': -8585681715226659916,
                                        'virtual_nw_x_pixel': 792602752,
                                        'virtual_nw_y_pixel': -1447251619,
                                        'virtual_width': 674162274,
                                        'virtual_height': 1712756947,
                                    },
                            {
                                        'source_monitor': 5360612,
                                        'source_nw_x_pixel': -3594713324591186579,
                                        'source_nw_y_pixel': -8182037114312426824,
                                        'source_pixel_width': -5048208488885894479,
                                        'source_pixel_height': -2217247667037647459,
                                        'rotation': -5502153903065351027,
                                        'virtual_nw_x_pixel': -1132718696,
                                        'virtual_nw_y_pixel': -435429652,
                                        'virtual_width': -93665775,
                                        'virtual_height': -837220704,
                                    },
                            {
                                        'source_monitor': 5672619,
                                        'source_nw_x_pixel': -5950328569129007336,
                                        'source_nw_y_pixel': -629476931936658793,
                                        'source_pixel_width': -4494023060024147600,
                                        'source_pixel_height': -7242915476398484973,
                                        'rotation': -5172797064296374439,
                                        'virtual_nw_x_pixel': -519827197,
                                        'virtual_nw_y_pixel': -1994757198,
                                        'virtual_width': -39954520,
                                        'virtual_height': -832455367,
                                    },
                            {
                                        'source_monitor': 5814597,
                                        'source_nw_x_pixel': -7723115432304619563,
                                        'source_nw_y_pixel': -1756632280563552338,
                                        'source_pixel_width': -4336487759611223974,
                                        'source_pixel_height': -9196119806204510121,
                                        'rotation': -3894106648714420556,
                                        'virtual_nw_x_pixel': -135853571,
                                        'virtual_nw_y_pixel': -1645464646,
                                        'virtual_width': -282313265,
                                        'virtual_height': 1228926422,
                                    },
                            {
                                        'source_monitor': 261150,
                                        'source_nw_x_pixel': -8614503455884809457,
                                        'source_nw_y_pixel': -3372577552447743797,
                                        'source_pixel_width': -1675466272413445600,
                                        'source_pixel_height': -7980829612020084186,
                                        'rotation': -6458457206740225009,
                                        'virtual_nw_x_pixel': 1636820859,
                                        'virtual_nw_y_pixel': -1337418874,
                                        'virtual_width': -808918638,
                                        'virtual_height': 1282287992,
                                    },
                            {
                                        'source_monitor': 5068539,
                                        'source_nw_x_pixel': -2270881253794885854,
                                        'source_nw_y_pixel': -4993113843857634451,
                                        'source_pixel_width': -4912627858764616243,
                                        'source_pixel_height': -5280878602447419848,
                                        'rotation': -7506218679273140529,
                                        'virtual_nw_x_pixel': 306749498,
                                        'virtual_nw_y_pixel': -1608470446,
                                        'virtual_width': -1994694867,
                                        'virtual_height': -1560741344,
                                    },
                            {
                                        'source_monitor': 9379307,
                                        'source_nw_x_pixel': -7704635546225981763,
                                        'source_nw_y_pixel': -6762831353878865637,
                                        'source_pixel_width': -2526366762855862486,
                                        'source_pixel_height': -2208020784910773931,
                                        'rotation': -2534205281497087326,
                                        'virtual_nw_x_pixel': -681762371,
                                        'virtual_nw_y_pixel': 1668317630,
                                        'virtual_width': 1294257218,
                                        'virtual_height': 1160934299,
                                    },
                            {
                                        'source_monitor': 2357772,
                                        'source_nw_x_pixel': -1339876893936554149,
                                        'source_nw_y_pixel': -1073129936871360322,
                                        'source_pixel_width': -125223353824962483,
                                        'source_pixel_height': -3008723050077027449,
                                        'rotation': -9030842178257317514,
                                        'virtual_nw_x_pixel': -194853048,
                                        'virtual_nw_y_pixel': 868170595,
                                        'virtual_width': 1682564631,
                                        'virtual_height': 359919566,
                                    },
                        ],
                },
                {
                    'description': 'җĝЫɼȸΡ\x96ӁѿÏĘɻƋɘʛĜɭкѨѹͶҌΊ7\x92ăȅҝδƜ',
                    'monitors': [
                            {
                                        'identifier': 2843180,
                                        'width': -3568653901871201313,
                                        'height': 2277483397328377319,
                                    },
                            {
                                        'identifier': 8342517,
                                        'width': -9182576735415104488,
                                        'height': 673279794310421463,
                                    },
                            {
                                        'identifier': 9388970,
                                        'width': 1185720548404879313,
                                        'height': 1702076144480568416,
                                    },
                            {
                                        'identifier': 4593953,
                                        'width': 9045017280511133034,
                                        'height': 4062955285748688363,
                                    },
                            {
                                        'identifier': 2836043,
                                        'width': -6733995010763354267,
                                        'height': 3892254381170857814,
                                    },
                            {
                                        'identifier': 5168317,
                                        'width': -8790412976757071682,
                                        'height': 910080473497868527,
                                    },
                            {
                                        'identifier': 4411122,
                                        'width': -7090506326292239648,
                                        'height': 3639834506553937356,
                                    },
                            {
                                        'identifier': 1413813,
                                        'width': 2184834207114945103,
                                        'height': -907342294285812691,
                                    },
                            {
                                        'identifier': 2215711,
                                        'width': 3586488098930002035,
                                        'height': -1436434005396104784,
                                    },
                            {
                                        'identifier': 4079961,
                                        'width': 6857741443109491532,
                                        'height': -2777411607354918940,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1259797,
                                        'source_nw_x_pixel': -7633775095347672556,
                                        'source_nw_y_pixel': -1780669882531939253,
                                        'source_pixel_width': -6062016270915699306,
                                        'source_pixel_height': -3543215677822467930,
                                        'rotation': -6851038526794685355,
                                        'virtual_nw_x_pixel': -1094793471,
                                        'virtual_nw_y_pixel': 361573427,
                                        'virtual_width': 12712262,
                                        'virtual_height': -461131716,
                                    },
                            {
                                        'source_monitor': 713577,
                                        'source_nw_x_pixel': -8414762914564760178,
                                        'source_nw_y_pixel': -7124222758146204479,
                                        'source_pixel_width': -4500410351994610621,
                                        'source_pixel_height': -1900408434000332926,
                                        'rotation': -7151264365215714379,
                                        'virtual_nw_x_pixel': -1079207629,
                                        'virtual_nw_y_pixel': 81763121,
                                        'virtual_width': -30595272,
                                        'virtual_height': 1229803532,
                                    },
                            {
                                        'source_monitor': 9195896,
                                        'source_nw_x_pixel': -4715233081175030211,
                                        'source_nw_y_pixel': -3524886950960753158,
                                        'source_pixel_width': -3180281512167853161,
                                        'source_pixel_height': -8281181728693333120,
                                        'rotation': -4892139067164114889,
                                        'virtual_nw_x_pixel': 1044773322,
                                        'virtual_nw_y_pixel': -195578632,
                                        'virtual_width': -182226958,
                                        'virtual_height': -1715319128,
                                    },
                            {
                                        'source_monitor': 9050554,
                                        'source_nw_x_pixel': -3721246100115091974,
                                        'source_nw_y_pixel': -8778030521119401072,
                                        'source_pixel_width': -6304946907134625859,
                                        'source_pixel_height': -753241645968376975,
                                        'rotation': -7369606717861836049,
                                        'virtual_nw_x_pixel': 376384234,
                                        'virtual_nw_y_pixel': -1496240977,
                                        'virtual_width': 1157962333,
                                        'virtual_height': -1231585161,
                                    },
                            {
                                        'source_monitor': 5831462,
                                        'source_nw_x_pixel': -3607398806217090257,
                                        'source_nw_y_pixel': -1613783538949375636,
                                        'source_pixel_width': -1430378139405558036,
                                        'source_pixel_height': -2859507060198308896,
                                        'rotation': -1148722492550533796,
                                        'virtual_nw_x_pixel': -655523274,
                                        'virtual_nw_y_pixel': 912078497,
                                        'virtual_width': -1266513466,
                                        'virtual_height': 239078340,
                                    },
                            {
                                        'source_monitor': 9159777,
                                        'source_nw_x_pixel': -8353842706809876001,
                                        'source_nw_y_pixel': -7937494860524504556,
                                        'source_pixel_width': -7238924641727988931,
                                        'source_pixel_height': -5613872310141461232,
                                        'rotation': -2473197684562649813,
                                        'virtual_nw_x_pixel': -184307902,
                                        'virtual_nw_y_pixel': -44858367,
                                        'virtual_width': -1517558768,
                                        'virtual_height': 326925557,
                                    },
                            {
                                        'source_monitor': 3847109,
                                        'source_nw_x_pixel': -5310641032252978584,
                                        'source_nw_y_pixel': -3018931403014033649,
                                        'source_pixel_width': -1542747682354462138,
                                        'source_pixel_height': -1687704752962073394,
                                        'rotation': -2915411925345033257,
                                        'virtual_nw_x_pixel': 519044393,
                                        'virtual_nw_y_pixel': 1477050300,
                                        'virtual_width': -676747991,
                                        'virtual_height': -1041344446,
                                    },
                            {
                                        'source_monitor': 8420618,
                                        'source_nw_x_pixel': -1332102832785840337,
                                        'source_nw_y_pixel': -929299994520385536,
                                        'source_pixel_width': -3369270218055767861,
                                        'source_pixel_height': -3620178678377654567,
                                        'rotation': -2454721378786941901,
                                        'virtual_nw_x_pixel': 349669970,
                                        'virtual_nw_y_pixel': -1773587955,
                                        'virtual_width': -1390369743,
                                        'virtual_height': -1941189425,
                                    },
                            {
                                        'source_monitor': 6653350,
                                        'source_nw_x_pixel': -3866559185244595801,
                                        'source_nw_y_pixel': -5982684624137403622,
                                        'source_pixel_width': -1260305510824529096,
                                        'source_pixel_height': -8764930977224064599,
                                        'rotation': -2527309562837080841,
                                        'virtual_nw_x_pixel': 95298096,
                                        'virtual_nw_y_pixel': 1182107004,
                                        'virtual_width': 910051382,
                                        'virtual_height': 1111147905,
                                    },
                            {
                                        'source_monitor': 5227721,
                                        'source_nw_x_pixel': -278509314559242140,
                                        'source_nw_y_pixel': -8072262113794581272,
                                        'source_pixel_width': -4768582282653503088,
                                        'source_pixel_height': -5837836631127369187,
                                        'rotation': -3539701452102319954,
                                        'virtual_nw_x_pixel': -321923810,
                                        'virtual_nw_y_pixel': -1127953148,
                                        'virtual_width': 1628406725,
                                        'virtual_height': -35844755,
                                    },
                        ],
                },
                {
                    'description': 'яϧӡљçfπΓѽƍƳf͵ɟɇƿҾιҩʽŖπǆ\x8cŔқƈ\u0379lЂ',
                    'monitors': [
                            {
                                        'identifier': 4416174,
                                        'width': -3311019754303681619,
                                        'height': -6706893899914148140,
                                    },
                            {
                                        'identifier': 2669823,
                                        'width': -2101281561490981960,
                                        'height': -3334304569717614010,
                                    },
                            {
                                        'identifier': 9903420,
                                        'width': -54885754355727,
                                        'height': 8585528145325521719,
                                    },
                            {
                                        'identifier': 1678254,
                                        'width': 1213582077037481523,
                                        'height': 1290476604669476416,
                                    },
                            {
                                        'identifier': 530184,
                                        'width': 5966047180102651231,
                                        'height': -4595534421267670859,
                                    },
                            {
                                        'identifier': 3329300,
                                        'width': -600423362676942463,
                                        'height': -1052863759638208488,
                                    },
                            {
                                        'identifier': 2571765,
                                        'width': -7962206568061444054,
                                        'height': 3799775326204487528,
                                    },
                            {
                                        'identifier': 4148151,
                                        'width': 4363794435992037428,
                                        'height': -8920077901702794622,
                                    },
                            {
                                        'identifier': 1999965,
                                        'width': -3822445367478615838,
                                        'height': -4242947679769548971,
                                    },
                            {
                                        'identifier': 5197665,
                                        'width': -8152208634824051355,
                                        'height': -448306945043263012,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 892497,
                                        'source_nw_x_pixel': -8545627063166530770,
                                        'source_nw_y_pixel': -1553203775316110462,
                                        'source_pixel_width': -5973309875816664156,
                                        'source_pixel_height': -2735386950054513403,
                                        'rotation': -6623100717099547408,
                                        'virtual_nw_x_pixel': 1369554463,
                                        'virtual_nw_y_pixel': -1316125642,
                                        'virtual_width': 1585485525,
                                        'virtual_height': 896224530,
                                    },
                            {
                                        'source_monitor': 5469517,
                                        'source_nw_x_pixel': -4459536824360737907,
                                        'source_nw_y_pixel': -4176289982086402816,
                                        'source_pixel_width': -1671028748036820639,
                                        'source_pixel_height': -7827613799592381917,
                                        'rotation': -2045192353583334682,
                                        'virtual_nw_x_pixel': -1118308747,
                                        'virtual_nw_y_pixel': 248105694,
                                        'virtual_width': -600998866,
                                        'virtual_height': -557420508,
                                    },
                            {
                                        'source_monitor': 6229683,
                                        'source_nw_x_pixel': -1124296841034101381,
                                        'source_nw_y_pixel': -7682955284599075818,
                                        'source_pixel_width': -1592081964032451787,
                                        'source_pixel_height': -1387323075978224313,
                                        'rotation': -3139141834895416454,
                                        'virtual_nw_x_pixel': 1322023812,
                                        'virtual_nw_y_pixel': -945806886,
                                        'virtual_width': 1354943066,
                                        'virtual_height': -939493203,
                                    },
                            {
                                        'source_monitor': 7402427,
                                        'source_nw_x_pixel': -3931351533262559792,
                                        'source_nw_y_pixel': -7182067574035885595,
                                        'source_pixel_width': -6284795217681192972,
                                        'source_pixel_height': -6034141065150072204,
                                        'rotation': -8324415334222452811,
                                        'virtual_nw_x_pixel': 821547318,
                                        'virtual_nw_y_pixel': -1657071307,
                                        'virtual_width': -11171322,
                                        'virtual_height': 105909450,
                                    },
                            {
                                        'source_monitor': 7652760,
                                        'source_nw_x_pixel': -8659849864056767307,
                                        'source_nw_y_pixel': -7432790013172148520,
                                        'source_pixel_width': -4311461708082785380,
                                        'source_pixel_height': -8039321571081561340,
                                        'rotation': -8884906442388925417,
                                        'virtual_nw_x_pixel': 404286029,
                                        'virtual_nw_y_pixel': 319572601,
                                        'virtual_width': -1978903270,
                                        'virtual_height': -1641926829,
                                    },
                            {
                                        'source_monitor': 3978593,
                                        'source_nw_x_pixel': -1387880291661056011,
                                        'source_nw_y_pixel': -7136850185345328232,
                                        'source_pixel_width': -2109455088518418033,
                                        'source_pixel_height': -891279952588146151,
                                        'rotation': -6051506520561791881,
                                        'virtual_nw_x_pixel': -1900603160,
                                        'virtual_nw_y_pixel': -877452975,
                                        'virtual_width': 804468154,
                                        'virtual_height': 644852312,
                                    },
                            {
                                        'source_monitor': 9205117,
                                        'source_nw_x_pixel': -2697464515846438145,
                                        'source_nw_y_pixel': -614956950825960171,
                                        'source_pixel_width': -2585449698743944315,
                                        'source_pixel_height': -2133261746665853780,
                                        'rotation': -2432193186081200179,
                                        'virtual_nw_x_pixel': -792928503,
                                        'virtual_nw_y_pixel': -1668601746,
                                        'virtual_width': 936734040,
                                        'virtual_height': 749578448,
                                    },
                            {
                                        'source_monitor': 8873029,
                                        'source_nw_x_pixel': -6465313399172210318,
                                        'source_nw_y_pixel': -8212274248661922674,
                                        'source_pixel_width': -2858010726174923396,
                                        'source_pixel_height': -6004448230898050722,
                                        'rotation': -2152720394261043943,
                                        'virtual_nw_x_pixel': 230821903,
                                        'virtual_nw_y_pixel': -1831383919,
                                        'virtual_width': -1753745092,
                                        'virtual_height': 243841322,
                                    },
                            {
                                        'source_monitor': 7793180,
                                        'source_nw_x_pixel': -3981769385361110443,
                                        'source_nw_y_pixel': -243000923877790612,
                                        'source_pixel_width': -1656202850613094664,
                                        'source_pixel_height': -958602860713147287,
                                        'rotation': -5501672441208759054,
                                        'virtual_nw_x_pixel': -640823695,
                                        'virtual_nw_y_pixel': -835147204,
                                        'virtual_width': -348166530,
                                        'virtual_height': 738288121,
                                    },
                            {
                                        'source_monitor': 7504678,
                                        'source_nw_x_pixel': -2230684788954763058,
                                        'source_nw_y_pixel': -7341212900563609606,
                                        'source_pixel_width': -4761246211166993618,
                                        'source_pixel_height': -2897846796982659675,
                                        'rotation': -3228074667784077401,
                                        'virtual_nw_x_pixel': 199808884,
                                        'virtual_nw_y_pixel': -1638014889,
                                        'virtual_width': -1048406423,
                                        'virtual_height': -80563893,
                                    },
                        ],
                },
                {
                    'description': 'ƅƑˏˬԋʷŶoԋɅцҺѠҟK\x98\x8cԭлÁŨǑΑ',
                    'monitors': [
                            {
                                        'identifier': 1751425,
                                        'width': -9036102537851269921,
                                        'height': -4922082998383054304,
                                    },
                            {
                                        'identifier': 212744,
                                        'width': 7854291922590903324,
                                        'height': -7103512745275632392,
                                    },
                            {
                                        'identifier': 2006546,
                                        'width': 4262364421993949151,
                                        'height': -385625361994671934,
                                    },
                            {
                                        'identifier': -433225,
                                        'width': 5993637999260973890,
                                        'height': -6860237331262539923,
                                    },
                            {
                                        'identifier': -86207,
                                        'width': -575238505747822396,
                                        'height': -1896718670575825852,
                                    },
                            {
                                        'identifier': 3539590,
                                        'width': 7754532111218607244,
                                        'height': -6966429488739195240,
                                    },
                            {
                                        'identifier': 7302441,
                                        'width': -3474593815208450597,
                                        'height': 3411012610537010048,
                                    },
                            {
                                        'identifier': 9010549,
                                        'width': 3926446405876373660,
                                        'height': 2831074037623871515,
                                    },
                            {
                                        'identifier': 2011894,
                                        'width': -2394162593408975045,
                                        'height': -2409283966494405007,
                                    },
                            {
                                        'identifier': 7219687,
                                        'width': -5884360823155990635,
                                        'height': -1887506544712177844,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 164258,
                                        'source_nw_x_pixel': -3021714249340705114,
                                        'source_nw_y_pixel': -380107544945366877,
                                        'source_pixel_width': -7662358201562098377,
                                        'source_pixel_height': -2566300856446513815,
                                        'rotation': -3867730649037682437,
                                        'virtual_nw_x_pixel': -549631819,
                                        'virtual_nw_y_pixel': 1535365039,
                                        'virtual_width': 1032910260,
                                        'virtual_height': -1493693251,
                                    },
                            {
                                        'source_monitor': 5886313,
                                        'source_nw_x_pixel': -7531613243455553513,
                                        'source_nw_y_pixel': -4077187249667328252,
                                        'source_pixel_width': -9032983286710891139,
                                        'source_pixel_height': -7547623367114667741,
                                        'rotation': -5729942821516920589,
                                        'virtual_nw_x_pixel': -1908627865,
                                        'virtual_nw_y_pixel': 293018462,
                                        'virtual_width': 1981197357,
                                        'virtual_height': 1083923380,
                                    },
                            {
                                        'source_monitor': -68538,
                                        'source_nw_x_pixel': -5731392465838183479,
                                        'source_nw_y_pixel': -7472077059296461557,
                                        'source_pixel_width': -3582804927029400898,
                                        'source_pixel_height': -1828253928478749556,
                                        'rotation': -7526616686035599215,
                                        'virtual_nw_x_pixel': 1328390528,
                                        'virtual_nw_y_pixel': 1629484656,
                                        'virtual_width': -771042173,
                                        'virtual_height': -1113479348,
                                    },
                            {
                                        'source_monitor': 6534932,
                                        'source_nw_x_pixel': -5323463843678215502,
                                        'source_nw_y_pixel': -9027196404206382512,
                                        'source_pixel_width': -513976520028437899,
                                        'source_pixel_height': -901709562033626617,
                                        'rotation': -9197420362156842800,
                                        'virtual_nw_x_pixel': 1833195158,
                                        'virtual_nw_y_pixel': 66682402,
                                        'virtual_width': -1867862818,
                                        'virtual_height': -1369301015,
                                    },
                            {
                                        'source_monitor': -730327,
                                        'source_nw_x_pixel': -3255380969644114463,
                                        'source_nw_y_pixel': -3094643784751066130,
                                        'source_pixel_width': -7530391336579690861,
                                        'source_pixel_height': -779956517588848292,
                                        'rotation': -4387166850110823181,
                                        'virtual_nw_x_pixel': 1645651258,
                                        'virtual_nw_y_pixel': -1095054766,
                                        'virtual_width': 292068741,
                                        'virtual_height': 1113528584,
                                    },
                            {
                                        'source_monitor': 3727657,
                                        'source_nw_x_pixel': -2254731344950396956,
                                        'source_nw_y_pixel': -1841471746961635175,
                                        'source_pixel_width': -73966768284165567,
                                        'source_pixel_height': -7747213265383651827,
                                        'rotation': -1932728480668899676,
                                        'virtual_nw_x_pixel': -1542536204,
                                        'virtual_nw_y_pixel': 1086640875,
                                        'virtual_width': -1729327328,
                                        'virtual_height': 64049084,
                                    },
                            {
                                        'source_monitor': -515978,
                                        'source_nw_x_pixel': -9002270487200865027,
                                        'source_nw_y_pixel': -3991490513678121801,
                                        'source_pixel_width': -2403909192999766539,
                                        'source_pixel_height': -2776023790110775279,
                                        'rotation': -3586982724087425446,
                                        'virtual_nw_x_pixel': -1057745914,
                                        'virtual_nw_y_pixel': 562709615,
                                        'virtual_width': -1410600943,
                                        'virtual_height': 526565932,
                                    },
                            {
                                        'source_monitor': 4099596,
                                        'source_nw_x_pixel': -2561696512882602142,
                                        'source_nw_y_pixel': -6497624171468543934,
                                        'source_pixel_width': -7807368599566648453,
                                        'source_pixel_height': -7275987830997698902,
                                        'rotation': -7047044756524168761,
                                        'virtual_nw_x_pixel': 1546706522,
                                        'virtual_nw_y_pixel': -933384973,
                                        'virtual_width': 1393012533,
                                        'virtual_height': 1431868558,
                                    },
                            {
                                        'source_monitor': 7892336,
                                        'source_nw_x_pixel': -3270096127545298380,
                                        'source_nw_y_pixel': -4284815754891283744,
                                        'source_pixel_width': -1609102016508540090,
                                        'source_pixel_height': -2151595656689861349,
                                        'rotation': -3527391683857314072,
                                        'virtual_nw_x_pixel': 1054921670,
                                        'virtual_nw_y_pixel': -182987883,
                                        'virtual_width': 1308463525,
                                        'virtual_height': -168572211,
                                    },
                            {
                                        'source_monitor': 2634920,
                                        'source_nw_x_pixel': -3295002714695883388,
                                        'source_nw_y_pixel': -491515389178407100,
                                        'source_pixel_width': -2482758507439693512,
                                        'source_pixel_height': -2929578579406741625,
                                        'rotation': -772829337577234798,
                                        'virtual_nw_x_pixel': -436448331,
                                        'virtual_nw_y_pixel': 1016053938,
                                        'virtual_width': 279936855,
                                        'virtual_height': -1422736324,
                                    },
                        ],
                },
                {
                    'description': 'ѭίӹӂʏʟλǑǚťλҺƠԈǡүƫʳƗƋйчʸç?ŷҕëѫԫ',
                    'monitors': [
                            {
                                        'identifier': 9405780,
                                        'width': 3655654750671257471,
                                        'height': 6502870808906647436,
                                    },
                            {
                                        'identifier': 4685713,
                                        'width': -3395346798185075414,
                                        'height': -248726563355266866,
                                    },
                            {
                                        'identifier': 3373865,
                                        'width': -2622988856107155014,
                                        'height': -1816401895588167718,
                                    },
                            {
                                        'identifier': -22840,
                                        'width': 1739261332088883045,
                                        'height': -5139970298188306445,
                                    },
                            {
                                        'identifier': 8408603,
                                        'width': 2740433795546270475,
                                        'height': 5776837014840424897,
                                    },
                            {
                                        'identifier': 1346452,
                                        'width': -2784554726498922657,
                                        'height': 2351097279327096356,
                                    },
                            {
                                        'identifier': 8603512,
                                        'width': -2310059866969802083,
                                        'height': -394330754746613740,
                                    },
                            {
                                        'identifier': 5690973,
                                        'width': -4289002519909348049,
                                        'height': 1289909624588839620,
                                    },
                            {
                                        'identifier': 9349494,
                                        'width': 5586659213098727207,
                                        'height': -8864950471077633912,
                                    },
                            {
                                        'identifier': 436458,
                                        'width': 8826425956045503940,
                                        'height': -3885686791441005069,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6663299,
                                        'source_nw_x_pixel': -2767873708897116823,
                                        'source_nw_y_pixel': -8911477364322617465,
                                        'source_pixel_width': -5179039026677320079,
                                        'source_pixel_height': -6526231951483666152,
                                        'rotation': -4110421578524950265,
                                        'virtual_nw_x_pixel': -1746114977,
                                        'virtual_nw_y_pixel': 86135788,
                                        'virtual_width': 1402675600,
                                        'virtual_height': 332569463,
                                    },
                            {
                                        'source_monitor': 3265361,
                                        'source_nw_x_pixel': -8832080398697708134,
                                        'source_nw_y_pixel': -6448767608236561735,
                                        'source_pixel_width': -7236779346100874929,
                                        'source_pixel_height': -7362299396994099406,
                                        'rotation': -3247961212287789285,
                                        'virtual_nw_x_pixel': 20119642,
                                        'virtual_nw_y_pixel': -449031395,
                                        'virtual_width': 1395015353,
                                        'virtual_height': 328338288,
                                    },
                            {
                                        'source_monitor': -753396,
                                        'source_nw_x_pixel': -6232486931021964629,
                                        'source_nw_y_pixel': -9144146745224865736,
                                        'source_pixel_width': -2422162280086989776,
                                        'source_pixel_height': -7713083861934974698,
                                        'rotation': -4322599737170543863,
                                        'virtual_nw_x_pixel': -978189239,
                                        'virtual_nw_y_pixel': 283499188,
                                        'virtual_width': -701587648,
                                        'virtual_height': 693038861,
                                    },
                            {
                                        'source_monitor': 901875,
                                        'source_nw_x_pixel': -4852785684883412796,
                                        'source_nw_y_pixel': -4975419637888855591,
                                        'source_pixel_width': -5949480850611503034,
                                        'source_pixel_height': -8032171011480341439,
                                        'rotation': -6932674052640974011,
                                        'virtual_nw_x_pixel': 1863770115,
                                        'virtual_nw_y_pixel': 477577117,
                                        'virtual_width': -19840916,
                                        'virtual_height': 1934480467,
                                    },
                            {
                                        'source_monitor': 8533269,
                                        'source_nw_x_pixel': -6149497947216598218,
                                        'source_nw_y_pixel': -4553296430136043125,
                                        'source_pixel_width': -659279801895467474,
                                        'source_pixel_height': -1107433979398317313,
                                        'rotation': -8202189687408402490,
                                        'virtual_nw_x_pixel': -1178649015,
                                        'virtual_nw_y_pixel': 600047796,
                                        'virtual_width': -1255554851,
                                        'virtual_height': -1189362014,
                                    },
                            {
                                        'source_monitor': -777214,
                                        'source_nw_x_pixel': -6102835909798610587,
                                        'source_nw_y_pixel': -190345132079400208,
                                        'source_pixel_width': -976973682299601777,
                                        'source_pixel_height': -2200819026541310547,
                                        'rotation': -121437423514605051,
                                        'virtual_nw_x_pixel': -490703680,
                                        'virtual_nw_y_pixel': 395302472,
                                        'virtual_width': 1753346562,
                                        'virtual_height': 1180901127,
                                    },
                            {
                                        'source_monitor': 3943781,
                                        'source_nw_x_pixel': -2506523931774714626,
                                        'source_nw_y_pixel': -5705922796802316742,
                                        'source_pixel_width': -3236919344008715285,
                                        'source_pixel_height': -7652337461838025322,
                                        'rotation': -4156537337071243561,
                                        'virtual_nw_x_pixel': -546563777,
                                        'virtual_nw_y_pixel': -466463036,
                                        'virtual_width': -948014270,
                                        'virtual_height': -1043001665,
                                    },
                            {
                                        'source_monitor': 7886119,
                                        'source_nw_x_pixel': -8824751857947578037,
                                        'source_nw_y_pixel': -7612256200170578291,
                                        'source_pixel_width': -2019003539399383390,
                                        'source_pixel_height': -1734004595415969381,
                                        'rotation': -2306006287885506441,
                                        'virtual_nw_x_pixel': -125770113,
                                        'virtual_nw_y_pixel': 1974281563,
                                        'virtual_width': -315615416,
                                        'virtual_height': -1170238254,
                                    },
                            {
                                        'source_monitor': 2321827,
                                        'source_nw_x_pixel': -3694412684668054587,
                                        'source_nw_y_pixel': -4825976372509940492,
                                        'source_pixel_width': -4576055005772808509,
                                        'source_pixel_height': -4494976475302513472,
                                        'rotation': -7896809523409891525,
                                        'virtual_nw_x_pixel': -68705480,
                                        'virtual_nw_y_pixel': 1772999308,
                                        'virtual_width': 1410094664,
                                        'virtual_height': -1054407280,
                                    },
                            {
                                        'source_monitor': 8835857,
                                        'source_nw_x_pixel': -8328413306852021146,
                                        'source_nw_y_pixel': -2453870634160659635,
                                        'source_pixel_width': -2313944628235042779,
                                        'source_pixel_height': -4040360874451617225,
                                        'rotation': -8855485868775142053,
                                        'virtual_nw_x_pixel': -611430658,
                                        'virtual_nw_y_pixel': 974684551,
                                        'virtual_width': 1778428204,
                                        'virtual_height': 1096559644,
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
                                        'identifier': 164342,
                                        'width': 8486378008018669994,
                                        'height': -5390673193782728001,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -858698724717820168,
                                        'source_nw_y_pixel': -7405505422702274503,
                                        'source_pixel_width': -5030293082952124079,
                                        'source_pixel_height': -6425498485557702799,
                                        'rotation': -5634232814644904095,
                                        'virtual_nw_x_pixel': 155839762,
                                        'virtual_nw_y_pixel': 641876903,
                                        'virtual_width': -860104067,
                                        'virtual_height': 1665099783,
                                    },
                        ],
                },
            ],

        },
    ),
]
