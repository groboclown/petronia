# GENERATED CODE - DO NOT MODIFY
# Created on 2021-02-28T02:46:15.205262+00:00

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
            'identifier': 9818565,
            'width': 6834849310073234430,
            'height': -1070086742094212830,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 7604843,

            'width': -8030655863058368967,

            'height': -7490966717989314852,

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
            'source_monitor': 3857357,
            'source_nw_x_pixel': -6750317893333609779,
            'source_nw_y_pixel': -6109774879564799712,
            'source_pixel_width': -7775166092187211028,
            'source_pixel_height': -8036234344278743157,
            'rotation': -2209600343026890673,
            'virtual_nw_x_pixel': -1320313037,
            'virtual_nw_y_pixel': 1304150185,
            'virtual_width': -478296441,
            'virtual_height': -1939207739,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -9093433457650582177,

            'source_nw_y_pixel': -4032819615923293111,

            'source_pixel_width': -6735235482048186357,

            'source_pixel_height': -1001015092354427924,

            'rotation': -4548851019660280025,

            'virtual_nw_x_pixel': -1016566924,

            'virtual_nw_y_pixel': -1554754473,

            'virtual_width': 1802971648,

            'virtual_height': 1759093787,

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
            'description': 'ӫǶЇӣɣϖDǕӳǊʨΉδǆԧсƺȊҹ0λϼˈ»ǋεҐκϠư',
            'monitors': [
                {
                    'identifier': 9140909,
                    'width': -7253631313663073164,
                    'height': 7009937632029970785,
                },
                {
                    'identifier': 1909347,
                    'width': -9176254014163575969,
                    'height': -6960491679521213565,
                },
                {
                    'identifier': 7800615,
                    'width': -6085745985501650038,
                    'height': 5386291235699965634,
                },
                {
                    'identifier': 2773174,
                    'width': 5341822091735547439,
                    'height': -7567400919434726408,
                },
                {
                    'identifier': 3031695,
                    'width': -1832343609190345208,
                    'height': -9149970672856022625,
                },
                {
                    'identifier': 4211772,
                    'width': -4674947964029197614,
                    'height': -8241608197475246170,
                },
                {
                    'identifier': 1596409,
                    'width': -1849820502175089305,
                    'height': -2968450040254655155,
                },
                {
                    'identifier': 7926916,
                    'width': 5029503328685233595,
                    'height': 5423142621395163766,
                },
                {
                    'identifier': 904943,
                    'width': 150882190444411892,
                    'height': 7696204005838187365,
                },
                {
                    'identifier': 8016774,
                    'width': 408264745120190270,
                    'height': -8943965432982641028,
                },
            ],
            'screen': [
                {
                    'source_monitor': 1248411,
                    'source_nw_x_pixel': -4776947280352930198,
                    'source_nw_y_pixel': -5379670863850298297,
                    'source_pixel_width': -5257763077819760469,
                    'source_pixel_height': -1630487584676456816,
                    'rotation': -9205812028383327113,
                    'virtual_nw_x_pixel': -1845728820,
                    'virtual_nw_y_pixel': 1452330742,
                    'virtual_width': -733976554,
                    'virtual_height': -1914828062,
                },
                {
                    'source_monitor': 3814359,
                    'source_nw_x_pixel': -5135922192841619604,
                    'source_nw_y_pixel': -893203391455345758,
                    'source_pixel_width': -1653328206635603505,
                    'source_pixel_height': -8764281223073767819,
                    'rotation': -9205573001803047779,
                    'virtual_nw_x_pixel': 1724977735,
                    'virtual_nw_y_pixel': 85318122,
                    'virtual_width': 232588696,
                    'virtual_height': -1586375074,
                },
                {
                    'source_monitor': 5731226,
                    'source_nw_x_pixel': -1309132834358016720,
                    'source_nw_y_pixel': -521921923073255566,
                    'source_pixel_width': -8125671032783152178,
                    'source_pixel_height': -1751986352282544199,
                    'rotation': -8071472884455854014,
                    'virtual_nw_x_pixel': 523536919,
                    'virtual_nw_y_pixel': 206401824,
                    'virtual_width': 1782547370,
                    'virtual_height': -61503318,
                },
                {
                    'source_monitor': 6214984,
                    'source_nw_x_pixel': -7132926912342091062,
                    'source_nw_y_pixel': -4254322513506280935,
                    'source_pixel_width': -1127532194036054754,
                    'source_pixel_height': -8791592808757264686,
                    'rotation': -1135888900106075746,
                    'virtual_nw_x_pixel': -1919628742,
                    'virtual_nw_y_pixel': 1342448097,
                    'virtual_width': -1919694755,
                    'virtual_height': -803246180,
                },
                {
                    'source_monitor': 7326180,
                    'source_nw_x_pixel': -5883165274939638093,
                    'source_nw_y_pixel': -7882914482802567994,
                    'source_pixel_width': -817682700580085249,
                    'source_pixel_height': -3233361853465574916,
                    'rotation': -9181754981883174274,
                    'virtual_nw_x_pixel': 577288588,
                    'virtual_nw_y_pixel': -1689253685,
                    'virtual_width': -1846341911,
                    'virtual_height': 250861041,
                },
                {
                    'source_monitor': 5863443,
                    'source_nw_x_pixel': -2073288197844184617,
                    'source_nw_y_pixel': -1623195836519225901,
                    'source_pixel_width': -3866268668722523558,
                    'source_pixel_height': -7045644878563254243,
                    'rotation': -4140136648381597311,
                    'virtual_nw_x_pixel': 1120019294,
                    'virtual_nw_y_pixel': -1776758466,
                    'virtual_width': -900847860,
                    'virtual_height': -1683621020,
                },
                {
                    'source_monitor': 3383169,
                    'source_nw_x_pixel': -1770712783995019909,
                    'source_nw_y_pixel': -4953927234337759191,
                    'source_pixel_width': -1997157869616622514,
                    'source_pixel_height': -5738292060383657446,
                    'rotation': -4481293791784476503,
                    'virtual_nw_x_pixel': -340452395,
                    'virtual_nw_y_pixel': 1782835158,
                    'virtual_width': 187692654,
                    'virtual_height': -1157318086,
                },
                {
                    'source_monitor': 1415029,
                    'source_nw_x_pixel': -297121691241993299,
                    'source_nw_y_pixel': -2531631626242849816,
                    'source_pixel_width': -7977021967113001833,
                    'source_pixel_height': -2398818296777247161,
                    'rotation': -5123778477244156410,
                    'virtual_nw_x_pixel': 89279798,
                    'virtual_nw_y_pixel': -1998584878,
                    'virtual_width': -109175741,
                    'virtual_height': -1024084069,
                },
                {
                    'source_monitor': 2325833,
                    'source_nw_x_pixel': -3152952687733987734,
                    'source_nw_y_pixel': -7194469734749532748,
                    'source_pixel_width': -7895654294104638990,
                    'source_pixel_height': -5366554634004360224,
                    'rotation': -5972652578505180589,
                    'virtual_nw_x_pixel': -325627831,
                    'virtual_nw_y_pixel': -1240310885,
                    'virtual_width': -1341586666,
                    'virtual_height': -645940332,
                },
                {
                    'source_monitor': 975921,
                    'source_nw_x_pixel': -6046293011328252100,
                    'source_nw_y_pixel': -2984962487650795046,
                    'source_pixel_width': -6052231080991776842,
                    'source_pixel_height': -4374516420340140624,
                    'rotation': -5171434538574804498,
                    'virtual_nw_x_pixel': 1691793331,
                    'virtual_nw_y_pixel': -131380627,
                    'virtual_width': -1223440772,
                    'virtual_height': -696897502,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 5986284,
                    'width': 8832488211210448237,
                    'height': -1911775617940684343,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -5968521063446322990,
                    'source_nw_y_pixel': -7137124125616221320,
                    'source_pixel_width': -4339692030091372495,
                    'source_pixel_height': -266956704256263540,
                    'rotation': -8871158912482598254,
                    'virtual_nw_x_pixel': -1597818104,
                    'virtual_nw_y_pixel': -651279957,
                    'virtual_width': -399714314,
                    'virtual_height': -1792480037,
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
            'request_id': 5693962,
            'mapped_screens_by_monitors': [
                {
                    'description': 'ɬƭȒɹҰοҦΆùбҍПŶėǋъoɏўРҰȪŖԍӐƫĿƏԄƽ',
                    'monitors': [
                            {
                                        'identifier': 6459958,
                                        'width': 679138068235835619,
                                        'height': 7914509110854448444,
                                    },
                            {
                                        'identifier': 464132,
                                        'width': -9131579070311418557,
                                        'height': -2209052558381450430,
                                    },
                            {
                                        'identifier': 1667856,
                                        'width': 7573174676123939509,
                                        'height': 4459398787118561102,
                                    },
                            {
                                        'identifier': 1853517,
                                        'width': -6552261258576775828,
                                        'height': 4735871162460312426,
                                    },
                            {
                                        'identifier': 2082788,
                                        'width': -7725448038592995899,
                                        'height': 8826980811465962951,
                                    },
                            {
                                        'identifier': 9581485,
                                        'width': -6632350848360584260,
                                        'height': 4257235395135403704,
                                    },
                            {
                                        'identifier': 1207989,
                                        'width': -3352270572691996199,
                                        'height': 223058976949286738,
                                    },
                            {
                                        'identifier': 7301361,
                                        'width': -4028734952460904235,
                                        'height': 1796551489586115643,
                                    },
                            {
                                        'identifier': 9741655,
                                        'width': -803858142332060253,
                                        'height': 3968257009825150374,
                                    },
                            {
                                        'identifier': 9511177,
                                        'width': 5794873202682942897,
                                        'height': 9135596110433698134,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5156457,
                                        'source_nw_x_pixel': -5521224955727207222,
                                        'source_nw_y_pixel': -8158129791435735695,
                                        'source_pixel_width': -5891241685092331263,
                                        'source_pixel_height': -1661603438877511658,
                                        'rotation': -4974668022269756557,
                                        'virtual_nw_x_pixel': 1261071659,
                                        'virtual_nw_y_pixel': -482953344,
                                        'virtual_width': 1292779683,
                                        'virtual_height': 127150327,
                                    },
                            {
                                        'source_monitor': 2651469,
                                        'source_nw_x_pixel': -9104189917654603012,
                                        'source_nw_y_pixel': -5503966891637335663,
                                        'source_pixel_width': -6253058327557009481,
                                        'source_pixel_height': -8976240494084591680,
                                        'rotation': -5742237876837402211,
                                        'virtual_nw_x_pixel': -92803184,
                                        'virtual_nw_y_pixel': 1365997542,
                                        'virtual_width': -420356171,
                                        'virtual_height': -154444813,
                                    },
                            {
                                        'source_monitor': 3934607,
                                        'source_nw_x_pixel': -38097210041703197,
                                        'source_nw_y_pixel': -5727125814351223419,
                                        'source_pixel_width': -5236576263733160242,
                                        'source_pixel_height': -3160211666509287903,
                                        'rotation': -5528804771962258893,
                                        'virtual_nw_x_pixel': 1657066981,
                                        'virtual_nw_y_pixel': 1197700118,
                                        'virtual_width': -1014101936,
                                        'virtual_height': -238310277,
                                    },
                            {
                                        'source_monitor': 9926797,
                                        'source_nw_x_pixel': -6078325821172319720,
                                        'source_nw_y_pixel': -4119866334945397017,
                                        'source_pixel_width': -2822427923987564350,
                                        'source_pixel_height': -2945433696469919812,
                                        'rotation': -7580324074313958923,
                                        'virtual_nw_x_pixel': 386003364,
                                        'virtual_nw_y_pixel': 1230264943,
                                        'virtual_width': 1470858481,
                                        'virtual_height': 644395171,
                                    },
                            {
                                        'source_monitor': -97540,
                                        'source_nw_x_pixel': -2215445795036513490,
                                        'source_nw_y_pixel': -4584079684634087589,
                                        'source_pixel_width': -6417823052402318678,
                                        'source_pixel_height': -6545023358347209382,
                                        'rotation': -1456849316104725598,
                                        'virtual_nw_x_pixel': 1014283282,
                                        'virtual_nw_y_pixel': -1879901569,
                                        'virtual_width': -772216876,
                                        'virtual_height': -1047620451,
                                    },
                            {
                                        'source_monitor': 3062269,
                                        'source_nw_x_pixel': -1075380458475437666,
                                        'source_nw_y_pixel': -5832861225634869218,
                                        'source_pixel_width': -889268991435135825,
                                        'source_pixel_height': -5679415250632533555,
                                        'rotation': -3657888117690477304,
                                        'virtual_nw_x_pixel': 409471705,
                                        'virtual_nw_y_pixel': -1065421623,
                                        'virtual_width': 693219164,
                                        'virtual_height': -1253903321,
                                    },
                            {
                                        'source_monitor': 4864180,
                                        'source_nw_x_pixel': -8582799217575457835,
                                        'source_nw_y_pixel': -8089931356631192675,
                                        'source_pixel_width': -8068085586789318239,
                                        'source_pixel_height': -835700896239834455,
                                        'rotation': -4984550426089896007,
                                        'virtual_nw_x_pixel': -1329619944,
                                        'virtual_nw_y_pixel': -1188684620,
                                        'virtual_width': 1994378033,
                                        'virtual_height': 374480450,
                                    },
                            {
                                        'source_monitor': -543373,
                                        'source_nw_x_pixel': -6875985617630950068,
                                        'source_nw_y_pixel': -3535055676231960784,
                                        'source_pixel_width': -6812756748303444418,
                                        'source_pixel_height': -1017522896159789755,
                                        'rotation': -2800832312434020951,
                                        'virtual_nw_x_pixel': 753332518,
                                        'virtual_nw_y_pixel': -836675929,
                                        'virtual_width': 273799026,
                                        'virtual_height': -999687039,
                                    },
                            {
                                        'source_monitor': 4186640,
                                        'source_nw_x_pixel': -7611581452875313209,
                                        'source_nw_y_pixel': -8127077798278178693,
                                        'source_pixel_width': -8615271529936790571,
                                        'source_pixel_height': -2026629371565589896,
                                        'rotation': -7903071166137893173,
                                        'virtual_nw_x_pixel': -539191392,
                                        'virtual_nw_y_pixel': -877494869,
                                        'virtual_width': 1792169388,
                                        'virtual_height': 1790505932,
                                    },
                            {
                                        'source_monitor': 8048554,
                                        'source_nw_x_pixel': -6897974648909315768,
                                        'source_nw_y_pixel': -4998218131010248362,
                                        'source_pixel_width': -911912295936270657,
                                        'source_pixel_height': -7393692114740527103,
                                        'rotation': -5135562516409319572,
                                        'virtual_nw_x_pixel': -752265581,
                                        'virtual_nw_y_pixel': -123253117,
                                        'virtual_width': -1201917893,
                                        'virtual_height': -1031513963,
                                    },
                        ],
                },
                {
                    'description': 'ʟЃʃȂb\x84Ē\xa0,ȲєӼċ;Ҍȫ\x96җĀ9ˌȧжԭǡāȇĢɗɫ',
                    'monitors': [
                            {
                                        'identifier': 8891805,
                                        'width': 588505667709979727,
                                        'height': -3014949746131604834,
                                    },
                            {
                                        'identifier': 4013379,
                                        'width': -3753662778422393475,
                                        'height': 4805492814347302450,
                                    },
                            {
                                        'identifier': 5500341,
                                        'width': -5279002165761326999,
                                        'height': 1202646988145131628,
                                    },
                            {
                                        'identifier': -278124,
                                        'width': -9069612067271103806,
                                        'height': -8480444436062544949,
                                    },
                            {
                                        'identifier': 9871148,
                                        'width': -6094550319858502364,
                                        'height': 7967485519596058924,
                                    },
                            {
                                        'identifier': 9358807,
                                        'width': 6151176626758051300,
                                        'height': 4808505710812403483,
                                    },
                            {
                                        'identifier': 803750,
                                        'width': 6895318506969596314,
                                        'height': 5653903799780618979,
                                    },
                            {
                                        'identifier': 7466228,
                                        'width': 6998194248364227289,
                                        'height': 6749642024148076788,
                                    },
                            {
                                        'identifier': 2297706,
                                        'width': 4372471452667710834,
                                        'height': 3435138065071582812,
                                    },
                            {
                                        'identifier': 2338451,
                                        'width': -2704413602011416636,
                                        'height': 5047444973380787294,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3954293,
                                        'source_nw_x_pixel': -5946536438028298363,
                                        'source_nw_y_pixel': -6795642931728380682,
                                        'source_pixel_width': -581189586831975971,
                                        'source_pixel_height': -4172522844651986902,
                                        'rotation': -7239982820603198564,
                                        'virtual_nw_x_pixel': 1842124398,
                                        'virtual_nw_y_pixel': 960019376,
                                        'virtual_width': -1732446343,
                                        'virtual_height': -1965268982,
                                    },
                            {
                                        'source_monitor': 2257453,
                                        'source_nw_x_pixel': -586166942702848460,
                                        'source_nw_y_pixel': -8141345130114560674,
                                        'source_pixel_width': -8160874098261286767,
                                        'source_pixel_height': -3191482855290792527,
                                        'rotation': -7733360356578567470,
                                        'virtual_nw_x_pixel': -758174593,
                                        'virtual_nw_y_pixel': 830954584,
                                        'virtual_width': 222492019,
                                        'virtual_height': 298327745,
                                    },
                            {
                                        'source_monitor': 1680029,
                                        'source_nw_x_pixel': -7937138633302119755,
                                        'source_nw_y_pixel': -4610895225836598438,
                                        'source_pixel_width': -2936162068406976106,
                                        'source_pixel_height': -3525343273032856803,
                                        'rotation': -4999171226882843751,
                                        'virtual_nw_x_pixel': 1314130418,
                                        'virtual_nw_y_pixel': 1308930018,
                                        'virtual_width': -841441235,
                                        'virtual_height': -399522669,
                                    },
                            {
                                        'source_monitor': 4521312,
                                        'source_nw_x_pixel': -5983047171572000289,
                                        'source_nw_y_pixel': -7937519856028721659,
                                        'source_pixel_width': -1431910399434784206,
                                        'source_pixel_height': -7366952859631842018,
                                        'rotation': -3606469983898612690,
                                        'virtual_nw_x_pixel': -16957088,
                                        'virtual_nw_y_pixel': -354358137,
                                        'virtual_width': -13496994,
                                        'virtual_height': -395218501,
                                    },
                            {
                                        'source_monitor': 1227568,
                                        'source_nw_x_pixel': -7657344506239690608,
                                        'source_nw_y_pixel': -5809404932670117843,
                                        'source_pixel_width': -4412784249422453572,
                                        'source_pixel_height': -930601397758848313,
                                        'rotation': -8686247579021773423,
                                        'virtual_nw_x_pixel': 1397898520,
                                        'virtual_nw_y_pixel': 972674926,
                                        'virtual_width': 1133909107,
                                        'virtual_height': -1078353424,
                                    },
                            {
                                        'source_monitor': 237927,
                                        'source_nw_x_pixel': -8546853774432482013,
                                        'source_nw_y_pixel': -9172225552793699075,
                                        'source_pixel_width': -6598323424384662673,
                                        'source_pixel_height': -9068193161168807185,
                                        'rotation': -4559852408563748746,
                                        'virtual_nw_x_pixel': 247224255,
                                        'virtual_nw_y_pixel': -393574933,
                                        'virtual_width': -310194203,
                                        'virtual_height': 1786181281,
                                    },
                            {
                                        'source_monitor': 335803,
                                        'source_nw_x_pixel': -2190833828306578870,
                                        'source_nw_y_pixel': -1807493650465384736,
                                        'source_pixel_width': -6125935857668925634,
                                        'source_pixel_height': -460495668097591079,
                                        'rotation': -8001992594188875653,
                                        'virtual_nw_x_pixel': 1929343685,
                                        'virtual_nw_y_pixel': 1332517951,
                                        'virtual_width': 1009347201,
                                        'virtual_height': -740398259,
                                    },
                            {
                                        'source_monitor': 9899139,
                                        'source_nw_x_pixel': -8757747402313186988,
                                        'source_nw_y_pixel': -831384364287102135,
                                        'source_pixel_width': -395634348964395056,
                                        'source_pixel_height': -2693152444082789961,
                                        'rotation': -8930804135748027913,
                                        'virtual_nw_x_pixel': -1522225802,
                                        'virtual_nw_y_pixel': 1016104937,
                                        'virtual_width': 1438528625,
                                        'virtual_height': 935396301,
                                    },
                            {
                                        'source_monitor': 3332131,
                                        'source_nw_x_pixel': -946363667449546240,
                                        'source_nw_y_pixel': -395637597708679415,
                                        'source_pixel_width': -7222817664155002897,
                                        'source_pixel_height': -6407969941720607853,
                                        'rotation': -9062077244932702499,
                                        'virtual_nw_x_pixel': -621210270,
                                        'virtual_nw_y_pixel': 912225531,
                                        'virtual_width': 1089931320,
                                        'virtual_height': -1389302543,
                                    },
                            {
                                        'source_monitor': 6600675,
                                        'source_nw_x_pixel': -2113505488829950334,
                                        'source_nw_y_pixel': -1407112170667067889,
                                        'source_pixel_width': -766864668853064343,
                                        'source_pixel_height': -8493601792602181984,
                                        'rotation': -5745619394672901991,
                                        'virtual_nw_x_pixel': -996476610,
                                        'virtual_nw_y_pixel': 243844743,
                                        'virtual_width': -1034596370,
                                        'virtual_height': 118166672,
                                    },
                        ],
                },
                {
                    'description': 'ԃвʞԈůħγ',
                    'monitors': [
                            {
                                        'identifier': 2148157,
                                        'width': 3783318769471553464,
                                        'height': 7988616443526692071,
                                    },
                            {
                                        'identifier': -989194,
                                        'width': 1656499923865256747,
                                        'height': 742475640343133786,
                                    },
                            {
                                        'identifier': 8125656,
                                        'width': -553647117086797946,
                                        'height': -8942118889284461693,
                                    },
                            {
                                        'identifier': 4200343,
                                        'width': 425398199187531460,
                                        'height': -8995002254594485658,
                                    },
                            {
                                        'identifier': 4035160,
                                        'width': 3141884443053536723,
                                        'height': 2937634028729735375,
                                    },
                            {
                                        'identifier': 6453686,
                                        'width': 7838902759759466821,
                                        'height': 8798562762218706078,
                                    },
                            {
                                        'identifier': 7962819,
                                        'width': -3470813212065753605,
                                        'height': -6154996073051339077,
                                    },
                            {
                                        'identifier': 2307772,
                                        'width': -6249880300283250245,
                                        'height': -5055029150005830642,
                                    },
                            {
                                        'identifier': 4779839,
                                        'width': -434622993642309448,
                                        'height': -8156846817131724245,
                                    },
                            {
                                        'identifier': 1358512,
                                        'width': -6235605082690184964,
                                        'height': 8885004697972393790,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3426260,
                                        'source_nw_x_pixel': -3995091037598558030,
                                        'source_nw_y_pixel': -113061295825553463,
                                        'source_pixel_width': -7358551832261808085,
                                        'source_pixel_height': -6084652185467522861,
                                        'rotation': -7364155526349714947,
                                        'virtual_nw_x_pixel': 590694149,
                                        'virtual_nw_y_pixel': -907209340,
                                        'virtual_width': 1249390563,
                                        'virtual_height': -1146079352,
                                    },
                            {
                                        'source_monitor': -293347,
                                        'source_nw_x_pixel': -4539551377156281615,
                                        'source_nw_y_pixel': -2546898859953136483,
                                        'source_pixel_width': -6189053405051293118,
                                        'source_pixel_height': -5468226218976451153,
                                        'rotation': -2941146350444812744,
                                        'virtual_nw_x_pixel': 1253453680,
                                        'virtual_nw_y_pixel': 60154423,
                                        'virtual_width': 58025465,
                                        'virtual_height': -885086983,
                                    },
                            {
                                        'source_monitor': 2455640,
                                        'source_nw_x_pixel': -2451973757783905075,
                                        'source_nw_y_pixel': -2486508835976632108,
                                        'source_pixel_width': -200722404474760920,
                                        'source_pixel_height': -7514679177933040005,
                                        'rotation': -2845668546516313585,
                                        'virtual_nw_x_pixel': -1272932546,
                                        'virtual_nw_y_pixel': 919050680,
                                        'virtual_width': 1141401402,
                                        'virtual_height': 915012574,
                                    },
                            {
                                        'source_monitor': 5705085,
                                        'source_nw_x_pixel': -2664983454216100191,
                                        'source_nw_y_pixel': -7646227062684011593,
                                        'source_pixel_width': -6299810925091939588,
                                        'source_pixel_height': -8249487316287403745,
                                        'rotation': -153199494476544221,
                                        'virtual_nw_x_pixel': 1101866656,
                                        'virtual_nw_y_pixel': 1154954008,
                                        'virtual_width': -1358197645,
                                        'virtual_height': 506187376,
                                    },
                            {
                                        'source_monitor': 7518631,
                                        'source_nw_x_pixel': -1267441650790180793,
                                        'source_nw_y_pixel': -8693596877958072882,
                                        'source_pixel_width': -3745816738623296496,
                                        'source_pixel_height': -4351456421109613822,
                                        'rotation': -6475009173636565131,
                                        'virtual_nw_x_pixel': -759312973,
                                        'virtual_nw_y_pixel': 1439202312,
                                        'virtual_width': -1985442973,
                                        'virtual_height': 799171694,
                                    },
                            {
                                        'source_monitor': 4893480,
                                        'source_nw_x_pixel': -7254537401624274970,
                                        'source_nw_y_pixel': -9148957773419234914,
                                        'source_pixel_width': -3992191315918905297,
                                        'source_pixel_height': -909640991060275414,
                                        'rotation': -1017012956035234189,
                                        'virtual_nw_x_pixel': 1556691100,
                                        'virtual_nw_y_pixel': 235089239,
                                        'virtual_width': 1064382563,
                                        'virtual_height': -805357702,
                                    },
                            {
                                        'source_monitor': 5088732,
                                        'source_nw_x_pixel': -3258974398981005374,
                                        'source_nw_y_pixel': -5791954881932214445,
                                        'source_pixel_width': -2954509591811386188,
                                        'source_pixel_height': -114875469726334490,
                                        'rotation': -3491026959216137496,
                                        'virtual_nw_x_pixel': 933617993,
                                        'virtual_nw_y_pixel': -1431540637,
                                        'virtual_width': 1707936139,
                                        'virtual_height': -236869861,
                                    },
                            {
                                        'source_monitor': 4449449,
                                        'source_nw_x_pixel': -1470803580345316239,
                                        'source_nw_y_pixel': -7791928422533779146,
                                        'source_pixel_width': -4906153174112586724,
                                        'source_pixel_height': -5471668108172411707,
                                        'rotation': -2394682542599878822,
                                        'virtual_nw_x_pixel': -94551432,
                                        'virtual_nw_y_pixel': -1981921932,
                                        'virtual_width': -64289449,
                                        'virtual_height': -1070638033,
                                    },
                            {
                                        'source_monitor': 560709,
                                        'source_nw_x_pixel': -194041750283202473,
                                        'source_nw_y_pixel': -4032075497756088876,
                                        'source_pixel_width': -301087132575391062,
                                        'source_pixel_height': -336566213845273137,
                                        'rotation': -5418077794224713117,
                                        'virtual_nw_x_pixel': -516398152,
                                        'virtual_nw_y_pixel': -1554828365,
                                        'virtual_width': -896987190,
                                        'virtual_height': -1687470040,
                                    },
                            {
                                        'source_monitor': 635095,
                                        'source_nw_x_pixel': -4594831959503445493,
                                        'source_nw_y_pixel': -3972060986721442930,
                                        'source_pixel_width': -7345676068281920839,
                                        'source_pixel_height': -8629840061035168374,
                                        'rotation': -7796089508101669749,
                                        'virtual_nw_x_pixel': 75424856,
                                        'virtual_nw_y_pixel': -383173555,
                                        'virtual_width': 1550777842,
                                        'virtual_height': 610894506,
                                    },
                        ],
                },
                {
                    'description': 'ͰӗǬȊȏˈ\x98ǶǈE¼ԇǥůԁΫˣҎлʾ\u03a28ɋȩśѯƙÿĵͼ',
                    'monitors': [
                            {
                                        'identifier': -821173,
                                        'width': 7851191063785762980,
                                        'height': -3530836740001709688,
                                    },
                            {
                                        'identifier': 6241066,
                                        'width': 1918216563180042539,
                                        'height': 4864789336378175655,
                                    },
                            {
                                        'identifier': 346804,
                                        'width': -2575980215952021806,
                                        'height': -8071302315844771132,
                                    },
                            {
                                        'identifier': 9214312,
                                        'width': -35187132522695839,
                                        'height': -739492773505689570,
                                    },
                            {
                                        'identifier': 8418044,
                                        'width': -514611934684655114,
                                        'height': 2484419072962626370,
                                    },
                            {
                                        'identifier': 7546626,
                                        'width': 7637737593734548767,
                                        'height': 1741105906258059656,
                                    },
                            {
                                        'identifier': 4594588,
                                        'width': -2060653000793289720,
                                        'height': -3356027379162193711,
                                    },
                            {
                                        'identifier': 9471926,
                                        'width': -65226895913821785,
                                        'height': -1538685674606513734,
                                    },
                            {
                                        'identifier': 9847201,
                                        'width': 2053892511813245047,
                                        'height': 7949082984523315377,
                                    },
                            {
                                        'identifier': 8578320,
                                        'width': -2432183644710841009,
                                        'height': -3213816609501266254,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6100090,
                                        'source_nw_x_pixel': -7698879381131028949,
                                        'source_nw_y_pixel': -7432945491456591554,
                                        'source_pixel_width': -7991002478126974807,
                                        'source_pixel_height': -8229676642125976853,
                                        'rotation': -649050574582965899,
                                        'virtual_nw_x_pixel': 283653849,
                                        'virtual_nw_y_pixel': -1799754002,
                                        'virtual_width': -196303298,
                                        'virtual_height': -301506905,
                                    },
                            {
                                        'source_monitor': 4177470,
                                        'source_nw_x_pixel': -1621543919123671408,
                                        'source_nw_y_pixel': -7303884901153888941,
                                        'source_pixel_width': -3382557343493899217,
                                        'source_pixel_height': -3552233884994627187,
                                        'rotation': -9041990368134249119,
                                        'virtual_nw_x_pixel': -1981093612,
                                        'virtual_nw_y_pixel': -1665003369,
                                        'virtual_width': -883106487,
                                        'virtual_height': 316158896,
                                    },
                            {
                                        'source_monitor': 3073268,
                                        'source_nw_x_pixel': -5894128595946851506,
                                        'source_nw_y_pixel': -5877082928425773309,
                                        'source_pixel_width': -5602921677055712497,
                                        'source_pixel_height': -4077868471523363586,
                                        'rotation': -1288464658657640392,
                                        'virtual_nw_x_pixel': -306069803,
                                        'virtual_nw_y_pixel': 350111466,
                                        'virtual_width': -373407848,
                                        'virtual_height': 1780620650,
                                    },
                            {
                                        'source_monitor': 5049814,
                                        'source_nw_x_pixel': -7422526246410140080,
                                        'source_nw_y_pixel': -5125938501596319217,
                                        'source_pixel_width': -7690203245210475762,
                                        'source_pixel_height': -9074352633900418806,
                                        'rotation': -684971269120867321,
                                        'virtual_nw_x_pixel': -530580166,
                                        'virtual_nw_y_pixel': -265598160,
                                        'virtual_width': 850170628,
                                        'virtual_height': -1577391789,
                                    },
                            {
                                        'source_monitor': 7274656,
                                        'source_nw_x_pixel': -885990575482332443,
                                        'source_nw_y_pixel': -5585979015876708479,
                                        'source_pixel_width': -6862861044014504617,
                                        'source_pixel_height': -2635024607345064393,
                                        'rotation': -7303186984189761648,
                                        'virtual_nw_x_pixel': 1612247212,
                                        'virtual_nw_y_pixel': -7691144,
                                        'virtual_width': 1998322864,
                                        'virtual_height': 222250141,
                                    },
                            {
                                        'source_monitor': 2261504,
                                        'source_nw_x_pixel': -5589047677849545055,
                                        'source_nw_y_pixel': -7118373865194428044,
                                        'source_pixel_width': -7643543103402903609,
                                        'source_pixel_height': -5249937130196801294,
                                        'rotation': -2475793612151903881,
                                        'virtual_nw_x_pixel': 1597076774,
                                        'virtual_nw_y_pixel': -1655210790,
                                        'virtual_width': 1138151794,
                                        'virtual_height': 1417502403,
                                    },
                            {
                                        'source_monitor': 7102407,
                                        'source_nw_x_pixel': -1012949617059649534,
                                        'source_nw_y_pixel': -915891315266817569,
                                        'source_pixel_width': -3251420973333406169,
                                        'source_pixel_height': -8170587251996993198,
                                        'rotation': -2492814795272494101,
                                        'virtual_nw_x_pixel': -1049842460,
                                        'virtual_nw_y_pixel': 1334635947,
                                        'virtual_width': -1938420632,
                                        'virtual_height': 1067841040,
                                    },
                            {
                                        'source_monitor': 247172,
                                        'source_nw_x_pixel': -7106124473868367091,
                                        'source_nw_y_pixel': -8220101321468826707,
                                        'source_pixel_width': -8994236235120098852,
                                        'source_pixel_height': -2428686901991141719,
                                        'rotation': -2630389282841310633,
                                        'virtual_nw_x_pixel': -637253755,
                                        'virtual_nw_y_pixel': -1494517302,
                                        'virtual_width': 1111147908,
                                        'virtual_height': -229926901,
                                    },
                            {
                                        'source_monitor': 3735612,
                                        'source_nw_x_pixel': -1088058820625476736,
                                        'source_nw_y_pixel': -5287458154260089532,
                                        'source_pixel_width': -597542496854113969,
                                        'source_pixel_height': -4670569545026355315,
                                        'rotation': -2370090458044948280,
                                        'virtual_nw_x_pixel': -132189114,
                                        'virtual_nw_y_pixel': 1924348409,
                                        'virtual_width': -986301671,
                                        'virtual_height': 124677496,
                                    },
                            {
                                        'source_monitor': 7888224,
                                        'source_nw_x_pixel': -3538424151231283466,
                                        'source_nw_y_pixel': -1764317822937206727,
                                        'source_pixel_width': -7822638922987188578,
                                        'source_pixel_height': -2995346474344217293,
                                        'rotation': -391677685254208150,
                                        'virtual_nw_x_pixel': 77430963,
                                        'virtual_nw_y_pixel': 1702033213,
                                        'virtual_width': 1588778575,
                                        'virtual_height': 1776215927,
                                    },
                        ],
                },
                {
                    'description': 'ʔ¡ǸˀǬΎȝʲϩưǔd΄\x94҉үýĳñģΣўԨìϿɷыУęѭ',
                    'monitors': [
                            {
                                        'identifier': 3632313,
                                        'width': -8155771611474900422,
                                        'height': 5347308171517552246,
                                    },
                            {
                                        'identifier': 4403582,
                                        'width': -2187196066447052234,
                                        'height': 4801567874049602674,
                                    },
                            {
                                        'identifier': 1763323,
                                        'width': 3160991256820459304,
                                        'height': -3640151308347932691,
                                    },
                            {
                                        'identifier': 9199953,
                                        'width': -4992325395944839263,
                                        'height': -3822879620721685651,
                                    },
                            {
                                        'identifier': 5433884,
                                        'width': 3326085572281674301,
                                        'height': -8316478985762689643,
                                    },
                            {
                                        'identifier': 4373565,
                                        'width': -2337356878345169368,
                                        'height': 8526242485828981938,
                                    },
                            {
                                        'identifier': 6890991,
                                        'width': -8644309849064803061,
                                        'height': 5269504531363380051,
                                    },
                            {
                                        'identifier': -560970,
                                        'width': 8552246076184764099,
                                        'height': 2515228570262294213,
                                    },
                            {
                                        'identifier': 6710026,
                                        'width': 2090378787769598770,
                                        'height': -4871811382820715687,
                                    },
                            {
                                        'identifier': 3876774,
                                        'width': 8472582210465354208,
                                        'height': -2645275602323308158,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8796924,
                                        'source_nw_x_pixel': -1760072887468684304,
                                        'source_nw_y_pixel': -8307542080412171086,
                                        'source_pixel_width': -5535614436724281670,
                                        'source_pixel_height': -6077566089118365584,
                                        'rotation': -3403110889398498603,
                                        'virtual_nw_x_pixel': -1459802205,
                                        'virtual_nw_y_pixel': -1495134287,
                                        'virtual_width': 1078470065,
                                        'virtual_height': 520955497,
                                    },
                            {
                                        'source_monitor': 3762259,
                                        'source_nw_x_pixel': -3521994182102871997,
                                        'source_nw_y_pixel': -3103458125134592686,
                                        'source_pixel_width': -6577201017022741546,
                                        'source_pixel_height': -7011168858403568864,
                                        'rotation': -5524074013219977584,
                                        'virtual_nw_x_pixel': 44731154,
                                        'virtual_nw_y_pixel': -634323792,
                                        'virtual_width': -745266984,
                                        'virtual_height': 1698794480,
                                    },
                            {
                                        'source_monitor': 1014256,
                                        'source_nw_x_pixel': -3735175450357013597,
                                        'source_nw_y_pixel': -219102418345977058,
                                        'source_pixel_width': -1292982665179156301,
                                        'source_pixel_height': -7619811546006897177,
                                        'rotation': -4336689108653951576,
                                        'virtual_nw_x_pixel': -1637073040,
                                        'virtual_nw_y_pixel': 135842702,
                                        'virtual_width': -322660550,
                                        'virtual_height': -647516613,
                                    },
                            {
                                        'source_monitor': 1317874,
                                        'source_nw_x_pixel': -6610372854136090433,
                                        'source_nw_y_pixel': -9059729723233264211,
                                        'source_pixel_width': -238634578396309314,
                                        'source_pixel_height': -6001445020069817590,
                                        'rotation': -2652297778320764651,
                                        'virtual_nw_x_pixel': 1008988090,
                                        'virtual_nw_y_pixel': -1607529789,
                                        'virtual_width': -1287953178,
                                        'virtual_height': 1801176506,
                                    },
                            {
                                        'source_monitor': 5913122,
                                        'source_nw_x_pixel': -1399621459979541132,
                                        'source_nw_y_pixel': -8500473607064483296,
                                        'source_pixel_width': -1979820278942308329,
                                        'source_pixel_height': -9142475694789734722,
                                        'rotation': -7504792623834379356,
                                        'virtual_nw_x_pixel': 705902765,
                                        'virtual_nw_y_pixel': -754708309,
                                        'virtual_width': -1332878697,
                                        'virtual_height': -1081958760,
                                    },
                            {
                                        'source_monitor': 5072241,
                                        'source_nw_x_pixel': -7380130900016481847,
                                        'source_nw_y_pixel': -6486627924833996148,
                                        'source_pixel_width': -455697061126634430,
                                        'source_pixel_height': -1450732239026570964,
                                        'rotation': -4412051340872406095,
                                        'virtual_nw_x_pixel': -360793023,
                                        'virtual_nw_y_pixel': 151854999,
                                        'virtual_width': -387652622,
                                        'virtual_height': -1840850714,
                                    },
                            {
                                        'source_monitor': 2567248,
                                        'source_nw_x_pixel': -7706171296936241148,
                                        'source_nw_y_pixel': -909880380748839749,
                                        'source_pixel_width': -5190669948853375462,
                                        'source_pixel_height': -566040410069724296,
                                        'rotation': -5020218743919871007,
                                        'virtual_nw_x_pixel': 615318408,
                                        'virtual_nw_y_pixel': 1363584930,
                                        'virtual_width': 62428912,
                                        'virtual_height': 1935028151,
                                    },
                            {
                                        'source_monitor': 7300851,
                                        'source_nw_x_pixel': -6819901288119440339,
                                        'source_nw_y_pixel': -6263719110642575756,
                                        'source_pixel_width': -3259834189945198414,
                                        'source_pixel_height': -1861632952239385763,
                                        'rotation': -8961885711609447931,
                                        'virtual_nw_x_pixel': 1319011961,
                                        'virtual_nw_y_pixel': 1224744781,
                                        'virtual_width': 921367113,
                                        'virtual_height': 1407494825,
                                    },
                            {
                                        'source_monitor': -936335,
                                        'source_nw_x_pixel': -864786769043921358,
                                        'source_nw_y_pixel': -5910795072966422619,
                                        'source_pixel_width': -2961007562420643614,
                                        'source_pixel_height': -7657791118009871854,
                                        'rotation': -3696025707936376460,
                                        'virtual_nw_x_pixel': 1643223666,
                                        'virtual_nw_y_pixel': 1917794159,
                                        'virtual_width': -145252427,
                                        'virtual_height': 476999977,
                                    },
                            {
                                        'source_monitor': 9020668,
                                        'source_nw_x_pixel': -345816275678714841,
                                        'source_nw_y_pixel': -8118327966083750358,
                                        'source_pixel_width': -6057389883426483309,
                                        'source_pixel_height': -467698041277505143,
                                        'rotation': -7969984002536637367,
                                        'virtual_nw_x_pixel': 58999505,
                                        'virtual_nw_y_pixel': 1316464178,
                                        'virtual_width': -1622434097,
                                        'virtual_height': 589992276,
                                    },
                        ],
                },
                {
                    'description': 'ˢΒŃƤͽԚƥӫàԥȑʗԖiƥnԞͶ҄˘ЋͱȧӀȉȭ\x9fȑϱƱ',
                    'monitors': [
                            {
                                        'identifier': 1371805,
                                        'width': -2110214056135233572,
                                        'height': 5941885039613305644,
                                    },
                            {
                                        'identifier': 2941154,
                                        'width': 3279921017251448977,
                                        'height': 4242846351127060755,
                                    },
                            {
                                        'identifier': 8317701,
                                        'width': 7399521683554598189,
                                        'height': 3170066309004302516,
                                    },
                            {
                                        'identifier': 8984246,
                                        'width': -8880473565289983388,
                                        'height': -4122111246106070092,
                                    },
                            {
                                        'identifier': 4818970,
                                        'width': 5184896974395943360,
                                        'height': 5157371384299375652,
                                    },
                            {
                                        'identifier': 7742209,
                                        'width': -8135312497435132429,
                                        'height': -168508022950636297,
                                    },
                            {
                                        'identifier': 3591077,
                                        'width': -2170631486327240621,
                                        'height': -8977770173898206776,
                                    },
                            {
                                        'identifier': 2595091,
                                        'width': -1992938396262770245,
                                        'height': 2663587554837759165,
                                    },
                            {
                                        'identifier': 2104758,
                                        'width': 5740359909177439101,
                                        'height': -5098455178504921920,
                                    },
                            {
                                        'identifier': 8077203,
                                        'width': 1008948218715053865,
                                        'height': -6379014717485457358,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8968671,
                                        'source_nw_x_pixel': -121045853910530110,
                                        'source_nw_y_pixel': -7442144127556619576,
                                        'source_pixel_width': -5988863988301982658,
                                        'source_pixel_height': -4514703780359174946,
                                        'rotation': -5103911861201458864,
                                        'virtual_nw_x_pixel': 822416695,
                                        'virtual_nw_y_pixel': 884034000,
                                        'virtual_width': -950877961,
                                        'virtual_height': 1146596201,
                                    },
                            {
                                        'source_monitor': 5805714,
                                        'source_nw_x_pixel': -4942031302862318626,
                                        'source_nw_y_pixel': -3012499339667627906,
                                        'source_pixel_width': -3312516099106838699,
                                        'source_pixel_height': -4852191337415127285,
                                        'rotation': -5723454517269063397,
                                        'virtual_nw_x_pixel': 1148500751,
                                        'virtual_nw_y_pixel': -154762248,
                                        'virtual_width': 1002201741,
                                        'virtual_height': -723581560,
                                    },
                            {
                                        'source_monitor': 3354963,
                                        'source_nw_x_pixel': -6039031648081215458,
                                        'source_nw_y_pixel': -1475588671240041829,
                                        'source_pixel_width': -383754734360504588,
                                        'source_pixel_height': -7370167523345746225,
                                        'rotation': -6227533124068790391,
                                        'virtual_nw_x_pixel': 1413179600,
                                        'virtual_nw_y_pixel': 1170669943,
                                        'virtual_width': 866204961,
                                        'virtual_height': 1276653029,
                                    },
                            {
                                        'source_monitor': 9699486,
                                        'source_nw_x_pixel': -6583698740516816515,
                                        'source_nw_y_pixel': -2762597620960056531,
                                        'source_pixel_width': -2068700330982572138,
                                        'source_pixel_height': -3428612916041447887,
                                        'rotation': -8703204610206887210,
                                        'virtual_nw_x_pixel': 1673853548,
                                        'virtual_nw_y_pixel': -1301117603,
                                        'virtual_width': 1106592390,
                                        'virtual_height': 1867195649,
                                    },
                            {
                                        'source_monitor': 9634842,
                                        'source_nw_x_pixel': -8114627391152325715,
                                        'source_nw_y_pixel': -2565067217710975607,
                                        'source_pixel_width': -5291158850232906590,
                                        'source_pixel_height': -6805981461972903286,
                                        'rotation': -449639132304784931,
                                        'virtual_nw_x_pixel': 729032748,
                                        'virtual_nw_y_pixel': 722190474,
                                        'virtual_width': -1686688694,
                                        'virtual_height': 131128261,
                                    },
                            {
                                        'source_monitor': 7474141,
                                        'source_nw_x_pixel': -565993190488685838,
                                        'source_nw_y_pixel': -4858968953691579521,
                                        'source_pixel_width': -686050508215794938,
                                        'source_pixel_height': -4321493285669781191,
                                        'rotation': -2909432782307754156,
                                        'virtual_nw_x_pixel': 444533408,
                                        'virtual_nw_y_pixel': -942631414,
                                        'virtual_width': 1831248562,
                                        'virtual_height': 399736252,
                                    },
                            {
                                        'source_monitor': -521834,
                                        'source_nw_x_pixel': -820677410564012376,
                                        'source_nw_y_pixel': -146002081842946061,
                                        'source_pixel_width': -5059803929418139504,
                                        'source_pixel_height': -1620483916856670795,
                                        'rotation': -6674480613724042947,
                                        'virtual_nw_x_pixel': -594797450,
                                        'virtual_nw_y_pixel': 343764897,
                                        'virtual_width': -464173538,
                                        'virtual_height': -1859584810,
                                    },
                            {
                                        'source_monitor': 1966469,
                                        'source_nw_x_pixel': -3912349098135786476,
                                        'source_nw_y_pixel': -2901970068686031160,
                                        'source_pixel_width': -3689028717863321455,
                                        'source_pixel_height': -8492219369233049505,
                                        'rotation': -7650360590383207804,
                                        'virtual_nw_x_pixel': 1787029713,
                                        'virtual_nw_y_pixel': 1981339875,
                                        'virtual_width': -1757889668,
                                        'virtual_height': -1009013487,
                                    },
                            {
                                        'source_monitor': 311923,
                                        'source_nw_x_pixel': -5984326028697867048,
                                        'source_nw_y_pixel': -4028453473650549907,
                                        'source_pixel_width': -7438880239372324281,
                                        'source_pixel_height': -5339134558467471464,
                                        'rotation': -3810714412688386317,
                                        'virtual_nw_x_pixel': -1702913575,
                                        'virtual_nw_y_pixel': 1597376207,
                                        'virtual_width': 1381906393,
                                        'virtual_height': -1347267189,
                                    },
                            {
                                        'source_monitor': 9556252,
                                        'source_nw_x_pixel': -3813363686278025231,
                                        'source_nw_y_pixel': -2990517609807260058,
                                        'source_pixel_width': -2961744735520945027,
                                        'source_pixel_height': -5770774018005671932,
                                        'rotation': -853831144659253658,
                                        'virtual_nw_x_pixel': 283512278,
                                        'virtual_nw_y_pixel': -839582729,
                                        'virtual_width': -1587520250,
                                        'virtual_height': 1018971685,
                                    },
                        ],
                },
                {
                    'description': 'ʍŧ˽\xa0őЙΡԎƬϺø\x83ĐѩÜЋˣɮȿǇλкѿ.Ӈťҁάȱħ',
                    'monitors': [
                            {
                                        'identifier': 4442071,
                                        'width': 6389511043722477397,
                                        'height': -261776206297900629,
                                    },
                            {
                                        'identifier': 2611716,
                                        'width': -7923462308575805610,
                                        'height': -7333990074198744076,
                                    },
                            {
                                        'identifier': 3379674,
                                        'width': 6927120276542873852,
                                        'height': 854484105068804839,
                                    },
                            {
                                        'identifier': -222154,
                                        'width': -4137341070577937742,
                                        'height': -2715634536336845289,
                                    },
                            {
                                        'identifier': -341838,
                                        'width': 515242524782915743,
                                        'height': 2496675783716403460,
                                    },
                            {
                                        'identifier': 9976170,
                                        'width': 5713983828176554915,
                                        'height': -8521462780578944390,
                                    },
                            {
                                        'identifier': 6074903,
                                        'width': 5064743919436232390,
                                        'height': -5705874421084520070,
                                    },
                            {
                                        'identifier': 7990828,
                                        'width': 8325678949543424410,
                                        'height': 3009991106967530290,
                                    },
                            {
                                        'identifier': 3228840,
                                        'width': 6836757172862747540,
                                        'height': 1012471151587788881,
                                    },
                            {
                                        'identifier': -577865,
                                        'width': -6623271756960749842,
                                        'height': 9209405116541135933,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7492994,
                                        'source_nw_x_pixel': -9069879389295858728,
                                        'source_nw_y_pixel': -3586035113834453436,
                                        'source_pixel_width': -8323945281521375173,
                                        'source_pixel_height': -1278775354849711841,
                                        'rotation': -1583400727600492675,
                                        'virtual_nw_x_pixel': 1868995528,
                                        'virtual_nw_y_pixel': 1991299679,
                                        'virtual_width': 1416274699,
                                        'virtual_height': -1011134050,
                                    },
                            {
                                        'source_monitor': 5727199,
                                        'source_nw_x_pixel': -7921416293852964312,
                                        'source_nw_y_pixel': -3530323114558036776,
                                        'source_pixel_width': -9080597518889498825,
                                        'source_pixel_height': -5518873807005158492,
                                        'rotation': -7492326022293415010,
                                        'virtual_nw_x_pixel': -1157425472,
                                        'virtual_nw_y_pixel': -702275140,
                                        'virtual_width': 1125660633,
                                        'virtual_height': 1894384823,
                                    },
                            {
                                        'source_monitor': 8579991,
                                        'source_nw_x_pixel': -6294279178690386765,
                                        'source_nw_y_pixel': -7842804691391472858,
                                        'source_pixel_width': -2563293264760866368,
                                        'source_pixel_height': -8942252828144903886,
                                        'rotation': -7209528224277765917,
                                        'virtual_nw_x_pixel': -733891968,
                                        'virtual_nw_y_pixel': 1770580358,
                                        'virtual_width': -1809631371,
                                        'virtual_height': -289888446,
                                    },
                            {
                                        'source_monitor': 2332869,
                                        'source_nw_x_pixel': -1582358412755922481,
                                        'source_nw_y_pixel': -7398541377791869993,
                                        'source_pixel_width': -5827539164784343935,
                                        'source_pixel_height': -654684105670031956,
                                        'rotation': -2144723895204317364,
                                        'virtual_nw_x_pixel': -1528258254,
                                        'virtual_nw_y_pixel': -1800555868,
                                        'virtual_width': -603312697,
                                        'virtual_height': 747553368,
                                    },
                            {
                                        'source_monitor': 4872357,
                                        'source_nw_x_pixel': -502138559768593415,
                                        'source_nw_y_pixel': -3811250698841877082,
                                        'source_pixel_width': -3119752096960523489,
                                        'source_pixel_height': -9169787936619622165,
                                        'rotation': -2945800670250586388,
                                        'virtual_nw_x_pixel': 984617083,
                                        'virtual_nw_y_pixel': -1994879505,
                                        'virtual_width': -789478078,
                                        'virtual_height': -842326348,
                                    },
                            {
                                        'source_monitor': 253576,
                                        'source_nw_x_pixel': -3564534032491907286,
                                        'source_nw_y_pixel': -9191105272088384741,
                                        'source_pixel_width': -511887461599539591,
                                        'source_pixel_height': -1349425512273488434,
                                        'rotation': -7634422748371400222,
                                        'virtual_nw_x_pixel': -579844230,
                                        'virtual_nw_y_pixel': -68553584,
                                        'virtual_width': -1807640946,
                                        'virtual_height': -13342523,
                                    },
                            {
                                        'source_monitor': 9461430,
                                        'source_nw_x_pixel': -1777471718388123131,
                                        'source_nw_y_pixel': -8691938154513921821,
                                        'source_pixel_width': -708314621950574739,
                                        'source_pixel_height': -6586314908137533855,
                                        'rotation': -2841438126466797504,
                                        'virtual_nw_x_pixel': -683356615,
                                        'virtual_nw_y_pixel': -167730368,
                                        'virtual_width': 1829094816,
                                        'virtual_height': -1535945974,
                                    },
                            {
                                        'source_monitor': 8503068,
                                        'source_nw_x_pixel': -4648412300034975894,
                                        'source_nw_y_pixel': -1759308993346959262,
                                        'source_pixel_width': -1118383636742976766,
                                        'source_pixel_height': -7091166933017830195,
                                        'rotation': -8667181615478160222,
                                        'virtual_nw_x_pixel': 201979660,
                                        'virtual_nw_y_pixel': 827063922,
                                        'virtual_width': -1665777628,
                                        'virtual_height': 36225030,
                                    },
                            {
                                        'source_monitor': 5914789,
                                        'source_nw_x_pixel': -4855178531603945047,
                                        'source_nw_y_pixel': -2962864276919571344,
                                        'source_pixel_width': -3163170336238009825,
                                        'source_pixel_height': -7793082180634572216,
                                        'rotation': -2685837064570194458,
                                        'virtual_nw_x_pixel': 361939797,
                                        'virtual_nw_y_pixel': 1181141006,
                                        'virtual_width': 75106938,
                                        'virtual_height': 1572286689,
                                    },
                            {
                                        'source_monitor': 8034874,
                                        'source_nw_x_pixel': -8800034388452727242,
                                        'source_nw_y_pixel': -3056005909904762404,
                                        'source_pixel_width': -6583213366852131489,
                                        'source_pixel_height': -2099260625272035827,
                                        'rotation': -571745493643264665,
                                        'virtual_nw_x_pixel': -1518711504,
                                        'virtual_nw_y_pixel': -1657567097,
                                        'virtual_width': 1252483634,
                                        'virtual_height': 454366431,
                                    },
                        ],
                },
                {
                    'description': '˴ʏˑԧɫɋ\x99ɴ\x89ѽϰϑʶ˗ȫ\x8aͻĬũѺʺOǀ˖чCʌìõ¢',
                    'monitors': [
                            {
                                        'identifier': -41094,
                                        'width': -3395838446888987970,
                                        'height': 6257973394267004751,
                                    },
                            {
                                        'identifier': 2867325,
                                        'width': -1592999682623102036,
                                        'height': 4294947328121915041,
                                    },
                            {
                                        'identifier': 7493571,
                                        'width': 7079418251041745838,
                                        'height': -4958179100926983287,
                                    },
                            {
                                        'identifier': 9566150,
                                        'width': -370323907279752390,
                                        'height': 5694823336892154266,
                                    },
                            {
                                        'identifier': 5778075,
                                        'width': -2715577383050134563,
                                        'height': -1490880319121550037,
                                    },
                            {
                                        'identifier': 5962106,
                                        'width': -1415531467223977523,
                                        'height': -5361280494997827609,
                                    },
                            {
                                        'identifier': 2201643,
                                        'width': 1678432212548993997,
                                        'height': 7230871996535314247,
                                    },
                            {
                                        'identifier': 9462953,
                                        'width': -7297050894930105740,
                                        'height': -3180137844693758127,
                                    },
                            {
                                        'identifier': 6921399,
                                        'width': -8066995251679302026,
                                        'height': 5114873599189496521,
                                    },
                            {
                                        'identifier': 5308582,
                                        'width': -1038267366267748252,
                                        'height': -4592868337910739249,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8849635,
                                        'source_nw_x_pixel': -4357844314891178582,
                                        'source_nw_y_pixel': -3635779032156768271,
                                        'source_pixel_width': -7182605120806632366,
                                        'source_pixel_height': -6089809836199518829,
                                        'rotation': -8928442878222085275,
                                        'virtual_nw_x_pixel': 696762737,
                                        'virtual_nw_y_pixel': 1164501944,
                                        'virtual_width': -782236908,
                                        'virtual_height': -1743137495,
                                    },
                            {
                                        'source_monitor': 64080,
                                        'source_nw_x_pixel': -7912013377446745460,
                                        'source_nw_y_pixel': -9103146721169824324,
                                        'source_pixel_width': -3069400230457892279,
                                        'source_pixel_height': -2325296025121024446,
                                        'rotation': -3431376405670231155,
                                        'virtual_nw_x_pixel': -21121539,
                                        'virtual_nw_y_pixel': -1402366102,
                                        'virtual_width': 350051092,
                                        'virtual_height': 1585559426,
                                    },
                            {
                                        'source_monitor': 9089310,
                                        'source_nw_x_pixel': -517169605251696895,
                                        'source_nw_y_pixel': -3064312436712148894,
                                        'source_pixel_width': -5082360665769904579,
                                        'source_pixel_height': -7601277926524970451,
                                        'rotation': -6061358627566750808,
                                        'virtual_nw_x_pixel': 1826051227,
                                        'virtual_nw_y_pixel': 1355811281,
                                        'virtual_width': 1087892220,
                                        'virtual_height': -116692821,
                                    },
                            {
                                        'source_monitor': 2683270,
                                        'source_nw_x_pixel': -1105397874703217655,
                                        'source_nw_y_pixel': -8402703902354622550,
                                        'source_pixel_width': -5851812553414702734,
                                        'source_pixel_height': -492476768714840972,
                                        'rotation': -8239993501144829546,
                                        'virtual_nw_x_pixel': 1960784802,
                                        'virtual_nw_y_pixel': -1803802926,
                                        'virtual_width': 1412551254,
                                        'virtual_height': -1551171036,
                                    },
                            {
                                        'source_monitor': -375493,
                                        'source_nw_x_pixel': -6460324990595224458,
                                        'source_nw_y_pixel': -3886826433951908101,
                                        'source_pixel_width': -3197438389469443913,
                                        'source_pixel_height': -7008467220163389129,
                                        'rotation': -220435238437666300,
                                        'virtual_nw_x_pixel': -654963273,
                                        'virtual_nw_y_pixel': 705151573,
                                        'virtual_width': -439543264,
                                        'virtual_height': 697264230,
                                    },
                            {
                                        'source_monitor': 7540238,
                                        'source_nw_x_pixel': -208330456771138740,
                                        'source_nw_y_pixel': -6932613783803327120,
                                        'source_pixel_width': -1464093204706517805,
                                        'source_pixel_height': -2054077251848874296,
                                        'rotation': -3993257049206669765,
                                        'virtual_nw_x_pixel': 1898502132,
                                        'virtual_nw_y_pixel': -960138553,
                                        'virtual_width': -1266078212,
                                        'virtual_height': 859277740,
                                    },
                            {
                                        'source_monitor': 1252037,
                                        'source_nw_x_pixel': -261028371195548537,
                                        'source_nw_y_pixel': -7739333089911717266,
                                        'source_pixel_width': -5246194603065922350,
                                        'source_pixel_height': -4891953011421363448,
                                        'rotation': -5700553816440436040,
                                        'virtual_nw_x_pixel': 425258760,
                                        'virtual_nw_y_pixel': -766266717,
                                        'virtual_width': 1573408859,
                                        'virtual_height': -429559177,
                                    },
                            {
                                        'source_monitor': 5007872,
                                        'source_nw_x_pixel': -8840521044858933282,
                                        'source_nw_y_pixel': -8010781234349849449,
                                        'source_pixel_width': -5034959268107420332,
                                        'source_pixel_height': -5895466398582382530,
                                        'rotation': -8276919957741937197,
                                        'virtual_nw_x_pixel': 1880134227,
                                        'virtual_nw_y_pixel': 1856602210,
                                        'virtual_width': 992309109,
                                        'virtual_height': 893084596,
                                    },
                            {
                                        'source_monitor': 1034523,
                                        'source_nw_x_pixel': -8387904331070635603,
                                        'source_nw_y_pixel': -6518098903648767589,
                                        'source_pixel_width': -7497139481602064558,
                                        'source_pixel_height': -5905080987048406091,
                                        'rotation': -9057439827546983984,
                                        'virtual_nw_x_pixel': -598421420,
                                        'virtual_nw_y_pixel': -1237652230,
                                        'virtual_width': 1933076555,
                                        'virtual_height': 393884093,
                                    },
                            {
                                        'source_monitor': 972484,
                                        'source_nw_x_pixel': -4299192952070219891,
                                        'source_nw_y_pixel': -8959132703050906222,
                                        'source_pixel_width': -4320867324714643860,
                                        'source_pixel_height': -8110790316334927884,
                                        'rotation': -6762440245239095510,
                                        'virtual_nw_x_pixel': -69874875,
                                        'virtual_nw_y_pixel': -1664704531,
                                        'virtual_width': 1822348207,
                                        'virtual_height': 1854264846,
                                    },
                        ],
                },
                {
                    'description': 'ǚ+ҽΉвЅԦǆҢbuȈɃɵЁǳ6ĕ9#ЙʀʢǻR˂ǭŢJŽ',
                    'monitors': [
                            {
                                        'identifier': 2220471,
                                        'width': -4302431915843461666,
                                        'height': -4824360287172982932,
                                    },
                            {
                                        'identifier': 1911878,
                                        'width': -8307798649557556300,
                                        'height': 1650027030574360132,
                                    },
                            {
                                        'identifier': 8872146,
                                        'width': 4760532334772928115,
                                        'height': 3895380240595442069,
                                    },
                            {
                                        'identifier': 2024807,
                                        'width': -6255914448452377911,
                                        'height': -8336859704238054257,
                                    },
                            {
                                        'identifier': -966397,
                                        'width': 3938081375408226248,
                                        'height': 739624572735161954,
                                    },
                            {
                                        'identifier': 879601,
                                        'width': 9083274075355877491,
                                        'height': -7056306235125795171,
                                    },
                            {
                                        'identifier': 1431146,
                                        'width': 2817823539002272856,
                                        'height': -6843073767908510841,
                                    },
                            {
                                        'identifier': -35901,
                                        'width': 114383059817316899,
                                        'height': -7973272959324806246,
                                    },
                            {
                                        'identifier': 535338,
                                        'width': 2562345696528117224,
                                        'height': 2525395084689954827,
                                    },
                            {
                                        'identifier': 7944228,
                                        'width': -1254309557334690792,
                                        'height': 8079016931673345768,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -247828,
                                        'source_nw_x_pixel': -6244123072521830969,
                                        'source_nw_y_pixel': -6810945076398150204,
                                        'source_pixel_width': -5421263811413405101,
                                        'source_pixel_height': -3320478234688482391,
                                        'rotation': -2239130702655475213,
                                        'virtual_nw_x_pixel': -1724550868,
                                        'virtual_nw_y_pixel': 426665503,
                                        'virtual_width': 1614680886,
                                        'virtual_height': 1006231358,
                                    },
                            {
                                        'source_monitor': 870052,
                                        'source_nw_x_pixel': -5463031317151648286,
                                        'source_nw_y_pixel': -3109189465713842148,
                                        'source_pixel_width': -5868054433440944231,
                                        'source_pixel_height': -6225881236871670418,
                                        'rotation': -3452323049998855319,
                                        'virtual_nw_x_pixel': -1845587583,
                                        'virtual_nw_y_pixel': -1365716164,
                                        'virtual_width': -1161405373,
                                        'virtual_height': -480532031,
                                    },
                            {
                                        'source_monitor': 567417,
                                        'source_nw_x_pixel': -5513374819514857128,
                                        'source_nw_y_pixel': -3912793761141766870,
                                        'source_pixel_width': -5943605030136706471,
                                        'source_pixel_height': -1492702954202310703,
                                        'rotation': -3076436430914554173,
                                        'virtual_nw_x_pixel': -1245594060,
                                        'virtual_nw_y_pixel': 942013426,
                                        'virtual_width': -292616668,
                                        'virtual_height': -1959612331,
                                    },
                            {
                                        'source_monitor': 5037275,
                                        'source_nw_x_pixel': -1399393656626874292,
                                        'source_nw_y_pixel': -2283908303448246477,
                                        'source_pixel_width': -42626214377368683,
                                        'source_pixel_height': -6746534632547054854,
                                        'rotation': -1073500417507245711,
                                        'virtual_nw_x_pixel': 853449005,
                                        'virtual_nw_y_pixel': -1345766124,
                                        'virtual_width': -683994574,
                                        'virtual_height': -1610247199,
                                    },
                            {
                                        'source_monitor': 1705516,
                                        'source_nw_x_pixel': -5350581588300720822,
                                        'source_nw_y_pixel': -6889809747685760248,
                                        'source_pixel_width': -2002357216339317571,
                                        'source_pixel_height': -5903854418982261064,
                                        'rotation': -2154762393176536042,
                                        'virtual_nw_x_pixel': 1897472671,
                                        'virtual_nw_y_pixel': -1626047873,
                                        'virtual_width': 1080031711,
                                        'virtual_height': 1155617803,
                                    },
                            {
                                        'source_monitor': 3674713,
                                        'source_nw_x_pixel': -5264314877907485151,
                                        'source_nw_y_pixel': -4587437314633076042,
                                        'source_pixel_width': -8836130646955395823,
                                        'source_pixel_height': -7345659978763700350,
                                        'rotation': -6568997300692287642,
                                        'virtual_nw_x_pixel': -1323056394,
                                        'virtual_nw_y_pixel': -1064459278,
                                        'virtual_width': 1401031354,
                                        'virtual_height': -1443944004,
                                    },
                            {
                                        'source_monitor': 7667701,
                                        'source_nw_x_pixel': -3632457858737513667,
                                        'source_nw_y_pixel': -7788625224426780044,
                                        'source_pixel_width': -5963578883564334011,
                                        'source_pixel_height': -5964919231907602671,
                                        'rotation': -7319637439952636119,
                                        'virtual_nw_x_pixel': -1132654897,
                                        'virtual_nw_y_pixel': -269789815,
                                        'virtual_width': -1343205808,
                                        'virtual_height': 1247294086,
                                    },
                            {
                                        'source_monitor': 8046772,
                                        'source_nw_x_pixel': -2719833314389071029,
                                        'source_nw_y_pixel': -5268740754856379062,
                                        'source_pixel_width': -38106595276687919,
                                        'source_pixel_height': -8568529994646528032,
                                        'rotation': -73064557852273004,
                                        'virtual_nw_x_pixel': 1328838003,
                                        'virtual_nw_y_pixel': 1184916058,
                                        'virtual_width': 1166047316,
                                        'virtual_height': -1592945114,
                                    },
                            {
                                        'source_monitor': 5366148,
                                        'source_nw_x_pixel': -7210214477011951118,
                                        'source_nw_y_pixel': -7907904957429938344,
                                        'source_pixel_width': -8697104366049216404,
                                        'source_pixel_height': -4554285571688025554,
                                        'rotation': -163492560055923156,
                                        'virtual_nw_x_pixel': -1380799676,
                                        'virtual_nw_y_pixel': -583122569,
                                        'virtual_width': -859502818,
                                        'virtual_height': 533537670,
                                    },
                            {
                                        'source_monitor': 1140480,
                                        'source_nw_x_pixel': -7222537872392029910,
                                        'source_nw_y_pixel': -2483988948205364598,
                                        'source_pixel_width': -5211180374594317099,
                                        'source_pixel_height': -558996468298435507,
                                        'rotation': -4012235249423158562,
                                        'virtual_nw_x_pixel': 44746437,
                                        'virtual_nw_y_pixel': -284045912,
                                        'virtual_width': -671253278,
                                        'virtual_height': -122897017,
                                    },
                        ],
                },
                {
                    'description': 'ђƑДʝȊȖǊԃӪιѐ\x95МҋșӝʒYҿǞԑɔѻҜœȽńʨәˆ',
                    'monitors': [
                            {
                                        'identifier': 2897650,
                                        'width': 5317690755907391574,
                                        'height': -4754389377688859028,
                                    },
                            {
                                        'identifier': 3980156,
                                        'width': -3469912994270279600,
                                        'height': 3565213053958985101,
                                    },
                            {
                                        'identifier': 5996827,
                                        'width': 2779178854995001623,
                                        'height': 1288278780102465689,
                                    },
                            {
                                        'identifier': 3959594,
                                        'width': -3314948640760117307,
                                        'height': -2141800997608830196,
                                    },
                            {
                                        'identifier': 1509361,
                                        'width': 7746126708069565332,
                                        'height': 7005897565301315524,
                                    },
                            {
                                        'identifier': -656705,
                                        'width': 5738827706639982589,
                                        'height': -2940336044059527227,
                                    },
                            {
                                        'identifier': 5706080,
                                        'width': 6031993937238725281,
                                        'height': -2229337416645049224,
                                    },
                            {
                                        'identifier': 4066929,
                                        'width': 8909316452853571818,
                                        'height': 1276501209095710690,
                                    },
                            {
                                        'identifier': 2020669,
                                        'width': -4950685581811115412,
                                        'height': 7458716767341658813,
                                    },
                            {
                                        'identifier': -587534,
                                        'width': -4557938996885629034,
                                        'height': 6574867184980147245,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -429549,
                                        'source_nw_x_pixel': -9181643321930544764,
                                        'source_nw_y_pixel': -500488560578452044,
                                        'source_pixel_width': -4216662338353806474,
                                        'source_pixel_height': -8446992906944338125,
                                        'rotation': -2862779306860073464,
                                        'virtual_nw_x_pixel': 558414147,
                                        'virtual_nw_y_pixel': -1788457125,
                                        'virtual_width': 1791821326,
                                        'virtual_height': -1981946079,
                                    },
                            {
                                        'source_monitor': 7193199,
                                        'source_nw_x_pixel': -2821365565160534173,
                                        'source_nw_y_pixel': -6222716747878093833,
                                        'source_pixel_width': -5276457385630682739,
                                        'source_pixel_height': -2855151536547560864,
                                        'rotation': -709732132163794987,
                                        'virtual_nw_x_pixel': -1156689388,
                                        'virtual_nw_y_pixel': 504778963,
                                        'virtual_width': 1864269046,
                                        'virtual_height': 795277593,
                                    },
                            {
                                        'source_monitor': 6558702,
                                        'source_nw_x_pixel': -4497129522008374092,
                                        'source_nw_y_pixel': -5453402828673828377,
                                        'source_pixel_width': -6743016816830216925,
                                        'source_pixel_height': -4129549059627857567,
                                        'rotation': -5349530537027679135,
                                        'virtual_nw_x_pixel': -711650338,
                                        'virtual_nw_y_pixel': 963969769,
                                        'virtual_width': 698520061,
                                        'virtual_height': -1186770004,
                                    },
                            {
                                        'source_monitor': 9824897,
                                        'source_nw_x_pixel': -2860660618338733786,
                                        'source_nw_y_pixel': -1522832945810569681,
                                        'source_pixel_width': -7099177726081149133,
                                        'source_pixel_height': -8093618370409964446,
                                        'rotation': -7930944985905906738,
                                        'virtual_nw_x_pixel': -340062214,
                                        'virtual_nw_y_pixel': 1249527606,
                                        'virtual_width': 1582670918,
                                        'virtual_height': 1596119543,
                                    },
                            {
                                        'source_monitor': 1057994,
                                        'source_nw_x_pixel': -2851603576866717927,
                                        'source_nw_y_pixel': -3037681733207893582,
                                        'source_pixel_width': -7655532644476904850,
                                        'source_pixel_height': -3436133614897409194,
                                        'rotation': -5704842398216059285,
                                        'virtual_nw_x_pixel': 495086906,
                                        'virtual_nw_y_pixel': -1291674100,
                                        'virtual_width': -729907033,
                                        'virtual_height': 1547665155,
                                    },
                            {
                                        'source_monitor': 5427345,
                                        'source_nw_x_pixel': -450470668057917036,
                                        'source_nw_y_pixel': -2061963999549253172,
                                        'source_pixel_width': -3305599308899814727,
                                        'source_pixel_height': -2926404025272264619,
                                        'rotation': -521445005496749584,
                                        'virtual_nw_x_pixel': -99469045,
                                        'virtual_nw_y_pixel': 1326228003,
                                        'virtual_width': -1977344756,
                                        'virtual_height': 714658441,
                                    },
                            {
                                        'source_monitor': 8310587,
                                        'source_nw_x_pixel': -1027178139064292626,
                                        'source_nw_y_pixel': -2864229390121903231,
                                        'source_pixel_width': -4074380600202155936,
                                        'source_pixel_height': -5082564077337530873,
                                        'rotation': -819452176528417710,
                                        'virtual_nw_x_pixel': 928616021,
                                        'virtual_nw_y_pixel': 535020481,
                                        'virtual_width': -568460909,
                                        'virtual_height': -1152510754,
                                    },
                            {
                                        'source_monitor': 4367837,
                                        'source_nw_x_pixel': -5396870707869029239,
                                        'source_nw_y_pixel': -3183021071767467748,
                                        'source_pixel_width': -7087046388129954319,
                                        'source_pixel_height': -930498994360689065,
                                        'rotation': -3874620619686200873,
                                        'virtual_nw_x_pixel': -1027000493,
                                        'virtual_nw_y_pixel': -683621818,
                                        'virtual_width': 817152394,
                                        'virtual_height': -1708460634,
                                    },
                            {
                                        'source_monitor': 1630724,
                                        'source_nw_x_pixel': -8344346206356233713,
                                        'source_nw_y_pixel': -83467892007653185,
                                        'source_pixel_width': -2045321140467580731,
                                        'source_pixel_height': -8623626010142217697,
                                        'rotation': -1103413525548394294,
                                        'virtual_nw_x_pixel': 1370100363,
                                        'virtual_nw_y_pixel': 1101812655,
                                        'virtual_width': 1180784103,
                                        'virtual_height': 1781929673,
                                    },
                            {
                                        'source_monitor': 1421994,
                                        'source_nw_x_pixel': -277444105757697276,
                                        'source_nw_y_pixel': -2457802126751024157,
                                        'source_pixel_width': -7759203071623735960,
                                        'source_pixel_height': -6410310262447710844,
                                        'rotation': -7386086592441246508,
                                        'virtual_nw_x_pixel': 66983285,
                                        'virtual_nw_y_pixel': 976772013,
                                        'virtual_width': 522419385,
                                        'virtual_height': 845947544,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 4503024,

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
            'request_id': 6571274,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 2072060,

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
            '$': 'бŠʃɌȀӯƷōƢɛĮόɣрȚϴԑɹŠъΩ¶ӨкǌнǐπҠЎ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 3443654864021900616,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 598872.7319987663,
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
            '$': '20210228:024615.136209:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                '&ßЙтюĲƨǃ͵ѩƖĕХӢɇϯ˧ҲĴӦɰŨā΄Γɏ\x8eЈåϡ',
                'йƣˀːфǙȚǳΕļè˺âûÿ˹ԕжПɤңυ΄6ʺʶȞGʎɆ',
                'ƙϦ}ӁїŪğ˚ԤҊѷįKʞϖҨӾ;ǵϰͻ$МϋɄƅĚӂӆԉ',
                'υuӀɺӷӀȍԘʩ\x9cЩƷƋȢ[ØɒΤtŃ\u038bѡɋďźӂƦҩ\x87Џ',
                'Ѻ˅˘ːЋɓ4˘gȺ`ξǻѝҍЁȀЦ\x7fǠЕΦēzӈґKǎɋɢ',
                'ӭͺюˢǏ˫ͷɪƼ˪ƁƺªÕŖҞØ҅ŮԩƮƹћ˳ˉԫɺͱΥʬ',
                'Ѹɕɥ҉ѭ@ӳКǢчҦϿʳaЪκɠǄ\u0380ƨõ=ƉіɪʃɬЩ¼\x80',
                'ɇёàʬѼ҂ǴȸÁɑѷ÷ͻ-ʜƲ΅шΨώͻ˷»имѳ\u0382ЧϽ\x9b',
                'Ƅ_γԒӓӢҞѧˌ˷ҫʾПÃvӈĹƠʴӠǲȩȂ\x94ɁâΥҶɾϻ',
                'ͽЈќˈŚ˝ғӄԥɚřƶҦӚǝ˔ǷŇà\x93ǙȬѭ:șaщΖfǦ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                1110638414892035556,
                -6145927374863479216,
                8350038948888616004,
                -6145855376535608727,
                -8039289422541891517,
                1825608701984672736,
                -6881896357284538164,
                -2276195575697754583,
                6956655305133132059,
                -448824841190381914,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                238148.47306002834,
                919546.8234360906,
                923944.7743431544,
                -34106.535833121816,
                190359.45372088533,
                -76666.72703472122,
                585253.3953272303,
                88572.38967332867,
                118552.39508225021,
                919107.5083603476,
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
                False,
                True,
                False,
                True,
                True,
                False,
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
                '20210228:024615.137974:+0000',
                '20210228:024615.138011:+0000',
                '20210228:024615.138026:+0000',
                '20210228:024615.138040:+0000',
                '20210228:024615.138053:+0000',
                '20210228:024615.138071:+0000',
                '20210228:024615.138090:+0000',
                '20210228:024615.138113:+0000',
                '20210228:024615.138132:+0000',
                '20210228:024615.138144:+0000',
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
            'name': 'ɐǉǳơ4ɳǟæʘt\x91ҶÌҼҾӴǣÿɽȍХкõĪҐëʊȕŐӫ',
            'value': {
                '^': 'bool',
                '$': False,
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԁ',

            'value': {
                '^': 'int',
                '$': -8685203562727230574,
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
            'catalog': 'ӝ;ùǒϭϝΞYģξψʃ\x7f\x9eȋѩĳėҐьȹŎ˯ƜӸҞӃȘаʫ',
            'message': 'ЩӆЎФˏӘƞĶκ.ŋƠŻʜ]ӖӺũԫϧϺȡǛΞʩ\u0382Ĳːʳ˾',
            'arguments': [
                {
                    'name': '|âŕЪЇɼɅPƔɬÓԓҎĸ+ϕɚ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        241933.9760091345,
                                        612047.7901993769,
                                        806175.0675429099,
                                        23810.949017956955,
                                        663503.6446467463,
                                        103925.60085011006,
                                        579286.0607870851,
                                        47810.1427732023,
                                        296589.0712243755,
                                        607585.323242609,
                                    ],
                        },
                },
                {
                    'name': 'γŃʟ\x90øѠšʌϤƱө·њʼƂѼԨԁԜҩ΅ғԬЈʵΦ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210228:024615.132972:+0000',
                                        '20210228:024615.132995:+0000',
                                        '20210228:024615.133003:+0000',
                                        '20210228:024615.133009:+0000',
                                        '20210228:024615.133016:+0000',
                                        '20210228:024615.133022:+0000',
                                        '20210228:024615.133028:+0000',
                                        '20210228:024615.133034:+0000',
                                        '20210228:024615.133040:+0000',
                                        '20210228:024615.133046:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ǺѦ\x83pĻПǝ\x83æʭřɦǴþǳȑҘŸҡϗŸғʏÏͺЫòҗԏ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ȯɫɦǙƔϘȿԔǉɯϪϓˌʼĶʝ[ԡŻԆјӆѥƊΪȏ˚үѰʛ',
                                        'Ӷ×ɊŧӻԈѰЂãԄ˘ҳӬ͵ɠɈČęǹзȟɧũʾПɒðӚЉҰ',
                                        'ʯѨҒ\x9bʙăӁѼāĥ\x95ȼʺǤҡʣϤҿįɼɑћӝͳŋͳÅԓhá',
                                        'ɤȇώҚѸ1ԡĐƻηǽɠҬнȲԏҕτͼѠġ]сѡдɌ˙Ģɂԗ',
                                        '˧ԏӔ1ɍÂϑĈ\x95ù;)ǘϾӨ\x9dģѢԥүАRÜ˜ǞѺΏɆɜϞ',
                                        'ˣ\x9eХϳвƨнӪʛҁϷ&ʹʀ~ʪʙ˸αȷÀƨɗˡεɒư^˨ϙ',
                                    ],
                        },
                },
                {
                    'name': 'ŮƌϾĳ˖κȼêǳ( ɞĭ§҂ćʗř\xad¯ӡYϜʟŻЕáӠϞ˰',
                    'value': {
                            '^': 'int',
                            '$': 4875260645920980523,
                        },
                },
                {
                    'name': 'ɫvџԊɖŸʦɡˉͶϠʿϻɏɎԊKʫˮʢщϟ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ŹȵĉҖʳÓӀ¸ЯɍǪɰԨ˔ѽѿѲćǶĨŊǟɮ˴ӇщїɘȢʱ',
                                        'ԋπѯkԀ˅Ьӱ΅Б|ɧʳɅїЙ\x9f˃ɕԨƓHʲǘӏӟЩˠΩȱ',
                                        'ȡԨʟžù\x7fƢϴĄ˙ƜΠĲŚҴϑŗˊ˅ǥҩϾЖСѩҦÿȇŃө',
                                        'ŭɑѪȭԒĸжњΕĔƄvЍѥ3ЍǈΧǢȓ˟ȐĭƁſČþˆάӗ',
                                        'ɧЍq҃ɱNȂ˞ZƲŖGȷƜвΜӀήɔˀŗѡèɁîůŉÊƨƦ',
                                        'ȢҨήɲηòƼɇėԀӕЖʑʶƽ-ӣӧԄƤ1иʑџʩÑÇϊϱɌ',
                                        "ɤŌǼLϵҤřɄ'ħϨϋԛńνѡȿдşƷͱРyНđДҋʘè\x7f",
                                        'ǛҨ˨ɩÀІЄȉĪ\x87ϰϵû\xa0ĨǆӍǥǠÌҧӴǚLƳКPjӥƱ',
                                        'ϙϭʞͲɖԎ҆Ȓ@ɉȮʁʂȆŘЛҦӫǈг¾΅ԫ\x93Ôƈ½ӅǳȒ',
                                        'Č\x81ɟIӣƍԣʠƮʉӼ-ԈZñʌϵ˱ҽԪưS,ѕɼȈƔЏāȮ',
                                    ],
                        },
                },
                {
                    'name': '÷ԟ˝ɞяɲсŒǚήđʟȰħˢǅ\u0379ʑ\x94ġƁƾƈŞЉ[ňȨȈ˒',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210228:024615.134415:+0000',
                                        '20210228:024615.134434:+0000',
                                        '20210228:024615.134442:+0000',
                                        '20210228:024615.134449:+0000',
                                        '20210228:024615.134455:+0000',
                                        '20210228:024615.134461:+0000',
                                        '20210228:024615.134467:+0000',
                                        '20210228:024615.134473:+0000',
                                        '20210228:024615.134479:+0000',
                                        '20210228:024615.134485:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ęͶk\x94ӁŞϿǕωӜ˪ЖÉŇЩƷ˳ӫˉʬϤ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3347892723402479080,
                                        7284875748639342439,
                                        8885885972352189201,
                                        8695668010577680281,
                                        7362133310549051795,
                                        -9144908034888153702,
                                        -1262412677095280614,
                                        3250956026504505440,
                                        -7801084806104955455,
                                        -791990256177606111,
                                    ],
                        },
                },
                {
                    'name': 'Σ^v˻VʧчўļΩήͷξζ\x9aɽ\u0379ʹýəɀ\x91ʜŕQ-ԦøĢ\x85',
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
                                        True,
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'ӅzυŨϽƇѤӪԢɗЧˋ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210228:024615.135241:+0000',
                                        '20210228:024615.135256:+0000',
                                        '20210228:024615.135264:+0000',
                                        '20210228:024615.135270:+0000',
                                        '20210228:024615.135276:+0000',
                                        '20210228:024615.135282:+0000',
                                        '20210228:024615.135288:+0000',
                                        '20210228:024615.135294:+0000',
                                        '20210228:024615.135300:+0000',
                                        '20210228:024615.135306:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ɑ˼±ʩКҶӽțӸɜù´dѼɞ˂ĭIϋÝǝΓQϲɇƲƕƚŉњ',
                    'value': {
                            '^': 'int',
                            '$': -336690921279029209,
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ū˜',

            'message': '>',

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
            'identifier': 'U\x9aӅǢ҇ѼǤŵŷл1ҰɺšʧҲƑɗʯӼӏ7\u0378ŶАȖƌ˴ÿҷ',
            'categories': [
                'os',
                'file',
                'file',
                'internal',
                'network',
                'internal',
                'configuration',
                'file',
                'invalid-user-action',
                'file',
            ],
            'source': 'șñΗÿҭȅƣͼӜŗЬàңǘą\x85¯Ϥвѹ˼ȐԫţԅŚƋƼǰԫ',
            'messages': [
                {
                    'catalog': 'œß\x96)ìвɂ+ǀͽӤіÓÏŗǕƯș8Χ˒\x9bŖǌѢȱƶүҢν',
                    'message': 'ώǒϜҽҼӏϳϨ¬ÙɷӅŒÔ~ěĈ®ѓΧϾãοʹ9ЂǶüөɢ',
                    'arguments': [
                            {
                                        'name': 'ƵʏŌǍΪўЖuѶeҡЉǝδȌӣɨɸΗήĊƴŢĕ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            911963.0158369519,
                                                                            300867.066389139,
                                                                            107785.34386507902,
                                                                            -40968.09631803887,
                                                                            123394.99864060365,
                                                                            -5358.790618625819,
                                                                            954369.4895486566,
                                                                            63136.58576365092,
                                                                            -96222.34768544191,
                                                                            697996.9814378308,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʏȸϰ\x94ÞЀηŉ˹Υ±ǌƟʅрІɸϔѫСŽΠ\x91мԞˣȎʭȒʈ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6192492915951690340,
                                                    },
                                    },
                            {
                                        'name': 'οɕ°Ƽ0 іӗЦɆɩӌǑЩˢζњсѪҀԧϿԪʛʄ±ʡ»Ȩ6',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            480337.47752190265,
                                                                            717677.5205284128,
                                                                            770513.3404730442,
                                                                            303161.1012495671,
                                                                            391467.24872927985,
                                                                            815461.1816688337,
                                                                            50809.99598826052,
                                                                            109030.20306104227,
                                                                            858420.71024748,
                                                                            501186.7955879676,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ľ²ŹҙŇųŮĎҒӂ'ˠȫˉˊЂӌҔ¤һN",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.093210:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȇƜǰԥϽpԮã¦ʐέԚɚʕĈȋ×ɥ˩Ƃę',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.093372:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӌ\x95*Ż˟ƬͰSɠþșƵзğЗ;ȮʜħͰϴϲǣӅϽˋTҹĀď',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'ԢԩпЊ}ÐɉӨħɋ,ӀGїɰαЧɰĠ\x97ϼǝˢȯųǲɿІҵѪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.093770:+0000',
                                                                            '20210228:024615.093784:+0000',
                                                                            '20210228:024615.093792:+0000',
                                                                            '20210228:024615.093798:+0000',
                                                                            '20210228:024615.093805:+0000',
                                                                            '20210228:024615.093811:+0000',
                                                                            '20210228:024615.093817:+0000',
                                                                            '20210228:024615.093823:+0000',
                                                                            '20210228:024615.093829:+0000',
                                                                            '20210228:024615.093835:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˘ԋɋƧˤßЮʋӜǎʭƓĊ\xa0ŀŰÊţϺȬ¡ă҃ҏǊϲӾϴҗǯ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1288941577685262861,
                                                                            -1721571419551808645,
                                                                            4262918969745977122,
                                                                            3153301202808333522,
                                                                            7788443047469246126,
                                                                            9124759801322103134,
                                                                            4836096170456432092,
                                                                            7842047660508236330,
                                                                            -6214367586667671365,
                                                                            -5246077580597893866,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѬԌˋȢԥѭʷÅҟЛΏbǉ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǣƲȊŒӐз:ƟưĺĠċ]%PХƌɝδĿЈŅŭyǛɯ{Ω\x93Ȉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 85565.2916487768,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʹhψЁƅ\u0378ɒįԌȤϏҲbŕżȢυΜӱԄԂΰɩľ¡цYχͶΗ',
                    'message': 'ȋ;ƀÕȂѳϻ˛ƵоȞȡŸϰъŧΥЏd±ȾùŨ6ԫ0Ԉͷԩ˂',
                    'arguments': [
                            {
                                        'name': 'лЩúȐƔȯÀßψӘϐ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            905807.511551112,
                                                                            5345.203865973119,
                                                                            413858.9528689424,
                                                                            441969.0162445832,
                                                                            115382.72239652148,
                                                                            652952.9645152314,
                                                                            630070.1014440344,
                                                                            182682.93701440823,
                                                                            890546.8890752473,
                                                                            418562.2225108686,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЕŃԔɔ\x84Ή¯ͳĒϚˊˡȥȅ©Ίʆѩ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĉƐАҩĎԫ´ΕúɇźƸҶȨϖ½ӐϰƸɍГaʑςƞѵË˺Ƴ˱',
                                                    },
                                    },
                            {
                                        'name': 'ӌКԇΝHɧƜ0ȩϺΤPYшŒzԋńƑӽ.ύ{ƟӈȾĈɐϽɹ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -3690007829894511279,
                                                                            8708205617707365316,
                                                                            3826546664939635512,
                                                                            4844327782468675695,
                                                                            4969572537188118819,
                                                                            -834825055362591587,
                                                                            -3159325054072407967,
                                                                            2547934487934715799,
                                                                            1105597951135841233,
                                                                            513378441403147520,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'хʺэҰWΖԏҳδÁҌМ;fʏ\x89Ó˖(ɰ˔ѶѧδΩ˳}Øʸ=',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȴόԂŖőɢŇœę ʇӉɩŇ˧ƴʺȫҌYъĶʳǪʦƍùɠĆǪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4866908024420441973,
                                                                            7230000142405918789,
                                                                            7797365463369156552,
                                                                            -3979675337313713695,
                                                                            625871353585856196,
                                                                            -7796762646305510906,
                                                                            7423324257834585614,
                                                                            -8186553765647008475,
                                                                            -467729964169990382,
                                                                            -1768886533847552492,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˕ӤԑҪʜîˈοª',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 473302.8754363959,
                                                    },
                                    },
                            {
                                        'name': 'Á\u0383ӓʽ\x83ǖϼȅ˔ʯʵЈҵѥӍʛЊǨѝøӕ2œ˫óȎőϥаѯ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '$ǆͷ;ӇΨ¿ԋÔσŬːǹHӋ˙ϥJӪϋˉҞ\x92Ч\x81Śϋ×Ǣˇ',
                                                                            'ȋɾƲʁҹ\x93ȼǚϞǲ˙ƲȘŽǶԧϙƏȵȼӋѨǖǦʆϬʭ¤фԝ',
                                                                            'ƋѳЍ˹ɱЍ˜ǮɿмҞ"šĽƘӈҎϽΉӇÌƭeǃҋ87˛XȀ',
                                                                            '˺ǿʌĴѐҨҸX;ˑɯǄĦҶьцІ\x93҄åΆǫǆƛǛ΅ȤҴҕŭ',
                                                                            'ƔɕƩkΦӉtЉǧ\x8eʻ˴ňĞϰÖӾǘȽӡјɟȝϒə˙ĔǝҹӐ',
                                                                            'ñγĭɼԃǵǮǼќǭԗԒǾÑ\x8dϴʂĤǴʶϪҕљĖйԌĻIŗΞ',
                                                                            'ӁÐźǈҞнȗљǋӿ\x9cƢȄҠз˘ŇЀν҄˭ļϱҿĳ\x9bĽх)Ϭ',
                                                                            'ԜdɦʛǜЈŚαԁɜʨъĸëȳǕȑЕԪɊˊ0ыѓʠ˯Ԛӯԝέ',
                                                                            'ѺŒϥԘϜӚƈҠЏЎƤɘкƝБСßкϨѫˋɆπ6ņŦίǚҘ¤',
                                                                            'ƈɜǟηƸԝ~ϰͻϻʘʼ+ʂМɜҤԪČȴŉЄΠŔЫƦΔĊǦ˖',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˭ˋSɥӨÊэgŽʀŨŇ˽\u0383ϜϩΨʯʋ˟ȷ\x8cʛ',
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
                                        'name': "ȺͼβɮũɫˆrҠԟŕįȷȚȚȺĕ-ũŷϔϼ'",
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.100670:+0000',
                                                                            '20210228:024615.100703:+0000',
                                                                            '20210228:024615.100743:+0000',
                                                                            '20210228:024615.100766:+0000',
                                                                            '20210228:024615.100786:+0000',
                                                                            '20210228:024615.100804:+0000',
                                                                            '20210228:024615.100823:+0000',
                                                                            '20210228:024615.100856:+0000',
                                                                            '20210228:024615.100876:+0000',
                                                                            '20210228:024615.100888:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ș0iƨʮԎ0˴ΣӌȱΞģӣF}Ư',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.101397:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҵӒȏ¶(ԖQпԬȂӻƛƸȓǀāɦΘȰЁŨ ŻɵҔ\x90āѵύѷ',
                    'message': 'ę҅ьƢΙʁӎŤϟї¥ʍʶЛȤЈζÖφȷßîΝƐˀþ\x8aƋŌЈ',
                    'arguments': [
                            {
                                        'name': 'ШǳhџĔ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɽӤȻϋΚԝͱźˮӁƯłźӎӉƺĽ²ņgΐȷ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ύуҫѩǚ3ĳҳ0βєŇԡɵϬ¥ǝÿӱέѾoœфԔΏmʓАσ',
                                                                            'ɈCѵ\x8fӼȲвИҐĥĎųпƑҴĸĪʊωśȚҸńJ˨˖ɞƩĩĞ',
                                                                            'җ÷ƓԐԮ«ʷɤεӔЂMƤƀʦ)έΑϛƔȂƒ·WĝʔӛʽōŲ',
                                                                            'Ѫ2\u03a2ѯΖӢğǪԨΦǦtʓŀӌԕͷʎČȌϫǂǻƓßϩǖΥɨѨ',
                                                                            'ћȦЍƲԘЪǡάϯΓˋǹΙȌԛфǝʋцȧʮӖͼӐ:˷ӃĮȰƒ',
                                                                            '\x86ԜӞЬHèídƁÇÁʩƯœ¨D\x8bèO\x9dǚɘ҅ŭÑϊíΌɩ¨',
                                                                            'щ\x93\u038bʹÇʉʯЄǘ.¿3ӳΟ5ұ\u03a2ɁĺŶõʬԚË\xa0(ӉɖӘǖ',
                                                                            'Φėӯe˩ŧÈϖ\xad@ƒҵϼԞ҂јx҉\x96ÉǌƱӪÛČų\u038bґϒβ',
                                                                            'Sȏ/ÉԃąäѢùÿÞƬȱȷМƀӬɐǟǞͱ\x80\x80б«\\ӀƘϣԂ',
                                                                            'ѓǌѕŻ˼Ø¯ϳҽϊʈЦǷ˙Гǂʹ¦\x86ʼΰƏĐЬáŎɮνɲЇ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ZʉΡӲȭ×ʋɓԝǫ7ӗƳѿʎМ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ΨĸҪ\x86á)Є~˨кF¥ćϛOŜǄŷvĈќxЮȻƔɺǻɸɝӬ',
                                                                            'ΔЮѓӬȟĈ˛ʜɻȗѰҶĥɃҭϪˎҧԤʥƳʱĐʣҭ+Ԟŗµȁ',
                                                                            'ԑϐҰʗÑ͵6ϯũɆԟɑśƥƉʝ\x8e\x9bŦȺ»б\u038dѵҌҒЧʥŞĄ',
                                                                            'Ѭҙŭ΄˯ԗüΖ˘ӎԍȸ˟ļɓȖǨńɛǡœԅƕQͷӰ\x88˹Ę΄',
                                                                            'ϧŲǕѦ\x89ŜƛǛǅŨŵˬΈԅФƞßŷìЋāˎϭ«ľ)ȘɲӚī',
                                                                            'ĩъʈӹФǀˣåɴǨȃȓ\x9fЂ˭ǒʍҦҀǶʠɆ˪ǓΤȝʮļʒė',
                                                                            'ɠΠϐŮȘǁ.ӋůɡνɧϺ\u038bР˪·˻ԫƚϪѺҦĘɂёw˚Ԅǭ',
                                                                            'ÔԍñɍӵӘĂʥPҋϖђУϥ˥ǡǹĐʓђ˗èǰҪϬ ϝǄů˧',
                                                                            'ʇǯл˒\u0381Ό҆ЅύͰɕϟĮˢƖƧʜȦǓɻȒӌƹǕ§ʔ_ôʲ-',
                                                                            'YϯǶWҽĭ3ϮɈǄˎʇĳɹͶǣԍбӝˮеɂЧψ»тђӸɋ(',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӧ˯¿˵Ԙʮϫ^\u0383ԄѤ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'rLԔȓӌ¦ʥźǜҏͲÒȕǚ|ȳьˤҷҷέùp®ǒԩ˰ĖȋƎ',
                                                    },
                                    },
                            {
                                        'name': 'ƧÇy¦җ÷ѴəɉΰəБhƉɸ\x91˖ԎÈԘɷȓѭ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            737033.564236113,
                                                                            512460.17385341774,
                                                                            206185.6329718795,
                                                                            837035.0575753114,
                                                                            705367.523758434,
                                                                            278412.64323553414,
                                                                            335741.7918863234,
                                                                            249740.35170408047,
                                                                            891677.1114605479,
                                                                            228418.13383466698,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9dȇѡÃ\x97+ϯȻƁѺɉЏǅѻǢþyďʏàhnaǼˆΥδ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ΝĶϼʕɡºŧŅȼδ@˸ǩǹ«ŷ˝ѕ\x99xҙAүɨnbƫā\x9e\x7f',
                                                    },
                                    },
                            {
                                        'name': 'Ĺ˖ЧΆĩ\u0382<ƀɗοԥȋǲȌʥȓωȩƂ$',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            965971.7296758932,
                                                                            840098.4980121648,
                                                                            378428.87078605854,
                                                                            964334.3460007897,
                                                                            411305.06945691275,
                                                                            -36537.835615071,
                                                                            381625.14048410335,
                                                                            311123.4754539412,
                                                                            414421.91937234096,
                                                                            675298.6536312266,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ťσ\u038bӝEҶɶŭ\u03a2Ûþ˳ŗӽϧ¡ΖӪGӶϏ˖Ʉдҫѻςάzƭ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 763924.6984453137,
                                                    },
                                    },
                            {
                                        'name': 'ȔʾЀ¬ӏҊ¨шԁϳƈñɓŉŵ˂¬¼űAșӃΨ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'J\x98ʻƛȳ§ÂēǪǞҳρӷӿӹɘЀӕůɳʴ˄ìŚǄ˹ĩƀӵď',
                                                                            'сĨɞì\x9aϲĞέɔыӝʵж¨\x8eϒУ˲Šà΅!ƿʕ΅ԟγǽМų',
                                                                            'ÿɀȡņ\u0379ÄȬȬнӷȥȑYǴ\xadʫѺɾǟ}қȍԣʸҝɏĢrϘμ',
                                                                            'ʞϺКӮȇȯƹΫŽ!ˋƲÜԉ\x90ő\x8cŚȚͺͻѐÈИўĘҔ|(Ȋ',
                                                                            'ɕОǍéˇЅŭŏѫƘϑΌѫÑѾǵΈ¾ħʡΖß0Ǵ¾ГЉΝѨД',
                                                                            'ːȾȥoӱǗƌþ^Ϫʜɟ˶y˥ԏюԔǭЁТțʩ˝йÏɲͼѹÑ',
                                                                            'ˣЍχΦ{įŴɣƬӃȿѪăІǦXʾǭſȳƫѿВʘ҈ʟÚӚŝË',
                                                                            'șғ6ΥџßӤƊ\x9dʦӒc[ǐҠzĹрͽϲ¡ҴÔ§äҪp(ΊŨ',
                                                                            'ѰϩŌЪʖӗФѪΎ;ƛΰß¤ιԡƔ8˗΄ƑɛĝҠDδDʵԜȻ',
                                                                            'ǚȮʬͻɬϿɏǿҚȱǤ\x92©˝TΣԀ\x95ʖŗŏƓҚѐÄҀʻ&ɹţ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ь',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -177118720442081854,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȟűaʔʍoǎdΟœұԜ͵ƫĮЋɋɆňžƫĂΣǃˍțƈŝūί',
                    'message': 'ċӌʉԐʧφƒʖĮҚśŇ\x92μѼǏĎˈèƆˏҗ˚Ӵɧɼæфўɏ',
                    'arguments': [
                            {
                                        'name': 'ě',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.108445:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ϷβąԀΜ[˱ȾʽäɚǑ®ľӖŐʭϘь\u03a2Үѭ$ϮīМƒʒʖƢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -21867575234775388,
                                                                            1312635721856903818,
                                                                            6663482161984890732,
                                                                            -531611847443289233,
                                                                            3623806670589371567,
                                                                            -1557273570065768211,
                                                                            -6643041495104279515,
                                                                            -3487829803391318231,
                                                                            5850336749726461865,
                                                                            796663751529978698,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѻϘ\x95´OӠŝϤƺȌ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -75785.63504361236,
                                                                            602797.6725936009,
                                                                            220432.93452800222,
                                                                            466900.71664513065,
                                                                            13983.152933103454,
                                                                            -41412.91021764514,
                                                                            165240.4180553453,
                                                                            787456.8731737026,
                                                                            558731.5305970622,
                                                                            196595.96946281003,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǶĩϼӃΗGҦȐԆ8VԉНΥļӶ\u0383ɏȭӧщҦή˝^ŘӇԘʌь',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 52776331272273840,
                                                    },
                                    },
                            {
                                        'name': 'Ƞf»t˓RʹƑ\x8eȅаҍʩͱºΦʷң<αͻȠѻ˱°ȩȁԞϨŧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 168968.4321388689,
                                                    },
                                    },
                            {
                                        'name': 'ӀӡƓѰ\x7fÀВӯҢɡӧɴ҃ҁϑĻϦʣԏ҆ѵЬӊÛІБ҈ϽƧ˚',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            526653.9304596336,
                                                                            118413.9051776971,
                                                                            85861.72068508717,
                                                                            613650.685811387,
                                                                            341556.5703475863,
                                                                            6894.503698229615,
                                                                            590644.1447978641,
                                                                            653871.7596460073,
                                                                            443182.59791744,
                                                                            380807.5634434286,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˯ӮҷϲѴҿȦ5ҟɟ@΅ÿФ¨ƺåϛӸŖЯзƛ§ƸȟɹцWО',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.110861:+0000',
                                                                            '20210228:024615.110892:+0000',
                                                                            '20210228:024615.110910:+0000',
                                                                            '20210228:024615.110927:+0000',
                                                                            '20210228:024615.110942:+0000',
                                                                            '20210228:024615.110958:+0000',
                                                                            '20210228:024615.110975:+0000',
                                                                            '20210228:024615.110991:+0000',
                                                                            '20210228:024615.111006:+0000',
                                                                            '20210228:024615.111022:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϳԫ\x86δtĦ˦ƑӭˌȲѷ±ӟҐΛВɅЍсɿ\\aӘćэʱ˗ʗ½',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ǌǐȌȹģºŚƆƨ˳ԜɇËцў˾ǩͽ#',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.112100:+0000',
                                                                            '20210228:024615.112116:+0000',
                                                                            '20210228:024615.112125:+0000',
                                                                            '20210228:024615.112132:+0000',
                                                                            '20210228:024615.112138:+0000',
                                                                            '20210228:024615.112144:+0000',
                                                                            '20210228:024615.112150:+0000',
                                                                            '20210228:024615.112156:+0000',
                                                                            '20210228:024615.112162:+0000',
                                                                            '20210228:024615.112168:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɝ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѿʷƟÑʹR\u0383ÆƞɷˋЄčǜ˄˼ÉΔ"ѠюƽcǁԬʁΧơnȄ',
                    'message': '˻ƫ΅ƟǭʨęЅӠ\x823҉ˏѤĦe£ǪĘ÷ӫјӛšȹıρӺԩϸ',
                    'arguments': [
                            {
                                        'name': 'ưГ*ԩхíцĩԌȌхĺƲĈôϢ˕ΒјőªΣȯѸƶԎ°Өŷ˚',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.112961:+0000',
                                                                            '20210228:024615.112976:+0000',
                                                                            '20210228:024615.112984:+0000',
                                                                            '20210228:024615.112990:+0000',
                                                                            '20210228:024615.112996:+0000',
                                                                            '20210228:024615.113002:+0000',
                                                                            '20210228:024615.113008:+0000',
                                                                            '20210228:024615.113014:+0000',
                                                                            '20210228:024615.113020:+0000',
                                                                            '20210228:024615.113026:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȗƗΦ˧ƝɣΛɆ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.113259:+0000',
                                                                            '20210228:024615.113270:+0000',
                                                                            '20210228:024615.113278:+0000',
                                                                            '20210228:024615.113285:+0000',
                                                                            '20210228:024615.113291:+0000',
                                                                            '20210228:024615.113297:+0000',
                                                                            '20210228:024615.113303:+0000',
                                                                            '20210228:024615.113308:+0000',
                                                                            '20210228:024615.113314:+0000',
                                                                            '20210228:024615.113320:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'PɵǆхҟƁ\\Νɥͻ\xa0Ц\x83ȝǨɁςɗӘC',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2187495093510801332,
                                                                            -5387209374734592156,
                                                                            -5546954636289942876,
                                                                            3432184673208180485,
                                                                            -3063090773887272137,
                                                                            -2032525261890965220,
                                                                            -4191842041913347249,
                                                                            8659958403434889632,
                                                                            9209450496292829930,
                                                                            4805910484899010263,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '÷ґкØ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2158480624566945051,
                                                                            4891706798932810439,
                                                                            6777542689863319281,
                                                                            -5249446597275324745,
                                                                            8770437772120288224,
                                                                            1929135946482048500,
                                                                            2458680811224520409,
                                                                            -4031419018759629088,
                                                                            -7953838160459004226,
                                                                            -8117637385596473481,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '2ȟœĳ?',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӮΐƇÕьƤͲèȢˑŢҖʴӨͼɦȒҰҴĻЄ\x94ȺŁƊЌƼɨŸΣ',
                                                    },
                                    },
                            {
                                        'name': 'QԂӸԓίĬŇÔϻöӱѕƂóПĦϭӯĕʇԘƦǁӘ?РgvϪ\u03a2',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '˞ǓʅҿˉɭPѨѻӄʡΗ¢˧βѐ˼ǔӻĻǕѶ\x98ъƭӨȮ҇Ħӳ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.114771:+0000',
                                                    },
                                    },
                            {
                                        'name': '¶ĞˋɟǬΔÕɘγ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ҡκ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɡǷȄàûĦцӽòɴыĠ юӗśõǏȇҝѫįȄűр\x8bƳКӞϦ',
                                                                            'ЖԟǴĂό˚ɊýƴȡĹȚҔģǗʢ\x98ԂǩҝϾжǶѰǄ˂ÀʽǂТ',
                                                                            'ʳΌǒӟœİԒȎʺAΚʘϠƼ\x98Ʋʓ\x92ĄԅĠҟοнƸȤ²έԦƜ',
                                                                            'Бš˔~ӵŘӱфԏĖҋȁƼϨʓҦǡN]ЎӓƬƥѤǽƏ˻ϸŚэ',
                                                                            'Ìǌє)ŽŎҪMƚ˟˫ѶPɲũ1_ыǛΛНɆÚɑΓĕʍàƜa',
                                                                            'Ť҇нϋʹƼϥРǦ˭ȁɌÎɻҐԬȇӜ±ȇĿʩʣХìűТV\x86Ü',
                                                                            'ӮŵʫӰȇ҄ΎО˹ҰɵǘϓӆȡфΣвпWțʛċėćӈɔß˂İ',
                                                                            'ʊȵǼɞͻӐDϘªɴcɚä\x98bĆɰɈƵРƥˎ˹Ěȫ`ЧхFя',
                                                                            'ϯϫԋлǄȟþŬ˸Cԕͷ\x90έџԉвԡˎ®ԐÃԑѮѡϵСҙŲl',
                                                                            'ӌÈƠӉΒўŔβѺфƓγӦˣƒəˮȶҊǹӰңĨΦſļҭϞ˳H',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ţƮыȘχ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4320817310584510742,
                                                                            134688883192969018,
                                                                            -4854560798992488580,
                                                                            -8402574187361317858,
                                                                            -6671681805137238603,
                                                                            -487240801767382880,
                                                                            2041943563440566516,
                                                                            6197469387573948776,
                                                                            -7830842973175693601,
                                                                            2988341251849778587,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ķКɏȀάі˲ŎΩЂӔ˱ń\u03a2ƁŃŎ˝ʃlǺȠ<˟ĮcЫÎıY',
                    'message': 'ҧŞѝҽćʠъϠØ\x88ðʝʴ˥ϏÖԥƇŽШƘ\x97ѶļɥŶ§ʀˣΌ',
                    'arguments': [
                            {
                                        'name': 'ΘĽӯ\x93ϦQãªΧҽψĮɜĪβΥҰɯ\x91Θ˽ƫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ЩӕÀъԠɑӇʻЉ¦ƷЌʎϪҥŬŰǓʇӂӘ˴˳ӟāԔԀЭȧà',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ҝ?ɎȒʧ҈Ƅ˺Ĉ΄çåВʏϟейʼ˨ΤЋ\x82ӗ˗~"Ĉtðˏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 175195344681712153,
                                                    },
                                    },
                            {
                                        'name': 'Ƞϋ\x82\x7fȇӁǩӞЏʸҊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.118923:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ˋΥҟγ\u03a2º\u0379ǽΜЩ/ΛǟȀ˷ȸͽ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɏɩ×Č\x97Ҥ\x83˝ʤPʫɿȨHϊǌȳ(Ѐǖ"ƨƢҧҒ"ȈjÚʛ',
                                                    },
                                    },
                            {
                                        'name': 'ўϮŐ\x8aſF÷QĈʤˑţѰȁϮVǾЌʑɖ°ŁϞ˄Л˲!ˣŔї',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            561790.7777343357,
                                                                            230015.4728353175,
                                                                            803051.7766120621,
                                                                            690563.3878617821,
                                                                            993275.8059377649,
                                                                            -99092.09584553893,
                                                                            403251.1601398284,
                                                                            377164.81147217273,
                                                                            553731.6133019166,
                                                                            783344.3127471181,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŧǍˣĩӐХԘɨɯƈҍ\x93БɑʍӴįŀÖѼ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.120159:+0000',
                                                                            '20210228:024615.120187:+0000',
                                                                            '20210228:024615.120205:+0000',
                                                                            '20210228:024615.120222:+0000',
                                                                            '20210228:024615.120238:+0000',
                                                                            '20210228:024615.120254:+0000',
                                                                            '20210228:024615.120270:+0000',
                                                                            '20210228:024615.120286:+0000',
                                                                            '20210228:024615.120302:+0000',
                                                                            '20210228:024615.120318:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Τҵʠǒ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.120773:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Фзʼ|ҕȄӛϙΟӾҭώʟ¦ǷˣÌȲъoŘÞӾɧȭ;ʓѻǋõ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҝώʢɡɠӛҮ2ЄʮˁѪȱǩ˥ϬҕѵȌ\u0379ІΪɖЬԡΝˠG%~',
                                                                            'ȏςuʻ¼»ɠΝʀqћҨ\u0383ýĒˎѷϒΖȣϒʺѡӄéЯҞǠʇҎ',
                                                                            'ЁӏϪϑ҉ЋŉśѭĚΗˇӻɫ¸ҁ˺ʚϦČÌЙêǫlǌÅϫ\u038bƒ',
                                                                            'ÙƑóqAӴȧǸǏљȋѣǒȕӣʃǢѝԟӠʽÄ±ԗǠȟơÍĉˎ',
                                                                            'җӲę7ǫЇәȃËӻnȧǦӟͽіӈЬɉǼ3YԌϞԋΚÉȏύ˺',
                                                                            'ƢԄѮĬ\x8aέęΤºЫĆrfȞҠǎΚĸGţƖȳɻǢŘſϾɕšZ',
                                                                            'Κя·úӞĝǪӪɂ*ćΝΑ ÿǌБʞǅ\x95ӢɸΉɦÎԝΏ\x8dˠѶ',
                                                                            'v\x8b˱ÂíТŅɷĕŘAȋŸŽзŖҀƱƝ#çĘӨưӲԬӓРA˽',
                                                                            'Ҹƪ˺ȹKǔ´\x80Ý®ӓІÅȚҦĖӼѩМȬŻʸxʲ}˛ɦƟӾƛ',
                                                                            'ЪɡƱән˃ǨĈͲ˴óҁƊJϷ£ҺÙоǚҏ3ĦԢѩѹƥƒ\x9fν',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͽȓκЖҸſLґΡϧŜ\x9bǨԡüǪҁʞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6551584013226749020,
                                                                            -5077932773368623782,
                                                                            -6789987119433578301,
                                                                            2101244118966044080,
                                                                            -369000251892519859,
                                                                            -4375548788860172793,
                                                                            8078925225148902937,
                                                                            7612638867684170754,
                                                                            -5689486068728011643,
                                                                            -3348556174302841709,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ȃ]ϘћɅ\x8fƃĳǂȀǹɤм˞YЦ',
                    'message': "ʆʾ˞Hƣ\x81'ȎşJzχſΑѷѕŻУӔȼĹǩƪυƅ\x90ъŮŐΫ",
                    'arguments': [
                            {
                                        'name': 'ăѹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӟ˜Ƙ}цŶũɬϲƩјϊτǉԮКԎëЖϤǠĸӿѺȅ(Đԥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.123554:+0000',
                                                                            '20210228:024615.123583:+0000',
                                                                            '20210228:024615.123593:+0000',
                                                                            '20210228:024615.123601:+0000',
                                                                            '20210228:024615.123608:+0000',
                                                                            '20210228:024615.123616:+0000',
                                                                            '20210228:024615.123623:+0000',
                                                                            '20210228:024615.123630:+0000',
                                                                            '20210228:024615.123636:+0000',
                                                                            '20210228:024615.123643:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƳκmјєÉ҃ɡƆRŦ˾ͺͳӼɾŇБԭКÁƹɒ³ͱı΄ʜÁΝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.123953:+0000',
                                                    },
                                    },
                            {
                                        'name': 'rŢгŕқŦћǝˇϧĂ«\x9bƟBЅҧùè',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˉʆ¼ʔśŻˎĩʏԍƞό«ǁĉӉÝөҬɒɎʯζʯʗëƦ\x85˅Ǭ',
                                                    },
                                    },
                            {
                                        'name': 'иҒĢҲ/ĳȣ[ˬΨўɠǇг)ų˔ӼʰθΘɪЯLЮҎƫ,\x9bԎ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -770565396947880129,
                                                                            -1329284312596023718,
                                                                            2237057353530388935,
                                                                            -8003149032626842583,
                                                                            171032553873394417,
                                                                            -5530859823127720542,
                                                                            -1797240021373870311,
                                                                            -5080627500549863222,
                                                                            -2703756912307967134,
                                                                            1865246433128418308,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҥ\u0378ƂhİǻЎɘȿСȭӟ\x8aЛ˚ɜө£ʱ=ȖԃҟӃT\x96˹ŏ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɝŶƊñƥžȺƞљƀºӈFʉӔΞßȚ\x8eɇэўζУџИοήýû',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8381912663985400275,
                                                    },
                                    },
                            {
                                        'name': '϶ŞƏǭŶʉzͿΌҐQҟƳŏӏǢēҨϚźʋНӥϰȤPӠ3\xa0Ȓ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'řV',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6242992463103054682,
                                                    },
                                    },
                            {
                                        'name': 'ҭ\x83ʻSƗѿȳŪľ2ӏɌҡ\x86Ǹ\x8fəϐВԩ\x8eӠҸoўńȱϭӗԝ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5862307558851846274,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҼƷÙƝˣĞɍÇʙϽŃʢˌ\u0383ӝ¿ϿùʉŬϲå_Óǡ{ԤȏȤɯ',
                    'message': 'ӀȟѣŹϟǑƃӬҟζԅwǦȖÒϽ·QДˁȥͰ\u03a2ɶҪиΗƒƵ~',
                    'arguments': [
                            {
                                        'name': 'Χǜϐ˼ĀuEР³ιɊɽйóʭҟԒӛԔɶɫTШMɝМˌƚɆͺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5533913846181704284,
                                                                            467196446749538362,
                                                                            2794784213062395704,
                                                                            -7324682050592919541,
                                                                            1137375675284821580,
                                                                            3380174621368103139,
                                                                            3107765904929924511,
                                                                            918454642548051983,
                                                                            -3931318143686809841,
                                                                            1483490203863940615,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӄԊѲ"ĿˎĿƪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            555794.894536353,
                                                                            690429.4280532672,
                                                                            620106.909314803,
                                                                            479463.48380444094,
                                                                            240127.0209856967,
                                                                            566791.2575500292,
                                                                            535402.2297020635,
                                                                            761493.4430635774,
                                                                            287931.20618806663,
                                                                            -33884.21602309651,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǒ˾ˑǹɥҚ\x8fΜԊʻӬŲ]ρ¤ŻХҩæƘđϳĩ҅ЖԧЦλ².',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3622444537551973093,
                                                    },
                                    },
                            {
                                        'name': 'Ыhęƨμ\u0378ĲǣțˉћĐ~ĈВЦƹҎȘʃęʡФόʽКѢӚ\x98˂',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ØЙƢӥϲŴЂˠº]ǍϷzBlɌԏ˯\u0379ŒɷȠҚȭЎĿ\x9cǃƕD',
                                                                            'Ü˕Φϑ˞\x8dƯΧǖūҪÊÉқ´ҭϗá"ƑțԊxɟΦћϡvʝϾ',
                                                                            '\xadԊːLɢB\x95ĦÃǻѷȦМ¡ªƩӄ˳ϧӥƄƤŵƻϯ҇ʕԌƾͷ',
                                                                            'ȗϺӢJ]ƔԪЦԅРȞњӔ\x9cȡÍѶΑˤ.ɘ˂ˋiμΚǄΰĦ¬',
                                                                            'ʈӘжϼӛ˳ΈБǩˉȖƹyώ\x9dă˨Ĉң\u0382ĲŖģќȿɅюȯөƉ',
                                                                            'ʤγϋͶкȇ΄њɀѳÇūϡΉ\x93ѐɩЬЮšÊѲ+}ҁģӮȁƛн',
                                                                            'ǝϬŔĺˏ\x98ʘ)Μ˲үѢìχЬ˦ԢВȨѠxȿɴ˨\x8bҀɮ\x86ҡǠ',
                                                                            'ӖΞƘÌȮ\u0378Ӈ:ǿʤŽϷɠŊѦӳˆLg\x8eǈƼɒжƳӐШÏģҌ',
                                                                            'ӂһҹʥЮƬІӐΈϯӵі˘ˢ҇ԫȃɊ?˜@ѤҝиͼµπÐӶċ',
                                                                            'ƋŒɁˮɢ\x89sͶÿЄӮ\u0381IЅƮƧfŮŬŉЏȥdȅƻНЁōдĜ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĔӐ4ϩɃ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5045087920429280637,
                                                                            1286543672048060678,
                                                                            7923603783203212560,
                                                                            3841526716175548223,
                                                                            -1180433104904975569,
                                                                            -7022941931205689401,
                                                                            -4630252843761600606,
                                                                            -2338830646757903284,
                                                                            2074367974798427733,
                                                                            -1518808698847203879,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'чҨĻΟëǵÙŖaҘ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǴɥҤ-àԩВ\x92ΰ˽Έ|ƕӂ(ѫЌ˩ɟƨиёƋ¯ɢſÒӊĉ#',
                                                                            'ƷǌәңņӛưЯʴˠǗ-Ύï%ĉйȲӤ\x98Ĉ\x80Ѹ*Ӣϕɝsҽю',
                                                                            'ǐвАԘȂƐˬj§ƴѷƫѤζɜɌơº&ôí\xa0¢ѦʕƇÔsƧó',
                                                                            'Ԫ҉ǉԫņőqŌŨɞƯԜʴӯӼǑϣȓӼĴМµĭԠeǋԎĊşǙ',
                                                                            'ояζ\x8bƣϋ3ιͺˋ½˄NǑԞ˜Ǘ˫żɩԡâʠâǑӆԔίűĻ',
                                                                            'Нҁѡ\u0382ɴǿÐӿǔҋʖřԛя˫úƷŞϭȘɤΫɧÊȞøЩˮ˫О',
                                                                            'ϯŘȴʃˢερɩ˂еŅn}ϖ-ǄҠԗťƵàȩʞӁӜĹĽīљʏ',
                                                                            'ĸ˧ӯĒ\xadŶҨʌϗ\x88ųřƨďҦqœ΅өȖɷÔ(ζіǔŌΆһҽ',
                                                                            'ɍèĿȍѢ¢q˗ƺң\x9eWaϥ˜ΐͶâʏΈÏȹaɞ˅ӱΎɼӲ\x88',
                                                                            '»ȔϴʲĨҗĒӃ;ǇҙFΆɛЭąԊɇѹĘŲџњβĘ³ԈіΨɠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϔ\x94˾:˼҃ήZƵǁҋͻ˹"˅УʿϮο',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'āˊϔΙwǿ/Ԕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': ' ʀеԜ£рӌlϺƶɶпzѝνӅєɗǅеɀҞˬФԧǪɯ˭ѕҒ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҕȲˍҐŷнRǾ¥˩ЈѺɬЀŒʁΒҸÌŕԏѤĭƳşϋ҃YЯǘ',
                                                    },
                                    },
                            {
                                        'name': 'ҫɘðҫ{ƟЫɈѐЉāҠășǤȠϟ\x91с£ùŀяԞÍƖưǘϋ\x8a',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -819920311305907440,
                                                                            -608654818157992926,
                                                                            637941428789827990,
                                                                            -1904292370433414752,
                                                                            -2167929182907284626,
                                                                            -9062159529552022018,
                                                                            8491123942256656387,
                                                                            2984380680279105689,
                                                                            -4876082978094681377,
                                                                            6893715240135424592,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӱɪƎ˟ȍԒ˅ңԄϰқȻ\u0379ҔԋԜԇǻӧēͷ˯ƪӆéêɀԫΘΔ',
                    'message': 'χĴҽвâAӉ\x94ӏ˧ʬʓͳˡėȑѪҷЭǻԉ¶ʇȀиē\x8aǁұĽ',
                    'arguments': [
                            {
                                        'name': 'ӫŏUŜ#\u0381ʺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Φ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'cºƞɑǋëʜʆŮ·ӑŖͿЕʰԔԥ}ʴҹȺΪöқƇΈϢɼ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.129154:+0000',
                                                    },
                                    },
                            {
                                        'name': '˹Σ>ŘҽчƁѢѦǷѶŕȞԀVoÁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɭФƾ\x86αͰұέXӐːƚĤώƲǵXӵƾǒ\u038bϷӎ\x88',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.129472:+0000',
                                                    },
                                    },
                            {
                                        'name': 'dɔŭʛ˩oɒɪӲτöУδѼͱ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210228:024615.129614:+0000',
                                                                            '20210228:024615.129625:+0000',
                                                                            '20210228:024615.129633:+0000',
                                                                            '20210228:024615.129640:+0000',
                                                                            '20210228:024615.129646:+0000',
                                                                            '20210228:024615.129652:+0000',
                                                                            '20210228:024615.129658:+0000',
                                                                            '20210228:024615.129664:+0000',
                                                                            '20210228:024615.129670:+0000',
                                                                            '20210228:024615.129676:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ìԔǄǎЫ\x96҉\u038dϐћ·ȆȸВӑɚŔȿȳʘА¬Қ˞ҪТȪʛBК',
                    'message': 'ԟњКŞÕˀϥ˪τʟƭ\u03a2ˌŉΐƮƱѳɓΥ·˃ɱԗD]Ԕ\u0382ҭǸ',
                    'arguments': [
                            {
                                        'name': 'ǉĺјέʯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 429924.7931806982,
                                                    },
                                    },
                            {
                                        'name': 'Ǡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ҳǐ\u038bԫłӐ˾ʱƛÇɏ˲ԄίϮʋƭŒ¦ęǊ\x80ƚbБϵˉԊȵĹ',
                                                                            'ҼüzʎŶεMΑÂá\x8cҺ˖ʭŵцǓ\x9bΦåϝΛ˷ԞĆΓÂʢɝ\x84',
                                                                            'ԡшʾļʵҶˡû\u0381Á¶ѿѕ˖§\x7f;ϫ¼ѿɹɳÆˍ{RΙǏԌ\u0381',
                                                                            'ѓąʎɴǚǦҶϜǔūĀѐΤȚ҇ҏҘYČ~àȺĭȈѸdʩXɘ½',
                                                                            'ΤĿl¨Ԏ˗øцȫϐʹӳӚʅδҢԟ@Ϸ¾˜ʏ˂ʴЀƾҝ\x8bϨŁ',
                                                                            "ĊCɩÄϥȼȩηVҙǌǦРԍȑį'ɤ¶ԂǂυȠӖмcϫȫГҡ",
                                                                            'ˎʠɴȔТȯѯӼцɫ˷Єʺéìӳnļģ҉җ7˦\u038bʾȡǠԮȚӥ',
                                                                            'ɡ5Ԣɣ÷ɕ~çцζɢRƓ·Ōѭяõ˵ΈǮԨфȄϓψˎԅάР',
                                                                            'ӕпȭ˅Ψ\x8eƧӺőλȃȮ˄ƺΝȾϒʪɊÍСũȋ\u038bľȪқǭÕÈ',
                                                                            'zĴҮƙҨ¬ʑɗˀƙĄĠҲ~вÚ}ԇ#ӨΏˀΕӉũϐ&ΖέΚ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѵ¿ǯϻЁ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ЈϰŉɏҺɷȖʓЊѶϤśǾͷΘ«',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210228:024615.130867:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĪӡгԆ}Σ7ɊŶˇͼĵđ¼EϙȗɡˡɪíͿȨɢAʟ;nӧӢ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3792616774993275515,
                                                                            2176624694317329000,
                                                                            -1219692730675220020,
                                                                            -82513444010050937,
                                                                            2963520718335465875,
                                                                            1807166158187649200,
                                                                            -5412583399945994429,
                                                                            241762831718205474,
                                                                            2259324669699581237,
                                                                            1936927455839609050,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǿӎ2ԡЅɻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            280707.25825815584,
                                                                            110281.05102238382,
                                                                            703377.2974668423,
                                                                            967633.6375241699,
                                                                            345630.31058877514,
                                                                            829923.8696038361,
                                                                            826775.974143784,
                                                                            745212.3661968232,
                                                                            393544.6643499881,
                                                                            3981.6221500798565,
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

            'identifier': 'ŴOΤ\x8aΰ',

            'categories': [
                'internal',
            ],

            'messages': [
                {
                    'catalog': 'ѥʲ',
                    'message': 'ſ',
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
            'request_id': 5969700,
            'error': {
                'identifier': 'ʼӥӑʠĴϮǡŧĻĢЇʫӾέˎƮγfʁ\x9aΡȢɱˀѬ·ԧ˂Yϴ',
                'categories': [
                    'access-restriction',
                    'access-restriction',
                    'configuration',
                    'invalid-user-action',
                    'internal',
                    'file',
                    'os',
                    'os',
                    'internal',
                    'network',
                ],
                'source': 'ϱѪƙжъUt$ǔW˓ӜѥʋΎƤφҺйɥ>ʻӔ+ɃαĽɉѤЧ',
                'messages': [
                    {
                            'catalog': 'Ύ÷ϫūŃǷӻǞϒĂҼdю\u038dҠ9ΪˇXӳ\x84¬=÷ѾƇμƜĽU',
                            'message': 'ˮǄ×ӺϑƧYαǪКŶɨ\x95\x96ЎȽԨ\x86Ϥƈ|ҫ¥oęΑȃѲľμ',
                            'arguments': [
                                        {
                                                        'name': 'ԫΔϒԖφ{ɐļʛ·Ǫҩұ\x9dʌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӏϯ\x9dзȟΦ~ĵѷÕŌϙćǣИ®ϊυȗæϙӖĿΧÎѮƦϩ\xadϤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԁʢŀ¡\x8fŀ|У҃ӃŞΤәȕʞǏƑøȔωвғʑđǄόѿȌǿȾ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǛϠYЉ\\º·\u038dʹőΏɝǔÉǮ}ԟɛćAΆ;ǻúȶǂʟѡЕȊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÜȤé¼{l÷Й4ȰʐӷȆ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ļɀ°ԓíɼѳѫJȬŔԏ\x95șŞĥ˓ĢŤĥ³oʳ>О¾ʅˆѯÄ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024615.054339:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¬үЬΡΎϜӇЦ-=ѣҦ˗ϙƵØϥĘqʔȆË˽ĈйӁƲɌU',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8261684094790181645,
                                                                        },
                                                    },
                                        {
                                                        'name': '¬Ò¾Ӡɠ2NӋĺϑĕƒδзҏŰβ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈТӾԭ«ȽˉīĞӂҒϑ>ǯҰŌңԍˡ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĚКǉ^ǁƇʔÿȯԨƈҽĎӨǤùJɗ\u03a2ͱǩ\x7fŉ˴ηâΠ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǿӯßāԌĊԭʗe\x96ǂŘϽɸӈÓыkɧӮɞáӶ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʎԚĹȹǈӞїƺʏʕcҕ³ʷƣeǤŽ\x9baƠ\x9bӴσeзԄԨɎ½',
                            'message': 'ŨʲҼˀϫǛЋôԀҸû˶ɰϗ\x84ƶ\x99ǝ˓ĽʛʵˑN\x91Ǹǵȵ}˱',
                            'arguments': [
                                        {
                                                        'name': 'ǒςή¬вѡ;ƻȩ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3221260038842555012,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɀӦЫö{ϱɌɖ-Ǡ˕ʔĖƂȽƸǫĞÍʊüČȅǒάΝҟ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ſ\x87Ȓ˰Ҍɕϧ˟"ɫҞԃҵPŁɕёĒ½ÎǉѐώùŶɓзƗσƶ',
                                                                        },
                                                    },
                                        {
                                                        'name': '1˫ȣДʕ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͷ*ԉǬǥӶǂƿęʼĹӈ\x94cŚʻпÅԓ¾ˍҍʼ)˘ΨǛĺ\x94ȏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϦΠ,\x95ȍШÇȭŷƯǢϚϱΉʂȿƝҨϱɴΪԨ1¡ѺͻĚѭʺO',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -95695.69904814655,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЪfƙѬȩϏ\u0379ɹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6275483294847666667,
                                                                        },
                                                    },
                                        {
                                                        'name': 'υʑɶÁ˚ɝĕǠǊȍ|ɺpūҸ¸ҺăӌτǻʺʘψϷӹˠ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ĕµ\x92ȺʴÜǷ>ȉ4әϮ\u0380οҷɹÔ¤ĐШưӑȟҫ5ʔDȚӿǴ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʚǎέԪԆπ·ѭѸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 295666.8946277122,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĞǬΖͳ¢\xadԬȶԕˌ҇ŝ5ǷȋʧŕíϗȻΔԟŷɾƜюËҕſ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'èԁäīӱщНįƑҳӃϐŀÕԖǈ¿ӍӄȝČĩPмſЙŮƤκЅ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϧǱƦĿωςԃʿċϗƂÐĒҐΏɰȬϹː.ęȰӪ!ɳ\u0383αϢɥж',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԡʛѤͷɷǮǹǍ˹˄ȍ\x9aѹґӕԔ˸ŶѸïʷϯӗ×ĹѤ\u0378ȵʢƽ',
                            'message': 'ΗϭԞ.ǝRѥϤȦɦƐ˔ǅϺӽʕäǍđůȏƙÅдӴąяÅ˼ɹ',
                            'arguments': [
                                        {
                                                        'name': 'ԎІƨʂΔѝɀ7ǝԢ|ÒưÜʪѡ\x8cеЇŰљóĩʲъÒӭøÒϕ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʓ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϖȦ¿<ûüӋƎȍиǿӌƊõοȭ҂',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȠÌУчԃˤǘšǚԡď˷ҚÊɒБôƃʚZȲһ\u038bΖгТˎ\\',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǜʌ\u0378=ЈхˈϭɟʾʨҤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3082368628469893586,
                                                                        },
                                                    },
                                        {
                                                        'name': 'εnªӞм¤ԕϹЧБȠҦſΑOņɴÌΩǎʐНʄʻǎƗӷӺ\x82Ø',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024615.059038:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѺƖϺҮroưǊǸԍЋХэʺɡͰǙҧÁɻ:Ş\x88ƯȹÒԞˑҫЋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -92237.75741398286,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĪßƳ¨ƞfЭĒ¨ǀ±҃łƐʟ\x9fĥȱo',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴϣŶɬʗȺÓÅӠΪƧn\x9aњλƭӵΠˎΔ\u0378ȊŝСŽɼґȇȬ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7328146391305156281,
                                                                        },
                                                    },
                                        {
                                                        'name': '%ȆϬǪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƒЏ˶n˴ӣăԁͷÉѿ˹ȦʴωƞɒӐ˖ǜςʔѺêɇϝѐУϽǡ',
                            'message': 'ˑʤԢ\x80ΦĆ҄вӓ˓ĸȍĻ:v<ΊԊԗ˞ϗήɩƯҺЁǧˠϭǔ',
                            'arguments': [
                                        {
                                                        'name': 'ǙΩǔЮÔ˳ͲǛ§ĿӯͷſяȗͻȖα\x8bʴ˂ɩӐƓűď¢¹Ů\x8d',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024615.061396:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'űP\x89ϊʸͽӥʶ˶ðзԗRǅ\x88ӪɌĖȲϟξ˓\x88ί˃ѦƈƂ\u0381Й',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5701592381014811226,
                                                                        },
                                                    },
                                        {
                                                        'name': '҆µʔӃ@lϴ˟ɘ-',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҩΛƩǿ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȿ\u0379њȀҵ\x86CƍɇɎ[óʤϧɥïƧŗ˽ϸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǁʮͼВ˰ϥʲ®τw\u0383$шʂx,ė˳ɒȸ\u038bѢ\u0378lſӥsƹ¬Ӥ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˻ʤςѧXǨʌčѰϦ;¾Ϭ4îA]˅ďšѮǂǝѥŲϢǕԓѐï',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĈŨƐȯҙľ;Ûм˚г˧цţϳіĤѩ:Сĳњ҄\x97ʷЊԕѾɧ³',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'һҽӉМǚńʞÆƕ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024615.063083:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȫ3ĀŢЮʘϋ÷ɗѮɥͰʽɍԖ˖ʲm¯ԦГȜĳŨ˄ѝΪπǁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Г˚Лđ\x80ҒəБϯӱŒ˰ƪЙ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˁȿì˭ǘϊќԎҐ˔ӡșũҙg҉\x9cρѝÅќơŉʼŚɒƾǞӼȯ',
                            'message': 'ɬåˋѶƻŴЌϸϞmѥÛҳΞPϴǑӷɁϭƌ\x82\x86ӕĻǘǡƛˤÛ',
                            'arguments': [
                                        {
                                                        'name': 'ҭĮʾЅΙҸȜ\u0381ÑҐŀƩӀΝʊҘҌɠԣC\u038bɾ\x8fЖүÉ˰ͽȲƁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 684088.2026270432,
                                                                        },
                                                    },
                                        {
                                                        'name': '£ϕҺŀô\x9e5ǽӍЊϡԎ"',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȶȣƥÀԤǫӍ\x89Ɉɷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝʗҋȚѕϫȮ¤ΞƎЂȭԬщʖɸγ\x80ǇњϏɬ˰ӑǋ¢Ũ҈Ӻǥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ђώ2βÌáɲǹȷǦę˫ӵ´ΛΉǆΨΈŎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҕғО\x8bʖġÎɠTȊʮɦĪ˩БҚǐҀƻƍ\x9bѿ?ΏӞίѭFӕҞ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˔\x98ұϭ Ç',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċъÀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔąʗҁ\u0380ʃƖé\x86ɽԆȔҊǏåþɣȟ²ӥ\x8b',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΨˑSðƿƷƌrɒҾʹӴϋͼøƎŴҝƬѧ5ɊѾǗѯϦРʹӫѱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьʟӹ\x8aӟ˵ԮŌȯl',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 377430.83427343954,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ȓK˪8ѴňɃ°ɩΑɬßЇ±ÜӝԈ=ǭЕɞɺ.\x97"ц¼ϴӹǲ',
                            'message': "ȼţ˦ˎĥĺ\u03a2ʮύàϋːìŜȢҶŘɀƝӌĿîS\\Ҵ¡ӡΓƍ'",
                            'arguments': [
                                        {
                                                        'name': 'ύʖЭªŅƢә<чϨųԠĢăςρÐν˅·ǟ\x8b\x8dԗ\\',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԡšрƨͿѴ˖ѲԌʨȭXӅЫӉj%ΧǹЯPϷøΐʨĘɉɂʄň',
                                                                        },
                                                    },
                                        {
                                                        'name': 'гĩ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŜУF\x97Ѡ\u03a2ɱԨƚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅґҪƶáˡəȑjȼǊǘƎχʳ˖ůpёԒÂԇƵŪ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'åWŸђ\x9cξ5ɌʘͰÿͷͳƤӶqνĂѾ:\x91ÚɠȮЏʙɞ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'гůɞ˫_ĐˠfG˟˦ҦkčοҴуͻ>¹¹\x99',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 282474702781326116,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºΏ ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'θσĕтŴԗϛʰ\xa0ȇҲҗԍAԊˬʷХӯԈfӪ\x83\x9eɬǰҍԈϏǁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ó',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӓϮʽжßЩɹфΧґϪŴ\x7fӁӻϳЅϺ{ӕҚϾ&śγʝԗΑƱ\x8b',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſǗЇkφʺĎӓț˼ԇİȈÒŨâɀɽ˼Ќ˒ΫȩϵȗɘѠԧȪғ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024615.072150:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɇҷΙқ-ɅȘ',
                            'message': 'Ε\x8aӞӊŦԄǠʛYӜĐYЗϝʏҰЂɿСѯǊɁӷĿәͶʵȧűB',
                            'arguments': [
                                        {
                                                        'name': 'ҒҠ\x8dԦ΅ҪԒӹɑſ˩ɢηȋгзɋƔȬõ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʲ¹ˋĚΚ ½φҞӻԭӰŷCøʶůȑȘхͰÉCѿČξ6Ӡųe',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΨӹŐԧßƻЦȨҺ\u0380ƻӠԤ£\x83ˍԄґѿŨԗÂĐҌЗХáҾТʺ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѩӈ8Ɣ£wΛЕ\x9cɐę¦',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƵŀŻґԗȚϨƺϱęȭ\x8eҹʕǠӉϷҗ¤ˎβФҥĝ\x94',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1650248329879349432,
                                                                        },
                                                    },
                                        {
                                                        'name': ',ΝɏʢǥƔ<ûȰξЃҼɮϕ҂мȇƖӻžύE¡ʂЮϵšѹâˋ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˄<҃Ȱȑ5ωҒѓɾ˩Åы˔ԅɘӇ8ŧѣĞҴӉ˾ǸӁΉƂÓ\u0381',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ũǀσƏԅԕĊӔИɄϿПòϚ¨¿ά҂Ρ1җȷŠAäwʠԉѭʹ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210228:024615.075807:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˦>ˮeĵÒҳȓĩ˟ņƵ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӕ˪\x8dˑˢĠɠȅ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 17200.51441221386,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˢN§ćчˣȣ#ϗĜŅӒÇҔʾǠǋȇʄϰǢїŉӕĐâ¹ӳʙҨ',
                            'message': 'I҈Ȥ\x82ȀǵҮЦƗǝˁȴФϲˍĒйςǫæώϡтʏ\x8c\x8aţˑ҅Æ',
                            'arguments': [
                                        {
                                                        'name': 'ϙȂGÆүʪљôʪЁÔыƙǹųɟТӘʚԀ)Ύ҃Cȿ˯ŷɊ\x93Ó',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʷď˨ѵʑ¤ϸϾɡρ\x9dŵȴϳƓˊԠő³ʵʊίÍқȴǅЦ¤ÊÇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳɱNц3ʜSϚ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѢŴBҥôǓ\u0381ԛáŚÙƇҁeĶΩǇ¤ѬǾηȖҷҘ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŦFϒ¡Ƹʹƌ#ĞÈʇ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЂŗѝCƃλȒъ»ӿеЮһ=ƻǊä˯˃ԧ\x87ҟыҗ\x84ϭĢ˻Ʈԛ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '9ԝΩаŝϿҴɠȐʥ\u0382àǍ¼ʑǴ4ǯbĩЎȪЌ¾ЕӻŇʠүˡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÒӾŴȳ¤Ѣ(ˎNϭ[ɤÞúϧͲΟѾʥюρʠΜϻǵЌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔˠʼǊȕúûйȀċǴƞVԐ\xa09ƮӖ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёʲҭ˛ʼЉπßƪȉƊǶ\u0383˽ãʥŷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĉʈúѧĄɡЎúʗ_ӏԃΗсЮΛ\x9eʧéǵǝȸɞŏɤΨ²ʻӠĘ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˔Ԓѵӽ ǒϦJ˾\x8bӓʯĸϨȢƺόǇʨĎΕůҪ˓ʗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 177384.13009614655,
                                                                        },
                                                    },
                                        {
                                                        'name': '~сϭuąϙԭԢĆԙϨͿſɱį¿ʶωӺżԤƠǑèқpӰQʑǓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5727539276248838358,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ӕʬȉ\x9cԫˣƵЏÍѣϡΠ@\x92œ\x97ГξѮԋԊÄĨӂӱĀ÷±ӔП',
                            'message': 'ĔЖƬ·ҨϢәԫ\x9bɟŎЭʹ\x86љЉȀˮӻƆϒ˘Ķ˰ĭň"ϸӵ\x91',
                            'arguments': [
                                        {
                                                        'name': 'ĠǨϣ˪eʹӇЩŋĆϩԤʣуÿAʛȺ#ǷͰ8ҁӝгÝƘӲɱš',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΗâƶzЀāːɵșÓđq˄Ҕ¤˽˓ЋӵͰұ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ýƈьҰɤŲŸrÐйǟ˟ҾʢԟҡӤÜӀǍ˴ζϏƷͺôh\x84ƂM',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŜѼĜӨҫ˃Αғ\x90ѢƵȚӰȴ\x89\u0382āĵѻĵǓ¡ԇʄ˹ȡ\x98qηϽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Φj7ȸÃкũӽԍǼċϺ|ШԋǼǶˉˮɺν',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5287069583474636106,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80˩҈ƯõAԖθΩД+ÃȇҠȖѶů',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɍ\\ČςїȽŕǀκϾǃάӎŬěΡǡΩƪˍ˫ͲΖɔqѸ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȧђ\u03a2ϢЗȖ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ĺĉ,ƤŸʺȺħěɰҍԣѕФϷѾŸӢ<ȈȻΩ)ȳΐˋϒɂϧӷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѤҢ\x95$ĉӖфԡσ˙ѩʻȋ˄ŜҤ˹¾ŤľѶġҎɂ|ʇӘčʳл',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĎɪȒ;ę$ǄŮϗȬʊɡ-¼˸љ3±"ȋRҿǢǽҴ9zɆ\u0381Ӛ',
                            'message': 'ɳѻжYɽȲѻƫİƵԣʓiӣȡƐǕƘѕєпĔňʘҨҽæѣǯ®',
                            'arguments': [
                                        {
                                                        'name': 'ɣȹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ȓ©ŨɫɅĮѧ˧Ƀҋʌ·ʠ±˪əǭʬVÁɯѝċʚĥƻñīˠ\x85',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕԞзķ*\x9fә˰ůɈϿċ˛eˌҏШ\x8dӛƂή\u0378γƪӎѮ\x7fǭŭć',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ͱпɚԗӂ\x88ΘʕȰ˲ęɵèŻˋȭ˖ŷβɂ˓Ҕȿϵ\u0382ȜƭɎɿʽ',
                                                                        },
                                                    },
                                        {
                                                        'name': ' ǳĮԦҥǤӧŐʳįɽЀyÓǣǲҘɫѨʞKS˄\x90óƥĚ\u0380ɼÄ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '΄Ȳˠʖǧĥ\u0379ƴӍéӧͱͻƒƂǞɤҔřȞԕƱɃʥɕѦ/Ɛӝq',
                                                                        },
                                                    },
                                        {
                                                        'name': "ɞҬź<ҩ'ǨΣ˗ϩə˪ӬγɐǦӆÈȡǛyǐ\x90OÅТ\xadaѥõ",
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 912873.0049985716,
                                                                        },
                                                    },
                                        {
                                                        'name': '҃ҀýŤҲʢλĚŰȰňþы˯=Ѩʋʰ\x96ª˳ƂΫηù\x8fĞŭɅÁ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 800770554585669465,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜ˾ЮʥԊϳːηΚҌ\x89ґԧҸĸ\x9aфɿҷЭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ľ˺mӉǫұϻ˦\u038bλnԏŠТƸÛĚƪ҃ΝΟУ\x93ӊɫƕŴɰç\x84',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 783047215009267112,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ξƔÔįĶԚωӘƞЛz˛ȵƞψΐǻ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԣ¹',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2745059507999194720,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʃÜŴǹʙńѲȼӟƽ¤ƤǳŐĸćŦɰӷ\x84ҍͷ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
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

            'request_id': 70752,

            'error': {
                'identifier': 'ɡ~Ȉ»ż',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': '\x84ɠ',
                            'message': 'ʒ',
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
            'nw_x_pixel': 781769371,
            'nw_y_pixel': -783175365,
            'width': -5652983833453122598,
            'height': -4765186925220320370,
            'ratio_x': 1196949298203265811,
            'ratio_y': 7595521282185431825,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -691581283,

            'nw_y_pixel': 1859609348,

            'width': -1618329670455428497,

            'height': -5082924743723559440,

            'ratio_x': -4369168223350947778,

            'ratio_y': 4530013412710662436,

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
                    'nw_x_pixel': 1129973341,
                    'nw_y_pixel': -1503400425,
                    'width': -7322462642070698074,
                    'height': -6957594293124499637,
                    'ratio_x': -414436207720615052,
                    'ratio_y': -5982593444183069081,
                },
                {
                    'nw_x_pixel': -531655487,
                    'nw_y_pixel': -1126694541,
                    'width': -1279890087638332969,
                    'height': -6364778829454434174,
                    'ratio_x': 8941002452414362191,
                    'ratio_y': -1143364649153278644,
                },
                {
                    'nw_x_pixel': -1582678311,
                    'nw_y_pixel': 1955375880,
                    'width': -1434181606584295421,
                    'height': -3012963400178246464,
                    'ratio_x': -926155163202079731,
                    'ratio_y': -8425093883423614137,
                },
                {
                    'nw_x_pixel': 1778859974,
                    'nw_y_pixel': 588685065,
                    'width': -28680065166690429,
                    'height': -4625668771501063561,
                    'ratio_x': -7177799551717993086,
                    'ratio_y': -7856114288688984940,
                },
                {
                    'nw_x_pixel': -1178451096,
                    'nw_y_pixel': -1320530897,
                    'width': -6687778491968597229,
                    'height': -8442506777510095174,
                    'ratio_x': 7151575861413374109,
                    'ratio_y': -191988421567196421,
                },
                {
                    'nw_x_pixel': -817682943,
                    'nw_y_pixel': 261048756,
                    'width': -3544338816068486150,
                    'height': -6681603149627112870,
                    'ratio_x': 701029398497651501,
                    'ratio_y': -6684549984678350281,
                },
                {
                    'nw_x_pixel': 1317818802,
                    'nw_y_pixel': 1140885548,
                    'width': -9159352407412235768,
                    'height': -3768017825406010581,
                    'ratio_x': 7850235633858695682,
                    'ratio_y': 8564410448057296558,
                },
                {
                    'nw_x_pixel': -1287312633,
                    'nw_y_pixel': -1684384230,
                    'width': -6303324148229740897,
                    'height': -8955961566862610453,
                    'ratio_x': -1202040020898468474,
                    'ratio_y': 2596453987678651340,
                },
                {
                    'nw_x_pixel': 698963331,
                    'nw_y_pixel': -1106763608,
                    'width': -7449498277110798539,
                    'height': -3241731640633228189,
                    'ratio_x': 8328082038109899818,
                    'ratio_y': 416418591142109734,
                },
                {
                    'nw_x_pixel': 254629327,
                    'nw_y_pixel': 870959652,
                    'width': -119437589819658907,
                    'height': -2165399333789495223,
                    'ratio_x': 8534918188209573386,
                    'ratio_y': 1432685457125272370,
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
