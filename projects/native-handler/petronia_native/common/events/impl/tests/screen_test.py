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
            'identifier': -193859,
            'width': 7941907106971924278,
            'height': 4665167148307818867,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 2271423,

            'width': 5966916122279720409,

            'height': 909272129724274771,

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
            'source_monitor': 1875404,
            'source_nw_x_pixel': -694851915536140486,
            'source_nw_y_pixel': -1412572304274481787,
            'source_pixel_width': -3667475471616940245,
            'source_pixel_height': -3321711679504251189,
            'rotation': -630895510652367096,
            'virtual_nw_x_pixel': 439169852,
            'virtual_nw_y_pixel': 579491468,
            'virtual_width': 423080292,
            'virtual_height': 635675380,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -6484137811492459732,

            'source_nw_y_pixel': -2092744072239981741,

            'source_pixel_width': -2299356238769688039,

            'source_pixel_height': -5815757414602655853,

            'rotation': -8737074823306328718,

            'virtual_nw_x_pixel': 1219841372,

            'virtual_nw_y_pixel': -810274193,

            'virtual_width': 1992088550,

            'virtual_height': -1659000404,

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
            'description': 'ҸǝЯҚîeBϚӏԦƖnƫɍǡıKɬщБɾɘǥɹΕҕѓ҇λß',
            'monitors': [
                {
                    'identifier': -726023,
                    'width': -5930614949573960714,
                    'height': 3247805162521809184,
                },
                {
                    'identifier': -869762,
                    'width': 3525973409185945264,
                    'height': -7410136987396218986,
                },
                {
                    'identifier': 6854382,
                    'width': -238019173628456752,
                    'height': -5760324132516568961,
                },
                {
                    'identifier': 2585532,
                    'width': -5395354725957993005,
                    'height': -6851834529170170553,
                },
                {
                    'identifier': -497020,
                    'width': 6923537563594161549,
                    'height': 5989448698510629672,
                },
                {
                    'identifier': -752796,
                    'width': -4908323426051747816,
                    'height': 1085619342192105299,
                },
                {
                    'identifier': 7608167,
                    'width': 7691323917092398943,
                    'height': 6059718101854531932,
                },
                {
                    'identifier': 1324679,
                    'width': 4022222109793995878,
                    'height': -864416009546075405,
                },
                {
                    'identifier': 9738923,
                    'width': 4887460954528869752,
                    'height': 3753771092213358341,
                },
                {
                    'identifier': -926787,
                    'width': -4000980901356342764,
                    'height': -1254592663925325726,
                },
            ],
            'screen': [
                {
                    'source_monitor': 3272374,
                    'source_nw_x_pixel': -8307805239987362095,
                    'source_nw_y_pixel': -182720633368914191,
                    'source_pixel_width': -3051510628927551754,
                    'source_pixel_height': -7304394628037967728,
                    'rotation': -6305975208271385103,
                    'virtual_nw_x_pixel': 1067067239,
                    'virtual_nw_y_pixel': -1918468952,
                    'virtual_width': 1723895721,
                    'virtual_height': 591593253,
                },
                {
                    'source_monitor': 456721,
                    'source_nw_x_pixel': -6003211235333592479,
                    'source_nw_y_pixel': -7838930638183092570,
                    'source_pixel_width': -5584148360222376906,
                    'source_pixel_height': -948013321678449131,
                    'rotation': -5371407573388882115,
                    'virtual_nw_x_pixel': 1965526564,
                    'virtual_nw_y_pixel': -1997891316,
                    'virtual_width': -1311279104,
                    'virtual_height': 1579860137,
                },
                {
                    'source_monitor': 5896918,
                    'source_nw_x_pixel': -2929190138339827620,
                    'source_nw_y_pixel': -7378137735604053523,
                    'source_pixel_width': -7811113252150948284,
                    'source_pixel_height': -6748755362500160482,
                    'rotation': -6836947077293050686,
                    'virtual_nw_x_pixel': -1617830229,
                    'virtual_nw_y_pixel': 297300327,
                    'virtual_width': 1663763617,
                    'virtual_height': 648121994,
                },
                {
                    'source_monitor': 1653022,
                    'source_nw_x_pixel': -6355091181695264509,
                    'source_nw_y_pixel': -6266279646238766701,
                    'source_pixel_width': -6590417255578369073,
                    'source_pixel_height': -2350486058259844229,
                    'rotation': -1596493629573754139,
                    'virtual_nw_x_pixel': 580473814,
                    'virtual_nw_y_pixel': 1889744259,
                    'virtual_width': -1368445084,
                    'virtual_height': -1590457532,
                },
                {
                    'source_monitor': 9593275,
                    'source_nw_x_pixel': -6944908148856656806,
                    'source_nw_y_pixel': -8074772905167674657,
                    'source_pixel_width': -8591813842136683743,
                    'source_pixel_height': -4514062758357372712,
                    'rotation': -5177066180536986629,
                    'virtual_nw_x_pixel': -1996123946,
                    'virtual_nw_y_pixel': -1957703536,
                    'virtual_width': -1730559355,
                    'virtual_height': -221129353,
                },
                {
                    'source_monitor': 3495506,
                    'source_nw_x_pixel': -4479474630313936067,
                    'source_nw_y_pixel': -3542495422727418241,
                    'source_pixel_width': -691575128519103198,
                    'source_pixel_height': -7812671929539930825,
                    'rotation': -8537987807417433052,
                    'virtual_nw_x_pixel': -1490205459,
                    'virtual_nw_y_pixel': 1391948832,
                    'virtual_width': -981691979,
                    'virtual_height': -1292614988,
                },
                {
                    'source_monitor': 3091266,
                    'source_nw_x_pixel': -287313313216908849,
                    'source_nw_y_pixel': -4777275902305999336,
                    'source_pixel_width': -1438435702289224630,
                    'source_pixel_height': -5190874600921175786,
                    'rotation': -3687122847463556707,
                    'virtual_nw_x_pixel': -1299030564,
                    'virtual_nw_y_pixel': 708286665,
                    'virtual_width': -833847294,
                    'virtual_height': 590885269,
                },
                {
                    'source_monitor': 3989136,
                    'source_nw_x_pixel': -2868772181551142472,
                    'source_nw_y_pixel': -4716578925249607510,
                    'source_pixel_width': -8111400112025995633,
                    'source_pixel_height': -6702029881810324808,
                    'rotation': -101928328242619802,
                    'virtual_nw_x_pixel': 939264603,
                    'virtual_nw_y_pixel': 1870587406,
                    'virtual_width': -337805224,
                    'virtual_height': -424134963,
                },
                {
                    'source_monitor': 8685808,
                    'source_nw_x_pixel': -2403373020705051155,
                    'source_nw_y_pixel': -523645367171203775,
                    'source_pixel_width': -7991252358045330215,
                    'source_pixel_height': -7816586259430927121,
                    'rotation': -1035976982074730176,
                    'virtual_nw_x_pixel': -657572794,
                    'virtual_nw_y_pixel': -108965052,
                    'virtual_width': 1745539997,
                    'virtual_height': -1847407985,
                },
                {
                    'source_monitor': 3579742,
                    'source_nw_x_pixel': -7813939489700399181,
                    'source_nw_y_pixel': -4687709677164273234,
                    'source_pixel_width': -7032146882477491272,
                    'source_pixel_height': -6808084593283045402,
                    'rotation': -8225668315908839681,
                    'virtual_nw_x_pixel': 1495655214,
                    'virtual_nw_y_pixel': 1121053735,
                    'virtual_width': -1140292898,
                    'virtual_height': -425653462,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 4399234,
                    'width': -7825602508454989381,
                    'height': -5878793364325030266,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -5346467102647581839,
                    'source_nw_y_pixel': -1663109549136165718,
                    'source_pixel_width': -7712076015326864930,
                    'source_pixel_height': -5279065223340522187,
                    'rotation': -5293719325125245958,
                    'virtual_nw_x_pixel': 1796111388,
                    'virtual_nw_y_pixel': -1945634997,
                    'virtual_width': 1399891208,
                    'virtual_height': -1920913030,
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
            'request_id': 6511298,
            'mapped_screens_by_monitors': [
                {
                    'description': 'ʊӐˢӌϤϧξǻѶ\x8bƪйxхƴϝӲԃȬȀùЬρΒŘѤѦ]ŻĻ',
                    'monitors': [
                            {
                                        'identifier': 5710764,
                                        'width': -6240252450380027190,
                                        'height': 669435623009322933,
                                    },
                            {
                                        'identifier': 3597730,
                                        'width': -3734921762591249005,
                                        'height': 312616821558416353,
                                    },
                            {
                                        'identifier': 5031905,
                                        'width': -6224752471647774459,
                                        'height': -2226460323610103344,
                                    },
                            {
                                        'identifier': 7409539,
                                        'width': 4937502491182471326,
                                        'height': -562240446409736439,
                                    },
                            {
                                        'identifier': 1781018,
                                        'width': -8104504117591184117,
                                        'height': -3608273054137590013,
                                    },
                            {
                                        'identifier': 1364098,
                                        'width': 8111339964639706746,
                                        'height': 3162209689396619939,
                                    },
                            {
                                        'identifier': 2440547,
                                        'width': -2044213534423391504,
                                        'height': -6926112689895681211,
                                    },
                            {
                                        'identifier': 8346370,
                                        'width': 3248333957703821227,
                                        'height': 738283790287788890,
                                    },
                            {
                                        'identifier': -713104,
                                        'width': 4430416977206314497,
                                        'height': 864616882384203850,
                                    },
                            {
                                        'identifier': 8326571,
                                        'width': -2015109166332870646,
                                        'height': 7656250923156719353,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2522523,
                                        'source_nw_x_pixel': -8951456185890599710,
                                        'source_nw_y_pixel': -3763918355477699722,
                                        'source_pixel_width': -3610562605103699167,
                                        'source_pixel_height': -6552192962214572302,
                                        'rotation': -5398724810211926268,
                                        'virtual_nw_x_pixel': 1328605340,
                                        'virtual_nw_y_pixel': 1398787169,
                                        'virtual_width': -1467984727,
                                        'virtual_height': 146578456,
                                    },
                            {
                                        'source_monitor': 5915676,
                                        'source_nw_x_pixel': -7183286717605912116,
                                        'source_nw_y_pixel': -4122449455034743392,
                                        'source_pixel_width': -3080039593414062454,
                                        'source_pixel_height': -8545153147183313145,
                                        'rotation': -5521104259057357311,
                                        'virtual_nw_x_pixel': -1881663396,
                                        'virtual_nw_y_pixel': 674044620,
                                        'virtual_width': -1842966824,
                                        'virtual_height': 1996689780,
                                    },
                            {
                                        'source_monitor': 5453675,
                                        'source_nw_x_pixel': -4192001994693955993,
                                        'source_nw_y_pixel': -1811678618267369859,
                                        'source_pixel_width': -6741662056195173752,
                                        'source_pixel_height': -145339032458956640,
                                        'rotation': -6813285499068874905,
                                        'virtual_nw_x_pixel': 1358284659,
                                        'virtual_nw_y_pixel': 1232277208,
                                        'virtual_width': -1527320377,
                                        'virtual_height': -976586660,
                                    },
                            {
                                        'source_monitor': 6335584,
                                        'source_nw_x_pixel': -8176591877233974669,
                                        'source_nw_y_pixel': -1199917029123158348,
                                        'source_pixel_width': -558946954093323970,
                                        'source_pixel_height': -9169458843565793913,
                                        'rotation': -7220184229760919988,
                                        'virtual_nw_x_pixel': -586574259,
                                        'virtual_nw_y_pixel': -1464751084,
                                        'virtual_width': 1275171665,
                                        'virtual_height': -1361900943,
                                    },
                            {
                                        'source_monitor': 8346779,
                                        'source_nw_x_pixel': -6174718134822132165,
                                        'source_nw_y_pixel': -8257973142944889312,
                                        'source_pixel_width': -5824867189421589854,
                                        'source_pixel_height': -7127334982245455335,
                                        'rotation': -2149801507696083730,
                                        'virtual_nw_x_pixel': -668059518,
                                        'virtual_nw_y_pixel': 1744409204,
                                        'virtual_width': -162471922,
                                        'virtual_height': 1115056536,
                                    },
                            {
                                        'source_monitor': 7966340,
                                        'source_nw_x_pixel': -961878991646359478,
                                        'source_nw_y_pixel': -3261365016748858516,
                                        'source_pixel_width': -5088193801584603281,
                                        'source_pixel_height': -3494875088000653024,
                                        'rotation': -2731601764107457391,
                                        'virtual_nw_x_pixel': 804991008,
                                        'virtual_nw_y_pixel': 754553214,
                                        'virtual_width': -1303511784,
                                        'virtual_height': 316302409,
                                    },
                            {
                                        'source_monitor': 5769688,
                                        'source_nw_x_pixel': -5168903828289343087,
                                        'source_nw_y_pixel': -5302890048740102136,
                                        'source_pixel_width': -3906187813779031886,
                                        'source_pixel_height': -7797229238034201203,
                                        'rotation': -7623213305927384606,
                                        'virtual_nw_x_pixel': 1462732021,
                                        'virtual_nw_y_pixel': 1775964215,
                                        'virtual_width': -1736522083,
                                        'virtual_height': 718808335,
                                    },
                            {
                                        'source_monitor': 1036654,
                                        'source_nw_x_pixel': -6560807039503247821,
                                        'source_nw_y_pixel': -6214812142584775731,
                                        'source_pixel_width': -7558389129929588283,
                                        'source_pixel_height': -8557335440301717099,
                                        'rotation': -6875194299975433445,
                                        'virtual_nw_x_pixel': -843386665,
                                        'virtual_nw_y_pixel': 1538278565,
                                        'virtual_width': 446780017,
                                        'virtual_height': -1869635034,
                                    },
                            {
                                        'source_monitor': 1181818,
                                        'source_nw_x_pixel': -6525240591656953190,
                                        'source_nw_y_pixel': -5166122084554143392,
                                        'source_pixel_width': -728732582065084314,
                                        'source_pixel_height': -2355465192394807683,
                                        'rotation': -5612743165106500663,
                                        'virtual_nw_x_pixel': -1901167992,
                                        'virtual_nw_y_pixel': 837973266,
                                        'virtual_width': 781000685,
                                        'virtual_height': -613643987,
                                    },
                            {
                                        'source_monitor': 1466313,
                                        'source_nw_x_pixel': -3708369724944956887,
                                        'source_nw_y_pixel': -7240131139815126014,
                                        'source_pixel_width': -7490029824584217586,
                                        'source_pixel_height': -3568434864035550572,
                                        'rotation': -125891753328419219,
                                        'virtual_nw_x_pixel': -1886077527,
                                        'virtual_nw_y_pixel': 1352590656,
                                        'virtual_width': 1062705959,
                                        'virtual_height': 1606079780,
                                    },
                        ],
                },
                {
                    'description': 'HÎƲėÖɭΏͲӥМƎȋΔ\u03a2ғ҃ȭӏ˚\x85вԎşƱ\x9dБ¥ϟԂ\x87',
                    'monitors': [
                            {
                                        'identifier': 9738170,
                                        'width': 9101224792119371344,
                                        'height': 5638707261973073321,
                                    },
                            {
                                        'identifier': 6908955,
                                        'width': 570258085628090796,
                                        'height': 2800535963080361720,
                                    },
                            {
                                        'identifier': 3962570,
                                        'width': 489792625821244073,
                                        'height': 8439997340211175118,
                                    },
                            {
                                        'identifier': 7743470,
                                        'width': 4029931045360117170,
                                        'height': 2371127597398543980,
                                    },
                            {
                                        'identifier': -486281,
                                        'width': -3482384815394124424,
                                        'height': -4407452555818622636,
                                    },
                            {
                                        'identifier': 276312,
                                        'width': -2403446051384081886,
                                        'height': 4792597292597419857,
                                    },
                            {
                                        'identifier': 5672783,
                                        'width': -1341985229107627544,
                                        'height': 2471400092103140613,
                                    },
                            {
                                        'identifier': 8235071,
                                        'width': 3897685958694486316,
                                        'height': -5354273356045960544,
                                    },
                            {
                                        'identifier': -181672,
                                        'width': 1668639483799371468,
                                        'height': 9042002890114664965,
                                    },
                            {
                                        'identifier': 4676893,
                                        'width': 6778983579259591184,
                                        'height': -9150100036976076765,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9950619,
                                        'source_nw_x_pixel': -7002024032524310417,
                                        'source_nw_y_pixel': -5542360085458426279,
                                        'source_pixel_width': -6361153834577938904,
                                        'source_pixel_height': -3872453821023601151,
                                        'rotation': -5882115179972289013,
                                        'virtual_nw_x_pixel': -327622662,
                                        'virtual_nw_y_pixel': 1891396139,
                                        'virtual_width': 1171723745,
                                        'virtual_height': -178695650,
                                    },
                            {
                                        'source_monitor': 2851610,
                                        'source_nw_x_pixel': -8017948032757132228,
                                        'source_nw_y_pixel': -3228527932221123159,
                                        'source_pixel_width': -3498324933699391718,
                                        'source_pixel_height': -7583135347660602916,
                                        'rotation': -6898143953602033844,
                                        'virtual_nw_x_pixel': 1781554081,
                                        'virtual_nw_y_pixel': 1545322158,
                                        'virtual_width': -1767899055,
                                        'virtual_height': 18892131,
                                    },
                            {
                                        'source_monitor': 1075506,
                                        'source_nw_x_pixel': -3177223897269626691,
                                        'source_nw_y_pixel': -6601734986119644104,
                                        'source_pixel_width': -7002625016019089328,
                                        'source_pixel_height': -386052586045013168,
                                        'rotation': -5873299377002134860,
                                        'virtual_nw_x_pixel': 1323003024,
                                        'virtual_nw_y_pixel': 1441821290,
                                        'virtual_width': -1778907987,
                                        'virtual_height': -1785757032,
                                    },
                            {
                                        'source_monitor': 893325,
                                        'source_nw_x_pixel': -6005112169038850851,
                                        'source_nw_y_pixel': -9087521381386371630,
                                        'source_pixel_width': -4580302457152702238,
                                        'source_pixel_height': -4651934370749235228,
                                        'rotation': -5343234419964724064,
                                        'virtual_nw_x_pixel': -1394331133,
                                        'virtual_nw_y_pixel': -778512605,
                                        'virtual_width': -1488528814,
                                        'virtual_height': 1873813224,
                                    },
                            {
                                        'source_monitor': 9614937,
                                        'source_nw_x_pixel': -8444301444214977467,
                                        'source_nw_y_pixel': -4517503541662469890,
                                        'source_pixel_width': -4229251357825995395,
                                        'source_pixel_height': -6883865899945356252,
                                        'rotation': -4665474707894133673,
                                        'virtual_nw_x_pixel': -424362470,
                                        'virtual_nw_y_pixel': -1627264709,
                                        'virtual_width': 1142177284,
                                        'virtual_height': -1208421047,
                                    },
                            {
                                        'source_monitor': 6218715,
                                        'source_nw_x_pixel': -6350040479541497759,
                                        'source_nw_y_pixel': -9140421676986884327,
                                        'source_pixel_width': -1358191952045805858,
                                        'source_pixel_height': -6606173080484371662,
                                        'rotation': -6320444430115626927,
                                        'virtual_nw_x_pixel': 331416341,
                                        'virtual_nw_y_pixel': 887115908,
                                        'virtual_width': -1863980065,
                                        'virtual_height': 656928440,
                                    },
                            {
                                        'source_monitor': 6096677,
                                        'source_nw_x_pixel': -4098382626852969306,
                                        'source_nw_y_pixel': -487073385475019093,
                                        'source_pixel_width': -8869133274062251126,
                                        'source_pixel_height': -4721954432229487787,
                                        'rotation': -7244071779114443924,
                                        'virtual_nw_x_pixel': 1581261748,
                                        'virtual_nw_y_pixel': -1511642023,
                                        'virtual_width': -730759767,
                                        'virtual_height': -1013150065,
                                    },
                            {
                                        'source_monitor': 2210197,
                                        'source_nw_x_pixel': -2254087114437138901,
                                        'source_nw_y_pixel': -7570833407562836359,
                                        'source_pixel_width': -4802977373317470184,
                                        'source_pixel_height': -834208527474873082,
                                        'rotation': -6368398550033336333,
                                        'virtual_nw_x_pixel': -1013427432,
                                        'virtual_nw_y_pixel': 461694846,
                                        'virtual_width': -677409297,
                                        'virtual_height': 1509869174,
                                    },
                            {
                                        'source_monitor': 9290236,
                                        'source_nw_x_pixel': -1512896646884726942,
                                        'source_nw_y_pixel': -8290922809695193277,
                                        'source_pixel_width': -5092531155677108258,
                                        'source_pixel_height': -1123914011033572404,
                                        'rotation': -2711967470107358288,
                                        'virtual_nw_x_pixel': -441190339,
                                        'virtual_nw_y_pixel': 847373301,
                                        'virtual_width': 1237505636,
                                        'virtual_height': 27164332,
                                    },
                            {
                                        'source_monitor': 8404685,
                                        'source_nw_x_pixel': -6787221563053896733,
                                        'source_nw_y_pixel': -5385668700136634081,
                                        'source_pixel_width': -4343620379462399025,
                                        'source_pixel_height': -8587033267177185366,
                                        'rotation': -5111515331628384656,
                                        'virtual_nw_x_pixel': -1878534986,
                                        'virtual_nw_y_pixel': -1566160417,
                                        'virtual_width': -774088046,
                                        'virtual_height': 1308267846,
                                    },
                        ],
                },
                {
                    'description': 'ư˚ȩϥ®/˻=ȼфΣ?ǧǞϤǣǅðӔԔҡĝƽԝǨĊЇͽiɆ',
                    'monitors': [
                            {
                                        'identifier': 7914304,
                                        'width': 2619906821479930853,
                                        'height': 6664056244067282404,
                                    },
                            {
                                        'identifier': 8741113,
                                        'width': 3400611702984061610,
                                        'height': -6428974816722974498,
                                    },
                            {
                                        'identifier': 9322088,
                                        'width': -5180345313253947906,
                                        'height': -2532458471656207331,
                                    },
                            {
                                        'identifier': 4286493,
                                        'width': -3540153379889271755,
                                        'height': -285473464526791646,
                                    },
                            {
                                        'identifier': 878657,
                                        'width': -535318226565571132,
                                        'height': 8386891684910871555,
                                    },
                            {
                                        'identifier': 653846,
                                        'width': -4797776956364799555,
                                        'height': 679635668477230551,
                                    },
                            {
                                        'identifier': 58278,
                                        'width': -4096701764196968194,
                                        'height': 1000721059870265739,
                                    },
                            {
                                        'identifier': 6486457,
                                        'width': 7863067848889078961,
                                        'height': -5521203907140148735,
                                    },
                            {
                                        'identifier': 3833321,
                                        'width': -8392390170046216687,
                                        'height': -1303234143330060061,
                                    },
                            {
                                        'identifier': 4726476,
                                        'width': 78081002505133904,
                                        'height': -162033171774069090,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2693134,
                                        'source_nw_x_pixel': -7793706098962955681,
                                        'source_nw_y_pixel': -3891997157502267411,
                                        'source_pixel_width': -2800695297830151788,
                                        'source_pixel_height': -8371329445714718939,
                                        'rotation': -5501389631762946946,
                                        'virtual_nw_x_pixel': 1415171099,
                                        'virtual_nw_y_pixel': 1140887199,
                                        'virtual_width': -146523145,
                                        'virtual_height': 110014012,
                                    },
                            {
                                        'source_monitor': 4082255,
                                        'source_nw_x_pixel': -751161939626312250,
                                        'source_nw_y_pixel': -8370636469994525970,
                                        'source_pixel_width': -7970686455462782976,
                                        'source_pixel_height': -1350612627347279284,
                                        'rotation': -1528228811086117476,
                                        'virtual_nw_x_pixel': 1505712869,
                                        'virtual_nw_y_pixel': 1253447179,
                                        'virtual_width': -910598826,
                                        'virtual_height': 1119563711,
                                    },
                            {
                                        'source_monitor': 3638742,
                                        'source_nw_x_pixel': -2213677136398857997,
                                        'source_nw_y_pixel': -7540698835899716226,
                                        'source_pixel_width': -1605284786098453137,
                                        'source_pixel_height': -8984343706930070771,
                                        'rotation': -1609785732647912366,
                                        'virtual_nw_x_pixel': -1598033766,
                                        'virtual_nw_y_pixel': -1796967188,
                                        'virtual_width': -1416095851,
                                        'virtual_height': 852308170,
                                    },
                            {
                                        'source_monitor': 9958745,
                                        'source_nw_x_pixel': -3573264422726704662,
                                        'source_nw_y_pixel': -7631604042096798290,
                                        'source_pixel_width': -4731163350228031347,
                                        'source_pixel_height': -7038500073912247863,
                                        'rotation': -5556338758126690524,
                                        'virtual_nw_x_pixel': -1114167805,
                                        'virtual_nw_y_pixel': -32996067,
                                        'virtual_width': 345316435,
                                        'virtual_height': 1012699532,
                                    },
                            {
                                        'source_monitor': -9250,
                                        'source_nw_x_pixel': -1305203935726805287,
                                        'source_nw_y_pixel': -4535927188929356587,
                                        'source_pixel_width': -6390397363941738804,
                                        'source_pixel_height': -7681551429177603818,
                                        'rotation': -4291298228199973226,
                                        'virtual_nw_x_pixel': -1195753387,
                                        'virtual_nw_y_pixel': -537777824,
                                        'virtual_width': -126752366,
                                        'virtual_height': 731511521,
                                    },
                            {
                                        'source_monitor': 8814772,
                                        'source_nw_x_pixel': -2896561756763279189,
                                        'source_nw_y_pixel': -9131125928137200092,
                                        'source_pixel_width': -8755049252602404908,
                                        'source_pixel_height': -2316490749846621698,
                                        'rotation': -4600904151873114131,
                                        'virtual_nw_x_pixel': 802809361,
                                        'virtual_nw_y_pixel': 1926618491,
                                        'virtual_width': -1529594654,
                                        'virtual_height': -1614328254,
                                    },
                            {
                                        'source_monitor': 408176,
                                        'source_nw_x_pixel': -896189548762110447,
                                        'source_nw_y_pixel': -2846458305261635693,
                                        'source_pixel_width': -4081597054943534204,
                                        'source_pixel_height': -298250816322952070,
                                        'rotation': -4060120213257603521,
                                        'virtual_nw_x_pixel': 846084024,
                                        'virtual_nw_y_pixel': 1246766567,
                                        'virtual_width': -1960929739,
                                        'virtual_height': -217487797,
                                    },
                            {
                                        'source_monitor': 4346782,
                                        'source_nw_x_pixel': -8795641804880784995,
                                        'source_nw_y_pixel': -8646254945348416064,
                                        'source_pixel_width': -2046891580215113992,
                                        'source_pixel_height': -4211258616672890922,
                                        'rotation': -7150772822651054190,
                                        'virtual_nw_x_pixel': -727884872,
                                        'virtual_nw_y_pixel': -1869459867,
                                        'virtual_width': 1182300749,
                                        'virtual_height': 1702187865,
                                    },
                            {
                                        'source_monitor': 5174617,
                                        'source_nw_x_pixel': -7346226904597930067,
                                        'source_nw_y_pixel': -6359172175916046103,
                                        'source_pixel_width': -3974398769473498028,
                                        'source_pixel_height': -2623322378706943444,
                                        'rotation': -5504448290232071699,
                                        'virtual_nw_x_pixel': -1592084776,
                                        'virtual_nw_y_pixel': 834347142,
                                        'virtual_width': -1621361546,
                                        'virtual_height': -495150672,
                                    },
                            {
                                        'source_monitor': -415000,
                                        'source_nw_x_pixel': -7851679942712885887,
                                        'source_nw_y_pixel': -5502009605441542769,
                                        'source_pixel_width': -1309878278784258472,
                                        'source_pixel_height': -2172690447634278014,
                                        'rotation': -6987641660108366397,
                                        'virtual_nw_x_pixel': -1483787524,
                                        'virtual_nw_y_pixel': -161193810,
                                        'virtual_width': -100708699,
                                        'virtual_height': -1954910948,
                                    },
                        ],
                },
                {
                    'description': '\x9dȺǉв\x85ŮȻȬǋτN\\©ҦʾϤƼϏԂӒŜѝ51έĂż©˳~',
                    'monitors': [
                            {
                                        'identifier': 514727,
                                        'width': -4764190999041332821,
                                        'height': 3481841025248663014,
                                    },
                            {
                                        'identifier': 8657106,
                                        'width': 8058325321197641334,
                                        'height': 3246863222165208440,
                                    },
                            {
                                        'identifier': 2819907,
                                        'width': 3677581115680734720,
                                        'height': 1491894362788102433,
                                    },
                            {
                                        'identifier': 5605541,
                                        'width': -5784993584954222581,
                                        'height': 7531789644524698338,
                                    },
                            {
                                        'identifier': 2431736,
                                        'width': 805819176352385339,
                                        'height': -1948283022337620580,
                                    },
                            {
                                        'identifier': 7885425,
                                        'width': -7553723808425431819,
                                        'height': -14412842913225288,
                                    },
                            {
                                        'identifier': 8692705,
                                        'width': 8305132845079708534,
                                        'height': 8031362435130278008,
                                    },
                            {
                                        'identifier': 6880615,
                                        'width': 8063491913347944939,
                                        'height': -2103374281034570570,
                                    },
                            {
                                        'identifier': 7981217,
                                        'width': -6938023494684548844,
                                        'height': 8401610629625689283,
                                    },
                            {
                                        'identifier': 2398006,
                                        'width': 4762499703551197316,
                                        'height': 105034209021397355,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4863514,
                                        'source_nw_x_pixel': -5180522906448982419,
                                        'source_nw_y_pixel': -621985007664156787,
                                        'source_pixel_width': -8034416332915630482,
                                        'source_pixel_height': -5142022624934151654,
                                        'rotation': -1198258097124325842,
                                        'virtual_nw_x_pixel': -1912141835,
                                        'virtual_nw_y_pixel': 80958763,
                                        'virtual_width': 1099864620,
                                        'virtual_height': -1746854433,
                                    },
                            {
                                        'source_monitor': 4699333,
                                        'source_nw_x_pixel': -4240845443451878672,
                                        'source_nw_y_pixel': -6782455374114072614,
                                        'source_pixel_width': -7014880917396206415,
                                        'source_pixel_height': -8481251527284916777,
                                        'rotation': -6464468077313059561,
                                        'virtual_nw_x_pixel': 111183855,
                                        'virtual_nw_y_pixel': -1751467087,
                                        'virtual_width': -1230417339,
                                        'virtual_height': 673026755,
                                    },
                            {
                                        'source_monitor': 6080675,
                                        'source_nw_x_pixel': -7550596035185225595,
                                        'source_nw_y_pixel': -1503304088283567945,
                                        'source_pixel_width': -5129770100769796636,
                                        'source_pixel_height': -8844811702514366797,
                                        'rotation': -6701399643507386740,
                                        'virtual_nw_x_pixel': -1403199905,
                                        'virtual_nw_y_pixel': 807225165,
                                        'virtual_width': -1965458320,
                                        'virtual_height': -544453017,
                                    },
                            {
                                        'source_monitor': 2437452,
                                        'source_nw_x_pixel': -7527668544156551977,
                                        'source_nw_y_pixel': -1558292093554375495,
                                        'source_pixel_width': -2134557339951039131,
                                        'source_pixel_height': -9131309927993787678,
                                        'rotation': -2706875206013844342,
                                        'virtual_nw_x_pixel': -1337774655,
                                        'virtual_nw_y_pixel': 175288674,
                                        'virtual_width': 900598564,
                                        'virtual_height': -1177391824,
                                    },
                            {
                                        'source_monitor': 4366987,
                                        'source_nw_x_pixel': -7589831489818779210,
                                        'source_nw_y_pixel': -541084165698219617,
                                        'source_pixel_width': -858103839782889836,
                                        'source_pixel_height': -2792844327323343778,
                                        'rotation': -5072470151334167800,
                                        'virtual_nw_x_pixel': -1236024768,
                                        'virtual_nw_y_pixel': -539854012,
                                        'virtual_width': 694205695,
                                        'virtual_height': -1260087458,
                                    },
                            {
                                        'source_monitor': 3170133,
                                        'source_nw_x_pixel': -1364174557550732472,
                                        'source_nw_y_pixel': -8153851936257123090,
                                        'source_pixel_width': -3334934728721082196,
                                        'source_pixel_height': -8485959671539108599,
                                        'rotation': -8723020381043634210,
                                        'virtual_nw_x_pixel': 1521807920,
                                        'virtual_nw_y_pixel': 1005834718,
                                        'virtual_width': 336278953,
                                        'virtual_height': 1958163211,
                                    },
                            {
                                        'source_monitor': 2564773,
                                        'source_nw_x_pixel': -7999210247227362147,
                                        'source_nw_y_pixel': -241832658323744911,
                                        'source_pixel_width': -8388629099799287023,
                                        'source_pixel_height': -6919488894526569561,
                                        'rotation': -8903011688253557015,
                                        'virtual_nw_x_pixel': 853029999,
                                        'virtual_nw_y_pixel': 46239607,
                                        'virtual_width': -739947812,
                                        'virtual_height': 1798821396,
                                    },
                            {
                                        'source_monitor': 2715163,
                                        'source_nw_x_pixel': -1736786883644318004,
                                        'source_nw_y_pixel': -5645953285473845886,
                                        'source_pixel_width': -2055001268419947142,
                                        'source_pixel_height': -201487626257650098,
                                        'rotation': -3468210851511157017,
                                        'virtual_nw_x_pixel': 1131539092,
                                        'virtual_nw_y_pixel': -155297291,
                                        'virtual_width': -1191750654,
                                        'virtual_height': 63724055,
                                    },
                            {
                                        'source_monitor': -919821,
                                        'source_nw_x_pixel': -7600027763741496550,
                                        'source_nw_y_pixel': -6809444152186896067,
                                        'source_pixel_width': -7714247107040847746,
                                        'source_pixel_height': -2719421889903165630,
                                        'rotation': -8404875419070149039,
                                        'virtual_nw_x_pixel': -838799095,
                                        'virtual_nw_y_pixel': 1267496791,
                                        'virtual_width': -1995065121,
                                        'virtual_height': -1122261036,
                                    },
                            {
                                        'source_monitor': 2546598,
                                        'source_nw_x_pixel': -3491519378462971825,
                                        'source_nw_y_pixel': -5722514811343689979,
                                        'source_pixel_width': -2912310459201440922,
                                        'source_pixel_height': -1489438642388531966,
                                        'rotation': -6120709768578230458,
                                        'virtual_nw_x_pixel': 716892336,
                                        'virtual_nw_y_pixel': -1625409054,
                                        'virtual_width': 56870012,
                                        'virtual_height': -1554059886,
                                    },
                        ],
                },
                {
                    'description': 'ӡϸӔӰτʶˋȦĢŘѱúÏŝuϻȏӮ\u038běӊѰǿϺɋӦǦдƅм',
                    'monitors': [
                            {
                                        'identifier': -198181,
                                        'width': 2732027959192427142,
                                        'height': 5461969340492652026,
                                    },
                            {
                                        'identifier': -428257,
                                        'width': 2264525817851310695,
                                        'height': -5026327485548798646,
                                    },
                            {
                                        'identifier': 5580477,
                                        'width': -2849650358386155416,
                                        'height': -5561053302636655383,
                                    },
                            {
                                        'identifier': 3939440,
                                        'width': 1343783150453008772,
                                        'height': 3760699598654080831,
                                    },
                            {
                                        'identifier': 539365,
                                        'width': -1908229501491867282,
                                        'height': 3245894868708154338,
                                    },
                            {
                                        'identifier': 2070953,
                                        'width': 8840642203818511257,
                                        'height': 31343114525525814,
                                    },
                            {
                                        'identifier': 266943,
                                        'width': -298034289826883313,
                                        'height': 6799857948646501770,
                                    },
                            {
                                        'identifier': 652433,
                                        'width': -4949978103661236383,
                                        'height': 6315961325129365001,
                                    },
                            {
                                        'identifier': -32348,
                                        'width': 6938969121190743039,
                                        'height': 6263061946373645963,
                                    },
                            {
                                        'identifier': -481704,
                                        'width': 5680890249756532139,
                                        'height': 918535184009545536,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7218282,
                                        'source_nw_x_pixel': -1647645029743968354,
                                        'source_nw_y_pixel': -4405927034443849286,
                                        'source_pixel_width': -6342507630079171556,
                                        'source_pixel_height': -6890123257747511874,
                                        'rotation': -2386993731376380425,
                                        'virtual_nw_x_pixel': 1259457529,
                                        'virtual_nw_y_pixel': 480652009,
                                        'virtual_width': 1060284769,
                                        'virtual_height': 1809044430,
                                    },
                            {
                                        'source_monitor': 713654,
                                        'source_nw_x_pixel': -6715048095074420672,
                                        'source_nw_y_pixel': -5559912101499394945,
                                        'source_pixel_width': -7398342678406135538,
                                        'source_pixel_height': -458207373603403657,
                                        'rotation': -8920738563499776549,
                                        'virtual_nw_x_pixel': -282879537,
                                        'virtual_nw_y_pixel': 971853574,
                                        'virtual_width': 829788520,
                                        'virtual_height': -1260878383,
                                    },
                            {
                                        'source_monitor': 1513158,
                                        'source_nw_x_pixel': -2690144624619289932,
                                        'source_nw_y_pixel': -668171498424259592,
                                        'source_pixel_width': -1532874497906888290,
                                        'source_pixel_height': -2815132811535013244,
                                        'rotation': -7547161357859654236,
                                        'virtual_nw_x_pixel': 1584964597,
                                        'virtual_nw_y_pixel': 1580714303,
                                        'virtual_width': 467094279,
                                        'virtual_height': -1087918259,
                                    },
                            {
                                        'source_monitor': 6027714,
                                        'source_nw_x_pixel': -2588766242013028062,
                                        'source_nw_y_pixel': -3154944541594001817,
                                        'source_pixel_width': -8237203629695883407,
                                        'source_pixel_height': -4104679451215943091,
                                        'rotation': -4370184316402758894,
                                        'virtual_nw_x_pixel': -51990730,
                                        'virtual_nw_y_pixel': -690803659,
                                        'virtual_width': -1631602158,
                                        'virtual_height': 416426195,
                                    },
                            {
                                        'source_monitor': 813347,
                                        'source_nw_x_pixel': -8374102630147330248,
                                        'source_nw_y_pixel': -3313570671109909532,
                                        'source_pixel_width': -3552947541838559541,
                                        'source_pixel_height': -5540703777066271986,
                                        'rotation': -2199219093070873472,
                                        'virtual_nw_x_pixel': -1285792402,
                                        'virtual_nw_y_pixel': -810981803,
                                        'virtual_width': -62852775,
                                        'virtual_height': 1406853854,
                                    },
                            {
                                        'source_monitor': 9938024,
                                        'source_nw_x_pixel': -2405275850087759452,
                                        'source_nw_y_pixel': -5617422803214517007,
                                        'source_pixel_width': -8142809168338360051,
                                        'source_pixel_height': -7083769878913112766,
                                        'rotation': -4270166739701150727,
                                        'virtual_nw_x_pixel': 1055255967,
                                        'virtual_nw_y_pixel': 952498353,
                                        'virtual_width': 10599418,
                                        'virtual_height': 667374308,
                                    },
                            {
                                        'source_monitor': 4983542,
                                        'source_nw_x_pixel': -6528770691309718262,
                                        'source_nw_y_pixel': -7367916373331647324,
                                        'source_pixel_width': -8466690673290699251,
                                        'source_pixel_height': -8688449318563199615,
                                        'rotation': -3951857594763939839,
                                        'virtual_nw_x_pixel': 885443364,
                                        'virtual_nw_y_pixel': 136097446,
                                        'virtual_width': -873190003,
                                        'virtual_height': -1923846403,
                                    },
                            {
                                        'source_monitor': 7712816,
                                        'source_nw_x_pixel': -525890920967444342,
                                        'source_nw_y_pixel': -6182770438565221849,
                                        'source_pixel_width': -2688432436640637525,
                                        'source_pixel_height': -3864652012581003109,
                                        'rotation': -2124379633844086272,
                                        'virtual_nw_x_pixel': 175704721,
                                        'virtual_nw_y_pixel': -480145933,
                                        'virtual_width': 1371234197,
                                        'virtual_height': 1954213292,
                                    },
                            {
                                        'source_monitor': 1227063,
                                        'source_nw_x_pixel': -7813142662929562112,
                                        'source_nw_y_pixel': -6448341138295330667,
                                        'source_pixel_width': -1199712794765272626,
                                        'source_pixel_height': -5790763860626743294,
                                        'rotation': -3648140246865586986,
                                        'virtual_nw_x_pixel': 1904675279,
                                        'virtual_nw_y_pixel': -1816454810,
                                        'virtual_width': 1891263084,
                                        'virtual_height': 1961416497,
                                    },
                            {
                                        'source_monitor': 4926962,
                                        'source_nw_x_pixel': -3108848358425430541,
                                        'source_nw_y_pixel': -2680006087292718460,
                                        'source_pixel_width': -1002263095735306447,
                                        'source_pixel_height': -3642487363121533725,
                                        'rotation': -6593270180763715189,
                                        'virtual_nw_x_pixel': -418522499,
                                        'virtual_nw_y_pixel': 1509983890,
                                        'virtual_width': -1288342462,
                                        'virtual_height': 977422048,
                                    },
                        ],
                },
                {
                    'description': 'ƗӐ!Ĩłņ\x83ľˎħɥүĨϘ?љυʴЋԎϭƺȴć˗ȝǷΣŦҰ',
                    'monitors': [
                            {
                                        'identifier': 2931984,
                                        'width': 5634486179600342845,
                                        'height': 9143162168565810300,
                                    },
                            {
                                        'identifier': 5073275,
                                        'width': 7123770406572185060,
                                        'height': -5324017428604130895,
                                    },
                            {
                                        'identifier': 6989230,
                                        'width': 4496510141248076299,
                                        'height': 6377772895710361993,
                                    },
                            {
                                        'identifier': 8907523,
                                        'width': 8358271631662285185,
                                        'height': 6380281936772278486,
                                    },
                            {
                                        'identifier': 7773051,
                                        'width': -6002068523164143709,
                                        'height': 5721164207140996897,
                                    },
                            {
                                        'identifier': 7699606,
                                        'width': 62833428867505976,
                                        'height': -6653887908238474745,
                                    },
                            {
                                        'identifier': -809292,
                                        'width': 3987158918206975453,
                                        'height': -1600756662787450540,
                                    },
                            {
                                        'identifier': -736554,
                                        'width': 5453080621922022938,
                                        'height': 3459733509223033220,
                                    },
                            {
                                        'identifier': 9166205,
                                        'width': -7752240424042099020,
                                        'height': 8473101225872520376,
                                    },
                            {
                                        'identifier': 7345962,
                                        'width': -8144621771056585916,
                                        'height': -3947599208276480704,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -822868,
                                        'source_nw_x_pixel': -3088549678136266747,
                                        'source_nw_y_pixel': -6705402621047207441,
                                        'source_pixel_width': -3744010109936520903,
                                        'source_pixel_height': -8585100434989900603,
                                        'rotation': -6472056744641878567,
                                        'virtual_nw_x_pixel': 312322113,
                                        'virtual_nw_y_pixel': -654985133,
                                        'virtual_width': 485001060,
                                        'virtual_height': -980546761,
                                    },
                            {
                                        'source_monitor': 3321076,
                                        'source_nw_x_pixel': -3275877153328038852,
                                        'source_nw_y_pixel': -8408171585139437628,
                                        'source_pixel_width': -7497146619811608568,
                                        'source_pixel_height': -8305351363740916135,
                                        'rotation': -6278625012173939676,
                                        'virtual_nw_x_pixel': 1539081355,
                                        'virtual_nw_y_pixel': 1110879434,
                                        'virtual_width': 1244749071,
                                        'virtual_height': 1544112752,
                                    },
                            {
                                        'source_monitor': 5851231,
                                        'source_nw_x_pixel': -8543081320663526373,
                                        'source_nw_y_pixel': -3241182776543339555,
                                        'source_pixel_width': -7979730853677558984,
                                        'source_pixel_height': -1864901122033304506,
                                        'rotation': -1076024264954379653,
                                        'virtual_nw_x_pixel': -1348511649,
                                        'virtual_nw_y_pixel': -836004110,
                                        'virtual_width': -1917126977,
                                        'virtual_height': 1412315457,
                                    },
                            {
                                        'source_monitor': 3665670,
                                        'source_nw_x_pixel': -3982074484869534084,
                                        'source_nw_y_pixel': -6869011539715130188,
                                        'source_pixel_width': -5769398529323892240,
                                        'source_pixel_height': -9023799253616574982,
                                        'rotation': -6599781780631943842,
                                        'virtual_nw_x_pixel': 1543177923,
                                        'virtual_nw_y_pixel': -642414674,
                                        'virtual_width': -1682842018,
                                        'virtual_height': 1896310215,
                                    },
                            {
                                        'source_monitor': 8643457,
                                        'source_nw_x_pixel': -4285366712563396015,
                                        'source_nw_y_pixel': -6988678217248878473,
                                        'source_pixel_width': -6639843552666779393,
                                        'source_pixel_height': -3213872637212089211,
                                        'rotation': -2751976684185305481,
                                        'virtual_nw_x_pixel': 1225584854,
                                        'virtual_nw_y_pixel': 1448587719,
                                        'virtual_width': -401225678,
                                        'virtual_height': -492722525,
                                    },
                            {
                                        'source_monitor': 4712936,
                                        'source_nw_x_pixel': -1408952278003687275,
                                        'source_nw_y_pixel': -2136430505790027048,
                                        'source_pixel_width': -288614154480735666,
                                        'source_pixel_height': -6460768989780366498,
                                        'rotation': -6248325203679177185,
                                        'virtual_nw_x_pixel': 222855504,
                                        'virtual_nw_y_pixel': 123122615,
                                        'virtual_width': -973551028,
                                        'virtual_height': 1288322616,
                                    },
                            {
                                        'source_monitor': 5281941,
                                        'source_nw_x_pixel': -1242901101971016572,
                                        'source_nw_y_pixel': -96970804544336289,
                                        'source_pixel_width': -346462367817703202,
                                        'source_pixel_height': -6819115921394057152,
                                        'rotation': -1504401516153013207,
                                        'virtual_nw_x_pixel': 390658450,
                                        'virtual_nw_y_pixel': 615382625,
                                        'virtual_width': 1973345057,
                                        'virtual_height': 1310188445,
                                    },
                            {
                                        'source_monitor': 2038104,
                                        'source_nw_x_pixel': -7336023739754367927,
                                        'source_nw_y_pixel': -916524288426029792,
                                        'source_pixel_width': -4514175363419021240,
                                        'source_pixel_height': -8384683658888135009,
                                        'rotation': -6896813377475978610,
                                        'virtual_nw_x_pixel': -1185481740,
                                        'virtual_nw_y_pixel': 1826494144,
                                        'virtual_width': 327268389,
                                        'virtual_height': 937339565,
                                    },
                            {
                                        'source_monitor': 9551011,
                                        'source_nw_x_pixel': -5155497105535211332,
                                        'source_nw_y_pixel': -7522016447793516777,
                                        'source_pixel_width': -960718219170088611,
                                        'source_pixel_height': -2061152601224765786,
                                        'rotation': -7246979747893477318,
                                        'virtual_nw_x_pixel': 429593003,
                                        'virtual_nw_y_pixel': -680071200,
                                        'virtual_width': -420132222,
                                        'virtual_height': -40187214,
                                    },
                            {
                                        'source_monitor': -625892,
                                        'source_nw_x_pixel': -6272069535355193040,
                                        'source_nw_y_pixel': -68628259701794594,
                                        'source_pixel_width': -186594120883612471,
                                        'source_pixel_height': -8808093062937876426,
                                        'rotation': -4248166164968422985,
                                        'virtual_nw_x_pixel': 1651531167,
                                        'virtual_nw_y_pixel': 131859675,
                                        'virtual_width': 1263870783,
                                        'virtual_height': -561687463,
                                    },
                        ],
                },
                {
                    'description': 'ӃӋԁï\x7fǖʆ±ˡWҸӻǁƗÃˮʤϕ\x95ÅσŔîǇҥɤ˂ƲҨЋ',
                    'monitors': [
                            {
                                        'identifier': 7286423,
                                        'width': 8190194435328302105,
                                        'height': -1978210762759612941,
                                    },
                            {
                                        'identifier': 4413589,
                                        'width': 4971150195779435948,
                                        'height': -7856693420391868860,
                                    },
                            {
                                        'identifier': 3737439,
                                        'width': -1287321740106976224,
                                        'height': -238991213222857613,
                                    },
                            {
                                        'identifier': -555017,
                                        'width': 5621403187051475013,
                                        'height': 5488998809988122542,
                                    },
                            {
                                        'identifier': 9726458,
                                        'width': 2728308409472614654,
                                        'height': 5264198971583158336,
                                    },
                            {
                                        'identifier': 3848892,
                                        'width': -165045979547800421,
                                        'height': -1278850191267575157,
                                    },
                            {
                                        'identifier': 1598393,
                                        'width': -2773810104297497139,
                                        'height': 6678766980422371934,
                                    },
                            {
                                        'identifier': 6446997,
                                        'width': 4183334292450191344,
                                        'height': -4447659570145043643,
                                    },
                            {
                                        'identifier': 5305224,
                                        'width': 2010131428542417171,
                                        'height': 1304845154324311105,
                                    },
                            {
                                        'identifier': 1998434,
                                        'width': -2206054594154623677,
                                        'height': -8257308270726161223,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6112529,
                                        'source_nw_x_pixel': -1994685916805624981,
                                        'source_nw_y_pixel': -5861740773022166613,
                                        'source_pixel_width': -4650318259088232926,
                                        'source_pixel_height': -1950438323665154101,
                                        'rotation': -7658379165089954028,
                                        'virtual_nw_x_pixel': -1412053248,
                                        'virtual_nw_y_pixel': 891625130,
                                        'virtual_width': -1645007766,
                                        'virtual_height': 1017376117,
                                    },
                            {
                                        'source_monitor': 9813529,
                                        'source_nw_x_pixel': -8227598438683013307,
                                        'source_nw_y_pixel': -5575360365757626255,
                                        'source_pixel_width': -7677201633192621802,
                                        'source_pixel_height': -6116180475888789774,
                                        'rotation': -3588307353690013665,
                                        'virtual_nw_x_pixel': -413358376,
                                        'virtual_nw_y_pixel': 889072876,
                                        'virtual_width': -875330833,
                                        'virtual_height': -1724815344,
                                    },
                            {
                                        'source_monitor': 7571869,
                                        'source_nw_x_pixel': -5089069225683005861,
                                        'source_nw_y_pixel': -7866186048025713103,
                                        'source_pixel_width': -5732949530731510964,
                                        'source_pixel_height': -5388023538641626897,
                                        'rotation': -5595547732811272739,
                                        'virtual_nw_x_pixel': -1727401226,
                                        'virtual_nw_y_pixel': 1734547215,
                                        'virtual_width': 192708592,
                                        'virtual_height': 1261512771,
                                    },
                            {
                                        'source_monitor': 7003979,
                                        'source_nw_x_pixel': -712723354197684689,
                                        'source_nw_y_pixel': -610038658657360900,
                                        'source_pixel_width': -23141979976687504,
                                        'source_pixel_height': -4437885239862135756,
                                        'rotation': -174278737380866870,
                                        'virtual_nw_x_pixel': 1032264896,
                                        'virtual_nw_y_pixel': 830835589,
                                        'virtual_width': 1838911220,
                                        'virtual_height': 1973035879,
                                    },
                            {
                                        'source_monitor': -960357,
                                        'source_nw_x_pixel': -60200440486536284,
                                        'source_nw_y_pixel': -4413770204062276823,
                                        'source_pixel_width': -3517071766412997736,
                                        'source_pixel_height': -5684187854211522999,
                                        'rotation': -6285848091134218867,
                                        'virtual_nw_x_pixel': 810498568,
                                        'virtual_nw_y_pixel': -1708322366,
                                        'virtual_width': -3632060,
                                        'virtual_height': 87873006,
                                    },
                            {
                                        'source_monitor': 7986844,
                                        'source_nw_x_pixel': -6411104174379663622,
                                        'source_nw_y_pixel': -3376104115302080074,
                                        'source_pixel_width': -3217296335092148915,
                                        'source_pixel_height': -4154543964145327685,
                                        'rotation': -4014191585852527827,
                                        'virtual_nw_x_pixel': 875276772,
                                        'virtual_nw_y_pixel': -1540160618,
                                        'virtual_width': 1872743614,
                                        'virtual_height': 591873815,
                                    },
                            {
                                        'source_monitor': 1004009,
                                        'source_nw_x_pixel': -5031443748129468518,
                                        'source_nw_y_pixel': -5818524324895772064,
                                        'source_pixel_width': -473621849921759748,
                                        'source_pixel_height': -340749484193706647,
                                        'rotation': -1860851834697214451,
                                        'virtual_nw_x_pixel': -1214003114,
                                        'virtual_nw_y_pixel': -464959540,
                                        'virtual_width': -1207663919,
                                        'virtual_height': -944306421,
                                    },
                            {
                                        'source_monitor': 6737485,
                                        'source_nw_x_pixel': -4175551224630411617,
                                        'source_nw_y_pixel': -3193238580604309061,
                                        'source_pixel_width': -7076163247905668924,
                                        'source_pixel_height': -1166781817384703785,
                                        'rotation': -7300850449336417507,
                                        'virtual_nw_x_pixel': 534930282,
                                        'virtual_nw_y_pixel': 1511960006,
                                        'virtual_width': 537514245,
                                        'virtual_height': -790184453,
                                    },
                            {
                                        'source_monitor': 7676063,
                                        'source_nw_x_pixel': -973526699814919553,
                                        'source_nw_y_pixel': -1384936483707420494,
                                        'source_pixel_width': -2425727104046625610,
                                        'source_pixel_height': -3217509025592175602,
                                        'rotation': -3668263759851891608,
                                        'virtual_nw_x_pixel': -1912670661,
                                        'virtual_nw_y_pixel': 515624743,
                                        'virtual_width': 1327080345,
                                        'virtual_height': 831037920,
                                    },
                            {
                                        'source_monitor': 4241842,
                                        'source_nw_x_pixel': -1586213845334887281,
                                        'source_nw_y_pixel': -4763892435748056557,
                                        'source_pixel_width': -477746324409163508,
                                        'source_pixel_height': -165173081604902268,
                                        'rotation': -7996687627717280824,
                                        'virtual_nw_x_pixel': 1007317517,
                                        'virtual_nw_y_pixel': -143040949,
                                        'virtual_width': 218508075,
                                        'virtual_height': 568048974,
                                    },
                        ],
                },
                {
                    'description': 'ɝĝȈ҉PiȊϾƙɷȦĢͰŞӣƕŀeŎʻˎΤ«úȌρӥТǒƗ',
                    'monitors': [
                            {
                                        'identifier': 4902434,
                                        'width': -8022869950885355706,
                                        'height': 8955235898209947334,
                                    },
                            {
                                        'identifier': 9632367,
                                        'width': 3967752445866904854,
                                        'height': -6559939230892021364,
                                    },
                            {
                                        'identifier': -537387,
                                        'width': 2672949553061439473,
                                        'height': -4561531777362264586,
                                    },
                            {
                                        'identifier': 3044374,
                                        'width': 7337301975129686587,
                                        'height': -6678544918021975727,
                                    },
                            {
                                        'identifier': 3207517,
                                        'width': 5733351719908222095,
                                        'height': -2167434516893026438,
                                    },
                            {
                                        'identifier': 8057824,
                                        'width': 1408425796775048817,
                                        'height': 7404498181792692345,
                                    },
                            {
                                        'identifier': 2366241,
                                        'width': -1380979172432093227,
                                        'height': -3721147538610549273,
                                    },
                            {
                                        'identifier': 1472324,
                                        'width': 9023612844974740889,
                                        'height': -5812586471038496385,
                                    },
                            {
                                        'identifier': 8533588,
                                        'width': -4229356609522117098,
                                        'height': 7621151744996862868,
                                    },
                            {
                                        'identifier': 1184702,
                                        'width': 8499477610194052251,
                                        'height': 9055679004461676555,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2465358,
                                        'source_nw_x_pixel': -8762221913549755740,
                                        'source_nw_y_pixel': -4933517810327759228,
                                        'source_pixel_width': -1903383828946886801,
                                        'source_pixel_height': -5867666980123199210,
                                        'rotation': -5033789716795108012,
                                        'virtual_nw_x_pixel': -698848140,
                                        'virtual_nw_y_pixel': -638066011,
                                        'virtual_width': 1204011475,
                                        'virtual_height': 629883673,
                                    },
                            {
                                        'source_monitor': 4725514,
                                        'source_nw_x_pixel': -7973376238872526868,
                                        'source_nw_y_pixel': -4432000779981779470,
                                        'source_pixel_width': -5011100562024505616,
                                        'source_pixel_height': -7503661345998685661,
                                        'rotation': -8878364196282937090,
                                        'virtual_nw_x_pixel': 244154861,
                                        'virtual_nw_y_pixel': -318571999,
                                        'virtual_width': -586051689,
                                        'virtual_height': 175587544,
                                    },
                            {
                                        'source_monitor': 6393062,
                                        'source_nw_x_pixel': -9168578161165286763,
                                        'source_nw_y_pixel': -8327982522283912098,
                                        'source_pixel_width': -5864793605213572180,
                                        'source_pixel_height': -6984860490403303445,
                                        'rotation': -5757431116672631332,
                                        'virtual_nw_x_pixel': 1960573232,
                                        'virtual_nw_y_pixel': -1212982419,
                                        'virtual_width': -434696982,
                                        'virtual_height': -199727771,
                                    },
                            {
                                        'source_monitor': 819627,
                                        'source_nw_x_pixel': -2948893249089990086,
                                        'source_nw_y_pixel': -8384276068133205419,
                                        'source_pixel_width': -5940819850309201665,
                                        'source_pixel_height': -5821166073602148154,
                                        'rotation': -6370543840635326873,
                                        'virtual_nw_x_pixel': 1385137243,
                                        'virtual_nw_y_pixel': 850846891,
                                        'virtual_width': 988798513,
                                        'virtual_height': -1968424617,
                                    },
                            {
                                        'source_monitor': 9503841,
                                        'source_nw_x_pixel': -7108580525465978447,
                                        'source_nw_y_pixel': -2313560622237811985,
                                        'source_pixel_width': -1300414861085342471,
                                        'source_pixel_height': -801451933767627907,
                                        'rotation': -1504696113705599843,
                                        'virtual_nw_x_pixel': -1670294885,
                                        'virtual_nw_y_pixel': 22100011,
                                        'virtual_width': 1970696758,
                                        'virtual_height': 92736978,
                                    },
                            {
                                        'source_monitor': 4483077,
                                        'source_nw_x_pixel': -7588576928954418818,
                                        'source_nw_y_pixel': -1064990144783615637,
                                        'source_pixel_width': -5714303385534830449,
                                        'source_pixel_height': -1029349063399861942,
                                        'rotation': -5776897960467565405,
                                        'virtual_nw_x_pixel': 1963181434,
                                        'virtual_nw_y_pixel': 482825549,
                                        'virtual_width': 1879861669,
                                        'virtual_height': 1960490553,
                                    },
                            {
                                        'source_monitor': 1826393,
                                        'source_nw_x_pixel': -9048507723541064941,
                                        'source_nw_y_pixel': -4459957286252616270,
                                        'source_pixel_width': -4241226056673100151,
                                        'source_pixel_height': -3676495327877934574,
                                        'rotation': -7933478226039002186,
                                        'virtual_nw_x_pixel': -333728532,
                                        'virtual_nw_y_pixel': -1214357521,
                                        'virtual_width': -191733346,
                                        'virtual_height': -936779127,
                                    },
                            {
                                        'source_monitor': 8529185,
                                        'source_nw_x_pixel': -598510478773307275,
                                        'source_nw_y_pixel': -823583882609742704,
                                        'source_pixel_width': -8187770312677283791,
                                        'source_pixel_height': -8747070581812298024,
                                        'rotation': -7279212071141551308,
                                        'virtual_nw_x_pixel': 299933002,
                                        'virtual_nw_y_pixel': 1878405771,
                                        'virtual_width': 88733369,
                                        'virtual_height': -1977703875,
                                    },
                            {
                                        'source_monitor': 7307211,
                                        'source_nw_x_pixel': -8398069534975627135,
                                        'source_nw_y_pixel': -5558625680643173216,
                                        'source_pixel_width': -5991646891924202414,
                                        'source_pixel_height': -5645287938434270784,
                                        'rotation': -3021386570980367296,
                                        'virtual_nw_x_pixel': -1105043719,
                                        'virtual_nw_y_pixel': -1684517840,
                                        'virtual_width': -147315173,
                                        'virtual_height': -1930595139,
                                    },
                            {
                                        'source_monitor': 648753,
                                        'source_nw_x_pixel': -3766286967571004764,
                                        'source_nw_y_pixel': -3007548661506756425,
                                        'source_pixel_width': -5665019811886588231,
                                        'source_pixel_height': -9160852224885571652,
                                        'rotation': -4296990950284191108,
                                        'virtual_nw_x_pixel': -1122318563,
                                        'virtual_nw_y_pixel': 1328987599,
                                        'virtual_width': 644747178,
                                        'virtual_height': 894374973,
                                    },
                        ],
                },
                {
                    'description': 'B\x8cЃͽɃ[ïjԘȫîҢŌ˞ȸɱɃө\x85ǓПСɐƫƋĕ\x95;ŉ2',
                    'monitors': [
                            {
                                        'identifier': 1888583,
                                        'width': -3288837320405878707,
                                        'height': -424393536285400449,
                                    },
                            {
                                        'identifier': -958153,
                                        'width': -6385867077663628172,
                                        'height': -8270930077334732830,
                                    },
                            {
                                        'identifier': 9422749,
                                        'width': 1693095246407457435,
                                        'height': -7697909660739717880,
                                    },
                            {
                                        'identifier': 1613665,
                                        'width': 2350999245096826349,
                                        'height': 8333118248337191396,
                                    },
                            {
                                        'identifier': 3004341,
                                        'width': 1195840213909058572,
                                        'height': -3881076785626945481,
                                    },
                            {
                                        'identifier': 6122261,
                                        'width': -4978483371614949358,
                                        'height': -7126364690495893171,
                                    },
                            {
                                        'identifier': 7573368,
                                        'width': 6311296718476575965,
                                        'height': 1443257636897808530,
                                    },
                            {
                                        'identifier': 6798728,
                                        'width': 6479192039521889626,
                                        'height': 6530664622068135015,
                                    },
                            {
                                        'identifier': 3625827,
                                        'width': -3763865017114370048,
                                        'height': -8086254774170308681,
                                    },
                            {
                                        'identifier': 1687091,
                                        'width': 1340255244147349896,
                                        'height': 7761054375583237971,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 14901,
                                        'source_nw_x_pixel': -2019229135162086962,
                                        'source_nw_y_pixel': -7989443734218177323,
                                        'source_pixel_width': -5312635513309200885,
                                        'source_pixel_height': -1689347780235099403,
                                        'rotation': -3641629073770923036,
                                        'virtual_nw_x_pixel': -1640464140,
                                        'virtual_nw_y_pixel': 1922375062,
                                        'virtual_width': 642120307,
                                        'virtual_height': 683689562,
                                    },
                            {
                                        'source_monitor': 7370763,
                                        'source_nw_x_pixel': -4129968677383462990,
                                        'source_nw_y_pixel': -7465158443247925794,
                                        'source_pixel_width': -2705418345691926923,
                                        'source_pixel_height': -4250992424551402298,
                                        'rotation': -8346681361772771004,
                                        'virtual_nw_x_pixel': -1285617985,
                                        'virtual_nw_y_pixel': 419379890,
                                        'virtual_width': 975154529,
                                        'virtual_height': -1680806426,
                                    },
                            {
                                        'source_monitor': 2542649,
                                        'source_nw_x_pixel': -6207868151828909204,
                                        'source_nw_y_pixel': -7831328968296697821,
                                        'source_pixel_width': -2520293260834900529,
                                        'source_pixel_height': -6584422588410037049,
                                        'rotation': -9137689898273349675,
                                        'virtual_nw_x_pixel': 1062969828,
                                        'virtual_nw_y_pixel': 816829296,
                                        'virtual_width': -320715015,
                                        'virtual_height': -1603482058,
                                    },
                            {
                                        'source_monitor': 5979845,
                                        'source_nw_x_pixel': -7543096348357583374,
                                        'source_nw_y_pixel': -8096048356503483837,
                                        'source_pixel_width': -3885501336081591706,
                                        'source_pixel_height': -2072080088400122203,
                                        'rotation': -1228269290443737884,
                                        'virtual_nw_x_pixel': -1127290980,
                                        'virtual_nw_y_pixel': 1450366851,
                                        'virtual_width': 1388913619,
                                        'virtual_height': 53120634,
                                    },
                            {
                                        'source_monitor': 3998002,
                                        'source_nw_x_pixel': -8080531533656850930,
                                        'source_nw_y_pixel': -4202264400877974201,
                                        'source_pixel_width': -1342328844229309059,
                                        'source_pixel_height': -2578724040390015222,
                                        'rotation': -3632725518872603251,
                                        'virtual_nw_x_pixel': -1829268221,
                                        'virtual_nw_y_pixel': -109686586,
                                        'virtual_width': -1797119537,
                                        'virtual_height': -1135988499,
                                    },
                            {
                                        'source_monitor': 112721,
                                        'source_nw_x_pixel': -4742815655537822533,
                                        'source_nw_y_pixel': -2700703401128046420,
                                        'source_pixel_width': -527688457241053267,
                                        'source_pixel_height': -7554361348373654972,
                                        'rotation': -4642611358186096216,
                                        'virtual_nw_x_pixel': 1096487475,
                                        'virtual_nw_y_pixel': -752843498,
                                        'virtual_width': -134715957,
                                        'virtual_height': -1468084007,
                                    },
                            {
                                        'source_monitor': -516815,
                                        'source_nw_x_pixel': -6461973219560314663,
                                        'source_nw_y_pixel': -1907275312792529757,
                                        'source_pixel_width': -4618471356088657172,
                                        'source_pixel_height': -7305734379707343651,
                                        'rotation': -3524945341100245653,
                                        'virtual_nw_x_pixel': -1328881203,
                                        'virtual_nw_y_pixel': -896935982,
                                        'virtual_width': 409050152,
                                        'virtual_height': 220535581,
                                    },
                            {
                                        'source_monitor': -40163,
                                        'source_nw_x_pixel': -4838890818967069620,
                                        'source_nw_y_pixel': -6585104515034718754,
                                        'source_pixel_width': -2586769543779297442,
                                        'source_pixel_height': -8174976092825464000,
                                        'rotation': -4596633306609159791,
                                        'virtual_nw_x_pixel': -1287513825,
                                        'virtual_nw_y_pixel': 1606613177,
                                        'virtual_width': 996772017,
                                        'virtual_height': -538998434,
                                    },
                            {
                                        'source_monitor': 5724677,
                                        'source_nw_x_pixel': -2796705915185596614,
                                        'source_nw_y_pixel': -2351221133916349323,
                                        'source_pixel_width': -4799168558001153806,
                                        'source_pixel_height': -1395659455826123339,
                                        'rotation': -3345251151443445228,
                                        'virtual_nw_x_pixel': -54675781,
                                        'virtual_nw_y_pixel': -1769665438,
                                        'virtual_width': 1535649540,
                                        'virtual_height': -1888701539,
                                    },
                            {
                                        'source_monitor': 8680322,
                                        'source_nw_x_pixel': -691460882551506459,
                                        'source_nw_y_pixel': -5985566677237717642,
                                        'source_pixel_width': -2434002141351479065,
                                        'source_pixel_height': -2860064142356760158,
                                        'rotation': -6639061026674906082,
                                        'virtual_nw_x_pixel': 583036018,
                                        'virtual_nw_y_pixel': 1489382878,
                                        'virtual_width': 1869013471,
                                        'virtual_height': -1336261484,
                                    },
                        ],
                },
                {
                    'description': 'ő',
                    'monitors': [
                            {
                                        'identifier': 4254610,
                                        'width': 6660373591952346815,
                                        'height': -6038518942154783506,
                                    },
                            {
                                        'identifier': 4533590,
                                        'width': -2757881743179039493,
                                        'height': 7905939764748647556,
                                    },
                            {
                                        'identifier': 7563342,
                                        'width': -1167059678550694897,
                                        'height': 4029398445902358647,
                                    },
                            {
                                        'identifier': 7312853,
                                        'width': 5259947335106427901,
                                        'height': 3854413882908120529,
                                    },
                            {
                                        'identifier': 7942580,
                                        'width': -1996490268685730502,
                                        'height': 518884642097695723,
                                    },
                            {
                                        'identifier': 8740007,
                                        'width': -1464890377920817697,
                                        'height': 3611378128752737787,
                                    },
                            {
                                        'identifier': 6032811,
                                        'width': -5210167015391881906,
                                        'height': 3480670345370685936,
                                    },
                            {
                                        'identifier': -166955,
                                        'width': 1848719072954889092,
                                        'height': -2617671616898280934,
                                    },
                            {
                                        'identifier': 4976999,
                                        'width': 4009668809366153509,
                                        'height': 8362618820236433762,
                                    },
                            {
                                        'identifier': -717864,
                                        'width': 2773593601829579043,
                                        'height': -6665161889304512089,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6534130,
                                        'source_nw_x_pixel': -8781220252129926184,
                                        'source_nw_y_pixel': -7163199369820887198,
                                        'source_pixel_width': -3529656098634912480,
                                        'source_pixel_height': -8168262182075538723,
                                        'rotation': -7799628087115135651,
                                        'virtual_nw_x_pixel': -1712180036,
                                        'virtual_nw_y_pixel': 1643714004,
                                        'virtual_width': 393974914,
                                        'virtual_height': -779405732,
                                    },
                            {
                                        'source_monitor': 3702745,
                                        'source_nw_x_pixel': -7569387418623232450,
                                        'source_nw_y_pixel': -9017008790474401054,
                                        'source_pixel_width': -6376129654797746334,
                                        'source_pixel_height': -5184257696475414569,
                                        'rotation': -2194559973514576978,
                                        'virtual_nw_x_pixel': -359488947,
                                        'virtual_nw_y_pixel': -1020861797,
                                        'virtual_width': 1310749431,
                                        'virtual_height': 1612627991,
                                    },
                            {
                                        'source_monitor': 1807899,
                                        'source_nw_x_pixel': -291455939148466135,
                                        'source_nw_y_pixel': -6005508526416817964,
                                        'source_pixel_width': -8038155517540654379,
                                        'source_pixel_height': -3643612996284799560,
                                        'rotation': -4330001284761707415,
                                        'virtual_nw_x_pixel': 32913512,
                                        'virtual_nw_y_pixel': -257121469,
                                        'virtual_width': -1477030378,
                                        'virtual_height': -97458897,
                                    },
                            {
                                        'source_monitor': 8549778,
                                        'source_nw_x_pixel': -4307068609848783400,
                                        'source_nw_y_pixel': -1326045915086227468,
                                        'source_pixel_width': -2600459212474119094,
                                        'source_pixel_height': -9018758855887857149,
                                        'rotation': -4473194999417435818,
                                        'virtual_nw_x_pixel': -1374898065,
                                        'virtual_nw_y_pixel': 1637321804,
                                        'virtual_width': 365563214,
                                        'virtual_height': 437087545,
                                    },
                            {
                                        'source_monitor': 1047476,
                                        'source_nw_x_pixel': -8730306290648317326,
                                        'source_nw_y_pixel': -5027265435743119104,
                                        'source_pixel_width': -7270202374006261008,
                                        'source_pixel_height': -5914287754068688085,
                                        'rotation': -5636358772005189422,
                                        'virtual_nw_x_pixel': -651115776,
                                        'virtual_nw_y_pixel': -1278681295,
                                        'virtual_width': -90308698,
                                        'virtual_height': -683935600,
                                    },
                            {
                                        'source_monitor': 5640866,
                                        'source_nw_x_pixel': -6931861748866751168,
                                        'source_nw_y_pixel': -3446325485485268919,
                                        'source_pixel_width': -5540008065085459361,
                                        'source_pixel_height': -5197214721749820365,
                                        'rotation': -3464243644703652075,
                                        'virtual_nw_x_pixel': -1960292919,
                                        'virtual_nw_y_pixel': -1642905719,
                                        'virtual_width': 1076475591,
                                        'virtual_height': -1874027706,
                                    },
                            {
                                        'source_monitor': 8407547,
                                        'source_nw_x_pixel': -4835831873433242853,
                                        'source_nw_y_pixel': -6091834282827732725,
                                        'source_pixel_width': -6639898091295656532,
                                        'source_pixel_height': -7655132583621779785,
                                        'rotation': -6616860904835523705,
                                        'virtual_nw_x_pixel': 1153163439,
                                        'virtual_nw_y_pixel': -656887263,
                                        'virtual_width': 447357786,
                                        'virtual_height': -1411799184,
                                    },
                            {
                                        'source_monitor': 8631798,
                                        'source_nw_x_pixel': -4664665722830499257,
                                        'source_nw_y_pixel': -6712874141739636962,
                                        'source_pixel_width': -4895378678903811210,
                                        'source_pixel_height': -5016140450534662278,
                                        'rotation': -1002650123960214859,
                                        'virtual_nw_x_pixel': 137960211,
                                        'virtual_nw_y_pixel': 1646969157,
                                        'virtual_width': -866558906,
                                        'virtual_height': -374141089,
                                    },
                            {
                                        'source_monitor': -322724,
                                        'source_nw_x_pixel': -3953287068119308721,
                                        'source_nw_y_pixel': -4357110112634198744,
                                        'source_pixel_width': -7076645387045883404,
                                        'source_pixel_height': -4178319877136756131,
                                        'rotation': -3166073619339770633,
                                        'virtual_nw_x_pixel': 82228778,
                                        'virtual_nw_y_pixel': -1160748041,
                                        'virtual_width': -168913988,
                                        'virtual_height': -640753176,
                                    },
                            {
                                        'source_monitor': 7190633,
                                        'source_nw_x_pixel': -4716414035821796894,
                                        'source_nw_y_pixel': -5388096316032845111,
                                        'source_pixel_width': -8068083419322818833,
                                        'source_pixel_height': -7340593354492224564,
                                        'rotation': -1999900654052149045,
                                        'virtual_nw_x_pixel': -1961932548,
                                        'virtual_nw_y_pixel': -1733213210,
                                        'virtual_width': -1018887984,
                                        'virtual_height': -1783629462,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 8964400,

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
            'request_id': 1260347,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 4258640,

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
            '$': 'ϐԍϴөɢɾ\x89ҞВ)ƘūʕûξƮ\x8aƁˋԨĩӟԇωʇƆҎ\xadӡά',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 2085393328498679629,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 647242.9241621934,
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
            '$': '20210909:201336.944354:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӁƺÆŽʯԌŹƆНţǈ˹ƗҨѢӢÊɳɝϾɖЈi˘ũĵŤϵϯǰ',
                "яԣˑԍЂŅԝãӧˍѪϪҥÂԒбō÷цȶњХϱ'Ȥ\u0380ѳʱǜɶ",
                'Ā҂ԑNđЊɈëÚӿɓҶĜ˱tфϑ˯ɪǒǞǴ¥ʪ˘ƃϡŜ˳Ϯ',
                'ӗľńŋӳȉŤ°ɻɗѺǿӹВųЎєʻŦ˾ȂĝĦϮƖѱĚɀˉƸ',
                'ƸͼИΌѓԂuѰϿўΓɅ¹ѱӢЫѓы\x90ȫKʾȥǲ˜śĿϳȭȇ',
                'тсY˩ϐʅΊ§¾ħ¼ԐçQȳŦʦЖƲыӕɷɴɷͰͲ\x82˧˚Ȳ',
                'ƽЬɑĶëΧ\u0378ʨдͱɜȝƌΔτȢɚá!ѫȦūҨҩŭŏӋұˇʨ',
                '6\x9bƄӴ\\Ϸǲ(ʟôɑˆѾɍŤҹˍĨůӡʁҍφ˶ԀДԢŤ҄î',
                'ɟӈʐ«ȢҞҖҁŲАмԗwƨƞЌϗ\x94ƟɃӽԩ˰ƓӖͳƪÚрP',
                'Ė˫ӲΕάċ}ΩЫʦͻţ[ԫnȂİľȰѣԅ\x80˪яńȥȲɎӬ]',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                2331416043657600513,
                6681265173681164180,
                -7776448058458957288,
                -7141046435811693583,
                4310990332750392749,
                1128524284784305574,
                5917158369279276085,
                6253927088915102481,
                -867675525422549861,
                7157887764898056982,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                282186.02667064994,
                653910.5189223997,
                325586.4177802906,
                742690.9423436598,
                475243.2744053737,
                342255.7402694909,
                530862.9308148762,
                589736.9425482299,
                100867.3028544861,
                684784.1618711067,
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
                '20210909:201337.804891:+0000',
                '20210909:201337.821547:+0000',
                '20210909:201337.838381:+0000',
                '20210909:201337.854289:+0000',
                '20210909:201337.870925:+0000',
                '20210909:201337.894665:+0000',
                '20210909:201337.912086:+0000',
                '20210909:201337.927842:+0000',
                '20210909:201337.944155:+0000',
                '20210909:201337.960080:+0000',
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
            'name': 'ɢ\u0380@ϏʶҿĒåЋsƽˢФɧΥҀϸґԛ-ī',
            'value': {
                '^': 'float_list',
                '$': [
                    388009.79445654165,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǒ',

            'value': {
                '^': 'datetime',
                '$': '20210909:201336.712536:+0000',
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
            'catalog': '.σÑϐ\x9dŊ\u0382ȢċεȐϘȍřɢôɦȔƨƥ˯\x94њGñåМŞ҄\x9c',
            'message': 'ӹƿϏʹʴҎƬђǽѬɀз˱>ƿĢʕҮԦżьŗʟÆϰ"ģ1ЕΒ',
            'arguments': [
                {
                    'name': 'ƏҒɸΙӆǯʔ~\x93ûȌ˜л\x82ѸıѿρѶ\x97Ǘѫϳˌɧ¬ϊȕļȘ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:201335.274363:+0000',
                        },
                },
                {
                    'name': 'ƸɁыiſΞǵ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        812470.8841132218,
                                        337844.8039622174,
                                        539916.2739745873,
                                        789463.4715189824,
                                        869582.059820887,
                                        314916.25744325086,
                                        -17444.922019009813,
                                        483959.8906643004,
                                        264095.10806077055,
                                        22836.221975723776,
                                    ],
                        },
                },
                {
                    'name': 'ҞɄӆЁєļ>є˹ҥϏɋ˷˔˅öƙќәΓҦ^ѳÝȗ\xa0½˱ȵѧ',
                    'value': {
                            '^': 'int',
                            '$': -9017869318441895591,
                        },
                },
                {
                    'name': 'ԘɓʕÉ\x9eτȿӃÙƉΥԖʢӪ˕ТƐΨɽπÝĘ´HȘЫŘȡƙ\u038b',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ԙńʚюŋчԄįːԎҾϕʇƥËс',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3980191545587851595,
                                        -6349990074385306924,
                                        1682130910089883575,
                                        5925320660025670991,
                                        6077648332466831083,
                                        6015719873753646323,
                                        -4814058995674732170,
                                        731925018222630649,
                                        8437166268605562761,
                                        -8397122390277652210,
                                    ],
                        },
                },
                {
                    'name': '4ΎдŘǪtŲǊӄĈԗºҦԞӍʽ˸Ԍ˄˅ȌɍӸƳ"Ϙǐǩ°ʀ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ǱɐʔΝϭҀ÷ԆфǒƗӇǜȂɛȜ³ƬľЯ',
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
                                    ],
                        },
                },
                {
                    'name': 'ͺǉbċЖϘʒОįӢҺϡlщɖǘϞӿǢèԟȹ',
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
                                        False,
                                    ],
                        },
                },
                {
                    'name': '\x801ɥʷӷ¹ʁǲΌ½üU8ҴчӦɘίѻ?ȢԥÊ\x80Ήɠöƭͽč',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:201336.451045:+0000',
                        },
                },
                {
                    'name': '¶',
                    'value': {
                            '^': 'datetime',
                            '$': '20210909:201336.517764:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'υˇ',

            'message': 'w',

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
            'identifier': 'ǵǛ\xadǋћȹïőɲňƍ·ɟСŌ҆ΫԓѲƆSӔѐăɳҪKԝ6?',
            'categories': [
                'invalid-user-action',
                'network',
                'internal',
                'configuration',
                'invalid-user-action',
                'network',
                'file',
                'configuration',
                'internal',
                'access-restriction',
            ],
            'source': 'ӭÓɋĲ\x81ŨĊʠЈЩѶɜԪӭŵԠȼҶǿ«ҏ҉˫ϮʌǞƮƦȻȮ',
            'messages': [
                {
                    'catalog': 'ÙрҪиΰOɥȴКʽöӹςÂζϸϷҌҙȲϴǐǎüYǠƝԄȡȻ',
                    'message': 'ǶТτÎɒϜ7ǲяƨӡɍуѿҥˡϩӵƆǴŦż´ү{ƪӹԠǖ«',
                    'arguments': [
                            {
                                        'name': 'σ)ˎΛЦAҏ\x9a·ʼjÆúɀӸȵϢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201319.342365:+0000',
                                                    },
                                    },
                            {
                                        'name': 'λʲˏ¢Ř˨=ͽ΄ȃČ˺d\x81ȋǏ\x7fʎˀςţŽdɝļ\x90ɔ´ơӸ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ј7Ԝơ˗ηˍǼυŮЕÙϒһ{ϓūǖюӖөҠәľe³ɭ\x93ȦЎ',
                                                    },
                                    },
                            {
                                        'name': 'ĉζ÷Ԛɢøϴϡ5ϗŕÞӄԀө\x85я±ѭǷ¡Ӽʔ\x89oȓтͶʐÅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɬҺĵʪĶϘ˘(ƗЄИɈΒƟқòə:īэˉκЎÐԬюȄϷѪŧ',
                                                    },
                                    },
                            {
                                        'name': 'ϱӢȥӧΠÜ$ˠƝʼћѵ˽ļʖԋƈ¡?ԐоэӸǍ`ÏȟıɁ\x8f',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8461955518644037757,
                                                                            -8244351365461121226,
                                                                            -1164570080233589294,
                                                                            -621962334241095084,
                                                                            -5519688837589032378,
                                                                            1149509849668836412,
                                                                            -5221319712016615059,
                                                                            2961529561866254282,
                                                                            7501030487468556315,
                                                                            -8542811205130701490,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'шМĉζҔпʟųϓʱԍʙŧξȻӋųĆљ\x8aǣ\x8cʨɖϛαԅϪїǪ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201319.790495:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŤөƖР6$ȸϿϫǱНƽҦҔǰσԁK\x80zĊȑːǏ˽ԦѵЫԮƛ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201319.873525:+0000',
                                                                            '20210909:201319.895909:+0000',
                                                                            '20210909:201319.913282:+0000',
                                                                            '20210909:201319.928999:+0000',
                                                                            '20210909:201319.951052:+0000',
                                                                            '20210909:201319.967813:+0000',
                                                                            '20210909:201319.984372:+0000',
                                                                            '20210909:201320.000102:+0000',
                                                                            '20210909:201320.015865:+0000',
                                                                            '20210909:201320.031596:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ƀþ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201320.114775:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÂӯȟǷQȻnӣώĔŔǍѫѢцØдãņʑһѪΝӁϝƔӔӕƅƙ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѭʅϵԝя',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ķυϣǯķ\x9aЅv˯˴κкƉпу\u038bƬӁɛȈľσÖїŉЮӭШҐɖ',
                                                    },
                                    },
                            {
                                        'name': 'іˡҚҔ<',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            419327.92219571886,
                                                                            381000.9994025288,
                                                                            881667.3382284581,
                                                                            759105.2932444243,
                                                                            128835.87087921196,
                                                                            147063.36913882405,
                                                                            -75442.93171823336,
                                                                            781610.1348675394,
                                                                            315051.20785951056,
                                                                            588378.6714200671,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȵˉçͲʿĈԘԚRİ|òԛʭǪËɽƌĿӹų*ӮеƂή´Йìȇ',
                    'message': 'ӹϪԮЮġĕWќβȗα4ͳơR˚ΰкòԝ4¿ɖņӊĻѣēѬĽ',
                    'arguments': [
                            {
                                        'name': 'әƉЁͷʗˊҩƺ˂θ\u038dʉȭǋ˕Ǝ\x9cҡʉHěʢůƆ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 21302.560315035327,
                                                    },
                                    },
                            {
                                        'name': 'ƣʊĬʻïɧѓɪӫΩͱŘΏѨ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201320.745266:+0000',
                                                                            '20210909:201320.765663:+0000',
                                                                            '20210909:201320.782499:+0000',
                                                                            '20210909:201320.798828:+0000',
                                                                            '20210909:201320.815321:+0000',
                                                                            '20210909:201320.831925:+0000',
                                                                            '20210909:201320.848423:+0000',
                                                                            '20210909:201320.866162:+0000',
                                                                            '20210909:201320.883462:+0000',
                                                                            '20210909:201320.903162:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '@˞\x86ΗǒѻëƼQЍȶрƗȽĭХҦȔLΑϩǼʊɕѿǽ\x97ΛӢ˷',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŨǉǂɎˈҽȈȽÊĽƽпӤȱFԜĸȭԥĦƗ\x83\x9eǲŽэМХθĆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201321.058232:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĄɰːρŰßφΚΘſНFҐ˛˫ԋѦʲƈƛÏjƻƣōˁӒΨƑԨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5605599722070360768,
                                                    },
                                    },
                            {
                                        'name': 'ŀ˼\xa0þӝŰӨΧΦЩй?ǗǙˢјþ\u0379ԗȵʐıѹʘpШ˕҈ρҜ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŁǤλƦȟТʝСӞΤȕҊɐ`ɴϻӓҘ˳ƥbѻTʉϲͽǚÚpЎ',
                                                                            '˲ƚǩϐ)ɀÈ\x8dɘϐĳɽЅ˫d`ШѬʇöρ϶Ѭ\x83ʠҖӗ˸тȸ',
                                                                            'ӌşǷԪв҅ѹҍӥíÊɀɼϺèǎΗƌϥǅÎԮDµѤѓȨȞљ»',
                                                                            ']¯κ\x9fɗΖÄȀĥѪԪұƑѳϛȫýӻ{\x83\x99ѿтǊ΄ÞĈ@ͰВ',
                                                                            'ȤǔEľčȉǹҒɂ:7ƴLӀЎͷϲгԀáϗӽǿɖǜËӼƷӭƲ',
                                                                            '\u0379ŢjĹ\x81ԇƢpȚƓA˓˔˄ǬϔΒÚ²Ȟїʝǘ.Ϳєɡǰ˦Ȧ',
                                                                            'ʴԊԩÕԤҔİȗƃæɣѴƠИθҨˉϹˠ\x8c)»ĻЁɕѧђǫô0',
                                                                            'ə\x80Tх\x81ѝсɌ!Ö˃«ԒʤǱɯƩЎʰ\x98ÌĉξωǐXHȿӅj',
                                                                            '˺ǎʙǿʕƈδȬÚвbĻƇξѽXϵʻˆҐώУȺӇТ˕ǔˁŴІ',
                                                                            'Ƥ)ӢҔƆµЅ>ӿ˫ԚьħâŞӿLNѧçȹ9ћƛЏ#ʸķԎҔ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'șɝ.ЉтіԋΰȤɌŭ\xadțþzɾĨ8#˃ΨЩOъЫ\x8eцˇџĨ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɯƃ\x91ϐҔӧǺĂ˓ϧ1εϬҞѯ\x91\x9a҇҃žΫȴ\u038dωϧШԍФĩĉ',
                                                    },
                                    },
                            {
                                        'name': 'ʱƟԩɪϚя˂ĭɯ˨ȡ5ӯÄķő\x80ѬįNɼɝþ¹ćƒˑʉƟɥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 819540.6314989328,
                                                    },
                                    },
                            {
                                        'name': '÷wҷʃȁīǢљš˶ԕùϱ\x96ԣѦƽʈɁʒü\x9c˨ђ˧ˇ˼¨Ҥі',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ł*ʧ͵ЛˑƿνҘӈEȣŏƂİԂЂƱƘEȠƭΎĜĿŰϠʹȘϞ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'СҎ¼ȭİ%ñȟӬљį˚˴ŜǤѰhȟǅQӮ\u0381Ǚȓ!ŞÈÆbϝ',
                    'message': 'ǷåvÌʷŠѴù\\ѨχǝɱπNėʚοǂǾϥƥDӻɤ˼ůʯӃȮ',
                    'arguments': [
                            {
                                        'name': 'Ǒȩӽ˦\x8dҲ\x90\xa0ϊɏʭϫ³@йVҺѿӼ΅ο\x87ΣƅȔŏ5ЛǌԐ',
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
                                        'name': 'ʴԍĝđԖĲJōƀǧԈҦʾ&ΒыǷǰŰҮӳѐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ģĝŁɆӴЧȲ\u038bȪԣϴ×[ʞˉ˵ӀϐxѩӏǡΑ¼kʪϽ\x87ҭӏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2744481583103714214,
                                                    },
                                    },
                            {
                                        'name': 'žŻԑʣǠ\x85ͺ˫\x89μň+ѵΉ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1906166644662610543,
                                                                            -6467698844413287118,
                                                                            -7455069037593163305,
                                                                            2934779780368234299,
                                                                            -7720419913197464562,
                                                                            9030945115977754476,
                                                                            149728548820620652,
                                                                            -6751288970225505612,
                                                                            -4822437081842529734,
                                                                            8515703576294038055,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ŖS'ǧŀJӆãơѹѦâ?ё",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7668462672475712822,
                                                    },
                                    },
                            {
                                        'name': 'Ņ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˰vûБŊȶϨěÝ÷ҾɿЍ[ǔˎ˗ǇȊѫԓƈǷǮķƱɼӱϽʁ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            149175.67444469215,
                                                                            226157.80045391893,
                                                                            264733.7435569903,
                                                                            772046.0648471679,
                                                                            916356.7685156469,
                                                                            618916.1259039553,
                                                                            123216.95262317386,
                                                                            422616.09932896425,
                                                                            131566.4299662829,
                                                                            886013.625075255,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӲΐȖʍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '3jÜƔųҞʎˌͶӭЮǛǴƅǀå®ɅϤƿŝԋɠƚѽɺ,ſЈL',
                                                                            'ÆƉķÌΞҜǾȱЬůіΠġԚȭǧǔĆýFëɃƨҳ¥ǓϛÁɖн',
                                                                            'ŞӮƈɠςƉ϶΅śэĈˁèуϖɶ˚Ʌы˞ЈqƤ\x91ɊõłÎï҆',
                                                                            'ҙˎϺΠȋАpʧǎvʏǯѿΒǢǳɷϥǩԬSǦϴĔÍȲʞĖʘГ',
                                                                            "ӋƱѶѡμ'ɈáйЮ҃ˮȜЯӜoVʢΘȇƑȌʏųȯřøλԥȜ",
                                                                            'ҐŲɝōȹʛēȂĩπχуѰÊţʍьԈό®ǦӶųfƨŜΌŕƅΊ',
                                                                            '˭ҠȫɃǕûËʮ7ӕҔ҅ӎŶɋʽȜ>УƏɨɓҗŭ\x94ŻϳWǏơ',
                                                                            'ϥʴϟōŅò]ÈlԮɍ¹ЄƧȯ϶ŃгПΈÛ˧êӶŉƯζҞǦƒ',
                                                                            '·āW\x9aѨχũĿdЖκ҉ʑѧѽǨОƟPԚ4ϮȉÿѳύƖ8Ԍф',
                                                                            '\x92ϖǔēӘĖӤ˼ϰҠӕƔόҜ͵ʡ˨¼ȘҩBҠńͳРȚĕʣžŲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ě',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'Ͽӟϝ=ʬƽӒϬȲԬӳԝɓԍ˫\u03a2ΠНДǻ/ˉ2ͻ˓ԪΕ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201323.241798:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Ԕѳηʂ˺ԋϼĬέșŷƗʺԝ˨\x86ŷ3ˆЉ\x82VҀșŠñaˢχИ',
                    'message': 'ҸϽ˜c\x94ƯÌɒǃΈŻ҉ȧǜб˛ĠςЪх0ȈϮ\x9e˫ɮŌѷưʷ',
                    'arguments': [
                            {
                                        'name': 'ѤμЕоӍķўϷºǥɏԃӐ±ʃåґƧÛƺϖΐпӓӾȆŵʑO҂',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "ϐäә·Sșŉϓԧ'ϣcњԙ\x82ŭǗѰ\x81ȁXӶJʲɔɩӳż3Ȧ",
                                                                            'ÒԒѢÛ¦ӏ\x87ȝΓӔ҉ӤӾχ˕ʹϵʈĵϕƈʦǭєǉĊӡԕώɚ',
                                                                            'ōͲЗҤѸĺӑtĉȍ\u0379ԇЮЖʠƙϞĔɏʠ\x8aѲ˛ƽʗǖɶhίƜ',
                                                                            'Ȩ˫іӐrvåНѓҵŕĆΝ`ԭÌhбƏ^ƘӮɠʢˑΉƹҶG7',
                                                                            'ƘĤԁһŽȍǷdӉŢƎțҔÖÞƩĭ)˅ХȚȶӧǼЀœƿʸЗȍ',
                                                                            ')уςӛφŢʇŲĢȾеƤƐхХбĤŕӱΡȺӍȊ\x80\x98Ѱ\x8dʗ9Ф',
                                                                            'ЦƣХȎӿҹeϋнӕѹ˖ǿЛőǠ\x9aˇб˟ʗÍӍϫɃ˰ĎͿТζ',
                                                                            'ϔƯʹÉΏȞȊpɯΔΉԘųƤǘθŉnG³Ğ˵Ћґɷҧʷѿà8',
                                                                            "ЦˍɡͲʢňϼɍŧ\x9cŔNҽĬ'ҟҭ@ľˏҺёŻӑţƗlӷƽϺ",
                                                                            'ƟêȻȤԘȍĨ¸ӫљɇēƹ\x9dŮŁÍ˥:ʏÌȕYѥƌԜ˳щȝҲ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ċҟ¶ҽӯɜwŉœɪԝȺɕ\u03a2#æȕʅϵ=',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʸ ǁ¬ǚþӜűƟ˕\x8c;ӹӨBȿ\u038bɸƁұʬǴНϹǯŃȠŕ_ǉ',
                                                                            'ϴŔӇǕŁƀɿХƺўōЬԠżԃʃЊƙ:µʾǱ҂ʇҙωĚȕѰɵ',
                                                                            'ȿɀÝҴӣĠʡǠƦȫƽʪёɊԚяÔr¸\x80ѧ˪Št˃ŖÉŤθʶ',
                                                                            'Ūaƣʸ\x8eŀűΒĤΑъ\x86Ӆ\u0380\x8fʭʉӨ\x7fӑwюsɳƩÐŵĒVӒ',
                                                                            'â\u0379¶ƓԎƃĲȡŁзЉт\x8bɀjŢΖ˓ԗȏɷ\xa0šӫȫϲƉD:ӂ',
                                                                            'ӟĠͶѦåǙ˟\x9d˥ˋһìGÜџϰ\x9aŸů»ȌюĵˈПѶ§ҠҾʹ',
                                                                            'αɧáƳҡǃ҇\u03a2ǥԋŢôʶͽҼôgεoОʹģԗЙƜΉ¾ŹЗ!',
                                                                            'йΑҍ÷ʶɨϠȱ?ӉÕƾ\x88ɰЖɾǝÑ\x88ȁɚú6ϫӒǠɲ=˶Ƽ',
                                                                            'ԇн˻ӯŒ!Āѩˠҁ҂жΰϼ˭ŴŦҧԌĐǿА˔CxϽ]ҘÂҮ',
                                                                            'ĠӇԅϧƌō¾˒ɹϯǾ˙ϧǧĻȯԛÐԫέЃȷΕ_ƦϺͷфԋƤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '+ӅδȪԌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            872784.3420550707,
                                                                            840525.1218692219,
                                                                            229795.3372351323,
                                                                            278611.46284296655,
                                                                            446398.6515337633,
                                                                            241310.09290525375,
                                                                            419021.39379788295,
                                                                            958951.6472346843,
                                                                            605272.3628873231,
                                                                            3373.1008621745277,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƧĶͽ}lВưӉ¶ĐĪǺВ¿DѭÆIǨԍ˯ё^Á˚ϾʰțŭŽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201324.098538:+0000',
                                                                            '20210909:201324.114827:+0000',
                                                                            '20210909:201324.130953:+0000',
                                                                            '20210909:201324.147949:+0000',
                                                                            '20210909:201324.164537:+0000',
                                                                            '20210909:201324.181878:+0000',
                                                                            '20210909:201324.198546:+0000',
                                                                            '20210909:201324.215460:+0000',
                                                                            '20210909:201324.234980:+0000',
                                                                            '20210909:201324.254121:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '4Wǿ%ϱsλϾǂáĎ˅Lƺ\u0380ǫԟ˹ϘԠҟʐʗ1ʔʦʈƽaϘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 233925.35722456058,
                                                    },
                                    },
                            {
                                        'name': 'ѪԤ*ɇͳϱˎĴɍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŭ¹Д˖ŜœѢ˓ť;ʮʌƹӍϴ{ȭÚ˙ǢɔǛԂƍğɣÉǘÕŹ',
                                                                            'ʸʗʭ2ÇƓÃˢþˉӅɚдͺũǌńǛԐgҢΆĥ҆ҮÐƻȬӒϩ',
                                                                            'мӹϓѪ1ˋŪΖƊ˖wӍƗÊʧɜ˹˹Šžӭłɠѥ¨"ȱȼȋϫ',
                                                                            'Ϲ@чӶВрɚɾžЯӔŕΎҔ¸ʰƈϲʳV\u038b\x86οǵmġѬƓĊҸ',
                                                                            "ΚǶϮÀ\x9cϋ5И!ņƺǣЯд'\u0379Ќ\x7fˎԑŒжβƦЈĄԩÍȶҢ",
                                                                            'ѨϣќҔƘНɜʀũяцƞϰýԦɝѨӝУ~ƊʡӷʳсԪĭŞԍП',
                                                                            'Ò+ŻʟǖιȸƟҟ΅ҐϭƱӀ˶ʒǉϢ˽Ԝԭ#ӓ\u0383ӐȐϽ±«Ѕ',
                                                                            'ҪFӉͼϘԥĻδÓŘʤśı\\ɌƜϯìͲʒрѣťøїɹȚ\u038bτˈ',
                                                                            'ƑβϹ\x8aѶȌǘΧѷɍŐò\x8aҬƓªÝťϽћ¯7ϳҵĶ˝ӂͷӮĀ',
                                                                            'ųЫʵфҍЏ\x93ЄëĔ˷ýːèśБΞƖʄԂԜƠNԣʛĐѬѣ˝Ӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'yʸϡΉɸˊӽɘͳŸԣ]ү\x96ŮϐǗƤҸШīϜȁлń˯ʯĄy',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ÆȎǭӃƧԗОʧǰšҲѕʾϲEбȁDĩȂϫÓНϮͿȍӰΞϷ\x84',
                                                                            'ÆˍǫȬ˻îŃʪȍН\x94ǸҽɱψȜ¯Џΰˣ˕ƫ˞Έ%үҶĄȏԖ',
                                                                            'ȷԩã҂ǐ©ΟɃӒɞвɬϐˆóǙϩӌȺАŊʹǌŠҘ,ìÃԓЁ',
                                                                            'ǂªSҊ\x8dʦĉŽͰʬȌǴ\x93rЈˡЯΥ\xadŰʂĐƛ¢VыĥÜͱƅ',
                                                                            'ȔӈύĺˎώŌƁ7ӆҔǴŪɚǲ˴ǻԌȬν%ϽŇѶχԧԆ҂Ԟˋ',
                                                                            'ŅȾ¾ĔˍǼхĀΚųźǋįӛʁĆЬÇėĥĀʥ˖\x99yɀĩЉŅ"',
                                                                            '5ԊǤɨОҠԌѴÅωҮҗϠùǎȔéЙoѳͿɺ\x8cϩÓōрÖȦж',
                                                                            'ȀλϩыҋЖҠФ˭Ӧ·ђÌˏȅίԥʺmǩк\x82ȵƲóȤȿ˩ԡ;',
                                                                            'ԫӄ҃ǖβ¯ͶĸsǄ9U˯ȒąǹĸǽϼƬƳҾʮ\x81ƔӞϝdѷӸ',
                                                                            'уͲ҅ήƗɍíŐϔҳɇ\x8dƨ`ӺҼ¯ԛưĕΈҧɋӢӀůlԮΠӤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΛИɣǾͳȶ³SϖδʧrͲʤ\xa0ԌԠgɖ;Φȍ-}ŌӧϡèΤb',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201324.914927:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ıіɷŽӹßӠӖȽƪʺ҄ɱȴ°ˢʻãÙƒĮ˾\x88ҘФъӢɷΒˋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˄§ƦȦèЖĝĥɞƫЙПԎüǁӳ˜ӟԨǇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201325.145679:+0000',
                                                                            '20210909:201325.162637:+0000',
                                                                            '20210909:201325.178741:+0000',
                                                                            '20210909:201325.195235:+0000',
                                                                            '20210909:201325.211271:+0000',
                                                                            '20210909:201325.229240:+0000',
                                                                            '20210909:201325.245595:+0000',
                                                                            '20210909:201325.261920:+0000',
                                                                            '20210909:201325.278749:+0000',
                                                                            '20210909:201325.295354:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˛șƏƬȘƋc\x9aʗΑ¸ԟȍɿӎӃį~ΐԊƤї\x96ПƤϩ\x83\x90$ƚ',
                    'message': 'ȸ(ёÌБСģђ7ΆӪʺ\x87ρƩȳЊΉΌияǌϣƛΟȼ{ЧНʋ',
                    'arguments': [
                            {
                                        'name': '#˓ͶйюΈϹψШƱЦ\x81ʝБ_ԊǮǜƾԤω˔ѥίƯςŽӐMϯ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ǿɐȱƐț\x8dѺƚ'ʩѪʙåϻ",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201325.699663:+0000',
                                                                            '20210909:201325.716539:+0000',
                                                                            '20210909:201325.733379:+0000',
                                                                            '20210909:201325.749821:+0000',
                                                                            '20210909:201325.767540:+0000',
                                                                            '20210909:201325.784336:+0000',
                                                                            '20210909:201325.800441:+0000',
                                                                            '20210909:201325.817276:+0000',
                                                                            '20210909:201325.834059:+0000',
                                                                            '20210909:201325.850480:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѼͷƎξǴԖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201325.941410:+0000',
                                                                            '20210909:201325.958051:+0000',
                                                                            '20210909:201325.974345:+0000',
                                                                            '20210909:201325.990493:+0000',
                                                                            '20210909:201326.007723:+0000',
                                                                            '20210909:201326.025236:+0000',
                                                                            '20210909:201326.042968:+0000',
                                                                            '20210909:201326.059865:+0000',
                                                                            '20210909:201326.076057:+0000',
                                                                            '20210909:201326.093194:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Eԅ{˳Ɍϯǲ\x8cĬɔ˩Óљǥϱ\x99˷ίɲʎ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            463030.5102639266,
                                                                            159814.17364995703,
                                                                            855091.0760105103,
                                                                            796872.7991493633,
                                                                            378248.072488589,
                                                                            346961.8036745862,
                                                                            531024.7009459651,
                                                                            997195.4745448953,
                                                                            495242.03010531503,
                                                                            122342.15543570241,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɺ\\΄˖}\x9bΈĠԀӍ˽Ɗ˧ǍùŴԅΩϤǴİĺ\xadʖÔƆĥҦʅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 476739.0750630854,
                                                    },
                                    },
                            {
                                        'name': 'ĆżԨñZѩˤƅˊĺΙÎѩҤφԙҎԖϗӸҭ`ӤɬѲѭѾčƫγ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҏѺʺНǺҰӱʶƒԐɢɑƖʫǻÏ\x92Ѹ£ƌĵĞɝԏгφӾƶОʍ',
                                                    },
                                    },
                            {
                                        'name': 'ǆIӈνΦπӍϬʐʀˬԀΣӇĉͱȳӪŗϦ;ʕȃīҒѰƃ\x93ɮ˵',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210909:201326.553714:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ħ:|DȀ˚ȼҡӋɹǙƞƑҰđԞўѤ¯ӐЬÏϑ\x7fǚϥͳÎӧβ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'χÝϒǧȑӞˎʡͺȩԢ;łĤңĸѥĝàͿΣϧԞɪϮȪŢ¸x˧',
                                                                            'χҏÀ\x88дЇѯіƣžέԟӦȕȑ˄ōǩɪɘӢŮƴӆуҷÁΫϫϏ',
                                                                            'ƌȻȦОǻʭ҇Ӯ҂јӄԃóӿŭԀ˳ƖѓԆ\x85ƹʞcļǯŕЊEӺ',
                                                                            'NΥԗ²ĝʬΐ˰ЌD9* ˞ʵĊҍːЊʤ\x8aÕ˂öѲʕȀіŤÊ',
                                                                            'ȸͼˇʅɺǥϰǽƀǴѻΔŌԁȰϡб\x8có[ʡȖ˞űȡпȋQ+Ӂ',
                                                                            'Ɖ˵ϒēϔĞԪӪгЮ®ВзǗ\u0380ȥuϰʭǉÑˊӺϤʒΧЈӐʹϕ',
                                                                            'ŮĵơȔ\x86\u0379ƨГɵ²Ǝ[ЫάƀœǚQȵɹϵӌЁ\xadӔĘčбˮɫ',
                                                                            'ϴҏҔķȑĢńʶʣѦ\x9d\x9eӐƌѳǳ˞\u0383òͱÌˍʒ˃6T\x84śɱ>',
                                                                            'ԀʦÅńзˡÃƸ\x82Ιŉήμ˦ƲĿłǆ΄bĖq·ЯӎԀұίΪŅ',
                                                                            'Ϲʳϴɶ\x9cıѭà҈ĶȊÌƯЭpƤΚǪƖɐǕ*ǝɣϭ˷ϣăϡʱ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '/ĦąѶɺѣƞƐǎǽѾƞјȯӡÑƲĩɇɤʃ£ǒȾŨ˷zȬȉˮ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 956889.0176080719,
                                                    },
                                    },
                            {
                                        'name': 'әҏиÃȥ¢ǶƉϙǽϐǊƇ\x8fбƆʬĄʰÿʜʷȾұȶĨ+Ç,Ӽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɼӧњʻɩvƏɁΘĎӶǹϩ"˳ňɇ҃˭ɚͽϳБұˏ-аʞσԡ',
                                                                            'Ӥƿї˨ƕùѐıѫđ\x8bԈϴ\x9fɑə\u0382҉ëź\x9aԎԒ^γƑ¨ϯÓɵ',
                                                                            'ˀҲI˝ГѢԈ˨Ӻɕҩ\x88ãȵǦϟԂ\\ϟńõȝõӻϣͽѥґ(ƚ',
                                                                            'ȇтП\x86ӓІϔ¿ϩȜ÷ӰͿĒˮʑŽѕ\x81ȿóƶğêɟʖɥü˵Я',
                                                                            'ԜԟȉŘõʽԋѰӱӟǿѸʐĬЊиΆƛԘѱјӥϝЅ\x89ѫƀΩȟĈ',
                                                                            '΄ůҔӏʎä\x9aƹ*xѹ\\˨ˎԤǧ˯Ѽ¤\u038dŮɁЄ\x92ѡlЃөԗf',
                                                                            'χЧÜσӠɲˋλ×ɐƊԐƥŞ\xa0ќƆʔ¼ԬϚɐӗ\x9fɾƿɩцѭф',
                                                                            'ЂƅЇΜ~ЫМƭӎ\\,ȶƻ,ưӭ3ɫԪҒaʮ҅yϷјTʒΤ҆',
                                                                            'әӊ\x9cćԛʫġӛIi\u0381˜ԋӠίŒϣҀɭ\u0378ěĠԒ\x87ΊƴΑIԈʏ',
                                                                            'Ȥ˷ʄ˫â\u0379ϣ1©ŀĴɸɓӣʈʰΦ\xadŁϹ˾ΠорɘA˳˶Ǿ\u03a2',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϷҒңΟĬƒʑ\x8dʵĢǗơɰӳʭʹȊʵӭаЗЂϋӘƥɐУԋёϙ',
                    'message': 'ɠӹĖΦˋΠӝψΰȎΞԩӒŵǞİʗϬÁÿȱϋΟωƶơ˛ǺϊǊ',
                    'arguments': [
                            {
                                        'name': '˓ҏ¯nεϫúĐ¯;ɓљ½ȤӒͼϠǖɹTЇžӓ_',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ϼzЛǁŽї\u0382ŻʝɅЖџŪ§Ԡ˂˨ɢ\x85жіԨԋR½ǃǷʯÂξ',
                                                    },
                                    },
                            {
                                        'name': 'ҼԝȂkȏ\u038bϫѹ¡ƣҷŤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            76119.39477621409,
                                                                            402481.3841937598,
                                                                            121213.40228551792,
                                                                            701937.4029936411,
                                                                            767576.5938019142,
                                                                            565785.4929188613,
                                                                            239461.57198629307,
                                                                            629488.0869526081,
                                                                            29702.59278371955,
                                                                            700295.6418201664,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'яϯӂǚēåƒϕϵӵ*\x86Ϛœ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5442683661635468871,
                                                                            -7470542696051212655,
                                                                            7606468624048723666,
                                                                            4728284679442799333,
                                                                            397561939103294952,
                                                                            7199542782337767069,
                                                                            2956480169053437383,
                                                                            5878703372714554849,
                                                                            438014103632070617,
                                                                            4373691827062289449,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'кȧѤəä˳оԃӎѠ;¼ǟĬԖЊЎΏɚȇ7įɆԈЇӺ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8073984724702981757,
                                                    },
                                    },
                            {
                                        'name': 'ќѦԚ\\¸\u038dԎІϡ0ŤϞˉoԇȧӪɜëƂ\x91ӂ˱Ěï˗\u03a2ҩŚӸ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201327.896383:+0000',
                                                                            '20210909:201327.913802:+0000',
                                                                            '20210909:201327.930832:+0000',
                                                                            '20210909:201327.947481:+0000',
                                                                            '20210909:201327.965687:+0000',
                                                                            '20210909:201327.982718:+0000',
                                                                            '20210909:201327.999596:+0000',
                                                                            '20210909:201328.017072:+0000',
                                                                            '20210909:201328.034353:+0000',
                                                                            '20210909:201328.051759:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҴɸӭӭѿɋҹӈҿӨüǼįЌԪʂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 532771.9324562508,
                                                    },
                                    },
                            {
                                        'name': 'ɧ²ĒѳĺlƞȽ\u0383ѝſ˛ŨNʹVÌСʇéȔ\x83',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ɻϨġ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 678444.440977942,
                                                    },
                                    },
                            {
                                        'name': 'ƶԩµǈ˗ªѼжϥƞƻѰCЊӔε7ѥÌŁ\x84Ż',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -53626.28984820304,
                                                    },
                                    },
                            {
                                        'name': 'Ôʘϥ˜˚ˋМγːȻȜM',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ФƕӶ΅˰Ԟ˷ԂyƩďńϏ͵҃¥£ͳΎӖƥȮĒČāųɔŊơϿ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɅɯӝĔ.ƸɸƋю}$ҒѐɮǙȂǽϏҴɀȉѴͷžɗԗʼƘҬ?',
                    'message': '£9\x80˯ǥ΄4]κʝ˓ЁρҷŽ˾ŽeșȘƶʑ)wͱЖɆŶcǿ',
                    'arguments': [
                            {
                                        'name': 'ЫϺзûȋȿşөҹʳ.ǴҜΞαùoΆɱ\x9fѸԈŸĂ\x95Ș³ΨӥΡ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˩ºǽȲŴƀ§ϜČκȊ?/ӲʏíƷȔӄǣ˅ťϟӿǺ9Ǜġxˏ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            516625.30230487394,
                                                                            -4440.646647899732,
                                                                            62173.39283429299,
                                                                            882312.5730435925,
                                                                            548603.0147890795,
                                                                            123587.6587532826,
                                                                            91863.0645038531,
                                                                            581400.239472214,
                                                                            530996.3730122264,
                                                                            621737.9937757129,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˭ɝǦԍƒĿɧЪŻ͵ó\x93ԛȓȥǔͶ-˳цҷǭMwѻϣҺԖФǦ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1760381080250512,
                                                    },
                                    },
                            {
                                        'name': 'ЪǎSɳÌÇRϩʠҫɑ϶æЖѐŝЀϺǞ\x89þǜͺςȤƂʲΐƲͳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            450701.57933488395,
                                                                            318412.24310300563,
                                                                            659902.9284114541,
                                                                            990522.606733826,
                                                                            853143.4529788222,
                                                                            907105.6241321726,
                                                                            633825.1978048491,
                                                                            972505.3628419929,
                                                                            862805.185163809,
                                                                            948622.3270694884,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΧxɈҰϧː˭ΧәӉɱ¢ɰŲ҇Ǐε\u038bнΖϴ\x89ɬв',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            176892.97431686253,
                                                                            -19066.111749250413,
                                                                            456217.08992649196,
                                                                            611455.3595644869,
                                                                            537422.795970899,
                                                                            940282.7144354844,
                                                                            -27318.442751155002,
                                                                            536264.8454694775,
                                                                            548868.9594732011,
                                                                            584568.0776682091,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌƺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˪ˊăÕdҊѬΚŋ/ȦǓƸʈύ˾èǐɜǘѱϡϓЋͶ˩Ϭӵ\x95ɉ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ƌäЈćĉњĚƐӮĶʤɅԠԚPΧԩƺǏϧʿ¨ɅƤĔԜ8Ҹ\x99Ӎ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѥϵ˴',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1236433253378035487,
                                                    },
                                    },
                            {
                                        'name': 'ǄŞԋѴƕĂʥÜóʨ¢Ż',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȂǷϞǇԪԚß˫Ф~SĊʦЗ˧ѡĎŬĶԑɀǱɳŐʡӝȹΦΚƣ',
                    'message': 'ͶѲΌͰț»ЋAИ_ɕϐӥǏ\x8bӖƴǛưχЅҲϝΧӯ΅ԀϞɉȜ',
                    'arguments': [
                            {
                                        'name': 'Ԏρλю\u0378ƖȐ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'βŐĴҔΝčǂһʜˮҽуӯԕđ\x9dϨ\x85˒ӲˋƯСÍįǥǙҝºp',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8590677537969569506,
                                                    },
                                    },
                            {
                                        'name': 'ƱƲΦ\x84Ю.ºǟҪΘɥ(\x97їѿγëʶĨҾǭþAáǃԧϟϖtƻ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'NǐȲɮ\x92ıƲƚςƃӅϳǝʿ\x96ˡ¼ɖʒ϶ӱˎʆҜĥĚǊӼͶ¸',
                                                    },
                                    },
                            {
                                        'name': 'ğķǎë΅ȿÚ\x94ЏǕ>ҦƚbФўıƛȦǂ˟ЌdєϞȢŝʢѝ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ōʗzʫȻ=űLЇÃ´˒ωǢҦʬţӂϣƙ[θϊ˜еƜĤŜÖǯ',
                                                    },
                                    },
                            {
                                        'name': 'ǨԃΰіҀХӳʂƲƬҦYOģɠƣ|ȚũŏͿѨşάǾ\x96˝Τˌȷ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5611207682675956944,
                                                                            -3245435088400943569,
                                                                            -845778907616583226,
                                                                            -2703991264234154233,
                                                                            6752893126549083529,
                                                                            7817071116405111560,
                                                                            6774184135051588275,
                                                                            -6012410528462692142,
                                                                            -772263365928849877,
                                                                            -5883922541787229542,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'їЊĝıǙӂǎЖʂгʤԅςȇşԌӺĚΰϗΞǪĐԁӑǘƠԌõƽ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201331.085412:+0000',
                                                                            '20210909:201331.109161:+0000',
                                                                            '20210909:201331.130334:+0000',
                                                                            '20210909:201331.152765:+0000',
                                                                            '20210909:201331.177043:+0000',
                                                                            '20210909:201331.199099:+0000',
                                                                            '20210909:201331.222800:+0000',
                                                                            '20210909:201331.245737:+0000',
                                                                            '20210909:201331.263428:+0000',
                                                                            '20210909:201331.280592:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ї±\x96ųÁόҏˌŬѐ¢jЏʰʨİɢӶȧęΌѕʘǻη]·ʞƸɎ',
                    'message': 'τ˝A{ϤȜ\x92ȣӠ˩˳ƤԒʑä\x80ɍ3oɵ˙Jeǲ˔VĻӇϿ´',
                    'arguments': [
                            {
                                        'name': 'ҚӥŌКЙūЬ˪ȊţƘάãŇèȴ+ѪsΨŖɼɹŒƿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ж˂ƥĦœЛӈӜϏ~ԪUо\x96ƷЍӾ¢?ʹˊĐ»ԜЯÃԪȈ\u0379Â',
                                                                            'ţwƂͻǛĶΐɾGȡϛтqʷƸ!°ŗƔ϶ѩɖėϭĉԌθЈԘþ',
                                                                            'љΩϫЦ\u0381ɰƅԊѳĢТ²\x89åˀʡҮТЋçʷȀλПˈɑѧȟźӡ',
                                                                            'ʷ?ĦԫΊʃg˜ϟЋnŹ\u0380¼ØͱȢÿЇɏơάОӋ¢ʯӁÎʙϫ',
                                                                            'ɁӽćͷѺԧ͵ƋǖâʀɥǹƠьŅϚñͿϰȮ˕ѴŰӜ\x89Ԡ',
                                                                            ']×ԟήϋɫӠуώǦҊæχͱӘȼҶӹΤϞӏÉɖʧʖĄvӁ}Ӳ',
                                                                            'mӎȥɔ\x81ʲŀƯƑԏϱʔ͵ʎÏȄӴ\x92ȂЊӱØļɱљ\x99ΕΔ\x98ě',
                                                                            'şƮʇτѠʃˉЅ\\ƂnǵďΦʶXÉӕҁ\u0379ҬϜͺ6<ƼƮʗTέ',
                                                                            'Ý1ÀєѻΌϩʄȸѸУǭԛéń҃˻ǧ˽;\x82ʽЁ¬ϸĎāԆήː',
                                                                            'tĂ҅ЩąÝóӐҾϤΑНĵɩ\u03a2ŇǻѓƀёҽıѧφϱŽΦȠϣΫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ғΌ˃ɅʁɍϽNś%Ɨį˾þɕƃɑɤʚҙӑ}˶ә4ϒȬ-²',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '¥Sɔ\u03a2Ć',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɶȪɱӫ\x8cĥƢǡӛтς#ÙĔοǢҜРҲωƩ£˽ЋϽuǶȬǢҙ',
                                                                            'хрVӼ£Ä˷\\ԏґсńÇţȺƘɈŶмıɡŸɪɖ¨ȰӫǼǴԥ',
                                                                            'ȞŢѕɾϴԚǿÿɒ<ӣϱƨŔ¼Ɲ˗Фʤ˪ėĈСɾԭȾˆҮ\x86ʁ',
                                                                            '¤sƨә\u0379\x99ӭԖɅԩҏуйѶСȎǞӱˡɽ\xadɽȷўłŎÿʹПԖ',
                                                                            'ȒǰěЂ\x97кϞΊξLĕҏӘˏżƑΤńì!ЯҸǨɪӏJΌԘˡŅ',
                                                                            'ѦӳЏʕ>ƦȘһϕčǬxΐЪƌȗγҬӈǓ˘ФǮɳĒўʛ\u0381±Ѿ',
                                                                            'Ŕøŧ˂ξǾ\x95˶ˀԠŠϮҔΘԛ\x936ˆϥéƴ\x93$Игϳ¿Җѥ\x81',
                                                                            'тɯԘϞń!˭ȯў˸Ǚϯǩuʡτ\u038bĹ\x80οʵƀFˋ\xa0¤НÈˮ¢',
                                                                            'ǥωѓÀԟПòɽʙǫʧОё҃υƗĄґǭӀĤʲȺοʣѫs÷Ϸª',
                                                                            '˷ԟбϾʈοƓԟƫyÜэ[ϴԢΧɎҜʭ@ʸ@ϛû˂ϙ\x8aϽʏԛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ïҴȞjƓԛһʃѦǽӶɣ҂ůЋАҺˍʌãǵ\u0383þŎƜŏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ëę£ψнȺȢóɆʩ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ņēȧ\x95ŧͺɂщ>γɦгРΐŁˮUч\x9d',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˴ΥêÔ˶ɼëíʚΑʞǣdĘɁԓÐϨэĹίǐŜԟ˓ǩϞҁӟҦ',
                                                                            'ɣȟԏÅ\x99ΙìÓčɇʄҀǇǗҲǓͰUĉǸӻĸʴԢǬќŸӾϭĖ',
                                                                            'ύѪγğǄҎΛŞȍ&Àϊ:ȍďˤǾʱσåыҽňĜʣϛɲjŕʟ',
                                                                            'ΞŗļʹƥӘ5<˺Ň1śԨ҆˗ǵ:Ɔǁʰϙњ·\x8dġ҉ʩνœӊ',
                                                                            'ſɐ·ζPȲƖӿѧʇŝģӀðϩϯÃґǌԝĬɦ͵ώxΩůɣţί',
                                                                            'ΘѸ˟ȫ`њBϐѿˋόҠϸeȄôɯēȬԂ\u0381ˊқӃ˺Ҹȿϣʩì',
                                                                            'ҊōљΚÙыμȵńƄôʐǬ`рѼȓ¨ґ´ІҀΊҖɯљаĳӌƋ',
                                                                            'ȑЬ҂ĮԖԆ¥ǁΫʲҗʜԨǊƅҸюǖʙʋǖʪѕċȇɷЂ\u0383ǯИ',
                                                                            'ôǚϓĞ˘ѥłϝƬƨ¼τǨԑϨΗ"ĔˣΜĦѝМøϖ©й˞ųĕ',
                                                                            'Ͻ\u0378ɻʡјyǼБԧε(&ԕӇԥҰƈГȅ¯ԝɍҋįΫǿԗȲǶǛ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŴΔǹăÊŋɏҲНˍæȭƣŜř',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŝ\u03a2ƧşǺʈÜτәϹΘtЗѼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '\u0379ĂȑʱŮź\x89$ʯӫԛ˺ˊӖς¶ɐ ĹҒOёȤԏÁȾѬƼŔǻ',
                                                    },
                                    },
                            {
                                        'name': 'ǚA»ƭϰϬĮʴӣǵˌŨħȱԞũʕ϶',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x9cԢ_ļˬңΛҳżɍǔїϽûĒʦȢÞҏюÍԀǈϚ΅ςõTΝϋ',
                                                                            'ȝΕ%Ͽԗҙћҽ¸ʇвԡЋÞʭєԀѕ˺ŉ҄҃ƤǗԘ)ʬĳˬї',
                                                                            'Ԅ\x84ƊԝҕƹˡǛӑ:ѐԖ϶«ȗˌǜ\xa0Ëԉӊɏǣșԃjǽθӹě',
                                                                            'ȰԙvYˁϱ\x9dÄzƒʦ\x9fӱȼЇѧƦщȡϼӄˀɵƬĸʡу˼ϦÇ',
                                                                            'ɹŢΐɾЛ¢ƽ\x98ƖΘİoҎжƵӾӰʱΡҝȓ˽ϛи\x83ςФϧUӟ',
                                                                            '"ĻІúĥ\x91ɗFρ§ÒԮҕEҜĠȞЂΨжҔɡ\x96ϒȪƽɌĊгԫ',
                                                                            'ˏÒςѸɶAj˷ѬѬĢǆǺԖԉľŶ˦ûLӽɪŅʽѕƟźÆԫύ',
                                                                            'ƁȇÏƻÚȐ˪ʹUș^ԘҚφǠˢԉԥ\x88ËϠǌǨŻqɀǍȽӺƢ',
                                                                            'ŅǁԈǱkƤ˫ӽyˡ\xa0ԕҍԨӉʟƄƧĽyυĻѧĢ\u0378Ԅöƿқɦ',
                                                                            'ӓҭǜȝƼмϊŖˉBό˱ҏǸȇӌȂEŲƀΝÙӷƋ\x8cͽΝƍхԙ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʰďͲЧʤ\x83ɆίÓ˙ĘѾʿʔsρэ˃ωЍȋǶ˂\u03a2Ӯӆρ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 376512.8098969664,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɟқɑ´ǼɹϱƀîϿЊхď~ØӊȆηˉɯɼҒɡ˸Ēʜ*ҴȭĹ',
                    'message': 'ӂɀ˖ƬůϫƪʒӅāːǘϪԓ4Őҍхҋю\x8bоȪЯG\x9bĺǕqņ',
                    'arguments': [
                            {
                                        'name': '+7ØЄѰɬȽЅ˕îsǲɪǡƣ!Ȝ&¹ϙΒˠĝǑ˸˖˺ŸǤi',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 459000.7289138776,
                                                    },
                                    },
                            {
                                        'name': 'ԤҙȳȠɅ\x98µǓ\x90ŵ˴з',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ņӾ˒ӿɺфUΰƎ˖ӁȂЮļИ;ϒʒǡΧέ¹șЬ×Μпψ˱ʳ',
                                                                            'ȶη½\x9fƜˣ\u038dŗѽѲmɻþԔєɢѵȎǏ¢>\x95΄ƮĬШӫЃģԇ',
                                                                            'ɚʎœŴòńϞÙļŲѳбÐΨɱϟϷΌ˻ϭͻʫrȘԀȆćӇЛÈ',
                                                                            'ĳˤȓрƥÔʊȭԬP\u0381L҅Р$ɿэјϊБʙɏȌʣʄƚ¸ȸқ˲',
                                                                            'cmǺ\x99#ŉԤʅǗ(ɴÄ\x9fÁ҂ȊĦΩĽʯʲɚʓÀѹƓɩƶɧċ',
                                                                            '҆҃ɿ˹ιіª%ӒˇƂźŰͺϘǀҪϧԅӱʥȘɊ˘ԤϝõψȈ$',
                                                                            'ϯҟ\x9bЛϚńӅƃ˪ũЩ΅ζȬŅ¢ƥ¯úȿԈ8ӭľϕлôǍҩȰ',
                                                                            'ÓFτҳ˯Ϻ?ǘ˓ИƥȆCŎӔϹτˤƄɴұƿζƟȞϟtąџϲ',
                                                                            'ɍϥǭο˝\x93ƿǌʷŰɟδ"ϐƂӉɭͲ7ĉ϶Ɏԍάηϑіѡһ҆',
                                                                            '$dӚLβѯ\x87ũþϏǖϹϙˎƷФ_;чñǵıƣȲӮʓҨȵǖ˅',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "âƱȦvсԄɮѢ'˂Ҝсϻ\u0378ҰĐɸ¬ȊyЌŸØƒ\x97ͺ9LŕԌ",
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '1¥Ӧšωұ<ɭεΧłƙɵɃԓAŘĊ϶',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʞЩʅԃȘЄѵ\x9aԘƒ\x8e@ξɃȥҫîɲɾӵкҀñ÷ʮų\x86ҽ@\x9c',
                                                    },
                                    },
                            {
                                        'name': 'ëğίɐӅǉø±ɑԨϟδÚ\x93єͽж˸úFЗӣ\x84ӦцƇÝʃȬ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1807651424214792388,
                                                                            -1683266671520041397,
                                                                            8809233962787398543,
                                                                            -7429016171656892063,
                                                                            -4455324149095202220,
                                                                            -7187286288146029678,
                                                                            -4694760643567757415,
                                                                            -948338749409732906,
                                                                            699567085511387390,
                                                                            -3275026290772934213,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ']јːη',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            849948.125912847,
                                                                            897633.7251395795,
                                                                            978415.117637319,
                                                                            827662.374656488,
                                                                            398311.84326264384,
                                                                            769177.3200447303,
                                                                            463812.85948472645,
                                                                            989182.4000259903,
                                                                            628225.3902777846,
                                                                            208850.2023775985,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'GҧŤɸа\x87ȀӌτѩôłʒƶǰΝ.ǑȴϞȍÑтКϯѐÿƲ΄Ђ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -9218956716779726228,
                                                    },
                                    },
                            {
                                        'name': '˫ÄƗĸȊ ȁɷӝʯǁɉ˒',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȫЇҮƟҶȻȑɴƝţǔİϩSϓĤǚ˄Ł˥ĕƯʐƜśҶëфĎʻ',
                                                                            'İĮоʀЙЮɪѧη7pΐȠXͷɵ¿ķϿ¾ҘѯŻїǞΌǴž\x92ɣ',
                                                                            '\x9bƷрʙд5ЦǾиÛП˺ӴΨÇʫŤǉ#αβƌƯӐ˸PÌɇŃӖ',
                                                                            'ѓÊѶОљǂόŮǨԄɌсşЉ\x9f\x94Ѥƾʵ÷ŕҤťȔΧǬʽИѕȭ',
                                                                            'ҁȈʠӹƾǠvͽĤԈ˸Ħ҃ƚʨƁ|\x96;ӯѾҔφԚфӑɔҸĬũ',
                                                                            'ϚƱϙ©·˅˚ѲĿҵůȵ\x9dvɸѷRЎȪɐtε.ŗőȁςľȥМ',
                                                                            'ƕŌЗЌлѩ½ȎЛſϸÙњ^ÅҐξҀCƩżæǇfƘȢȈ>Ӧ˔',
                                                                            'ʞѯãӇһгˠ;ҫсƁÀæǴǰԨʢтԣԨԞƭѡǗϺώ2ѫLѸ',
                                                                            'ά҄νèŹľŻҤEǢǀ¿ΘɩşȍƵӬίӝ¥XуȱʬεăϩЭŌ',
                                                                            'ȨŘȟĝ¾ΓІW˜ʩƫзӸʒфʸżЀǴϋ\x84·ʙρ¨ɧĊFDԬ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȷпɥƾȉʞӜɼƑăӱŠƯϕΙĻяTΈДʄ˯ƷіϘʞШ˃\u0379ľ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210909:201334.737458:+0000',
                                                                            '20210909:201334.753560:+0000',
                                                                            '20210909:201334.769470:+0000',
                                                                            '20210909:201334.785956:+0000',
                                                                            '20210909:201334.802058:+0000',
                                                                            '20210909:201334.817386:+0000',
                                                                            '20210909:201334.833646:+0000',
                                                                            '20210909:201334.849526:+0000',
                                                                            '20210909:201334.865185:+0000',
                                                                            '20210909:201334.881011:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʫѾĨʨԓԤϱӰŉɞҹ˙şϴ·Ĝ\x95öɫТ˷ǳȒɮZϿȕƕLǤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'юǕϜđϯѴҺԓи˼йŕҺӮ\x85\x98ӟΪʢ{Ȭ˵EЊήǾМȿԜҽ',
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

            'identifier': '\u0378ʗƁ\x86Ҡ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': '˝Ӫ',
                    'message': 'Ϥ',
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
            'request_id': 4226647,
            'error': {
                'identifier': '*϶ԣ¬@ƉΞ®ͰѷȋďƹӰǗÑΛƅʭԀɳʃŔɝĳõɰпЁШ',
                'categories': [
                    'os',
                    'network',
                    'access-restriction',
                    'os',
                    'os',
                    'internal',
                    'invalid-user-action',
                    'invalid-user-action',
                    'internal',
                    'file',
                ],
                'source': 'үǵȐ^¦6ÎҗϘħҰzǙĥĖѪҀZόϊEɸԡĴѸȔKѪÅǵ',
                'messages': [
                    {
                            'catalog': 'ˑ!ɻԍɿž˼ĘЙБđ«ѹΊҫĨˣ\x85ɢíԡӳԁűˇ9ǸВüś',
                            'message': 'ğɲʐťӾ\\вjͽόºĊ˂úӗқ\x9d˗ŦҀǱҵʹĬ}ȿɺ¥Ŷê',
                            'arguments': [
                                        {
                                                        'name': 'ӮǜЃϜӍΟкȶΆƜ˷НԅʫӪҴϗŏȤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ςҹİ;Ύϙfӈ\x87ǡǍą©ѕ\x95ҵȺÅϞ¯ǼҲΊôԩ˲ǥĜ˩ҹ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Üκoɑ϶ƪԁɹʐ҆ÌԚЌϹϋЪˍąʂЇʺĶҹѹǸˍϙϩŞԧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'pĖ«Ӓ1ʸӸyƗĳʸĴȹˢɼϾТū3ȻΙ˄ϔǤŧҺÑũWǩ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x8dÁŴ҆а҉ϏƂκƙϠ҈Ů¼Ȩъȣт\x97ˇϞſȘϥ\x93˯˶Ɩˑʞ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЖҡгėȔȻÕϧϲƍ˅ѨǿƬɵǌǏ¬ԢǋˍИƽʤơгԛŉǜέ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӭˑÈĸjƸqǱę˖ŷѽ\x93żxԊƕҬĬǽԚßԥЌѺң',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '1Ө҂˒ͶЖөˢőԃkºůɧЌұĳҠ7һ\x83ѿjĳĞ¢ó^ȃʥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɑΘǴєɆǹ?ϸņ˭ǁYκŷӖŷȚΜhƔǑѝĩ˝iȜҾǹ|Ÿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѨҴ˃\x9eҌДª,ԊĻʸгˇΎѯ\x8fɮ\x8fˊѤȜhͱĔ½ĺԦϤʷЎ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'z¹ҏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȃӹ˜ƪŒβӍԡͱƇWƉԑӰ',
                                                        'value': {
                                                                            '^': 'string_list',
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

            'request_id': 6290237,

            'error': {
                'identifier': '˲҇˥Ӗԍ',
                'categories': [
                    'file',
                ],
                'messages': [
                    {
                            'catalog': 'Ȍ\xad',
                            'message': 'ѧ',
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
            'nw_x_pixel': -1547653759,
            'nw_y_pixel': 1747993799,
            'width': -3894022383051323896,
            'height': -3008834128765175390,
            'ratio_x': -298659981732594656,
            'ratio_y': 1462349289031394153,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1410082953,

            'nw_y_pixel': 1598288682,

            'width': -3058118923191251071,

            'height': -227397712483677743,

            'ratio_x': 6988696136172195360,

            'ratio_y': -4910484235354410656,

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
                    'nw_x_pixel': 521122435,
                    'nw_y_pixel': -311612768,
                    'width': -3643790037403170229,
                    'height': -5728508601088129742,
                    'ratio_x': -8874109111203877705,
                    'ratio_y': -2246298144841324426,
                },
                {
                    'nw_x_pixel': -631901370,
                    'nw_y_pixel': 1769382787,
                    'width': -2684806094561459240,
                    'height': -46559449964170235,
                    'ratio_x': -5751594532309124345,
                    'ratio_y': 8983878117907345975,
                },
                {
                    'nw_x_pixel': -1365252788,
                    'nw_y_pixel': 1919635877,
                    'width': -7850385035225310930,
                    'height': -3067517219216717915,
                    'ratio_x': -646389124392688137,
                    'ratio_y': 7740435343178215918,
                },
                {
                    'nw_x_pixel': -1843419243,
                    'nw_y_pixel': -1853675761,
                    'width': -9066787803911578502,
                    'height': -2080427115731575121,
                    'ratio_x': 544037659735866444,
                    'ratio_y': 441268503184720792,
                },
                {
                    'nw_x_pixel': -849762962,
                    'nw_y_pixel': 685352594,
                    'width': -174482669302826715,
                    'height': -8607882928211279507,
                    'ratio_x': 1042096136471047431,
                    'ratio_y': 1142419485806750619,
                },
                {
                    'nw_x_pixel': 72924898,
                    'nw_y_pixel': 1338957022,
                    'width': -47234973518238195,
                    'height': -3519977477971648844,
                    'ratio_x': -7528286309514465680,
                    'ratio_y': -4216500856399343693,
                },
                {
                    'nw_x_pixel': -821221346,
                    'nw_y_pixel': -1235023601,
                    'width': -2270669969177475945,
                    'height': -2065861246646560058,
                    'ratio_x': -9084867625983883249,
                    'ratio_y': 3587970383331086645,
                },
                {
                    'nw_x_pixel': 879258593,
                    'nw_y_pixel': 654677196,
                    'width': -3133767009715144719,
                    'height': -3663146350163719582,
                    'ratio_x': 7137154986194918142,
                    'ratio_y': -4843832619928644355,
                },
                {
                    'nw_x_pixel': -1748826431,
                    'nw_y_pixel': -561465606,
                    'width': -494128598662881762,
                    'height': -3016241957663971656,
                    'ratio_x': 673076772689035884,
                    'ratio_y': -834746250857362303,
                },
                {
                    'nw_x_pixel': -236612410,
                    'nw_y_pixel': -1195624367,
                    'width': -5584900014838993347,
                    'height': -2482758866625508601,
                    'ratio_x': -9201781019449937443,
                    'ratio_y': -3407474303479397420,
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
                    'description': 'Δɍīúǹԏ˭Ԓ@\x8fÎʿњǊИϳʯιăťН\x85ãʵιµɱϿƴİ',
                    'monitors': [
                            {
                                        'identifier': 4552541,
                                        'width': 9002035206082263995,
                                        'height': -1713467728391253180,
                                    },
                            {
                                        'identifier': 8003621,
                                        'width': 8841208436356547907,
                                        'height': -9014318371204215111,
                                    },
                            {
                                        'identifier': 5631358,
                                        'width': -3408722015522076356,
                                        'height': 3977742412606368509,
                                    },
                            {
                                        'identifier': 6112308,
                                        'width': 3872870930879152357,
                                        'height': 2922207274869072359,
                                    },
                            {
                                        'identifier': 7793312,
                                        'width': 6576390955379072867,
                                        'height': -625008532005061622,
                                    },
                            {
                                        'identifier': 3426572,
                                        'width': -7885765512501299741,
                                        'height': -4892282909575504725,
                                    },
                            {
                                        'identifier': 3788967,
                                        'width': -5073601124231111544,
                                        'height': -835534288993701255,
                                    },
                            {
                                        'identifier': 156326,
                                        'width': -1087686670222905807,
                                        'height': 7466232807856887830,
                                    },
                            {
                                        'identifier': 6385720,
                                        'width': 6051094166226370236,
                                        'height': 1148950031679612668,
                                    },
                            {
                                        'identifier': 6820724,
                                        'width': -8448273582148091577,
                                        'height': -9202570267579985190,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7871306,
                                        'source_nw_x_pixel': -670150921377620800,
                                        'source_nw_y_pixel': -5631918160192848395,
                                        'source_pixel_width': -6144152147573508328,
                                        'source_pixel_height': -1172417745225867849,
                                        'rotation': -8902087329622609166,
                                        'virtual_nw_x_pixel': 977772589,
                                        'virtual_nw_y_pixel': -1266037392,
                                        'virtual_width': -969812377,
                                        'virtual_height': -1306609654,
                                    },
                            {
                                        'source_monitor': 4963553,
                                        'source_nw_x_pixel': -5604229929864184590,
                                        'source_nw_y_pixel': -750446492183610061,
                                        'source_pixel_width': -4037841317287531905,
                                        'source_pixel_height': -7978965902644340091,
                                        'rotation': -1443219188999654255,
                                        'virtual_nw_x_pixel': -969423046,
                                        'virtual_nw_y_pixel': -765889658,
                                        'virtual_width': -951478980,
                                        'virtual_height': -1507312634,
                                    },
                            {
                                        'source_monitor': 1428886,
                                        'source_nw_x_pixel': -3733320010447628896,
                                        'source_nw_y_pixel': -2188815100100694294,
                                        'source_pixel_width': -3618479782472091062,
                                        'source_pixel_height': -572186757758951741,
                                        'rotation': -4709779683776324134,
                                        'virtual_nw_x_pixel': 1301922023,
                                        'virtual_nw_y_pixel': 197881340,
                                        'virtual_width': -1751901596,
                                        'virtual_height': 1242711089,
                                    },
                            {
                                        'source_monitor': 6724766,
                                        'source_nw_x_pixel': -8518798118966022848,
                                        'source_nw_y_pixel': -7755848925156055934,
                                        'source_pixel_width': -719226557157688056,
                                        'source_pixel_height': -397170473277421152,
                                        'rotation': -7710494286606105025,
                                        'virtual_nw_x_pixel': -859016993,
                                        'virtual_nw_y_pixel': 1820602528,
                                        'virtual_width': -76084207,
                                        'virtual_height': -397469649,
                                    },
                            {
                                        'source_monitor': 3321673,
                                        'source_nw_x_pixel': -7898234754795577095,
                                        'source_nw_y_pixel': -6080730788199915378,
                                        'source_pixel_width': -2244887690286865805,
                                        'source_pixel_height': -4696326695511981555,
                                        'rotation': -4235193501166274484,
                                        'virtual_nw_x_pixel': -1866246101,
                                        'virtual_nw_y_pixel': -1128391673,
                                        'virtual_width': 1996444756,
                                        'virtual_height': 836504142,
                                    },
                            {
                                        'source_monitor': 1316208,
                                        'source_nw_x_pixel': -6904830899379267540,
                                        'source_nw_y_pixel': -8771127088179019190,
                                        'source_pixel_width': -8453755344755870174,
                                        'source_pixel_height': -8088543993896358508,
                                        'rotation': -8307574916419207677,
                                        'virtual_nw_x_pixel': -1287073693,
                                        'virtual_nw_y_pixel': 1662080488,
                                        'virtual_width': 1798656344,
                                        'virtual_height': -904251776,
                                    },
                            {
                                        'source_monitor': 6570978,
                                        'source_nw_x_pixel': -2257513857422944637,
                                        'source_nw_y_pixel': -7663795749259431541,
                                        'source_pixel_width': -7105979963713435518,
                                        'source_pixel_height': -2920624792682850398,
                                        'rotation': -1968608536549623684,
                                        'virtual_nw_x_pixel': 290006373,
                                        'virtual_nw_y_pixel': -1861221359,
                                        'virtual_width': 526148299,
                                        'virtual_height': 557819834,
                                    },
                            {
                                        'source_monitor': 5800788,
                                        'source_nw_x_pixel': -8786876140862765008,
                                        'source_nw_y_pixel': -3183018325304821825,
                                        'source_pixel_width': -6353543652093518490,
                                        'source_pixel_height': -2382953555007001402,
                                        'rotation': -4578545274631059165,
                                        'virtual_nw_x_pixel': -706745688,
                                        'virtual_nw_y_pixel': 939783019,
                                        'virtual_width': -352295643,
                                        'virtual_height': -1987155298,
                                    },
                            {
                                        'source_monitor': 8484304,
                                        'source_nw_x_pixel': -5898157533193836303,
                                        'source_nw_y_pixel': -7407242614414827155,
                                        'source_pixel_width': -1278342507693254268,
                                        'source_pixel_height': -1873135624892134996,
                                        'rotation': -5149954371895813021,
                                        'virtual_nw_x_pixel': -1353456475,
                                        'virtual_nw_y_pixel': 304629881,
                                        'virtual_width': -335095192,
                                        'virtual_height': -495332762,
                                    },
                            {
                                        'source_monitor': -371338,
                                        'source_nw_x_pixel': -703725404399330103,
                                        'source_nw_y_pixel': -612477276358458596,
                                        'source_pixel_width': -7806550000041759151,
                                        'source_pixel_height': -1230365016672170152,
                                        'rotation': -2572073899767702276,
                                        'virtual_nw_x_pixel': 1084034900,
                                        'virtual_nw_y_pixel': -1413330973,
                                        'virtual_width': -1866203360,
                                        'virtual_height': -1793844071,
                                    },
                        ],
                },
                {
                    'description': '˄ɹ«\u03803ɐûɅǅƽʺӀşāƢВµӅǗʯÑ)υʸǁεϷ˄¿т',
                    'monitors': [
                            {
                                        'identifier': 4557516,
                                        'width': -632289872009970553,
                                        'height': 3580654787993189711,
                                    },
                            {
                                        'identifier': 6497809,
                                        'width': 4256300643394458399,
                                        'height': -4380202297525626211,
                                    },
                            {
                                        'identifier': 8627385,
                                        'width': 1001173261915262013,
                                        'height': 7741427150694913012,
                                    },
                            {
                                        'identifier': 558581,
                                        'width': 5793238663823437023,
                                        'height': -4684021805559368130,
                                    },
                            {
                                        'identifier': 7005524,
                                        'width': -2811111266039130894,
                                        'height': 4843617805657235086,
                                    },
                            {
                                        'identifier': 2361934,
                                        'width': 742962194988552805,
                                        'height': -4439961463276779144,
                                    },
                            {
                                        'identifier': 9766833,
                                        'width': -9193362605847202193,
                                        'height': 7213501051319956821,
                                    },
                            {
                                        'identifier': 2050536,
                                        'width': 7895374648094755958,
                                        'height': -8541913388920600875,
                                    },
                            {
                                        'identifier': 6845741,
                                        'width': -3166772589515763611,
                                        'height': -8930085512613333246,
                                    },
                            {
                                        'identifier': 1563787,
                                        'width': 8277852221330899065,
                                        'height': 5945557367977148273,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9724706,
                                        'source_nw_x_pixel': -5696744838783822819,
                                        'source_nw_y_pixel': -7041098591622773813,
                                        'source_pixel_width': -4131672862978280694,
                                        'source_pixel_height': -6465638699929058781,
                                        'rotation': -6003661340878342626,
                                        'virtual_nw_x_pixel': 1709547761,
                                        'virtual_nw_y_pixel': 1111695623,
                                        'virtual_width': 1098418279,
                                        'virtual_height': 1385416390,
                                    },
                            {
                                        'source_monitor': 2908415,
                                        'source_nw_x_pixel': -2708490462504794578,
                                        'source_nw_y_pixel': -3525764826385360857,
                                        'source_pixel_width': -793341121619526422,
                                        'source_pixel_height': -4457375126938534159,
                                        'rotation': -8170217105734835143,
                                        'virtual_nw_x_pixel': -832541293,
                                        'virtual_nw_y_pixel': 1236364168,
                                        'virtual_width': 875949568,
                                        'virtual_height': 238463339,
                                    },
                            {
                                        'source_monitor': 3702504,
                                        'source_nw_x_pixel': -7683010910310795874,
                                        'source_nw_y_pixel': -7045808757520919058,
                                        'source_pixel_width': -3186598594009187749,
                                        'source_pixel_height': -6718262371554017934,
                                        'rotation': -6676796420116114612,
                                        'virtual_nw_x_pixel': 616645451,
                                        'virtual_nw_y_pixel': -722682177,
                                        'virtual_width': -31514200,
                                        'virtual_height': -744847967,
                                    },
                            {
                                        'source_monitor': 1262233,
                                        'source_nw_x_pixel': -752782775399178059,
                                        'source_nw_y_pixel': -5942469604333344842,
                                        'source_pixel_width': -4318301112201459766,
                                        'source_pixel_height': -5990464899871543878,
                                        'rotation': -3242529620365618570,
                                        'virtual_nw_x_pixel': 1842178727,
                                        'virtual_nw_y_pixel': -1141632192,
                                        'virtual_width': 1159102573,
                                        'virtual_height': -978130293,
                                    },
                            {
                                        'source_monitor': 5100270,
                                        'source_nw_x_pixel': -3233241927538132858,
                                        'source_nw_y_pixel': -6630122715812369919,
                                        'source_pixel_width': -9131922644171928665,
                                        'source_pixel_height': -5689749210521306816,
                                        'rotation': -8495763643837518084,
                                        'virtual_nw_x_pixel': -724832262,
                                        'virtual_nw_y_pixel': -1197619156,
                                        'virtual_width': 886146765,
                                        'virtual_height': -1104738208,
                                    },
                            {
                                        'source_monitor': 2973701,
                                        'source_nw_x_pixel': -5245513789456832347,
                                        'source_nw_y_pixel': -403363602500116183,
                                        'source_pixel_width': -4957123008300503341,
                                        'source_pixel_height': -6220643316983707706,
                                        'rotation': -8657618194808144284,
                                        'virtual_nw_x_pixel': 366050328,
                                        'virtual_nw_y_pixel': 1358576624,
                                        'virtual_width': 768110819,
                                        'virtual_height': 1264988647,
                                    },
                            {
                                        'source_monitor': 1427697,
                                        'source_nw_x_pixel': -6164394083678006027,
                                        'source_nw_y_pixel': -562794306117621380,
                                        'source_pixel_width': -5896501165488084894,
                                        'source_pixel_height': -1751594480114319175,
                                        'rotation': -5605914165468505877,
                                        'virtual_nw_x_pixel': -944139653,
                                        'virtual_nw_y_pixel': -781827827,
                                        'virtual_width': -207625585,
                                        'virtual_height': 1811241071,
                                    },
                            {
                                        'source_monitor': 4136192,
                                        'source_nw_x_pixel': -8362606991583743812,
                                        'source_nw_y_pixel': -5404221007440354898,
                                        'source_pixel_width': -3536929560387311601,
                                        'source_pixel_height': -3508625975681812055,
                                        'rotation': -6385631910695626918,
                                        'virtual_nw_x_pixel': -100832369,
                                        'virtual_nw_y_pixel': 1005012267,
                                        'virtual_width': 299393680,
                                        'virtual_height': 341353467,
                                    },
                            {
                                        'source_monitor': -198330,
                                        'source_nw_x_pixel': -8510614143633630868,
                                        'source_nw_y_pixel': -3878093199530259348,
                                        'source_pixel_width': -1171360603220064193,
                                        'source_pixel_height': -5278796089375371605,
                                        'rotation': -2427901641901948603,
                                        'virtual_nw_x_pixel': 1098263208,
                                        'virtual_nw_y_pixel': 254597213,
                                        'virtual_width': 957546462,
                                        'virtual_height': 1107808610,
                                    },
                            {
                                        'source_monitor': 4285778,
                                        'source_nw_x_pixel': -6078571040637069918,
                                        'source_nw_y_pixel': -5711902732530255987,
                                        'source_pixel_width': -7973070396034682738,
                                        'source_pixel_height': -2263214516201909807,
                                        'rotation': -3182463981136586769,
                                        'virtual_nw_x_pixel': 1614230648,
                                        'virtual_nw_y_pixel': 1088703352,
                                        'virtual_width': -1944934126,
                                        'virtual_height': 325654569,
                                    },
                        ],
                },
                {
                    'description': 'ĒȝΆǡəĎӂƀn0\x9dʟĄϧ˴ҿʇǲҬŤĨԮʿНǍĦžСЧЫ',
                    'monitors': [
                            {
                                        'identifier': 2462661,
                                        'width': -3294628426419294651,
                                        'height': 589975827168676552,
                                    },
                            {
                                        'identifier': -305848,
                                        'width': 4425109730371906755,
                                        'height': -5545320412114583290,
                                    },
                            {
                                        'identifier': 6968702,
                                        'width': -5484397240144797927,
                                        'height': 2771890634742836242,
                                    },
                            {
                                        'identifier': 9589230,
                                        'width': -1573281304987214796,
                                        'height': -8795671469695735501,
                                    },
                            {
                                        'identifier': 8741313,
                                        'width': 3722921652374254727,
                                        'height': 7739960037260452569,
                                    },
                            {
                                        'identifier': 3732050,
                                        'width': 2952769014095309357,
                                        'height': -8123820891769329139,
                                    },
                            {
                                        'identifier': 5799674,
                                        'width': 7479764525068712066,
                                        'height': 229676301244738194,
                                    },
                            {
                                        'identifier': 208096,
                                        'width': -5672370058038866136,
                                        'height': -7205995433817879308,
                                    },
                            {
                                        'identifier': -449077,
                                        'width': -5046170030569968001,
                                        'height': 7903779562829262089,
                                    },
                            {
                                        'identifier': 3222519,
                                        'width': 8567224435545475610,
                                        'height': 3020404074144139410,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4152039,
                                        'source_nw_x_pixel': -8638348614477062103,
                                        'source_nw_y_pixel': -5794217414753708917,
                                        'source_pixel_width': -3168736265499905145,
                                        'source_pixel_height': -4516242440446237448,
                                        'rotation': -3026699674907936749,
                                        'virtual_nw_x_pixel': 1730949848,
                                        'virtual_nw_y_pixel': 18202606,
                                        'virtual_width': 1495986735,
                                        'virtual_height': -971777860,
                                    },
                            {
                                        'source_monitor': 8959359,
                                        'source_nw_x_pixel': -1801504034028472032,
                                        'source_nw_y_pixel': -6043195212938529892,
                                        'source_pixel_width': -8154745856223772782,
                                        'source_pixel_height': -4479233212229313025,
                                        'rotation': -1543191487368665145,
                                        'virtual_nw_x_pixel': -1115984327,
                                        'virtual_nw_y_pixel': -1985085932,
                                        'virtual_width': -1783320231,
                                        'virtual_height': -1509544748,
                                    },
                            {
                                        'source_monitor': 2371756,
                                        'source_nw_x_pixel': -1508152495222197750,
                                        'source_nw_y_pixel': -3543967067585265290,
                                        'source_pixel_width': -2821782585143718556,
                                        'source_pixel_height': -8839688583955450020,
                                        'rotation': -1918219393186088313,
                                        'virtual_nw_x_pixel': 1574644642,
                                        'virtual_nw_y_pixel': 707813786,
                                        'virtual_width': 401952119,
                                        'virtual_height': 845918976,
                                    },
                            {
                                        'source_monitor': 3376094,
                                        'source_nw_x_pixel': -6675858977852837586,
                                        'source_nw_y_pixel': -7552599909698964319,
                                        'source_pixel_width': -7318054027864351503,
                                        'source_pixel_height': -785269209095680196,
                                        'rotation': -103872893677319901,
                                        'virtual_nw_x_pixel': 1874884777,
                                        'virtual_nw_y_pixel': 1993050910,
                                        'virtual_width': 666451533,
                                        'virtual_height': -1778334431,
                                    },
                            {
                                        'source_monitor': 3420353,
                                        'source_nw_x_pixel': -6208273010715239423,
                                        'source_nw_y_pixel': -8835764579370974990,
                                        'source_pixel_width': -4496425692344785439,
                                        'source_pixel_height': -6640054234859988106,
                                        'rotation': -4920320190137202674,
                                        'virtual_nw_x_pixel': 1619602395,
                                        'virtual_nw_y_pixel': -864567987,
                                        'virtual_width': 75688369,
                                        'virtual_height': -430461875,
                                    },
                            {
                                        'source_monitor': 3473073,
                                        'source_nw_x_pixel': -4649826196031990883,
                                        'source_nw_y_pixel': -707841807813368692,
                                        'source_pixel_width': -6722800217275937882,
                                        'source_pixel_height': -7858042845903989974,
                                        'rotation': -2487897501655776891,
                                        'virtual_nw_x_pixel': 252235212,
                                        'virtual_nw_y_pixel': 1909797245,
                                        'virtual_width': -1547493285,
                                        'virtual_height': 485033589,
                                    },
                            {
                                        'source_monitor': 3389967,
                                        'source_nw_x_pixel': -4145920973737825275,
                                        'source_nw_y_pixel': -1577388479990393165,
                                        'source_pixel_width': -1957237603973309220,
                                        'source_pixel_height': -4757207654278240398,
                                        'rotation': -217179724777727291,
                                        'virtual_nw_x_pixel': 440822651,
                                        'virtual_nw_y_pixel': -1419839686,
                                        'virtual_width': 525607205,
                                        'virtual_height': 695106286,
                                    },
                            {
                                        'source_monitor': -428273,
                                        'source_nw_x_pixel': -4041434258693919060,
                                        'source_nw_y_pixel': -7048637438654156533,
                                        'source_pixel_width': -8367461365198242654,
                                        'source_pixel_height': -7334659562872890007,
                                        'rotation': -1843669628173771536,
                                        'virtual_nw_x_pixel': 1227215525,
                                        'virtual_nw_y_pixel': -1859383096,
                                        'virtual_width': 439610260,
                                        'virtual_height': -1566780215,
                                    },
                            {
                                        'source_monitor': 5976425,
                                        'source_nw_x_pixel': -8023642936014535036,
                                        'source_nw_y_pixel': -6149756824489162097,
                                        'source_pixel_width': -8240369892694652066,
                                        'source_pixel_height': -4677630189699011959,
                                        'rotation': -8487170716513181191,
                                        'virtual_nw_x_pixel': 76621603,
                                        'virtual_nw_y_pixel': 108756919,
                                        'virtual_width': -1261328289,
                                        'virtual_height': -1237513129,
                                    },
                            {
                                        'source_monitor': 2349869,
                                        'source_nw_x_pixel': -9067749617730810268,
                                        'source_nw_y_pixel': -5013060084588557019,
                                        'source_pixel_width': -3060185186471702306,
                                        'source_pixel_height': -2305104259067506752,
                                        'rotation': -2373855994390759601,
                                        'virtual_nw_x_pixel': 508334230,
                                        'virtual_nw_y_pixel': 375466821,
                                        'virtual_width': 983312847,
                                        'virtual_height': -1082453789,
                                    },
                        ],
                },
                {
                    'description': '\x83\x89ÆȳǨˎûϚђŉԙ)δԋғďƁŽĝѥӺÖΫсǁ˗jъ¢Ȍ',
                    'monitors': [
                            {
                                        'identifier': 9662396,
                                        'width': -8002310901397246209,
                                        'height': 3024654813211536893,
                                    },
                            {
                                        'identifier': 3914277,
                                        'width': 360095762134040023,
                                        'height': 331385431286139169,
                                    },
                            {
                                        'identifier': 8326961,
                                        'width': 5782290359957681869,
                                        'height': 4193462483981631673,
                                    },
                            {
                                        'identifier': 3811340,
                                        'width': -4558464137710206594,
                                        'height': 4876244019052583603,
                                    },
                            {
                                        'identifier': 1941573,
                                        'width': -1096613861860380219,
                                        'height': 1569739549870819005,
                                    },
                            {
                                        'identifier': 2945547,
                                        'width': -9104277283799295024,
                                        'height': 486272526909927576,
                                    },
                            {
                                        'identifier': 7039242,
                                        'width': 7008247601946155233,
                                        'height': 15376691306521731,
                                    },
                            {
                                        'identifier': 171485,
                                        'width': 8968639872662000279,
                                        'height': 6789724844619680936,
                                    },
                            {
                                        'identifier': 2124046,
                                        'width': -2467089688683414977,
                                        'height': 6566061842167729669,
                                    },
                            {
                                        'identifier': -635812,
                                        'width': -926183914613574104,
                                        'height': -893156649337246415,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8747455,
                                        'source_nw_x_pixel': -2953459145887491546,
                                        'source_nw_y_pixel': -2483469248988858020,
                                        'source_pixel_width': -7218277883086899171,
                                        'source_pixel_height': -5831225290183406277,
                                        'rotation': -7452313882359354461,
                                        'virtual_nw_x_pixel': 7887976,
                                        'virtual_nw_y_pixel': -1545440411,
                                        'virtual_width': 319261137,
                                        'virtual_height': 981860068,
                                    },
                            {
                                        'source_monitor': 3630730,
                                        'source_nw_x_pixel': -5480875875403369575,
                                        'source_nw_y_pixel': -6173582025781743129,
                                        'source_pixel_width': -3597528972080601297,
                                        'source_pixel_height': -2314051727101018274,
                                        'rotation': -8062272992224058484,
                                        'virtual_nw_x_pixel': 525248391,
                                        'virtual_nw_y_pixel': 622859867,
                                        'virtual_width': 1665808041,
                                        'virtual_height': 551272714,
                                    },
                            {
                                        'source_monitor': 2670772,
                                        'source_nw_x_pixel': -4584138896606459587,
                                        'source_nw_y_pixel': -2368138989641038435,
                                        'source_pixel_width': -2355183100135816731,
                                        'source_pixel_height': -3456016199160818398,
                                        'rotation': -1974540532557981405,
                                        'virtual_nw_x_pixel': -1550853097,
                                        'virtual_nw_y_pixel': -124966302,
                                        'virtual_width': 742147952,
                                        'virtual_height': -1497748657,
                                    },
                            {
                                        'source_monitor': 9394380,
                                        'source_nw_x_pixel': -7037665336773540883,
                                        'source_nw_y_pixel': -3245206844683892162,
                                        'source_pixel_width': -2451336742065767137,
                                        'source_pixel_height': -5983146664566216618,
                                        'rotation': -3204073830979783961,
                                        'virtual_nw_x_pixel': 1333825243,
                                        'virtual_nw_y_pixel': 1163229824,
                                        'virtual_width': 1059371523,
                                        'virtual_height': -1444493938,
                                    },
                            {
                                        'source_monitor': 2058758,
                                        'source_nw_x_pixel': -5572261781587155928,
                                        'source_nw_y_pixel': -7148338430633421933,
                                        'source_pixel_width': -8229523864399233955,
                                        'source_pixel_height': -237031805591149528,
                                        'rotation': -2131993040052757009,
                                        'virtual_nw_x_pixel': 747711677,
                                        'virtual_nw_y_pixel': 674931020,
                                        'virtual_width': -800587763,
                                        'virtual_height': 1229883128,
                                    },
                            {
                                        'source_monitor': 283799,
                                        'source_nw_x_pixel': -257077386889288960,
                                        'source_nw_y_pixel': -9107219718015637970,
                                        'source_pixel_width': -4774644326601296081,
                                        'source_pixel_height': -3756337685243435504,
                                        'rotation': -3316915544177204321,
                                        'virtual_nw_x_pixel': -1663648633,
                                        'virtual_nw_y_pixel': 1707289072,
                                        'virtual_width': 921374083,
                                        'virtual_height': -1733261474,
                                    },
                            {
                                        'source_monitor': 1630127,
                                        'source_nw_x_pixel': -4636879518316038503,
                                        'source_nw_y_pixel': -3270730405271099527,
                                        'source_pixel_width': -739619746054271485,
                                        'source_pixel_height': -4858494435672935242,
                                        'rotation': -4967978385370483517,
                                        'virtual_nw_x_pixel': -1565361004,
                                        'virtual_nw_y_pixel': 1198326521,
                                        'virtual_width': 1420803237,
                                        'virtual_height': 1580799489,
                                    },
                            {
                                        'source_monitor': 5806935,
                                        'source_nw_x_pixel': -5723898186687889125,
                                        'source_nw_y_pixel': -6024647486615726149,
                                        'source_pixel_width': -4700209980702756143,
                                        'source_pixel_height': -4749347287315490778,
                                        'rotation': -5531728043982823388,
                                        'virtual_nw_x_pixel': 632888934,
                                        'virtual_nw_y_pixel': -930060150,
                                        'virtual_width': -649259361,
                                        'virtual_height': 1826495431,
                                    },
                            {
                                        'source_monitor': 7695127,
                                        'source_nw_x_pixel': -6333122188954921451,
                                        'source_nw_y_pixel': -3613807317212913661,
                                        'source_pixel_width': -8042881117983477943,
                                        'source_pixel_height': -3452883170246271162,
                                        'rotation': -3443604306240540376,
                                        'virtual_nw_x_pixel': 1309777953,
                                        'virtual_nw_y_pixel': -811976356,
                                        'virtual_width': -1003125027,
                                        'virtual_height': 998001963,
                                    },
                            {
                                        'source_monitor': 5534939,
                                        'source_nw_x_pixel': -8201946992685280388,
                                        'source_nw_y_pixel': -819370043142457747,
                                        'source_pixel_width': -1398299455012394505,
                                        'source_pixel_height': -914653396897611737,
                                        'rotation': -1722327374989033128,
                                        'virtual_nw_x_pixel': -1629400917,
                                        'virtual_nw_y_pixel': 1294746026,
                                        'virtual_width': -1612503942,
                                        'virtual_height': 981115959,
                                    },
                        ],
                },
                {
                    'description': 'ôԡŶʎʠç˕ϙʾÝґϝć\x8aǰŕщԊʥɺǋΓʩĿłŉɉȰKӠ',
                    'monitors': [
                            {
                                        'identifier': -875731,
                                        'width': 3045437953194483341,
                                        'height': -5711999723661243513,
                                    },
                            {
                                        'identifier': 6773615,
                                        'width': 734967460447206678,
                                        'height': -520544526096346941,
                                    },
                            {
                                        'identifier': 3323174,
                                        'width': -7988166490628055730,
                                        'height': 3495442051899458452,
                                    },
                            {
                                        'identifier': 759816,
                                        'width': 4359266187080611140,
                                        'height': -4345746232602327019,
                                    },
                            {
                                        'identifier': 1842350,
                                        'width': 4299634134937464067,
                                        'height': -5199130037224946961,
                                    },
                            {
                                        'identifier': 9517724,
                                        'width': 8715623206007452217,
                                        'height': -892360669106820226,
                                    },
                            {
                                        'identifier': 827675,
                                        'width': 4756325164843956416,
                                        'height': 6667823776914426646,
                                    },
                            {
                                        'identifier': 6532400,
                                        'width': 5383125221354916306,
                                        'height': -1500769353046650121,
                                    },
                            {
                                        'identifier': 7247663,
                                        'width': -7438785139056296290,
                                        'height': -1331126199197162633,
                                    },
                            {
                                        'identifier': 2193249,
                                        'width': -4209115808415808861,
                                        'height': -7756362634878049746,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5646788,
                                        'source_nw_x_pixel': -8309611510896507175,
                                        'source_nw_y_pixel': -7968141915129804547,
                                        'source_pixel_width': -2157429998907581432,
                                        'source_pixel_height': -6168557763138651160,
                                        'rotation': -2855726084648304679,
                                        'virtual_nw_x_pixel': -509218270,
                                        'virtual_nw_y_pixel': 441526792,
                                        'virtual_width': -1916694371,
                                        'virtual_height': 1548672532,
                                    },
                            {
                                        'source_monitor': 326057,
                                        'source_nw_x_pixel': -5028920934982733843,
                                        'source_nw_y_pixel': -1202205939936932252,
                                        'source_pixel_width': -2265832779798739783,
                                        'source_pixel_height': -7705347636125225605,
                                        'rotation': -5906428852669256723,
                                        'virtual_nw_x_pixel': 613131707,
                                        'virtual_nw_y_pixel': -1751669171,
                                        'virtual_width': -1493833468,
                                        'virtual_height': -1432185280,
                                    },
                            {
                                        'source_monitor': 3377876,
                                        'source_nw_x_pixel': -4084116861767694605,
                                        'source_nw_y_pixel': -5083906213639210603,
                                        'source_pixel_width': -145681979814928265,
                                        'source_pixel_height': -975206830596733170,
                                        'rotation': -3283954447904750303,
                                        'virtual_nw_x_pixel': 1622930245,
                                        'virtual_nw_y_pixel': 1854213289,
                                        'virtual_width': 1031996343,
                                        'virtual_height': 1815842080,
                                    },
                            {
                                        'source_monitor': 5250238,
                                        'source_nw_x_pixel': -6553925031466371193,
                                        'source_nw_y_pixel': -2147557590201597179,
                                        'source_pixel_width': -1591950013832485705,
                                        'source_pixel_height': -6208216144380351810,
                                        'rotation': -4021334249863845892,
                                        'virtual_nw_x_pixel': 766429462,
                                        'virtual_nw_y_pixel': -1291301689,
                                        'virtual_width': 1878793443,
                                        'virtual_height': 190150272,
                                    },
                            {
                                        'source_monitor': 4705756,
                                        'source_nw_x_pixel': -8145952726072791783,
                                        'source_nw_y_pixel': -2434047037759535933,
                                        'source_pixel_width': -4314711834623173900,
                                        'source_pixel_height': -4905918042264031954,
                                        'rotation': -2781364097964868741,
                                        'virtual_nw_x_pixel': -1670052148,
                                        'virtual_nw_y_pixel': 1043343922,
                                        'virtual_width': 216166249,
                                        'virtual_height': 1728209680,
                                    },
                            {
                                        'source_monitor': 9262702,
                                        'source_nw_x_pixel': -8266951280874029445,
                                        'source_nw_y_pixel': -9153190843003874319,
                                        'source_pixel_width': -9126988856620971334,
                                        'source_pixel_height': -7985800684328195597,
                                        'rotation': -2970876693668532932,
                                        'virtual_nw_x_pixel': -88174696,
                                        'virtual_nw_y_pixel': 1067746893,
                                        'virtual_width': -256174656,
                                        'virtual_height': -208662780,
                                    },
                            {
                                        'source_monitor': 498112,
                                        'source_nw_x_pixel': -8591341415130657840,
                                        'source_nw_y_pixel': -4383252576841331985,
                                        'source_pixel_width': -329509608609715095,
                                        'source_pixel_height': -3926780212959935514,
                                        'rotation': -8297576795974884904,
                                        'virtual_nw_x_pixel': -1085178878,
                                        'virtual_nw_y_pixel': 1125177837,
                                        'virtual_width': -717019286,
                                        'virtual_height': 1300085696,
                                    },
                            {
                                        'source_monitor': 5425184,
                                        'source_nw_x_pixel': -5939813080334534978,
                                        'source_nw_y_pixel': -1182695221885536818,
                                        'source_pixel_width': -2413719079196711987,
                                        'source_pixel_height': -440785153232111949,
                                        'rotation': -6043797191129311764,
                                        'virtual_nw_x_pixel': 834005957,
                                        'virtual_nw_y_pixel': -1223769137,
                                        'virtual_width': -1638034151,
                                        'virtual_height': -381862665,
                                    },
                            {
                                        'source_monitor': 5829997,
                                        'source_nw_x_pixel': -6091805939178142300,
                                        'source_nw_y_pixel': -2709758949725774112,
                                        'source_pixel_width': -1062787105561060009,
                                        'source_pixel_height': -398360848271524415,
                                        'rotation': -6430750034254697371,
                                        'virtual_nw_x_pixel': 1153821169,
                                        'virtual_nw_y_pixel': -206746968,
                                        'virtual_width': 745385662,
                                        'virtual_height': 1325812299,
                                    },
                            {
                                        'source_monitor': 1776458,
                                        'source_nw_x_pixel': -6846132674032912521,
                                        'source_nw_y_pixel': -5410899280215129755,
                                        'source_pixel_width': -1970403236821586878,
                                        'source_pixel_height': -8958561796864203581,
                                        'rotation': -3626735248162178671,
                                        'virtual_nw_x_pixel': 1713442482,
                                        'virtual_nw_y_pixel': 1840874298,
                                        'virtual_width': 1061802653,
                                        'virtual_height': -1051028525,
                                    },
                        ],
                },
                {
                    'description': 'ŢĘÖӠѪͽWτcȇ¼ɫԧӫɬԥȿҽщ˻ΰ҇ĽѺíˋ¼ȣҕʠ',
                    'monitors': [
                            {
                                        'identifier': 9493091,
                                        'width': -8797654645919062407,
                                        'height': -3301396151420557040,
                                    },
                            {
                                        'identifier': 7265344,
                                        'width': -1731950245343693147,
                                        'height': -2922182538499909326,
                                    },
                            {
                                        'identifier': 1911686,
                                        'width': 5647326814816280457,
                                        'height': 787108086054318205,
                                    },
                            {
                                        'identifier': 5471261,
                                        'width': -7494541811492880541,
                                        'height': -2048392183525012285,
                                    },
                            {
                                        'identifier': 3751708,
                                        'width': 7078679131594944851,
                                        'height': 1917585644541759394,
                                    },
                            {
                                        'identifier': 1049199,
                                        'width': -4828002780937777105,
                                        'height': -4701763174072944385,
                                    },
                            {
                                        'identifier': 3799336,
                                        'width': 7906763217216064292,
                                        'height': 1344806022326004880,
                                    },
                            {
                                        'identifier': 7399024,
                                        'width': 2289085869296543582,
                                        'height': 1656644028343387835,
                                    },
                            {
                                        'identifier': 5840658,
                                        'width': 2363098383816955457,
                                        'height': -4278671534378826524,
                                    },
                            {
                                        'identifier': 5484614,
                                        'width': 4355069754904867399,
                                        'height': 365230316759774730,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2501782,
                                        'source_nw_x_pixel': -711899761903064798,
                                        'source_nw_y_pixel': -2716156787190580927,
                                        'source_pixel_width': -3789878754485034366,
                                        'source_pixel_height': -163572979317947659,
                                        'rotation': -7906278893977734554,
                                        'virtual_nw_x_pixel': -1680850819,
                                        'virtual_nw_y_pixel': -197605059,
                                        'virtual_width': -658698480,
                                        'virtual_height': -930911204,
                                    },
                            {
                                        'source_monitor': 8531794,
                                        'source_nw_x_pixel': -1411374657570687412,
                                        'source_nw_y_pixel': -5479654994446665161,
                                        'source_pixel_width': -6687400396573421757,
                                        'source_pixel_height': -5138390856572023180,
                                        'rotation': -6259512438507443573,
                                        'virtual_nw_x_pixel': 272849317,
                                        'virtual_nw_y_pixel': -72546813,
                                        'virtual_width': -448365148,
                                        'virtual_height': 1806544925,
                                    },
                            {
                                        'source_monitor': 9287698,
                                        'source_nw_x_pixel': -5417867892607340965,
                                        'source_nw_y_pixel': -1190064124819742180,
                                        'source_pixel_width': -7873242106453034024,
                                        'source_pixel_height': -1058929246787516971,
                                        'rotation': -8768308337461257184,
                                        'virtual_nw_x_pixel': 1260145956,
                                        'virtual_nw_y_pixel': 1637735338,
                                        'virtual_width': 1709902384,
                                        'virtual_height': -146564070,
                                    },
                            {
                                        'source_monitor': 2988737,
                                        'source_nw_x_pixel': -8864428455791632967,
                                        'source_nw_y_pixel': -587242022232257598,
                                        'source_pixel_width': -5994370135460858179,
                                        'source_pixel_height': -8914199071843700823,
                                        'rotation': -8822355482842902188,
                                        'virtual_nw_x_pixel': -659362423,
                                        'virtual_nw_y_pixel': 1021638373,
                                        'virtual_width': -1122040305,
                                        'virtual_height': 1827478974,
                                    },
                            {
                                        'source_monitor': 350232,
                                        'source_nw_x_pixel': -1696772148505539113,
                                        'source_nw_y_pixel': -2172940712894065273,
                                        'source_pixel_width': -1497166841509615559,
                                        'source_pixel_height': -7985232661098301120,
                                        'rotation': -1066715168401142147,
                                        'virtual_nw_x_pixel': -400254696,
                                        'virtual_nw_y_pixel': -158671892,
                                        'virtual_width': 1271882792,
                                        'virtual_height': 1875473635,
                                    },
                            {
                                        'source_monitor': 9852066,
                                        'source_nw_x_pixel': -6121514145702133994,
                                        'source_nw_y_pixel': -1501441211794900663,
                                        'source_pixel_width': -6134798919263203572,
                                        'source_pixel_height': -5157039542387341929,
                                        'rotation': -677220538422276825,
                                        'virtual_nw_x_pixel': -1461528804,
                                        'virtual_nw_y_pixel': 1039694222,
                                        'virtual_width': 1829610085,
                                        'virtual_height': 202873058,
                                    },
                            {
                                        'source_monitor': 8615188,
                                        'source_nw_x_pixel': -6229127281211310619,
                                        'source_nw_y_pixel': -4216084760014373412,
                                        'source_pixel_width': -4018159525685453929,
                                        'source_pixel_height': -1366924831825051091,
                                        'rotation': -5167923577440179832,
                                        'virtual_nw_x_pixel': -163623063,
                                        'virtual_nw_y_pixel': -1012172492,
                                        'virtual_width': 562008222,
                                        'virtual_height': 1982789082,
                                    },
                            {
                                        'source_monitor': 2338686,
                                        'source_nw_x_pixel': -87042695322288179,
                                        'source_nw_y_pixel': -2919498518882899674,
                                        'source_pixel_width': -7753659760755346748,
                                        'source_pixel_height': -916766100243512820,
                                        'rotation': -7944669536646760438,
                                        'virtual_nw_x_pixel': -1220540221,
                                        'virtual_nw_y_pixel': 1040630125,
                                        'virtual_width': 561563180,
                                        'virtual_height': 916565905,
                                    },
                            {
                                        'source_monitor': 7338475,
                                        'source_nw_x_pixel': -8377020055509120946,
                                        'source_nw_y_pixel': -3358082490739469086,
                                        'source_pixel_width': -1714328115627582610,
                                        'source_pixel_height': -1854918706608198209,
                                        'rotation': -983874155336287035,
                                        'virtual_nw_x_pixel': 395078827,
                                        'virtual_nw_y_pixel': -1062091353,
                                        'virtual_width': 811327176,
                                        'virtual_height': -902477230,
                                    },
                            {
                                        'source_monitor': 4907471,
                                        'source_nw_x_pixel': -5099429001275939629,
                                        'source_nw_y_pixel': -8915046761640396201,
                                        'source_pixel_width': -8953612086057668252,
                                        'source_pixel_height': -5661861958013261910,
                                        'rotation': -7728861102014196270,
                                        'virtual_nw_x_pixel': -638773114,
                                        'virtual_nw_y_pixel': 1082992331,
                                        'virtual_width': 1907412363,
                                        'virtual_height': -25339845,
                                    },
                        ],
                },
                {
                    'description': 'ԎĕԖρˀǸ˞ΖɖĨ¥њѰǼƿӢȗѥηȃϘȍȍåϦԅŅΫЄ˦',
                    'monitors': [
                            {
                                        'identifier': 7807068,
                                        'width': -3034081983340925328,
                                        'height': 231711319155041993,
                                    },
                            {
                                        'identifier': 5733392,
                                        'width': 3406619866943965869,
                                        'height': 5311679961496758027,
                                    },
                            {
                                        'identifier': 1297857,
                                        'width': -3937709846283062564,
                                        'height': -8699176215000042181,
                                    },
                            {
                                        'identifier': 9777753,
                                        'width': -4118395853105094481,
                                        'height': 8340535510807097890,
                                    },
                            {
                                        'identifier': 2208608,
                                        'width': 4854074689539149291,
                                        'height': -5832357012794582674,
                                    },
                            {
                                        'identifier': 3843895,
                                        'width': -29330459010145031,
                                        'height': 3353907321679365780,
                                    },
                            {
                                        'identifier': 8170853,
                                        'width': -6328162247449513951,
                                        'height': 1399452757469964740,
                                    },
                            {
                                        'identifier': 343012,
                                        'width': 2995819283935506758,
                                        'height': 414624296124251555,
                                    },
                            {
                                        'identifier': 8723535,
                                        'width': 1387745695709256502,
                                        'height': 454570058546004176,
                                    },
                            {
                                        'identifier': 4434788,
                                        'width': 8270612950515717017,
                                        'height': 3818925050162092608,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2760720,
                                        'source_nw_x_pixel': -1695302572508958289,
                                        'source_nw_y_pixel': -7073080188572742825,
                                        'source_pixel_width': -1701478327112682491,
                                        'source_pixel_height': -1313876715989484019,
                                        'rotation': -5070886837808751827,
                                        'virtual_nw_x_pixel': -1070918471,
                                        'virtual_nw_y_pixel': 1778969095,
                                        'virtual_width': 1232066835,
                                        'virtual_height': -1436522017,
                                    },
                            {
                                        'source_monitor': 1285129,
                                        'source_nw_x_pixel': -5009905229850465379,
                                        'source_nw_y_pixel': -8813579100068126109,
                                        'source_pixel_width': -4783791828523289603,
                                        'source_pixel_height': -2552344683732960109,
                                        'rotation': -9160932207480020123,
                                        'virtual_nw_x_pixel': -143761779,
                                        'virtual_nw_y_pixel': -110480481,
                                        'virtual_width': 922530900,
                                        'virtual_height': 700201746,
                                    },
                            {
                                        'source_monitor': 8634822,
                                        'source_nw_x_pixel': -4808540609463087453,
                                        'source_nw_y_pixel': -5967114568294065398,
                                        'source_pixel_width': -4174914857872707818,
                                        'source_pixel_height': -1885086452479675891,
                                        'rotation': -7604556462842204681,
                                        'virtual_nw_x_pixel': -1719157001,
                                        'virtual_nw_y_pixel': -964995866,
                                        'virtual_width': 1885232537,
                                        'virtual_height': 1123114911,
                                    },
                            {
                                        'source_monitor': 2167529,
                                        'source_nw_x_pixel': -2047953512337638381,
                                        'source_nw_y_pixel': -3205519869833852,
                                        'source_pixel_width': -4553567019033678857,
                                        'source_pixel_height': -607078632091447250,
                                        'rotation': -3806931599230635497,
                                        'virtual_nw_x_pixel': 1088306463,
                                        'virtual_nw_y_pixel': -1660023354,
                                        'virtual_width': -1363992940,
                                        'virtual_height': 1871474436,
                                    },
                            {
                                        'source_monitor': 4612374,
                                        'source_nw_x_pixel': -1969265372508384971,
                                        'source_nw_y_pixel': -4560780353523017029,
                                        'source_pixel_width': -6360078671539487150,
                                        'source_pixel_height': -9007995594974383732,
                                        'rotation': -3079977224885851881,
                                        'virtual_nw_x_pixel': -720382348,
                                        'virtual_nw_y_pixel': -1627226430,
                                        'virtual_width': 1953519474,
                                        'virtual_height': -1748246650,
                                    },
                            {
                                        'source_monitor': 6845663,
                                        'source_nw_x_pixel': -3862142909355277459,
                                        'source_nw_y_pixel': -7412309174083857480,
                                        'source_pixel_width': -7101562423765027015,
                                        'source_pixel_height': -4760119631918824191,
                                        'rotation': -2391960716947311567,
                                        'virtual_nw_x_pixel': 1612910535,
                                        'virtual_nw_y_pixel': -1124924340,
                                        'virtual_width': -1429701213,
                                        'virtual_height': -344924569,
                                    },
                            {
                                        'source_monitor': 7582674,
                                        'source_nw_x_pixel': -4646669353721976777,
                                        'source_nw_y_pixel': -7319121521593761560,
                                        'source_pixel_width': -94051414365363706,
                                        'source_pixel_height': -7565191547698595359,
                                        'rotation': -6945447287553780216,
                                        'virtual_nw_x_pixel': -1949532511,
                                        'virtual_nw_y_pixel': -1056364477,
                                        'virtual_width': -366966465,
                                        'virtual_height': -536224799,
                                    },
                            {
                                        'source_monitor': 4334065,
                                        'source_nw_x_pixel': -1229390971850121956,
                                        'source_nw_y_pixel': -5600752060825270822,
                                        'source_pixel_width': -360419756123822246,
                                        'source_pixel_height': -7829061993481810384,
                                        'rotation': -4045912668164566677,
                                        'virtual_nw_x_pixel': 1617412096,
                                        'virtual_nw_y_pixel': -796183028,
                                        'virtual_width': -1316286628,
                                        'virtual_height': 1382474720,
                                    },
                            {
                                        'source_monitor': -37001,
                                        'source_nw_x_pixel': -4495133022793464119,
                                        'source_nw_y_pixel': -7470242984767292197,
                                        'source_pixel_width': -4019960520658171326,
                                        'source_pixel_height': -5612049035371249739,
                                        'rotation': -4688294423753206236,
                                        'virtual_nw_x_pixel': 811800279,
                                        'virtual_nw_y_pixel': 1235339794,
                                        'virtual_width': -469323689,
                                        'virtual_height': -1398795461,
                                    },
                            {
                                        'source_monitor': 6541590,
                                        'source_nw_x_pixel': -7772263995445063956,
                                        'source_nw_y_pixel': -6988227117876670669,
                                        'source_pixel_width': -4295238344928427727,
                                        'source_pixel_height': -845841453487105381,
                                        'rotation': -2733347845615682445,
                                        'virtual_nw_x_pixel': -721402925,
                                        'virtual_nw_y_pixel': -747606242,
                                        'virtual_width': 1130668878,
                                        'virtual_height': -241264404,
                                    },
                        ],
                },
                {
                    'description': 'ǆēȼǅʨǴú¹Ƌѹϑ,ȘƛƺƛíyȸʱїˏҪåԣзuɦǮȶ',
                    'monitors': [
                            {
                                        'identifier': 3841607,
                                        'width': 4873975612729892897,
                                        'height': -4682280734580589138,
                                    },
                            {
                                        'identifier': 8115300,
                                        'width': -5792372231147617462,
                                        'height': 8571612103358955008,
                                    },
                            {
                                        'identifier': 4216191,
                                        'width': -7612919280270788510,
                                        'height': -1578584591113828706,
                                    },
                            {
                                        'identifier': 4195826,
                                        'width': -7811671231787619982,
                                        'height': 2523221003323762682,
                                    },
                            {
                                        'identifier': 4372980,
                                        'width': -2939030604859855407,
                                        'height': -3067975320900533238,
                                    },
                            {
                                        'identifier': 523570,
                                        'width': -8807809470422200404,
                                        'height': -1490901447509604089,
                                    },
                            {
                                        'identifier': 9667937,
                                        'width': 6277461460150632301,
                                        'height': -1705167643812351373,
                                    },
                            {
                                        'identifier': 6603595,
                                        'width': 1832075221146677703,
                                        'height': 5545466774505594046,
                                    },
                            {
                                        'identifier': 9300556,
                                        'width': 3299183729338302106,
                                        'height': -4870858713260865270,
                                    },
                            {
                                        'identifier': 8192881,
                                        'width': -4858552738487463335,
                                        'height': -7527892156282218050,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2543353,
                                        'source_nw_x_pixel': -7190309714171454188,
                                        'source_nw_y_pixel': -1098723319512464744,
                                        'source_pixel_width': -5258931708738775340,
                                        'source_pixel_height': -2091206242806123900,
                                        'rotation': -9048944759407390919,
                                        'virtual_nw_x_pixel': 1331132227,
                                        'virtual_nw_y_pixel': 1711466462,
                                        'virtual_width': 1898348719,
                                        'virtual_height': -1942937832,
                                    },
                            {
                                        'source_monitor': 6353045,
                                        'source_nw_x_pixel': -3169054898328348847,
                                        'source_nw_y_pixel': -2893787712974483164,
                                        'source_pixel_width': -7444226006050322431,
                                        'source_pixel_height': -2267537985845280836,
                                        'rotation': -3374476904730848815,
                                        'virtual_nw_x_pixel': -634419301,
                                        'virtual_nw_y_pixel': -1025993705,
                                        'virtual_width': 195967188,
                                        'virtual_height': -883395871,
                                    },
                            {
                                        'source_monitor': -612107,
                                        'source_nw_x_pixel': -6991253213619173276,
                                        'source_nw_y_pixel': -7213446442052595416,
                                        'source_pixel_width': -2615053410910810212,
                                        'source_pixel_height': -3219889165976544760,
                                        'rotation': -1913468654736425388,
                                        'virtual_nw_x_pixel': 64930779,
                                        'virtual_nw_y_pixel': 1773128103,
                                        'virtual_width': -544438753,
                                        'virtual_height': -1514350373,
                                    },
                            {
                                        'source_monitor': 5785284,
                                        'source_nw_x_pixel': -2441194607923433760,
                                        'source_nw_y_pixel': -3973752488235874798,
                                        'source_pixel_width': -8356513809807281402,
                                        'source_pixel_height': -3510954191049920933,
                                        'rotation': -5126900919812775223,
                                        'virtual_nw_x_pixel': -623952042,
                                        'virtual_nw_y_pixel': -534824574,
                                        'virtual_width': 670120734,
                                        'virtual_height': 1442637077,
                                    },
                            {
                                        'source_monitor': 9753052,
                                        'source_nw_x_pixel': -7369045718841722137,
                                        'source_nw_y_pixel': -4989186022092644741,
                                        'source_pixel_width': -6276750215176846218,
                                        'source_pixel_height': -153066850089938128,
                                        'rotation': -6865833431554987195,
                                        'virtual_nw_x_pixel': -1853630922,
                                        'virtual_nw_y_pixel': 972960660,
                                        'virtual_width': -410379988,
                                        'virtual_height': -750451352,
                                    },
                            {
                                        'source_monitor': 5319897,
                                        'source_nw_x_pixel': -5086691312468852392,
                                        'source_nw_y_pixel': -6548880884303201530,
                                        'source_pixel_width': -3674675736672011981,
                                        'source_pixel_height': -6594509666900619046,
                                        'rotation': -800999681659870565,
                                        'virtual_nw_x_pixel': -1679452765,
                                        'virtual_nw_y_pixel': -1345796438,
                                        'virtual_width': -838274255,
                                        'virtual_height': -907832611,
                                    },
                            {
                                        'source_monitor': 9431214,
                                        'source_nw_x_pixel': -7954974223975579065,
                                        'source_nw_y_pixel': -5708158035772987944,
                                        'source_pixel_width': -3388179424048625936,
                                        'source_pixel_height': -1694448542122591619,
                                        'rotation': -7042929077024004463,
                                        'virtual_nw_x_pixel': -964906155,
                                        'virtual_nw_y_pixel': -229065002,
                                        'virtual_width': 1274633147,
                                        'virtual_height': 1960018342,
                                    },
                            {
                                        'source_monitor': 9928138,
                                        'source_nw_x_pixel': -6484837320148575451,
                                        'source_nw_y_pixel': -4801781613851049167,
                                        'source_pixel_width': -4710145613563123606,
                                        'source_pixel_height': -8118669332176552959,
                                        'rotation': -1077161359662326368,
                                        'virtual_nw_x_pixel': -1282187828,
                                        'virtual_nw_y_pixel': 1425856222,
                                        'virtual_width': -617980992,
                                        'virtual_height': 987010149,
                                    },
                            {
                                        'source_monitor': 2722599,
                                        'source_nw_x_pixel': -4195517293366634874,
                                        'source_nw_y_pixel': -3249946199838769313,
                                        'source_pixel_width': -5210830686202526467,
                                        'source_pixel_height': -3272466958246992949,
                                        'rotation': -9047859792865768548,
                                        'virtual_nw_x_pixel': 1578447023,
                                        'virtual_nw_y_pixel': 760887186,
                                        'virtual_width': 1178083696,
                                        'virtual_height': 660221515,
                                    },
                            {
                                        'source_monitor': 7340751,
                                        'source_nw_x_pixel': -3881849766595832421,
                                        'source_nw_y_pixel': -7363536636591700649,
                                        'source_pixel_width': -1287003319435976014,
                                        'source_pixel_height': -6140329480278036691,
                                        'rotation': -5943343902268323623,
                                        'virtual_nw_x_pixel': -1589219106,
                                        'virtual_nw_y_pixel': 1914537662,
                                        'virtual_width': -672344741,
                                        'virtual_height': 675123547,
                                    },
                        ],
                },
                {
                    'description': 'ХŀƻϮɪŖЭǕã=ŭӷgϜрұ¿ԒūŰϤҵԞКɰ?\x8aőɖѤ',
                    'monitors': [
                            {
                                        'identifier': 508682,
                                        'width': -7933747778825459469,
                                        'height': 5991321232588122770,
                                    },
                            {
                                        'identifier': 5125330,
                                        'width': 5283037429655411200,
                                        'height': -7757734791838535480,
                                    },
                            {
                                        'identifier': 169559,
                                        'width': -5128388119591236613,
                                        'height': 961529838762450656,
                                    },
                            {
                                        'identifier': 8737062,
                                        'width': -7648581432762701982,
                                        'height': 4836336831646922321,
                                    },
                            {
                                        'identifier': 905126,
                                        'width': -7868312906235995012,
                                        'height': -8680387593510479506,
                                    },
                            {
                                        'identifier': 6672663,
                                        'width': -4478378127701968833,
                                        'height': 5277971772128248859,
                                    },
                            {
                                        'identifier': -448253,
                                        'width': 3734382595378881909,
                                        'height': -6254878637676923482,
                                    },
                            {
                                        'identifier': 9312514,
                                        'width': 8630001255028893957,
                                        'height': -2842852153182675468,
                                    },
                            {
                                        'identifier': 5581202,
                                        'width': 2134037501037621137,
                                        'height': 4164055642272295085,
                                    },
                            {
                                        'identifier': 6318906,
                                        'width': 7232949829394982846,
                                        'height': -3409133219068927226,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 456177,
                                        'source_nw_x_pixel': -374173737357136560,
                                        'source_nw_y_pixel': -7246214605804512001,
                                        'source_pixel_width': -4151955783115047870,
                                        'source_pixel_height': -5951575862847105326,
                                        'rotation': -6856172121653780394,
                                        'virtual_nw_x_pixel': -1173069040,
                                        'virtual_nw_y_pixel': -1060176971,
                                        'virtual_width': -193466778,
                                        'virtual_height': -1794895875,
                                    },
                            {
                                        'source_monitor': 5077043,
                                        'source_nw_x_pixel': -4227315369000225993,
                                        'source_nw_y_pixel': -7766654995192064776,
                                        'source_pixel_width': -3084930194847187187,
                                        'source_pixel_height': -3120327695828897645,
                                        'rotation': -6825567080036512864,
                                        'virtual_nw_x_pixel': 328129093,
                                        'virtual_nw_y_pixel': 1469281004,
                                        'virtual_width': -236739431,
                                        'virtual_height': 7483009,
                                    },
                            {
                                        'source_monitor': -409429,
                                        'source_nw_x_pixel': -539863165205672828,
                                        'source_nw_y_pixel': -8323076227077982503,
                                        'source_pixel_width': -5778209852667547622,
                                        'source_pixel_height': -5144174385175303095,
                                        'rotation': -6742653718678179238,
                                        'virtual_nw_x_pixel': 473548816,
                                        'virtual_nw_y_pixel': 1759327636,
                                        'virtual_width': 1096785533,
                                        'virtual_height': -1450982185,
                                    },
                            {
                                        'source_monitor': 2686342,
                                        'source_nw_x_pixel': -6337396459293625544,
                                        'source_nw_y_pixel': -150130792312469895,
                                        'source_pixel_width': -7534199539434395766,
                                        'source_pixel_height': -6005349927816270266,
                                        'rotation': -7306686725728780402,
                                        'virtual_nw_x_pixel': -1389892228,
                                        'virtual_nw_y_pixel': -1402352153,
                                        'virtual_width': -589244813,
                                        'virtual_height': 1114969946,
                                    },
                            {
                                        'source_monitor': 3877791,
                                        'source_nw_x_pixel': -1001162936175434630,
                                        'source_nw_y_pixel': -5327481851121508570,
                                        'source_pixel_width': -4352498540797442310,
                                        'source_pixel_height': -2685843055522356785,
                                        'rotation': -4887424056356588260,
                                        'virtual_nw_x_pixel': -236009710,
                                        'virtual_nw_y_pixel': 624435367,
                                        'virtual_width': -1037819233,
                                        'virtual_height': -535269929,
                                    },
                            {
                                        'source_monitor': 8580279,
                                        'source_nw_x_pixel': -5447662188817637766,
                                        'source_nw_y_pixel': -2496280981934223056,
                                        'source_pixel_width': -6603776297756025489,
                                        'source_pixel_height': -3316703310220366709,
                                        'rotation': -4302477711522903577,
                                        'virtual_nw_x_pixel': 1184713402,
                                        'virtual_nw_y_pixel': -307527922,
                                        'virtual_width': 1288548770,
                                        'virtual_height': -229047439,
                                    },
                            {
                                        'source_monitor': 873499,
                                        'source_nw_x_pixel': -7430387126398356917,
                                        'source_nw_y_pixel': -4833450990807992782,
                                        'source_pixel_width': -8013926598809045008,
                                        'source_pixel_height': -5521882268761843060,
                                        'rotation': -7999143778322345672,
                                        'virtual_nw_x_pixel': 1552508540,
                                        'virtual_nw_y_pixel': 164345541,
                                        'virtual_width': -322492902,
                                        'virtual_height': -541460611,
                                    },
                            {
                                        'source_monitor': 6378944,
                                        'source_nw_x_pixel': -2271676525068282947,
                                        'source_nw_y_pixel': -2139811581545399301,
                                        'source_pixel_width': -8621059311117584304,
                                        'source_pixel_height': -7467505102687767698,
                                        'rotation': -8326198351206775480,
                                        'virtual_nw_x_pixel': -480728644,
                                        'virtual_nw_y_pixel': -466184132,
                                        'virtual_width': -1395271409,
                                        'virtual_height': 122228729,
                                    },
                            {
                                        'source_monitor': 8698641,
                                        'source_nw_x_pixel': -4345424958190695367,
                                        'source_nw_y_pixel': -336574773387639785,
                                        'source_pixel_width': -6363055225552968553,
                                        'source_pixel_height': -7480639622436815847,
                                        'rotation': -8849067767272908671,
                                        'virtual_nw_x_pixel': 1355198255,
                                        'virtual_nw_y_pixel': -617059740,
                                        'virtual_width': 726859301,
                                        'virtual_height': 1702665495,
                                    },
                            {
                                        'source_monitor': 5310258,
                                        'source_nw_x_pixel': -4844620528641074998,
                                        'source_nw_y_pixel': -5118321833674972384,
                                        'source_pixel_width': -6450450685260564592,
                                        'source_pixel_height': -3332932349372952185,
                                        'rotation': -7545410765369785116,
                                        'virtual_nw_x_pixel': -1226869887,
                                        'virtual_nw_y_pixel': -1013501423,
                                        'virtual_width': -305698090,
                                        'virtual_height': 1488551802,
                                    },
                        ],
                },
                {
                    'description': 'йԠǒŲΛƴНӂ!Ù˵ȫȀƈŪĿԩЁɕ\x94ψԄ˵ҷͷʶВ\x95đă',
                    'monitors': [
                            {
                                        'identifier': 6318090,
                                        'width': -4778047571849469763,
                                        'height': 4282434866531603754,
                                    },
                            {
                                        'identifier': 2119864,
                                        'width': -9126292326775021074,
                                        'height': -1600904620640093023,
                                    },
                            {
                                        'identifier': 3291033,
                                        'width': -6820886243596704164,
                                        'height': -2275573047445075347,
                                    },
                            {
                                        'identifier': 1278270,
                                        'width': 4547224162271068541,
                                        'height': -9140254929931132058,
                                    },
                            {
                                        'identifier': 9088445,
                                        'width': -4946934670651639554,
                                        'height': 5444469790838157913,
                                    },
                            {
                                        'identifier': 1320108,
                                        'width': -7602605634562030346,
                                        'height': 4454923128486968577,
                                    },
                            {
                                        'identifier': 6211638,
                                        'width': -2384845395246233308,
                                        'height': 6107659160670864137,
                                    },
                            {
                                        'identifier': 1323252,
                                        'width': 7267997628120011953,
                                        'height': 8549743478930658486,
                                    },
                            {
                                        'identifier': 879720,
                                        'width': 5281323022941057739,
                                        'height': -2571285350198816461,
                                    },
                            {
                                        'identifier': 8862158,
                                        'width': -6862948008219995439,
                                        'height': -7302064083915076413,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1545558,
                                        'source_nw_x_pixel': -276285672260110837,
                                        'source_nw_y_pixel': -3398763346028433089,
                                        'source_pixel_width': -7616201238896955257,
                                        'source_pixel_height': -3878467637156921022,
                                        'rotation': -2442201711388709045,
                                        'virtual_nw_x_pixel': 1193639824,
                                        'virtual_nw_y_pixel': 355066927,
                                        'virtual_width': 97007215,
                                        'virtual_height': 1975618126,
                                    },
                            {
                                        'source_monitor': 8246754,
                                        'source_nw_x_pixel': -4758410751760778416,
                                        'source_nw_y_pixel': -401924422479545089,
                                        'source_pixel_width': -3810515141379029743,
                                        'source_pixel_height': -8957268815515230447,
                                        'rotation': -3993975165826117187,
                                        'virtual_nw_x_pixel': 1242559557,
                                        'virtual_nw_y_pixel': 968807226,
                                        'virtual_width': 620566928,
                                        'virtual_height': 1713907420,
                                    },
                            {
                                        'source_monitor': 4062490,
                                        'source_nw_x_pixel': -3285204401579094298,
                                        'source_nw_y_pixel': -6661788473179929602,
                                        'source_pixel_width': -7289100539938670981,
                                        'source_pixel_height': -951943367944504200,
                                        'rotation': -7727123568866183425,
                                        'virtual_nw_x_pixel': -1910704420,
                                        'virtual_nw_y_pixel': 988947740,
                                        'virtual_width': -908811377,
                                        'virtual_height': -227919839,
                                    },
                            {
                                        'source_monitor': 9735295,
                                        'source_nw_x_pixel': -5672042974788842344,
                                        'source_nw_y_pixel': -720646269456278533,
                                        'source_pixel_width': -5281704322492167498,
                                        'source_pixel_height': -686945859997005561,
                                        'rotation': -1148791053209670053,
                                        'virtual_nw_x_pixel': -579643994,
                                        'virtual_nw_y_pixel': -1811984953,
                                        'virtual_width': -21051684,
                                        'virtual_height': -232552880,
                                    },
                            {
                                        'source_monitor': 2904555,
                                        'source_nw_x_pixel': -86066035647738859,
                                        'source_nw_y_pixel': -6736394600565134429,
                                        'source_pixel_width': -6553673455333719595,
                                        'source_pixel_height': -6037994551057094353,
                                        'rotation': -690370181814827511,
                                        'virtual_nw_x_pixel': 884505900,
                                        'virtual_nw_y_pixel': -1626871171,
                                        'virtual_width': -1923710866,
                                        'virtual_height': 217192481,
                                    },
                            {
                                        'source_monitor': 5377065,
                                        'source_nw_x_pixel': -4582469230473596185,
                                        'source_nw_y_pixel': -849122276443240093,
                                        'source_pixel_width': -3866699046328849888,
                                        'source_pixel_height': -2792165667598640878,
                                        'rotation': -5716624855917410694,
                                        'virtual_nw_x_pixel': -1366640277,
                                        'virtual_nw_y_pixel': 9418031,
                                        'virtual_width': -1757860627,
                                        'virtual_height': -1027954143,
                                    },
                            {
                                        'source_monitor': 8829196,
                                        'source_nw_x_pixel': -629335368378545518,
                                        'source_nw_y_pixel': -2881108545140841746,
                                        'source_pixel_width': -1398249205407812580,
                                        'source_pixel_height': -341127542390627681,
                                        'rotation': -2960661612174540567,
                                        'virtual_nw_x_pixel': -1218016050,
                                        'virtual_nw_y_pixel': -1177561712,
                                        'virtual_width': -536635113,
                                        'virtual_height': 1988618186,
                                    },
                            {
                                        'source_monitor': 856330,
                                        'source_nw_x_pixel': -7539442671130970308,
                                        'source_nw_y_pixel': -3507005633417781741,
                                        'source_pixel_width': -1713861015195518656,
                                        'source_pixel_height': -1643406372068795415,
                                        'rotation': -4381985372081750418,
                                        'virtual_nw_x_pixel': 459447373,
                                        'virtual_nw_y_pixel': -242279169,
                                        'virtual_width': -788759248,
                                        'virtual_height': 1207815207,
                                    },
                            {
                                        'source_monitor': 5027961,
                                        'source_nw_x_pixel': -6760597780507469947,
                                        'source_nw_y_pixel': -9156255408689618392,
                                        'source_pixel_width': -509092935078770811,
                                        'source_pixel_height': -3407724863389320237,
                                        'rotation': -4168923167522816159,
                                        'virtual_nw_x_pixel': 1450002533,
                                        'virtual_nw_y_pixel': 1023987233,
                                        'virtual_width': -537155405,
                                        'virtual_height': -594363325,
                                    },
                            {
                                        'source_monitor': 7943636,
                                        'source_nw_x_pixel': -1340566558752033545,
                                        'source_nw_y_pixel': -1512984399697306285,
                                        'source_pixel_width': -9030286287447900196,
                                        'source_pixel_height': -5540881411290294741,
                                        'rotation': -4114768741131867199,
                                        'virtual_nw_x_pixel': 712142958,
                                        'virtual_nw_y_pixel': -327246636,
                                        'virtual_width': -1082175714,
                                        'virtual_height': -878001096,
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
                                        'identifier': 5165101,
                                        'width': -62891969460070404,
                                        'height': -7764882106104180094,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -8829285452938145581,
                                        'source_nw_y_pixel': -90570102919337209,
                                        'source_pixel_width': -4112560349106852048,
                                        'source_pixel_height': -4341667361168598613,
                                        'rotation': -2010508347897580792,
                                        'virtual_nw_x_pixel': 618273922,
                                        'virtual_nw_y_pixel': -782450217,
                                        'virtual_width': -1732250453,
                                        'virtual_height': 298509912,
                                    },
                        ],
                },
            ],

        },
    ),
]
