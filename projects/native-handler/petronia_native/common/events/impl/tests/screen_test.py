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
            'identifier': 4464753,
            'width': 7722286626460001002,
            'height': -2433791469855032825,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 7155690,

            'width': 1280110619040101752,

            'height': -5945862695921639065,

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
            'source_monitor': 6949449,
            'source_nw_x_pixel': -7959354325807487791,
            'source_nw_y_pixel': -2753772042394749043,
            'source_pixel_width': -4159920546986303252,
            'source_pixel_height': -8370322695048915769,
            'rotation': -6948918320389893506,
            'virtual_nw_x_pixel': -932454175,
            'virtual_nw_y_pixel': 1241081835,
            'virtual_width': -1734094578,
            'virtual_height': 214377772,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -8639404338588110200,

            'source_nw_y_pixel': -2380191861814469939,

            'source_pixel_width': -3058030557537146929,

            'source_pixel_height': -6801569691824151888,

            'rotation': -2689989790517021692,

            'virtual_nw_x_pixel': 964913455,

            'virtual_nw_y_pixel': 1078570621,

            'virtual_width': 1827039833,

            'virtual_height': -902583129,

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
            'description': 'ӼоɃʽͷĖəʏϕĝ˚\x97ʪπÛȾ˩ǖԜ:ӖбˬŁɘvǴѵӻч',
            'monitors': [
                {
                    'identifier': 4769733,
                    'width': 6427108481244138077,
                    'height': -2194505112521383512,
                },
                {
                    'identifier': -995495,
                    'width': -4414389277814705611,
                    'height': -1148503879878751660,
                },
                {
                    'identifier': 7613686,
                    'width': 2205047635243706182,
                    'height': 2076444988076679722,
                },
                {
                    'identifier': -142591,
                    'width': -8686895777162583485,
                    'height': -9097144565110667593,
                },
                {
                    'identifier': 8313456,
                    'width': -2149895114081685580,
                    'height': 7295509776356126547,
                },
                {
                    'identifier': 3120987,
                    'width': 3720756872873514198,
                    'height': 5981530722578973570,
                },
                {
                    'identifier': -533667,
                    'width': -8339513698813602236,
                    'height': -8124629507769911038,
                },
                {
                    'identifier': 3949016,
                    'width': -3474149878131004165,
                    'height': -9052421532155643849,
                },
                {
                    'identifier': 5416904,
                    'width': 7526128855479231066,
                    'height': -4161733438911496676,
                },
                {
                    'identifier': 1276670,
                    'width': -2856779435414958213,
                    'height': -1874009183623689500,
                },
            ],
            'screen': [
                {
                    'source_monitor': 3875962,
                    'source_nw_x_pixel': -5565143818795829943,
                    'source_nw_y_pixel': -9175853731926615201,
                    'source_pixel_width': -145426432491689624,
                    'source_pixel_height': -488482277444824547,
                    'rotation': -8997693840375138435,
                    'virtual_nw_x_pixel': -1773310913,
                    'virtual_nw_y_pixel': 1852844320,
                    'virtual_width': -1339523408,
                    'virtual_height': -537935719,
                },
                {
                    'source_monitor': -957253,
                    'source_nw_x_pixel': -1246716423999967173,
                    'source_nw_y_pixel': -1461702957802617449,
                    'source_pixel_width': -3689545239779071543,
                    'source_pixel_height': -4721923872343798208,
                    'rotation': -3097765702299033812,
                    'virtual_nw_x_pixel': 1159407028,
                    'virtual_nw_y_pixel': 180642548,
                    'virtual_width': 1056136420,
                    'virtual_height': 131914630,
                },
                {
                    'source_monitor': 8056959,
                    'source_nw_x_pixel': -1618065986856629364,
                    'source_nw_y_pixel': -7738664232103895006,
                    'source_pixel_width': -6479393516878782649,
                    'source_pixel_height': -4505788290911027022,
                    'rotation': -5066196618586793522,
                    'virtual_nw_x_pixel': -1781576307,
                    'virtual_nw_y_pixel': 1935066389,
                    'virtual_width': 155283497,
                    'virtual_height': -1591943880,
                },
                {
                    'source_monitor': 8649028,
                    'source_nw_x_pixel': -5078915824820565003,
                    'source_nw_y_pixel': -2144165486358556257,
                    'source_pixel_width': -6749572617042999211,
                    'source_pixel_height': -8147410991515314958,
                    'rotation': -3673150776926136903,
                    'virtual_nw_x_pixel': 827006336,
                    'virtual_nw_y_pixel': -358978469,
                    'virtual_width': 980972380,
                    'virtual_height': -439932767,
                },
                {
                    'source_monitor': 8882784,
                    'source_nw_x_pixel': -1440678965521453776,
                    'source_nw_y_pixel': -2292062128675789370,
                    'source_pixel_width': -3151062612964379566,
                    'source_pixel_height': -6683584757501573559,
                    'rotation': -507472138613045102,
                    'virtual_nw_x_pixel': 1588132085,
                    'virtual_nw_y_pixel': 1528926429,
                    'virtual_width': -1608369647,
                    'virtual_height': -1087858863,
                },
                {
                    'source_monitor': 7417754,
                    'source_nw_x_pixel': -7952688904116671223,
                    'source_nw_y_pixel': -3778081833313725108,
                    'source_pixel_width': -2925931408770285476,
                    'source_pixel_height': -4810529874974182234,
                    'rotation': -2851375922755376029,
                    'virtual_nw_x_pixel': -1739193534,
                    'virtual_nw_y_pixel': -928572374,
                    'virtual_width': -1876982711,
                    'virtual_height': 749618138,
                },
                {
                    'source_monitor': 494096,
                    'source_nw_x_pixel': -8474906437811688104,
                    'source_nw_y_pixel': -3573068366817543844,
                    'source_pixel_width': -2933306755070709126,
                    'source_pixel_height': -7072280375481848695,
                    'rotation': -136936449263672387,
                    'virtual_nw_x_pixel': 119098087,
                    'virtual_nw_y_pixel': -411913419,
                    'virtual_width': -1464697802,
                    'virtual_height': 488423709,
                },
                {
                    'source_monitor': 7820179,
                    'source_nw_x_pixel': -8800104088130094258,
                    'source_nw_y_pixel': -6752743705322947686,
                    'source_pixel_width': -8977518522957014169,
                    'source_pixel_height': -8202397582555562595,
                    'rotation': -4957060333228260493,
                    'virtual_nw_x_pixel': 618380154,
                    'virtual_nw_y_pixel': 14898018,
                    'virtual_width': 1389857511,
                    'virtual_height': -281112792,
                },
                {
                    'source_monitor': 3701868,
                    'source_nw_x_pixel': -3903660667872355515,
                    'source_nw_y_pixel': -7456484228032594416,
                    'source_pixel_width': -6504474918133583265,
                    'source_pixel_height': -1986385655551436792,
                    'rotation': -344530341159216978,
                    'virtual_nw_x_pixel': 1099661293,
                    'virtual_nw_y_pixel': 1959577689,
                    'virtual_width': 908519427,
                    'virtual_height': 136003678,
                },
                {
                    'source_monitor': 937832,
                    'source_nw_x_pixel': -8251207767025894361,
                    'source_nw_y_pixel': -2172570383971185720,
                    'source_pixel_width': -6064302833780936995,
                    'source_pixel_height': -5896648736449486004,
                    'rotation': -1499497249962935736,
                    'virtual_nw_x_pixel': 1424918705,
                    'virtual_nw_y_pixel': -1608478838,
                    'virtual_width': -1602093084,
                    'virtual_height': 1999413152,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 327813,
                    'width': 8410852127198580492,
                    'height': -3768264215677146522,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -467791365902237671,
                    'source_nw_y_pixel': -3116423105434837812,
                    'source_pixel_width': -4139375518538639966,
                    'source_pixel_height': -6435391316104946702,
                    'rotation': -3284606810870590711,
                    'virtual_nw_x_pixel': 967090407,
                    'virtual_nw_y_pixel': 348725161,
                    'virtual_width': -1954512468,
                    'virtual_height': 1555249099,
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
            'request_id': 1507801,
            'mapped_screens_by_monitors': [
                {
                    'description': 'ĭʒЏí҈ѱĪǛТQě8ȺßĽѸ"]ϖɇĐĻиԤсǺ˅ƣǏň',
                    'monitors': [
                            {
                                        'identifier': 6242889,
                                        'width': -8895363072935679817,
                                        'height': -8817040256020398624,
                                    },
                            {
                                        'identifier': 2670805,
                                        'width': -6757007731113529473,
                                        'height': -7273047861918163381,
                                    },
                            {
                                        'identifier': 7651784,
                                        'width': 5041897446026307196,
                                        'height': -8559197049311287365,
                                    },
                            {
                                        'identifier': 5995656,
                                        'width': 6734265530144330029,
                                        'height': -1239965445080785028,
                                    },
                            {
                                        'identifier': 2516444,
                                        'width': 129904336515087299,
                                        'height': 7667975140816633020,
                                    },
                            {
                                        'identifier': 8282684,
                                        'width': 8985119432991813963,
                                        'height': -2960170264974107778,
                                    },
                            {
                                        'identifier': 3410591,
                                        'width': 2945552314290365716,
                                        'height': 5231885643183402084,
                                    },
                            {
                                        'identifier': 1795620,
                                        'width': -6583477054473362867,
                                        'height': -5438991780412234247,
                                    },
                            {
                                        'identifier': 3856487,
                                        'width': 8945765845396863871,
                                        'height': 1437360624448496267,
                                    },
                            {
                                        'identifier': 9644198,
                                        'width': 2269129106624255088,
                                        'height': -2478036232171025915,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9508475,
                                        'source_nw_x_pixel': -857869250200409913,
                                        'source_nw_y_pixel': -8527512116603476974,
                                        'source_pixel_width': -2693995201100771997,
                                        'source_pixel_height': -6331002259650717993,
                                        'rotation': -7761800891286018464,
                                        'virtual_nw_x_pixel': 467391542,
                                        'virtual_nw_y_pixel': -1442335926,
                                        'virtual_width': 660547073,
                                        'virtual_height': -75483672,
                                    },
                            {
                                        'source_monitor': 8114072,
                                        'source_nw_x_pixel': -7640974215480848139,
                                        'source_nw_y_pixel': -2006714690733644969,
                                        'source_pixel_width': -3718036565024999115,
                                        'source_pixel_height': -2153985810788295775,
                                        'rotation': -8972876952501594741,
                                        'virtual_nw_x_pixel': 1367833296,
                                        'virtual_nw_y_pixel': 838471017,
                                        'virtual_width': -1776411677,
                                        'virtual_height': -802608527,
                                    },
                            {
                                        'source_monitor': 2598228,
                                        'source_nw_x_pixel': -3310648773290745797,
                                        'source_nw_y_pixel': -325905742216291985,
                                        'source_pixel_width': -5427185435482283124,
                                        'source_pixel_height': -4728089170369467928,
                                        'rotation': -3324890158672466941,
                                        'virtual_nw_x_pixel': 1778627228,
                                        'virtual_nw_y_pixel': -1670842794,
                                        'virtual_width': -908713603,
                                        'virtual_height': 1832318517,
                                    },
                            {
                                        'source_monitor': 6776400,
                                        'source_nw_x_pixel': -7399611268208217955,
                                        'source_nw_y_pixel': -186348392521828495,
                                        'source_pixel_width': -858647398185345893,
                                        'source_pixel_height': -3752822936197629815,
                                        'rotation': -6135148626358563211,
                                        'virtual_nw_x_pixel': -1614548977,
                                        'virtual_nw_y_pixel': -802963099,
                                        'virtual_width': 985152275,
                                        'virtual_height': -1551009471,
                                    },
                            {
                                        'source_monitor': 6879602,
                                        'source_nw_x_pixel': -1828300964977065705,
                                        'source_nw_y_pixel': -8819392816380791048,
                                        'source_pixel_width': -7454528677353600941,
                                        'source_pixel_height': -454500797030692356,
                                        'rotation': -8885244212490520208,
                                        'virtual_nw_x_pixel': 1813017213,
                                        'virtual_nw_y_pixel': 1493223929,
                                        'virtual_width': -164620585,
                                        'virtual_height': -1281024022,
                                    },
                            {
                                        'source_monitor': 3035928,
                                        'source_nw_x_pixel': -5896125357261469547,
                                        'source_nw_y_pixel': -8614369805869802813,
                                        'source_pixel_width': -5513533900507789187,
                                        'source_pixel_height': -2665132991186795057,
                                        'rotation': -8375047365554434171,
                                        'virtual_nw_x_pixel': -175078996,
                                        'virtual_nw_y_pixel': 987148852,
                                        'virtual_width': 785846093,
                                        'virtual_height': 1485592584,
                                    },
                            {
                                        'source_monitor': 3558512,
                                        'source_nw_x_pixel': -4621627049412874340,
                                        'source_nw_y_pixel': -5963520427766387614,
                                        'source_pixel_width': -3037753763121731817,
                                        'source_pixel_height': -1327921617637054567,
                                        'rotation': -5086521718756079010,
                                        'virtual_nw_x_pixel': -1468005985,
                                        'virtual_nw_y_pixel': 455579419,
                                        'virtual_width': -1168875682,
                                        'virtual_height': 1492828371,
                                    },
                            {
                                        'source_monitor': 5417106,
                                        'source_nw_x_pixel': -1928759900507667012,
                                        'source_nw_y_pixel': -2639884838122752024,
                                        'source_pixel_width': -4789905359305972557,
                                        'source_pixel_height': -4363884432026417050,
                                        'rotation': -7033826310087907169,
                                        'virtual_nw_x_pixel': 1137050752,
                                        'virtual_nw_y_pixel': 1430682656,
                                        'virtual_width': -1968303397,
                                        'virtual_height': -1849084013,
                                    },
                            {
                                        'source_monitor': -987459,
                                        'source_nw_x_pixel': -50342124772458247,
                                        'source_nw_y_pixel': -7693682834552737962,
                                        'source_pixel_width': -5467938065709456433,
                                        'source_pixel_height': -5861023290387486058,
                                        'rotation': -5819833278442928,
                                        'virtual_nw_x_pixel': 972672701,
                                        'virtual_nw_y_pixel': -148107929,
                                        'virtual_width': -1946549439,
                                        'virtual_height': 844511614,
                                    },
                            {
                                        'source_monitor': 9074589,
                                        'source_nw_x_pixel': -6235677825748046953,
                                        'source_nw_y_pixel': -3455513910579041170,
                                        'source_pixel_width': -3922387153704675499,
                                        'source_pixel_height': -4901820925446357125,
                                        'rotation': -4308959058326276594,
                                        'virtual_nw_x_pixel': -1878385670,
                                        'virtual_nw_y_pixel': 490005240,
                                        'virtual_width': 1246033376,
                                        'virtual_height': -1504386931,
                                    },
                        ],
                },
                {
                    'description': 'Ľʹ˫Еňčʢц²ӷτυδϼ҈ŗӵúУŗǟԣΜöʘΤįȌϢG',
                    'monitors': [
                            {
                                        'identifier': 9096048,
                                        'width': -5807260239436766023,
                                        'height': -7591480460720929188,
                                    },
                            {
                                        'identifier': 8709758,
                                        'width': 2828475958967889316,
                                        'height': -554282432680182568,
                                    },
                            {
                                        'identifier': 5185629,
                                        'width': 3698210975959106536,
                                        'height': -1917019469276851447,
                                    },
                            {
                                        'identifier': -223920,
                                        'width': 6789849187072399611,
                                        'height': -1997949766984088974,
                                    },
                            {
                                        'identifier': 8631321,
                                        'width': -7678526306109807094,
                                        'height': 3925813747811162565,
                                    },
                            {
                                        'identifier': 9583490,
                                        'width': -2532209016123185179,
                                        'height': 8633363933413337129,
                                    },
                            {
                                        'identifier': 9673889,
                                        'width': -1293966564932273143,
                                        'height': -2129675256970246989,
                                    },
                            {
                                        'identifier': 503127,
                                        'width': -5820189409188087115,
                                        'height': -26081637116998367,
                                    },
                            {
                                        'identifier': 481088,
                                        'width': -5671741509041051301,
                                        'height': 6285629999636399874,
                                    },
                            {
                                        'identifier': 7271186,
                                        'width': -664810722724473124,
                                        'height': -2429621704587900960,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 806290,
                                        'source_nw_x_pixel': -1104903120404510198,
                                        'source_nw_y_pixel': -6096068270229235441,
                                        'source_pixel_width': -5381772516730985698,
                                        'source_pixel_height': -86219339434337372,
                                        'rotation': -4499259836761608918,
                                        'virtual_nw_x_pixel': 284534369,
                                        'virtual_nw_y_pixel': -141186524,
                                        'virtual_width': -424912396,
                                        'virtual_height': -1729314414,
                                    },
                            {
                                        'source_monitor': 1514465,
                                        'source_nw_x_pixel': -185496715650094901,
                                        'source_nw_y_pixel': -9208477009611755540,
                                        'source_pixel_width': -8953794681949095519,
                                        'source_pixel_height': -3026357928245401236,
                                        'rotation': -1677359732829094728,
                                        'virtual_nw_x_pixel': 1192323533,
                                        'virtual_nw_y_pixel': 1796200180,
                                        'virtual_width': 335586571,
                                        'virtual_height': -1445583552,
                                    },
                            {
                                        'source_monitor': 172295,
                                        'source_nw_x_pixel': -5618580214603906979,
                                        'source_nw_y_pixel': -9075756046975349709,
                                        'source_pixel_width': -3173994703821638989,
                                        'source_pixel_height': -8375128786656049917,
                                        'rotation': -3620375597951769193,
                                        'virtual_nw_x_pixel': 1002440545,
                                        'virtual_nw_y_pixel': -503365667,
                                        'virtual_width': -1244464018,
                                        'virtual_height': -249259536,
                                    },
                            {
                                        'source_monitor': 2365249,
                                        'source_nw_x_pixel': -6926384049874841213,
                                        'source_nw_y_pixel': -3437543317612253255,
                                        'source_pixel_width': -7030592181036341000,
                                        'source_pixel_height': -6687425031556671609,
                                        'rotation': -6845729329584657261,
                                        'virtual_nw_x_pixel': 107668730,
                                        'virtual_nw_y_pixel': -1572177339,
                                        'virtual_width': 594078371,
                                        'virtual_height': -918370557,
                                    },
                            {
                                        'source_monitor': 3079958,
                                        'source_nw_x_pixel': -6688184091975719703,
                                        'source_nw_y_pixel': -8885326728804829783,
                                        'source_pixel_width': -4965411894716396891,
                                        'source_pixel_height': -2009770838607691603,
                                        'rotation': -7245984073887865614,
                                        'virtual_nw_x_pixel': -380084209,
                                        'virtual_nw_y_pixel': 1398475673,
                                        'virtual_width': 1642074717,
                                        'virtual_height': 149731793,
                                    },
                            {
                                        'source_monitor': 1784758,
                                        'source_nw_x_pixel': -2763983322341739870,
                                        'source_nw_y_pixel': -6754119318461541475,
                                        'source_pixel_width': -9103762389076963411,
                                        'source_pixel_height': -3301520459185998131,
                                        'rotation': -9183360549240094804,
                                        'virtual_nw_x_pixel': 1676076606,
                                        'virtual_nw_y_pixel': 456230971,
                                        'virtual_width': 1083204005,
                                        'virtual_height': 1597655715,
                                    },
                            {
                                        'source_monitor': 1063983,
                                        'source_nw_x_pixel': -5107963151547990135,
                                        'source_nw_y_pixel': -4912154507473849094,
                                        'source_pixel_width': -2386146564913064689,
                                        'source_pixel_height': -7971264005847641933,
                                        'rotation': -5952186412935175597,
                                        'virtual_nw_x_pixel': 1158390360,
                                        'virtual_nw_y_pixel': 1296414791,
                                        'virtual_width': -59750584,
                                        'virtual_height': -1958903625,
                                    },
                            {
                                        'source_monitor': 7606132,
                                        'source_nw_x_pixel': -8158986724902251983,
                                        'source_nw_y_pixel': -5292485139086911239,
                                        'source_pixel_width': -4353830093712399209,
                                        'source_pixel_height': -8092461431644593531,
                                        'rotation': -2585342840113438236,
                                        'virtual_nw_x_pixel': 1614582962,
                                        'virtual_nw_y_pixel': -322143140,
                                        'virtual_width': 848275482,
                                        'virtual_height': 389838503,
                                    },
                            {
                                        'source_monitor': 5626261,
                                        'source_nw_x_pixel': -8881270175838742057,
                                        'source_nw_y_pixel': -735468609823550223,
                                        'source_pixel_width': -5649865046771400193,
                                        'source_pixel_height': -8336117291835103487,
                                        'rotation': -8685081889156590934,
                                        'virtual_nw_x_pixel': 469595389,
                                        'virtual_nw_y_pixel': -73487942,
                                        'virtual_width': -233467153,
                                        'virtual_height': 526918419,
                                    },
                            {
                                        'source_monitor': 3749658,
                                        'source_nw_x_pixel': -6671282474133685670,
                                        'source_nw_y_pixel': -4972915113572655578,
                                        'source_pixel_width': -4853844593064127330,
                                        'source_pixel_height': -1202248667527873791,
                                        'rotation': -3661176402270178954,
                                        'virtual_nw_x_pixel': -1729446942,
                                        'virtual_nw_y_pixel': 1206557836,
                                        'virtual_width': -1661535516,
                                        'virtual_height': -345052546,
                                    },
                        ],
                },
                {
                    'description': 'ϻāŬȉε҃ʳHϿ\x9bZĲǰҩÑҭ\x8aŋƋÑūҶ˅ĊƴΔƙʥŠǂ',
                    'monitors': [
                            {
                                        'identifier': -608510,
                                        'width': -8126634957573346023,
                                        'height': -3083466263491063486,
                                    },
                            {
                                        'identifier': 963696,
                                        'width': 6591749937696930541,
                                        'height': -842766955975919769,
                                    },
                            {
                                        'identifier': 9401903,
                                        'width': 8692348522421780092,
                                        'height': 5738773981309874053,
                                    },
                            {
                                        'identifier': 3799623,
                                        'width': -8676512208706386272,
                                        'height': -6130147890346822732,
                                    },
                            {
                                        'identifier': 6175206,
                                        'width': 5573430581073690945,
                                        'height': 6335282471795381698,
                                    },
                            {
                                        'identifier': 1033930,
                                        'width': 6793579759861658113,
                                        'height': 3045708397865721672,
                                    },
                            {
                                        'identifier': 9040858,
                                        'width': -8788446091102824662,
                                        'height': -149296580699202454,
                                    },
                            {
                                        'identifier': 2698778,
                                        'width': -5622796895743021978,
                                        'height': 5306716499937675601,
                                    },
                            {
                                        'identifier': 1584325,
                                        'width': -7510452953788579980,
                                        'height': -4102849123490202188,
                                    },
                            {
                                        'identifier': 9915650,
                                        'width': 6591142682834216585,
                                        'height': -5187630707794866900,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7075456,
                                        'source_nw_x_pixel': -5285222240195392959,
                                        'source_nw_y_pixel': -2060034649873482074,
                                        'source_pixel_width': -5191329000181182301,
                                        'source_pixel_height': -859830155924243126,
                                        'rotation': -1506691500067490551,
                                        'virtual_nw_x_pixel': -1609786591,
                                        'virtual_nw_y_pixel': 1032939914,
                                        'virtual_width': -1709534554,
                                        'virtual_height': -513417185,
                                    },
                            {
                                        'source_monitor': 6598227,
                                        'source_nw_x_pixel': -1957458235106490389,
                                        'source_nw_y_pixel': -8156841607673545463,
                                        'source_pixel_width': -5454213830897171668,
                                        'source_pixel_height': -6973029614004246757,
                                        'rotation': -3448829298072353828,
                                        'virtual_nw_x_pixel': 1854549646,
                                        'virtual_nw_y_pixel': 466694725,
                                        'virtual_width': 39051900,
                                        'virtual_height': 85660040,
                                    },
                            {
                                        'source_monitor': 461645,
                                        'source_nw_x_pixel': -2478958297781196955,
                                        'source_nw_y_pixel': -489087824454893885,
                                        'source_pixel_width': -4525195072016089449,
                                        'source_pixel_height': -3213972525447101751,
                                        'rotation': -911922026167390933,
                                        'virtual_nw_x_pixel': -693757132,
                                        'virtual_nw_y_pixel': 959566831,
                                        'virtual_width': 129222016,
                                        'virtual_height': -1637133733,
                                    },
                            {
                                        'source_monitor': 3003239,
                                        'source_nw_x_pixel': -8557324614990706111,
                                        'source_nw_y_pixel': -6633763133203227551,
                                        'source_pixel_width': -110867199373005287,
                                        'source_pixel_height': -9013603448383920830,
                                        'rotation': -7519589004475885431,
                                        'virtual_nw_x_pixel': 1889514546,
                                        'virtual_nw_y_pixel': -1241186852,
                                        'virtual_width': -1589955048,
                                        'virtual_height': 1258856047,
                                    },
                            {
                                        'source_monitor': 4035708,
                                        'source_nw_x_pixel': -5317515519989592232,
                                        'source_nw_y_pixel': -9168682718335869426,
                                        'source_pixel_width': -3481372794431403952,
                                        'source_pixel_height': -88730576454893832,
                                        'rotation': -7885147598432728066,
                                        'virtual_nw_x_pixel': -1226070382,
                                        'virtual_nw_y_pixel': 1442823919,
                                        'virtual_width': 580046174,
                                        'virtual_height': -1599778997,
                                    },
                            {
                                        'source_monitor': 9983987,
                                        'source_nw_x_pixel': -3788610161556338241,
                                        'source_nw_y_pixel': -7291252998230963523,
                                        'source_pixel_width': -4358634026580863777,
                                        'source_pixel_height': -4302742233093882956,
                                        'rotation': -7603549941131107971,
                                        'virtual_nw_x_pixel': 1206634606,
                                        'virtual_nw_y_pixel': -1071914147,
                                        'virtual_width': 1738604976,
                                        'virtual_height': -1000941809,
                                    },
                            {
                                        'source_monitor': 1961968,
                                        'source_nw_x_pixel': -3108385924935854980,
                                        'source_nw_y_pixel': -3466952877110530931,
                                        'source_pixel_width': -4659321417163359584,
                                        'source_pixel_height': -3549387594154179585,
                                        'rotation': -1373319916687280580,
                                        'virtual_nw_x_pixel': 1735729147,
                                        'virtual_nw_y_pixel': 1792285133,
                                        'virtual_width': -1519130592,
                                        'virtual_height': -1298915034,
                                    },
                            {
                                        'source_monitor': 6484593,
                                        'source_nw_x_pixel': -4550208342678156596,
                                        'source_nw_y_pixel': -6702840512123157950,
                                        'source_pixel_width': -1259521762992633564,
                                        'source_pixel_height': -6674501059231632737,
                                        'rotation': -8031180823018241244,
                                        'virtual_nw_x_pixel': 594376286,
                                        'virtual_nw_y_pixel': -349830465,
                                        'virtual_width': -1319050814,
                                        'virtual_height': -1734409319,
                                    },
                            {
                                        'source_monitor': 2269507,
                                        'source_nw_x_pixel': -1579387665026221880,
                                        'source_nw_y_pixel': -2306795830767090104,
                                        'source_pixel_width': -4214546664520177011,
                                        'source_pixel_height': -4036090293938852328,
                                        'rotation': -1124502339593898967,
                                        'virtual_nw_x_pixel': 267697229,
                                        'virtual_nw_y_pixel': 1818308827,
                                        'virtual_width': -1759687172,
                                        'virtual_height': -1089754029,
                                    },
                            {
                                        'source_monitor': -755717,
                                        'source_nw_x_pixel': -368764326206676323,
                                        'source_nw_y_pixel': -1452683222734784346,
                                        'source_pixel_width': -2088805580807598523,
                                        'source_pixel_height': -715804332358934969,
                                        'rotation': -3736278202204499321,
                                        'virtual_nw_x_pixel': 1968539348,
                                        'virtual_nw_y_pixel': 1599854326,
                                        'virtual_width': -1692430521,
                                        'virtual_height': 593118224,
                                    },
                        ],
                },
                {
                    'description': 'ӹˬƄŴlyȧʾӹӚɧÍӤ£ÖŤjȡИ˾Ѥ:ӥԂɫĹ˄ʈɆі',
                    'monitors': [
                            {
                                        'identifier': 2821766,
                                        'width': 9196280148624328843,
                                        'height': 885219809375887523,
                                    },
                            {
                                        'identifier': 8527773,
                                        'width': 1750523967391337310,
                                        'height': 6313831216538967669,
                                    },
                            {
                                        'identifier': 2643688,
                                        'width': 4012402996396617917,
                                        'height': -6423257853212432427,
                                    },
                            {
                                        'identifier': 587319,
                                        'width': -188648551248896253,
                                        'height': -635862553831020510,
                                    },
                            {
                                        'identifier': 2946855,
                                        'width': 1823464676304327377,
                                        'height': 5182869243380188485,
                                    },
                            {
                                        'identifier': 5693882,
                                        'width': 3438292940585768576,
                                        'height': -2743798468040606704,
                                    },
                            {
                                        'identifier': 2287425,
                                        'width': 8725498760677349638,
                                        'height': 8026309661458738341,
                                    },
                            {
                                        'identifier': 4791646,
                                        'width': -1187465255769808293,
                                        'height': -6441888926241813278,
                                    },
                            {
                                        'identifier': 4782128,
                                        'width': 4087841734060709919,
                                        'height': 8066928715587320960,
                                    },
                            {
                                        'identifier': 3241821,
                                        'width': -5641966243505430822,
                                        'height': 8873704433586010711,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2974111,
                                        'source_nw_x_pixel': -3712141390424399884,
                                        'source_nw_y_pixel': -695178424319187813,
                                        'source_pixel_width': -7588361630732577648,
                                        'source_pixel_height': -6581143802861537532,
                                        'rotation': -4121309018179245676,
                                        'virtual_nw_x_pixel': -648387932,
                                        'virtual_nw_y_pixel': 1078999214,
                                        'virtual_width': -707806943,
                                        'virtual_height': -969465047,
                                    },
                            {
                                        'source_monitor': 4895705,
                                        'source_nw_x_pixel': -5940479734080878065,
                                        'source_nw_y_pixel': -7761630102928422245,
                                        'source_pixel_width': -2263898877136820505,
                                        'source_pixel_height': -3643649022009336758,
                                        'rotation': -5437281205391979029,
                                        'virtual_nw_x_pixel': -56654743,
                                        'virtual_nw_y_pixel': -1752236281,
                                        'virtual_width': 513077071,
                                        'virtual_height': 203978327,
                                    },
                            {
                                        'source_monitor': 8617646,
                                        'source_nw_x_pixel': -6790628430555218532,
                                        'source_nw_y_pixel': -3194378508940543818,
                                        'source_pixel_width': -8384416399312352010,
                                        'source_pixel_height': -3535625876813683446,
                                        'rotation': -495421796975593322,
                                        'virtual_nw_x_pixel': -1829409066,
                                        'virtual_nw_y_pixel': -960089483,
                                        'virtual_width': 735358664,
                                        'virtual_height': -526151915,
                                    },
                            {
                                        'source_monitor': 3787036,
                                        'source_nw_x_pixel': -6354370631183737508,
                                        'source_nw_y_pixel': -68070659827305364,
                                        'source_pixel_width': -5167570265305634618,
                                        'source_pixel_height': -1579037894565226147,
                                        'rotation': -4129415760194541857,
                                        'virtual_nw_x_pixel': -1095621567,
                                        'virtual_nw_y_pixel': -1711281855,
                                        'virtual_width': 1294452112,
                                        'virtual_height': -164902977,
                                    },
                            {
                                        'source_monitor': 7658291,
                                        'source_nw_x_pixel': -2234586674615624547,
                                        'source_nw_y_pixel': -5664636418254261411,
                                        'source_pixel_width': -4605588184645236496,
                                        'source_pixel_height': -5675481873505623435,
                                        'rotation': -5523187517406421048,
                                        'virtual_nw_x_pixel': 917631065,
                                        'virtual_nw_y_pixel': 1412332148,
                                        'virtual_width': 1258978568,
                                        'virtual_height': 500783533,
                                    },
                            {
                                        'source_monitor': 1580212,
                                        'source_nw_x_pixel': -261781296236908339,
                                        'source_nw_y_pixel': -674970858540847144,
                                        'source_pixel_width': -4307674351579702110,
                                        'source_pixel_height': -5251685685203127264,
                                        'rotation': -6348656928455646277,
                                        'virtual_nw_x_pixel': -613641619,
                                        'virtual_nw_y_pixel': 1778516272,
                                        'virtual_width': -622075552,
                                        'virtual_height': 265599209,
                                    },
                            {
                                        'source_monitor': 7797254,
                                        'source_nw_x_pixel': -5319455331992375284,
                                        'source_nw_y_pixel': -2285503712181601009,
                                        'source_pixel_width': -8557665087901460320,
                                        'source_pixel_height': -5407468633744684949,
                                        'rotation': -4565412558496571110,
                                        'virtual_nw_x_pixel': -39979329,
                                        'virtual_nw_y_pixel': 551202591,
                                        'virtual_width': 3710359,
                                        'virtual_height': -1502485097,
                                    },
                            {
                                        'source_monitor': 7681036,
                                        'source_nw_x_pixel': -2027044332267311973,
                                        'source_nw_y_pixel': -185003516740365678,
                                        'source_pixel_width': -8614759674535753878,
                                        'source_pixel_height': -1061469256911572291,
                                        'rotation': -8748843941522879114,
                                        'virtual_nw_x_pixel': -855858881,
                                        'virtual_nw_y_pixel': -1574932982,
                                        'virtual_width': 700819776,
                                        'virtual_height': 66823415,
                                    },
                            {
                                        'source_monitor': 8035330,
                                        'source_nw_x_pixel': -3952872447550918388,
                                        'source_nw_y_pixel': -3322509120626204945,
                                        'source_pixel_width': -4352033763449658768,
                                        'source_pixel_height': -5052343014144247440,
                                        'rotation': -8898611845197274725,
                                        'virtual_nw_x_pixel': -155706367,
                                        'virtual_nw_y_pixel': -611629018,
                                        'virtual_width': -870849311,
                                        'virtual_height': -1654866172,
                                    },
                            {
                                        'source_monitor': 8384826,
                                        'source_nw_x_pixel': -2160435176522696128,
                                        'source_nw_y_pixel': -2243548617562879238,
                                        'source_pixel_width': -1411664545830332734,
                                        'source_pixel_height': -2891289985782723310,
                                        'rotation': -6546560604827043641,
                                        'virtual_nw_x_pixel': 1095705493,
                                        'virtual_nw_y_pixel': -1304062126,
                                        'virtual_width': 1115771867,
                                        'virtual_height': -188156392,
                                    },
                        ],
                },
                {
                    'description': '\x9dϕɃʩԥӰѤƂnεɹҪӕ\x95ɧÕ\x9b҅лƍƬ΄Ë£˟әȼί˨r',
                    'monitors': [
                            {
                                        'identifier': 1660637,
                                        'width': -8589416755512796203,
                                        'height': -6214639299670576956,
                                    },
                            {
                                        'identifier': 5406404,
                                        'width': -4611556432692929847,
                                        'height': 3816154697797008488,
                                    },
                            {
                                        'identifier': 7341803,
                                        'width': -2633339174767490598,
                                        'height': 8574404528955596168,
                                    },
                            {
                                        'identifier': 589328,
                                        'width': -4019453497619720567,
                                        'height': 2030108643849679689,
                                    },
                            {
                                        'identifier': 6150330,
                                        'width': 144595208863570417,
                                        'height': -6253292249821598921,
                                    },
                            {
                                        'identifier': 333431,
                                        'width': -8451463713603898152,
                                        'height': 4836071032799693039,
                                    },
                            {
                                        'identifier': 1307075,
                                        'width': 6639432265308601289,
                                        'height': 5822699006798042938,
                                    },
                            {
                                        'identifier': 6820995,
                                        'width': -504163984868406556,
                                        'height': 3408303160800606071,
                                    },
                            {
                                        'identifier': 6695795,
                                        'width': -6846980308871130850,
                                        'height': 8052779438129876589,
                                    },
                            {
                                        'identifier': 3042307,
                                        'width': 3211066804263042918,
                                        'height': -2299268049140669204,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5940880,
                                        'source_nw_x_pixel': -3126583712418820204,
                                        'source_nw_y_pixel': -5144902691237670727,
                                        'source_pixel_width': -8641553864326526699,
                                        'source_pixel_height': -2825172126042733691,
                                        'rotation': -4887912544373827970,
                                        'virtual_nw_x_pixel': 43794807,
                                        'virtual_nw_y_pixel': -1803854290,
                                        'virtual_width': -1147787331,
                                        'virtual_height': 1397909762,
                                    },
                            {
                                        'source_monitor': 7668348,
                                        'source_nw_x_pixel': -3621787844087300064,
                                        'source_nw_y_pixel': -4367577735018677424,
                                        'source_pixel_width': -4461757231509798377,
                                        'source_pixel_height': -6186594616040973390,
                                        'rotation': -1859467098782590014,
                                        'virtual_nw_x_pixel': 1059413115,
                                        'virtual_nw_y_pixel': 1281729263,
                                        'virtual_width': 1109899739,
                                        'virtual_height': -1720000583,
                                    },
                            {
                                        'source_monitor': 451135,
                                        'source_nw_x_pixel': -4039860212290119613,
                                        'source_nw_y_pixel': -6627117868228546116,
                                        'source_pixel_width': -4387456824838763505,
                                        'source_pixel_height': -3352137041795280828,
                                        'rotation': -7379109743807328926,
                                        'virtual_nw_x_pixel': 432688148,
                                        'virtual_nw_y_pixel': 138580874,
                                        'virtual_width': 460271564,
                                        'virtual_height': -147315311,
                                    },
                            {
                                        'source_monitor': 6557485,
                                        'source_nw_x_pixel': -556856123668086044,
                                        'source_nw_y_pixel': -2026423224528344697,
                                        'source_pixel_width': -2632082953289523008,
                                        'source_pixel_height': -4524823201155092236,
                                        'rotation': -7923855677348578570,
                                        'virtual_nw_x_pixel': 1381537071,
                                        'virtual_nw_y_pixel': 1880174040,
                                        'virtual_width': 1755974279,
                                        'virtual_height': 64934462,
                                    },
                            {
                                        'source_monitor': 9490963,
                                        'source_nw_x_pixel': -7186171122527437109,
                                        'source_nw_y_pixel': -1833920526426774684,
                                        'source_pixel_width': -1635388158729758647,
                                        'source_pixel_height': -5389101657003126026,
                                        'rotation': -2352605953725288563,
                                        'virtual_nw_x_pixel': 1602257699,
                                        'virtual_nw_y_pixel': -1399915438,
                                        'virtual_width': 769704221,
                                        'virtual_height': -1981404844,
                                    },
                            {
                                        'source_monitor': 4995245,
                                        'source_nw_x_pixel': -6909108040541590650,
                                        'source_nw_y_pixel': -127415026291922874,
                                        'source_pixel_width': -6583729602002975001,
                                        'source_pixel_height': -6852929595935976966,
                                        'rotation': -250126774340264976,
                                        'virtual_nw_x_pixel': 1478416295,
                                        'virtual_nw_y_pixel': 644779248,
                                        'virtual_width': -97188080,
                                        'virtual_height': 1287394577,
                                    },
                            {
                                        'source_monitor': 4518550,
                                        'source_nw_x_pixel': -7746796737015806142,
                                        'source_nw_y_pixel': -7392158002944745883,
                                        'source_pixel_width': -658775643155356752,
                                        'source_pixel_height': -743978825091007421,
                                        'rotation': -5118750872369765480,
                                        'virtual_nw_x_pixel': 497805440,
                                        'virtual_nw_y_pixel': 1772019931,
                                        'virtual_width': 122614792,
                                        'virtual_height': -690438366,
                                    },
                            {
                                        'source_monitor': 3255375,
                                        'source_nw_x_pixel': -4088392846269879632,
                                        'source_nw_y_pixel': -4796859946866706893,
                                        'source_pixel_width': -8556420947863230296,
                                        'source_pixel_height': -5604212862545939001,
                                        'rotation': -6097717055755298647,
                                        'virtual_nw_x_pixel': 97267496,
                                        'virtual_nw_y_pixel': 1280426899,
                                        'virtual_width': 1269403306,
                                        'virtual_height': -1043493066,
                                    },
                            {
                                        'source_monitor': 2945398,
                                        'source_nw_x_pixel': -348834152648791267,
                                        'source_nw_y_pixel': -3595073198624539999,
                                        'source_pixel_width': -1060339136137696833,
                                        'source_pixel_height': -9175265450154974139,
                                        'rotation': -7695167014337519418,
                                        'virtual_nw_x_pixel': 1189418384,
                                        'virtual_nw_y_pixel': 586940072,
                                        'virtual_width': 713900864,
                                        'virtual_height': 1471787965,
                                    },
                            {
                                        'source_monitor': 812235,
                                        'source_nw_x_pixel': -4462120620767580813,
                                        'source_nw_y_pixel': -3906983705369489770,
                                        'source_pixel_width': -1173718712846362406,
                                        'source_pixel_height': -7736728015195971247,
                                        'rotation': -8447068481611896176,
                                        'virtual_nw_x_pixel': -1247573609,
                                        'virtual_nw_y_pixel': 715323322,
                                        'virtual_width': -1854229326,
                                        'virtual_height': -29744600,
                                    },
                        ],
                },
                {
                    'description': 'ůˠìϏҟҺpĎћǚÚȧž˧ͱǰʟJϤ˩Ƶ\x9eКȏ˜Љɱȹɷɧ',
                    'monitors': [
                            {
                                        'identifier': 4938185,
                                        'width': -5002049640212360761,
                                        'height': 208786768230057087,
                                    },
                            {
                                        'identifier': 6432146,
                                        'width': -7787223901992044870,
                                        'height': -8635240733843823662,
                                    },
                            {
                                        'identifier': 2923119,
                                        'width': 4778005670163472625,
                                        'height': -4105192889079144290,
                                    },
                            {
                                        'identifier': 4111006,
                                        'width': -2866373099308933815,
                                        'height': 7089451406951499382,
                                    },
                            {
                                        'identifier': 9245042,
                                        'width': 6611222209909921171,
                                        'height': 6364069042373667298,
                                    },
                            {
                                        'identifier': 4727220,
                                        'width': 2425422428642889697,
                                        'height': 5057593886542027211,
                                    },
                            {
                                        'identifier': 8731893,
                                        'width': -8331032683599235409,
                                        'height': 7831872044302350589,
                                    },
                            {
                                        'identifier': 8471846,
                                        'width': -3987137642286436478,
                                        'height': 6054620469200423545,
                                    },
                            {
                                        'identifier': -232280,
                                        'width': -1580508670934594534,
                                        'height': -3608183945910275565,
                                    },
                            {
                                        'identifier': 5113681,
                                        'width': -7589122317209847658,
                                        'height': 1216041080218433024,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 688828,
                                        'source_nw_x_pixel': -8653689600446221980,
                                        'source_nw_y_pixel': -2052707960866197860,
                                        'source_pixel_width': -5008936604028696183,
                                        'source_pixel_height': -7708430989885009660,
                                        'rotation': -2114876412934447403,
                                        'virtual_nw_x_pixel': -813770906,
                                        'virtual_nw_y_pixel': 1074196395,
                                        'virtual_width': 1864937777,
                                        'virtual_height': -1730320679,
                                    },
                            {
                                        'source_monitor': 8358133,
                                        'source_nw_x_pixel': -7410476552639871582,
                                        'source_nw_y_pixel': -4014678428909127903,
                                        'source_pixel_width': -6268718964693691650,
                                        'source_pixel_height': -6980595696154377335,
                                        'rotation': -7764112075240975692,
                                        'virtual_nw_x_pixel': -1635929448,
                                        'virtual_nw_y_pixel': 714309889,
                                        'virtual_width': -1812246206,
                                        'virtual_height': 367814992,
                                    },
                            {
                                        'source_monitor': 7871981,
                                        'source_nw_x_pixel': -2304340557178063918,
                                        'source_nw_y_pixel': -3801244598736732623,
                                        'source_pixel_width': -6335439934259994156,
                                        'source_pixel_height': -1871192274385661907,
                                        'rotation': -3026030444411116786,
                                        'virtual_nw_x_pixel': -323097226,
                                        'virtual_nw_y_pixel': 909625745,
                                        'virtual_width': 734005068,
                                        'virtual_height': 1873093963,
                                    },
                            {
                                        'source_monitor': 7029178,
                                        'source_nw_x_pixel': -2448157787241334965,
                                        'source_nw_y_pixel': -2024856453721584147,
                                        'source_pixel_width': -8060479518684587947,
                                        'source_pixel_height': -2263622697584663784,
                                        'rotation': -6684163669968242518,
                                        'virtual_nw_x_pixel': -887468079,
                                        'virtual_nw_y_pixel': -403651354,
                                        'virtual_width': 288339518,
                                        'virtual_height': -891249842,
                                    },
                            {
                                        'source_monitor': 344388,
                                        'source_nw_x_pixel': -5613418602139829164,
                                        'source_nw_y_pixel': -2070449414271676758,
                                        'source_pixel_width': -4361732193323793090,
                                        'source_pixel_height': -8229110342114449746,
                                        'rotation': -96051174311165892,
                                        'virtual_nw_x_pixel': -1833931658,
                                        'virtual_nw_y_pixel': -1867578754,
                                        'virtual_width': -854419745,
                                        'virtual_height': 873629460,
                                    },
                            {
                                        'source_monitor': 101665,
                                        'source_nw_x_pixel': -3206991720873606341,
                                        'source_nw_y_pixel': -2322815130887933410,
                                        'source_pixel_width': -5026203282531864659,
                                        'source_pixel_height': -7376962805686073698,
                                        'rotation': -191330672022109784,
                                        'virtual_nw_x_pixel': 638540808,
                                        'virtual_nw_y_pixel': 1112727154,
                                        'virtual_width': -533470976,
                                        'virtual_height': -630628539,
                                    },
                            {
                                        'source_monitor': -181392,
                                        'source_nw_x_pixel': -1660580572910054671,
                                        'source_nw_y_pixel': -8830347977272926091,
                                        'source_pixel_width': -3781487699648108396,
                                        'source_pixel_height': -8574479857024886647,
                                        'rotation': -450167967753802524,
                                        'virtual_nw_x_pixel': -911200886,
                                        'virtual_nw_y_pixel': -720864396,
                                        'virtual_width': -335744764,
                                        'virtual_height': 229178498,
                                    },
                            {
                                        'source_monitor': -510257,
                                        'source_nw_x_pixel': -836677599674479033,
                                        'source_nw_y_pixel': -8178208250880964899,
                                        'source_pixel_width': -8575992570084086083,
                                        'source_pixel_height': -5367534429565751310,
                                        'rotation': -6599253073296477889,
                                        'virtual_nw_x_pixel': 1920962526,
                                        'virtual_nw_y_pixel': -1514705011,
                                        'virtual_width': -1171869668,
                                        'virtual_height': 304684292,
                                    },
                            {
                                        'source_monitor': 1242187,
                                        'source_nw_x_pixel': -6232911237080429708,
                                        'source_nw_y_pixel': -2454272064418908398,
                                        'source_pixel_width': -4708287847857248396,
                                        'source_pixel_height': -8731394483370920662,
                                        'rotation': -8855133686170282221,
                                        'virtual_nw_x_pixel': 1245412677,
                                        'virtual_nw_y_pixel': -642279929,
                                        'virtual_width': -1160622627,
                                        'virtual_height': -984995640,
                                    },
                            {
                                        'source_monitor': 5293238,
                                        'source_nw_x_pixel': -8750985020586405289,
                                        'source_nw_y_pixel': -787704270253907227,
                                        'source_pixel_width': -439393478646856278,
                                        'source_pixel_height': -5580022559561366168,
                                        'rotation': -8970984292948172781,
                                        'virtual_nw_x_pixel': 304781037,
                                        'virtual_nw_y_pixel': -547832902,
                                        'virtual_width': 1423281474,
                                        'virtual_height': 222064226,
                                    },
                        ],
                },
                {
                    'description': 'Xϊ˷ƟȩҭҴϸ рЩg˺\x944ԨȄԤĘˍʚ˱\x9aɂǸ\x80ɌԊѭϣ',
                    'monitors': [
                            {
                                        'identifier': 772579,
                                        'width': -7794113162887111073,
                                        'height': -5873767798043698347,
                                    },
                            {
                                        'identifier': 6518995,
                                        'width': -7036299095586020990,
                                        'height': 5493020158819730766,
                                    },
                            {
                                        'identifier': 4973049,
                                        'width': -5499545490627015068,
                                        'height': -623834101779121384,
                                    },
                            {
                                        'identifier': 8105849,
                                        'width': -4909265163475604569,
                                        'height': 3252351106798365236,
                                    },
                            {
                                        'identifier': 9206291,
                                        'width': -1227149051770223990,
                                        'height': -2662655606716963451,
                                    },
                            {
                                        'identifier': 3065621,
                                        'width': -348760876266158376,
                                        'height': -6923182235104282746,
                                    },
                            {
                                        'identifier': 1568242,
                                        'width': -8594263650214302681,
                                        'height': 4142903521861303136,
                                    },
                            {
                                        'identifier': 6516065,
                                        'width': -5262563178545381949,
                                        'height': 7150850157521045699,
                                    },
                            {
                                        'identifier': 3898598,
                                        'width': 65811885661243131,
                                        'height': 3503037044863443929,
                                    },
                            {
                                        'identifier': 4180580,
                                        'width': -4983191670292846311,
                                        'height': 755429786848444213,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8606258,
                                        'source_nw_x_pixel': -5133262120624260773,
                                        'source_nw_y_pixel': -4137572666736120821,
                                        'source_pixel_width': -5203179294387698166,
                                        'source_pixel_height': -6704013821552187657,
                                        'rotation': -3063078347097416321,
                                        'virtual_nw_x_pixel': 952859142,
                                        'virtual_nw_y_pixel': -1621332581,
                                        'virtual_width': -1819908043,
                                        'virtual_height': 791393722,
                                    },
                            {
                                        'source_monitor': -377831,
                                        'source_nw_x_pixel': -4004528940093484538,
                                        'source_nw_y_pixel': -3475954358309357865,
                                        'source_pixel_width': -800540871060105138,
                                        'source_pixel_height': -8369471807349737820,
                                        'rotation': -7068076269391054596,
                                        'virtual_nw_x_pixel': -1632863516,
                                        'virtual_nw_y_pixel': -1794124284,
                                        'virtual_width': 959050201,
                                        'virtual_height': 904100823,
                                    },
                            {
                                        'source_monitor': 5180156,
                                        'source_nw_x_pixel': -3376466999595991913,
                                        'source_nw_y_pixel': -3222047772231730054,
                                        'source_pixel_width': -2222506520541464350,
                                        'source_pixel_height': -3169982026608965329,
                                        'rotation': -4035618698623239671,
                                        'virtual_nw_x_pixel': 1526849450,
                                        'virtual_nw_y_pixel': -1392182401,
                                        'virtual_width': -561256265,
                                        'virtual_height': 1398622744,
                                    },
                            {
                                        'source_monitor': 1758493,
                                        'source_nw_x_pixel': -1000708721446852442,
                                        'source_nw_y_pixel': -8804937362482756452,
                                        'source_pixel_width': -6060891414829693895,
                                        'source_pixel_height': -8581109406465600047,
                                        'rotation': -8044203757528924129,
                                        'virtual_nw_x_pixel': 1306368001,
                                        'virtual_nw_y_pixel': -1542392089,
                                        'virtual_width': -1664260177,
                                        'virtual_height': 13093857,
                                    },
                            {
                                        'source_monitor': -277816,
                                        'source_nw_x_pixel': -2836588834876128179,
                                        'source_nw_y_pixel': -5842214555747871036,
                                        'source_pixel_width': -4360725354275346180,
                                        'source_pixel_height': -2979274121925340382,
                                        'rotation': -2520768012672872346,
                                        'virtual_nw_x_pixel': -642835595,
                                        'virtual_nw_y_pixel': -863271667,
                                        'virtual_width': -1871798203,
                                        'virtual_height': 66442944,
                                    },
                            {
                                        'source_monitor': 2368079,
                                        'source_nw_x_pixel': -4479486076064470539,
                                        'source_nw_y_pixel': -4831767448154945001,
                                        'source_pixel_width': -7972583995898539989,
                                        'source_pixel_height': -693804305964083636,
                                        'rotation': -128704500337412246,
                                        'virtual_nw_x_pixel': -1767899787,
                                        'virtual_nw_y_pixel': -241143481,
                                        'virtual_width': -967881199,
                                        'virtual_height': -797753537,
                                    },
                            {
                                        'source_monitor': 8132719,
                                        'source_nw_x_pixel': -4813872212425434075,
                                        'source_nw_y_pixel': -1775554513722837044,
                                        'source_pixel_width': -5930684696289164664,
                                        'source_pixel_height': -8631184505965724415,
                                        'rotation': -8987514113998897742,
                                        'virtual_nw_x_pixel': -824086339,
                                        'virtual_nw_y_pixel': -1066152677,
                                        'virtual_width': -1601601676,
                                        'virtual_height': -210931552,
                                    },
                            {
                                        'source_monitor': 3885477,
                                        'source_nw_x_pixel': -1988524985436767934,
                                        'source_nw_y_pixel': -2646588086620821683,
                                        'source_pixel_width': -3787744408977176252,
                                        'source_pixel_height': -4160033718380319540,
                                        'rotation': -9001551056995225331,
                                        'virtual_nw_x_pixel': -1421437296,
                                        'virtual_nw_y_pixel': 1930730701,
                                        'virtual_width': -519847341,
                                        'virtual_height': -1406816058,
                                    },
                            {
                                        'source_monitor': 3896443,
                                        'source_nw_x_pixel': -5442999212124765588,
                                        'source_nw_y_pixel': -8567894192155243606,
                                        'source_pixel_width': -6405905734760894953,
                                        'source_pixel_height': -1129813364950272239,
                                        'rotation': -8456548032654579977,
                                        'virtual_nw_x_pixel': 1372095986,
                                        'virtual_nw_y_pixel': 131732726,
                                        'virtual_width': 1838013245,
                                        'virtual_height': 1384068929,
                                    },
                            {
                                        'source_monitor': 3661413,
                                        'source_nw_x_pixel': -3518312243996155254,
                                        'source_nw_y_pixel': -2686623320230732392,
                                        'source_pixel_width': -4497751470983589425,
                                        'source_pixel_height': -7871598592497625772,
                                        'rotation': -8156934615925414564,
                                        'virtual_nw_x_pixel': 731446947,
                                        'virtual_nw_y_pixel': 680938609,
                                        'virtual_width': -656366583,
                                        'virtual_height': -1639939660,
                                    },
                        ],
                },
                {
                    'description': 'ƥφ¹Ɗďԕ^ĕˣ\x82I҃ʓŵ)ҏǒʏˊŔƣƢĩτη¶ÿŢ<ԅ',
                    'monitors': [
                            {
                                        'identifier': 8584864,
                                        'width': 8314353006167617185,
                                        'height': -6099111982390406642,
                                    },
                            {
                                        'identifier': 7559420,
                                        'width': 6296154707500399054,
                                        'height': 6970480319465647494,
                                    },
                            {
                                        'identifier': 4822603,
                                        'width': -1560508471715291528,
                                        'height': 5770219368391618759,
                                    },
                            {
                                        'identifier': 1796836,
                                        'width': -5827216722255964610,
                                        'height': 8876782700890096304,
                                    },
                            {
                                        'identifier': 1325964,
                                        'width': 4177483556260587181,
                                        'height': -3243112540879973074,
                                    },
                            {
                                        'identifier': -449911,
                                        'width': 2779782828400125713,
                                        'height': 1036866274381104851,
                                    },
                            {
                                        'identifier': -676039,
                                        'width': 6295999375388014201,
                                        'height': -6207221526085500674,
                                    },
                            {
                                        'identifier': 2824265,
                                        'width': 4017141347831785341,
                                        'height': -6916663179354556331,
                                    },
                            {
                                        'identifier': 430992,
                                        'width': -2041514194904544196,
                                        'height': -1181465727793615852,
                                    },
                            {
                                        'identifier': 2066290,
                                        'width': 2350532982614684246,
                                        'height': -7450258808487702419,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7997470,
                                        'source_nw_x_pixel': -5987095682314455039,
                                        'source_nw_y_pixel': -2863536765931513623,
                                        'source_pixel_width': -4465245069063296938,
                                        'source_pixel_height': -8968162323108526776,
                                        'rotation': -8194797127129239199,
                                        'virtual_nw_x_pixel': -1325469232,
                                        'virtual_nw_y_pixel': -928498402,
                                        'virtual_width': -1516255713,
                                        'virtual_height': 1093479503,
                                    },
                            {
                                        'source_monitor': 6740777,
                                        'source_nw_x_pixel': -225307899301760069,
                                        'source_nw_y_pixel': -193298285382939921,
                                        'source_pixel_width': -702337857756298579,
                                        'source_pixel_height': -8656857267105719522,
                                        'rotation': -131964029239763939,
                                        'virtual_nw_x_pixel': -1604187517,
                                        'virtual_nw_y_pixel': 123391832,
                                        'virtual_width': 1653402872,
                                        'virtual_height': -1604578499,
                                    },
                            {
                                        'source_monitor': 6542324,
                                        'source_nw_x_pixel': -7251572673485379766,
                                        'source_nw_y_pixel': -1944866895280489073,
                                        'source_pixel_width': -6176455343419231351,
                                        'source_pixel_height': -8162169360350250847,
                                        'rotation': -229357763014394687,
                                        'virtual_nw_x_pixel': 1813112163,
                                        'virtual_nw_y_pixel': 1307154635,
                                        'virtual_width': -1772608073,
                                        'virtual_height': -1945612901,
                                    },
                            {
                                        'source_monitor': 3940153,
                                        'source_nw_x_pixel': -8159730933425837094,
                                        'source_nw_y_pixel': -815207070850709776,
                                        'source_pixel_width': -6159983646138573234,
                                        'source_pixel_height': -718248525222951277,
                                        'rotation': -5955315354766758847,
                                        'virtual_nw_x_pixel': -1706316103,
                                        'virtual_nw_y_pixel': -772526108,
                                        'virtual_width': 782762970,
                                        'virtual_height': 1299158487,
                                    },
                            {
                                        'source_monitor': 4773385,
                                        'source_nw_x_pixel': -5714032827109230402,
                                        'source_nw_y_pixel': -4691811029828539531,
                                        'source_pixel_width': -9083740043569190206,
                                        'source_pixel_height': -1749636992177292487,
                                        'rotation': -1342436296369295877,
                                        'virtual_nw_x_pixel': -946915565,
                                        'virtual_nw_y_pixel': -956506885,
                                        'virtual_width': 1357039800,
                                        'virtual_height': 614366,
                                    },
                            {
                                        'source_monitor': 9919766,
                                        'source_nw_x_pixel': -4409367099714886321,
                                        'source_nw_y_pixel': -946473723462433351,
                                        'source_pixel_width': -6969579709914723858,
                                        'source_pixel_height': -7748244214900319283,
                                        'rotation': -7098771451591134347,
                                        'virtual_nw_x_pixel': -12964458,
                                        'virtual_nw_y_pixel': -367694041,
                                        'virtual_width': -697614169,
                                        'virtual_height': 465748598,
                                    },
                            {
                                        'source_monitor': 5119015,
                                        'source_nw_x_pixel': -902882716596050261,
                                        'source_nw_y_pixel': -6842800822597218911,
                                        'source_pixel_width': -1580612648474233033,
                                        'source_pixel_height': -5321014125546994798,
                                        'rotation': -6009554242043118884,
                                        'virtual_nw_x_pixel': 1096909183,
                                        'virtual_nw_y_pixel': 1722389374,
                                        'virtual_width': -528031711,
                                        'virtual_height': -381257033,
                                    },
                            {
                                        'source_monitor': 884337,
                                        'source_nw_x_pixel': -4425445843023790475,
                                        'source_nw_y_pixel': -1482541218236808208,
                                        'source_pixel_width': -7520511986147632699,
                                        'source_pixel_height': -550307195395234352,
                                        'rotation': -7084626387768955284,
                                        'virtual_nw_x_pixel': -264666880,
                                        'virtual_nw_y_pixel': 1501377885,
                                        'virtual_width': 622043897,
                                        'virtual_height': -449878648,
                                    },
                            {
                                        'source_monitor': 3397038,
                                        'source_nw_x_pixel': -5389239304899224740,
                                        'source_nw_y_pixel': -7981430964856909678,
                                        'source_pixel_width': -8176376418916722859,
                                        'source_pixel_height': -543091177236268572,
                                        'rotation': -9134815120650688276,
                                        'virtual_nw_x_pixel': -1817563011,
                                        'virtual_nw_y_pixel': 426370266,
                                        'virtual_width': -372673693,
                                        'virtual_height': -14541413,
                                    },
                            {
                                        'source_monitor': 8266573,
                                        'source_nw_x_pixel': -5874629591456237028,
                                        'source_nw_y_pixel': -2932902457243009139,
                                        'source_pixel_width': -3028325655747804322,
                                        'source_pixel_height': -7564438252967021650,
                                        'rotation': -7746768455079775251,
                                        'virtual_nw_x_pixel': -1155566307,
                                        'virtual_nw_y_pixel': -1354886424,
                                        'virtual_width': -89795778,
                                        'virtual_height': -1192933423,
                                    },
                        ],
                },
                {
                    'description': 'k;ƅøϔ\u0381ѠΫȮ+ԡͶ\x88˨ѧÃ¹ǿȼGҀŗĞŇȐɭďȝǔƏ',
                    'monitors': [
                            {
                                        'identifier': -43151,
                                        'width': 954239193820043105,
                                        'height': 4172224469187100908,
                                    },
                            {
                                        'identifier': 5591924,
                                        'width': 2984832602683598203,
                                        'height': -2630602151830371291,
                                    },
                            {
                                        'identifier': 7114944,
                                        'width': 3266626850026953884,
                                        'height': -4960481951189157584,
                                    },
                            {
                                        'identifier': 9941836,
                                        'width': 3483507290099273559,
                                        'height': 637585152116703796,
                                    },
                            {
                                        'identifier': 9985414,
                                        'width': 226989350430164574,
                                        'height': 8202381963075220282,
                                    },
                            {
                                        'identifier': 1704059,
                                        'width': 1846304773532571653,
                                        'height': -9060348668672920659,
                                    },
                            {
                                        'identifier': 8829960,
                                        'width': -8515602611679271564,
                                        'height': -5596442105644778747,
                                    },
                            {
                                        'identifier': 5829748,
                                        'width': -6424008403020959463,
                                        'height': 406699495584955693,
                                    },
                            {
                                        'identifier': 779065,
                                        'width': -28841910684759122,
                                        'height': 2674987473590076812,
                                    },
                            {
                                        'identifier': 8785152,
                                        'width': -3453942424321498719,
                                        'height': -6705171463445115149,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3447015,
                                        'source_nw_x_pixel': -1250264123881214536,
                                        'source_nw_y_pixel': -9015726628004504444,
                                        'source_pixel_width': -320650611919765325,
                                        'source_pixel_height': -8872424866681523656,
                                        'rotation': -4923240386219712013,
                                        'virtual_nw_x_pixel': 1059501975,
                                        'virtual_nw_y_pixel': 1376479670,
                                        'virtual_width': -470324621,
                                        'virtual_height': 726654992,
                                    },
                            {
                                        'source_monitor': 1028463,
                                        'source_nw_x_pixel': -1605502058494838401,
                                        'source_nw_y_pixel': -7284455505920834505,
                                        'source_pixel_width': -3828596011843663947,
                                        'source_pixel_height': -6053031315441668978,
                                        'rotation': -4322782720653391455,
                                        'virtual_nw_x_pixel': -1815353913,
                                        'virtual_nw_y_pixel': -1849437896,
                                        'virtual_width': 807405441,
                                        'virtual_height': 785931545,
                                    },
                            {
                                        'source_monitor': 4218489,
                                        'source_nw_x_pixel': -6495177438053931752,
                                        'source_nw_y_pixel': -5228196843636324620,
                                        'source_pixel_width': -6185990236220441856,
                                        'source_pixel_height': -3971545959019552085,
                                        'rotation': -3259488677570551376,
                                        'virtual_nw_x_pixel': 146210448,
                                        'virtual_nw_y_pixel': 1122459947,
                                        'virtual_width': 1448039330,
                                        'virtual_height': 804006089,
                                    },
                            {
                                        'source_monitor': 5638828,
                                        'source_nw_x_pixel': -3967827405096514584,
                                        'source_nw_y_pixel': -5055421757024808563,
                                        'source_pixel_width': -8666469434702621574,
                                        'source_pixel_height': -3995594682290978091,
                                        'rotation': -5822149869699274763,
                                        'virtual_nw_x_pixel': 1619167173,
                                        'virtual_nw_y_pixel': 1406628278,
                                        'virtual_width': -1240161712,
                                        'virtual_height': -301397541,
                                    },
                            {
                                        'source_monitor': 2148026,
                                        'source_nw_x_pixel': -6367093525991196011,
                                        'source_nw_y_pixel': -5184571817836640920,
                                        'source_pixel_width': -1292920883364436860,
                                        'source_pixel_height': -8722906119182557424,
                                        'rotation': -8462179322283727242,
                                        'virtual_nw_x_pixel': 1780409632,
                                        'virtual_nw_y_pixel': 811476100,
                                        'virtual_width': 476227955,
                                        'virtual_height': -1454115675,
                                    },
                            {
                                        'source_monitor': 105624,
                                        'source_nw_x_pixel': -2011498308412659246,
                                        'source_nw_y_pixel': -8062699245428860939,
                                        'source_pixel_width': -7841295495399307931,
                                        'source_pixel_height': -2492414234788455391,
                                        'rotation': -675091860661073792,
                                        'virtual_nw_x_pixel': 1737349458,
                                        'virtual_nw_y_pixel': -700343916,
                                        'virtual_width': 1763138356,
                                        'virtual_height': 1133350682,
                                    },
                            {
                                        'source_monitor': 2881322,
                                        'source_nw_x_pixel': -8058818882741444245,
                                        'source_nw_y_pixel': -2757834221242118533,
                                        'source_pixel_width': -6315277387246286768,
                                        'source_pixel_height': -7904374440013503733,
                                        'rotation': -3594241386218409863,
                                        'virtual_nw_x_pixel': 943552386,
                                        'virtual_nw_y_pixel': 1370226029,
                                        'virtual_width': 99173058,
                                        'virtual_height': -1621178435,
                                    },
                            {
                                        'source_monitor': 7084308,
                                        'source_nw_x_pixel': -5252637495614633631,
                                        'source_nw_y_pixel': -5099831873013633059,
                                        'source_pixel_width': -1501131024729479644,
                                        'source_pixel_height': -5437213652873141617,
                                        'rotation': -426969341708855454,
                                        'virtual_nw_x_pixel': -1968304670,
                                        'virtual_nw_y_pixel': -1869315598,
                                        'virtual_width': 590772561,
                                        'virtual_height': 1888720940,
                                    },
                            {
                                        'source_monitor': 7453301,
                                        'source_nw_x_pixel': -3106931773741325922,
                                        'source_nw_y_pixel': -8969068410409697295,
                                        'source_pixel_width': -871528372532828609,
                                        'source_pixel_height': -9194778896113537758,
                                        'rotation': -2553451500935896961,
                                        'virtual_nw_x_pixel': 824372046,
                                        'virtual_nw_y_pixel': -1455503784,
                                        'virtual_width': 252651185,
                                        'virtual_height': -1200396570,
                                    },
                            {
                                        'source_monitor': 5075620,
                                        'source_nw_x_pixel': -2378726073817063291,
                                        'source_nw_y_pixel': -7997020585214242806,
                                        'source_pixel_width': -8686506130989902533,
                                        'source_pixel_height': -7128392706209223798,
                                        'rotation': -7502542185609693690,
                                        'virtual_nw_x_pixel': -1032617919,
                                        'virtual_nw_y_pixel': -906560852,
                                        'virtual_width': -176434485,
                                        'virtual_height': -1958159590,
                                    },
                        ],
                },
                {
                    'description': 'ćĿāóɩɭȬ҅ȰÙpʨ-˛ΟƫČĘ˒¯~ɤʆȺȎԁ_ΡɤǦ',
                    'monitors': [
                            {
                                        'identifier': 8637338,
                                        'width': 3658157097940362989,
                                        'height': -8841822957131266479,
                                    },
                            {
                                        'identifier': 5275068,
                                        'width': 2932447195551366708,
                                        'height': -2907031875818198981,
                                    },
                            {
                                        'identifier': 9481799,
                                        'width': 5818466091069556100,
                                        'height': 1532189476281938545,
                                    },
                            {
                                        'identifier': 9591031,
                                        'width': -8795931253807813113,
                                        'height': -4807196108522342214,
                                    },
                            {
                                        'identifier': 6030746,
                                        'width': -636047539302862968,
                                        'height': -8040797035916271035,
                                    },
                            {
                                        'identifier': 2898755,
                                        'width': -2235414537526324983,
                                        'height': -1266529454750075870,
                                    },
                            {
                                        'identifier': 7554246,
                                        'width': 7996899045651381286,
                                        'height': 592271795924654656,
                                    },
                            {
                                        'identifier': 8720283,
                                        'width': -613391578536715313,
                                        'height': 4221455839374628041,
                                    },
                            {
                                        'identifier': 4978462,
                                        'width': -366474799850591177,
                                        'height': 8030829990936880200,
                                    },
                            {
                                        'identifier': 8193778,
                                        'width': -5784143272938802386,
                                        'height': 8067112320044130242,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1354763,
                                        'source_nw_x_pixel': -3633694209894120800,
                                        'source_nw_y_pixel': -7854204041973998368,
                                        'source_pixel_width': -5371542204915500468,
                                        'source_pixel_height': -3850628052359109657,
                                        'rotation': -6702321902305359780,
                                        'virtual_nw_x_pixel': -31362325,
                                        'virtual_nw_y_pixel': 1353575301,
                                        'virtual_width': -866110924,
                                        'virtual_height': 618668209,
                                    },
                            {
                                        'source_monitor': 6897747,
                                        'source_nw_x_pixel': -2838731984158983547,
                                        'source_nw_y_pixel': -1338811985790246978,
                                        'source_pixel_width': -1748969576799328373,
                                        'source_pixel_height': -1580058875423074774,
                                        'rotation': -1050477869877885761,
                                        'virtual_nw_x_pixel': 410046284,
                                        'virtual_nw_y_pixel': 1854473867,
                                        'virtual_width': -340680398,
                                        'virtual_height': -454437767,
                                    },
                            {
                                        'source_monitor': 2717298,
                                        'source_nw_x_pixel': -6880402768029937162,
                                        'source_nw_y_pixel': -6002157414842531907,
                                        'source_pixel_width': -6810887572363281863,
                                        'source_pixel_height': -6214693914059140684,
                                        'rotation': -6655412351831219199,
                                        'virtual_nw_x_pixel': 1934167062,
                                        'virtual_nw_y_pixel': 241673600,
                                        'virtual_width': -1005447012,
                                        'virtual_height': -937763656,
                                    },
                            {
                                        'source_monitor': 6465880,
                                        'source_nw_x_pixel': -1908508071024935195,
                                        'source_nw_y_pixel': -7297499887353219953,
                                        'source_pixel_width': -3555670760777019814,
                                        'source_pixel_height': -8234704864097072610,
                                        'rotation': -3614204468635800622,
                                        'virtual_nw_x_pixel': 973480575,
                                        'virtual_nw_y_pixel': 102749221,
                                        'virtual_width': 1267681072,
                                        'virtual_height': -1829796967,
                                    },
                            {
                                        'source_monitor': 9822093,
                                        'source_nw_x_pixel': -2265124290843156143,
                                        'source_nw_y_pixel': -7086389155478543527,
                                        'source_pixel_width': -2075249591952079987,
                                        'source_pixel_height': -2982224935884939379,
                                        'rotation': -8965659221136286838,
                                        'virtual_nw_x_pixel': 465385592,
                                        'virtual_nw_y_pixel': 1201956539,
                                        'virtual_width': 170984428,
                                        'virtual_height': -415875623,
                                    },
                            {
                                        'source_monitor': 5057221,
                                        'source_nw_x_pixel': -869966059454352678,
                                        'source_nw_y_pixel': -6597554272574088329,
                                        'source_pixel_width': -6582521706727394103,
                                        'source_pixel_height': -7456472325308775934,
                                        'rotation': -8232273081971230130,
                                        'virtual_nw_x_pixel': 1276195182,
                                        'virtual_nw_y_pixel': -1053362458,
                                        'virtual_width': -801117550,
                                        'virtual_height': -1307888226,
                                    },
                            {
                                        'source_monitor': 6967123,
                                        'source_nw_x_pixel': -8596717888430993262,
                                        'source_nw_y_pixel': -7052967932482606134,
                                        'source_pixel_width': -183300498213086385,
                                        'source_pixel_height': -5439893620016191512,
                                        'rotation': -7738335105612309860,
                                        'virtual_nw_x_pixel': -1658960307,
                                        'virtual_nw_y_pixel': 1489803710,
                                        'virtual_width': -1047456636,
                                        'virtual_height': 605288693,
                                    },
                            {
                                        'source_monitor': 8016384,
                                        'source_nw_x_pixel': -7647916345896472400,
                                        'source_nw_y_pixel': -2582019054937072518,
                                        'source_pixel_width': -433748961207561952,
                                        'source_pixel_height': -775997690006043159,
                                        'rotation': -5856288704857829086,
                                        'virtual_nw_x_pixel': 366385001,
                                        'virtual_nw_y_pixel': 56807769,
                                        'virtual_width': -1250690596,
                                        'virtual_height': -1533030919,
                                    },
                            {
                                        'source_monitor': 714596,
                                        'source_nw_x_pixel': -5552438653736880334,
                                        'source_nw_y_pixel': -6590610655216049395,
                                        'source_pixel_width': -2192183045827620805,
                                        'source_pixel_height': -2918662877584022223,
                                        'rotation': -1986489181490403102,
                                        'virtual_nw_x_pixel': -635777358,
                                        'virtual_nw_y_pixel': -1476169196,
                                        'virtual_width': 699642966,
                                        'virtual_height': 877570452,
                                    },
                            {
                                        'source_monitor': 5242066,
                                        'source_nw_x_pixel': -7561285080780998101,
                                        'source_nw_y_pixel': -2322103836846180791,
                                        'source_pixel_width': -67398358401360902,
                                        'source_pixel_height': -8067672597631392317,
                                        'rotation': -9130161499823193185,
                                        'virtual_nw_x_pixel': 181756146,
                                        'virtual_nw_y_pixel': -44381781,
                                        'virtual_width': 917586062,
                                        'virtual_height': -983627560,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 1580835,

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
            'request_id': 2327385,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 8870447,

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
            '$': '˄ȵÐʬ\u0383ˬĭĈÐEȭͰӰϫɡʂŅȘĴǦŲGƝѡūэµ\u038bёѕ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8880618060228667946,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 205688.86112213263,
        },
    ),

    (
        'bool',
        {
            '^': 'bool',
            '$': False,
        },
    ),

    (
        'datetime',
        {
            '^': 'datetime',
            '$': '20220523:220036.478848:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ú˻hƮÝUƪĘв˧KЁÎʜЄΨʣǔƔʩ\x8fȩǱɤŒćș\x88\x8bĥ',
                'ǈ½ʕϘҕTƜȊϙǐʫʤɣɫπžԑˋ˥ȽʫϿΊҬɈӇƽʋΊа',
                '˱ˣӊŇЎĆåԚэƝǺϳŧɟǸӝɷ\x9dƿ\x93ŠȽȞxЬqԝrș҂',
                '҄ІЅƞǣɺҡŵѤ\x83ýĻιѤǭЌć҈ϢҜňίЇˁϢvŸĊpŜ',
                '˩ҢĜи\x86ɲ~ȎƥқϞʄЌǨѥ˴ӅӃĦЀ+ȳȺɒнϸϕȘMʔ',
                'ɀƼȔѿɀƣˇξ˥ҞɆ]ŝȐʾљȺӮ|гҝˊǖϖäїϡηĶŖ',
                'ǵϲ>ĐŋԞѹʩƺϪɛǜŭѹԫáԉ˳Ӂ҅ŸåħӯσȩɮʅɑӜ',
                'Ќҵ˙\x97ʹʛćʞʑϣĸ˞ŋğyáɚͺţԧҵɠϚԕҾʡʶсAɟ',
                'ϧņcè\x89ȳɳʦ×ȸқӰǫʤϦÀЏŰáƈmҙ>҂ƦЅSπηƜ',
                'ƹҬԭҘͱßѕNºĻZȈ˛ѽԑʰӛǵЮӗ˭ȮҬΖáŋ<ʬ҂ª',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                6312797591230788123,
                -3467812443427642309,
                7681848757440199314,
                4367486851321932427,
                -3237470988768154067,
                6496016445427183121,
                -9084257577787895460,
                8675292249244227574,
                1319206374932816991,
                -8083133076069860334,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                570017.6989399372,
                267060.74433625076,
                191020.75924984942,
                896854.1494274575,
                372143.92489219893,
                880968.2115615025,
                -89586.5275578196,
                567818.79656281,
                518274.7641568369,
                268125.0384623173,
            ],
        },
    ),

    (
        'bool_list',
        {
            '^': 'bool_list',
            '$': [
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220523:220036.483232:+0000',
                '20220523:220036.483324:+0000',
                '20220523:220036.483414:+0000',
                '20220523:220036.483502:+0000',
                '20220523:220036.483590:+0000',
                '20220523:220036.483677:+0000',
                '20220523:220036.483764:+0000',
                '20220523:220036.483851:+0000',
                '20220523:220036.483938:+0000',
                '20220523:220036.484026:+0000',
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
            'name': 'ʷфҏ\u03831ҪǰӘ\xa0ɔcӹ^\x9cˍҁӂ4Ҹ·ǝʜȲɼĪѿғƘEʷ',
            'value': {
                '^': 'float_list',
                '$': [
                    547410.9505059782,
                    328140.20334464486,
                    12176.071511016708,
                    327683.14032501925,
                    294573.8208155035,
                    149942.75258383216,
                    964114.5930487548,
                    889478.2958122995,
                    876585.6859832588,
                    15774.6424868857,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'L',

            'value': {
                '^': 'float',
                '$': 252328.97014662245,
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
            'catalog': 'Ʋʓ˜JIњςÜHӴɻԚćЏϼl\x9e\x8fҊƪҟюʞʾ×ξƻīрԭ',
            'message': "ӢˡǱ?\u0383ʅȝǸёћƒӆ'Ǹì$ƃχ|ΦȞҿɑɧɇͲɸÿϠч",
            'arguments': [
                {
                    'name': 'ұш:ȧȉƚķĩüɃЂјˎɁЪǰ%ə±ҵǑɖϿ\x83\x8dѦŋȘǸÔ',
                    'value': {
                            '^': 'string',
                            '$': 'Ͽ¯Ӝ˒Ľκùʊű˦ģ\x98ʛҝҾӑȱѹƔнԮƓϠQ.ʱ˷ЃҧѸ',
                        },
                },
                {
                    'name': 'ņѫƮɳ˓êŅ~ÉӄȧЦ~΄ЅɸΜы¦ȉһ·Øǉ\x7fԬɞƀʬΡ',
                    'value': {
                            '^': 'string',
                            '$': 'Ɲ\u0381ʙʊżDūЛ\x87ΩǩҴΡΣӃÐĐÔϋњƲΩȊ\x8dͱӑāŶϱǾ',
                        },
                },
                {
                    'name': 'ʷъ҃ψӡx\x8eÛ¬ԬϪÞŲºΕЃĕø\x90ӀbʜYhȜ\x82wõ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'Ѳ8ƭȿƪӔʾԀÿϞ§Ҳцԁƪo:҃0ȇЊ}Ѡө"ΤǮœʓģ',
                                        'ЍĊȢǶΙ˘Ԫ\u0382,ΨԤçȌƮѧт{ŤҼ¨ϛ˃эĥԆĦԥ˱ɢ˾',
                                        'ŻԛĔΡӤɏ·Ðд-Ҍːb\x89ɦѐŖɅ\x80юȢҎİʗƥɎƓѪɽƛ',
                                        'ĸĚžѝȦ\x86ÔșȼďŧʗΌÙΛǮʇ\x9bтѻӷĐͲǥ\xadӁϯӊǨô',
                                        '¼ŒӗɉȅʧНοӦiâɓϋԨЁɛðʣ\x89fǰKǩà@Рӻ\x8a\x96я',
                                        'ÖȗΏŖϓҎǫ\u0380ҾƉªɓԖ¦ʸ\x90JϜѯ\x9fƕҘÍȒːŲKȟӴҥ',
                                        '˾æүЍмɟԎƗЁǇϿƝƦȪŢ˩ʴҏˡˉ\u0381˭ɟҌĜҮĲɶȶɓ',
                                        'ēɦkĀì˫҄ǠęŻŧˈ˴ъ\u03a2ɚӆͿÄĔmʄdҳ+ʩż\x9bЯϩ',
                                        'ӁƋ¤ӘƲ;ÝɜÖҴƮР\u038b-¡ɐżӸӝΉùVĽԥҕӦϫPΊԧ',
                                        'ú}ũ҂ӵ\x98љ$ӚȌƱJϗΞҺTѡ˃ËИ\xadāʴ҆ÜUŶҥȵ˒',
                                    ],
                        },
                },
                {
                    'name': 'θ±ԀϴĂѓčp˵ɯŒЊҏͰ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        5308299104573491857,
                                        -5742027129970696881,
                                        -4087844339405451600,
                                        212965518712687823,
                                        -5872592804908869160,
                                        -4800762896695771558,
                                        5641497655592510385,
                                        2168234305579328826,
                                        -333353606629851264,
                                        3408592233071094069,
                                    ],
                        },
                },
                {
                    'name': 'ӖǛ\u038d\x92ăʳƶ±Ɨ°ѧʞOϊʆʮҷ³ǥ÷ˏ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ΗƀѼӂȕgҺŤtN\x8dĩʣ\x86ϵͳхÉÞ!Ѡ¸ǉðϞƽʡԬѳΚ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        469043.6949076699,
                                        168971.56375512487,
                                        387767.80824818276,
                                        589410.7489461802,
                                        844720.6454095774,
                                        -53826.98953002354,
                                        75639.87689481783,
                                        720542.4345441841,
                                        743202.8594932975,
                                        573245.8438265651,
                                    ],
                        },
                },
                {
                    'name': '\u0382ȟъĘΎЌóǥȧƵ÷èӟϲϢŹԌwвΨʟЏŦʣɍɳ°˓ѳ\x85',
                    'value': {
                            '^': 'datetime',
                            '$': '20220523:220036.473717:+0000',
                        },
                },
                {
                    'name': 'ӁӖΌȖҬқ\x87ºÜʽÁƸˍɡƟйů\x82ƨяYȶʮʔԛϡĤɽΫӰ',
                    'value': {
                            '^': 'float',
                            '$': 819356.7323048465,
                        },
                },
                {
                    'name': 'ӪĦqӯϋϴҧўɬý˸\x8fԀΛŚѻœϨǷǍ«þύ˼ЂkŦұҳW',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        712003.9453789102,
                                        38158.631563436444,
                                        366279.9863343866,
                                        -59630.051241432935,
                                        492032.1786765818,
                                        -98970.13133681683,
                                        487380.69174570334,
                                        898610.3894307559,
                                        -94070.89489635103,
                                        332184.11749119736,
                                    ],
                        },
                },
                {
                    'name': 'źϞ',
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

            'catalog': 'ԛş',

            'message': 'ɬ',

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
            'identifier': "ɝΏʷĥȢǇ-цò҆ǢԝΨŧ´'\x86ɀƤ\x97ȼǝеӆĸ\x9fϑԑȘƂ",
            'categories': [
                'file',
                'internal',
                'configuration',
                'access-restriction',
                'access-restriction',
                'internal',
                'access-restriction',
                'os',
                'network',
                'os',
            ],
            'source': '¼¥_ǛŬҢӯŴSǊˍϻ҄ϒčŉǝЬđˆʇзτӵӯΰПȧеǟ',
            'messages': [
                {
                    'catalog': 'ëΝ0ԡƁºλҙӑ҇ːϳRǤԈȚϥΔȽƓȚʶɷǰҹϢҦѐԣ\x7f',
                    'message': 'ʁЬҰįҷxƬ+tͶΕȲǵǡѮGțЖÔΓƘσ·ǋÓǊ+ҰĮȿ',
                    'arguments': [
                            {
                                        'name': 'ёǅь´иͺΏưЇÊ˫\x8cȈϳйyҩėƳЀȂпӢЪɵф',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.383476:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ɆӭϘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.383888:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѐ\\åÉɞȯtɽŁdÛˠǑѮдFŲͺ\x8aŰɽΜďĚ˼ĿcϺ¶Ƅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ļĲƫǡӱŦĐ\x94ɞʥŃƃΌvФѨϊƼжҧë˨ԗ·Åԕ˖Ǐεԕ',
                                                                            'ѷȕҟƙϿЊǘҝҳ\x95ϓς¥ƸoɿȓɞɄԬc©¯ҩѣ\x90ƩҎˏȮ',
                                                                            'ʫ:ũ˛ɖ\x87ʚßϙȺцϡėMԠʱѧАʼΞʁƍƄҏό\u03a2ȈԀ¹ƽ',
                                                                            '!ǍîɯŮ˩\x94ãwŤƀҼϸш\x90Ɛǆ¥Āͷú,Ѷa°˙~ěʢЊ',
                                                                            'ΌəҋͻcΚœÂԚʊÍŷǓʴϽЯӿʨѰ\x89Њĵ¤ȏʲȃtƌШǳ',
                                                                            'ΊѮŠэ¢ǶӫҎѨĹΓǞҶȹˌʛũìԌҲ\u0378џ\x9bȩзů³МѺЃ',
                                                                            'ĵșʞǭȁ\x93\x91ӇƱʅзƱЉ\x90~ĒъѧYαь`βҀĬƏ8Ӟʞϑ',
                                                                            '%nǲ\x84ҾˎЩǇЛǂÅȷĒŰЫƣΈКȨɝǦ)ǉҳώɃѓмˬĲ',
                                                                            'Ȣʥ~ԗ²ѱJҸԬӒʮɮӎ\x9dɷɲԑɮӞ3ϭϵ·yοˣΐҀҽй',
                                                                            'ĜøŚлѫЎʱЦʮќŞҝщƷѻɊɟ_Ůʲӧө7ɖήϰȏɫпČ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɉÑͷŘŲәʦ\x92ӎzЛ¸аϐϏӮʴҲϬӉрεҿǐ¬ҨҊ\x96Ӆĭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'VʳԆχϰϸ\x8e4ÂɻԠӎϲJßʉϫKȯɘҬǡȚʥÌʜӅѓǞ˄',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɂӉİȵɯЭ(\u0379ƬѨ\x88èӡˉǦǩ§ϱSǳʜŹÿβΑƷȍƧɮį',
                                                                            '',
                                                                            'ԭɖ˔Ĕϣ҉ĳǜ»ҠǿѺʉӑзƃϑӁŷ7ΠkǾȌɾԠ\x86гȋщ',
                                                                            '\x95ȓJǙӠĶbѓ\x99ŗƅɒđȰΊʤâkȟȐůɩ˕ȸҞ҇ҩ0ʒѨ',
                                                                            'ͶɻҋČ$ɏƸӽүғͻƵʹʹȞēɿѴң\x8a˷ņҾɦΰ\x83iʕː˸',
                                                                            'ʘćʝϦλʊÚˋˋƠ\u0380КΡԙӷɦҹʾȐѧfˤ˖ɶњģʓђɼԆ',
                                                                            'O<@˾í\x95пƳŌǁɴ\x91Ѯ˄ʛŵѝ°Ǻǿ6άƂʸȷŬъ˺һҡ',
                                                                            'Ö˧ԂɻɦIS˃ʱòyǮɄƱϣʯϾӍęҥʦƛΝʼNыùţ\x9dŔ',
                                                                            'ˉ˭×ŠǌϏϝ§ï˗ıƠɮĻϳϕ4æȧƦґƭ˹\x8aƦҖӯʒ(΄',
                                                                            'ɨҕͶȵʎȚɽс\u0378ɪÇɵÜ²ѱΧʑîǪζҬĺɤʒЪʧƠҚĆϏ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Óǉ\x7f҂ӡѮźΜИɛɰɄˋԣ¸ӵ.ϣ\x89Ӣ³ұŅƭ\x91ԓҨӦơ\x94',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɖнƀˍɑľˑЁɋ˫ǕīθΎu',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8235220141375597024,
                                                    },
                                    },
                            {
                                        'name': 'ǔԤӏȠАô©ǶϗҳϯȬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            108602.00500615619,
                                                                            196238.61305633973,
                                                                            153619.71590012725,
                                                                            787395.6592513853,
                                                                            902795.6348227784,
                                                                            362025.76026604977,
                                                                            331063.7666993802,
                                                                            947501.9383843939,
                                                                            144322.6921304943,
                                                                            714233.9310203429,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƁN',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.391038:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ãԑɶ9Ǆҵс\u038dɺƍúʧңнɊұƦϔÓʌ˞\x9cȆ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.391453:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÂҼæ',
                    'message': 'ҹˤχ\u0379ȳҒ˨ʿǟҲoͳɍĖɼɊҕʪfʴ˾ΫuȴϪǹǆɭҋԁ',
                    'arguments': [
                            {
                                        'name': 'Һҙ\\˭',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5711557788437832507,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '<ӎʪ9GҸ$ĂсԣŃϟȔΠĝ}Ϸ±ѥȄ\x90ːˣ}Ο\x8d!ǑXÅ',
                    'message': 'ʳňȹVĩːԩԠ<İ\x94ѸɜԓÄҫӼ\x87ԝͰPҎĞǎÀёɯӦʜƤ',
                    'arguments': [
                            {
                                        'name': 'ӖϡҪΉ˵ЊИЃёљ\x82˾ЭǐϽŅʸыϔƉŜϝSɹҒ͵ˢ҃ŵĊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '©ƠψęƮsʸЩ<ΡːиԈЬǘˮ9Û˦ϷɞˉϧÀӏB˷xҾŝ',
                                                    },
                                    },
                            {
                                        'name': 'љѤđĝRΦÃ×Ǝ\x98Ϫ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            163074.57323819102,
                                                                            -75709.92219900189,
                                                                            448423.64020856854,
                                                                            569604.3408011727,
                                                                            855227.4720709954,
                                                                            966585.2745290627,
                                                                            723401.1333532385,
                                                                            879586.9054037501,
                                                                            -33286.80082886008,
                                                                            632424.8968173724,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Żί\x82TØљİ˼ǏŋɬҘ¡ȱΧ\x92ƮÇʹ҉ƀϣĉϿɅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'áґКBȿψҦɀʹЧäɵсϜʧΤπΧ¨ҥɳŒϑѐ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
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
                                    },
                            {
                                        'name': 'ҖƕȖƕ˞҅ϽȂ˳ԋӳ\x94Ѹ\xad\\ȥɻӴÅǌѦі',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ҧԉѫ˜ÖȨŅχƨΦ8ōʥóˑȼǞ!ŋɑԮɨŎȽǢˇŗήʎņ',
                                                    },
                                    },
                            {
                                        'name': 'ĠÔɹ˼țāǹҪΰϛǮηд\x97ӋұÑȝаӻ˛ԒЉњϢ¨ͿΖƋҭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʃǜΘaˌϯԙ+Ҽаѥй',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            263714.23373655276,
                                                                            376371.7598416012,
                                                                            836698.9888114879,
                                                                            210815.76446354657,
                                                                            270778.4365993601,
                                                                            799342.9311063176,
                                                                            292157.6700283949,
                                                                            199301.34834984294,
                                                                            415692.641427615,
                                                                            718104.4880223393,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ưЎŤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.399225:+0000',
                                                                            '20220523:220036.399309:+0000',
                                                                            '20220523:220036.399416:+0000',
                                                                            '20220523:220036.399497:+0000',
                                                                            '20220523:220036.399576:+0000',
                                                                            '20220523:220036.399656:+0000',
                                                                            '20220523:220036.399735:+0000',
                                                                            '20220523:220036.399813:+0000',
                                                                            '20220523:220036.399892:+0000',
                                                                            '20220523:220036.399971:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϬѠЅјҮччΕYԉěŕԜɓӪ!ͲԔťӐѫı\x9fӧËƴz\x9eȹԘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 921883.4616137685,
                                                    },
                                    },
                            {
                                        'name': 'ɨǏ6τPɤӊƀЍ¬\x7fĀЖ\x90ǭʷÇˬȔɏļ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "?èϦ¾ԄļyˁќψƧȌź'ѯτǕхҫɤíцϫƭҠԠŮƟ˦Ӛ",
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǈʘɑУśԐ˩ӷȪŵʞѫʸбƻű˕өωЙ9ɑ',
                    'message': 'ӌζǌßюſӐſĻ˅ȓǹñTèӖӺ\u038d϶ѻņơβȀӡʭkГëҬ',
                    'arguments': [
                            {
                                        'name': 'σԓ>ȞĜҋŎ±ÉϋͿƖʇĥȀƺÜáƄƩHƼƯʉŇȸǔžԣÖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            176790.29049755447,
                                                                            817157.694219443,
                                                                            471434.9582900038,
                                                                            341300.7476654474,
                                                                            960471.1364991132,
                                                                            -84517.786664819,
                                                                            974941.621601932,
                                                                            238164.3142480853,
                                                                            612526.4803558192,
                                                                            777154.221103315,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʣеͷɻʿŉČ§hŵȂԓǏǍ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.403166:+0000',
                                                                            '20220523:220036.403256:+0000',
                                                                            '20220523:220036.403337:+0000',
                                                                            '20220523:220036.403417:+0000',
                                                                            '20220523:220036.403497:+0000',
                                                                            '20220523:220036.403576:+0000',
                                                                            '20220523:220036.403656:+0000',
                                                                            '20220523:220036.403735:+0000',
                                                                            '20220523:220036.403814:+0000',
                                                                            '20220523:220036.403894:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ';¼Ԅ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.404471:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ͷ˺ɣҿMүƓ¾ɚΠƱξӢԤÚÄ˃ȿȮсˮ\x8eԐäeƒә',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.404917:+0000',
                                                                            '20220523:220036.405000:+0000',
                                                                            '20220523:220036.405081:+0000',
                                                                            '20220523:220036.405161:+0000',
                                                                            '20220523:220036.405241:+0000',
                                                                            '20220523:220036.405320:+0000',
                                                                            '20220523:220036.405400:+0000',
                                                                            '20220523:220036.405478:+0000',
                                                                            '20220523:220036.405557:+0000',
                                                                            '20220523:220036.405636:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȉıν˭˳æŐ˙Ιʒ\x8cϪӿĪѯï',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ϳ8щÐ\u0383}(ȜĚ\xa0ɿԘHȳԧĸgұұǇȮ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -34489.137258507086,
                                                                            91445.42298812611,
                                                                            988396.4314393837,
                                                                            333721.1779577433,
                                                                            127681.67310845118,
                                                                            -77597.39801584493,
                                                                            203516.16006333777,
                                                                            -19312.781410603377,
                                                                            553441.2584764682,
                                                                            608281.956652428,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƩƝӋĔΣѷӮ˯ɤαȈɭνɲА±ƒӏԐɾƊӎʠƊҲԈɪąÜǦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            690924.0732598546,
                                                                            985131.1161232875,
                                                                            591633.3582958712,
                                                                            316577.7061651179,
                                                                            310172.6191646206,
                                                                            166405.20332973293,
                                                                            911831.8108138588,
                                                                            649900.5316580188,
                                                                            433260.66064120724,
                                                                            923657.9254583602,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѷԡǎqϒ»ԖѡĒÜΛȉí˟ʌ˞HǞˇ\x98ʸϬ]ȾѨҪ\x99Ȫ>Ɂ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.409063:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʋДҎÞӱĪ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            ' \x9dԭйʿӉБшԬԅΘіȫүǸӝӅΉ\\ЙʏӀӭЕǮԋǪӕӕӤ',
                                                                            'ϖӊ˘ǷɭĬɛƂįϱζŲȺČ\x83ºŚ<ŌØϙ҉Ĉɘΐ\x98ϗɒįӹ',
                                                                            'häYӑӗѤʘ¼ЎřÐҗı˒зԞӅȔŰӮƭǙúo¼ϔƿƖƀл',
                                                                            'ͰØ҉ʹʰ˘ӖϹͷŜ˝`Ӭ˓ʗȞ)ϒĺΘңșʚćƻʘ]ӡu\u038d',
                                                                            'Ý˖ƹ]ɗӶɇ»ŵcӡKҕǮÑEćљˮɖÃ7ȌӔȨэʛԑͶĶ',
                                                                            'Ī³ÛʪϽvȻȟɂҙȎѣ\x93ϬɿԗІϺԜƹȷЍæøϨЧÄśҘϢ',
                                                                            'ƽԪŀɤ\x99ɔǁұʃЖвĪǦǜԆ×ʇѺ˜#ԋ҈ŵ˸ʮΨāÎ®ә',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȯӈĝˮҒң҅ƧɎ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.410621:+0000',
                                                                            '20220523:220036.410707:+0000',
                                                                            '20220523:220036.410788:+0000',
                                                                            '20220523:220036.410868:+0000',
                                                                            '20220523:220036.410948:+0000',
                                                                            '20220523:220036.411027:+0000',
                                                                            '20220523:220036.411107:+0000',
                                                                            '20220523:220036.411186:+0000',
                                                                            '20220523:220036.411265:+0000',
                                                                            '20220523:220036.411344:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˛ɑɷ=®ũƯҺ»ϲԒӤȋ·єƥsӊ.^ɐôŤǮΑ0ѽŭńϓ',
                    'message': 'ҮąЫ˓úԋӊΩ\x9aΎ\x87Ǆ°\x81пʜȰǦʁĵɋόȨɓkɦКϭͲԒ',
                    'arguments': [
                            {
                                        'name': 'ǹǦƦϠӮĀƭ"ЦȺϹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 853500.988495363,
                                                    },
                                    },
                            {
                                        'name': 'ȷƪ˵ǔ2ƼүԝƻĜЏćźƒϠҙȘͷ¯ĠӉǛýĤǧɾ´џˊɵ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 67017.37364901742,
                                                    },
                                    },
                            {
                                        'name': 'ȉΊҗʛӃӰ(ʪϛƽơƲlҸ˼ŔѻКʧӃĔɕïſѸѠϜØԅѺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɮʿδʄƛЋǀ˹ЇɑǆLʔŨӀхÞʉ˽һȤԡԭϪь2ØƫǫƷ',
                                                    },
                                    },
                            {
                                        'name': 'ƧɚˏҲФϔǋқҰԈʹ˘oЕ˓ºʞƹΠӟӸYӲȚ!йϢȀԂ\x93',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -89149.16148164634,
                                                    },
                                    },
                            {
                                        'name': 'ĞłȨ§ĥϿ˲Ó6ϧȪ\x87',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ʳʒǍҺʛȨȧΔ\x95ʆǼƂʑ˜',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.415368:+0000',
                                                                            '20220523:220036.415457:+0000',
                                                                            '20220523:220036.415538:+0000',
                                                                            '20220523:220036.415618:+0000',
                                                                            '20220523:220036.415697:+0000',
                                                                            '20220523:220036.415777:+0000',
                                                                            '20220523:220036.415856:+0000',
                                                                            '20220523:220036.415935:+0000',
                                                                            '20220523:220036.416041:+0000',
                                                                            '20220523:220036.416121:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ρŎɞǖǶǯ1ɳȏźӦņӘШːζȎdƊ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.416705:+0000',
                                                                            '20220523:220036.416786:+0000',
                                                                            '20220523:220036.416866:+0000',
                                                                            '20220523:220036.416945:+0000',
                                                                            '20220523:220036.417024:+0000',
                                                                            '20220523:220036.417103:+0000',
                                                                            '20220523:220036.417182:+0000',
                                                                            '20220523:220036.417262:+0000',
                                                                            '20220523:220036.417340:+0000',
                                                                            '20220523:220036.417420:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԏѵж\u0381҆ȃ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.417996:+0000',
                                                                            '20220523:220036.418079:+0000',
                                                                            '20220523:220036.418159:+0000',
                                                                            '20220523:220036.418238:+0000',
                                                                            '20220523:220036.418317:+0000',
                                                                            '20220523:220036.418396:+0000',
                                                                            '20220523:220036.418475:+0000',
                                                                            '20220523:220036.418554:+0000',
                                                                            '20220523:220036.418633:+0000',
                                                                            '20220523:220036.418712:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˡ¸ĤѬьˑqȷ-цEʪЮӸ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1531255336354700724,
                                                                            4444562788743353374,
                                                                            -1902435659217763196,
                                                                            -8770779772021996696,
                                                                            4703618786765257752,
                                                                            1435916474542970455,
                                                                            -2652134165858830819,
                                                                            8175520912741605654,
                                                                            -6779160267711806652,
                                                                            583719102757623444,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ûф҈ɱȝӽĒƌ_ʌʹҵϫäˍЋưƀ˶ѕҬȭļÉҔϺӘƗͺÂ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 983193.706366156,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЁĔӫŧDїƫҿƜɎǻːŅå¹ȵ\x84ԏȱȘӽϚĉ\x99Ҿɰ˴ҤΉч',
                    'message': 'ǊĽɐkγʔϵ2ų°ӾťʑԠȑҥ\x9a\u0380˽ʖԕȘý\u038bҋĈÜνPƺ',
                    'arguments': [
                            {
                                        'name': 'ӻʙʥøǻƓθŘ$ЀȂХĮʆҚѣÙθ˪ЗčȢҲǖŘ)˶әĆĉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'вΐøʹǀȁŮʻѲӾþʇѮʟɔ˖ȸ=]ʴǝΐƩȺԙмŝƝ.ǒ',
                                                                            '^ԛĕǽǀԣȐΈĊˈӸΤ:yӣˢăMӸɸЖöшǚϘ,ҠΛĥҮ',
                                                                            'ÉůʧǱžʓģȣŜƉƭԂƴΕŶZϽİԣψǧ϶űǺĜɭďǼȳˈ',
                                                                            '@ΒԮŻѾÅɮϬϰх]¿ùΏĵ\x8bƓͼӾǜ\x9eʢC¡Ѳ˼ƃήϓɉ',
                                                                            'ϋ˖ɲȉѝĹ3ĲĮǾǿӤ˹ĕϭɊ҉ȹȅȚƫίКɘʫҋʪ|Уū',
                                                                            'ʠȇ§ƋʠҦκҖėd˔ɔ¦ǳɴz҇IrΉƉˢŹφFæǏ˹ȇǆ',
                                                                            'ҿɑЩЋĥԍľҥάʧƻ˚а¬ШȺѥʫǧĴȰԬLőɂΉɯѳˊӵ',
                                                                            'бԎӥԛѺĉűƸԌәʼ˔kҚŵѷĩǂȼB¡ȝмɏǝѼ˽ɷPñ',
                                                                            'ӲŘјəƱȠӈҷŵɾʯДЀэÝƞβưá\x87ϫǐζи¼ƢѠυ\x8eț',
                                                                            '!ȃòяҢӗӋƃӽˢ˻ӌȎū.ɰ˙ӕȿ҅ɗӸ\x9eπϲēӶ΅êѸ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'υȏϞÖѧĪӜ ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 371883.5206679525,
                                                    },
                                    },
                            {
                                        'name': 'ϔл\x81ԭͽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.423303:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʇѹϝ˯ВˁҖЏĸ˯ϭ\xa0ŕҍȦӯȪ\x89Ăӳ;',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x89ҾǡǾϗċ"ľґɪĹʌūŕмӋэƸ\x8aƔ\x85',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            746809.4717014736,
                                                                            454277.0174827231,
                                                                            851695.8511114445,
                                                                            492683.4940660548,
                                                                            443573.10300134216,
                                                                            -6277.401187521929,
                                                                            517952.962281115,
                                                                            600912.309398741,
                                                                            474611.1552327429,
                                                                            641239.9745747277,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƕ˭ĨȪѸʪŉƯϨńıӠ\x80Àгdλӻë\x92=Λԇ|ưôVĬŨˏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8807361174807971765,
                                                    },
                                    },
                            {
                                        'name': 'ľӌı˭āƳȾ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '«ӄәѲ\x99#ʯȬƯԧϱӅôѫĿʚǣ\x88ȬƍʝͻüΊdΡłÖ\x8bј',
                                                    },
                                    },
                            {
                                        'name': 'ϗ\x9aǿЅȝ˱6äΰ= Ȟȹ;ӲΆɾÝįϱƂчҮǃбϦН\x9bWѩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8586180803308788920,
                                                    },
                                    },
                            {
                                        'name': 'ć:ˌµʋğŉ¿ī\x96ʹЌÍňѕДɺýʓͱŋϘ¿ӨҋÎ>Ї҃Ȏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʒϳƑ$Ŷ¹ýNōǣӞοƤʄɹʀёϒʈӇƍɾѨȬªԕƳĒ>Ԏ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 887988.8851491308,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ØʾŐˠҞ\x97\u0382ϤӶȗäeů$µ\x7fҵ҅҈ǹƇȫěđєԘ҅˥ƾw',
                    'message': 'ʜāԦԌù҃ŷǤsï§Ԇ˳ƾʭ>ʭҩνАǐŋЫ&ʤöʆѹΝȟ',
                    'arguments': [
                            {
                                        'name': 'ÐӬ9ӂрżģŴǣËƛԠўΊːӁƈ6ȓȻʃϫΝѓΖPQ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.428767:+0000',
                                                                            '20220523:220036.428868:+0000',
                                                                            '20220523:220036.428960:+0000',
                                                                            '20220523:220036.429041:+0000',
                                                                            '20220523:220036.429120:+0000',
                                                                            '20220523:220036.429198:+0000',
                                                                            '20220523:220036.429278:+0000',
                                                                            '20220523:220036.429385:+0000',
                                                                            '20220523:220036.429476:+0000',
                                                                            '20220523:220036.429565:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xa0cɹëǫˁŭěȭϢsŧŘTªЭӼԛњŉȢӃгǀΆ˝эҝďʬ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            87023.10994308634,
                                                                            6249.416390953687,
                                                                            250426.53779487597,
                                                                            597461.6629949189,
                                                                            522076.79598732933,
                                                                            426099.2337686595,
                                                                            566544.0963317977,
                                                                            823261.6779917994,
                                                                            226482.77012950653,
                                                                            960845.8874500131,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'чʦƑԧӛ҈ӴSȤ\x9dрŖEGӫøςȡ\x94ѯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɩķҟщʵǛ\x9f/ϡƺиåӝĬґӅĒ\u0379@,ҙ\x81ƧǽɭſȘʒ\u038bҞ',
                                                    },
                                    },
                            {
                                        'name': 'ήӦ\x90ϐŇɣČɮӒԞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2553220879549982554,
                                                    },
                                    },
                            {
                                        'name': 'ƒӱ%ʺŎӯCƚĐȳÐǀUsӔѠҬӨʱ.Ƈ6лѷҖŏǴǫÒţ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -75855.91567415946,
                                                                            576757.7167270185,
                                                                            197565.8923871881,
                                                                            623011.3127023181,
                                                                            496315.2184396285,
                                                                            803209.133602321,
                                                                            915103.0712632654,
                                                                            264353.80721031904,
                                                                            82150.6260451161,
                                                                            577472.5024409802,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '5ϧİдǬҫ˞ŞĄRϸu5ϯsʊŧÛΌȺӲŧƻϬ?ĪҴʬԆҮ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǖ¸ĂFˠҌŞíԤɜ\x7f\u0380ѧù\x95ɏԖͼѶɄУYŢӞȮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.434272:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҳƯĩЊŠnϢÖʆј¹ȠȤFԚĸ\\ŭƳɮ\x88țӬуŀͻůʷν]',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.434694:+0000',
                                                                            '20220523:220036.434777:+0000',
                                                                            '20220523:220036.434857:+0000',
                                                                            '20220523:220036.434937:+0000',
                                                                            '20220523:220036.435016:+0000',
                                                                            '20220523:220036.435095:+0000',
                                                                            '20220523:220036.435174:+0000',
                                                                            '20220523:220036.435252:+0000',
                                                                            '20220523:220036.435351:+0000',
                                                                            '20220523:220036.435451:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'а˦ӛͻͲӚūӆăԢԘǙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƝƆҧЌȻɞѹȧџΏđϑυɍЙ\x94ЙϬ#Ю\x82ƒ~lʄȨg³ѽ¸',
                                                                            'ɿԖ˵ƼѠȕÜѩϮӚ˦mϏϱԎ͵ŭӴ˅\x87яs\x82,ɑǥĠіYӔ',
                                                                            '\u0378ʅв½ӦλɴưŇ˼°˩ѯǲΛ˚ʕ\x83Ł{ԂĽΟнʜɨǯұnҝ',
                                                                            'ӁˣӲĝ¤ԪȊăѭɹ0ԟϾϽȱʗБϙÂȚǇtĴ]ȢБ=ӊÙɩ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΞϯЁÊŰӀȪЂÀρЀϺя˲?τʲęːҭŹҗ³ϥƥ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȡПʥ8ϔӚƑǵΝƧӋѴηɧʠƺƍǍĉȴӈ?ˏҹΪɞʈϰǌɤ',
                                                                            'ԈЎȩ»ƔΦЙ\x7fӮȕˀǸӜ\x8cԕXɮԆȁɫЂå\x9dӧϰԄʑҨ҃»',
                                                                            '¨ċºӢʅşɗΈӔΙ˖ǘĠɤͻӒŜêйɏǜ?ƙѩԭӑλȉ\x89҇',
                                                                            'ʭψ6ԝ¥*Âǿ˯;ӝО\x81҅Ǟö˽жΦв«ôØSυÆǍԎǒϯ',
                                                                            'ˆġʑӐŤď\x81ϜѤɍһѕȄҊĀΓǲϺȅÍƭ\xa0åҰͶƦĉѪЭȒ',
                                                                            'ϗ;σ8Ņ¿ϿԖƚŃˡӊϣӿӳ\x81ѝ˶ɜĈÕѿϵϲѕźȫǲͲˇ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƝłúԕѦƂɡЙ×ȳȵӬʵεęĐпʚ(œđľìƽЌοӜ!Μ\u038d',
                    'message': 'ѯӺ¬ĔøĤǯʃѰċԍѬ\u0379ƈÝʅ˴ʆʫńҼ˕ҶԈђm˹ҌΜY',
                    'arguments': [
                            {
                                        'name': 'ȨǙĪĒϩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'dĈ×ӜŤäiѨҽɖé˘Ѽ°λșΛϜԐĆŤʛǧą{¼ԊѨġȷ',
                                                                            'ϖӂƬΞӲiҁ\x97ȂǵԄ˜3ȡýĻĞκǪȊԥǖӞЋ˧ǻњɣŻˀ',
                                                                            'ƒҟѻˈ!Ԫ0äКΞȔҫΧƚ\x96ҔȂϺŵ˧ɊȿɭԍȱM$ќǷό',
                                                                            'ԢϴȩȔɌљńˣ=ʴˣыêĥeƈΪӯbϥ³ӌʎŸΌΫ<ԢЂԍ',
                                                                            'џϧȻҺ҅Ũ;íеԃǃǞƝӉǒǚńƤ_ĸǢƶƨŧȁχ˃ѠӢÝ',
                                                                            '˱¢ЉɥÚԫðтŐˤж¾ҲҡʎTъϟǟΝȷЕҴɩx¿ǼʌҚӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ªäɲӗơɁУύҏ ǉҲԜҷȞ˷ί±ԎĘɡúςҭπ˝ԇХ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220523:220036.439530:+0000',
                                                                            '20220523:220036.439613:+0000',
                                                                            '20220523:220036.439694:+0000',
                                                                            '20220523:220036.439774:+0000',
                                                                            '20220523:220036.439854:+0000',
                                                                            '20220523:220036.439933:+0000',
                                                                            '20220523:220036.440013:+0000',
                                                                            '20220523:220036.440092:+0000',
                                                                            '20220523:220036.440172:+0000',
                                                                            '20220523:220036.440251:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x98ŢƳɖΓђʼΟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4585151425390476721,
                                                                            -7725167272777304158,
                                                                            -3477090937313535084,
                                                                            -2050230571714910164,
                                                                            -1500450469471433666,
                                                                            74187816931094849,
                                                                            2731575839278564908,
                                                                            7875964544602344038,
                                                                            2511247874286843805,
                                                                            -6194403646024266802,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǞмɁƵĂɾtНԒѧƑɼüȕǘ˦įԘϯ\x87ЎƐÃ-ʜʕǯɑΈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'şÞϞӶқԜ˅³ŗǚ`ǼŔҦ΅ÐϟȢȁʔ!ƲȔ˄ѹ/Ѐѩ\x86ʦ',
                                                    },
                                    },
                            {
                                        'name': 'НЅ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȺʙҺšoȓyӭ͵өӸŮ\x80ōѹªЎыϲˣƾ©˧ӤϫʼФҩˀĭ',
                                                                            'ίӛσ˂\x95ҵˏBϘʬĕʤȋťзҲŪD²åļԠØɄ\u0380бΉƵЉǦ',
                                                                            'ύӺђNԢȾŸȲӉƫƚʭíȥãҡˏàȰЙҷʁɞӠΪWȇəσͱ',
                                                                            'ыűĂҘѐӶ˱ȨǩȐāǷ˪е\x95ʪɑıÍɸˍʡƮó\u038bӣϜӽ@c',
                                                                            'Ԯt вĳθѡņͶэ˙ď,ԒԎєĵ$ƬĪ%¦®ƽĜ˶ԐϮϹΏ',
                                                                            '\x95ƾǱ§ÍѧѪϞɥ\u038dѝґſ\x8fӺӖѩ¦ʌúęЗ2˺ϐƻӷƐȑΧ',
                                                                            'Ř͵҃ɸŻѥЦӵʰЈòŋ\x87ɓЏΙżʋΊбĬ¼%ɞ8Ś˦1Ƃ˱',
                                                                            'ѧÊЭťΌŞхȣaȞэНҗԈżɆӀĊωШ¸ɌДѓňūàħѥӉ',
                                                                            'ӔΤ\x94ȍЗħɽ˜ԆҸʩŽɈΝȦγȱŰĕġĒѫŎˏS\x8cʿñɎŴ',
                                                                            'ʦΡѠϛӰƓ҆Ǧňȱе×ЭѭмɻΎЄ˷Ҫʆı6ЉTǭґƩцð',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҦȏɘϠʩʁ\xadЅϵƇѶĆӃ`ǬȡЃ\x91ӴŴ,ʹӗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ʉөfɫЁθȷŵԉŁɷȯ\x8dӏѣͻӳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                        'name': 'µDӰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 736068.3225291965,
                                                    },
                                    },
                            {
                                        'name': 'Ӭӄă×ӡ5ķѡŃÇӨ/ΈƂЫ/зѴȳƓЉ;ƔȘļňəѠĹɔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7055419614692125290,
                                                                            -855425108910054274,
                                                                            -3101170482878111671,
                                                                            -3753711905298529416,
                                                                            271721702426848646,
                                                                            -5461786807552109145,
                                                                            6006393529493050512,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x91șʢ\x88ùǝʏȁ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ʥϗ¹δƲԟĉ2ΰόŉ¾ӵΣŹμÈÿǊƤˌбæ˃чɈыҐϩœ',
                                                                            'лʷΓȌӐű\x83Pϩ\x91ƘәźΕ˻ѮїϠЯЇђȅɰɤɝҰɽɸϮǒ',
                                                                            'ҳϪ˯ȏƞİϴͱƪļе˱CʉʡЀͳ\x9bΕŋԥǛҺɷȰ\x81˟\u0383ӢƖ',
                                                                            'Ȃ˩ҖɳΌJ/ʪȱǕϐ¯ƫξΗӶĴѐӁÙȸсđǘǂҷãҡ´Ɯ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ҝCԨŘƁ\u0378υɭÄŖϕŗȝǿŎόȉϷ˫ʗԛȊɬÉȾӊǜƟƱǻ',
                    'message': 'ίĹ6ЗâÙ6°˪ªк¥?ˊÕʛ1иϟϭǡϘʽʟęÎÚԦӾV',
                    'arguments': [
                            {
                                        'name': 'ΥΜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            897645203785768792,
                                                                            -7121464533267892101,
                                                                            5208242613256349230,
                                                                            -2119550174496740760,
                                                                            5103952909734674021,
                                                                            4777528359705450373,
                                                                            156666431747299955,
                                                                            4407939234014485750,
                                                                            1586464299264309606,
                                                                            -7712815931959089128,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'jңɔöңϛɄ҂',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '\u038dʂɰѕж¼ϑr˒ˊ}ГǮԚГҮ5ЗȃϑĒĄљÍȲϒ\x98˵ΠǶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1404026987387109306,
                                                                            7584577269394759664,
                                                                            5380471974642699741,
                                                                            -8458852198870204615,
                                                                            5883641271908390202,
                                                                            -1039453938914293002,
                                                                            670659790945642860,
                                                                            184489526698420916,
                                                                            -6835568718058802965,
                                                                            1474724436447010185,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '|ѵƈШ-ϔĔ·[ǔóʛǕǅϥѭˋɏƷ\\ʕѡҙůɛȳWԏãι',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 9144150642262965013,
                                                    },
                                    },
                            {
                                        'name': 'ɻ<εЋȓƎӋƎɺѭӲҌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӂҹӪ˼²ѨȱȵҬϣ˒"˩ŨǏͶɲǓǼҞҏүԙɟGе;ȼβǟ',
                                                                            'ϒљ˲jѼ5ϖƣÉʊӹǧӪȷȿƩ҄ηƗȳˡ¶ҝȥѾȨʼ\x87ƨĮ',
                                                                            'ȧŏúŖȷēħ˴ǴЄNԝȡ\x9fGþ\u0382v\\ɞmƫ-:οэшɏŭƴ',
                                                                            'kԬĲŘЧȣҼ«Ϙ±\x9cϐù˗ίǻȮʦҧʃ¹ȍĨǰ˰Ƣҩ¤ʈK',
                                                                            'ȱȥӓίVDēʠÊȬ=Їǎ2ȃʝʚԕӏǞθ˹\x97ʩӮǀϱ\x97Rğ',
                                                                            '¯¾ӕQˎЅўǽΗҦŁǼһɒѯǆ\x8dǒԒҬεÈ˦\x9eYǳĝПǥ˅',
                                                                            'ҞKӸθȈ¥оα҃ɹζӆÔȿǦßҿԣӑәѧ£ёϚŸįΆȃϔǇ',
                                                                            'ĬaŹҎǒŠÐԤ˷\x95ɚƁωӨӣέĪЍмȸƟxÖԔʜʸ_ãǅҹ',
                                                                            '^ԝҪГЦЃ?΄Ȯı˔ҚǠȱƏАёÆYωhǃϴӲƬǸȬǝ҇Ǝ',
                                                                            'ʏ÷кƱӫíŖϐЛ¨ċΩѤк˲*ӯɺŉԪѪǌȳņźɁȀʝ\x9aƗ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͳĞΙϭηǀ,ѹŵİ˄Rӹ6ÈǼ\u0379ĜdʒƮυҁǧѽ%ѿAƒǢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 875574.5027296371,
                                                    },
                                    },
                            {
                                        'name': 'ҎΔζήʴŁ',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɽԢ¹LŽЍ͵sѕƲɫĜаǉÐϰΑВéĻŎȒɗуэǲƴ˝φǕ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '×ƚχϰ\x8cțcƉӯӄѫɜƇѭƖԑԡ£ʐѮŢ˸зǅĻͳ*όҋ¡',
                                                                            'ѰѱԀȦӾӭҪˀ5ƞŬU}έʋʀ΄ĭľԡȷǖɶĶϮļȣԁДԀ',
                                                                            'нϣɎ=ȊfԔľќǛΔҠǼФĩǝŏӾҳɬ¸İӎƀҋƯǵƀʔɱ',
                                                                            'ӌņÕȷɯɸƩ˃ǅǬ\x81ɎҵʝԄɓ)ŭ΄áǣ҇ңИɑόƁĖƄű',
                                                                            '϶Μ˅ŉƹųԇҏPʑȣŮŲȉΒɋƴ\x9bßҔ\x9eϕŊćͼaƃɟŘҼ',
                                                                            'ԦǶiъȲTɇɾ˟ωáƔȧÕȨяǟx\u0383ԉұƭҌ˸ĵԤĪĘ˨Ƶ',
                                                                            'ʨψĨȦΫÃҡȸӄı˲łҀȬǠъʃȺгӢçӑτ|џӪȝŕѓ-',
                                                                            'ūԙìǄX\x86ɐєҡӅʹԑ΅˰ƑϱǠ¢ӅRӷǓŋ\x8a˽ŲċϏʇӵ',
                                                                            '´ϰǵϠǺʹʩԕϏúϐѐxǴŬӭΥæώûĔĘŤć·ɽΠӓɪÏ',
                                                                            'Ǔ\x93ѽĲ΅§ȷҨʣͶ˨vʌìǌßӿѫЇԆǄǺzǸѽĞТʼŚͳ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȓцΝΈ˯ϦѥϼϽМƟ˶ʻXϴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.455826:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҥ˩$ϊÎǀʐΓθқҁѷˀħÓŭ§ΨăѨԗˠΪѧɠđȞȠčȑ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'Óy&ѣ˵ҲѬɿɂϯњɘΕϫƖ«Ѽ˽˙ƤѮ\x93\x87Nϰ!Ӻԕ*Ȏ',
                    'message': 'ҴƯ\u03a2δʅ ӢЀҀΊҪƗСɶѝŷɪϟmƮ˖Ԡã¸ƫ˞ĩ-Џɩ',
                    'arguments': [
                            {
                                        'name': '\u038bԨȿŎ˹ВʟȖʀӔθʸӛƭч\x92"ǔʬĔ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӜǄϬʀʜѳƍvқÆʴÊ\xadϲ҇ӷɄ\x94Ѩõɟșɧ\x96',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'җʄƭГԅºˤƱ˙čɂzʷ¾{3њΆŰȋ˵˗ýĨχμͺȰ\x9f˹',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220523:220036.459663:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ВѵĠȩҕԅӽeӆЊŶӽƦʴêхʈŸs[œǦϨßѣt«ɴ͵Ĉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'цűӇ˄œȟʻδɝɠ\x91ǍȄó]ƂZҹÓ7ÀȶƷƼŀŅƦ\x858ҁ',
                                                    },
                                    },
                            {
                                        'name': 'iČŀêǥϞ\u0381LY\x88ҸЧɭЏ·ɫЩŚБpɚɍȁʠÉOΒwƁZ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -9133909362201890680,
                                                                            1014788241649829042,
                                                                            6110997014507592236,
                                                                            -8411945593614173344,
                                                                            3303892498759725282,
                                                                            -8833032564476716675,
                                                                            -8217987299540757717,
                                                                            8234919406009433084,
                                                                            2841142037522615498,
                                                                            -1101339731697396595,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˸ԐɣɮԁҔҵѢҍϲόʼɶɕõƊȔˏΒӻȁū˾Κė\x8bЯOҴ(',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7046769015790927238,
                                                                            -573258767221297933,
                                                                            7959012173685885173,
                                                                            -4365698727709329395,
                                                                            7134639576705586594,
                                                                            -6637797875671352563,
                                                                            1311182727362563216,
                                                                            4206563611350089806,
                                                                            5206278620352809944,
                                                                            -3612380829727623601,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͽѬƚԖ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            231656.66698660067,
                                                                            495248.2151660415,
                                                                            138505.21961839998,
                                                                            757779.018174815,
                                                                            494077.17263263103,
                                                                            139213.6655261471,
                                                                            269763.0286977609,
                                                                            53764.42882066363,
                                                                            803300.1294264711,
                                                                            33348.672462742485,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӻѫ\u038b×ŲĿԉɃΚˢʊҘђɶӍӗīƁ˯\x8eұĵƖɛƣɃîıӍñ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            793121.2978914507,
                                                                            -82120.06275169212,
                                                                            109103.11290784692,
                                                                            205376.17836212832,
                                                                            147321.61988542686,
                                                                            462995.2966947652,
                                                                            -57484.91446221019,
                                                                            418101.90747004637,
                                                                            -56613.18312252996,
                                                                            535951.7695768217,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ðόŀ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˫ʲƝЀÜӨÓɥØíѤмяϛóȚӼԌϦӎћċưΤȘϳ¥ōRφ',
                                                    },
                                    },
                            {
                                        'name': '\x88ǄħԘèϓҀʻ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2842025886216321975,
                                                                            3146229764544352125,
                                                                            384613563280105494,
                                                                            2393516212063782949,
                                                                            5235989895673641675,
                                                                            3897852306797149366,
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

            'identifier': "ɓɗÕҿ'",

            'categories': [
                'network',
            ],

            'messages': [
                {
                    'catalog': 'þĝ',
                    'message': 'Ԩ',
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
            'request_id': 6412274,
            'error': {
                'identifier': 'ϾĺȩýӄƯѲʄ+ЭʭϹϭɻАӝīÎɲȖӍē;Xϭʽȱâf\x82',
                'categories': [
                    'internal',
                    'file',
                    'network',
                    'internal',
                    'os',
                    'file',
                    'network',
                    'network',
                    'os',
                    'os',
                ],
                'source': 'ŝ¸lʍӿɀǅȟЫќŽûĳʊȵвˁûĎɞѧӈǚԦĹōґ\x99¯ǰ',
                'messages': [
                    {
                            'catalog': 'Ă˫lɼӥ8ʹ˂ŒƙΐŉӤԣƀӒmĘԇҫǻÜϿöˊÄŃҋ\x83Ŧ',
                            'message': 'ɩӫ9ʵϢ\x8cǍɲīĄŦɲĻåī@ͶѴ˗ô©˻ѡdȤŲêҬƲϠ',
                            'arguments': [
                                        {
                                                        'name': '|ȑӹȷЈ×Ϋԥ ˕¶Ŀ1Ӣ΅\x84ӧԫӹUñѸƾХѷǵӎ˦ПĞ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʱʯɨƙΑȯԝ/°ɘɗҷԕҍжӭǁ@ǝѡǮɹ¨ɹDАԣԮϧˍ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ј2ҼʄλԈ˯ǠԪÈȬʶ҅ɋMΟǯϳіχƲ²ӊÞԕɱΩΕǍӄ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŗөLˊāӉƾǕ˯ȭØ\x9bŔĝȭö\x97˂·ƹӤΨөɁƨҲʭѳĶǏ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4591982921839817171,
                                                                        },
                                                    },
                                        {
                                                        'name': '˼ǰӻéҹҪҿʬ7ɥс˝ʐșϯѲћҔōȾʠʰϣǊыʌϨƨҷу',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĺǱʒԔӍʹҲuǐƭǇǭѻɈøÃЫƢФΠԗɷ\x99ώǄϽΏʁɚć',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7841635637993659847,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΧҼãЙúȗȿǤφń˱ҔҶηˤz\u0383ЭҎɑӻЉԚͽˏόҖƕƍ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƊơʩōΧ.ɹǹ ŅĨίŃź\x80;ӄʷĪĶǇҤӼ®˽ѯйά00',
                                                                        },
                                                    },
                                        {
                                                        'name': '8Ő÷˥ÝӾçʕfǻԒƺͳˁ΅ĕǎѻýƠӱÙѦǿȧȕʁǊƳǷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3133962511944991572,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǧ«ʊβԊ:˯ʟʩǀѼ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.340186:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'žĆԟŐʪƗ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.340587:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǽʸԂŘƱΥӂȉÈƜΜɧÞĚ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ҌòҺɪχӵ˲ĝˏϩЂΩİУº;ǙÝ',
                            'message': 'бʍ/ɪșǔvȘλǹσÇĢ¡ǕϺ˫ÁѩÑџӷǥͽӪţ\u0380ƸҏΣ',
                            'arguments': [
                                        {
                                                        'name': 'өř\x85ăǱƁʱýɮ\u0378ѥόĆυКʰѽӸԘ¿ӋΠľȱζ:ҡҟ˃ŀ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʯҦȸвʅǕäġɵźyĎɚƸԃώј=ƣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.342274:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʎÝΔʳ˧pҽȥƮʹ\x9a8TϒȲɾьʼ°ňʏ˧ƠσȊʠɤǤϤѸ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'àȔХҕД+ӃɪƇϭɵʌҲΦ\x86ѻқԧÇȚzӃÞȥӷЪҮϋɐԭ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɆĖѷɻćìϾ\x82zƋƩʣӲʪѮˢŗҲɷŸjъ¦±АǽȀʍηó',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΈҭǂѪВҴфрĵ\x8d һˊʇìҚνϴЊӂŵ˲͵Ï\u038dѻӼΟԜ˃',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӺήɌ¼ӚҶң\x96\x8cаɓϦȎ´сƦ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ţ§Ћ҈óÙʎкϋɡǙϵ4ÿʴŽԞůʈp\u0380Ϗ\x81μЫԩȈәΡú',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˼ʳʌľҠ҃ϞũʨƍŖкЂǼɧƳŊƜΜңŉˉΗ²ʩʸɢҮ:Ҷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.345129:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ºʣϊŻ˄ĎɼʉǖƭńԗѽǕǚIˎʍ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʸɥѼԀȓҮ˶ԣѮΝʆƾΟТbɜóʃКЄĶÒтɎI#\x8cӍçӢ',
                            'message': 'ϖωǋάӭ\x89ӇԝȿʆǷġҊӘΑʾǵԃǎ˭ŃƲǹĦIΨ\x94ťɮԭ',
                            'arguments': [
                                        {
                                                        'name': 'ҶƴϘKźǒƉ>ќɸÒʭɖƧ=\u03a2ˍȚ\x9fϖü¨ӊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϿҸŨтˣҽƈѠsʏ[ËϸЅƋҐø',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ʕD§¦ͽƮĲңǤ˄ɫʰоӏЉȚXϾϫѽʸ˒ȥϯʋı_Πϖԝ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Æ¯ǯ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'оüǍԮʃƙɌʬȦЙПѥͶǃțЩκ¥ǷҷƧʋϘgłĥСƀgΖ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -67304.0974830793,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹʬɂĦļψҦԎѰ˭ʂΡÛɝgȕˈǩǧԤZɪøԚɀʳƇćԃě',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǟTƕӃĆӎƺф¡ʙ˺=Ή˥JØ´ɽҍZˇɼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȝǙ³^ǵȥȖɄ\x8a;П',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƐѩΠʢλdȃӛʍʁTҪ%ҾĐÉȠрοʠǮGϰ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.349306:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝȇˀԑʽƶͲ¤ҼĂ?ϟҨΤ\x88҆і˃Ƈϸ#ԛ˕öʚҐπ҉¾Į',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 4989.614648264585,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǪɵǋԐĘѳ΅ĸ¸ѝɩȇő\u0382kώśЄǈԕ҉Ī',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '.\x7fŕǂÎĵɮίƴ}qQȋԀǰEԛʽЅԕҾĲњűƋžƛǭӸâ',
                            'message': 'ҎҰ½ԭ˳ːˊĤGϦâþҀϬҪuȹ{³ɯԠʻɖέˏӣ˸Ƕģή',
                            'arguments': [
                                        {
                                                        'name': 'Ѐ´ƏǇá҆ϰԩΌǟǺōȡӖƙԪrƃÆǸAȰɣϝ¥ҾǩҳʎЭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɵϗʂb¹Ԍ˖ө',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǔΈʑьЭěǴĞԗԄʎǺЦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'º˖Σ¿ϏҊƷҀϜˬŁȪȾͰʤ±ЉjǧĆɑƠǤǤϬˉϖ\x92ӫÑ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 891046.9330674208,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0380ГАğγļČ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -654341835295873,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŅͶþǭŴɼʿԐӔοƮІҁÀΓѯŅ˃Ѹɨ9ӈĴ˲ʜьҵ%ƮL',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǜʩԡǚ^ϹϰƝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѩˮ)[ΪηнӻϱǌД˟łγņƦƂğҦͽȦ\x90ŦҬȞƸ҄Ǚǌ½',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҳҵʄ˓ ɽҦτͷ҈Ϟýұǆǆ)ÍǓχŨɚ˧ҾǦƽ£΄ӫÃȧ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŽįʀŢԇɁǫΣʍђƘ˝pͻΐěĈ"Ψӈθҫ¬7',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇΩ˱!ʢ¦ǹʴƣZė¯үÔӭʹ#ЇȤî\x99',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʡóɟЎҲīҡŷʠƟɸΦѝϷ¸ǳČĎћƈxʉү',
                            'message': 'ǹҀϼοЖɾ®˦\x88ƟōJщ8ɎфƏ½Ő^ɂЎҷŮõŐĮ\x8e\u03a2ˋ',
                            'arguments': [
                                        {
                                                        'name': 'Ǫư}´ŕȳѴҗЂòʹƈ^ԐǛgїӭçԫ˻eʫÏ\x85ȁDʜǬɱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '5Ơεȁ\x9cǻĸ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'əʪϟЦƹ҇ŃɐѯŗɃȰҟԪҔϛíΗƒ˾хϯƅɨƔÆӔƽHĖ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.356330:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԁ\u0383ӚɁņƍǠȷ?ɫÖПѓσÝүXŃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.356725:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӞӃ\u0383ʩϲ$üßζŀєƻȱάИƤǍ0áːêŢk˅ǁΔǞŒͺ˛',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѶΰŃɶƸʹƏ\x94\x91Ǩɠʙƨϳǒ˲8\x91ÔŞΘź˝ρҎϳԦĨÖү',
                                                                        },
                                                    },
                                        {
                                                        'name': '5Ԭ¿Ҟ\x92ҡȍMУÞHӹ5ȶɯРϰȪÛ^ȲԤъΌѱɮƟБ˳Ƅ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5056899990437119862,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıοԎϻҞ«҉¯ʑʞˌȚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ˢą\x89юɴʽþƩîωϒʣĸÐǟʌȨԢӬӊŔԪɞΉһ\u0380\x96ƬѠO',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ï',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.358284:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϷˤĳȖϝӟʀӉʘ\u038bҕØҎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'љŝӴȔ0ǗźƳșvĚ\xa0ѸήïΗ»ЯĩυͶňoΩĨԂúҎ˪˹',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -1688410282037664778,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ǻǟς˚\x9fйцзӔʃԕёHŌίĬ\u0381ĭ˳˧wȿȘԃаÀʨ˭Ѥϗ',
                            'message': 'εʝĎѬΎɸʊ\x8dƬƣѱũɭЛ,ӕʠɶƮïʳӄ\x8bԧҶǞ3εİǤ',
                            'arguments': [
                                        {
                                                        'name': 'ÒŞҵØέ˛ůһèȄФȖǓ\x8aʬҖʹҥ¢ԨοИˑ¥4«°Оǵ6',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȭęšӠϫԌʜǅҶ\u0382ӵ\u0380§ҡОϾãɒϖʠӱˡɸ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˁɲʱõҜƥͱԩϜ˔цɒӺБŞǟvÄЍƟŃӄԫǧß͵хŘƫț',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌɠԍδ˛˨ЅǪΦŞԖʞȴƺ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2227081025743806481,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯɂĭԜԇǺӹʽƆɯ˕Ԫ˒öţП˅×}ЭҗɅýѼοҸőŋɖъ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ăɑ˝ԀǘɎԬɗæ\u038bЪƽΗӗĳɞ%ϻɧъ˻щĠ3ҧԐːϼӘѭ',
                            'message': 'φτȧÿӕƲαȆàůȋɊ4ǬѦƟӢӕ;ԝΏЭŽÿ>иҝеÞҝ',
                            'arguments': [
                                        {
                                                        'name': 's·ҿδˋȞ˒ˊԤ˃ʮȺң˓ĤţɌїƓǸфЦҞÖϖ˂ȌŐüѣ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¾Њ ϮsҕΐϡķːɷϛϳĥħųųʓѧңǞӼ)ԧ҆˅ёŏw',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġɞȠʪȟʍĄˬȒӸϟΧŻϷƃ\u03a2\xad\x94])˰˭ƟɖΚ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȸńʹѲĲŰͽțНńʦ¬ҩǳ˜ʆȚˮԟɎȚȇʢ^Р/ϕИ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'qə˦ԏӷҲИҵ»ƼѱôεøƵίӤq˺ҺȓР ƲӈʲŽœϑƣ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԕǲӵҭҟʹŰ͵ҪͱƎɊʎОԀΝԁĵƱÄι˻ԄθȌĄ%ǭЛҭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7754051551132961324,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϥʟ\x9fǾÞŜjɺӷСΗ2Ѫǵģ;\x8bҶɸ\x8dЏӿ~ԌӺſϸсѓѧ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѻc¾\xa0Ƿҹ˦уҨ΄ǋÚήƒԑʂ҈ǷӓΟșԔȃτɨɆÎfǤЉ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7094522153854576677,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņOΙǊ\u0378pź˒ϰΏ΄ŉΆbѡϮĒ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 174465.8675973722,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Щ¶p˙ǪтĔ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѽʦżǐѼѫSԁĚdȬĬұТЫƑȸSfǔςɋş_σλΖƯmϟ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'NȒÚĬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ԅź˔ɱʯΣõĤǆrðŻ ɨжϻƼȄkɨ\x8dԊǬũǒρȏ¦ϋ\x81',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ӸʛŤҶѩԟ˧œѿ˸ɪ\x84ĴӋÀîґΏ¡Ûěß5Úǂі\x9bȟɌq',
                            'message': 'ҥ˗Тʸαʸƙėů¾ǉϘŘѓǏÖϽkƪеȂƟŧÛѰɶèL÷Ɏ',
                            'arguments': [
                                        {
                                                        'name': 'ӬɈɯɀȟњˁώǇȻ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'БЅɢûӣǟÅTɹªƤЀɁ˷ͼšŠΤƤǩҏʩưąǩȭ϶ψ˱ʽ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 574672.2547046107,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻ\u038dͱǦӕӼɥƘ`ǅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƠҼԫѼҚϿƛǧԞƣǐМƫӾϐơϭΓҹϱЖӺČ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2980683112216527902,
                                                                        },
                                                    },
                                        {
                                                        'name': 'mƏæԎ˼ЮÁθa\x8fɥȂӣˈҩ\x82ɳWҹѩŻĴƧǕ\x98HŚуΔЁ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'мθÚáͶҀʽэ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȜΘƺ¦ƃȐɦżʤțÓŴϳƆ.ΒƄđӃϿϱѸˬГʘǤϯŋã˳',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӂ\x8cŒҸɨωήϱIůƍǴӖƠŦñҚˬÚӟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.369712:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '¥Ә;˧\x85ңΓʵũąʾʏ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӸϒˬEȤԃÛÏνɄǃƷѓ¨ӫҸӈƪіŧ\x8cϚҦɨ˴ɝЩά\x9dÀ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɬҟώòɇƼЂɱŰ\u0379ΎǀѤ˳ƂŚ=ͷʜԀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǳɷϦɕ$рԍ8qГÆϦǗ=О¤ҡNƁ˃˖ȋƒŶȨδԋ\x86Ƹǰ',
                            'message': 'Γĺ2\x9b§ňҘϕûúʙЮ\x9aăӇɸ?Ҵԥo¶ŪӶ\x8d\u038dѩԀǱƳ\u0380',
                            'arguments': [
                                        {
                                                        'name': 'ǷзĒȌҀǗƕɸɧЦѶȕͻўЎˬμß6Ő˗ɱħȽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˎšęҿˮʵļԇΆɯʓ\xad˅иЫԐżŚǉɖγʯѶΠå҈ƌӓͰȌ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŸǗŘʉĆƸmĻ+ǀҥфˠ$ҐȨ·ǷԔVЫӑÉΖВůϞɑSʹ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9aʰŖΦƯ\x99ê7ѫűӷźҴÛ\x9b»Ѝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8072051620922291162,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǾĝяŢκҘǤэрΤǰӵ6ҭȦўšаȽǢĕ;ǖԣϧʋӇ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 33204.928042920335,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҹəȼȉȀɼԐşƗʐƝƑ_ϏѭŲȧԘŕԫʨЫƪҺҰбѴҠÑϺ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĊӗçңұΞѽĝŒÒϬđѼΆζ˾Å\x81ЅŔœÛǇľͿʑϢ8ЇӸ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x84ɣĘÓǟǾJɠȈďсʑ\x85ΧǁƏϧ[ήϢ<¨\u0382#bʳёɣȰк',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '2˴ȣŭɠТϿʖ\x99ǘѺ˗ΠNĢſÊУƳ»',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6966763120142755422,
                                                                        },
                                                    },
                                        {
                                                        'name': '˧êЪêeÒҁ\\ϬΗĎ¨eˇǡ6ǸҁϢ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'φΗԒ"Ŭѝʢξcpȝˢ¸ƽРčțЛ˳ѐЭҗʦ˩Ņ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4304961614905400302,
                                                                        },
                                                    },
                                        {
                                                        'name': 'е°\x92ǲӴԀѷcҨbʤ·',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˥Û˶˺Ǽ¸Жʼs\u038bǑЃ\x85˽\u0383\x8b˨\x83ӥӶѰɒ8Ѷёɭ²]Ƨ˪',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'цφ΄ǻ\x7fļӳƆ·ҦŴΩ\x91ĥȒΘЉԖȏкΦҨĩÕʋĿȤǼǦѵ',
                            'message': 'ȂÞ1˂ǢcӢŉҗȷѥԀ/ɜӄѦҔӽѕȔΫ<ӕҎћӰгǮŖɧ',
                            'arguments': [
                                        {
                                                        'name': 'φԧ҇À\x8b^ÙƀʻԡȃͰƴԥ×æȚĲˆĻІԊ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˞ȅǕXӏоǛԅʎҪĀʫ\x85ԉı^ɷˊҾϩ(όHĸƻƢŋʵcȃ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¤ҧӀԝÈғ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.376689:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Њˁ˳ùʄҺŕ҂ʲеȿǮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '½ɍЕԭʭȷԆ҈ùǛͽ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'țǲÖԕ\u0381ʔόйģĚƭˤԍ\x86БІ\x8d˫ȩԁˁÛ˶\x9eƝΪөүɌǌ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'őѥΆԢMΘ¥ǯӢ;ȐȴұǘɓԈɡϫĺ˟υҵ˥\x80ΧУӲНƣԕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 972467.3506842672,
                                                                        },
                                                    },
                                        {
                                                        'name': 'κ˥ȌĤƼщӀýȺԣόů',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220523:220036.378271:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x8cǶбұŢŋ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 857619.5662598445,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӼѿžȤɺΒ˽ДʓɠѣǢ\x95σØɌȵ˙ŕȇɫД|òưČ·ÖƚÍ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁƄǃɳїͰԇ§ӱѝғěǟ\x8eRƇćϻæÎә',
                                                        'value': {
                                                                            '^': 'bool_list',
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

            'request_id': 4154932,

            'error': {
                'identifier': 'šӘͺЛT',
                'categories': [
                    'access-restriction',
                ],
                'messages': [
                    {
                            'catalog': 'ΝĄ',
                            'message': 'ϻ',
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
            'nw_x_pixel': -1557142483,
            'nw_y_pixel': -1348001196,
            'width': -7534506555107283970,
            'height': -8473916964205673909,
            'ratio_x': 5928461169331738292,
            'ratio_y': -7308818913219654270,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1878237823,

            'nw_y_pixel': 1211705263,

            'width': -8534380392347100270,

            'height': -8274853210383140605,

            'ratio_x': 7681681149801766121,

            'ratio_y': 686010751057985548,

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
                    'nw_x_pixel': 1054769096,
                    'nw_y_pixel': 751578643,
                    'width': -549551556912598095,
                    'height': -1352088932848505645,
                    'ratio_x': -186625174749855492,
                    'ratio_y': -8606988166091155203,
                },
                {
                    'nw_x_pixel': -1407372488,
                    'nw_y_pixel': -192028014,
                    'width': -6880432744798462163,
                    'height': -4377204276820483529,
                    'ratio_x': -7454829920255559117,
                    'ratio_y': 2993064746705152506,
                },
                {
                    'nw_x_pixel': 1640376955,
                    'nw_y_pixel': -1789900968,
                    'width': -6275308209568278962,
                    'height': -170027665297228630,
                    'ratio_x': -6397273128152487216,
                    'ratio_y': 4549263738769369207,
                },
                {
                    'nw_x_pixel': -147379937,
                    'nw_y_pixel': -996414461,
                    'width': -1331252970577047979,
                    'height': -7991672679679219308,
                    'ratio_x': -7014345347945144962,
                    'ratio_y': 1560929802682146286,
                },
                {
                    'nw_x_pixel': -511063859,
                    'nw_y_pixel': 579548085,
                    'width': -8226100076945091017,
                    'height': -3074763332175215963,
                    'ratio_x': 2192454155999825803,
                    'ratio_y': 2955156424178822217,
                },
                {
                    'nw_x_pixel': 367780655,
                    'nw_y_pixel': -643272093,
                    'width': -8085672677186504626,
                    'height': -2749376417676107417,
                    'ratio_x': 6913117640996924286,
                    'ratio_y': -3630500171265792295,
                },
                {
                    'nw_x_pixel': -948746229,
                    'nw_y_pixel': 155969587,
                    'width': -4754019927820870516,
                    'height': -3960206783455528819,
                    'ratio_x': 3395811328051652734,
                    'ratio_y': -2516931528021852533,
                },
                {
                    'nw_x_pixel': 1682988804,
                    'nw_y_pixel': -1415282124,
                    'width': -4634449314026914571,
                    'height': -3075295754833354708,
                    'ratio_x': -8480637019708038670,
                    'ratio_y': 2067723956362760865,
                },
                {
                    'nw_x_pixel': 1685014539,
                    'nw_y_pixel': 1073499654,
                    'width': -2610001851367847533,
                    'height': -8460249532798040432,
                    'ratio_x': 671950845099433355,
                    'ratio_y': -2726092433021935947,
                },
                {
                    'nw_x_pixel': 1415548175,
                    'nw_y_pixel': 1868658141,
                    'width': -753353012417086705,
                    'height': -2882161090279080231,
                    'ratio_x': 3381046591988293238,
                    'ratio_y': 2322183357523558651,
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
                    'description': 'Ρ\x83ѲŐĬʠÃǚѭ҃ԟcCМ«ϐįҳjӞҥɞʮč\u0380Ɗ7ɽ\x9eш',
                    'monitors': [
                            {
                                        'identifier': 5197300,
                                        'width': 6083496844557655347,
                                        'height': 1851573196684866080,
                                    },
                            {
                                        'identifier': 9585854,
                                        'width': -6945999843285354247,
                                        'height': 6592274620380513015,
                                    },
                            {
                                        'identifier': 8813201,
                                        'width': 4123788139462479007,
                                        'height': -4982870521260765029,
                                    },
                            {
                                        'identifier': 9888332,
                                        'width': 9037870188594445347,
                                        'height': -2203636656586128088,
                                    },
                            {
                                        'identifier': 9721351,
                                        'width': -5515877962795343219,
                                        'height': 2509808723299338426,
                                    },
                            {
                                        'identifier': 5443838,
                                        'width': -3759048461388930062,
                                        'height': -5262616356652170862,
                                    },
                            {
                                        'identifier': 1622228,
                                        'width': -545681364532084373,
                                        'height': 2511928668127225189,
                                    },
                            {
                                        'identifier': 5267187,
                                        'width': 4701972703659531096,
                                        'height': 8256221067832540610,
                                    },
                            {
                                        'identifier': 9963307,
                                        'width': -3347621668455177297,
                                        'height': 4381782097971576396,
                                    },
                            {
                                        'identifier': 1409388,
                                        'width': 1586415022038821441,
                                        'height': 8262368474713856242,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8714187,
                                        'source_nw_x_pixel': -3078372708434264036,
                                        'source_nw_y_pixel': -6469160154720583075,
                                        'source_pixel_width': -7726894792321037794,
                                        'source_pixel_height': -2196647403488821880,
                                        'rotation': -3066248801144482810,
                                        'virtual_nw_x_pixel': 1486580836,
                                        'virtual_nw_y_pixel': 1988243671,
                                        'virtual_width': -1149715420,
                                        'virtual_height': -1243287144,
                                    },
                            {
                                        'source_monitor': 3272292,
                                        'source_nw_x_pixel': -8549287818604092481,
                                        'source_nw_y_pixel': -3859597699807293589,
                                        'source_pixel_width': -8812023684092440757,
                                        'source_pixel_height': -1008627647464532187,
                                        'rotation': -2792433400185883157,
                                        'virtual_nw_x_pixel': -704898920,
                                        'virtual_nw_y_pixel': 590901817,
                                        'virtual_width': -778225932,
                                        'virtual_height': 968999534,
                                    },
                            {
                                        'source_monitor': 7878719,
                                        'source_nw_x_pixel': -7828089647817916662,
                                        'source_nw_y_pixel': -5271383872458081125,
                                        'source_pixel_width': -1910773705613238751,
                                        'source_pixel_height': -2008605018679348402,
                                        'rotation': -4464326091624587735,
                                        'virtual_nw_x_pixel': 1363475512,
                                        'virtual_nw_y_pixel': 1209385094,
                                        'virtual_width': 1179822193,
                                        'virtual_height': 994165759,
                                    },
                            {
                                        'source_monitor': 4396433,
                                        'source_nw_x_pixel': -7450563399351495642,
                                        'source_nw_y_pixel': -3545486000015303847,
                                        'source_pixel_width': -573189002628496704,
                                        'source_pixel_height': -8565764837277164217,
                                        'rotation': -6676806831142304845,
                                        'virtual_nw_x_pixel': 1150521784,
                                        'virtual_nw_y_pixel': 23411391,
                                        'virtual_width': 380634889,
                                        'virtual_height': 176783110,
                                    },
                            {
                                        'source_monitor': 4040709,
                                        'source_nw_x_pixel': -3299313345353136200,
                                        'source_nw_y_pixel': -3256424685284376599,
                                        'source_pixel_width': -4287391981640698074,
                                        'source_pixel_height': -4609816752089323848,
                                        'rotation': -2758883759388713799,
                                        'virtual_nw_x_pixel': 1717675000,
                                        'virtual_nw_y_pixel': -701294772,
                                        'virtual_width': -1376905706,
                                        'virtual_height': 241879386,
                                    },
                            {
                                        'source_monitor': 8092887,
                                        'source_nw_x_pixel': -6351083156482876705,
                                        'source_nw_y_pixel': -7050031585844811893,
                                        'source_pixel_width': -5229990828583863372,
                                        'source_pixel_height': -2528544542145061824,
                                        'rotation': -515421134540153109,
                                        'virtual_nw_x_pixel': 1277111708,
                                        'virtual_nw_y_pixel': -179619814,
                                        'virtual_width': -1888408066,
                                        'virtual_height': -560858457,
                                    },
                            {
                                        'source_monitor': 4184841,
                                        'source_nw_x_pixel': -1490579940032797542,
                                        'source_nw_y_pixel': -6295424626075050190,
                                        'source_pixel_width': -6904041559057155089,
                                        'source_pixel_height': -7620070469604707717,
                                        'rotation': -303796052003880868,
                                        'virtual_nw_x_pixel': 114906843,
                                        'virtual_nw_y_pixel': -685169227,
                                        'virtual_width': 1488926115,
                                        'virtual_height': 413247224,
                                    },
                            {
                                        'source_monitor': 28441,
                                        'source_nw_x_pixel': -9192498339813964091,
                                        'source_nw_y_pixel': -907551686757099934,
                                        'source_pixel_width': -5831437915327821097,
                                        'source_pixel_height': -4774884519774497576,
                                        'rotation': -7896524920556177758,
                                        'virtual_nw_x_pixel': 519692649,
                                        'virtual_nw_y_pixel': 1311099222,
                                        'virtual_width': -1427670333,
                                        'virtual_height': 259565135,
                                    },
                            {
                                        'source_monitor': 2823818,
                                        'source_nw_x_pixel': -6436383078386576039,
                                        'source_nw_y_pixel': -1915777522772125920,
                                        'source_pixel_width': -1443055545711117468,
                                        'source_pixel_height': -3404331976816514919,
                                        'rotation': -771416135775869000,
                                        'virtual_nw_x_pixel': 1461199841,
                                        'virtual_nw_y_pixel': 91651908,
                                        'virtual_width': 1919108037,
                                        'virtual_height': -13707029,
                                    },
                            {
                                        'source_monitor': 7803351,
                                        'source_nw_x_pixel': -7235947132113279578,
                                        'source_nw_y_pixel': -7248881528744097111,
                                        'source_pixel_width': -1256793349216237263,
                                        'source_pixel_height': -4818923051841863428,
                                        'rotation': -5224661568142985041,
                                        'virtual_nw_x_pixel': -1227744966,
                                        'virtual_nw_y_pixel': -97969737,
                                        'virtual_width': -1688217235,
                                        'virtual_height': -677253651,
                                    },
                        ],
                },
                {
                    'description': '2ƈͳ\x88ҿŉƑɃo0ҞDΧʟν½ŜMúʀȶΧƬĿZáɁԝǝǐ',
                    'monitors': [
                            {
                                        'identifier': 714306,
                                        'width': 2600264009789202552,
                                        'height': 1700585180118846785,
                                    },
                            {
                                        'identifier': 6854619,
                                        'width': -253280397875772666,
                                        'height': 4109719916496306577,
                                    },
                            {
                                        'identifier': 9664358,
                                        'width': 6017763198652633615,
                                        'height': 1314441718044327689,
                                    },
                            {
                                        'identifier': 8267544,
                                        'width': -7647842761066017227,
                                        'height': 3553765877690215244,
                                    },
                            {
                                        'identifier': 8268780,
                                        'width': 5044946044289077072,
                                        'height': -71931723533518059,
                                    },
                            {
                                        'identifier': 7036435,
                                        'width': 5653136713788478468,
                                        'height': 5256478856346705552,
                                    },
                            {
                                        'identifier': 8485519,
                                        'width': 2662195799635914995,
                                        'height': 5404667064169036153,
                                    },
                            {
                                        'identifier': 3451286,
                                        'width': -1888224174512493888,
                                        'height': -4073636609600400554,
                                    },
                            {
                                        'identifier': 6998031,
                                        'width': 6338945287321551771,
                                        'height': -5001830470871984112,
                                    },
                            {
                                        'identifier': 7776315,
                                        'width': 8256163958963168602,
                                        'height': 8499131989085508355,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 210359,
                                        'source_nw_x_pixel': -6898546098564660670,
                                        'source_nw_y_pixel': -5588916223295365309,
                                        'source_pixel_width': -940628276701323325,
                                        'source_pixel_height': -3463087781861925319,
                                        'rotation': -4443498565244480916,
                                        'virtual_nw_x_pixel': -397973160,
                                        'virtual_nw_y_pixel': 531489138,
                                        'virtual_width': -1305796905,
                                        'virtual_height': 954668374,
                                    },
                            {
                                        'source_monitor': 466332,
                                        'source_nw_x_pixel': -6378278706484475207,
                                        'source_nw_y_pixel': -2695585131475778533,
                                        'source_pixel_width': -4910696955943442369,
                                        'source_pixel_height': -7341927102721626150,
                                        'rotation': -2860191211525483056,
                                        'virtual_nw_x_pixel': -1501426134,
                                        'virtual_nw_y_pixel': 1437536646,
                                        'virtual_width': -1106055414,
                                        'virtual_height': -1093901146,
                                    },
                            {
                                        'source_monitor': 8937168,
                                        'source_nw_x_pixel': -8495768998032972547,
                                        'source_nw_y_pixel': -9190270374184085221,
                                        'source_pixel_width': -5865410189115402374,
                                        'source_pixel_height': -2127659960228368490,
                                        'rotation': -8177651924237661669,
                                        'virtual_nw_x_pixel': 1014417910,
                                        'virtual_nw_y_pixel': -1572954762,
                                        'virtual_width': -1328551167,
                                        'virtual_height': 427105909,
                                    },
                            {
                                        'source_monitor': 1341315,
                                        'source_nw_x_pixel': -8578980867057658269,
                                        'source_nw_y_pixel': -4061650372830661574,
                                        'source_pixel_width': -6224344434255696297,
                                        'source_pixel_height': -2852278963493678194,
                                        'rotation': -5670690554774411107,
                                        'virtual_nw_x_pixel': 709955583,
                                        'virtual_nw_y_pixel': 1986248780,
                                        'virtual_width': 413052586,
                                        'virtual_height': -536446965,
                                    },
                            {
                                        'source_monitor': 3750784,
                                        'source_nw_x_pixel': -5579907423933830360,
                                        'source_nw_y_pixel': -5065029307626545805,
                                        'source_pixel_width': -4416238466642907902,
                                        'source_pixel_height': -5090185837680611964,
                                        'rotation': -7882936130022984486,
                                        'virtual_nw_x_pixel': 319950754,
                                        'virtual_nw_y_pixel': 1588514431,
                                        'virtual_width': -998209745,
                                        'virtual_height': 344326248,
                                    },
                            {
                                        'source_monitor': 9247515,
                                        'source_nw_x_pixel': -5313304238439189111,
                                        'source_nw_y_pixel': -8984707596935317562,
                                        'source_pixel_width': -4244035343945283421,
                                        'source_pixel_height': -8763307955564861287,
                                        'rotation': -5598571888831330112,
                                        'virtual_nw_x_pixel': -1042485240,
                                        'virtual_nw_y_pixel': -1585200923,
                                        'virtual_width': 260727449,
                                        'virtual_height': -43391994,
                                    },
                            {
                                        'source_monitor': 499069,
                                        'source_nw_x_pixel': -5573395151268682027,
                                        'source_nw_y_pixel': -8851561314381579568,
                                        'source_pixel_width': -3516090152216891846,
                                        'source_pixel_height': -2444554814064555479,
                                        'rotation': -2749822003709362052,
                                        'virtual_nw_x_pixel': 468577265,
                                        'virtual_nw_y_pixel': -1063494563,
                                        'virtual_width': -881142309,
                                        'virtual_height': -1213564244,
                                    },
                            {
                                        'source_monitor': 8850864,
                                        'source_nw_x_pixel': -4304874994439962716,
                                        'source_nw_y_pixel': -7439125032050542926,
                                        'source_pixel_width': -8478794017672462782,
                                        'source_pixel_height': -6146574869672194134,
                                        'rotation': -3209686530006764909,
                                        'virtual_nw_x_pixel': -1020968622,
                                        'virtual_nw_y_pixel': -950073924,
                                        'virtual_width': 1888135822,
                                        'virtual_height': 676601218,
                                    },
                            {
                                        'source_monitor': 3801816,
                                        'source_nw_x_pixel': -7068499445341600477,
                                        'source_nw_y_pixel': -4651290910114250501,
                                        'source_pixel_width': -7192494519293886888,
                                        'source_pixel_height': -7444341666963869570,
                                        'rotation': -1287361201035508851,
                                        'virtual_nw_x_pixel': -1866595011,
                                        'virtual_nw_y_pixel': -1405687094,
                                        'virtual_width': -689532529,
                                        'virtual_height': 78121117,
                                    },
                            {
                                        'source_monitor': -309803,
                                        'source_nw_x_pixel': -4895623235191162938,
                                        'source_nw_y_pixel': -2838842380193300169,
                                        'source_pixel_width': -2986406883994792599,
                                        'source_pixel_height': -688332099128917116,
                                        'rotation': -5785383854117019435,
                                        'virtual_nw_x_pixel': -1682512648,
                                        'virtual_nw_y_pixel': -1929005070,
                                        'virtual_width': 795566865,
                                        'virtual_height': 514379551,
                                    },
                        ],
                },
                {
                    'description': 'ЇbѠɡИΗʗĬǾ˽DŲǄ˄υʮΤʟͳЬɠ\x9cȏ˔ΫљʊӀȹǂ',
                    'monitors': [
                            {
                                        'identifier': 2714713,
                                        'width': -1861486920090685723,
                                        'height': -2369314326841269504,
                                    },
                            {
                                        'identifier': 6692565,
                                        'width': 5476262623948847307,
                                        'height': -6735182251452699101,
                                    },
                            {
                                        'identifier': 5394794,
                                        'width': 621837139572576509,
                                        'height': -310480998607491696,
                                    },
                            {
                                        'identifier': 5808398,
                                        'width': -6248124824738610145,
                                        'height': 2468250782215008783,
                                    },
                            {
                                        'identifier': 7097552,
                                        'width': -8415973044781740620,
                                        'height': -1498993078832311311,
                                    },
                            {
                                        'identifier': 1040485,
                                        'width': 2658984259791522256,
                                        'height': -3131609419928304981,
                                    },
                            {
                                        'identifier': 5503539,
                                        'width': -1060738891320252829,
                                        'height': 4235694094517160361,
                                    },
                            {
                                        'identifier': 2683757,
                                        'width': 4954085110857965170,
                                        'height': 7827438372298894240,
                                    },
                            {
                                        'identifier': -381993,
                                        'width': -3317056774813262821,
                                        'height': 4366627247367293416,
                                    },
                            {
                                        'identifier': 8368502,
                                        'width': -7900717704696429909,
                                        'height': 8204307001458174630,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4023651,
                                        'source_nw_x_pixel': -2263939632823514036,
                                        'source_nw_y_pixel': -1714522280114436750,
                                        'source_pixel_width': -631732197005120053,
                                        'source_pixel_height': -78162128738754071,
                                        'rotation': -4355984633852375009,
                                        'virtual_nw_x_pixel': 191054687,
                                        'virtual_nw_y_pixel': 820812802,
                                        'virtual_width': -208660849,
                                        'virtual_height': -561543315,
                                    },
                            {
                                        'source_monitor': 474144,
                                        'source_nw_x_pixel': -9064861325284193688,
                                        'source_nw_y_pixel': -4111427110967036435,
                                        'source_pixel_width': -4238015112996098095,
                                        'source_pixel_height': -1257814587477098858,
                                        'rotation': -4222767298171965995,
                                        'virtual_nw_x_pixel': -208924348,
                                        'virtual_nw_y_pixel': 619806164,
                                        'virtual_width': -1011219186,
                                        'virtual_height': 985447407,
                                    },
                            {
                                        'source_monitor': 8230177,
                                        'source_nw_x_pixel': -8332281652791027001,
                                        'source_nw_y_pixel': -384080808585533200,
                                        'source_pixel_width': -847251692480016984,
                                        'source_pixel_height': -9081783372524501733,
                                        'rotation': -618221973019461075,
                                        'virtual_nw_x_pixel': 608872312,
                                        'virtual_nw_y_pixel': -1197391707,
                                        'virtual_width': 1453868461,
                                        'virtual_height': 1875091787,
                                    },
                            {
                                        'source_monitor': 5470574,
                                        'source_nw_x_pixel': -6161783212262385438,
                                        'source_nw_y_pixel': -2843561479106316054,
                                        'source_pixel_width': -5168895762594211222,
                                        'source_pixel_height': -6447753406601692216,
                                        'rotation': -6558371951365099423,
                                        'virtual_nw_x_pixel': -1483654281,
                                        'virtual_nw_y_pixel': -1823002713,
                                        'virtual_width': 289692526,
                                        'virtual_height': 1345891792,
                                    },
                            {
                                        'source_monitor': 3272743,
                                        'source_nw_x_pixel': -6416131306505725259,
                                        'source_nw_y_pixel': -798307942529294930,
                                        'source_pixel_width': -5567485890171940713,
                                        'source_pixel_height': -5736584126832177617,
                                        'rotation': -400889608240330051,
                                        'virtual_nw_x_pixel': -951055562,
                                        'virtual_nw_y_pixel': 759812608,
                                        'virtual_width': -1860540367,
                                        'virtual_height': 137848503,
                                    },
                            {
                                        'source_monitor': 7165289,
                                        'source_nw_x_pixel': -206254600063512721,
                                        'source_nw_y_pixel': -1484846551288836714,
                                        'source_pixel_width': -9022680522983512730,
                                        'source_pixel_height': -242710939175697487,
                                        'rotation': -309791681950732274,
                                        'virtual_nw_x_pixel': 1470818070,
                                        'virtual_nw_y_pixel': 460532980,
                                        'virtual_width': -1356324991,
                                        'virtual_height': 423935144,
                                    },
                            {
                                        'source_monitor': 2257755,
                                        'source_nw_x_pixel': -4620912914157165900,
                                        'source_nw_y_pixel': -2289132162127243928,
                                        'source_pixel_width': -2928849632963803919,
                                        'source_pixel_height': -3362283686373280183,
                                        'rotation': -8220947637559873936,
                                        'virtual_nw_x_pixel': 310551613,
                                        'virtual_nw_y_pixel': 1375038876,
                                        'virtual_width': 594156224,
                                        'virtual_height': -1211832144,
                                    },
                            {
                                        'source_monitor': 9557274,
                                        'source_nw_x_pixel': -8682532239717969701,
                                        'source_nw_y_pixel': -6866457639932062594,
                                        'source_pixel_width': -5883243475084387632,
                                        'source_pixel_height': -6989735617611315950,
                                        'rotation': -4717336246234850680,
                                        'virtual_nw_x_pixel': -1394496196,
                                        'virtual_nw_y_pixel': 1440702966,
                                        'virtual_width': -1992415308,
                                        'virtual_height': 1319744053,
                                    },
                            {
                                        'source_monitor': -230368,
                                        'source_nw_x_pixel': -5587182767682047700,
                                        'source_nw_y_pixel': -651527044725955118,
                                        'source_pixel_width': -1441545782505128065,
                                        'source_pixel_height': -1146649027160061007,
                                        'rotation': -1601418602641626304,
                                        'virtual_nw_x_pixel': 1878569765,
                                        'virtual_nw_y_pixel': 1179516563,
                                        'virtual_width': -1668316534,
                                        'virtual_height': -629162458,
                                    },
                            {
                                        'source_monitor': -686470,
                                        'source_nw_x_pixel': -4361889008552801111,
                                        'source_nw_y_pixel': -6620486988203373518,
                                        'source_pixel_width': -4081562711557329541,
                                        'source_pixel_height': -1607260415483918726,
                                        'rotation': -4155278929192914526,
                                        'virtual_nw_x_pixel': -697300502,
                                        'virtual_nw_y_pixel': -1168857325,
                                        'virtual_width': -998925037,
                                        'virtual_height': -464057018,
                                    },
                        ],
                },
                {
                    'description': 'ȡN\u0378NχЇɵʵ=n\x95˸ΩИw˃ăҎǝvʛɠ)ȐˉŮѓ±ì\x92',
                    'monitors': [
                            {
                                        'identifier': 2238368,
                                        'width': -8729438813411665567,
                                        'height': 4240203821143859335,
                                    },
                            {
                                        'identifier': 9222401,
                                        'width': 3575352542024196701,
                                        'height': -6599064817418958508,
                                    },
                            {
                                        'identifier': 9088392,
                                        'width': -692575499591561092,
                                        'height': -7862667870685080784,
                                    },
                            {
                                        'identifier': 5421154,
                                        'width': 9007411696367974971,
                                        'height': 3436935364575053904,
                                    },
                            {
                                        'identifier': -857787,
                                        'width': 460528546435559839,
                                        'height': 2011152112887791057,
                                    },
                            {
                                        'identifier': 3957561,
                                        'width': 4219041593332990790,
                                        'height': 5515882166777237842,
                                    },
                            {
                                        'identifier': 1457362,
                                        'width': 5094799364443224609,
                                        'height': 8386821235397671093,
                                    },
                            {
                                        'identifier': 7939201,
                                        'width': -3293285829565320802,
                                        'height': 2622695947764004604,
                                    },
                            {
                                        'identifier': 7790915,
                                        'width': 2435651835300711004,
                                        'height': -5931179639868655153,
                                    },
                            {
                                        'identifier': 4746334,
                                        'width': 9178918361385232207,
                                        'height': 994062960665565083,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9881170,
                                        'source_nw_x_pixel': -719075320634412269,
                                        'source_nw_y_pixel': -7870916943624125027,
                                        'source_pixel_width': -2838716471181434816,
                                        'source_pixel_height': -5123864321678896650,
                                        'rotation': -456489445942028358,
                                        'virtual_nw_x_pixel': 13546761,
                                        'virtual_nw_y_pixel': 1308034953,
                                        'virtual_width': 592994937,
                                        'virtual_height': -1666609770,
                                    },
                            {
                                        'source_monitor': 4782788,
                                        'source_nw_x_pixel': -4907358794313859968,
                                        'source_nw_y_pixel': -317219098981697024,
                                        'source_pixel_width': -1301502364243756992,
                                        'source_pixel_height': -2585411759273670878,
                                        'rotation': -7984764797221358234,
                                        'virtual_nw_x_pixel': -1246630065,
                                        'virtual_nw_y_pixel': 1723950957,
                                        'virtual_width': 677653283,
                                        'virtual_height': -1251868793,
                                    },
                            {
                                        'source_monitor': 1934901,
                                        'source_nw_x_pixel': -8734265073499691679,
                                        'source_nw_y_pixel': -1001448104205601917,
                                        'source_pixel_width': -2042632402070995918,
                                        'source_pixel_height': -3131005612997742875,
                                        'rotation': -6574145620156061885,
                                        'virtual_nw_x_pixel': 1061286340,
                                        'virtual_nw_y_pixel': 1051841699,
                                        'virtual_width': -710175560,
                                        'virtual_height': 1249059451,
                                    },
                            {
                                        'source_monitor': 6377533,
                                        'source_nw_x_pixel': -4665027471149874118,
                                        'source_nw_y_pixel': -3772882416418642065,
                                        'source_pixel_width': -6236158153442113275,
                                        'source_pixel_height': -1025015010833128854,
                                        'rotation': -1520620603519280053,
                                        'virtual_nw_x_pixel': -1104913348,
                                        'virtual_nw_y_pixel': 1429692956,
                                        'virtual_width': 1685225524,
                                        'virtual_height': 1027442032,
                                    },
                            {
                                        'source_monitor': 991489,
                                        'source_nw_x_pixel': -1545625558790828328,
                                        'source_nw_y_pixel': -6863205432141444566,
                                        'source_pixel_width': -7325422694970534349,
                                        'source_pixel_height': -8748815933102436356,
                                        'rotation': -5684315698827312335,
                                        'virtual_nw_x_pixel': -1948496818,
                                        'virtual_nw_y_pixel': -934458950,
                                        'virtual_width': -1165967033,
                                        'virtual_height': -215632150,
                                    },
                            {
                                        'source_monitor': 8318673,
                                        'source_nw_x_pixel': -7051099846799530984,
                                        'source_nw_y_pixel': -1773239099458728356,
                                        'source_pixel_width': -207978356396479938,
                                        'source_pixel_height': -7212387247224381205,
                                        'rotation': -8330541751230745696,
                                        'virtual_nw_x_pixel': -497645322,
                                        'virtual_nw_y_pixel': -1689669353,
                                        'virtual_width': -1933514980,
                                        'virtual_height': 594765537,
                                    },
                            {
                                        'source_monitor': 1447555,
                                        'source_nw_x_pixel': -3159604407642068026,
                                        'source_nw_y_pixel': -216315147536260870,
                                        'source_pixel_width': -1914208172016511267,
                                        'source_pixel_height': -8191453508449943350,
                                        'rotation': -7433055416801822102,
                                        'virtual_nw_x_pixel': -1728544305,
                                        'virtual_nw_y_pixel': 1941787739,
                                        'virtual_width': 1679480131,
                                        'virtual_height': -564481950,
                                    },
                            {
                                        'source_monitor': 3822910,
                                        'source_nw_x_pixel': -9033937829812210861,
                                        'source_nw_y_pixel': -7439739536097173195,
                                        'source_pixel_width': -97172277943007514,
                                        'source_pixel_height': -7556821299127197017,
                                        'rotation': -3299792053514259856,
                                        'virtual_nw_x_pixel': -195426063,
                                        'virtual_nw_y_pixel': 570801601,
                                        'virtual_width': -1097904532,
                                        'virtual_height': 1809071248,
                                    },
                            {
                                        'source_monitor': 1495676,
                                        'source_nw_x_pixel': -6157725966892197899,
                                        'source_nw_y_pixel': -3272043293430907362,
                                        'source_pixel_width': -2183172193204831863,
                                        'source_pixel_height': -1311348953529081798,
                                        'rotation': -8071396494638036732,
                                        'virtual_nw_x_pixel': -646820358,
                                        'virtual_nw_y_pixel': 1423592832,
                                        'virtual_width': -1898849293,
                                        'virtual_height': 1168231327,
                                    },
                            {
                                        'source_monitor': 9342025,
                                        'source_nw_x_pixel': -8134264795261362162,
                                        'source_nw_y_pixel': -7518314622982890192,
                                        'source_pixel_width': -1042735030275499311,
                                        'source_pixel_height': -5583558926628412163,
                                        'rotation': -5672660849899829737,
                                        'virtual_nw_x_pixel': 1456892264,
                                        'virtual_nw_y_pixel': -1447940611,
                                        'virtual_width': 1912237228,
                                        'virtual_height': -128907161,
                                    },
                        ],
                },
                {
                    'description': 'í\x91Ђɜ\u03a25ȔʨȨȮ+ȀõϜϨƽјÃζʠɊϲĚȢиΪҪӣõҷ',
                    'monitors': [
                            {
                                        'identifier': 4907510,
                                        'width': -4247308572682900056,
                                        'height': 8710228346771344647,
                                    },
                            {
                                        'identifier': 8683734,
                                        'width': 6895482555238156549,
                                        'height': 8470649709344460838,
                                    },
                            {
                                        'identifier': 9587597,
                                        'width': -8303995894431322917,
                                        'height': -5234828137505299100,
                                    },
                            {
                                        'identifier': 5156571,
                                        'width': 8635065844697481356,
                                        'height': -2825362243386028062,
                                    },
                            {
                                        'identifier': 2295821,
                                        'width': -6827092343237651820,
                                        'height': 3473078604120879235,
                                    },
                            {
                                        'identifier': 6754021,
                                        'width': -1473438294404103279,
                                        'height': -5917044050497512060,
                                    },
                            {
                                        'identifier': 7598669,
                                        'width': 1587468286868806246,
                                        'height': -9213354278133427316,
                                    },
                            {
                                        'identifier': 8604096,
                                        'width': 5322996471436982213,
                                        'height': -8210647121698541451,
                                    },
                            {
                                        'identifier': 8467235,
                                        'width': 4623013026974633027,
                                        'height': 8367363774370384590,
                                    },
                            {
                                        'identifier': 1727319,
                                        'width': 640959529454240133,
                                        'height': -2508072668601002178,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4659709,
                                        'source_nw_x_pixel': -8792426648423947360,
                                        'source_nw_y_pixel': -6953535840728914421,
                                        'source_pixel_width': -9085484313587564952,
                                        'source_pixel_height': -2809472366979505763,
                                        'rotation': -2235621069456367294,
                                        'virtual_nw_x_pixel': -1632518837,
                                        'virtual_nw_y_pixel': -890904968,
                                        'virtual_width': -1136239910,
                                        'virtual_height': 853696198,
                                    },
                            {
                                        'source_monitor': 1458695,
                                        'source_nw_x_pixel': -368313571663192219,
                                        'source_nw_y_pixel': -1304690828171482742,
                                        'source_pixel_width': -3258981201018337149,
                                        'source_pixel_height': -9096207666142246773,
                                        'rotation': -1572278685145397154,
                                        'virtual_nw_x_pixel': -1789571192,
                                        'virtual_nw_y_pixel': -1361930920,
                                        'virtual_width': 1696806234,
                                        'virtual_height': -1215691152,
                                    },
                            {
                                        'source_monitor': 8171591,
                                        'source_nw_x_pixel': -3791862813008223396,
                                        'source_nw_y_pixel': -4746822257910216828,
                                        'source_pixel_width': -7988213225966764240,
                                        'source_pixel_height': -194363032420681590,
                                        'rotation': -1156544957617108537,
                                        'virtual_nw_x_pixel': -30807219,
                                        'virtual_nw_y_pixel': -377540853,
                                        'virtual_width': 1600151944,
                                        'virtual_height': 201274697,
                                    },
                            {
                                        'source_monitor': 3703115,
                                        'source_nw_x_pixel': -1565205424761111183,
                                        'source_nw_y_pixel': -4776828645448831662,
                                        'source_pixel_width': -5638073444142866803,
                                        'source_pixel_height': -1332663420036739832,
                                        'rotation': -7660850652889748694,
                                        'virtual_nw_x_pixel': -1221203778,
                                        'virtual_nw_y_pixel': -584601092,
                                        'virtual_width': 529525346,
                                        'virtual_height': -1646538576,
                                    },
                            {
                                        'source_monitor': 6618243,
                                        'source_nw_x_pixel': -3896205795334456794,
                                        'source_nw_y_pixel': -1303857934774486962,
                                        'source_pixel_width': -3923595529598134844,
                                        'source_pixel_height': -1640341184651773673,
                                        'rotation': -6110725177142770867,
                                        'virtual_nw_x_pixel': -453329642,
                                        'virtual_nw_y_pixel': -77669217,
                                        'virtual_width': 175832046,
                                        'virtual_height': -816256763,
                                    },
                            {
                                        'source_monitor': 1740758,
                                        'source_nw_x_pixel': -2870290049887225425,
                                        'source_nw_y_pixel': -8465543985152871275,
                                        'source_pixel_width': -5789230279067523667,
                                        'source_pixel_height': -7806757509044913267,
                                        'rotation': -841380765104905089,
                                        'virtual_nw_x_pixel': -737985748,
                                        'virtual_nw_y_pixel': 602718378,
                                        'virtual_width': 1239141308,
                                        'virtual_height': -292140243,
                                    },
                            {
                                        'source_monitor': 557743,
                                        'source_nw_x_pixel': -1322782138104092490,
                                        'source_nw_y_pixel': -6752697851897516724,
                                        'source_pixel_width': -1270244427129799803,
                                        'source_pixel_height': -1234356202788894877,
                                        'rotation': -1927779887491064748,
                                        'virtual_nw_x_pixel': -1807303556,
                                        'virtual_nw_y_pixel': 653088683,
                                        'virtual_width': 1419739248,
                                        'virtual_height': 750930118,
                                    },
                            {
                                        'source_monitor': 6316018,
                                        'source_nw_x_pixel': -6002655121341130353,
                                        'source_nw_y_pixel': -1489678223200687440,
                                        'source_pixel_width': -2556989894873940635,
                                        'source_pixel_height': -6417621493203474003,
                                        'rotation': -8069171600873810355,
                                        'virtual_nw_x_pixel': 1069315013,
                                        'virtual_nw_y_pixel': -242661073,
                                        'virtual_width': -176629761,
                                        'virtual_height': -1153804862,
                                    },
                            {
                                        'source_monitor': 4461705,
                                        'source_nw_x_pixel': -3655485543121998195,
                                        'source_nw_y_pixel': -643420135789748404,
                                        'source_pixel_width': -275858146861258560,
                                        'source_pixel_height': -1980098969177775360,
                                        'rotation': -540433879024770315,
                                        'virtual_nw_x_pixel': -1729612312,
                                        'virtual_nw_y_pixel': 1000760640,
                                        'virtual_width': -951765448,
                                        'virtual_height': 1679021386,
                                    },
                            {
                                        'source_monitor': 3483692,
                                        'source_nw_x_pixel': -3010604815998409890,
                                        'source_nw_y_pixel': -2358968281799024446,
                                        'source_pixel_width': -5172610489628349347,
                                        'source_pixel_height': -7369486350004869024,
                                        'rotation': -3454167344444324276,
                                        'virtual_nw_x_pixel': -37076434,
                                        'virtual_nw_y_pixel': 1784176217,
                                        'virtual_width': 764248487,
                                        'virtual_height': 1223222341,
                                    },
                        ],
                },
                {
                    'description': 'ŧƖàɲÒ˸ҲÙΐńsŅõϩβÙŚ˥ȃǩŏ¯В£ǥɻϻ\x83Ғǉ',
                    'monitors': [
                            {
                                        'identifier': 8546915,
                                        'width': -6124691667579779133,
                                        'height': 7044589293200236707,
                                    },
                            {
                                        'identifier': 6151696,
                                        'width': 6088229264212870890,
                                        'height': -6040135551710305895,
                                    },
                            {
                                        'identifier': 8525762,
                                        'width': -6488203322817805278,
                                        'height': -5565815497816643405,
                                    },
                            {
                                        'identifier': 8075691,
                                        'width': -2253041192601603541,
                                        'height': -7048276213659211247,
                                    },
                            {
                                        'identifier': 4836966,
                                        'width': 346140308351450969,
                                        'height': -2731486112042463843,
                                    },
                            {
                                        'identifier': 1775484,
                                        'width': -3425701825929872510,
                                        'height': -795918879852380897,
                                    },
                            {
                                        'identifier': 4738967,
                                        'width': 6970364379396034931,
                                        'height': -6955241247116678808,
                                    },
                            {
                                        'identifier': 7643864,
                                        'width': 8790326779200036388,
                                        'height': -3595252325034436347,
                                    },
                            {
                                        'identifier': 3916482,
                                        'width': -6093625289702292205,
                                        'height': 6420180945549696978,
                                    },
                            {
                                        'identifier': 7396841,
                                        'width': 7685758484549885507,
                                        'height': 4465061400303717426,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7464785,
                                        'source_nw_x_pixel': -8596950498153588760,
                                        'source_nw_y_pixel': -3634772776503450692,
                                        'source_pixel_width': -7468568543576360295,
                                        'source_pixel_height': -3840023799506210951,
                                        'rotation': -7459726191905822262,
                                        'virtual_nw_x_pixel': 1216397179,
                                        'virtual_nw_y_pixel': 1111225385,
                                        'virtual_width': -112958438,
                                        'virtual_height': -985391292,
                                    },
                            {
                                        'source_monitor': 5528122,
                                        'source_nw_x_pixel': -5410395930636614365,
                                        'source_nw_y_pixel': -418559132520937643,
                                        'source_pixel_width': -5864010760539918733,
                                        'source_pixel_height': -248400552630820848,
                                        'rotation': -686816002440509172,
                                        'virtual_nw_x_pixel': -998963546,
                                        'virtual_nw_y_pixel': -1422099967,
                                        'virtual_width': 1558149896,
                                        'virtual_height': -1257551899,
                                    },
                            {
                                        'source_monitor': 2157713,
                                        'source_nw_x_pixel': -6766498536270185364,
                                        'source_nw_y_pixel': -1834086256698074292,
                                        'source_pixel_width': -8867191170246928719,
                                        'source_pixel_height': -8768173892136597131,
                                        'rotation': -2378844785989649466,
                                        'virtual_nw_x_pixel': 1455460079,
                                        'virtual_nw_y_pixel': 376491546,
                                        'virtual_width': -965964900,
                                        'virtual_height': -947107322,
                                    },
                            {
                                        'source_monitor': -860978,
                                        'source_nw_x_pixel': -3879360116613842678,
                                        'source_nw_y_pixel': -3891333311319872923,
                                        'source_pixel_width': -167965134962246572,
                                        'source_pixel_height': -1455224914701269697,
                                        'rotation': -1621520800880357064,
                                        'virtual_nw_x_pixel': -1205597837,
                                        'virtual_nw_y_pixel': 39690936,
                                        'virtual_width': 1649253131,
                                        'virtual_height': 826835630,
                                    },
                            {
                                        'source_monitor': 1514215,
                                        'source_nw_x_pixel': -7548275764472633525,
                                        'source_nw_y_pixel': -1097484459023738702,
                                        'source_pixel_width': -1985411958802264207,
                                        'source_pixel_height': -5904613679374702489,
                                        'rotation': -2139890969753054883,
                                        'virtual_nw_x_pixel': -26120834,
                                        'virtual_nw_y_pixel': -231987286,
                                        'virtual_width': 301126202,
                                        'virtual_height': -682212001,
                                    },
                            {
                                        'source_monitor': 8456649,
                                        'source_nw_x_pixel': -5714092930940624255,
                                        'source_nw_y_pixel': -6666051607397100441,
                                        'source_pixel_width': -3545959201550393667,
                                        'source_pixel_height': -5352809840727099086,
                                        'rotation': -3791295075794717459,
                                        'virtual_nw_x_pixel': -1179458006,
                                        'virtual_nw_y_pixel': 612735966,
                                        'virtual_width': -68307345,
                                        'virtual_height': -1405402585,
                                    },
                            {
                                        'source_monitor': 3821030,
                                        'source_nw_x_pixel': -5971616031640979526,
                                        'source_nw_y_pixel': -3937763428200932409,
                                        'source_pixel_width': -3851723010819937342,
                                        'source_pixel_height': -534564298578105094,
                                        'rotation': -4776575802987495811,
                                        'virtual_nw_x_pixel': -334170092,
                                        'virtual_nw_y_pixel': -944546580,
                                        'virtual_width': -493753545,
                                        'virtual_height': 187744787,
                                    },
                            {
                                        'source_monitor': 8127045,
                                        'source_nw_x_pixel': -7317423228815468797,
                                        'source_nw_y_pixel': -4492090706317606070,
                                        'source_pixel_width': -5516671945673755487,
                                        'source_pixel_height': -156259024602839845,
                                        'rotation': -1198988740148676866,
                                        'virtual_nw_x_pixel': -643480565,
                                        'virtual_nw_y_pixel': -1392499083,
                                        'virtual_width': -499625030,
                                        'virtual_height': -285258130,
                                    },
                            {
                                        'source_monitor': 4833148,
                                        'source_nw_x_pixel': -2696664759104556335,
                                        'source_nw_y_pixel': -3165551693746745460,
                                        'source_pixel_width': -5385712374534558514,
                                        'source_pixel_height': -8166635161183147570,
                                        'rotation': -3921856052646834194,
                                        'virtual_nw_x_pixel': 1126679650,
                                        'virtual_nw_y_pixel': -1515890193,
                                        'virtual_width': 1473135315,
                                        'virtual_height': -1361351742,
                                    },
                            {
                                        'source_monitor': 8873258,
                                        'source_nw_x_pixel': -661197973632624857,
                                        'source_nw_y_pixel': -8657743708330411300,
                                        'source_pixel_width': -8525087661768037038,
                                        'source_pixel_height': -4280762061206690761,
                                        'rotation': -7387917775242638441,
                                        'virtual_nw_x_pixel': 973606534,
                                        'virtual_nw_y_pixel': 475619566,
                                        'virtual_width': -1464767526,
                                        'virtual_height': -587570103,
                                    },
                        ],
                },
                {
                    'description': 'ʔ\x8eηʲįΑϓŅӲɠюˆġԩȔļ˰ĄĽĩ\x9cɼʣԄƌċ˻ҹʇƞ',
                    'monitors': [
                            {
                                        'identifier': 7320914,
                                        'width': 8698788103389310196,
                                        'height': 1404317291592054474,
                                    },
                            {
                                        'identifier': 3246694,
                                        'width': 2513838240794102946,
                                        'height': 8229943557484864607,
                                    },
                            {
                                        'identifier': 668644,
                                        'width': -4163774502680411555,
                                        'height': 8240707242775643603,
                                    },
                            {
                                        'identifier': 768678,
                                        'width': 574375132732673769,
                                        'height': -4125247549166591148,
                                    },
                            {
                                        'identifier': 3983097,
                                        'width': 2278293290033965264,
                                        'height': -5851843708003866269,
                                    },
                            {
                                        'identifier': 2845658,
                                        'width': 1650018893575039278,
                                        'height': -7702866944475736148,
                                    },
                            {
                                        'identifier': 7195143,
                                        'width': -6194682007856154912,
                                        'height': -1680541386089257206,
                                    },
                            {
                                        'identifier': 1664058,
                                        'width': -2335596444177919593,
                                        'height': -1012498897917437055,
                                    },
                            {
                                        'identifier': 2844619,
                                        'width': 1046960920937474991,
                                        'height': 4980694152843632347,
                                    },
                            {
                                        'identifier': 2080022,
                                        'width': 1514506363588782942,
                                        'height': -375499284703849341,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7727159,
                                        'source_nw_x_pixel': -8931309493772557767,
                                        'source_nw_y_pixel': -3250597898734997565,
                                        'source_pixel_width': -4003809840786710868,
                                        'source_pixel_height': -4555866176805253456,
                                        'rotation': -6799553908358207018,
                                        'virtual_nw_x_pixel': 1549672937,
                                        'virtual_nw_y_pixel': 1439928562,
                                        'virtual_width': 1221931464,
                                        'virtual_height': 1364243071,
                                    },
                            {
                                        'source_monitor': 6452370,
                                        'source_nw_x_pixel': -1977431003316462359,
                                        'source_nw_y_pixel': -2899322461171065892,
                                        'source_pixel_width': -5986601375183390098,
                                        'source_pixel_height': -7664119697822717438,
                                        'rotation': -3065606088317418012,
                                        'virtual_nw_x_pixel': 1937617074,
                                        'virtual_nw_y_pixel': 338004473,
                                        'virtual_width': 1906059485,
                                        'virtual_height': -1782256636,
                                    },
                            {
                                        'source_monitor': 7588759,
                                        'source_nw_x_pixel': -4714945911193644904,
                                        'source_nw_y_pixel': -1927614597200199179,
                                        'source_pixel_width': -8268730530556464057,
                                        'source_pixel_height': -8820565928124504050,
                                        'rotation': -5424772786051655318,
                                        'virtual_nw_x_pixel': -1084912992,
                                        'virtual_nw_y_pixel': -425449455,
                                        'virtual_width': -924183468,
                                        'virtual_height': -1319855001,
                                    },
                            {
                                        'source_monitor': 4465198,
                                        'source_nw_x_pixel': -7942000461094075787,
                                        'source_nw_y_pixel': -8538255029366244506,
                                        'source_pixel_width': -5484850923670861736,
                                        'source_pixel_height': -8181298785279623885,
                                        'rotation': -5417080952594929774,
                                        'virtual_nw_x_pixel': 1225822096,
                                        'virtual_nw_y_pixel': -412567443,
                                        'virtual_width': -498932984,
                                        'virtual_height': 1365234695,
                                    },
                            {
                                        'source_monitor': 7129537,
                                        'source_nw_x_pixel': -8847634196630312293,
                                        'source_nw_y_pixel': -8258245512743208885,
                                        'source_pixel_width': -5523154274001416614,
                                        'source_pixel_height': -331559609832972785,
                                        'rotation': -8706239134798824202,
                                        'virtual_nw_x_pixel': 1743878106,
                                        'virtual_nw_y_pixel': 142782166,
                                        'virtual_width': 261604536,
                                        'virtual_height': 1024075390,
                                    },
                            {
                                        'source_monitor': 4566925,
                                        'source_nw_x_pixel': -6588534169000455474,
                                        'source_nw_y_pixel': -7488534243330516288,
                                        'source_pixel_width': -533361402991376187,
                                        'source_pixel_height': -5875727199837365422,
                                        'rotation': -3582811017083302008,
                                        'virtual_nw_x_pixel': 1179831543,
                                        'virtual_nw_y_pixel': 945878423,
                                        'virtual_width': -539418010,
                                        'virtual_height': -1595224073,
                                    },
                            {
                                        'source_monitor': 690903,
                                        'source_nw_x_pixel': -2986493310171738977,
                                        'source_nw_y_pixel': -6866540812486552029,
                                        'source_pixel_width': -8861219891820108986,
                                        'source_pixel_height': -1975706011991464107,
                                        'rotation': -1668065585859015520,
                                        'virtual_nw_x_pixel': -839458943,
                                        'virtual_nw_y_pixel': -1033921918,
                                        'virtual_width': 49291542,
                                        'virtual_height': 215553990,
                                    },
                            {
                                        'source_monitor': 7974477,
                                        'source_nw_x_pixel': -9060988300999113532,
                                        'source_nw_y_pixel': -1303703767052766561,
                                        'source_pixel_width': -1243771401352090874,
                                        'source_pixel_height': -2595192917252087887,
                                        'rotation': -6838339574298543272,
                                        'virtual_nw_x_pixel': 995212897,
                                        'virtual_nw_y_pixel': 445064246,
                                        'virtual_width': -647709722,
                                        'virtual_height': 1669866360,
                                    },
                            {
                                        'source_monitor': 5260423,
                                        'source_nw_x_pixel': -3871666348890907165,
                                        'source_nw_y_pixel': -5627498162427053944,
                                        'source_pixel_width': -3941635087283904886,
                                        'source_pixel_height': -2241474828316917653,
                                        'rotation': -6963381674156874067,
                                        'virtual_nw_x_pixel': 238150910,
                                        'virtual_nw_y_pixel': 880487713,
                                        'virtual_width': 1603821691,
                                        'virtual_height': -94644908,
                                    },
                            {
                                        'source_monitor': 6438287,
                                        'source_nw_x_pixel': -1816100131192441376,
                                        'source_nw_y_pixel': -1311815691846122459,
                                        'source_pixel_width': -9179494063359740861,
                                        'source_pixel_height': -5602490732567588628,
                                        'rotation': -4914731327686516043,
                                        'virtual_nw_x_pixel': -1584840119,
                                        'virtual_nw_y_pixel': -1178322692,
                                        'virtual_width': -1118651850,
                                        'virtual_height': -347157507,
                                    },
                        ],
                },
                {
                    'description': 'ɤιԐʓ',
                    'monitors': [
                            {
                                        'identifier': 2823411,
                                        'width': -4588416310891649386,
                                        'height': -7147447720810836302,
                                    },
                            {
                                        'identifier': 7389318,
                                        'width': -8198632398044895831,
                                        'height': 1699866213620880479,
                                    },
                            {
                                        'identifier': 3583443,
                                        'width': -5894731755191671659,
                                        'height': -7004362931122497655,
                                    },
                            {
                                        'identifier': 2334212,
                                        'width': 3827701024847743050,
                                        'height': 2277515259040871787,
                                    },
                            {
                                        'identifier': 5591261,
                                        'width': -5917935969296740526,
                                        'height': -6368220360976471224,
                                    },
                            {
                                        'identifier': 6712442,
                                        'width': 5878447029249391013,
                                        'height': 110024285884209404,
                                    },
                            {
                                        'identifier': 5900414,
                                        'width': -7698371087363155751,
                                        'height': 3110422595154035758,
                                    },
                            {
                                        'identifier': 2593462,
                                        'width': 886669173824017777,
                                        'height': 7630808119105727041,
                                    },
                            {
                                        'identifier': 9653622,
                                        'width': -3072275299018615353,
                                        'height': 3057026743023277962,
                                    },
                            {
                                        'identifier': 2167271,
                                        'width': 5773735245635398812,
                                        'height': 8310297214359625314,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4488609,
                                        'source_nw_x_pixel': -8265185611227158027,
                                        'source_nw_y_pixel': -2138584407535980693,
                                        'source_pixel_width': -2439888326537885505,
                                        'source_pixel_height': -5478634589704826209,
                                        'rotation': -853169530888129572,
                                        'virtual_nw_x_pixel': -854155171,
                                        'virtual_nw_y_pixel': -605790638,
                                        'virtual_width': -1780890463,
                                        'virtual_height': -1870981899,
                                    },
                            {
                                        'source_monitor': -953733,
                                        'source_nw_x_pixel': -4119861568949566000,
                                        'source_nw_y_pixel': -5561557610029668396,
                                        'source_pixel_width': -8462138800100983786,
                                        'source_pixel_height': -8163342827150496220,
                                        'rotation': -8897658080735195859,
                                        'virtual_nw_x_pixel': 298614342,
                                        'virtual_nw_y_pixel': 1327567878,
                                        'virtual_width': -1476242956,
                                        'virtual_height': -1453910340,
                                    },
                            {
                                        'source_monitor': 3941711,
                                        'source_nw_x_pixel': -5366658545175754551,
                                        'source_nw_y_pixel': -9135758841085387936,
                                        'source_pixel_width': -7316228754187432747,
                                        'source_pixel_height': -2856478836327605402,
                                        'rotation': -6881353451166648059,
                                        'virtual_nw_x_pixel': -451843203,
                                        'virtual_nw_y_pixel': -635371613,
                                        'virtual_width': 260352027,
                                        'virtual_height': -1615959286,
                                    },
                            {
                                        'source_monitor': 4285743,
                                        'source_nw_x_pixel': -8008272488689940684,
                                        'source_nw_y_pixel': -5662474325673921817,
                                        'source_pixel_width': -5397195633274931245,
                                        'source_pixel_height': -3464059224499662804,
                                        'rotation': -6262725542341210779,
                                        'virtual_nw_x_pixel': -869031328,
                                        'virtual_nw_y_pixel': 114667249,
                                        'virtual_width': -504645911,
                                        'virtual_height': -1008576069,
                                    },
                            {
                                        'source_monitor': 6225089,
                                        'source_nw_x_pixel': -8723146638120615255,
                                        'source_nw_y_pixel': -2980481362765382187,
                                        'source_pixel_width': -2018021665721135350,
                                        'source_pixel_height': -1572317567788917927,
                                        'rotation': -1445698943484197745,
                                        'virtual_nw_x_pixel': -763141457,
                                        'virtual_nw_y_pixel': -880906633,
                                        'virtual_width': 1606055020,
                                        'virtual_height': -190225188,
                                    },
                            {
                                        'source_monitor': 1900610,
                                        'source_nw_x_pixel': -5833945168710115002,
                                        'source_nw_y_pixel': -5816295039210361464,
                                        'source_pixel_width': -2424236656232639696,
                                        'source_pixel_height': -4762200635393082596,
                                        'rotation': -5159276969331134164,
                                        'virtual_nw_x_pixel': 402170302,
                                        'virtual_nw_y_pixel': 1164451923,
                                        'virtual_width': -316243575,
                                        'virtual_height': -1012316513,
                                    },
                            {
                                        'source_monitor': 605627,
                                        'source_nw_x_pixel': -7220500398229042280,
                                        'source_nw_y_pixel': -8221284700575807531,
                                        'source_pixel_width': -2631096517878936219,
                                        'source_pixel_height': -9106027105807264683,
                                        'rotation': -2135871559518357379,
                                        'virtual_nw_x_pixel': 1827458406,
                                        'virtual_nw_y_pixel': 768336449,
                                        'virtual_width': -173455531,
                                        'virtual_height': 889671069,
                                    },
                            {
                                        'source_monitor': 6536156,
                                        'source_nw_x_pixel': -7480968888366517672,
                                        'source_nw_y_pixel': -4423379009753957360,
                                        'source_pixel_width': -1386736522330836440,
                                        'source_pixel_height': -123583784183094092,
                                        'rotation': -6336577189092790314,
                                        'virtual_nw_x_pixel': -131865435,
                                        'virtual_nw_y_pixel': 572516574,
                                        'virtual_width': -729938867,
                                        'virtual_height': 1520670180,
                                    },
                            {
                                        'source_monitor': 9180692,
                                        'source_nw_x_pixel': -4410644900639315013,
                                        'source_nw_y_pixel': -7683186811495688743,
                                        'source_pixel_width': -4917675690628848978,
                                        'source_pixel_height': -472586047050590532,
                                        'rotation': -4275120755245282666,
                                        'virtual_nw_x_pixel': -319852246,
                                        'virtual_nw_y_pixel': 974056023,
                                        'virtual_width': -221444554,
                                        'virtual_height': -1629975163,
                                    },
                            {
                                        'source_monitor': 3929276,
                                        'source_nw_x_pixel': -4187386086294202882,
                                        'source_nw_y_pixel': -2830166273691672017,
                                        'source_pixel_width': -3192411629687219869,
                                        'source_pixel_height': -175512866867575368,
                                        'rotation': -7506935536803352271,
                                        'virtual_nw_x_pixel': 751164676,
                                        'virtual_nw_y_pixel': 890028282,
                                        'virtual_width': 1722871409,
                                        'virtual_height': 30245541,
                                    },
                        ],
                },
                {
                    'description': 'ˤRϘϪƄͼĵ҉҆ĖȖȼɜҔ$ǍΦҌZ˂јǾʄҟЫΤԘŇȶĜ',
                    'monitors': [
                            {
                                        'identifier': 1580281,
                                        'width': 3302642993146311462,
                                        'height': 4921524727770920137,
                                    },
                            {
                                        'identifier': 1127172,
                                        'width': 8839375057763775376,
                                        'height': 989571702744942336,
                                    },
                            {
                                        'identifier': 6655481,
                                        'width': -7411869761698427684,
                                        'height': 1666399415566478118,
                                    },
                            {
                                        'identifier': 6301514,
                                        'width': 5676197653663399657,
                                        'height': -1595098982024079008,
                                    },
                            {
                                        'identifier': 8510991,
                                        'width': -6430997521021085544,
                                        'height': 3106953459719319929,
                                    },
                            {
                                        'identifier': 260576,
                                        'width': -6600937129314149609,
                                        'height': -5811536599649211589,
                                    },
                            {
                                        'identifier': 787646,
                                        'width': -7439882070121649830,
                                        'height': -3654214851735660965,
                                    },
                            {
                                        'identifier': 346163,
                                        'width': 1042766962455639556,
                                        'height': 1228697289973396188,
                                    },
                            {
                                        'identifier': 2665277,
                                        'width': 1121184938281460335,
                                        'height': 1657770334916269249,
                                    },
                            {
                                        'identifier': 4834176,
                                        'width': 5024899515615397655,
                                        'height': 7054297630381737707,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -79376,
                                        'source_nw_x_pixel': -4601851416016285596,
                                        'source_nw_y_pixel': -4446438052894469647,
                                        'source_pixel_width': -6633931863563769342,
                                        'source_pixel_height': -824372785583666800,
                                        'rotation': -3417141394918402755,
                                        'virtual_nw_x_pixel': -1036306062,
                                        'virtual_nw_y_pixel': 1874670360,
                                        'virtual_width': -246950321,
                                        'virtual_height': -1349392192,
                                    },
                            {
                                        'source_monitor': 8954122,
                                        'source_nw_x_pixel': -1412287117906243537,
                                        'source_nw_y_pixel': -8031450250412493298,
                                        'source_pixel_width': -8380576677311389849,
                                        'source_pixel_height': -5721243530666449240,
                                        'rotation': -5543371856804426048,
                                        'virtual_nw_x_pixel': -333877805,
                                        'virtual_nw_y_pixel': 1714537708,
                                        'virtual_width': 807868249,
                                        'virtual_height': 719819358,
                                    },
                            {
                                        'source_monitor': -708928,
                                        'source_nw_x_pixel': -1052361529542351205,
                                        'source_nw_y_pixel': -3390503569128721485,
                                        'source_pixel_width': -647775954525326097,
                                        'source_pixel_height': -4749018726364710391,
                                        'rotation': -8231375065679766258,
                                        'virtual_nw_x_pixel': 1810414704,
                                        'virtual_nw_y_pixel': -37016638,
                                        'virtual_width': -77430190,
                                        'virtual_height': -209801612,
                                    },
                            {
                                        'source_monitor': -422234,
                                        'source_nw_x_pixel': -3458594760561949179,
                                        'source_nw_y_pixel': -8143948140797754500,
                                        'source_pixel_width': -6609708541784858495,
                                        'source_pixel_height': -1403096353652689926,
                                        'rotation': -8725190868606454332,
                                        'virtual_nw_x_pixel': -36683825,
                                        'virtual_nw_y_pixel': -1269870208,
                                        'virtual_width': 1483781020,
                                        'virtual_height': -1122901254,
                                    },
                            {
                                        'source_monitor': 4434862,
                                        'source_nw_x_pixel': -2481887551839795018,
                                        'source_nw_y_pixel': -5661229874355790114,
                                        'source_pixel_width': -2384236467098344796,
                                        'source_pixel_height': -5563849742207074833,
                                        'rotation': -7857052563876211278,
                                        'virtual_nw_x_pixel': -1227547030,
                                        'virtual_nw_y_pixel': -1410420624,
                                        'virtual_width': -1365312610,
                                        'virtual_height': -1950131311,
                                    },
                            {
                                        'source_monitor': 4880388,
                                        'source_nw_x_pixel': -1846705601853752698,
                                        'source_nw_y_pixel': -594528541542562719,
                                        'source_pixel_width': -2184186584954466403,
                                        'source_pixel_height': -3484478506403357926,
                                        'rotation': -3771393732608821743,
                                        'virtual_nw_x_pixel': -1029705470,
                                        'virtual_nw_y_pixel': 885340042,
                                        'virtual_width': -390158437,
                                        'virtual_height': 322982319,
                                    },
                            {
                                        'source_monitor': 2887356,
                                        'source_nw_x_pixel': -8984236748493411908,
                                        'source_nw_y_pixel': -6698390672878082778,
                                        'source_pixel_width': -5988352310446719799,
                                        'source_pixel_height': -3490148572846084631,
                                        'rotation': -4800094301843632180,
                                        'virtual_nw_x_pixel': -764483016,
                                        'virtual_nw_y_pixel': 475421395,
                                        'virtual_width': 386817595,
                                        'virtual_height': 1384849132,
                                    },
                            {
                                        'source_monitor': 7592869,
                                        'source_nw_x_pixel': -6241723441484354731,
                                        'source_nw_y_pixel': -3690824761359896309,
                                        'source_pixel_width': -6565025000225082813,
                                        'source_pixel_height': -4488792071219159282,
                                        'rotation': -8168078654418603136,
                                        'virtual_nw_x_pixel': 1725911027,
                                        'virtual_nw_y_pixel': 1841190171,
                                        'virtual_width': 1530515170,
                                        'virtual_height': 1905773781,
                                    },
                            {
                                        'source_monitor': 3072784,
                                        'source_nw_x_pixel': -6836425960882945608,
                                        'source_nw_y_pixel': -2341640352425270991,
                                        'source_pixel_width': -1679940937125842579,
                                        'source_pixel_height': -8777207196737842622,
                                        'rotation': -4093086896477082618,
                                        'virtual_nw_x_pixel': -268941425,
                                        'virtual_nw_y_pixel': -1776493147,
                                        'virtual_width': -283704524,
                                        'virtual_height': 1439261554,
                                    },
                            {
                                        'source_monitor': -350341,
                                        'source_nw_x_pixel': -3438287381270631310,
                                        'source_nw_y_pixel': -3934207357045013597,
                                        'source_pixel_width': -1890473202064371173,
                                        'source_pixel_height': -1972639132154993972,
                                        'rotation': -6863029043833516069,
                                        'virtual_nw_x_pixel': 1741326899,
                                        'virtual_nw_y_pixel': 1578991935,
                                        'virtual_width': 780402381,
                                        'virtual_height': 486244945,
                                    },
                        ],
                },
                {
                    'description': 'êʣўɩ\x9dCͽʱξȤϏ8˰˅ȌùϭȃӄԄʄӱŧ˧ǵʹ˟ȰȇЅ',
                    'monitors': [
                            {
                                        'identifier': 9728322,
                                        'width': 7091948492756882794,
                                        'height': 2923168347263718855,
                                    },
                            {
                                        'identifier': 6142442,
                                        'width': 6191899443804753447,
                                        'height': -8690229142017862687,
                                    },
                            {
                                        'identifier': 4076610,
                                        'width': 7172834483759435554,
                                        'height': 5100947630239064216,
                                    },
                            {
                                        'identifier': 3213554,
                                        'width': 6705506288032027767,
                                        'height': -1732256820740301010,
                                    },
                            {
                                        'identifier': 621271,
                                        'width': 7397052618673425697,
                                        'height': 4383653503519612095,
                                    },
                            {
                                        'identifier': 774641,
                                        'width': 6044216344223119772,
                                        'height': 5438933896855207161,
                                    },
                            {
                                        'identifier': 2045894,
                                        'width': -3976176142054935165,
                                        'height': 7237928062275141525,
                                    },
                            {
                                        'identifier': 9374658,
                                        'width': 82760123044048021,
                                        'height': 8855917286085090760,
                                    },
                            {
                                        'identifier': 5024951,
                                        'width': -8144833505389996299,
                                        'height': 6948312205669406184,
                                    },
                            {
                                        'identifier': 4348346,
                                        'width': -3259491293602625477,
                                        'height': -8939993512798196449,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1862551,
                                        'source_nw_x_pixel': -4585941568727143119,
                                        'source_nw_y_pixel': -2652117051902301088,
                                        'source_pixel_width': -7619374164311490745,
                                        'source_pixel_height': -3649718252182892656,
                                        'rotation': -8737721979092764148,
                                        'virtual_nw_x_pixel': -1872817060,
                                        'virtual_nw_y_pixel': -1001914821,
                                        'virtual_width': 373054333,
                                        'virtual_height': 1154891387,
                                    },
                            {
                                        'source_monitor': 3014376,
                                        'source_nw_x_pixel': -9075919714088084689,
                                        'source_nw_y_pixel': -4769730747998654740,
                                        'source_pixel_width': -7190678816868772993,
                                        'source_pixel_height': -5929959354487453798,
                                        'rotation': -7127086796879479715,
                                        'virtual_nw_x_pixel': -1247977110,
                                        'virtual_nw_y_pixel': -294328565,
                                        'virtual_width': -1038370947,
                                        'virtual_height': 1418055235,
                                    },
                            {
                                        'source_monitor': 6859661,
                                        'source_nw_x_pixel': -7612448551351120808,
                                        'source_nw_y_pixel': -8396538899543203239,
                                        'source_pixel_width': -8189518433475466441,
                                        'source_pixel_height': -1901978550986433190,
                                        'rotation': -712774111975417956,
                                        'virtual_nw_x_pixel': 1259050977,
                                        'virtual_nw_y_pixel': -486000765,
                                        'virtual_width': -499127036,
                                        'virtual_height': -1749945514,
                                    },
                            {
                                        'source_monitor': 9297452,
                                        'source_nw_x_pixel': -4150515598387089326,
                                        'source_nw_y_pixel': -2338798876872537068,
                                        'source_pixel_width': -392484187076238645,
                                        'source_pixel_height': -890779338945125375,
                                        'rotation': -8853984611120462931,
                                        'virtual_nw_x_pixel': -1841251799,
                                        'virtual_nw_y_pixel': -44531279,
                                        'virtual_width': -132342299,
                                        'virtual_height': -1927848491,
                                    },
                            {
                                        'source_monitor': 7830039,
                                        'source_nw_x_pixel': -5766442197040157417,
                                        'source_nw_y_pixel': -1535487935696553402,
                                        'source_pixel_width': -8371679810554027174,
                                        'source_pixel_height': -4376021523671495117,
                                        'rotation': -4504960095001137894,
                                        'virtual_nw_x_pixel': 1012876843,
                                        'virtual_nw_y_pixel': 603888473,
                                        'virtual_width': -1619307388,
                                        'virtual_height': 981206447,
                                    },
                            {
                                        'source_monitor': 2436359,
                                        'source_nw_x_pixel': -6040592117529995838,
                                        'source_nw_y_pixel': -5584095215045642627,
                                        'source_pixel_width': -718018565442548656,
                                        'source_pixel_height': -6826121209600264993,
                                        'rotation': -1036570148762283600,
                                        'virtual_nw_x_pixel': -1780321952,
                                        'virtual_nw_y_pixel': -723661295,
                                        'virtual_width': 755893451,
                                        'virtual_height': 570393646,
                                    },
                            {
                                        'source_monitor': 3730154,
                                        'source_nw_x_pixel': -6662045112278810027,
                                        'source_nw_y_pixel': -4147535791403717548,
                                        'source_pixel_width': -1447497542150356595,
                                        'source_pixel_height': -3401511666514347547,
                                        'rotation': -3336624038502447541,
                                        'virtual_nw_x_pixel': 511294846,
                                        'virtual_nw_y_pixel': -675545863,
                                        'virtual_width': 890331727,
                                        'virtual_height': -1115386497,
                                    },
                            {
                                        'source_monitor': 5348324,
                                        'source_nw_x_pixel': -200850392035111491,
                                        'source_nw_y_pixel': -952361873999444387,
                                        'source_pixel_width': -1685306255946264463,
                                        'source_pixel_height': -8789634218258749708,
                                        'rotation': -2456751387327095986,
                                        'virtual_nw_x_pixel': 278680202,
                                        'virtual_nw_y_pixel': -1692733420,
                                        'virtual_width': -1243148777,
                                        'virtual_height': -1775132852,
                                    },
                            {
                                        'source_monitor': 1789019,
                                        'source_nw_x_pixel': -8636619083384238499,
                                        'source_nw_y_pixel': -2780981980765866231,
                                        'source_pixel_width': -3287127560189513299,
                                        'source_pixel_height': -8610948253372899953,
                                        'rotation': -1146869835125247505,
                                        'virtual_nw_x_pixel': -1407830144,
                                        'virtual_nw_y_pixel': -1279151587,
                                        'virtual_width': 388573612,
                                        'virtual_height': 248180505,
                                    },
                            {
                                        'source_monitor': 1362293,
                                        'source_nw_x_pixel': -1178783569612518260,
                                        'source_nw_y_pixel': -118602946402354364,
                                        'source_pixel_width': -1609733337160359122,
                                        'source_pixel_height': -3990020364119765031,
                                        'rotation': -262211087250618656,
                                        'virtual_nw_x_pixel': -1675686907,
                                        'virtual_nw_y_pixel': -1481108634,
                                        'virtual_width': 428589640,
                                        'virtual_height': 1290911415,
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
                                        'identifier': 1394215,
                                        'width': -6088266955522053364,
                                        'height': -7950072927936306938,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -841672374206849429,
                                        'source_nw_y_pixel': -6188397184348191664,
                                        'source_pixel_width': -6571687302335996556,
                                        'source_pixel_height': -8748180310761585926,
                                        'rotation': -8056765506786332027,
                                        'virtual_nw_x_pixel': 955992540,
                                        'virtual_nw_y_pixel': 328520845,
                                        'virtual_width': 920441171,
                                        'virtual_height': 1316670938,
                                    },
                        ],
                },
            ],

        },
    ),
]
