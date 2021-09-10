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
            'identifier': 6776573,
            'width': -7945305297016012759,
            'height': 3750019750450233488,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 422556,

            'width': -2393165221823884047,

            'height': -1362641333356277940,

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
            'source_monitor': 1463906,
            'source_nw_x_pixel': -8618620270732445009,
            'source_nw_y_pixel': -3270597275290274428,
            'source_pixel_width': -7989081832686534926,
            'source_pixel_height': -7265874468905826807,
            'rotation': -3065657409639462226,
            'virtual_nw_x_pixel': 385683190,
            'virtual_nw_y_pixel': -1809644727,
            'virtual_width': 1639031962,
            'virtual_height': -1037934347,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -6781808758014161884,

            'source_nw_y_pixel': -7482984816279857916,

            'source_pixel_width': -9140493359479458542,

            'source_pixel_height': -7645700755377098916,

            'rotation': -5778582324595026689,

            'virtual_nw_x_pixel': 113629267,

            'virtual_nw_y_pixel': -504076132,

            'virtual_width': -791899493,

            'virtual_height': 1324026582,

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
            'description': 'Л»Ӑûʄ҉/ƛɢȼʢȏſΣѥ˹Eʁ\u03a2ŭà)ǿńŵѿѬǇѧ\x80',
            'monitors': [
                {
                    'identifier': 7698109,
                    'width': -7360468969030191941,
                    'height': 6570792851837998732,
                },
                {
                    'identifier': 6312790,
                    'width': 2886727639350571843,
                    'height': -7815443092745842553,
                },
                {
                    'identifier': -73568,
                    'width': 3165986817626556836,
                    'height': 3087877922295307053,
                },
                {
                    'identifier': 442415,
                    'width': -1070012322770465922,
                    'height': -1873347667713679584,
                },
                {
                    'identifier': 3456747,
                    'width': -7881655997256245276,
                    'height': 2105847992866131515,
                },
                {
                    'identifier': 1920919,
                    'width': 4206320139030940782,
                    'height': 1438319141646239854,
                },
                {
                    'identifier': 9521546,
                    'width': 1523580578453045083,
                    'height': 4060278266608057906,
                },
                {
                    'identifier': 8884056,
                    'width': -8066364517277194314,
                    'height': -7295686175593929273,
                },
                {
                    'identifier': 6592155,
                    'width': -8420523895601753226,
                    'height': -267281734884435661,
                },
                {
                    'identifier': 2707875,
                    'width': -8751799723598725466,
                    'height': 7053334053363074701,
                },
            ],
            'screen': [
                {
                    'source_monitor': 3468850,
                    'source_nw_x_pixel': -2911503015378681291,
                    'source_nw_y_pixel': -7191924603221897309,
                    'source_pixel_width': -8878508350969707168,
                    'source_pixel_height': -8837964757181614209,
                    'rotation': -863641424750463062,
                    'virtual_nw_x_pixel': 605840586,
                    'virtual_nw_y_pixel': -555425304,
                    'virtual_width': -586737694,
                    'virtual_height': -314359090,
                },
                {
                    'source_monitor': 638721,
                    'source_nw_x_pixel': -9124854391117139439,
                    'source_nw_y_pixel': -5220183043622475745,
                    'source_pixel_width': -6361496779483684567,
                    'source_pixel_height': -3633849065512949885,
                    'rotation': -7332734973802428740,
                    'virtual_nw_x_pixel': 44136558,
                    'virtual_nw_y_pixel': -1302482858,
                    'virtual_width': -855041329,
                    'virtual_height': 520181553,
                },
                {
                    'source_monitor': 1983232,
                    'source_nw_x_pixel': -6846025947983675340,
                    'source_nw_y_pixel': -5482061326288734358,
                    'source_pixel_width': -6452107357239001517,
                    'source_pixel_height': -9107964786899885548,
                    'rotation': -6098094937934500264,
                    'virtual_nw_x_pixel': -460201001,
                    'virtual_nw_y_pixel': 692783044,
                    'virtual_width': -901180663,
                    'virtual_height': 1304560360,
                },
                {
                    'source_monitor': 5740235,
                    'source_nw_x_pixel': -3840008793625403471,
                    'source_nw_y_pixel': -785924037867312902,
                    'source_pixel_width': -139966708049495820,
                    'source_pixel_height': -3280627757405566353,
                    'rotation': -4040480008710120166,
                    'virtual_nw_x_pixel': 211439524,
                    'virtual_nw_y_pixel': 444557480,
                    'virtual_width': 112349483,
                    'virtual_height': 609657595,
                },
                {
                    'source_monitor': 8961758,
                    'source_nw_x_pixel': -8382191200793821133,
                    'source_nw_y_pixel': -6118387454875090433,
                    'source_pixel_width': -3308300559922476682,
                    'source_pixel_height': -1764696448621716788,
                    'rotation': -5601601647241248835,
                    'virtual_nw_x_pixel': 688562816,
                    'virtual_nw_y_pixel': -80536170,
                    'virtual_width': -1212125589,
                    'virtual_height': 1647886981,
                },
                {
                    'source_monitor': -673504,
                    'source_nw_x_pixel': -3162513099858243693,
                    'source_nw_y_pixel': -1199262463019300909,
                    'source_pixel_width': -3003961227983028607,
                    'source_pixel_height': -1520871569288581265,
                    'rotation': -4010143329972349262,
                    'virtual_nw_x_pixel': 722140826,
                    'virtual_nw_y_pixel': -1435571500,
                    'virtual_width': 1982456597,
                    'virtual_height': -1791174243,
                },
                {
                    'source_monitor': 1841265,
                    'source_nw_x_pixel': -405040302795162351,
                    'source_nw_y_pixel': -5748593083902565945,
                    'source_pixel_width': -1586306033896365837,
                    'source_pixel_height': -5249358779292543776,
                    'rotation': -8915172748212442002,
                    'virtual_nw_x_pixel': -1239342731,
                    'virtual_nw_y_pixel': 1308884422,
                    'virtual_width': 1208638939,
                    'virtual_height': 667334613,
                },
                {
                    'source_monitor': 9025064,
                    'source_nw_x_pixel': -7981571694133662543,
                    'source_nw_y_pixel': -8104865653613775320,
                    'source_pixel_width': -56307339842723100,
                    'source_pixel_height': -1600930342916307776,
                    'rotation': -1679339010003678236,
                    'virtual_nw_x_pixel': 1241487601,
                    'virtual_nw_y_pixel': 855734412,
                    'virtual_width': 391397949,
                    'virtual_height': 642966350,
                },
                {
                    'source_monitor': 1788421,
                    'source_nw_x_pixel': -4040193283063243497,
                    'source_nw_y_pixel': -3835937993980942615,
                    'source_pixel_width': -2837094663675631195,
                    'source_pixel_height': -421078092287614688,
                    'rotation': -4719418950497044858,
                    'virtual_nw_x_pixel': 1224148131,
                    'virtual_nw_y_pixel': 1429803238,
                    'virtual_width': 1248199501,
                    'virtual_height': 1611063188,
                },
                {
                    'source_monitor': 3556741,
                    'source_nw_x_pixel': -1397638409089216670,
                    'source_nw_y_pixel': -7743626421814015647,
                    'source_pixel_width': -3342325798259184461,
                    'source_pixel_height': -8382666764930294696,
                    'rotation': -7904218191715850432,
                    'virtual_nw_x_pixel': 1411386754,
                    'virtual_nw_y_pixel': 1613534416,
                    'virtual_width': -1669037285,
                    'virtual_height': 1167597205,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 6800338,
                    'width': -2840811687990162228,
                    'height': -5549430275282532079,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -7218343959252504293,
                    'source_nw_y_pixel': -2425699576279966098,
                    'source_pixel_width': -7620575363941855439,
                    'source_pixel_height': -8451482920840120256,
                    'rotation': -6566447160894569246,
                    'virtual_nw_x_pixel': 350980880,
                    'virtual_nw_y_pixel': 1378608325,
                    'virtual_width': 1241663907,
                    'virtual_height': 546808984,
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
            'request_id': 8227099,
            'mapped_screens_by_monitors': [
                {
                    'description': 'ȌƳȉѬηèіıϟʱԀӘΖӛŠӟӔԈѭȍ',
                    'monitors': [
                            {
                                        'identifier': 2588949,
                                        'width': 6168245977896382317,
                                        'height': 8826987786209346967,
                                    },
                            {
                                        'identifier': 7097460,
                                        'width': 6530666193949011783,
                                        'height': 2745548962346400630,
                                    },
                            {
                                        'identifier': 1014248,
                                        'width': 5648621899618890718,
                                        'height': 6566256864562328389,
                                    },
                            {
                                        'identifier': 7478834,
                                        'width': -4687436509822077495,
                                        'height': -1157514549312626237,
                                    },
                            {
                                        'identifier': 9203777,
                                        'width': 7782047878747749089,
                                        'height': -557354936574975010,
                                    },
                            {
                                        'identifier': 5080887,
                                        'width': -4216493693211623219,
                                        'height': 3970290792909825228,
                                    },
                            {
                                        'identifier': 7522519,
                                        'width': 3721318582999695779,
                                        'height': 1594953266501838310,
                                    },
                            {
                                        'identifier': 1765551,
                                        'width': 3319450492157258591,
                                        'height': 8057320034682440357,
                                    },
                            {
                                        'identifier': 4823944,
                                        'width': 9176733174515258478,
                                        'height': 897027062374805130,
                                    },
                            {
                                        'identifier': 3506007,
                                        'width': 2388374720841194096,
                                        'height': -1592901702358236282,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8865481,
                                        'source_nw_x_pixel': -9060765977624036886,
                                        'source_nw_y_pixel': -443894077234495455,
                                        'source_pixel_width': -3761322000893105144,
                                        'source_pixel_height': -7738157630255397606,
                                        'rotation': -6304965417961713438,
                                        'virtual_nw_x_pixel': -1132636387,
                                        'virtual_nw_y_pixel': -1044747176,
                                        'virtual_width': -205436953,
                                        'virtual_height': -662063636,
                                    },
                            {
                                        'source_monitor': 3888424,
                                        'source_nw_x_pixel': -8684027721548673472,
                                        'source_nw_y_pixel': -7320798370835590731,
                                        'source_pixel_width': -4148134809052955185,
                                        'source_pixel_height': -5994422951868356129,
                                        'rotation': -8607836168882595907,
                                        'virtual_nw_x_pixel': -1477547721,
                                        'virtual_nw_y_pixel': 955041957,
                                        'virtual_width': -398970491,
                                        'virtual_height': 1684047246,
                                    },
                            {
                                        'source_monitor': 3956738,
                                        'source_nw_x_pixel': -5266840868970205906,
                                        'source_nw_y_pixel': -8329991453534959939,
                                        'source_pixel_width': -398331458734565591,
                                        'source_pixel_height': -2018731260020451309,
                                        'rotation': -757094579597800526,
                                        'virtual_nw_x_pixel': -1178757808,
                                        'virtual_nw_y_pixel': 111580620,
                                        'virtual_width': -369146131,
                                        'virtual_height': -1042131212,
                                    },
                            {
                                        'source_monitor': 2189002,
                                        'source_nw_x_pixel': -7020611989828915817,
                                        'source_nw_y_pixel': -2245460996523068291,
                                        'source_pixel_width': -3727080667800241970,
                                        'source_pixel_height': -5176982852113493711,
                                        'rotation': -8142325283664281707,
                                        'virtual_nw_x_pixel': -1479128215,
                                        'virtual_nw_y_pixel': 1681598115,
                                        'virtual_width': 1688450139,
                                        'virtual_height': -1222663414,
                                    },
                            {
                                        'source_monitor': 2944373,
                                        'source_nw_x_pixel': -3761833089230055611,
                                        'source_nw_y_pixel': -2588037206867239896,
                                        'source_pixel_width': -6677089430783253641,
                                        'source_pixel_height': -4751266846521468739,
                                        'rotation': -1463738201021710725,
                                        'virtual_nw_x_pixel': -1537276567,
                                        'virtual_nw_y_pixel': -1678305193,
                                        'virtual_width': 1471922261,
                                        'virtual_height': -1457947509,
                                    },
                            {
                                        'source_monitor': -219973,
                                        'source_nw_x_pixel': -2752854610722382178,
                                        'source_nw_y_pixel': -6305665598079193446,
                                        'source_pixel_width': -3543937330461688915,
                                        'source_pixel_height': -7232657784600534582,
                                        'rotation': -3523989630244245624,
                                        'virtual_nw_x_pixel': 1284952164,
                                        'virtual_nw_y_pixel': 1752906155,
                                        'virtual_width': -715172812,
                                        'virtual_height': 236714872,
                                    },
                            {
                                        'source_monitor': 7828997,
                                        'source_nw_x_pixel': -8252604894440688448,
                                        'source_nw_y_pixel': -5267373929043896111,
                                        'source_pixel_width': -1807265904381749996,
                                        'source_pixel_height': -6372789841509618870,
                                        'rotation': -8398328867884052471,
                                        'virtual_nw_x_pixel': -1444208087,
                                        'virtual_nw_y_pixel': -1934206814,
                                        'virtual_width': -934565674,
                                        'virtual_height': 1578678478,
                                    },
                            {
                                        'source_monitor': 3691972,
                                        'source_nw_x_pixel': -8700520330851633642,
                                        'source_nw_y_pixel': -3736551185179018424,
                                        'source_pixel_width': -546274335753327046,
                                        'source_pixel_height': -7434447630682661691,
                                        'rotation': -1203211916875899405,
                                        'virtual_nw_x_pixel': -662638499,
                                        'virtual_nw_y_pixel': -1529588503,
                                        'virtual_width': -1618565767,
                                        'virtual_height': -1011022952,
                                    },
                            {
                                        'source_monitor': 41653,
                                        'source_nw_x_pixel': -8832696711525730755,
                                        'source_nw_y_pixel': -947206089984787433,
                                        'source_pixel_width': -6662900962092110969,
                                        'source_pixel_height': -9162713720086533311,
                                        'rotation': -7852623231196377447,
                                        'virtual_nw_x_pixel': 1580526452,
                                        'virtual_nw_y_pixel': -975854605,
                                        'virtual_width': -225554023,
                                        'virtual_height': -950402344,
                                    },
                            {
                                        'source_monitor': 9301341,
                                        'source_nw_x_pixel': -7549726648649440961,
                                        'source_nw_y_pixel': -8353339758745122867,
                                        'source_pixel_width': -7528645579940235092,
                                        'source_pixel_height': -7598219298466647037,
                                        'rotation': -2993219101977169034,
                                        'virtual_nw_x_pixel': -845996662,
                                        'virtual_nw_y_pixel': -1561545187,
                                        'virtual_width': -1751594802,
                                        'virtual_height': 1601809272,
                                    },
                        ],
                },
                {
                    'description': 'Μ¬ϘӭǈϮźȰӺ\x82mǭҼʃ\x96ҞƐπǚˢϼǦϳ9ǰƠϊƤźļ',
                    'monitors': [
                            {
                                        'identifier': 300924,
                                        'width': 3943364420798902074,
                                        'height': 2606686007081266785,
                                    },
                            {
                                        'identifier': 6438236,
                                        'width': -4525198349517717419,
                                        'height': 6265504335148840418,
                                    },
                            {
                                        'identifier': 1450828,
                                        'width': 6953769271571871129,
                                        'height': 1172331097286836041,
                                    },
                            {
                                        'identifier': 3440630,
                                        'width': -1450441611807089697,
                                        'height': -8235601289460970131,
                                    },
                            {
                                        'identifier': -994157,
                                        'width': 6545908856492050294,
                                        'height': 3489253187962044609,
                                    },
                            {
                                        'identifier': 2823687,
                                        'width': 4427168635183553578,
                                        'height': -7343461137730420401,
                                    },
                            {
                                        'identifier': 2443103,
                                        'width': -9022193502290005301,
                                        'height': 2985235059568864097,
                                    },
                            {
                                        'identifier': -668338,
                                        'width': -7261434690169266679,
                                        'height': 8425250093909261388,
                                    },
                            {
                                        'identifier': 6878065,
                                        'width': 8226744274319634947,
                                        'height': -1596846822718106149,
                                    },
                            {
                                        'identifier': -131571,
                                        'width': -2776585414446714783,
                                        'height': -8819267784143066798,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2075510,
                                        'source_nw_x_pixel': -1532152904016478096,
                                        'source_nw_y_pixel': -3641286984962323498,
                                        'source_pixel_width': -8062241059233293143,
                                        'source_pixel_height': -5594620288103555579,
                                        'rotation': -3533915992067900199,
                                        'virtual_nw_x_pixel': 598875085,
                                        'virtual_nw_y_pixel': 1690142448,
                                        'virtual_width': 1706775486,
                                        'virtual_height': 238274877,
                                    },
                            {
                                        'source_monitor': 573416,
                                        'source_nw_x_pixel': -5491779605100036856,
                                        'source_nw_y_pixel': -8535929103265240727,
                                        'source_pixel_width': -2819798677718562921,
                                        'source_pixel_height': -6851113928719495278,
                                        'rotation': -1487255844301306168,
                                        'virtual_nw_x_pixel': 387712368,
                                        'virtual_nw_y_pixel': -1410019608,
                                        'virtual_width': 998698278,
                                        'virtual_height': 1366868926,
                                    },
                            {
                                        'source_monitor': 3185852,
                                        'source_nw_x_pixel': -4729991099418478290,
                                        'source_nw_y_pixel': -448944661599003550,
                                        'source_pixel_width': -3167208497292369115,
                                        'source_pixel_height': -6286004617818584623,
                                        'rotation': -154401671888177657,
                                        'virtual_nw_x_pixel': -713350827,
                                        'virtual_nw_y_pixel': 1321190790,
                                        'virtual_width': -50772830,
                                        'virtual_height': -1500425458,
                                    },
                            {
                                        'source_monitor': 3098062,
                                        'source_nw_x_pixel': -5085042344136816734,
                                        'source_nw_y_pixel': -6305742766622797593,
                                        'source_pixel_width': -3407822525291608048,
                                        'source_pixel_height': -8938530212148468758,
                                        'rotation': -2892977951951543984,
                                        'virtual_nw_x_pixel': 77218801,
                                        'virtual_nw_y_pixel': -1426577451,
                                        'virtual_width': -1690969054,
                                        'virtual_height': 1296032706,
                                    },
                            {
                                        'source_monitor': 8787720,
                                        'source_nw_x_pixel': -1147440757545443819,
                                        'source_nw_y_pixel': -4740795838311341695,
                                        'source_pixel_width': -1986450468335389037,
                                        'source_pixel_height': -8242610248593576945,
                                        'rotation': -2834238916381781906,
                                        'virtual_nw_x_pixel': -523577352,
                                        'virtual_nw_y_pixel': -848671062,
                                        'virtual_width': -579473022,
                                        'virtual_height': 1744897457,
                                    },
                            {
                                        'source_monitor': 7056715,
                                        'source_nw_x_pixel': -6022604705319620153,
                                        'source_nw_y_pixel': -556471739928636488,
                                        'source_pixel_width': -1446307539535753149,
                                        'source_pixel_height': -1659881742772453087,
                                        'rotation': -179640919148860134,
                                        'virtual_nw_x_pixel': -842946976,
                                        'virtual_nw_y_pixel': 881578109,
                                        'virtual_width': -415292316,
                                        'virtual_height': 1439383617,
                                    },
                            {
                                        'source_monitor': 659518,
                                        'source_nw_x_pixel': -7314442761739071669,
                                        'source_nw_y_pixel': -4550644119258297405,
                                        'source_pixel_width': -4115375945823030049,
                                        'source_pixel_height': -3075144595875496893,
                                        'rotation': -628307903043586919,
                                        'virtual_nw_x_pixel': 522615730,
                                        'virtual_nw_y_pixel': 607104065,
                                        'virtual_width': 3621562,
                                        'virtual_height': -1343288930,
                                    },
                            {
                                        'source_monitor': 4311345,
                                        'source_nw_x_pixel': -3795929668906621823,
                                        'source_nw_y_pixel': -2347670532201176202,
                                        'source_pixel_width': -2813095387979204709,
                                        'source_pixel_height': -2628627532843542190,
                                        'rotation': -5836618890932329972,
                                        'virtual_nw_x_pixel': -478107062,
                                        'virtual_nw_y_pixel': 1335732040,
                                        'virtual_width': -273601648,
                                        'virtual_height': -909465863,
                                    },
                            {
                                        'source_monitor': -532434,
                                        'source_nw_x_pixel': -8121640105896511487,
                                        'source_nw_y_pixel': -5455865541101466360,
                                        'source_pixel_width': -7702903365459071164,
                                        'source_pixel_height': -4520650546129455261,
                                        'rotation': -8306293655165599452,
                                        'virtual_nw_x_pixel': 238437029,
                                        'virtual_nw_y_pixel': 1702478659,
                                        'virtual_width': 1795759576,
                                        'virtual_height': -1813663352,
                                    },
                            {
                                        'source_monitor': 3389269,
                                        'source_nw_x_pixel': -7214453602321963329,
                                        'source_nw_y_pixel': -2567492443695637798,
                                        'source_pixel_width': -4490638366626555189,
                                        'source_pixel_height': -2072534497059295729,
                                        'rotation': -6310943852154458954,
                                        'virtual_nw_x_pixel': -1275681370,
                                        'virtual_nw_y_pixel': -502553424,
                                        'virtual_width': -1670523553,
                                        'virtual_height': 997515863,
                                    },
                        ],
                },
                {
                    'description': 'ˎжŹѶԩСыǞʊțҩǍPƱȭăÚҶʾʆǅλӾϪԀ˷Пǀϖõ',
                    'monitors': [
                            {
                                        'identifier': 1111639,
                                        'width': -7200755607939042466,
                                        'height': -3597282525137188268,
                                    },
                            {
                                        'identifier': 5506538,
                                        'width': -1881129709837129944,
                                        'height': -7860034890336634224,
                                    },
                            {
                                        'identifier': 4040530,
                                        'width': 4076739094783370670,
                                        'height': -8200848041442122369,
                                    },
                            {
                                        'identifier': 3316400,
                                        'width': -7519324652272080457,
                                        'height': 491114878533407147,
                                    },
                            {
                                        'identifier': -310437,
                                        'width': 6314921042914407008,
                                        'height': 6205882793292546445,
                                    },
                            {
                                        'identifier': 3249879,
                                        'width': 2307920151215483989,
                                        'height': 4499088726910658777,
                                    },
                            {
                                        'identifier': 7269667,
                                        'width': -9160160400146377459,
                                        'height': 8510637001516330610,
                                    },
                            {
                                        'identifier': 5919299,
                                        'width': 3087856495245226665,
                                        'height': -1323871051992185448,
                                    },
                            {
                                        'identifier': 8870477,
                                        'width': -9161550587903662662,
                                        'height': 1669375559450848494,
                                    },
                            {
                                        'identifier': 7990504,
                                        'width': -2138749522515577426,
                                        'height': -7234417165379338232,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -558128,
                                        'source_nw_x_pixel': -3328214824521458572,
                                        'source_nw_y_pixel': -7560810907497628945,
                                        'source_pixel_width': -6436273491089022524,
                                        'source_pixel_height': -501924312460623153,
                                        'rotation': -1461422559320469066,
                                        'virtual_nw_x_pixel': 992953747,
                                        'virtual_nw_y_pixel': -1459489121,
                                        'virtual_width': 1526253956,
                                        'virtual_height': 452618165,
                                    },
                            {
                                        'source_monitor': 9223340,
                                        'source_nw_x_pixel': -4498297996920489906,
                                        'source_nw_y_pixel': -1901506365060440597,
                                        'source_pixel_width': -5866103867592849472,
                                        'source_pixel_height': -6487303958786889000,
                                        'rotation': -6037635441974983904,
                                        'virtual_nw_x_pixel': -718104224,
                                        'virtual_nw_y_pixel': -520229095,
                                        'virtual_width': -959321073,
                                        'virtual_height': 503052577,
                                    },
                            {
                                        'source_monitor': -523111,
                                        'source_nw_x_pixel': -2626651858996596425,
                                        'source_nw_y_pixel': -905082082817766056,
                                        'source_pixel_width': -230734022248231541,
                                        'source_pixel_height': -3037319660894513088,
                                        'rotation': -7610948222033739975,
                                        'virtual_nw_x_pixel': 1066245538,
                                        'virtual_nw_y_pixel': -1566076755,
                                        'virtual_width': -598649569,
                                        'virtual_height': 146123649,
                                    },
                            {
                                        'source_monitor': 1648933,
                                        'source_nw_x_pixel': -6568383121978072568,
                                        'source_nw_y_pixel': -4872375066509866008,
                                        'source_pixel_width': -7864662100657093784,
                                        'source_pixel_height': -2065299665156584841,
                                        'rotation': -8729398958112778047,
                                        'virtual_nw_x_pixel': -524965792,
                                        'virtual_nw_y_pixel': -1491857235,
                                        'virtual_width': 232109198,
                                        'virtual_height': -871572166,
                                    },
                            {
                                        'source_monitor': 75656,
                                        'source_nw_x_pixel': -4994293645794600904,
                                        'source_nw_y_pixel': -8086223880804293893,
                                        'source_pixel_width': -933345127786223116,
                                        'source_pixel_height': -5650371952740517289,
                                        'rotation': -8767849097963102748,
                                        'virtual_nw_x_pixel': 1170428541,
                                        'virtual_nw_y_pixel': -1071668080,
                                        'virtual_width': 213077449,
                                        'virtual_height': 7042127,
                                    },
                            {
                                        'source_monitor': 6574404,
                                        'source_nw_x_pixel': -1396701482249872702,
                                        'source_nw_y_pixel': -8675447319707020659,
                                        'source_pixel_width': -4464008030888281902,
                                        'source_pixel_height': -6627951689838161286,
                                        'rotation': -8416718315054337351,
                                        'virtual_nw_x_pixel': -1394758631,
                                        'virtual_nw_y_pixel': 1182955139,
                                        'virtual_width': -1375657154,
                                        'virtual_height': -762777840,
                                    },
                            {
                                        'source_monitor': 1103301,
                                        'source_nw_x_pixel': -6302878978567256728,
                                        'source_nw_y_pixel': -2332632297027087239,
                                        'source_pixel_width': -6927072024851047841,
                                        'source_pixel_height': -7071922087254542609,
                                        'rotation': -1043857975257235463,
                                        'virtual_nw_x_pixel': 10725285,
                                        'virtual_nw_y_pixel': 1044693079,
                                        'virtual_width': 735677909,
                                        'virtual_height': 1805799414,
                                    },
                            {
                                        'source_monitor': 7345838,
                                        'source_nw_x_pixel': -1097580836108598883,
                                        'source_nw_y_pixel': -3378523778609085867,
                                        'source_pixel_width': -837787166460602603,
                                        'source_pixel_height': -4112708737559622658,
                                        'rotation': -1550869776819082825,
                                        'virtual_nw_x_pixel': 1974517705,
                                        'virtual_nw_y_pixel': 1110278947,
                                        'virtual_width': 113131268,
                                        'virtual_height': 237132988,
                                    },
                            {
                                        'source_monitor': -983642,
                                        'source_nw_x_pixel': -3841379603400207764,
                                        'source_nw_y_pixel': -8255569393464926300,
                                        'source_pixel_width': -616428609410395381,
                                        'source_pixel_height': -8634693316726665682,
                                        'rotation': -813167865336320321,
                                        'virtual_nw_x_pixel': 5573711,
                                        'virtual_nw_y_pixel': -1992994496,
                                        'virtual_width': -149375369,
                                        'virtual_height': -1640394351,
                                    },
                            {
                                        'source_monitor': 8779762,
                                        'source_nw_x_pixel': -914714013505260421,
                                        'source_nw_y_pixel': -8462722468603837311,
                                        'source_pixel_width': -4738468760623825515,
                                        'source_pixel_height': -1102282711782196692,
                                        'rotation': -4051079209188118080,
                                        'virtual_nw_x_pixel': -541362542,
                                        'virtual_nw_y_pixel': 279088675,
                                        'virtual_width': 177068467,
                                        'virtual_height': -826508237,
                                    },
                        ],
                },
                {
                    'description': 'ӦπēΒρȺϕCëɇ9͵˶ӛϥϺӴљТ\x9bôEǶ·ǳɸý·±Ҏ',
                    'monitors': [
                            {
                                        'identifier': 2068917,
                                        'width': 8498408926026736030,
                                        'height': 200049884085765141,
                                    },
                            {
                                        'identifier': 8357843,
                                        'width': -1458426413219380936,
                                        'height': -7215247702840628945,
                                    },
                            {
                                        'identifier': 1512487,
                                        'width': -4447198559064912728,
                                        'height': 6124071912628389705,
                                    },
                            {
                                        'identifier': 9528462,
                                        'width': -2657532296670689914,
                                        'height': 1152204055913190539,
                                    },
                            {
                                        'identifier': 7141021,
                                        'width': -7839662552377080403,
                                        'height': -396434044366378580,
                                    },
                            {
                                        'identifier': 1722023,
                                        'width': 5494060777854153069,
                                        'height': 2578430395005031959,
                                    },
                            {
                                        'identifier': 9358491,
                                        'width': -5522244403015540378,
                                        'height': 4074362706849119784,
                                    },
                            {
                                        'identifier': 3836651,
                                        'width': 885615934275221127,
                                        'height': 2326810344538205747,
                                    },
                            {
                                        'identifier': 3250888,
                                        'width': -8474600645871762095,
                                        'height': -8335800106182475732,
                                    },
                            {
                                        'identifier': 2100957,
                                        'width': 5453968591563721784,
                                        'height': 6426727419173354726,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -411263,
                                        'source_nw_x_pixel': -8940215383294033562,
                                        'source_nw_y_pixel': -4693110588030777574,
                                        'source_pixel_width': -4594152739243926661,
                                        'source_pixel_height': -1333014283130754246,
                                        'rotation': -6393327665039415919,
                                        'virtual_nw_x_pixel': -1010912891,
                                        'virtual_nw_y_pixel': 681325892,
                                        'virtual_width': -272507437,
                                        'virtual_height': 1779205090,
                                    },
                            {
                                        'source_monitor': 5795580,
                                        'source_nw_x_pixel': -3687825135921221100,
                                        'source_nw_y_pixel': -1192765433223963407,
                                        'source_pixel_width': -7675079927239308005,
                                        'source_pixel_height': -8194130455327489796,
                                        'rotation': -7869262345798699461,
                                        'virtual_nw_x_pixel': 285900652,
                                        'virtual_nw_y_pixel': 433291140,
                                        'virtual_width': 931720987,
                                        'virtual_height': 775560165,
                                    },
                            {
                                        'source_monitor': 6945313,
                                        'source_nw_x_pixel': -7635090740276769049,
                                        'source_nw_y_pixel': -1046181519359493900,
                                        'source_pixel_width': -8250003588298154460,
                                        'source_pixel_height': -1399984765993670349,
                                        'rotation': -5650241819736821504,
                                        'virtual_nw_x_pixel': 1900158006,
                                        'virtual_nw_y_pixel': 1900656518,
                                        'virtual_width': 1732300476,
                                        'virtual_height': 997757069,
                                    },
                            {
                                        'source_monitor': 8530730,
                                        'source_nw_x_pixel': -619591171526664492,
                                        'source_nw_y_pixel': -6988279346465209149,
                                        'source_pixel_width': -6406926072195590618,
                                        'source_pixel_height': -2436417944441070096,
                                        'rotation': -6505385228074208073,
                                        'virtual_nw_x_pixel': -1212152300,
                                        'virtual_nw_y_pixel': -9426556,
                                        'virtual_width': -166492438,
                                        'virtual_height': 1909066796,
                                    },
                            {
                                        'source_monitor': 7105503,
                                        'source_nw_x_pixel': -6702694058024577554,
                                        'source_nw_y_pixel': -1678353021896477871,
                                        'source_pixel_width': -6982846756882996021,
                                        'source_pixel_height': -7801864480404363698,
                                        'rotation': -6515507963279619926,
                                        'virtual_nw_x_pixel': 1221872803,
                                        'virtual_nw_y_pixel': -727411447,
                                        'virtual_width': 290880984,
                                        'virtual_height': -1259589201,
                                    },
                            {
                                        'source_monitor': 8465925,
                                        'source_nw_x_pixel': -1189084343275602235,
                                        'source_nw_y_pixel': -8642050906865398979,
                                        'source_pixel_width': -3012991128656831841,
                                        'source_pixel_height': -1046432288395610140,
                                        'rotation': -4362194671993366143,
                                        'virtual_nw_x_pixel': -1936618550,
                                        'virtual_nw_y_pixel': -16664116,
                                        'virtual_width': 1690178856,
                                        'virtual_height': -1592916645,
                                    },
                            {
                                        'source_monitor': 6026063,
                                        'source_nw_x_pixel': -2798046866717767070,
                                        'source_nw_y_pixel': -1436431926022581123,
                                        'source_pixel_width': -157177110532809217,
                                        'source_pixel_height': -3179112572535791658,
                                        'rotation': -7256635794395715004,
                                        'virtual_nw_x_pixel': 1962853189,
                                        'virtual_nw_y_pixel': -95165605,
                                        'virtual_width': 1570180956,
                                        'virtual_height': -1261091158,
                                    },
                            {
                                        'source_monitor': 4651848,
                                        'source_nw_x_pixel': -5304659833755251592,
                                        'source_nw_y_pixel': -3376352211816002548,
                                        'source_pixel_width': -9192822267498663000,
                                        'source_pixel_height': -6803527386916174238,
                                        'rotation': -5695050176135059857,
                                        'virtual_nw_x_pixel': 1207022119,
                                        'virtual_nw_y_pixel': -691101805,
                                        'virtual_width': 987092510,
                                        'virtual_height': 1336573586,
                                    },
                            {
                                        'source_monitor': 9389679,
                                        'source_nw_x_pixel': -3316902317761416503,
                                        'source_nw_y_pixel': -8212032737503105654,
                                        'source_pixel_width': -3939804931262181693,
                                        'source_pixel_height': -800981955403275065,
                                        'rotation': -420004640170835207,
                                        'virtual_nw_x_pixel': 1554863390,
                                        'virtual_nw_y_pixel': -226614411,
                                        'virtual_width': -723721886,
                                        'virtual_height': 378177892,
                                    },
                            {
                                        'source_monitor': 7026186,
                                        'source_nw_x_pixel': -5158216800842844344,
                                        'source_nw_y_pixel': -1598476567078954759,
                                        'source_pixel_width': -8648534937760712652,
                                        'source_pixel_height': -6553742659766571626,
                                        'rotation': -6686349931715031005,
                                        'virtual_nw_x_pixel': -1803584664,
                                        'virtual_nw_y_pixel': 176007363,
                                        'virtual_width': -866305506,
                                        'virtual_height': 1896423934,
                                    },
                        ],
                },
                {
                    'description': 'ЀʪĐ\x88OƝȊΩ!Θ;ŀϧȆӶǐØӛͺ˨ҸƎōҋоηÀӔ¯Ҝ',
                    'monitors': [
                            {
                                        'identifier': 3432174,
                                        'width': -5608767403415238294,
                                        'height': 2201453991994298602,
                                    },
                            {
                                        'identifier': 6711882,
                                        'width': 4815019785884234169,
                                        'height': -1675542459600065094,
                                    },
                            {
                                        'identifier': 1611688,
                                        'width': 6678779522133118462,
                                        'height': 8165788896342103964,
                                    },
                            {
                                        'identifier': -17807,
                                        'width': 7141923458097956897,
                                        'height': -3229006064187628501,
                                    },
                            {
                                        'identifier': 3266783,
                                        'width': -3059107884885072025,
                                        'height': -8501933269539441493,
                                    },
                            {
                                        'identifier': 3731666,
                                        'width': -1409894520633980716,
                                        'height': 7914663216113050212,
                                    },
                            {
                                        'identifier': 6914823,
                                        'width': 1045461221282294924,
                                        'height': -2500514952806253642,
                                    },
                            {
                                        'identifier': 390134,
                                        'width': -5264583710568285622,
                                        'height': -2514355417369873751,
                                    },
                            {
                                        'identifier': 9395459,
                                        'width': 2295998522323409520,
                                        'height': -7146583089903032349,
                                    },
                            {
                                        'identifier': 5833182,
                                        'width': 2600252724719253943,
                                        'height': 4114333046740547858,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 288435,
                                        'source_nw_x_pixel': -9038102644894214834,
                                        'source_nw_y_pixel': -5219001665531743765,
                                        'source_pixel_width': -2937053124792060902,
                                        'source_pixel_height': -3718511125666656141,
                                        'rotation': -1134718371009421999,
                                        'virtual_nw_x_pixel': -1415949918,
                                        'virtual_nw_y_pixel': -1601050861,
                                        'virtual_width': -924305536,
                                        'virtual_height': 1281148321,
                                    },
                            {
                                        'source_monitor': 6832831,
                                        'source_nw_x_pixel': -3195520517237790824,
                                        'source_nw_y_pixel': -4670732862701402696,
                                        'source_pixel_width': -8003201117540572667,
                                        'source_pixel_height': -152312924201683780,
                                        'rotation': -1072167190127095176,
                                        'virtual_nw_x_pixel': -1246527316,
                                        'virtual_nw_y_pixel': 1393495940,
                                        'virtual_width': 1916786764,
                                        'virtual_height': -558759832,
                                    },
                            {
                                        'source_monitor': 7131932,
                                        'source_nw_x_pixel': -674511718164194147,
                                        'source_nw_y_pixel': -4067313940150872190,
                                        'source_pixel_width': -5226449382451490281,
                                        'source_pixel_height': -5810247503137894520,
                                        'rotation': -7904279498443660446,
                                        'virtual_nw_x_pixel': -1470651593,
                                        'virtual_nw_y_pixel': -1335195421,
                                        'virtual_width': 1220043545,
                                        'virtual_height': 418785035,
                                    },
                            {
                                        'source_monitor': 5085798,
                                        'source_nw_x_pixel': -2119994740566838103,
                                        'source_nw_y_pixel': -12905143186884633,
                                        'source_pixel_width': -6332214868437028033,
                                        'source_pixel_height': -2516702368510474100,
                                        'rotation': -7091898480687165085,
                                        'virtual_nw_x_pixel': -1437630255,
                                        'virtual_nw_y_pixel': 629309194,
                                        'virtual_width': 454476282,
                                        'virtual_height': 796482736,
                                    },
                            {
                                        'source_monitor': -610090,
                                        'source_nw_x_pixel': -1881731725019301385,
                                        'source_nw_y_pixel': -4146808764541983238,
                                        'source_pixel_width': -3123435967319111165,
                                        'source_pixel_height': -8283732167303166162,
                                        'rotation': -8327574610466070662,
                                        'virtual_nw_x_pixel': -1151718086,
                                        'virtual_nw_y_pixel': 1202042166,
                                        'virtual_width': 1315524819,
                                        'virtual_height': -51436677,
                                    },
                            {
                                        'source_monitor': 3405961,
                                        'source_nw_x_pixel': -7737286725506424266,
                                        'source_nw_y_pixel': -103991259088883220,
                                        'source_pixel_width': -4793352333327989280,
                                        'source_pixel_height': -6075959761607266695,
                                        'rotation': -7226543111705099898,
                                        'virtual_nw_x_pixel': 1478981748,
                                        'virtual_nw_y_pixel': 781445139,
                                        'virtual_width': -441070120,
                                        'virtual_height': 731694907,
                                    },
                            {
                                        'source_monitor': 1107335,
                                        'source_nw_x_pixel': -7394127275980763760,
                                        'source_nw_y_pixel': -1283044559550630719,
                                        'source_pixel_width': -5528031511564143241,
                                        'source_pixel_height': -1026419543034579925,
                                        'rotation': -831350488035072826,
                                        'virtual_nw_x_pixel': 1021571185,
                                        'virtual_nw_y_pixel': 961019043,
                                        'virtual_width': -1868853642,
                                        'virtual_height': -1254599061,
                                    },
                            {
                                        'source_monitor': 6837257,
                                        'source_nw_x_pixel': -6099148678281996668,
                                        'source_nw_y_pixel': -5550385004282718557,
                                        'source_pixel_width': -3633682049188961092,
                                        'source_pixel_height': -464964435357413248,
                                        'rotation': -4929609172533902909,
                                        'virtual_nw_x_pixel': -1266557297,
                                        'virtual_nw_y_pixel': 1024504224,
                                        'virtual_width': 203606885,
                                        'virtual_height': -1853766118,
                                    },
                            {
                                        'source_monitor': -223708,
                                        'source_nw_x_pixel': -7624094408910332681,
                                        'source_nw_y_pixel': -5222596839108842205,
                                        'source_pixel_width': -8155396854532939120,
                                        'source_pixel_height': -2263576062332874533,
                                        'rotation': -4348195578399589868,
                                        'virtual_nw_x_pixel': 232829483,
                                        'virtual_nw_y_pixel': -866124795,
                                        'virtual_width': 1287342095,
                                        'virtual_height': 209191235,
                                    },
                            {
                                        'source_monitor': 6577829,
                                        'source_nw_x_pixel': -522415647300368357,
                                        'source_nw_y_pixel': -8948189003879139107,
                                        'source_pixel_width': -3863170983539191850,
                                        'source_pixel_height': -6411514342044975509,
                                        'rotation': -442689609982471156,
                                        'virtual_nw_x_pixel': -540895819,
                                        'virtual_nw_y_pixel': 1350823063,
                                        'virtual_width': -1988557830,
                                        'virtual_height': -975424797,
                                    },
                        ],
                },
                {
                    'description': 'ҼɅɺBdˑľδńҥʹȰЕą±ҽZԋ+ѠʝĴ˛ҎōřĬЍǜ;',
                    'monitors': [
                            {
                                        'identifier': -588515,
                                        'width': 5695840000891780502,
                                        'height': -2428673893690092928,
                                    },
                            {
                                        'identifier': 8674785,
                                        'width': -594393950412496822,
                                        'height': 261540131817470634,
                                    },
                            {
                                        'identifier': 1911822,
                                        'width': -2278748910010300632,
                                        'height': 7699251561262196206,
                                    },
                            {
                                        'identifier': 7836677,
                                        'width': 4620607860618335008,
                                        'height': -8137466336308546368,
                                    },
                            {
                                        'identifier': 715126,
                                        'width': -3645420749963047426,
                                        'height': -3259312338327233929,
                                    },
                            {
                                        'identifier': 9610071,
                                        'width': 2999195214388217096,
                                        'height': -3537861007212837127,
                                    },
                            {
                                        'identifier': 8863790,
                                        'width': -5224410916191472935,
                                        'height': 1258942540354657742,
                                    },
                            {
                                        'identifier': 9379468,
                                        'width': -7775430735196305246,
                                        'height': 7864258524021112477,
                                    },
                            {
                                        'identifier': 7262440,
                                        'width': -3026345502620145812,
                                        'height': -848247188885284190,
                                    },
                            {
                                        'identifier': 1353181,
                                        'width': 5227983923247449656,
                                        'height': -5094498729016922770,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8483470,
                                        'source_nw_x_pixel': -3677309472316330234,
                                        'source_nw_y_pixel': -4093160437894834514,
                                        'source_pixel_width': -7118972326315010573,
                                        'source_pixel_height': -2457519009353341007,
                                        'rotation': -4231204925112953909,
                                        'virtual_nw_x_pixel': -1517046511,
                                        'virtual_nw_y_pixel': -1915750188,
                                        'virtual_width': 1222410804,
                                        'virtual_height': 160659296,
                                    },
                            {
                                        'source_monitor': 6020492,
                                        'source_nw_x_pixel': -4603689380548625448,
                                        'source_nw_y_pixel': -8177219259740576055,
                                        'source_pixel_width': -7194569335905813549,
                                        'source_pixel_height': -8664218122500322287,
                                        'rotation': -7828853513484799177,
                                        'virtual_nw_x_pixel': -1114665807,
                                        'virtual_nw_y_pixel': -966899266,
                                        'virtual_width': 956224654,
                                        'virtual_height': -226178699,
                                    },
                            {
                                        'source_monitor': 2143045,
                                        'source_nw_x_pixel': -642056147131337480,
                                        'source_nw_y_pixel': -3228555570071065925,
                                        'source_pixel_width': -3522848797811717733,
                                        'source_pixel_height': -4345512723753806361,
                                        'rotation': -3493504691170984717,
                                        'virtual_nw_x_pixel': 153953702,
                                        'virtual_nw_y_pixel': 1904088775,
                                        'virtual_width': 664766793,
                                        'virtual_height': -237499645,
                                    },
                            {
                                        'source_monitor': 5720044,
                                        'source_nw_x_pixel': -3282539499877128882,
                                        'source_nw_y_pixel': -4157906456599880956,
                                        'source_pixel_width': -4882216817902848920,
                                        'source_pixel_height': -1983767576276624432,
                                        'rotation': -6668154122270065352,
                                        'virtual_nw_x_pixel': -1301639764,
                                        'virtual_nw_y_pixel': 321620213,
                                        'virtual_width': -10565355,
                                        'virtual_height': 1675475950,
                                    },
                            {
                                        'source_monitor': 678847,
                                        'source_nw_x_pixel': -3552750339040650315,
                                        'source_nw_y_pixel': -8575394728156023543,
                                        'source_pixel_width': -4364959603968192276,
                                        'source_pixel_height': -573926937832451703,
                                        'rotation': -6712463782232280096,
                                        'virtual_nw_x_pixel': 764677015,
                                        'virtual_nw_y_pixel': -258287253,
                                        'virtual_width': -897192970,
                                        'virtual_height': 300127872,
                                    },
                            {
                                        'source_monitor': 1986797,
                                        'source_nw_x_pixel': -3413524045202403505,
                                        'source_nw_y_pixel': -5294524897030337602,
                                        'source_pixel_width': -2485875553152943794,
                                        'source_pixel_height': -6438281785643600946,
                                        'rotation': -7282475249732828538,
                                        'virtual_nw_x_pixel': -1937917883,
                                        'virtual_nw_y_pixel': -1431249278,
                                        'virtual_width': -1804700278,
                                        'virtual_height': -1746114378,
                                    },
                            {
                                        'source_monitor': 9723280,
                                        'source_nw_x_pixel': -6547900196035800566,
                                        'source_nw_y_pixel': -893896018629675304,
                                        'source_pixel_width': -7948213466612321865,
                                        'source_pixel_height': -7007869228049050519,
                                        'rotation': -3375279670468818001,
                                        'virtual_nw_x_pixel': 1189781628,
                                        'virtual_nw_y_pixel': -835351113,
                                        'virtual_width': 999009030,
                                        'virtual_height': 74999025,
                                    },
                            {
                                        'source_monitor': 4960619,
                                        'source_nw_x_pixel': -7405989739657284299,
                                        'source_nw_y_pixel': -865387875427708958,
                                        'source_pixel_width': -1321807406845055971,
                                        'source_pixel_height': -5157955537516318558,
                                        'rotation': -3837795765735911804,
                                        'virtual_nw_x_pixel': 123786984,
                                        'virtual_nw_y_pixel': 416615628,
                                        'virtual_width': -1676622681,
                                        'virtual_height': -167528918,
                                    },
                            {
                                        'source_monitor': 7506287,
                                        'source_nw_x_pixel': -3774253270396699941,
                                        'source_nw_y_pixel': -7651887363869356118,
                                        'source_pixel_width': -6750151503313476318,
                                        'source_pixel_height': -7781615330904336094,
                                        'rotation': -2783453366406666577,
                                        'virtual_nw_x_pixel': -598272639,
                                        'virtual_nw_y_pixel': 1873362692,
                                        'virtual_width': 220577955,
                                        'virtual_height': 1438413378,
                                    },
                            {
                                        'source_monitor': 5735779,
                                        'source_nw_x_pixel': -3410217675182802997,
                                        'source_nw_y_pixel': -6130402681065433205,
                                        'source_pixel_width': -3555009186523731776,
                                        'source_pixel_height': -7954146880680628802,
                                        'rotation': -5474277472333957551,
                                        'virtual_nw_x_pixel': 498887274,
                                        'virtual_nw_y_pixel': -497482361,
                                        'virtual_width': 433719952,
                                        'virtual_height': 63617735,
                                    },
                        ],
                },
                {
                    'description': 'ǈė\xadӒʐE}ȖƂҶʿѿƱИʯƅȲØ\x8dŎǮǊŗh0ͰUǺ҂Ө',
                    'monitors': [
                            {
                                        'identifier': 3188309,
                                        'width': -6175846682420235512,
                                        'height': 4602096449260692305,
                                    },
                            {
                                        'identifier': 7658586,
                                        'width': 2372378297570306898,
                                        'height': 554325998983116053,
                                    },
                            {
                                        'identifier': 8706743,
                                        'width': -6737719228323149234,
                                        'height': 3283797298481658358,
                                    },
                            {
                                        'identifier': 9479005,
                                        'width': -2354632766504130256,
                                        'height': 3008013403029170497,
                                    },
                            {
                                        'identifier': 5349854,
                                        'width': -7278416157213766114,
                                        'height': 393958954770546826,
                                    },
                            {
                                        'identifier': 8195655,
                                        'width': 6452216944026378418,
                                        'height': -4724653692267319841,
                                    },
                            {
                                        'identifier': 9860747,
                                        'width': -6244885297576352691,
                                        'height': -4928639588469317153,
                                    },
                            {
                                        'identifier': 1181213,
                                        'width': 8100914416412116787,
                                        'height': -4171779761665406839,
                                    },
                            {
                                        'identifier': 1531707,
                                        'width': -5462157559539048858,
                                        'height': -3605510345699895793,
                                    },
                            {
                                        'identifier': 6949923,
                                        'width': 360408508918704769,
                                        'height': -1974026227994958601,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6735438,
                                        'source_nw_x_pixel': -5524466729999736909,
                                        'source_nw_y_pixel': -1892695160131990198,
                                        'source_pixel_width': -6001960730251917134,
                                        'source_pixel_height': -9090578769459504179,
                                        'rotation': -1258325157473538970,
                                        'virtual_nw_x_pixel': -162124791,
                                        'virtual_nw_y_pixel': -1059701374,
                                        'virtual_width': 1617357400,
                                        'virtual_height': 414462998,
                                    },
                            {
                                        'source_monitor': -155538,
                                        'source_nw_x_pixel': -4134029102319677916,
                                        'source_nw_y_pixel': -2579958533958850015,
                                        'source_pixel_width': -4560344271474242407,
                                        'source_pixel_height': -6614153502882963794,
                                        'rotation': -2590004980121468064,
                                        'virtual_nw_x_pixel': 40083373,
                                        'virtual_nw_y_pixel': 64213591,
                                        'virtual_width': -1159486269,
                                        'virtual_height': -184951241,
                                    },
                            {
                                        'source_monitor': 4245379,
                                        'source_nw_x_pixel': -4492971009469108438,
                                        'source_nw_y_pixel': -1095311589820469612,
                                        'source_pixel_width': -4293728450982404376,
                                        'source_pixel_height': -8265730230967166971,
                                        'rotation': -1522826304772665690,
                                        'virtual_nw_x_pixel': -64708481,
                                        'virtual_nw_y_pixel': 1356163387,
                                        'virtual_width': -187963247,
                                        'virtual_height': 863900044,
                                    },
                            {
                                        'source_monitor': 2175212,
                                        'source_nw_x_pixel': -1542503513777944120,
                                        'source_nw_y_pixel': -688391599918186572,
                                        'source_pixel_width': -8876095239589552675,
                                        'source_pixel_height': -394101884258746890,
                                        'rotation': -5515051404910439477,
                                        'virtual_nw_x_pixel': 1977041276,
                                        'virtual_nw_y_pixel': 1918245020,
                                        'virtual_width': -1848572420,
                                        'virtual_height': -508980889,
                                    },
                            {
                                        'source_monitor': 621008,
                                        'source_nw_x_pixel': -6746084388949733127,
                                        'source_nw_y_pixel': -8247324842207155356,
                                        'source_pixel_width': -9191228478168070106,
                                        'source_pixel_height': -2528205184859727323,
                                        'rotation': -8417265648797918497,
                                        'virtual_nw_x_pixel': 965185123,
                                        'virtual_nw_y_pixel': -1615640989,
                                        'virtual_width': -249067592,
                                        'virtual_height': 724181771,
                                    },
                            {
                                        'source_monitor': 9648098,
                                        'source_nw_x_pixel': -8797364220561355046,
                                        'source_nw_y_pixel': -8858038233001506656,
                                        'source_pixel_width': -3607274100513549449,
                                        'source_pixel_height': -943767839318153775,
                                        'rotation': -8708694200998726900,
                                        'virtual_nw_x_pixel': 465079407,
                                        'virtual_nw_y_pixel': 384145703,
                                        'virtual_width': -1460252019,
                                        'virtual_height': 1966803241,
                                    },
                            {
                                        'source_monitor': 7511967,
                                        'source_nw_x_pixel': -3458511299626063155,
                                        'source_nw_y_pixel': -7800455771416129256,
                                        'source_pixel_width': -7373121885816859950,
                                        'source_pixel_height': -1055010095858539706,
                                        'rotation': -4081524358333570168,
                                        'virtual_nw_x_pixel': -930523949,
                                        'virtual_nw_y_pixel': 437149201,
                                        'virtual_width': -341506477,
                                        'virtual_height': 848628983,
                                    },
                            {
                                        'source_monitor': -837320,
                                        'source_nw_x_pixel': -1292988999053291104,
                                        'source_nw_y_pixel': -4449142896149053685,
                                        'source_pixel_width': -9066670825611286392,
                                        'source_pixel_height': -2368921648816406662,
                                        'rotation': -4714550229888889007,
                                        'virtual_nw_x_pixel': 1135917550,
                                        'virtual_nw_y_pixel': 315035425,
                                        'virtual_width': -167177002,
                                        'virtual_height': 1067760611,
                                    },
                            {
                                        'source_monitor': 6630559,
                                        'source_nw_x_pixel': -225613988565370380,
                                        'source_nw_y_pixel': -6020211370505843666,
                                        'source_pixel_width': -1534900865997241623,
                                        'source_pixel_height': -7720170752042420546,
                                        'rotation': -4715601659063783592,
                                        'virtual_nw_x_pixel': 664055890,
                                        'virtual_nw_y_pixel': 230104188,
                                        'virtual_width': 1523536305,
                                        'virtual_height': -363727367,
                                    },
                            {
                                        'source_monitor': 2458276,
                                        'source_nw_x_pixel': -989389222394201077,
                                        'source_nw_y_pixel': -7086533191247307310,
                                        'source_pixel_width': -6966898080710436185,
                                        'source_pixel_height': -1067827888863913418,
                                        'rotation': -7679098320861390281,
                                        'virtual_nw_x_pixel': -734092392,
                                        'virtual_nw_y_pixel': -1591553755,
                                        'virtual_width': -1410493346,
                                        'virtual_height': -1220994124,
                                    },
                        ],
                },
                {
                    'description': 'Ѩ˞Ðɐϩ7ć&уâʒďäЯԃȫӯϳ˙ɛњЂ8ʂδƇķш\x9e<',
                    'monitors': [
                            {
                                        'identifier': 5595784,
                                        'width': -9010601794414006793,
                                        'height': -2314851061360636748,
                                    },
                            {
                                        'identifier': 6339087,
                                        'width': 7986706500544291133,
                                        'height': 3005521664034141238,
                                    },
                            {
                                        'identifier': 5192599,
                                        'width': 8009324527028275586,
                                        'height': -793743537359492268,
                                    },
                            {
                                        'identifier': 3432269,
                                        'width': -5860438276730846981,
                                        'height': 2647293113567527835,
                                    },
                            {
                                        'identifier': 5056949,
                                        'width': 3391133450273351526,
                                        'height': -6671316788956442569,
                                    },
                            {
                                        'identifier': -990241,
                                        'width': -6136140744753784825,
                                        'height': 2124610650262246634,
                                    },
                            {
                                        'identifier': 9958378,
                                        'width': 2431394168333229579,
                                        'height': 2690142450765732681,
                                    },
                            {
                                        'identifier': 7999983,
                                        'width': -9005797303948707822,
                                        'height': -5205836852252296292,
                                    },
                            {
                                        'identifier': 8418187,
                                        'width': 6136973936630787853,
                                        'height': 7755194967277560323,
                                    },
                            {
                                        'identifier': 319139,
                                        'width': -1362576991250328314,
                                        'height': 4644460840167839493,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5257246,
                                        'source_nw_x_pixel': -3609428378598567753,
                                        'source_nw_y_pixel': -894546673894377922,
                                        'source_pixel_width': -2289211270068382619,
                                        'source_pixel_height': -3793174626887650595,
                                        'rotation': -5235217574254104602,
                                        'virtual_nw_x_pixel': 327592595,
                                        'virtual_nw_y_pixel': 823092302,
                                        'virtual_width': 1203320131,
                                        'virtual_height': 68849613,
                                    },
                            {
                                        'source_monitor': 7401837,
                                        'source_nw_x_pixel': -969695561638757554,
                                        'source_nw_y_pixel': -4967003802402333299,
                                        'source_pixel_width': -3114229185282423472,
                                        'source_pixel_height': -7978823747807328253,
                                        'rotation': -4103643635502114101,
                                        'virtual_nw_x_pixel': -1403953130,
                                        'virtual_nw_y_pixel': -796674908,
                                        'virtual_width': -1953901282,
                                        'virtual_height': 685896608,
                                    },
                            {
                                        'source_monitor': 6816044,
                                        'source_nw_x_pixel': -4536524182148113248,
                                        'source_nw_y_pixel': -1444939689286117787,
                                        'source_pixel_width': -6276966792878239024,
                                        'source_pixel_height': -676477935421492523,
                                        'rotation': -3222101373669623183,
                                        'virtual_nw_x_pixel': 1596280953,
                                        'virtual_nw_y_pixel': 34193307,
                                        'virtual_width': 947031954,
                                        'virtual_height': -930475800,
                                    },
                            {
                                        'source_monitor': 8104930,
                                        'source_nw_x_pixel': -1296826358796860127,
                                        'source_nw_y_pixel': -6909937997885155180,
                                        'source_pixel_width': -1410917363657783308,
                                        'source_pixel_height': -6051266276273519171,
                                        'rotation': -684869151380375818,
                                        'virtual_nw_x_pixel': -30571804,
                                        'virtual_nw_y_pixel': 412296723,
                                        'virtual_width': -6359703,
                                        'virtual_height': -665709721,
                                    },
                            {
                                        'source_monitor': -661976,
                                        'source_nw_x_pixel': -4306608768823660299,
                                        'source_nw_y_pixel': -4962949784774532522,
                                        'source_pixel_width': -689348370243854131,
                                        'source_pixel_height': -8439881948694464461,
                                        'rotation': -8023205239272292008,
                                        'virtual_nw_x_pixel': -1366543280,
                                        'virtual_nw_y_pixel': -1641074318,
                                        'virtual_width': 942185049,
                                        'virtual_height': 770262647,
                                    },
                            {
                                        'source_monitor': 5666450,
                                        'source_nw_x_pixel': -7822724126862288090,
                                        'source_nw_y_pixel': -8949688061771829218,
                                        'source_pixel_width': -2296903602682665337,
                                        'source_pixel_height': -2363394993287536528,
                                        'rotation': -1587892843814255779,
                                        'virtual_nw_x_pixel': 1623882059,
                                        'virtual_nw_y_pixel': 1046014378,
                                        'virtual_width': -378292027,
                                        'virtual_height': 1449157449,
                                    },
                            {
                                        'source_monitor': 5778587,
                                        'source_nw_x_pixel': -3220817570316952114,
                                        'source_nw_y_pixel': -8523708996254894675,
                                        'source_pixel_width': -5990746756669979915,
                                        'source_pixel_height': -648925082950741460,
                                        'rotation': -8701155372441428934,
                                        'virtual_nw_x_pixel': 121315426,
                                        'virtual_nw_y_pixel': 464175489,
                                        'virtual_width': 1746278377,
                                        'virtual_height': 1755371256,
                                    },
                            {
                                        'source_monitor': 2970901,
                                        'source_nw_x_pixel': -683303880423573986,
                                        'source_nw_y_pixel': -757794520490401075,
                                        'source_pixel_width': -3393682956068540426,
                                        'source_pixel_height': -6347177464933828717,
                                        'rotation': -7248333706243735734,
                                        'virtual_nw_x_pixel': 1767625459,
                                        'virtual_nw_y_pixel': -1919088529,
                                        'virtual_width': -786097095,
                                        'virtual_height': 1505741070,
                                    },
                            {
                                        'source_monitor': 8806020,
                                        'source_nw_x_pixel': -3776580579427941073,
                                        'source_nw_y_pixel': -904601616294891665,
                                        'source_pixel_width': -7264105140081244927,
                                        'source_pixel_height': -7796864145676560701,
                                        'rotation': -6125270001125075987,
                                        'virtual_nw_x_pixel': -301934062,
                                        'virtual_nw_y_pixel': -1169861087,
                                        'virtual_width': 1008021232,
                                        'virtual_height': -1460456428,
                                    },
                            {
                                        'source_monitor': 8633119,
                                        'source_nw_x_pixel': -7068114532588888848,
                                        'source_nw_y_pixel': -2732190802039369809,
                                        'source_pixel_width': -7677927851223340894,
                                        'source_pixel_height': -8432443179582530256,
                                        'rotation': -6998018753290246286,
                                        'virtual_nw_x_pixel': 517748694,
                                        'virtual_nw_y_pixel': -1732241102,
                                        'virtual_width': 601489513,
                                        'virtual_height': 1690975224,
                                    },
                        ],
                },
                {
                    'description': 'ɒ6ìˣϾѭϳĵѬҺΎƊηĉðɺƖȘȳǠŊƧȀʧβĐǿ\x98ѼɆ',
                    'monitors': [
                            {
                                        'identifier': 6797877,
                                        'width': -8736244112764233562,
                                        'height': -2576471984716987648,
                                    },
                            {
                                        'identifier': 9832049,
                                        'width': 1888610090054216505,
                                        'height': -8572938097857195078,
                                    },
                            {
                                        'identifier': -415989,
                                        'width': -4188606960776393919,
                                        'height': 1454262917777187608,
                                    },
                            {
                                        'identifier': 5553218,
                                        'width': 8198684315339474270,
                                        'height': 3912268602393387635,
                                    },
                            {
                                        'identifier': -92621,
                                        'width': 8656320480549772807,
                                        'height': 146949506379791093,
                                    },
                            {
                                        'identifier': 4603579,
                                        'width': -5344846811533222109,
                                        'height': 2719326652605805753,
                                    },
                            {
                                        'identifier': 2000369,
                                        'width': -7210955300564454795,
                                        'height': -3865795266003358169,
                                    },
                            {
                                        'identifier': -32828,
                                        'width': 1670629570820066871,
                                        'height': 6272764507828625994,
                                    },
                            {
                                        'identifier': 8048721,
                                        'width': 2228330154405290067,
                                        'height': -6900443190792818943,
                                    },
                            {
                                        'identifier': 9518130,
                                        'width': -7639605342967692153,
                                        'height': 791726389871645909,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3192702,
                                        'source_nw_x_pixel': -3328266306548944796,
                                        'source_nw_y_pixel': -1607743815514148698,
                                        'source_pixel_width': -7434327306366331346,
                                        'source_pixel_height': -2224157591554679785,
                                        'rotation': -631284126155188594,
                                        'virtual_nw_x_pixel': 1337605376,
                                        'virtual_nw_y_pixel': 1931125105,
                                        'virtual_width': 832455095,
                                        'virtual_height': -1737015645,
                                    },
                            {
                                        'source_monitor': 2450071,
                                        'source_nw_x_pixel': -6922560772877489763,
                                        'source_nw_y_pixel': -2199199556240445467,
                                        'source_pixel_width': -1759053049094912156,
                                        'source_pixel_height': -7475955669829084732,
                                        'rotation': -6951082387986948869,
                                        'virtual_nw_x_pixel': 311736048,
                                        'virtual_nw_y_pixel': -1132797377,
                                        'virtual_width': -908003604,
                                        'virtual_height': -855576885,
                                    },
                            {
                                        'source_monitor': 4855348,
                                        'source_nw_x_pixel': -6647798003592859796,
                                        'source_nw_y_pixel': -8017197723548247920,
                                        'source_pixel_width': -8066471996644569521,
                                        'source_pixel_height': -6400001486173989668,
                                        'rotation': -5731878778230266939,
                                        'virtual_nw_x_pixel': -811169523,
                                        'virtual_nw_y_pixel': 1819439117,
                                        'virtual_width': -6831120,
                                        'virtual_height': 1296213927,
                                    },
                            {
                                        'source_monitor': 9697026,
                                        'source_nw_x_pixel': -2666239357960890682,
                                        'source_nw_y_pixel': -8555365687651719345,
                                        'source_pixel_width': -1057717762238596282,
                                        'source_pixel_height': -5033564368215838684,
                                        'rotation': -2611581788317611282,
                                        'virtual_nw_x_pixel': -319947940,
                                        'virtual_nw_y_pixel': -1760421314,
                                        'virtual_width': 558959836,
                                        'virtual_height': -1989841710,
                                    },
                            {
                                        'source_monitor': 3852073,
                                        'source_nw_x_pixel': -8233066338794368918,
                                        'source_nw_y_pixel': -2311075776471517075,
                                        'source_pixel_width': -3046339374552548755,
                                        'source_pixel_height': -3773369376546323458,
                                        'rotation': -6201814189738947205,
                                        'virtual_nw_x_pixel': -23164170,
                                        'virtual_nw_y_pixel': 400470434,
                                        'virtual_width': -1085764974,
                                        'virtual_height': 716458786,
                                    },
                            {
                                        'source_monitor': 5891337,
                                        'source_nw_x_pixel': -5965908921057732982,
                                        'source_nw_y_pixel': -3360651389227576059,
                                        'source_pixel_width': -5530414347835388074,
                                        'source_pixel_height': -1275301888180594070,
                                        'rotation': -7125567419757195125,
                                        'virtual_nw_x_pixel': -373508965,
                                        'virtual_nw_y_pixel': 1505283424,
                                        'virtual_width': -1226623640,
                                        'virtual_height': 1521093937,
                                    },
                            {
                                        'source_monitor': 6724302,
                                        'source_nw_x_pixel': -5445231062311959955,
                                        'source_nw_y_pixel': -5062175544804450078,
                                        'source_pixel_width': -817882507957664333,
                                        'source_pixel_height': -4989571292668312355,
                                        'rotation': -5163347735977129782,
                                        'virtual_nw_x_pixel': -1843173409,
                                        'virtual_nw_y_pixel': -1555736024,
                                        'virtual_width': -1615296057,
                                        'virtual_height': -1524038366,
                                    },
                            {
                                        'source_monitor': -371145,
                                        'source_nw_x_pixel': -6569601538237340700,
                                        'source_nw_y_pixel': -5952108028163966106,
                                        'source_pixel_width': -8900963250401800582,
                                        'source_pixel_height': -2398594018304001010,
                                        'rotation': -1625673133386988984,
                                        'virtual_nw_x_pixel': 1608448451,
                                        'virtual_nw_y_pixel': -1065500111,
                                        'virtual_width': -1486676633,
                                        'virtual_height': -1895313261,
                                    },
                            {
                                        'source_monitor': 9667516,
                                        'source_nw_x_pixel': -2047171771215614154,
                                        'source_nw_y_pixel': -3708414204829299395,
                                        'source_pixel_width': -2517845182476848209,
                                        'source_pixel_height': -4802961630317592514,
                                        'rotation': -1817525686296589077,
                                        'virtual_nw_x_pixel': 44688694,
                                        'virtual_nw_y_pixel': 430730680,
                                        'virtual_width': 384270184,
                                        'virtual_height': -1149894104,
                                    },
                            {
                                        'source_monitor': 5503699,
                                        'source_nw_x_pixel': -2381706433775120803,
                                        'source_nw_y_pixel': -1619874207504574540,
                                        'source_pixel_width': -1765177478604723138,
                                        'source_pixel_height': -2545455137127677457,
                                        'rotation': -7506593470178098143,
                                        'virtual_nw_x_pixel': 626424903,
                                        'virtual_nw_y_pixel': -1035701020,
                                        'virtual_width': 1115122688,
                                        'virtual_height': 1857120227,
                                    },
                        ],
                },
                {
                    'description': 'Ȝ\x91ҤфŔДҟą5ӫЋъҸɖԅ˛Ï0ʗϫԎǷʵνԎѵЙҬa®',
                    'monitors': [
                            {
                                        'identifier': 125542,
                                        'width': 2921182677393508372,
                                        'height': 2780953091065107426,
                                    },
                            {
                                        'identifier': 265078,
                                        'width': 7390679728045132314,
                                        'height': -3624408887936778593,
                                    },
                            {
                                        'identifier': 9392554,
                                        'width': 1194800608390058835,
                                        'height': -5106780040764627006,
                                    },
                            {
                                        'identifier': 190175,
                                        'width': 9176178681456079313,
                                        'height': 624462933803851404,
                                    },
                            {
                                        'identifier': 2889923,
                                        'width': 3142893874834761438,
                                        'height': 1600304604381953433,
                                    },
                            {
                                        'identifier': 2932207,
                                        'width': -3995398564545181361,
                                        'height': -5460254747832584168,
                                    },
                            {
                                        'identifier': 7300632,
                                        'width': 7972279530416883534,
                                        'height': 7892440745936051332,
                                    },
                            {
                                        'identifier': 8632161,
                                        'width': 5310310222230805082,
                                        'height': -2279450914721769523,
                                    },
                            {
                                        'identifier': 2335438,
                                        'width': 5447504794900798113,
                                        'height': 8309333218950058720,
                                    },
                            {
                                        'identifier': 4734322,
                                        'width': 2007434964857424570,
                                        'height': -6977189239858735429,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1649533,
                                        'source_nw_x_pixel': -5118403200352323227,
                                        'source_nw_y_pixel': -2114750051356000147,
                                        'source_pixel_width': -6936145162623123719,
                                        'source_pixel_height': -7352180851399553025,
                                        'rotation': -7803632712806524852,
                                        'virtual_nw_x_pixel': -808699420,
                                        'virtual_nw_y_pixel': 687257534,
                                        'virtual_width': 137958671,
                                        'virtual_height': 1871471439,
                                    },
                            {
                                        'source_monitor': 7171145,
                                        'source_nw_x_pixel': -6384669576450123235,
                                        'source_nw_y_pixel': -5542787425140726340,
                                        'source_pixel_width': -5529993951871739947,
                                        'source_pixel_height': -4866958045871531026,
                                        'rotation': -5011354157946462995,
                                        'virtual_nw_x_pixel': 665973011,
                                        'virtual_nw_y_pixel': -1715722296,
                                        'virtual_width': 586107157,
                                        'virtual_height': 393189358,
                                    },
                            {
                                        'source_monitor': 1098476,
                                        'source_nw_x_pixel': -5093305133667602095,
                                        'source_nw_y_pixel': -5302695491878468456,
                                        'source_pixel_width': -503162800398740972,
                                        'source_pixel_height': -4262080159961220014,
                                        'rotation': -7390712009215474767,
                                        'virtual_nw_x_pixel': -1572119361,
                                        'virtual_nw_y_pixel': -485793885,
                                        'virtual_width': 1857669161,
                                        'virtual_height': -1814318234,
                                    },
                            {
                                        'source_monitor': 8474147,
                                        'source_nw_x_pixel': -2807659893306630194,
                                        'source_nw_y_pixel': -578951281569287554,
                                        'source_pixel_width': -4990134681109677344,
                                        'source_pixel_height': -7343485452097784346,
                                        'rotation': -2983373945397312187,
                                        'virtual_nw_x_pixel': -1114114109,
                                        'virtual_nw_y_pixel': -1767530221,
                                        'virtual_width': -1993147408,
                                        'virtual_height': 886990795,
                                    },
                            {
                                        'source_monitor': 7888993,
                                        'source_nw_x_pixel': -4375293343039215237,
                                        'source_nw_y_pixel': -4151791740573187985,
                                        'source_pixel_width': -3940557475566304976,
                                        'source_pixel_height': -6948335988673130163,
                                        'rotation': -4597332376376437325,
                                        'virtual_nw_x_pixel': 1702221184,
                                        'virtual_nw_y_pixel': -1190201971,
                                        'virtual_width': 1778303152,
                                        'virtual_height': -1759282538,
                                    },
                            {
                                        'source_monitor': 5529355,
                                        'source_nw_x_pixel': -6288636567371193785,
                                        'source_nw_y_pixel': -6571392276804927358,
                                        'source_pixel_width': -7356135108583160728,
                                        'source_pixel_height': -243985486527418347,
                                        'rotation': -964188824838287923,
                                        'virtual_nw_x_pixel': -1789425758,
                                        'virtual_nw_y_pixel': 915649429,
                                        'virtual_width': 1457971082,
                                        'virtual_height': 1063748884,
                                    },
                            {
                                        'source_monitor': 7629669,
                                        'source_nw_x_pixel': -2384440494682047199,
                                        'source_nw_y_pixel': -4740612395193772815,
                                        'source_pixel_width': -7298321604659686860,
                                        'source_pixel_height': -3939127867748885051,
                                        'rotation': -1586559204061906217,
                                        'virtual_nw_x_pixel': 1251527843,
                                        'virtual_nw_y_pixel': -483573594,
                                        'virtual_width': 231196228,
                                        'virtual_height': -206588993,
                                    },
                            {
                                        'source_monitor': 9324896,
                                        'source_nw_x_pixel': -3791333345462738884,
                                        'source_nw_y_pixel': -8104767803791208898,
                                        'source_pixel_width': -9003688608134583348,
                                        'source_pixel_height': -2945050550381365939,
                                        'rotation': -7797732440563543876,
                                        'virtual_nw_x_pixel': 1338732553,
                                        'virtual_nw_y_pixel': 246991029,
                                        'virtual_width': 508725829,
                                        'virtual_height': 290744453,
                                    },
                            {
                                        'source_monitor': 6909427,
                                        'source_nw_x_pixel': -2459656741743502201,
                                        'source_nw_y_pixel': -296559454881852658,
                                        'source_pixel_width': -3057192254768468622,
                                        'source_pixel_height': -3904775536172611645,
                                        'rotation': -3981541788729694449,
                                        'virtual_nw_x_pixel': 1248020191,
                                        'virtual_nw_y_pixel': -1589290155,
                                        'virtual_width': -627041449,
                                        'virtual_height': -31228238,
                                    },
                            {
                                        'source_monitor': 4261474,
                                        'source_nw_x_pixel': -3950858597569962165,
                                        'source_nw_y_pixel': -6309214870605815136,
                                        'source_pixel_width': -8065860715638865048,
                                        'source_pixel_height': -6569107369470841908,
                                        'rotation': -5867402266666954538,
                                        'virtual_nw_x_pixel': 1051520120,
                                        'virtual_nw_y_pixel': 1270802711,
                                        'virtual_width': 765702329,
                                        'virtual_height': 1866009296,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': -918005,

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
            'request_id': 6180918,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 8455570,

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
            '$': 'hóƓϸŚĉɢåƴͿϛĄϻϽ˖\x8dĶ˝ѻԐ\x9bƞǠŜԃͳðϽƬ\x81',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -745550349361505535,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 32511.330577073764,
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
            '$': '20210910:162219.095328:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ͼƐ\x87ɕµʥćĢtʝιưʶŃƊʟÕύİǢАʐβǷˊǂ¼ЂȜɬ',
                'ιϩrιҾƿӏ;ҥаȻmɆҁʻ˛,ƣȤʍˢĿÉ\x94ĸ˹ĪĈʢʶ',
                'Ĵ\x82ʡλΞŶǬʋʷǻǻɽѮőŀԌ˛δJïÀɐνɸÄӉԬɟÑq',
                'ү\x83ҌǀĊŲΈш҆ѬӠμƳˊϒŜ\x94Û]cө¡ˈӴʽ±ʋǾͻΚ',
                'ԫʤόĤòΣӔηǆƛ%ϡΎїθ¸ɮǐɫҎΆȥӏЗɶ$ÈΔЮÏ',
                'ÝĸřҳҎҷŴȖɀӣˍІÛɐ˂wкҾʟϑԎËϣÉТȷǱ*ʒʷ',
                '¾˕ӄ=ǆӶŃұӆʭЅ\x86ȑѕҳЯйϽʷēʣϥӚпʉÝȗƯӻġ',
                'ԬȰė§ěÁҠѽ˖+ş%WˇĕȵǞıұoʴѵȒΪ˜ÐΜÈ˱ɇ',
                'ΪХȝԧӟюȇѽԎǖ˜ӂϗӕĪÚÿšǌÞŭʞʉÚҸǵɼƌЯΜ',
                '˽ӹǅʔǂAMʏRĞ)\x9a˳ԝĞǷӟǏĨȫdȎј҇ҫυҞǐԩɔ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                7201448802061777448,
                4484937611815421391,
                -6359348244105015317,
                2775461973769811242,
                -3462038487940592727,
                -9067248920973734899,
                1421777455651066085,
                5337472514257335931,
                -7021355283030954906,
                6962979227952411990,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                -68800.2034461814,
                209265.54113709996,
                373240.15053526394,
                94739.80500120478,
                204616.99467784417,
                80016.15937402204,
                472032.6381000206,
                -69393.71694923285,
                -97038.97585520646,
                574969.4828177509,
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
                False,
                True,
                True,
                True,
                False,
                True,
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
                '20210910:162220.191906:+0000',
                '20210910:162220.209123:+0000',
                '20210910:162220.226953:+0000',
                '20210910:162220.249592:+0000',
                '20210910:162220.270344:+0000',
                '20210910:162220.291721:+0000',
                '20210910:162220.318878:+0000',
                '20210910:162220.343671:+0000',
                '20210910:162220.360995:+0000',
                '20210910:162220.377802:+0000',
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
            'name': 'Ɗ;Ėʀä˔iҼȤѪ5ʤӃÀɳӂ\x97Ŋ¼õқ$ˎұԢΌʽȝҙ¢',
            'value': {
                '^': 'bool_list',
                '$': [
                    False,
                    False,
                    False,
                    True,
                    True,
                    False,
                    True,
                    False,
                    False,
                    True,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ˠ',

            'value': {
                '^': 'int_list',
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
            'catalog': 'ԢǍǷȒƆπ»іҠÆʴʞҦγȘɘͲȳƀ\u038dȝơɟѱƎȥœѤ7)',
            'message': '˞\x81ϥÝȼǙ\x96ăĢҥ=ȣҊӊzȀȚ¼ʦьѿӓԭΟyǝʼОʱ˾',
            'arguments': [
                {
                    'name': 'ĵӇÃ\x90',
                    'value': {
                            '^': 'string',
                            '$': 'ΨȻЩƥ˹ȗҎıƦZΊʝǳϹӓҢļԭħќѯӯɑҔОЩBŶΩμ',
                        },
                },
                {
                    'name': 'ʋ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ȏϞоŴǮ˳є?ʵȄƻ-ӧµǮΰĂ͵ѮǢӗȆ{µŻҘҥ;ȳҏ',
                                        'ɰβƛpԘǁȸ6ȽљĕәӪȭƽŗÃѧӶɌΪÑȝȒӝMǑŁʚ\u038b',
                                        '>ģʴӜAӆʱѷŗчιѲkƳ\x8dǖʾɞј`\u0382ә϶¢VΛŇ\x87ϴˍ',
                                        ';˧ƨ§θɇΉń΄ǃʲҬԆ˥әѦԒȾX˧\x98ϙˠΨͿΈʙ ҝˏ',
                                        'ŶđÍ¨ϾҙжӨOʈGÁϒĬѧǈѭ\u0378Þůǌδğѣʛu:Ή˅Ш',
                                        'Ǧη\x87͵ŀԊХǽĪǥƉΕԢӤ-ѡ;ӎ\x85ʑΤʚҀϬʡԎdη\x88ÿ',
                                        'ͳ@ʱƻŦɑӍĕĒɁˣ-ȉĚП\u0382\x87·ω˙ӸԑĢǙĘќћ˞ӎȀ',
                                        '˱ϓdτµǓěѢkԮяłҌ\x93ƠϣǋR\x7f1īȌСɴϰУϳΏĽѭ',
                                        'ɅӮӹˎʜʢʊÀΞ-ЄҗюUŧϑŬô\x84ɫ©πԌŒƣ¬ǲ˵ѰҪ',
                                        'ÐsЦӖđCυ]ԎΎ«ȱžđΫ\x8bvQёњҖɻЍ\x97ϓˎˀXЄĔ',
                                    ],
                        },
                },
                {
                    'name': 'Νg˯˩ȽԅѢ',
                    'value': {
                            '^': 'float',
                            '$': 401299.55856311147,
                        },
                },
                {
                    'name': 'ąÔǶ!è\u0378Ȭ˵ʋԁêɔɃȥйɔӎįӁѣƖʵƐɠʼɅҽòҀӔ',
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
                                        False,
                                        True,
                                    ],
                        },
                },
                {
                    'name': 'Ͻøϳʌŏ\x91Ԇɰ1ûѮǄŰЋѦαŝѥ΄ǶϞ*ȃʞ҇àζ΅Ȕѩ',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        3302805773226011492,
                                        -9016914517815350463,
                                        5182904870869315171,
                                        -6862671161977984303,
                                        -3192673732713698319,
                                        -479273526499221991,
                                        4984777839636622616,
                                        -7773574737531518411,
                                        6974354544671195448,
                                        1546478302103084823,
                                    ],
                        },
                },
                {
                    'name': 'Ҟ˘оɕԖьȵ\x90иƫÔ÷ö0',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'AԊƬԥȺ9ĤȮuеŴӔ˖ж˃ʺ!ѩѐӾǫǷȾʙ˧?µȪʁͻ',
                                        'ɤƋҲ4Ɗ³ǯȜɍŏǺŉΕȇϡΤԅυŕʱ˦˗ӑɧҶɭԬζŞ\x90',
                                        'ƀπԡϰ˔9Θ°ƭɳþԬќƿԒÕĺġϧ0ȷȖ\x99ԃƬǵėĲĿӝ',
                                        'ĶɘӛĊêȰΖԞȜ¨ƪÀì\\aʖŊtԟμǣø˅ˬĒЄҺ˚Č&',
                                        'ӝѪѐɕŲ×ēǩěȪӤˏьшЯɱ9ĩɔɭϘȴǕP˼ǧԡʜϣƈ',
                                        'ΓˌȼаőкҍǷԚȞмϲԬͷ˭õʇϯȨΎљȺđſϸ×İЇӒʀ',
                                        'ԅŽңԪѝ\x9aӬҶΩȼƌαΔŵkΪĶȜÓɁӇίЭɑ"ƭԣÑҶɷ',
                                    ],
                        },
                },
                {
                    'name': 'ȠɳБǬӼΑӜƅEȇŃă1ƿ˼ŹȆ·Ń˔Ҫӈѿ҂ΰnʪ{ˁʄ',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        True,
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
                    'name': 'øѫϓԀј\x92żЄѝöΕqТʺĂˆõ҂',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210910:162218.066603:+0000',
                                        '20210910:162218.095551:+0000',
                                        '20210910:162218.118322:+0000',
                                        '20210910:162218.139018:+0000',
                                        '20210910:162218.160368:+0000',
                                        '20210910:162218.181760:+0000',
                                        '20210910:162218.199323:+0000',
                                        '20210910:162218.217041:+0000',
                                        '20210910:162218.235386:+0000',
                                        '20210910:162218.252308:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ĺúЊÉԟђҪѪǠҺĳΞɵČÞοƯ',
                    'value': {
                            '^': 'datetime',
                            '$': '20210910:162218.340067:+0000',
                        },
                },
                {
                    'name': 'ѳгϽ\x80ťǷЭǠHӭ˷οӊS:ɰ\x8cѹӴϊ3ǟӍϚū«ʮй',
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

            'catalog': 'βю',

            'message': 'ë',

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
            'identifier': 'ȼҵq\xa0ĚҧҤʎƖ¥ǳȄΞʱĨ8ԂɜÓ\x8e9ʢƾҾȻʘϨЁȊҚ',
            'categories': [
                'network',
                'file',
                'network',
                'file',
                'internal',
                'invalid-user-action',
                'configuration',
                'internal',
                'network',
                'internal',
            ],
            'source': '|ϕžŲҖơ\u0380Μýƫɉɬʃ\x82їԥԌȧ\x81¼\u0380ƽÞ\x80àȝӎɧ\x81˾',
            'messages': [
                {
                    'catalog': 'ϽþÿǼѺʷԂΒɨƗѽǇԄƆƙŲҼе˯ʧŪҹԅԌʉLȸƗ˔é',
                    'message': 'ԕΊΓԎüȌǦҟǑƱFǣĴ§ȽrʑƣnċϐǱ\x97ëӞͻųϯǔȈ',
                    'arguments': [
                            {
                                        'name': 'ѪƾΗӪĺìƾЫʦθʂɢEҩeДWÁӻӱʭ˜NԄĞɱͶȺϽī',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            713003.4455184755,
                                                                            650515.3216033004,
                                                                            991431.6717048953,
                                                                            48822.12532574861,
                                                                            291921.58964734786,
                                                                            -84625.67659720025,
                                                                            -8983.182928243506,
                                                                            41554.081086529535,
                                                                            -27019.01758685468,
                                                                            531794.3192236598,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƑɃļ\u0381ԭǇƂԫlɅǏʃУӹΡ҂ȴAεӐ¸ȣщǓDÚϸΫӟȾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162201.031601:+0000',
                                                                            '20210910:162201.055874:+0000',
                                                                            '20210910:162201.075660:+0000',
                                                                            '20210910:162201.093022:+0000',
                                                                            '20210910:162201.109972:+0000',
                                                                            '20210910:162201.127565:+0000',
                                                                            '20210910:162201.145330:+0000',
                                                                            '20210910:162201.163228:+0000',
                                                                            '20210910:162201.180428:+0000',
                                                                            '20210910:162201.197845:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĬɲϠɹϑˤĪǑԎŔ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 6576066739619151653,
                                                    },
                                    },
                            {
                                        'name': '҈ΌĤҶ·ƨѽϴȁķʓȱϿ¼я7ƙĉǇŐĮȳɀУӰ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162201.365674:+0000',
                                                    },
                                    },
                            {
                                        'name': 'êѠǐϻϧ\x94\x85*ǘɯ\x93ѶѤɎĪ҃ ßϒĮ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1917987423183488623,
                                                                            6607695799127856780,
                                                                            8648292714704987612,
                                                                            7625237151196680490,
                                                                            -3466040594288253,
                                                                            -4099519396922434057,
                                                                            7200491099389775254,
                                                                            -7255188487367703686,
                                                                            8726023410643038540,
                                                                            2318220035690438662,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҼƃʇӲҮɎғѬϨşȱøǬ\x86ӟŖɍǭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'өɇϋΣɭǬƺФџѼΉ/Һh˼ĬËʁɽ7',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
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
                                        'name': 'ΣǩóӃĥГ\x9aŤÄʂҽǖIˣĠĀѧƕƷȵȽѪfʦӚÿîϣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7979841697737015000,
                                                                            -7087668423553430281,
                                                                            6316596376266294689,
                                                                            7661579718535366903,
                                                                            -5908042403046004132,
                                                                            5562367141929003714,
                                                                            -6915481593306400882,
                                                                            -5532168463374894348,
                                                                            -9015861312589119281,
                                                                            -7563530873086634869,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǅЯʡİЖĕǌҸȗtрȞęǷĤǚÿɾӦϺΠ˅ǰɐ҂ưѤǃġ´',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162202.317856:+0000',
                                                    },
                                    },
                            {
                                        'name': 'βȺɓƲ¨&\x82Ϥʯѿǵ˶ЋЮɳɷϡĖʬÑЪσʽ˜ήźҋɜƸÆ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɷűҥȧ˻ӊƺȳČʍΌТԭюҒȹűÅƪ>ӬΏĚǼ÷\xadњОȤª',
                    'message': 'Ȝ˥ȫҏǱўʼöƊʺŤȕГƶȭsӛĿҋЉԍƺĠƴѲԦɢǪγΤ',
                    'arguments': [
                            {
                                        'name': 'GӸȻĢГ˪Ӫ5',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԖʀȠŸϱƬĴʻ\x90\x81ϛǨɸeΙZԆʀ?\x86.Ϛ˹ÞʍŶϖӎƂ˸',
                                                    },
                                    },
                            {
                                        'name': 'ˊYʘȝ˦ý',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            382364.27242462436,
                                                                            501561.1228379054,
                                                                            378507.9305992668,
                                                                            545921.5244592676,
                                                                            449419.30790676235,
                                                                            756159.0742725433,
                                                                            108952.56278245672,
                                                                            84917.61600926152,
                                                                            722405.3738204403,
                                                                            659419.0034883469,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x92',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162203.099175:+0000',
                                                                            '20210910:162203.120186:+0000',
                                                                            '20210910:162203.140709:+0000',
                                                                            '20210910:162203.161730:+0000',
                                                                            '20210910:162203.182832:+0000',
                                                                            '20210910:162203.203874:+0000',
                                                                            '20210910:162203.231094:+0000',
                                                                            '20210910:162203.253348:+0000',
                                                                            '20210910:162203.271528:+0000',
                                                                            '20210910:162203.289087:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӷɂϿ~бϠɃǦŎɉǐčȳ\x9cӦ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            145918.91519143287,
                                                                            570056.2192502626,
                                                                            750662.9504681238,
                                                                            714444.6826936333,
                                                                            538042.2474479143,
                                                                            278766.8361032369,
                                                                            147785.18238254037,
                                                                            828359.8677481974,
                                                                            780155.4386349111,
                                                                            269213.6685049917,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɞȹӨĞɡEˑηŌəi˭˹îӲƚ\x8fʑlĺΓΰ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 627326.3082009036,
                                                    },
                                    },
                            {
                                        'name': 'ôэѶǨŀ΄ƺԔǮʴ˞К\x82ς϶ʘ¿ȚÉąӈțϻϔϖё²ɒРΏ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7657828411610672821,
                                                                            5065518911707401244,
                                                                            4152145923829914726,
                                                                            -485824916466719027,
                                                                            -3590358184736849772,
                                                                            -193674883152682427,
                                                                            2124776941898758092,
                                                                            4566957887233880997,
                                                                            -6979712346772646795,
                                                                            6687134992424820793,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƫҢţ\x92ɼԝζÐȃԑӐ\x8fǡ,ӉQˑ\x92тѠ²ȠŅӡϋΐӉύϦʱ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҇ƪҺѳİΙρԡҮВϪäϕɇϛ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϗѫ2ʕѮχӜϪБ\x9bĨ\x88ÁʣãĚčϴҭɜΕʈѾ\x86ŰӱšΞŕӎ',
                                                                            'ͺȭɶļĥҔi\x9c£ӘͶΔϸĲĉȶ˰ӊȞіұǹ҉ɩʮŐW¾іԘ',
                                                                            '¸«ѬÜҫ|ӱ˲ӍƚķȬʟΟɜӗKʹϙϷȝѤĩӧŧɂpǏіϿ',
                                                                            'ǊːȓȣŖŢÍѽʫσͶɿñӪ\xadҙêȴHӜȽԖˊ5ĺKɡȀϷ~',
                                                                            'җʎđıǜɼϝȄһ\u0379ӵӘrĬĉԈ\x9b¡\x841өĎҫʇԢ°xԟѣ,',
                                                                            'ѓέƍsŸÓԭίхΗѶýΠʫёΟ\x98˶җ\x9fʂʮҿаϤԪʣÀїΈ',
                                                                            'æĴʒĵÚǼлĥǄˢʴɪԝŏ˻ԪςƠYζƍѮШҽɣNʰŔҋЈ',
                                                                            '˳ȚѐƄȳíñǼ¸Ƌ˄Ͷ¸ӚӚ\x87ʓ\u0378ȿʦѱҍγƂĚ\x81иҩŖǍ',
                                                                            'ЙȎҳ¿.ǱǩȨίǿ\x92Θ(ИσƼɔЅåȕԘȔõʦĸÉӼơĪϧ',
                                                                            '˝rɂSĐьǟň-ƺƃЩɜċɨΓ˾зȐŁ˝ЧҟҐǶŅӱѷİД',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ãϪԦԡȐǧĒǛƁǡýŨǠԃо˅ˢӬӬŊ5ǱТӖѻ»\x93\u0383½Ӵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162204.423141:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʔøκƻҪ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6373842802520179846,
                                                                            6362444970982016058,
                                                                            8241489037685086493,
                                                                            -2443962346056370178,
                                                                            -8009776621235985971,
                                                                            5015626344851937097,
                                                                            8163046223270000769,
                                                                            -6016252445352853455,
                                                                            -4153771821090935910,
                                                                            119649318078179735,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӌ˱ιȒ×eƗǙĤ˥φͲƅŌȒ¸΅ҰŵŮǬ҇ŊӖĂǚ;ǘqÚ',
                    'message': '˼ȪώċĒōŊĺȷÿȭTΉ˻ӮȷÅЍҍɤəɽoɩǵϗŒΥǁԗ',
                    'arguments': [
                            {
                                        'name': 'ί',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x7fˌӑƟĬıĀRұǕƾϰŲːʋҽҔӄтѹΔθȠ˒ɱŊФǥѾƢ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': "ԭķ\u0380˧nϐԘǑѣ\x81њɕ\x8bŬСЧΖϚӝfɽʯƽ÷qѬýԒ'Ś",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2930050346006853921,
                                                    },
                                    },
                            {
                                        'name': 'ĳͻԌɵԛɺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '\x86E\u0378àʕфϿҧ\x90ΣǍϯҢǨҾĻŌƴƕHөȍȓÓęm',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8373113921377553422,
                                                    },
                                    },
                            {
                                        'name': 'ƓϤƮб&ǌϤǲÁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -409969122962629040,
                                                                            -8073702153638185221,
                                                                            6680567669427184710,
                                                                            5892541338657163583,
                                                                            -7584583619013287501,
                                                                            -6482554974937635871,
                                                                            -1663096583862661395,
                                                                            -5080146006493423986,
                                                                            -5668429980582494456,
                                                                            -4843429836389087145,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǝœΈЛńȢȮȠȼӧȳх·ʯȮЯϪǱʴԨ\x96ӣĜZ˼rĜ8ŗϼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƎɬŔȏũҹ҉ŭӨӔĦ\x86ϛӞmҡĒҐѹjΚƛƮϤ͵ҔѬΛÌӗ',
                                                    },
                                    },
                            {
                                        'name': '¾ǼԤҨИҪҤĚ\u0379ҰϘĮǬѥұ˷ĵΜ\xa0њƼʐ\x9bЂƁĺ\x96¥ȉ1',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҊѓŌƧӾͿɇӡηςԚӵʴɗгŖʺȓВƸɽΥѐЂɸÁƯʵɍe',
                                                    },
                                    },
                            {
                                        'name': 'Ӫ˟ɺ¶ɶȺЧБǠǢЗɴǼƽЯÒ˻ǆêȂƎёɧӖ\u0380ŤǫʩǙԛ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5782221521490383057,
                                                    },
                                    },
                            {
                                        'name': 'ӁĄɜϦ\x84ζǋӑӜҚџϷ3ӴΕwʝԈБ¼ЄДГǵ#ŰϙͰӹϴ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'қ\x8eђǽȪʈϿêԁѸīϜƨҿǽ\x99ԨŽҁŶ ԎˌʗѪ˺!˫\u038bŘ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ɘȝԥȓғҌãџϽ˸ɚƾ\xadʄƚ\x90Ω_\xa0УԆɀˮӐѪƒ/ƪ[Ŀ',
                    'message': 'ʥʁԨɉŹĻӟӛÆħŷɷr\u0380ɰӋȔȴГˏòĴƭ˙Ĭŗĥǻȡч',
                    'arguments': [
                            {
                                        'name': 'ļ(ɌƆψ/ғЍ°ƾȵb\x9cͻϑʦŀԡЯɁϔªӧǙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7082108865698187469,
                                                                            6461955059384029347,
                                                                            3085135448042574485,
                                                                            -2594130796060168970,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЯƛӸĤŸ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3503251620206232618,
                                                    },
                                    },
                            {
                                        'name': "ñȶ'ьԋϏǐˇȨ˞ΉĥϞ\x98šȍǜчЁыˆ^\x83Œǧȴƃ˕ů\u0383",
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '˒ƫǊ\x87ʜ°çԉӝҰiȞԕʅƧϯÓϐώɠйǮάęΉǌȾAңѹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'ҙ΄јĴԖųѳâɭɐ\x95ǆԓєΎȘ§ĒǥŬ\x9eЁκȖGǜȳҤ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 861810.0549449595,
                                                    },
                                    },
                            {
                                        'name': '\x7fɴ\x9fNԢ\x81ǀЭː9ǅΌ½ϸ7Ĵˡӛ˙ҲæǗяȯȀƐŨʲѳǬ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ϫϮӃȫпɖönÍöӷ˂Ͽ%џДäҀ/ĿūÂϟьΎųтȁʾҭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162206.676397:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ķ\x94Ӌʙ϶ӣūеϙʤȹǢn˱ҸÛ4Ў',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1613734783267190858,
                                                    },
                                    },
                            {
                                        'name': 'ТƫƁ6ԁȸ=Ǧʌǽԙԝ҉ӎAӾӫƧuϒӘĢģҊ·˜ÈB\u0380ȡ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ǇϯϘ\x81ҮɲǩĨɚ2Ⱥ\x8eǌƤŕȻ°ϭʾȻǅоƸӳӓϙ4ȟÑ˔',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ӫŅɮʂҥjΧĪʬžĔ˙ɘѝРť?ɂĒҮǝjӻ5ӲϠӟϬʋƱ',
                    'message': 'ȕĜǃÇƬøɔɖʺȶԣΆŞԐƀ|¶ΦΏ\x85ĽɄǜ϶șӳϿʲáх',
                    'arguments': [
                            {
                                        'name': 'ɩǥðҥyɊ}ÿȝã˚ǍĩϗġZӫϙӪҬˋ;ʎǧĉŻΪԫŜˠ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ЃӚ¾Ǎ҉\x95ɖ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162207.118506:+0000',
                                                                            '20210910:162207.135871:+0000',
                                                                            '20210910:162207.152750:+0000',
                                                                            '20210910:162207.170048:+0000',
                                                                            '20210910:162207.187988:+0000',
                                                                            '20210910:162207.205784:+0000',
                                                                            '20210910:162207.223433:+0000',
                                                                            '20210910:162207.241546:+0000',
                                                                            '20210910:162207.259169:+0000',
                                                                            '20210910:162207.276536:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˺ȼԆíµǹʮƟʷ˹ҶȖũŅˊѥ˝ӺȠǇƅʧԭüə˷Ĥɤȗ±',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            284795.0283907006,
                                                                            14039.502399214383,
                                                                            765781.4638858165,
                                                                            796222.312069525,
                                                                            888008.6824444929,
                                                                            697296.5654671867,
                                                                            224603.03234883305,
                                                                            942143.8915026288,
                                                                            96881.44329368678,
                                                                            345605.3290902393,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҕK>˒ˢϝƆ҄ɭƈƂAЁļ÷ĲҩʭŨхόǦѮĮзԈǰhˡś',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɪͽ=κáǍųŋԒÇ{УɼӚū2ύɳЭŭǅēɃɜˣŞɰԧǎ^',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            142866.78142096964,
                                                                            -77924.00082403368,
                                                                            186415.75824106619,
                                                                            603825.6619168227,
                                                                            831048.3269175399,
                                                                            210038.9728432694,
                                                                            -80491.21403383603,
                                                                            763908.9723413493,
                                                                            745888.511737214,
                                                                            764687.2032000406,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϸӪΥ˛Ðü\x89Ҕ\x96ȥĘА£ģˑȧμɅӏϿŦΝː',
                    'message': 'ɄԀιNͶЫ¯ηӫң§ҔάħҿÝiϹȑҽҌĈ}ɇȤ¸\u03a2WԂɖ',
                    'arguments': [
                            {
                                        'name': 'ȥΫԂϵР',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            416887.18510259513,
                                                                            300805.88490652747,
                                                                            220289.082137028,
                                                                            137217.73170317395,
                                                                            532984.9169920299,
                                                                            607745.6539827156,
                                                                            286915.2664210311,
                                                                            618810.1504041507,
                                                                            543122.3234664534,
                                                                            960819.2011908046,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ό˭OȎɹiȌ˗ɯвÁŽƠҮɏʌҩѥ\u0382ˉêŇʆЉϛȏȸĹ}ũ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǨƶʃĝÅČȭ˓яȞ6ϺĖȭΝϼlΤџːȠϒѴԫґ˴ǻƼŖǄ',
                                                                            '?ɖ@ЦɸϣɡɋίƄEˆрϴòҤǺɦ˛δƛɖȮ˰ʂbʌ\x90\x96Ԉ',
                                                                            'ȩƙϳSЬϳвñzԇǠśǌŘoȚĈҋӧȕΈȰȻτɿѼѼӞ4ȅ',
                                                                            'Ӵӡé¥С\x88ǑЋ\x93ʂԛP¸ϕńȱǬҋƘʿԬ˭ԣ#ӥ§ӡ¾ċǄ',
                                                                            'ԃήƥӲ\x9e˂8\x97Ψ)ȘԔɩӬЖȠΫɓѥȽƆȑɢ;řѝ˂Іxù',
                                                                            'ɩ\x8dìʢŝƦđ˼eƦұ҈ƕʦpƸ\u03a2ԮѨĹӯЎHȴжҹȷͷϰӼ',
                                                                            'ÌĲ҃ªĬв-ѫѺѽɮʻЛɢΆЇáYЊӉƞɀ¦ɫлӖг2҅ǿ',
                                                                            'ԋƕƱ«ќӶЪҢĢ6\x97Ķȿη^²RӜҿ¥˧ƺƜГԐЭȯäćԙ',
                                                                            'ĥsįѓЧη\x82ρƴǥʫǧ\u0379ѭ҆ńҍԘɤʫ\x82\x82ȣ˞ÁźɾԬʘʌ',
                                                                            'ҦƯҹ[ѳșťȇ˩ɴӊ\x82m҆ĢѲÒϵGҤƇ˭ˇҏɼ\x8cÑ"ԥƁ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҴŎʀȺĀǢĈκʁ˖×ԗ˔´ҫΊάǜчЌɴǛ]ҫɲ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162208.599800:+0000',
                                                                            '20210910:162208.616874:+0000',
                                                                            '20210910:162208.633806:+0000',
                                                                            '20210910:162208.650908:+0000',
                                                                            '20210910:162208.668689:+0000',
                                                                            '20210910:162208.686409:+0000',
                                                                            '20210910:162208.704585:+0000',
                                                                            '20210910:162208.729510:+0000',
                                                                            '20210910:162208.752804:+0000',
                                                                            '20210910:162208.772816:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӢԏΒЛŮBъö\x89ËǤÞļȯsƽΎɐ˳ңśӺѹŶƝʊǔ˛āĹ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'õǬҡº˭ԥUԦˣ˜ËǾҼɛĠ}ŪȎšӖӉШĭjȋɹіǩШɸ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162209.126070:+0000',
                                                                            '20210910:162209.145492:+0000',
                                                                            '20210910:162209.163010:+0000',
                                                                            '20210910:162209.180154:+0000',
                                                                            '20210910:162209.197031:+0000',
                                                                            '20210910:162209.214286:+0000',
                                                                            '20210910:162209.231651:+0000',
                                                                            '20210910:162209.249322:+0000',
                                                                            '20210910:162209.270662:+0000',
                                                                            '20210910:162209.294491:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x9cѿѠ,ȏƈ&ƞMɖóҐІоδŚ{\x88ʠφ˃ɮIϴ%ɓѵΫɏʶ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            773222.6532932096,
                                                                            632474.5090707258,
                                                                            465597.7919040177,
                                                                            337757.51760279975,
                                                                            519829.30400965095,
                                                                            241940.64600517135,
                                                                            608852.7117810744,
                                                                            490924.72426348727,
                                                                            33657.03318938179,
                                                                            951753.2097889937,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'UƯ\u0380ȓӽΞÝɬɤ˴ѫзҘѠʭͷ˄eɣӁĈʌ˘¿˩ņċ\x98Ɔғ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162209.668870:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĳԁ*©ŜƼȯ˨7˴˔\x95ƽǉȒӽҤҵĪ҂ϳųƂǽτηɇʚĭѯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'đϙťǇѼӄÒӵШŊĻˡιĴήˎǀϜʕƿɱԋʼΓΊĝɍɭрó',
                                                    },
                                    },
                            {
                                        'name': 'ҨƳϰĝɖƃƀʸÜƮɞʧԎÊʵÔҀH¡ƛŢ ɤ°ыʌʱϐĢƓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ūĸ°ˏоӮĶĥѥ!ŨȊ\xadіȟćƼśˋΠʻμΧҁӫɢƻёýԩ',
                                                    },
                                    },
                            {
                                        'name': 'ѭϏыϘ\x88˳ӳ҂ԊɷtƱƋɯͷ}ġEʅԫɰʒˎAëʄ|ʻάѺ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǭԘàьŃ˟ԊĐĕʳȡкĚіĽĊʍϴƿѰϑ\x9aƵϫ҅ĈiĪPɪ',
                    'message': '6ŦҳxċˇΟІǞ˥Ë=ȼůџVπԬȤЬţ϶ʅ=˶ñNήΛа',
                    'arguments': [
                            {
                                        'name': 'ɑ/ƿȯϽʰідюȝΩѐѠˍжȚʵ\u0378ƇȄϰˇəуϘаɴƪ˄Ĳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            829136.0099535407,
                                                                            -49096.686105120265,
                                                                            900995.127452051,
                                                                            315605.952780583,
                                                                            261199.36698956438,
                                                                            498012.839655456,
                                                                            75883.63962852681,
                                                                            334917.62965549604,
                                                                            561081.0787516913,
                                                                            808904.1400530289,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˆрЊԍĭǅЬ¿мǽķЕРʡĘ˽ôʋг?ϣʹђӟĿύ˄ҡмυ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162210.554433:+0000',
                                                                            '20210910:162210.573701:+0000',
                                                                            '20210910:162210.600228:+0000',
                                                                            '20210910:162210.620602:+0000',
                                                                            '20210910:162210.648181:+0000',
                                                                            '20210910:162210.672569:+0000',
                                                                            '20210910:162210.689740:+0000',
                                                                            '20210910:162210.706531:+0000',
                                                                            '20210910:162210.724682:+0000',
                                                                            '20210910:162210.742493:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŞűɜçïЙӼě\x8fїƲǒðҹЯ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162210.831344:+0000',
                                                                            '20210910:162210.848690:+0000',
                                                                            '20210910:162210.866027:+0000',
                                                                            '20210910:162210.882935:+0000',
                                                                            '20210910:162210.899790:+0000',
                                                                            '20210910:162210.923270:+0000',
                                                                            '20210910:162210.943076:+0000',
                                                                            '20210910:162210.961198:+0000',
                                                                            '20210910:162210.979936:+0000',
                                                                            '20210910:162210.998185:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Żɨ²ĒɻƢ\x9bʄȺő\x95Ԡѩ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "Á|ɋȧϚΨϐњĘ'Ѝ˙ƭΥɎяʬґʖȿVǝɖĉˌȩѦϘˠҞ",
                                                                            '\x90ȧùӆǢӷǆ\x86Ý°ϵΥȥĠɝɺæЎˉĬԥŴ˞\u038dʄOБнFm',
                                                                            'ŴCӞҒԦԈ\x95ǸЄ˅ӝͻńčĞ\xadɤɳýƍ\\lԖťЅҞń˜Ї˅',
                                                                            'ӧʄ3жŷ\x95ğɀΦʖдČȮëǏĐʈԧԎ{ЁӽŭˀύӮҡ{ǁƭ',
                                                                            'ŐʚǳӨĉɔȚћԋЧ˙®ǤҒżѓђɜŔҳ\u0379ТŕњþǔǮГ(Ε',
                                                                            'ʰЍԟϻ-ҲɨФӔϪō˚ϲYǝнŎǞό9ŋҔˉҒ\x94ǭë\xad+±',
                                                                            'ƙŨÎ5Іҫğšҿę\u038dǖķԦ¸˖µÖΪ˭ϣÎР˨ƳЙɍΟ¹φ',
                                                                            'Ν˻ӻàɉƢ˛ʹĶԊӦʔ©ǚŞàlҤпȻȫŜ2ƺϝ8\x9eÖĜө',
                                                                            'ÁǬŭ^%ϮǒʻɪͼϮƍï˛*ħҗvеɦƌƃŀũˉӉ\x80Ƞ˞ζ',
                                                                            'ơȷӌϳˣø]Їъҁɠϼ\x82ˤ?θвƶʼ˔ƤʊĂєң¥ʻð?\x8d',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԢεĖǓёɱ\x93&Ӷ˺έªǂϔʭӉDůȩӵfҫʦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˯˹΄ӥϯɶȢˁfȒĵŵλԠԞĸ«´!ŐU΅Ӎ\x93ȗΰӎӄ\x96ƣ',
                                                    },
                                    },
                            {
                                        'name': 'Ωӝ´ʄҮЯŘǘʶǥŜӈìǞѽʍǮʶÄҜҢ˔ΥƬΝӡƛЅˇ҅',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ŊԘźŖȝ\x85ŬеOŎ\x9aGˉtԖƃŒƞñοҐŖӧҥ¥ç|Ȥ\x99Ζ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162211.515728:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ҹǎ˽ΡĵŸ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ȺЖıͼԋÔМĦӧ˪ğ,ҚцȐҳguϬͿõ\x80άǘЊŀʕ˛˙ˇ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162211.669084:+0000',
                                                                            '20210910:162211.685986:+0000',
                                                                            '20210910:162211.704238:+0000',
                                                                            '20210910:162211.721614:+0000',
                                                                            '20210910:162211.739010:+0000',
                                                                            '20210910:162211.764158:+0000',
                                                                            '20210910:162211.789069:+0000',
                                                                            '20210910:162211.805793:+0000',
                                                                            '20210910:162211.826809:+0000',
                                                                            '20210910:162211.843948:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƙė˚ʠ²ѹfëӻԆ҅ӷ˛҂{ЫɌΩƹ\x98ăz6\x99¿OʮǕƈҴ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 602950.8053650602,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ą\x9a$еͻʲˋĉƂǑŮ~ϞƸEȢ҅ҝЋЅGɿ˦ѕŚÛϑͰȌq',
                    'message': 'γΰӶ˹ʯіúɩ.˯íΫ˧ÞΖż\x8dϱƫa\u038dѯϾϤ1ɩ4ĲΔˣ',
                    'arguments': [
                            {
                                        'name': 'ѫĔúŤœʳтȶƒϰŚíʰҸƣ\x88ŤƢˇxʙϼӗK-ɳèɎ\x92ģ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162212.085772:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ύɺĎɹʒāǏԨ˦ӳεæҴńЇˆʅӮIȭĸїԒҿˊƧ¤Ҙǃ\x8b',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ъſˤƢÎ´UZӅҕ˕Ԣ˼£:ҰȒκĈȢȆɓʐ˒ǞȘŚϫΤҤ',
                                                                            'ЋӼ\x97Ũэ4ɼӨ\x90=ÉōTʴϿǨŵ-ȅԣƓξÔЭҗń˨Ѷİʏ',
                                                                            '\x95΅\u0381ȝӋǦaҷƬáЇʾȐ˧ЧȾɏͽĮZɏɥċÃƈ®ǋZúӅ',
                                                                            "ν\x96\x84vѰʃȕҊğŠYмԥˌƥxΊԌĄԝ'ʓҁŤǉ¡ȎÉͱh",
                                                                            'ӄϼɃMԁÅʇȸΓɰŏƞʆӥҳӤφѶ5ԆʟƯԥβԚϊǳŲ&ʆ',
                                                                            "ĳò{ʞӂӉǉŐŸț#ɩàѾ'ǕŤːǶˎПƋfɘ˼ƹ$Πʛх",
                                                                            'ķ҈Ďĉԋ\x96Ƀζ¾Ƽ\x99ԘˡНɟӭjԧɧmҡӉъƠЏĄǠόľԌ',
                                                                            'ʺĩ˪ˆѺĦʮыƐǡŷÝę÷ÏҚϺÿȁ×ΙԀҰƻʱрǋТΪΣ',
                                                                            'ř\x9eϺ5;ǊĮҘKΚ\x81ĿӃӰ\x90ʺ¹ίЏǻȌ˵ΡĭÆтήĺô˓',
                                                                            'ДV´ZʣӺϓϓӻíʎκƅЛԁΌŲʽµfʳǪ΅ȺӬƈ\x81Ɲ˝ȥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԉƈέɗuҥƹО',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǮȒɲ\u0380чѾŘўМâϢÊ˴-ԗΜԦћѯřņӁҹɥĤӂlŃƥԍ',
                                                                            "ȮӄȟѨˠȠɛİҩ5ѨǔȖ'Íͳ!YŴňƥq{°ѵİԧӆӄʠ",
                                                                            "½Ĝҕ\x8eӈχΑόƿѹϽˁԥɉбˋ˩ҠћЌ'ҲѰ\u038bǢÊźŗœӞ",
                                                                            'ҏĿ\x99ԉϫŻʻɶԤҬ\u03a2Ċɚ\x9eΓƓӳМӈԨ¡ȣǝòϗԩщʠš˴',
                                                                            'ЎPȵ\x8bԙӎȮϟӳӓʯҥӈьσϿ˅ɴǟњȩ\x96Ȋ-үŢǣƒǃӤ',
                                                                            'ҰƀɸƎӺçVŏʳŠ\x99˩ΫǱĹą^ƬԩΨԎ҄ńïҠ#ːŞʆȽ',
                                                                            'ƃʢüœԭӽưMҨϼĀʬƘƑȜТŜȣӗрÛВІ×\x87óϞŶ=Љ',
                                                                            'ȧъƴǗѹ\x83ÈőǉµΐǻȢөиϗҤӗɁȚƍτľԡͿĸӹȋǻҥ',
                                                                            'Ҟ҉ʶƜѥġϲƉT˔Ÿ§ˉ[Ńž¢ƄÓХ\xadr3ƵҜҺĘҫǢ"',
                                                                            "ȚσMӳWȱ϶ďĽСͱʔɁʉǉºʿǲ0йƌӒ\x9esфʰʑϸ'ϊ",
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӧ¨ʔĵτȪǹʖЉʡěϝӶɅˏǚǏ¾ԑƧųĎП',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210910:162212.697463:+0000',
                                                                            '20210910:162212.714360:+0000',
                                                                            '20210910:162212.731447:+0000',
                                                                            '20210910:162212.749472:+0000',
                                                                            '20210910:162212.766232:+0000',
                                                                            '20210910:162212.783213:+0000',
                                                                            '20210910:162212.800669:+0000',
                                                                            '20210910:162212.821341:+0000',
                                                                            '20210910:162212.841124:+0000',
                                                                            '20210910:162212.863850:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҮlrμĎȈɈˇδǯÔϣ˸Ō<',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162212.954342:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x8dȪ5˵ʒӾɩƦѩϐϩҕˋ\u0382',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԟԐϼщʉʢ҆ʌɌ¡\u0383Ӎ\xa0ϪҞʖ˥ɪϪΓβ×ҿƽ˜ŷ˕ԟүƪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 102253.91047922213,
                                                    },
                                    },
                            {
                                        'name': 'ӕ\u0380йɕǌȷʟ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ɯ¤Ï˩Ҫȓʗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 764526.8297562394,
                                                    },
                                    },
                            {
                                        'name': 'ҲԀ¯ϗϬƈΝǝΓőɐń}\x8fϣˍѵĺ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΏÔʟӏӛƈǫʜŌļ]±ÊҸȖɬϔƶяЅ˓сЖʠԩ˜ӳεY,',
                    'message': 'зҶOƶ˘\u0382ƧȪːkøƟԙʙĞÞǏ\x8eЯԘϵԓÞȺˏ\x84Įɑыő',
                    'arguments': [
                            {
                                        'name': 'ʡĮ9ǐǈɩ3ӏ͵ωřȻ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 494160.9317283336,
                                                    },
                                    },
                            {
                                        'name': '˝Ŏʹ+$ҾʻȓǁÕǅ\xa0ϿҀȈмӦӈǊαNŔÏӘħʤҎ˻ȋх',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            623383.206089945,
                                                                            834375.376260207,
                                                                            819918.9500464081,
                                                                            541845.9218775029,
                                                                            970143.0555760008,
                                                                            556221.402486666,
                                                                            439004.9464180864,
                                                                            429743.4876854223,
                                                                            386687.2608252527,
                                                                            764947.9566585219,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩϓǎȆѸ\u038dОģ҆ƉϞTҼÅɸͲ%WӌʒͲȂнƃ\x8fԅҥ˶˹ј',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7466560458496864871,
                                                                            -4709673011755912702,
                                                                            7311594507485295271,
                                                                            -8811602754494207347,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'μǌʨƢЛЌȯȁfɍøńΙʔǅŲί',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            971183.682369554,
                                                                            11558.679040789706,
                                                                            271833.89429006056,
                                                                            353697.43552526424,
                                                                            791281.6508859112,
                                                                            259585.12489200762,
                                                                            -38574.506925464295,
                                                                            362057.8243575314,
                                                                            597859.2391965836,
                                                                            608374.1137511595,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɩˍʁƇ˻ǧҙʿǆĆˀΰρЌѣ*ŰτӇʼқǸžʚĲЯƁγȸ˻',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ůɣǂŉ҅ӊ˺ǣω\x95ˤȰзѦœɨ˳џ˘ɀʽѫ<ʆ\xadʳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -34722.32568436735,
                                                                            -21399.484475394158,
                                                                            881592.7496293992,
                                                                            763812.8310404456,
                                                                            117710.2467778447,
                                                                            875836.576824755,
                                                                            993882.3111931146,
                                                                            946404.3389923673,
                                                                            105400.50989390543,
                                                                            695723.9556357192,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'їȅӐѱ\x95ťҸǙϚɗːǿԌóZè\x92ǻƓɁ˹ˤǗǄѤхѰ¡˻o',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3638766581758007715,
                                                    },
                                    },
                            {
                                        'name': 'жҡhѵйѷ˭l\xad\x85˳êIKˌɄѳҚµӒȂĺ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162214.854521:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Őӑŀʵŋĥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            218254.89216613607,
                                                                            987709.2777531215,
                                                                            146252.59045712612,
                                                                            714813.0412830233,
                                                                            276055.1988821178,
                                                                            523166.27305164794,
                                                                            1247.3719648787956,
                                                                            691785.117802182,
                                                                            558926.4569103109,
                                                                            -59251.90703223928,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x8fҒԜƏɪŦSÆȈǌхнԓԭϪНȐӽ˸j',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162215.190827:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'řʹʈòԈʮŏӸ˝ɛэƲκȨӏÒѣÅvʽєӢдưȝѯÍǅŅͱ',
                    'message': 'ҍƌӭȓɱǬ˗АȬԧȕӴìƊĤХбϓж}Ҵʋð\x98ȜДҨԨ×q',
                    'arguments': [
                            {
                                        'name': 'ʈ½ǫҙЃǽ5ύԝЁΦ˛œĳωҢΠ\x82Ϥʟʹ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 139049.13782284822,
                                                    },
                                    },
                            {
                                        'name': 'ͲһÆʀԪœЕ{ðǐԏΊѮʣɣ˵ƿҝԔ\x9fӰ˯ƔĢКǒЎǸҾϵ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6736506325737474226,
                                                                            -3455438357447623194,
                                                                            7769082600321297357,
                                                                            5061482214159682724,
                                                                            -4088944451047406030,
                                                                            3641261396942922480,
                                                                            1868396619132471471,
                                                                            5509230902774277179,
                                                                            8678240651596156471,
                                                                            -808228314020651682,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѮнHɃŸȉȵƀč²Р&ЄԥΤ¥ȪЬʽĞӬŽӞΞʷщƧȘЛʜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'τОǈȆΟȂόςˡŊҫԬѵʦGGӮΦΕԩǪþĪѨмνәė¬Ԛ',
                                                    },
                                    },
                            {
                                        'name': 'еͳ)˼ʾԎɉÃŰƿЎĵԡν³ƚɈЯȶƠƏʋǾљȱɝ˓Ӌ¶˓',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŸКЁǶǷ\xad϶´ŕӿ;ЏƥéЩϏь\x94юǤғˌĭȹԔΫѓҴβə',
                                                    },
                                    },
                            {
                                        'name': '\x97Ҋʡ˳=ԊҚàѤ¸¡ά\x86ʸϬѩ˳ĎӉŒƨΏƉqΌ\x97ȶϾʶņ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 237873.1879497122,
                                                    },
                                    },
                            {
                                        'name': 'ʤºɛˬғĮėҗƸʴĕϒǎхīÞ ĬРЖϧŭ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ÛɎ\x8bȽµћʰȖ\x97ɫAĺӒҽƾ0Ȳq˃ѯΔӍ˥¯',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210910:162215.961417:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӓţlΦǖɑʬж˷ΊĆӟǃÿZɜӏϿʜØǈӭ\u0383ċҢĆϺàǜǊ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            2204139105762939212,
                                                                            8487941470574484937,
                                                                            -5323679417975522318,
                                                                            8964659425067600726,
                                                                            -2274839088982400809,
                                                                            802058010379254701,
                                                                            -2665759960942282235,
                                                                            8195109839091245016,
                                                                            -1824685939595951246,
                                                                            2035173349729559250,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ďĠȬЁʖǿɉKѣюǹОȷϮō˔U\x90˗ԅ\u038dȔ»ѨɑΛΨƹʕê',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 369820.81179156277,
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

            'identifier': 'Ĳˬŷäʹ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'ǽѰ',
                    'message': 'ľ',
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
            'request_id': 8951743,
            'error': {
                'identifier': 'ƫy\x95hǷƼđÁΑɝӆ=ÎҨΪԑԍ\x8dҒšғĳȒҟ;Ȝù|οƖ',
                'categories': [
                    'invalid-user-action',
                    'network',
                    'file',
                    'file',
                    'network',
                    'file',
                    'network',
                    'file',
                    'file',
                    'invalid-user-action',
                ],
                'source': 'ʡϭĳSб\x82ɎѩΔќȩƸϦѕǤzɫƻİQ4yǮNʰϑνƋŏƠ',
                'messages': [
                    {
                            'catalog': 'МнZ˻ԝҤ΅Ȱ Ë:ɾƘâʗʭͱϸӌԣɨԎˁʺӒѻ\x9fʸԭѭ',
                            'message': '^ѸʦǣͺɴӮʒҘ~ĄЯɼûǠПΩťΪ!.ŴΉ\u03a2țżԋ`ҏę',
                            'arguments': [
                                        {
                                                        'name': 'ÙʛЮÀɕ\u038bѰȦӖ˖ļĲ˙ӴԕǑςʒѠ҇ýɥQҨɹӦћ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8499762107619422549,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȈʎǻɄѴ¾Ӏһбӂ52Ѐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Đʐʔį˃әưɡɽǒҊȄņ\x96ϭϤƁχӳИȶÁţӌgɏőĆŮǛ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɰ˙ÂcØ\x97ʈςѭɅҁӑтĂѭ,áͺ±²ХλȜǴγĥĦ\u0379Ԕҷ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3230444845393372421,
                                                                        },
                                                    },
                                        {
                                                        'name': 'fӬǭǥĄŹ/ɤӮӛзż&ѐΆΥѺʝAГԁο\x83ҞŔƼʯӍ˲Ѱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ġѯƍϳΏŅаʜŶ`ӒұI\x82ω3ƣʛȻn\x89}˕Ӎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҟɣЗΈòʤΉɥҳϋϢϷ(ԞȡĠǃйҺȪӊσѠ˸ϊʮĈɠМǇ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'PƯąӹ¬ʅʆšaƗйʏѨ˘ҵȠǢÙǤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'MҪ\x99lǌƽЯĪГЈΜКÇѴsxПʃыŴ×ĜǢИƩƑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ѯ\x9f˒ӒųҼ΅ІʡҠԜўǌ\x81ҌȸŠş([ΐʀδ΅ӂőʵɤęˤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ċΦRį˚Ƒг˫Ɛнˑŀ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'т˹ӋԛǒнПҩȭӭ˵ˣƹԎtʝϻ«ȿİˈ˾ϱȪȀăυǒѡˋ',
                            'message': 'Н\x86Νӗμԣ¹χџ_іʞśĎɱǜԀ·ļ1ПҊҽiУ˷ӰVµͶ',
                            'arguments': [
                                        {
                                                        'name': 'еӁȼķŚ˗ӓλѝʎѶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162153.354686:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɡ˕ҬͱƪōƶĊрϘʘƚҏӑŤŮĐвʉЀχÑƏ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162153.426573:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҦԦʱσӗƶFʹ˵Ȗ6ӎɆȂɤ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5009016283771188671,
                                                                        },
                                                    },
                                        {
                                                        'name': '·Οӡˮ˒èѺϜӜǼƹ}΄ȓɟȝǳщϔѹœϣϠ}nәʊƉл',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -91975.7044750847,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϫɋǢ ώWċ\x9aΖŧуѯ˨ӔɫǼŷҿԓİ9ԇʁǲË¿Űëˡų',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8686946551038244418,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԓЫʂʤʣԀΏhÓԢə¼z˼ǆÇәҕϸаİҦÂӸʪө˪ԥʝ]',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5152302482800468293,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӟɀ\x7fϘω\x88дű˾êн˯ÄʌԦӷūÃԧĶˈмԮǏԑӏԞȳӪʯ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˒ȲŽʊƃяˏҠĴҧĢΖӲԍɈϣ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐӾӜɲΨЩѴsǣԅeǾ˂ΣǆπƸϻϴƷłϯϓϰȠѲЭСԃƸ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӆτƍӏˑ͵ġυƈҭɾƢ?җSΫȭ£lYǳԀӒϑϨРќԙ\x94Ȫ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˾ԂʐӭҎЪƷӵӊӍæ0®ȆǦͽôȎїĔƅԃǶ˕ΆϹ;+ƨo',
                            'message': 'ȐͰļҪNҎɻηҩɝ\x85İŘЌљϮϻЀŷŁƶǾԫԇϴʸӠųΔӽ',
                            'arguments': [
                                        {
                                                        'name': 'ŘƼʽʶǥ˅ɟѧгɛƘ҉ƸyϚÍ\x8aŪ҄πșӖ˕х',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҲȇǬǫу˾ŌλəФԛϕӋʁˬһǄĕŰĂєϭШпʨͿĀеɱʈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2305379385179730233,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Êǭ˱Ε6-ϖРˍžWəƴ\x9fŰǵʶҮŅ@Ŭ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9cJÜǬƻ\x97ŀіhέǗ«ԁвČηͰƅϧɒǱǛƛ˽ɑԚƧ¥ƣӐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҥ>βäϾűƕĨӷοɣѥʮ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŲǛέʛ˺ǔuȠ~ЛϴƷĺԊϛ˜',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162154.643761:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɹӐЬǭӅϕ˳ѿČɘπ·ȇʗ\x8eѠʜœԁԊʆҀʶҡЖȣҤͼ˽v',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЭǆƂѷœŲzѫҢϽǧɔԆУUȀŅԄѓCčϹ9ʓXãӝ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҝѸƨԞæȴ¢˼ʟ\x9fǄѐȚȾʭôƊʛӸęӁЃҸþҢÀѿƊƦŌ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162154.902990:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '%ҫ˅ƼȫԍɐȨ´ΡүaǂR҇ǪÑыȨӽҫzþ˅ơӶÛŢ\x82ђ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ƏƃιêʼǸϯɠGŷĹҧӪʼȐ§њʐʷҷĶϓ΄Ħõ-\x97ǃȆα',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'κEЛâ҄ƘȄӶҡ΄ͱђƃҦƟŋ@\x87āÞʠͲ ҄XʸŇԋʒԖ',
                            'message': "ԍ\x8bȾȅ҅π'\x91ΉˠљĄƊпԒь\\ǇтԦɉρ΅αŅŢ\u0383ϐҡ˪",
                            'arguments': [
                                        {
                                                        'name': 'ƍ˴ɸǬśʲ˩ȊɚϳǭǸȆtțʝĄʟHѢʰӿ¾ϐ:ȠbΣ\x97Ѱ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸčʄɊаѵēζ\x84ˤЃÎƷŶѥѿţӷԘȣĴҙԞTvʀˮŗ˄˾',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1100694137248491182,
                                                                        },
                                                    },
                                        {
                                                        'name': 'îѭ˙ίɂƆđˣҝεf\u0378ǎʜʲ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɾŌˡűӟƋӍġnÂʚÑ҄áʎпϻҟơґʫ˱ҹÒŁǉtǩд¦',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʷН҇ͳ\x96ĶɆӴRΓhјҊюʇ_ȱȡˋυМԝϢнƏǞӚʗηҮ',
                            'message': 'ϖӞί҃˟\x9cˮªȧƬÂǮǝƟĭ;ȃ6ĿɅɗӎяԗSǔïȠè\u0381',
                            'arguments': [
                                        {
                                                        'name': "z'ԣ˃ѪСѕ˙",
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162155.444042:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': ']ϥԧ\x90ƁǷŖήò\x8cКїҫ\x94ġĹКƲOHҖsɍáɟīŦҨʣʐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŖӑҌʂЙĻҀÝȈхǰΛϞʧӈÚˀÍǻҗˉш\x9aƇˡǒǝгӉt',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ōϳŭѯ«ӊ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 8542384227055432071,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϋ\x92ƞϨŐԚŎìTî\x8eìўLԥ\x90łΣԣЗҙɫς˴ҹőȁĸξԪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸɁɢϑҡ\x85ƼѤʛŎųϥʂƴ˶ӸɷȊ˕ѱ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162155.762197:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʀʆĩӹӿ\u0383ǜ±',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x88{Й҆ρɟӺŸˀſĄυЂţǝǨŮєŨМфƆɵƢƓѦϝŹӓÂ',
                            'message': 'ӉȃВǗƪ\x8bˋȍƥˉϫХƢɏËШһѥʁѝ\x7fƔȽ?ӮЅɋȫҕ҇',
                            'arguments': [
                                        {
                                                        'name': 'ШƲУ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -87267.4511260954,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЦʓɌɿɚ˚ԨɜӅ˹ēǊmҫнґƑĨśȜŢәԡѭѺ¨ŎĹʅќ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'óɔπЁѓʾıϞГäɒΞԓбНΔɽǞͶœɡ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĈÝ8ǜʬљӗЏ˭ˣƬӀˌ\u0380_Ю\x80ĴͻѪϳ˟Ѭԩ\x9cČˈűŃ%',
                                                                        },
                                                    },
                                        {
                                                        'name': 'јь:ɉǹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ʉѻʢ˸ЗĝΡƤcÎǍÃͷ˯ӴͽãҋƈĊÕҪΫƄ·ͰZͲѡ\u0381',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƚōɉʷKX',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 's!\u0379рϒǇʣȺЙǏЪƟϯӥʼơǿǴKӫ\u0379',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѤʛҏȑьБʷ\x9dƧɟȜȆƥК҅҄ĮɢðʝэĕҥĦҵĶ¹',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '>ŲѵχʸøĊʡшˡĸҠŃʲпƟǾҫĩƏĨЃϏđБoΐşe',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƕχԜІȿʉǱ˩˰ţʯëğìϱВЇϦϙШȡϑϻ^á˼ȣƜТi',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 3513.938889048979,
                                                                        },
                                                    },
                                        {
                                                        'name': "oſʽǺ˓ґ'PΘƲƭПÑ^ԣȈѕb˷Vҗ¿ӮɭɐԗĩßӡĐ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѫ\x88φΈӊĝѽ¡ȹε`њԬɥϑњʺUãƂԒÛ҅ŗАñ΅ώOϹ',
                            'message': 'ȓϽѤ&ϖӎÐĀʩÁƲʮιЫʪǆóѷɟɏʆ9Ýϯ˻Ėͷ\x82ЉÔ',
                            'arguments': [
                                        {
                                                        'name': 'ѳȳԗĻuʷн~ЂˁӢОԋɭʷǲ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4997385515140192623,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˠӀl˴ćчȫԬǪǺLке˥ήüϸǥƒҀԚϲȦьѻɱΝ_ɂM',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162156.917350:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЁӊɹЬƎŨ\xadǒҷͳƍϛ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162157.002786:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǗǄѨƖˬӧʯǺӠҴďʸɎɔʗķPɏɵҐŬΝRβĨʳƹˁɼͶ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ŗ˷ÍƲƲ2ƇĨŇә\x9dŃʻÈȃƣäҶȧ˔ıɂƳƐЎ9Ġ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ċғɱӕ˽ʷҢҿɠņӉȻØͿԥʵԜǤȐΜѓǷȭƘ\x82ʧ;ǈēƻ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÔԩͷĭˣĒωοȆҔЍѥƓɈŒƮ\x8bѣӺǨʂƚΧȉщ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x88ȃ·ÌǀԎҬӱ\xadǛŨϋϨȣɅ˹ϚXϢҔʾӸњΰπ»ҜǛȚ˕',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȘɒÑ˧¶ʍĢǴюЮԖƒϩԥӧĎŰЇȡԨɕЗ˵££¼ēơè',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'đ гӵȜ(ùόĶjý®ԉжРɂĆϸ\x83өӸιΪώ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '?ϲGȤǴ\x9e˼ԕŐҽʇԁҕҐͰ2ҍӢʱˌÖ«ԕΛÒ\x92VƛʳƬ',
                            'message': 'M\\љʐΛϝJфʪˮПԣˮʈԙβŎ҉ôψʬ҃ǾɝѪʃʢЯ϶ś',
                            'arguments': [
                                        {
                                                        'name': '˝ËåҶϼԤΰ\x86ВƇΞѵµȯɛͻƅɎȞjșȈǩƤΣǷ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԪƛǠȸŇĚkɉßњˈԃťӥϣΊѤďÆΑjĚӿ§ϝί\x96ϙƽΑ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'щϱ˧ҹϊхȤÏάŀȵłЯÕùʪЏͳÛţȯ˥Қ\x99ҚҘΎ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÙӢÿŕӈ\xadŒƖєɣǠ˵Ƥ˕ҚȤ\u0378ϢȲǿ˶BŹɢβәƅЂϊѤ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'σoƛΰΕԅϪơȭ\u0379Ǒ÷ΛĄ˲Ҍ҅϶ҜȔÈӞЩħ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӝħĕːѹ¹ƒɘʺӼ,ѱΔƳůΰԙΔˁӪǋˠȤΔȕͻайÌϞ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧЩҪáˎўӞñJʡѤʃZѵȂ×љѮΏʧǭƩƑў',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'jƠΝЪ˞PӮɁȰӆӭӕʆϳĻϑFˌ!ӣҀÈҵÖ7ЌʊϤΊΔ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΗΦϔόʱɨ\x92ȥĭͱ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǐ˒kӻɯʺžƵУƩŊ˫ǐԝͱŕσĻƖƼΦφćӜm',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162158.259256:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЪũŶO¬ȕʻҳɨǈƹ»',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7258559696834886415,
                                                                        },
                                                    },
                                        {
                                                        'name': '¼ŷËċǿŬФѬ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '҄tϜǨf˺ʱøύͳЇ\u0379ӛėʠԏõ˼āɄóϑƻ\x9f\x8bƮϪҷǄ˳',
                            'message': 'lЁǓʹŒАEӉ˓Ƭø¤ͲŽăçɍшӍҨHϽ=ƎȂǭŸɎ¤Ԕ',
                            'arguments': [
                                        {
                                                        'name': 'ǾӀСǉƦӔɂϨãпʠÃӜȗĒ\x82\xa0șʰ>ǭɋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʝǱѤɊҒÛĻƩЊѵΥǠƐĪˤкǔɫҿӵŶįi',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ХȈȊǜҽʩFйóβБȁҵʫǃƽϙʇſϝƽɨƭιȆǝβϕǺƮ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 304112.0614360316,
                                                                        },
                                                    },
                                        {
                                                        'name': "!ŌLʉUԎ\x83ψдʏġθʕċȚƭuɾԣѧ'ʆԮīǡч϶ϪѝѪ",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6477956491833195306,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŞώϥɖюӰţFөЉIșġIĖθƝˬμǰªѮʠψ¹GDʪ"Ƞ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʪʙȐ˚ϒˎМϓç΄ҶλņɾѱЃζĕӢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Âťӿӌԗ&ɫųǠŒˀѰпу|`pԛԮԬÞϛϖɀ\u038bҎBō',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѷϝ\x8c\\Ұʪјʨ\x96тϚŝѢ¬˩ÞȝŬGͶϊͼÿƫǶͺӜҋ\u0380ʒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˮøɎ˃ϮΣåʁϓʾӲ%ͼYԝԢď',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ωˊŴлϿæƟŁҁǇ@ǤĜũǚԗҦςˆΈŎíʾĠ\xa0Ǌȼˢ½Ɏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɂ\x8eȳͲǩǍƱȹɨѥǋҎìĝŚҁDǝ\u0378ǲPӻƔʮȑԑNĈÏˢ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÉďҕŸ˪ªţԐΑЪƯ҅đʽˎĖʢťђτʳ\x94©˓χҤƟӌӌƐ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ѻ˃',
                            'message': 'ȡѸȑǅŮűßŋSϋ˭ȬԞεmΊDW˨ĴĕŋϪ҃яZ˯TȀҌ',
                            'arguments': [
                                        {
                                                        'name': 'ɹ·ьѤƴѿǌЇЁőÏʿ˕ҋ˸ɜԨȫө æɷʄҙʳΖЖ2Ҭχ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӚҔƯӦǎɯџѲŹϕȤ˛ҊǑϳɄЇĉQƊȺӽ\x84Ɨ˰ƙƱ˕Øϣ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'd\u0382ҼÞƜİ˪ȃѠϤғ%ӾԌҢ˩ДәΖ˽ǝǲūѣӒţGӁΙĪ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǣѪςÄΜkǊí·ӣȍvϼņğѫÕʍǻҜъΉʤʲωЍϕǞԦǂ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 856905.3618538551,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ίƍ˩ȂΥŮůˉ1ҌәˌƙϸčΌӚѼnʢÝʣЕƶЬȨŗΌȡ\x8b',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162159.637404:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐČͼɧēɓ\x94˝ȐΆϏɡΥȑ˰źɢтѴªȏƩϋϱˬʻαǣɃ˼',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2069685048431380652,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԧę\x90ΧoŐɱ\u038dҢҠʮҦЦ®șϹčсΐFƛ\x86ȎūˎǔҦ^ђˬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'KΗ˃Ѹ˩ʷϤūƎЪǤ~Ө»őťđ\x8aŌӨϧGѕǐѴι\x7fąєГ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӴέсĞҤĘɻОʡӌӖǡһˊԞѱOҥԭӝѸʂʥӳŭѬȻѩΟӃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210910:162159.962205:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɔ҇ǓƮʻƩԋΝȠ\x9bэʂ7˫ҁΫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Λ˾΄нцҾǓ²¾ΓϏŗϨϗʳrЪ˜иХˠΟˣɗĸ˔ώɤǲȣ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8312082528779139253,
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

            'request_id': 3522313,

            'error': {
                'identifier': 'ķǊΓɇҩ',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'Ҧ6',
                            'message': 'Ķ',
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
            'nw_x_pixel': 1992621200,
            'nw_y_pixel': 691542463,
            'width': -7176833688831242640,
            'height': -691851944695249247,
            'ratio_x': 779840514331300517,
            'ratio_y': -2941825973934112966,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -546535221,

            'nw_y_pixel': -1757810597,

            'width': -3060302360790705985,

            'height': -6934249106647321489,

            'ratio_x': -1983174167776928729,

            'ratio_y': -5916802255483834215,

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
                    'nw_x_pixel': -1685411607,
                    'nw_y_pixel': -1787617074,
                    'width': -908570059730385755,
                    'height': -1153865902253255272,
                    'ratio_x': -3759793294134232643,
                    'ratio_y': -4434721490723906299,
                },
                {
                    'nw_x_pixel': 1965664217,
                    'nw_y_pixel': 289156954,
                    'width': -5513752640613938104,
                    'height': -6974150636068377954,
                    'ratio_x': 7500922193063063599,
                    'ratio_y': -8034245656671471071,
                },
                {
                    'nw_x_pixel': -1255404614,
                    'nw_y_pixel': -1696495958,
                    'width': -4614437862312608299,
                    'height': -2034981720993945533,
                    'ratio_x': -3200803517665275888,
                    'ratio_y': 3393248266417222043,
                },
                {
                    'nw_x_pixel': 309686527,
                    'nw_y_pixel': -575790126,
                    'width': -8173941509377043983,
                    'height': -2733341953584616613,
                    'ratio_x': -1054095299140476548,
                    'ratio_y': -793310997773829486,
                },
                {
                    'nw_x_pixel': 952534370,
                    'nw_y_pixel': 118880983,
                    'width': -1231836529535090982,
                    'height': -4805608273801620945,
                    'ratio_x': -21558246205335268,
                    'ratio_y': -1839737863911041224,
                },
                {
                    'nw_x_pixel': -635956202,
                    'nw_y_pixel': -177345869,
                    'width': -6957821965798907756,
                    'height': -8329958610001318642,
                    'ratio_x': 1612091453261001816,
                    'ratio_y': -6995314641787230864,
                },
                {
                    'nw_x_pixel': -295926754,
                    'nw_y_pixel': -1764326070,
                    'width': -5700730598787416161,
                    'height': -8729271104990225415,
                    'ratio_x': -8702478677858271602,
                    'ratio_y': 8703389366028559289,
                },
                {
                    'nw_x_pixel': -588714157,
                    'nw_y_pixel': 1686823183,
                    'width': -9009939894185160958,
                    'height': -1227227321693923034,
                    'ratio_x': -5982132259308104443,
                    'ratio_y': -5694202782051081501,
                },
                {
                    'nw_x_pixel': 285245457,
                    'nw_y_pixel': -1334412057,
                    'width': -3741926577408541472,
                    'height': -7645768565391525565,
                    'ratio_x': -8394741627038969486,
                    'ratio_y': -2235626837926331180,
                },
                {
                    'nw_x_pixel': 947611670,
                    'nw_y_pixel': -666160954,
                    'width': -1520721406146089231,
                    'height': -5911753207368280411,
                    'ratio_x': -631280435235329170,
                    'ratio_y': -7673829126240692741,
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
                    'description': 'ԔѮŁ˄ģз#ģɷρԢѵ¨φӅʈ(Đɶ¤ƁюќɟēĹЃЬĺƞ',
                    'monitors': [
                            {
                                        'identifier': 9707405,
                                        'width': 5514970535613870514,
                                        'height': -2955773144234754318,
                                    },
                            {
                                        'identifier': 2299846,
                                        'width': -6683062679366122610,
                                        'height': 3551502855568121986,
                                    },
                            {
                                        'identifier': 391292,
                                        'width': 4504610465012650233,
                                        'height': -1907676811839017783,
                                    },
                            {
                                        'identifier': 4852999,
                                        'width': -2739271388194787828,
                                        'height': -6886372108894014496,
                                    },
                            {
                                        'identifier': 9645794,
                                        'width': -5060930056957953603,
                                        'height': -8344782693193156893,
                                    },
                            {
                                        'identifier': 5219122,
                                        'width': 2736334679210445719,
                                        'height': 855292549991839769,
                                    },
                            {
                                        'identifier': 9900001,
                                        'width': 2558229158615884596,
                                        'height': 1929494060554624113,
                                    },
                            {
                                        'identifier': 2288499,
                                        'width': -2746190858912136929,
                                        'height': -4233101192547863695,
                                    },
                            {
                                        'identifier': 4295644,
                                        'width': 7727882604722702243,
                                        'height': 2073182459097602122,
                                    },
                            {
                                        'identifier': 7641609,
                                        'width': 3033696953236755192,
                                        'height': 9139799600342289397,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5832336,
                                        'source_nw_x_pixel': -595349776497350739,
                                        'source_nw_y_pixel': -1312270128737805164,
                                        'source_pixel_width': -1517022822757720626,
                                        'source_pixel_height': -7983997090788346458,
                                        'rotation': -1488158216086700295,
                                        'virtual_nw_x_pixel': -1805731192,
                                        'virtual_nw_y_pixel': -58280524,
                                        'virtual_width': -581843671,
                                        'virtual_height': -1200345284,
                                    },
                            {
                                        'source_monitor': 1089038,
                                        'source_nw_x_pixel': -2317758825558230228,
                                        'source_nw_y_pixel': -8529751738219731594,
                                        'source_pixel_width': -7813388332452255341,
                                        'source_pixel_height': -4963744169493952151,
                                        'rotation': -5130563148818294765,
                                        'virtual_nw_x_pixel': -298711947,
                                        'virtual_nw_y_pixel': -1569145743,
                                        'virtual_width': 883288671,
                                        'virtual_height': 1353922776,
                                    },
                            {
                                        'source_monitor': 7392961,
                                        'source_nw_x_pixel': -9193022419409058293,
                                        'source_nw_y_pixel': -1844110168801276074,
                                        'source_pixel_width': -5494169686956291015,
                                        'source_pixel_height': -2582186970588022837,
                                        'rotation': -2670738714872239911,
                                        'virtual_nw_x_pixel': 658853518,
                                        'virtual_nw_y_pixel': -1361647930,
                                        'virtual_width': 56987400,
                                        'virtual_height': 1561106196,
                                    },
                            {
                                        'source_monitor': -738690,
                                        'source_nw_x_pixel': -2067364591010480542,
                                        'source_nw_y_pixel': -7701959805317841416,
                                        'source_pixel_width': -5856565816770834897,
                                        'source_pixel_height': -4287074366525276797,
                                        'rotation': -5111696046438519110,
                                        'virtual_nw_x_pixel': 1214427198,
                                        'virtual_nw_y_pixel': -1910805330,
                                        'virtual_width': -140739472,
                                        'virtual_height': -1212608759,
                                    },
                            {
                                        'source_monitor': 9226347,
                                        'source_nw_x_pixel': -5806183137765570919,
                                        'source_nw_y_pixel': -1672070722464365938,
                                        'source_pixel_width': -1331643520465127561,
                                        'source_pixel_height': -7742459666331832354,
                                        'rotation': -1374251735477047285,
                                        'virtual_nw_x_pixel': -305031648,
                                        'virtual_nw_y_pixel': -446592677,
                                        'virtual_width': 1107198571,
                                        'virtual_height': -161817878,
                                    },
                            {
                                        'source_monitor': 121054,
                                        'source_nw_x_pixel': -5723682672355149565,
                                        'source_nw_y_pixel': -206626349131580066,
                                        'source_pixel_width': -4296327807755736766,
                                        'source_pixel_height': -8353495465978573195,
                                        'rotation': -4248212602129448435,
                                        'virtual_nw_x_pixel': 358012175,
                                        'virtual_nw_y_pixel': -295789157,
                                        'virtual_width': -1145677945,
                                        'virtual_height': 222739189,
                                    },
                            {
                                        'source_monitor': -150340,
                                        'source_nw_x_pixel': -7205098007915072129,
                                        'source_nw_y_pixel': -7005845816520079827,
                                        'source_pixel_width': -3758131543416171641,
                                        'source_pixel_height': -7854299304402756795,
                                        'rotation': -6946831146921301868,
                                        'virtual_nw_x_pixel': 399529899,
                                        'virtual_nw_y_pixel': 232935051,
                                        'virtual_width': 1850043504,
                                        'virtual_height': -1253499708,
                                    },
                            {
                                        'source_monitor': -116564,
                                        'source_nw_x_pixel': -3042475854564428375,
                                        'source_nw_y_pixel': -1575827083117165897,
                                        'source_pixel_width': -4452170192067998462,
                                        'source_pixel_height': -5395760458664583349,
                                        'rotation': -7958760655268775466,
                                        'virtual_nw_x_pixel': -528947795,
                                        'virtual_nw_y_pixel': 1722838385,
                                        'virtual_width': -1003811850,
                                        'virtual_height': -1594370493,
                                    },
                            {
                                        'source_monitor': -738073,
                                        'source_nw_x_pixel': -7554870108853185636,
                                        'source_nw_y_pixel': -4419594982562581057,
                                        'source_pixel_width': -660201465859254334,
                                        'source_pixel_height': -1593939543777293868,
                                        'rotation': -1907991327046860411,
                                        'virtual_nw_x_pixel': 1982260523,
                                        'virtual_nw_y_pixel': -1480653660,
                                        'virtual_width': -1607666696,
                                        'virtual_height': -1714380036,
                                    },
                            {
                                        'source_monitor': 7242748,
                                        'source_nw_x_pixel': -8383641736946924795,
                                        'source_nw_y_pixel': -5672107109072535436,
                                        'source_pixel_width': -4818935429337563458,
                                        'source_pixel_height': -324894326302019657,
                                        'rotation': -4164177095433710987,
                                        'virtual_nw_x_pixel': 575157842,
                                        'virtual_nw_y_pixel': -1099964625,
                                        'virtual_width': -1701153099,
                                        'virtual_height': 854425998,
                                    },
                        ],
                },
                {
                    'description': 'žӍőѸĝӤǀȷӒ¢ԈɂЋùȾǣСԩȺ9ˬșèSÎǖχќΖǶ',
                    'monitors': [
                            {
                                        'identifier': -311981,
                                        'width': -8448632565535657400,
                                        'height': -1922954103037010351,
                                    },
                            {
                                        'identifier': 7307176,
                                        'width': -296187104288438547,
                                        'height': 7458016121480018922,
                                    },
                            {
                                        'identifier': 8249513,
                                        'width': 7826278121385617225,
                                        'height': 1616626921615202148,
                                    },
                            {
                                        'identifier': 4282510,
                                        'width': 5312129502137033948,
                                        'height': 163305990767008029,
                                    },
                            {
                                        'identifier': -185813,
                                        'width': 8221986213635562401,
                                        'height': -7572095531504886262,
                                    },
                            {
                                        'identifier': -699633,
                                        'width': 5261987817736623144,
                                        'height': 4806383797277572652,
                                    },
                            {
                                        'identifier': 5027198,
                                        'width': 6155636219182588298,
                                        'height': -6080575099318282601,
                                    },
                            {
                                        'identifier': 2432786,
                                        'width': -8521400104601627473,
                                        'height': 560481085660308437,
                                    },
                            {
                                        'identifier': 7104100,
                                        'width': -5487424093364497397,
                                        'height': 5415865039770666785,
                                    },
                            {
                                        'identifier': 7220474,
                                        'width': 3198222305148045912,
                                        'height': -2191532869449977899,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 552638,
                                        'source_nw_x_pixel': -3543672467561457901,
                                        'source_nw_y_pixel': -5465241753325552049,
                                        'source_pixel_width': -1427739324475024096,
                                        'source_pixel_height': -4368107619429347251,
                                        'rotation': -7042591917620766455,
                                        'virtual_nw_x_pixel': -1405351555,
                                        'virtual_nw_y_pixel': -1878537444,
                                        'virtual_width': -1209496705,
                                        'virtual_height': 1591531342,
                                    },
                            {
                                        'source_monitor': 2363605,
                                        'source_nw_x_pixel': -4787343040853440085,
                                        'source_nw_y_pixel': -852881361289624053,
                                        'source_pixel_width': -3480674352272755960,
                                        'source_pixel_height': -3199042681943246815,
                                        'rotation': -2580729536402677749,
                                        'virtual_nw_x_pixel': -920342870,
                                        'virtual_nw_y_pixel': -872646277,
                                        'virtual_width': 1167150794,
                                        'virtual_height': 1212143511,
                                    },
                            {
                                        'source_monitor': 4742345,
                                        'source_nw_x_pixel': -486061899803450617,
                                        'source_nw_y_pixel': -434698374862901980,
                                        'source_pixel_width': -4354867043946263826,
                                        'source_pixel_height': -6681534394099349181,
                                        'rotation': -2756926010320973723,
                                        'virtual_nw_x_pixel': 979682636,
                                        'virtual_nw_y_pixel': 1910979899,
                                        'virtual_width': 73692040,
                                        'virtual_height': 676086800,
                                    },
                            {
                                        'source_monitor': 3971368,
                                        'source_nw_x_pixel': -3615157824530001048,
                                        'source_nw_y_pixel': -7373889434468764151,
                                        'source_pixel_width': -2055065407982179036,
                                        'source_pixel_height': -2035268060565496886,
                                        'rotation': -8298520697862991201,
                                        'virtual_nw_x_pixel': 1003752468,
                                        'virtual_nw_y_pixel': -251578219,
                                        'virtual_width': -1562169993,
                                        'virtual_height': 15391940,
                                    },
                            {
                                        'source_monitor': 8563741,
                                        'source_nw_x_pixel': -56587866842736225,
                                        'source_nw_y_pixel': -799217314690169085,
                                        'source_pixel_width': -2821136528104605945,
                                        'source_pixel_height': -2808374129596869115,
                                        'rotation': -2897052559005372380,
                                        'virtual_nw_x_pixel': 972122739,
                                        'virtual_nw_y_pixel': 385046666,
                                        'virtual_width': 1945278288,
                                        'virtual_height': -1668722809,
                                    },
                            {
                                        'source_monitor': 9641349,
                                        'source_nw_x_pixel': -6116625281825119115,
                                        'source_nw_y_pixel': -2469025273995485121,
                                        'source_pixel_width': -2767518349195944015,
                                        'source_pixel_height': -4573936016842807102,
                                        'rotation': -7564110519187717622,
                                        'virtual_nw_x_pixel': -79625906,
                                        'virtual_nw_y_pixel': -545540145,
                                        'virtual_width': -1231987450,
                                        'virtual_height': 845085333,
                                    },
                            {
                                        'source_monitor': -984442,
                                        'source_nw_x_pixel': -5106950713967442402,
                                        'source_nw_y_pixel': -1770728327720239269,
                                        'source_pixel_width': -1119148394054452685,
                                        'source_pixel_height': -6527243643813658415,
                                        'rotation': -5655916550804832704,
                                        'virtual_nw_x_pixel': 218202711,
                                        'virtual_nw_y_pixel': -1003959507,
                                        'virtual_width': 962119306,
                                        'virtual_height': -1308176639,
                                    },
                            {
                                        'source_monitor': 3974600,
                                        'source_nw_x_pixel': -3475121003310372072,
                                        'source_nw_y_pixel': -146141324418578462,
                                        'source_pixel_width': -6097059386731982548,
                                        'source_pixel_height': -7986246881383942234,
                                        'rotation': -574134894529213880,
                                        'virtual_nw_x_pixel': 1070981052,
                                        'virtual_nw_y_pixel': -1353671073,
                                        'virtual_width': -1950791275,
                                        'virtual_height': -1937827142,
                                    },
                            {
                                        'source_monitor': 2879858,
                                        'source_nw_x_pixel': -5199207682496358609,
                                        'source_nw_y_pixel': -3662488526277806210,
                                        'source_pixel_width': -8089451008733322596,
                                        'source_pixel_height': -4591473991317308043,
                                        'rotation': -3353697921360615679,
                                        'virtual_nw_x_pixel': -1701083565,
                                        'virtual_nw_y_pixel': 704340496,
                                        'virtual_width': 1172423225,
                                        'virtual_height': -1602123255,
                                    },
                            {
                                        'source_monitor': 6462772,
                                        'source_nw_x_pixel': -2884123166703833692,
                                        'source_nw_y_pixel': -130565561407817536,
                                        'source_pixel_width': -8031531224023001325,
                                        'source_pixel_height': -6100157002402529094,
                                        'rotation': -8317783753386022607,
                                        'virtual_nw_x_pixel': -1687498558,
                                        'virtual_nw_y_pixel': -180907745,
                                        'virtual_width': 973721425,
                                        'virtual_height': -1403242803,
                                    },
                        ],
                },
                {
                    'description': "Qʐǜʧ҅@ЄӍϚąѓЀHƲ'ϭҳЉǢфзʥtύɾцϪĹΧæ",
                    'monitors': [
                            {
                                        'identifier': 2960665,
                                        'width': 4468855172770195924,
                                        'height': 2485171981035000437,
                                    },
                            {
                                        'identifier': 1293464,
                                        'width': -3370979316733392442,
                                        'height': -3326626684634828373,
                                    },
                            {
                                        'identifier': 4966639,
                                        'width': 8519298083783320935,
                                        'height': 509060351398038479,
                                    },
                            {
                                        'identifier': 1241070,
                                        'width': 2611504000476526438,
                                        'height': -676612728366688782,
                                    },
                            {
                                        'identifier': 6527425,
                                        'width': -5295395012715393145,
                                        'height': 1351229201945742638,
                                    },
                            {
                                        'identifier': 2462813,
                                        'width': 6282150245874726758,
                                        'height': -8072890530787522506,
                                    },
                            {
                                        'identifier': 797003,
                                        'width': 1008914855259700274,
                                        'height': -3162669776682935874,
                                    },
                            {
                                        'identifier': 8551335,
                                        'width': -4082653228624542202,
                                        'height': -1935368000168442977,
                                    },
                            {
                                        'identifier': 5497241,
                                        'width': -7576608188742500193,
                                        'height': -244778962088022980,
                                    },
                            {
                                        'identifier': 847239,
                                        'width': 8949490767090466957,
                                        'height': 2752552879150228176,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3776696,
                                        'source_nw_x_pixel': -4486965584748143482,
                                        'source_nw_y_pixel': -37134893763056504,
                                        'source_pixel_width': -7657686481086516202,
                                        'source_pixel_height': -7349820867804998613,
                                        'rotation': -3689831790826854842,
                                        'virtual_nw_x_pixel': 1393856864,
                                        'virtual_nw_y_pixel': -1650439894,
                                        'virtual_width': 1068618460,
                                        'virtual_height': -148560460,
                                    },
                            {
                                        'source_monitor': 2607982,
                                        'source_nw_x_pixel': -3237851245906918942,
                                        'source_nw_y_pixel': -6648427980987880565,
                                        'source_pixel_width': -2719184326031719155,
                                        'source_pixel_height': -5563913894691064632,
                                        'rotation': -8497958219285357359,
                                        'virtual_nw_x_pixel': -1261385846,
                                        'virtual_nw_y_pixel': -1123785735,
                                        'virtual_width': 1061543357,
                                        'virtual_height': 158351667,
                                    },
                            {
                                        'source_monitor': 6721916,
                                        'source_nw_x_pixel': -7163035265412022339,
                                        'source_nw_y_pixel': -3505752289941062170,
                                        'source_pixel_width': -3207151502256671730,
                                        'source_pixel_height': -7708611872136144759,
                                        'rotation': -588380517121440732,
                                        'virtual_nw_x_pixel': 864481940,
                                        'virtual_nw_y_pixel': -1863593340,
                                        'virtual_width': 1203146238,
                                        'virtual_height': 418980305,
                                    },
                            {
                                        'source_monitor': 7142689,
                                        'source_nw_x_pixel': -4353713212000217512,
                                        'source_nw_y_pixel': -2516104227084509374,
                                        'source_pixel_width': -5374574975254610710,
                                        'source_pixel_height': -311221921963653806,
                                        'rotation': -366742453601554931,
                                        'virtual_nw_x_pixel': -915921440,
                                        'virtual_nw_y_pixel': -398255872,
                                        'virtual_width': 1876472096,
                                        'virtual_height': 1660644800,
                                    },
                            {
                                        'source_monitor': 1223499,
                                        'source_nw_x_pixel': -4461698470616562037,
                                        'source_nw_y_pixel': -1144756919774748718,
                                        'source_pixel_width': -8214477120305269957,
                                        'source_pixel_height': -3202693214918057711,
                                        'rotation': -7879904168325403921,
                                        'virtual_nw_x_pixel': 1401408010,
                                        'virtual_nw_y_pixel': -603174036,
                                        'virtual_width': -131725180,
                                        'virtual_height': 890828259,
                                    },
                            {
                                        'source_monitor': -239929,
                                        'source_nw_x_pixel': -8633690452427194770,
                                        'source_nw_y_pixel': -6871763228242898655,
                                        'source_pixel_width': -2329400860443531456,
                                        'source_pixel_height': -4280395246525267915,
                                        'rotation': -6974182927046557167,
                                        'virtual_nw_x_pixel': 1561097167,
                                        'virtual_nw_y_pixel': -462669737,
                                        'virtual_width': 222917468,
                                        'virtual_height': 791879932,
                                    },
                            {
                                        'source_monitor': 5661921,
                                        'source_nw_x_pixel': -8542356967451799877,
                                        'source_nw_y_pixel': -7073022312619047239,
                                        'source_pixel_width': -9190920084425040816,
                                        'source_pixel_height': -8556200835545006326,
                                        'rotation': -6420858609489697362,
                                        'virtual_nw_x_pixel': 833465573,
                                        'virtual_nw_y_pixel': 1113138615,
                                        'virtual_width': 570319690,
                                        'virtual_height': 39331473,
                                    },
                            {
                                        'source_monitor': 6634379,
                                        'source_nw_x_pixel': -666486147058092521,
                                        'source_nw_y_pixel': -971725022085801547,
                                        'source_pixel_width': -6662128886028593814,
                                        'source_pixel_height': -7711528437510001996,
                                        'rotation': -4995486452814591605,
                                        'virtual_nw_x_pixel': -1472874605,
                                        'virtual_nw_y_pixel': -1947838057,
                                        'virtual_width': -1881896428,
                                        'virtual_height': 1386076434,
                                    },
                            {
                                        'source_monitor': 1541381,
                                        'source_nw_x_pixel': -7241886281684547278,
                                        'source_nw_y_pixel': -6213316931302488553,
                                        'source_pixel_width': -6110612844541668373,
                                        'source_pixel_height': -6416260636387431741,
                                        'rotation': -2862608846220877911,
                                        'virtual_nw_x_pixel': -1094807926,
                                        'virtual_nw_y_pixel': 137509439,
                                        'virtual_width': -134141491,
                                        'virtual_height': 604123955,
                                    },
                            {
                                        'source_monitor': -543671,
                                        'source_nw_x_pixel': -7817456263122590884,
                                        'source_nw_y_pixel': -6868883850253324193,
                                        'source_pixel_width': -7939280318306114761,
                                        'source_pixel_height': -5272771840278732355,
                                        'rotation': -2356678158580161178,
                                        'virtual_nw_x_pixel': 1143472232,
                                        'virtual_nw_y_pixel': 1380122676,
                                        'virtual_width': -580379589,
                                        'virtual_height': 843177697,
                                    },
                        ],
                },
                {
                    'description': 'yЗȅѧVʩ¼Ĺʿːύͽʹƫԣ\x9cɊǀθ5ӃOʁϣɣǮ\x99ԙöЖ',
                    'monitors': [
                            {
                                        'identifier': -178783,
                                        'width': -2521332075567417022,
                                        'height': 1796676721856843710,
                                    },
                            {
                                        'identifier': 4159552,
                                        'width': 2757674969989362881,
                                        'height': 7090043982736142907,
                                    },
                            {
                                        'identifier': 4078037,
                                        'width': 4079957618092358575,
                                        'height': 6735345262414422542,
                                    },
                            {
                                        'identifier': 2317455,
                                        'width': 4199208077014148782,
                                        'height': 4114830490087207977,
                                    },
                            {
                                        'identifier': 3327438,
                                        'width': 2898486114030611034,
                                        'height': -877329925202399052,
                                    },
                            {
                                        'identifier': 6665861,
                                        'width': 8778256250365828563,
                                        'height': 4525932440469261649,
                                    },
                            {
                                        'identifier': 3475772,
                                        'width': 6402698965285981798,
                                        'height': 6423040525729289287,
                                    },
                            {
                                        'identifier': 6101659,
                                        'width': 3378533350890298301,
                                        'height': -4333754197069577056,
                                    },
                            {
                                        'identifier': 1194795,
                                        'width': 2501136247566925392,
                                        'height': 6516396395321789212,
                                    },
                            {
                                        'identifier': 3704715,
                                        'width': -8880271992394586617,
                                        'height': -3503331207481363829,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 666426,
                                        'source_nw_x_pixel': -7773474154588127579,
                                        'source_nw_y_pixel': -100444325000487690,
                                        'source_pixel_width': -3843816561982136447,
                                        'source_pixel_height': -542615524122125508,
                                        'rotation': -4243704808309540455,
                                        'virtual_nw_x_pixel': 67522330,
                                        'virtual_nw_y_pixel': -1764996955,
                                        'virtual_width': 294125860,
                                        'virtual_height': 1878511947,
                                    },
                            {
                                        'source_monitor': 9885289,
                                        'source_nw_x_pixel': -2457154686883415605,
                                        'source_nw_y_pixel': -447074867301932529,
                                        'source_pixel_width': -8262811674448363083,
                                        'source_pixel_height': -304239821666974035,
                                        'rotation': -2748681846187579221,
                                        'virtual_nw_x_pixel': -1587857975,
                                        'virtual_nw_y_pixel': 379767697,
                                        'virtual_width': 1627517111,
                                        'virtual_height': 1871042475,
                                    },
                            {
                                        'source_monitor': 5387219,
                                        'source_nw_x_pixel': -3045276877526213006,
                                        'source_nw_y_pixel': -500355691561936644,
                                        'source_pixel_width': -4738136719924818659,
                                        'source_pixel_height': -1377128255703574798,
                                        'rotation': -5149300135658242901,
                                        'virtual_nw_x_pixel': -593749553,
                                        'virtual_nw_y_pixel': -969490693,
                                        'virtual_width': 12721040,
                                        'virtual_height': 1727678462,
                                    },
                            {
                                        'source_monitor': 2045362,
                                        'source_nw_x_pixel': -7342818762742764437,
                                        'source_nw_y_pixel': -1554803295723838875,
                                        'source_pixel_width': -9160893535546476142,
                                        'source_pixel_height': -3472215604784946512,
                                        'rotation': -4481925334491157088,
                                        'virtual_nw_x_pixel': -1874492699,
                                        'virtual_nw_y_pixel': 1656568881,
                                        'virtual_width': -704881673,
                                        'virtual_height': 1448024160,
                                    },
                            {
                                        'source_monitor': 8248004,
                                        'source_nw_x_pixel': -1351524947391267550,
                                        'source_nw_y_pixel': -1945369913683034664,
                                        'source_pixel_width': -1678243134547052392,
                                        'source_pixel_height': -1768738133677740609,
                                        'rotation': -304032623624940662,
                                        'virtual_nw_x_pixel': 336026155,
                                        'virtual_nw_y_pixel': 1929131754,
                                        'virtual_width': 1860649671,
                                        'virtual_height': 1851726048,
                                    },
                            {
                                        'source_monitor': 5608062,
                                        'source_nw_x_pixel': -5006741666604515329,
                                        'source_nw_y_pixel': -8082369295815928833,
                                        'source_pixel_width': -8407468388892955870,
                                        'source_pixel_height': -5976351196832252866,
                                        'rotation': -4468437563429572121,
                                        'virtual_nw_x_pixel': 744790852,
                                        'virtual_nw_y_pixel': 1153478218,
                                        'virtual_width': 514591430,
                                        'virtual_height': -847742014,
                                    },
                            {
                                        'source_monitor': 3659371,
                                        'source_nw_x_pixel': -7987690858435834060,
                                        'source_nw_y_pixel': -3726644725888872042,
                                        'source_pixel_width': -8877360223276862854,
                                        'source_pixel_height': -4292050741688871563,
                                        'rotation': -6993052861611664122,
                                        'virtual_nw_x_pixel': -96647709,
                                        'virtual_nw_y_pixel': -887494649,
                                        'virtual_width': 1958799309,
                                        'virtual_height': -246746568,
                                    },
                            {
                                        'source_monitor': 5758055,
                                        'source_nw_x_pixel': -6986694844001382867,
                                        'source_nw_y_pixel': -1165907625841844488,
                                        'source_pixel_width': -1835770069413879572,
                                        'source_pixel_height': -8492848075999096780,
                                        'rotation': -7186626517032320400,
                                        'virtual_nw_x_pixel': -1115152105,
                                        'virtual_nw_y_pixel': 1580306690,
                                        'virtual_width': -1101083579,
                                        'virtual_height': 1912932888,
                                    },
                            {
                                        'source_monitor': 7098126,
                                        'source_nw_x_pixel': -423899345855207732,
                                        'source_nw_y_pixel': -6392292106598367757,
                                        'source_pixel_width': -4732341624362061851,
                                        'source_pixel_height': -7220755641986702184,
                                        'rotation': -1698056965692112115,
                                        'virtual_nw_x_pixel': 852940810,
                                        'virtual_nw_y_pixel': 1735237226,
                                        'virtual_width': 1484543557,
                                        'virtual_height': 1724130168,
                                    },
                            {
                                        'source_monitor': -353129,
                                        'source_nw_x_pixel': -1105646589680170782,
                                        'source_nw_y_pixel': -2537803386705301964,
                                        'source_pixel_width': -4032571454687915482,
                                        'source_pixel_height': -4263244822736632591,
                                        'rotation': -7606415428511611838,
                                        'virtual_nw_x_pixel': -1914723190,
                                        'virtual_nw_y_pixel': -1437370827,
                                        'virtual_width': -609710795,
                                        'virtual_height': 998529657,
                                    },
                        ],
                },
                {
                    'description': 'ʛȶ\x8aрєҰ»ɹҍԘOӘƇ!ҽȐɗЅ˩î\x9fόΖɛƕrӁϷɟԍ',
                    'monitors': [
                            {
                                        'identifier': 4854954,
                                        'width': 7532419156216058276,
                                        'height': -3914434604885998376,
                                    },
                            {
                                        'identifier': 9532768,
                                        'width': 6766033062222645225,
                                        'height': 8697018947007969362,
                                    },
                            {
                                        'identifier': 6379468,
                                        'width': -6363104459051108174,
                                        'height': 5221377446946365329,
                                    },
                            {
                                        'identifier': 957644,
                                        'width': -6326463706137930758,
                                        'height': -3173818822320183669,
                                    },
                            {
                                        'identifier': 4376402,
                                        'width': -3157651524005773783,
                                        'height': -6006328488329410967,
                                    },
                            {
                                        'identifier': 3741944,
                                        'width': 2928886818317768992,
                                        'height': -3051660646056421406,
                                    },
                            {
                                        'identifier': 8556701,
                                        'width': 609971646102834831,
                                        'height': 5207836572394811539,
                                    },
                            {
                                        'identifier': 5292394,
                                        'width': 3718872187646295613,
                                        'height': 218329464411290243,
                                    },
                            {
                                        'identifier': 5824369,
                                        'width': 7301640715950146294,
                                        'height': -820423123923551138,
                                    },
                            {
                                        'identifier': -607004,
                                        'width': 1849474502285724775,
                                        'height': 4838137462972108188,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 345676,
                                        'source_nw_x_pixel': -2827603873779826627,
                                        'source_nw_y_pixel': -1547443797092563707,
                                        'source_pixel_width': -1852980046203788027,
                                        'source_pixel_height': -4241761968103535439,
                                        'rotation': -2938775569081648144,
                                        'virtual_nw_x_pixel': -904713890,
                                        'virtual_nw_y_pixel': -1534270926,
                                        'virtual_width': 1190074142,
                                        'virtual_height': 369678798,
                                    },
                            {
                                        'source_monitor': 535245,
                                        'source_nw_x_pixel': -2653035010667428667,
                                        'source_nw_y_pixel': -1736544393966142947,
                                        'source_pixel_width': -6372849115508493676,
                                        'source_pixel_height': -466942838494865687,
                                        'rotation': -6525453711415945262,
                                        'virtual_nw_x_pixel': -1542437404,
                                        'virtual_nw_y_pixel': 1626675122,
                                        'virtual_width': 322881033,
                                        'virtual_height': -949528485,
                                    },
                            {
                                        'source_monitor': 8250485,
                                        'source_nw_x_pixel': -7878926444418523728,
                                        'source_nw_y_pixel': -7982875599202812105,
                                        'source_pixel_width': -7276840533337707349,
                                        'source_pixel_height': -2245456355412451108,
                                        'rotation': -4036016026251937507,
                                        'virtual_nw_x_pixel': -855239130,
                                        'virtual_nw_y_pixel': 143708769,
                                        'virtual_width': 180097850,
                                        'virtual_height': 110597781,
                                    },
                            {
                                        'source_monitor': 7479368,
                                        'source_nw_x_pixel': -2960089495744630856,
                                        'source_nw_y_pixel': -1710799123663686869,
                                        'source_pixel_width': -1738387741657889393,
                                        'source_pixel_height': -9190366879320935901,
                                        'rotation': -6248390846214072318,
                                        'virtual_nw_x_pixel': -1516069695,
                                        'virtual_nw_y_pixel': -645148855,
                                        'virtual_width': -333306091,
                                        'virtual_height': -1093846656,
                                    },
                            {
                                        'source_monitor': 6577257,
                                        'source_nw_x_pixel': -8258808379642508934,
                                        'source_nw_y_pixel': -1843093740626307997,
                                        'source_pixel_width': -1553199220643654594,
                                        'source_pixel_height': -6054269554744638120,
                                        'rotation': -6750364436877923522,
                                        'virtual_nw_x_pixel': 1176973497,
                                        'virtual_nw_y_pixel': -331329043,
                                        'virtual_width': 30214410,
                                        'virtual_height': 963026784,
                                    },
                            {
                                        'source_monitor': 9608289,
                                        'source_nw_x_pixel': -2818285997734879588,
                                        'source_nw_y_pixel': -7185394447973271068,
                                        'source_pixel_width': -4312772823698992370,
                                        'source_pixel_height': -3168728950999373928,
                                        'rotation': -835480537151768251,
                                        'virtual_nw_x_pixel': 783398719,
                                        'virtual_nw_y_pixel': 1769169380,
                                        'virtual_width': 70683475,
                                        'virtual_height': -1456431280,
                                    },
                            {
                                        'source_monitor': -367771,
                                        'source_nw_x_pixel': -5318220881285801396,
                                        'source_nw_y_pixel': -8186835116358352993,
                                        'source_pixel_width': -3215221068619026241,
                                        'source_pixel_height': -8873128893979347263,
                                        'rotation': -2001948074371857339,
                                        'virtual_nw_x_pixel': -1344834673,
                                        'virtual_nw_y_pixel': -367051494,
                                        'virtual_width': -1497483541,
                                        'virtual_height': -1318837043,
                                    },
                            {
                                        'source_monitor': 4945584,
                                        'source_nw_x_pixel': -2178137198425058537,
                                        'source_nw_y_pixel': -5217110563140466644,
                                        'source_pixel_width': -518240442906014698,
                                        'source_pixel_height': -6433330164530196835,
                                        'rotation': -3536980840834877384,
                                        'virtual_nw_x_pixel': -423621636,
                                        'virtual_nw_y_pixel': -1467452228,
                                        'virtual_width': 1252076553,
                                        'virtual_height': 432257683,
                                    },
                            {
                                        'source_monitor': 3241669,
                                        'source_nw_x_pixel': -5587311373123317914,
                                        'source_nw_y_pixel': -9073610378153784464,
                                        'source_pixel_width': -7825159864705180714,
                                        'source_pixel_height': -2154550045284224003,
                                        'rotation': -6593742337950648542,
                                        'virtual_nw_x_pixel': -1133105445,
                                        'virtual_nw_y_pixel': -969177597,
                                        'virtual_width': 1671798540,
                                        'virtual_height': -469073652,
                                    },
                            {
                                        'source_monitor': 2627995,
                                        'source_nw_x_pixel': -8094231278050058355,
                                        'source_nw_y_pixel': -1838435991208822578,
                                        'source_pixel_width': -3442875259629103424,
                                        'source_pixel_height': -4613908800307563031,
                                        'rotation': -6381685395295425261,
                                        'virtual_nw_x_pixel': 287310077,
                                        'virtual_nw_y_pixel': -1894698108,
                                        'virtual_width': 995293355,
                                        'virtual_height': -59984502,
                                    },
                        ],
                },
                {
                    'description': 'ЏɢӛƬ>ЙķɳʤFȨʵƵѳȰ\u038bɺ\x8aӣƖҼŪԥΫəƲѭӶӭ\x8a',
                    'monitors': [
                            {
                                        'identifier': 3214383,
                                        'width': 7828229758455288736,
                                        'height': -5175313271713866726,
                                    },
                            {
                                        'identifier': 6118321,
                                        'width': -8558064202552507733,
                                        'height': -8660259801518640695,
                                    },
                            {
                                        'identifier': 2382820,
                                        'width': 3342367279265731891,
                                        'height': -2326563626011457357,
                                    },
                            {
                                        'identifier': 9164154,
                                        'width': 8726098485223853775,
                                        'height': -4077972169902594139,
                                    },
                            {
                                        'identifier': 8606505,
                                        'width': -6136474379572108255,
                                        'height': 5983988397293413398,
                                    },
                            {
                                        'identifier': 5316066,
                                        'width': 4793146167095404885,
                                        'height': -7786129016242220289,
                                    },
                            {
                                        'identifier': 419686,
                                        'width': 4149627619121037701,
                                        'height': -2980269380228890422,
                                    },
                            {
                                        'identifier': -318413,
                                        'width': -1017883297741053336,
                                        'height': -7449021910084842082,
                                    },
                            {
                                        'identifier': 7479946,
                                        'width': -8641376210771976589,
                                        'height': 1963186997126218105,
                                    },
                            {
                                        'identifier': -39873,
                                        'width': 2833176872041018894,
                                        'height': 2276947007741312858,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2718674,
                                        'source_nw_x_pixel': -7183527056407150036,
                                        'source_nw_y_pixel': -8414651445441777606,
                                        'source_pixel_width': -3949411097659465435,
                                        'source_pixel_height': -4942971714581885262,
                                        'rotation': -4000330191343159402,
                                        'virtual_nw_x_pixel': -1021473448,
                                        'virtual_nw_y_pixel': 1624198348,
                                        'virtual_width': 1533276074,
                                        'virtual_height': -994451373,
                                    },
                            {
                                        'source_monitor': 8745923,
                                        'source_nw_x_pixel': -3567101168261936453,
                                        'source_nw_y_pixel': -629351323727013698,
                                        'source_pixel_width': -901456738435521624,
                                        'source_pixel_height': -407326284999278376,
                                        'rotation': -8658141077078034352,
                                        'virtual_nw_x_pixel': -1169016879,
                                        'virtual_nw_y_pixel': 1154529767,
                                        'virtual_width': -308857684,
                                        'virtual_height': 1861906098,
                                    },
                            {
                                        'source_monitor': 4442209,
                                        'source_nw_x_pixel': -763591337442428520,
                                        'source_nw_y_pixel': -6750965335843174567,
                                        'source_pixel_width': -1640306807980077390,
                                        'source_pixel_height': -6213890540787454239,
                                        'rotation': -7783249113056364148,
                                        'virtual_nw_x_pixel': 1083189892,
                                        'virtual_nw_y_pixel': 737603401,
                                        'virtual_width': 1426871969,
                                        'virtual_height': 614787734,
                                    },
                            {
                                        'source_monitor': 1933029,
                                        'source_nw_x_pixel': -7145247768564892552,
                                        'source_nw_y_pixel': -3257800043948418698,
                                        'source_pixel_width': -3016895065071038356,
                                        'source_pixel_height': -2593249265851556403,
                                        'rotation': -7046195500356531002,
                                        'virtual_nw_x_pixel': -867349727,
                                        'virtual_nw_y_pixel': 1410392572,
                                        'virtual_width': -1778743961,
                                        'virtual_height': -1187989573,
                                    },
                            {
                                        'source_monitor': 9382577,
                                        'source_nw_x_pixel': -3462099162781878459,
                                        'source_nw_y_pixel': -5138350660990537250,
                                        'source_pixel_width': -8577900389268995307,
                                        'source_pixel_height': -6139765005319882943,
                                        'rotation': -5995620098319134620,
                                        'virtual_nw_x_pixel': -1198795899,
                                        'virtual_nw_y_pixel': 1001980926,
                                        'virtual_width': 406189606,
                                        'virtual_height': -1908740542,
                                    },
                            {
                                        'source_monitor': 6877644,
                                        'source_nw_x_pixel': -7531744994202855227,
                                        'source_nw_y_pixel': -5078288886206922646,
                                        'source_pixel_width': -8396895209663421790,
                                        'source_pixel_height': -8267814305041339196,
                                        'rotation': -4369663424043627831,
                                        'virtual_nw_x_pixel': -1665231772,
                                        'virtual_nw_y_pixel': 337878636,
                                        'virtual_width': 194331671,
                                        'virtual_height': -214798518,
                                    },
                            {
                                        'source_monitor': -76556,
                                        'source_nw_x_pixel': -6008152291166643336,
                                        'source_nw_y_pixel': -220255693440199223,
                                        'source_pixel_width': -3253775034486569753,
                                        'source_pixel_height': -1214815223998406828,
                                        'rotation': -2379295477342175632,
                                        'virtual_nw_x_pixel': -922278743,
                                        'virtual_nw_y_pixel': -1680100703,
                                        'virtual_width': 1321195181,
                                        'virtual_height': 1871522309,
                                    },
                            {
                                        'source_monitor': 5827959,
                                        'source_nw_x_pixel': -3371699103146575481,
                                        'source_nw_y_pixel': -185814976909962717,
                                        'source_pixel_width': -6051497856280391783,
                                        'source_pixel_height': -5527862791461783840,
                                        'rotation': -3519723273251226487,
                                        'virtual_nw_x_pixel': -1093068909,
                                        'virtual_nw_y_pixel': 1309644314,
                                        'virtual_width': -1676829543,
                                        'virtual_height': 1934193291,
                                    },
                            {
                                        'source_monitor': -377402,
                                        'source_nw_x_pixel': -1432086615067381639,
                                        'source_nw_y_pixel': -3761417973786219730,
                                        'source_pixel_width': -2946314940089165037,
                                        'source_pixel_height': -7720163267189320361,
                                        'rotation': -4900294351441098246,
                                        'virtual_nw_x_pixel': 262190989,
                                        'virtual_nw_y_pixel': -561005850,
                                        'virtual_width': 1805236186,
                                        'virtual_height': -1488099001,
                                    },
                            {
                                        'source_monitor': 2768867,
                                        'source_nw_x_pixel': -3042517367919926200,
                                        'source_nw_y_pixel': -6555962095908600524,
                                        'source_pixel_width': -8274360739212894743,
                                        'source_pixel_height': -1736668407736387688,
                                        'rotation': -6758274360129195731,
                                        'virtual_nw_x_pixel': 1758296271,
                                        'virtual_nw_y_pixel': -1614322491,
                                        'virtual_width': 1905179106,
                                        'virtual_height': 1053733318,
                                    },
                        ],
                },
                {
                    'description': 'Čӣ\x83ӶϢxˌǺӗāЍˑ\xadÚόʃ\u0380ȌΡѿһDӾƩ˱şҋϡђ/',
                    'monitors': [
                            {
                                        'identifier': 3647891,
                                        'width': -4724314734891363400,
                                        'height': -7088541500418804069,
                                    },
                            {
                                        'identifier': 4487503,
                                        'width': -3504048942616433540,
                                        'height': -6112013096710539900,
                                    },
                            {
                                        'identifier': -261363,
                                        'width': -5440832463928763017,
                                        'height': -3069751459587587509,
                                    },
                            {
                                        'identifier': 7512283,
                                        'width': 6401181202263038763,
                                        'height': 2008737959013043109,
                                    },
                            {
                                        'identifier': 3100246,
                                        'width': -3587793032073794673,
                                        'height': 183029730431885723,
                                    },
                            {
                                        'identifier': 3283236,
                                        'width': -4463995159450603138,
                                        'height': -1730225995262849903,
                                    },
                            {
                                        'identifier': 8821887,
                                        'width': 1957012740291474570,
                                        'height': -1561901309491005063,
                                    },
                            {
                                        'identifier': 2454237,
                                        'width': 4862950227018988603,
                                        'height': 3566089268695876712,
                                    },
                            {
                                        'identifier': 7794426,
                                        'width': -3473931540472474816,
                                        'height': 6537026800559769048,
                                    },
                            {
                                        'identifier': 8752461,
                                        'width': -3135904409803927106,
                                        'height': -2781315834126090827,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 602861,
                                        'source_nw_x_pixel': -7463608758774744261,
                                        'source_nw_y_pixel': -5167820290168081693,
                                        'source_pixel_width': -4237296488593260172,
                                        'source_pixel_height': -1523444351395956320,
                                        'rotation': -6838085557091562049,
                                        'virtual_nw_x_pixel': 1851190134,
                                        'virtual_nw_y_pixel': 1266449457,
                                        'virtual_width': 438103647,
                                        'virtual_height': 1298096426,
                                    },
                            {
                                        'source_monitor': 8693419,
                                        'source_nw_x_pixel': -157098634573022310,
                                        'source_nw_y_pixel': -7624953567904987855,
                                        'source_pixel_width': -1033072692521500381,
                                        'source_pixel_height': -6389404113817081024,
                                        'rotation': -4749406040669100684,
                                        'virtual_nw_x_pixel': -668842349,
                                        'virtual_nw_y_pixel': 1427955196,
                                        'virtual_width': 76436128,
                                        'virtual_height': 1218870662,
                                    },
                            {
                                        'source_monitor': 4038005,
                                        'source_nw_x_pixel': -3161849505326977086,
                                        'source_nw_y_pixel': -1212312360795802649,
                                        'source_pixel_width': -5771058421612779774,
                                        'source_pixel_height': -7558921594288566537,
                                        'rotation': -1282059741028791073,
                                        'virtual_nw_x_pixel': -1267039923,
                                        'virtual_nw_y_pixel': 851312431,
                                        'virtual_width': 91614182,
                                        'virtual_height': 540307424,
                                    },
                            {
                                        'source_monitor': 9327960,
                                        'source_nw_x_pixel': -415491080096609976,
                                        'source_nw_y_pixel': -3279571496742481693,
                                        'source_pixel_width': -2866798464922697911,
                                        'source_pixel_height': -5571544227796798683,
                                        'rotation': -2669753960876181981,
                                        'virtual_nw_x_pixel': 291384296,
                                        'virtual_nw_y_pixel': -558694676,
                                        'virtual_width': 1398981513,
                                        'virtual_height': -1143666834,
                                    },
                            {
                                        'source_monitor': -931846,
                                        'source_nw_x_pixel': -8025766184098884801,
                                        'source_nw_y_pixel': -780862913537945121,
                                        'source_pixel_width': -657670282939794441,
                                        'source_pixel_height': -1912192000742813696,
                                        'rotation': -7076550879658442536,
                                        'virtual_nw_x_pixel': 1228634264,
                                        'virtual_nw_y_pixel': -1981678313,
                                        'virtual_width': -365443921,
                                        'virtual_height': -1631740700,
                                    },
                            {
                                        'source_monitor': 7054395,
                                        'source_nw_x_pixel': -4304086506859447677,
                                        'source_nw_y_pixel': -6337385122382005536,
                                        'source_pixel_width': -1839064489008558194,
                                        'source_pixel_height': -440134928126273443,
                                        'rotation': -8084492569825129113,
                                        'virtual_nw_x_pixel': -1036353994,
                                        'virtual_nw_y_pixel': 1612738760,
                                        'virtual_width': 961274074,
                                        'virtual_height': 1463288908,
                                    },
                            {
                                        'source_monitor': 5227689,
                                        'source_nw_x_pixel': -5870332085895683120,
                                        'source_nw_y_pixel': -6114869780283062481,
                                        'source_pixel_width': -7546766029767520335,
                                        'source_pixel_height': -7874862720070267208,
                                        'rotation': -3171557670608819225,
                                        'virtual_nw_x_pixel': 119055691,
                                        'virtual_nw_y_pixel': -1100825658,
                                        'virtual_width': -654246687,
                                        'virtual_height': 23595469,
                                    },
                            {
                                        'source_monitor': 2758892,
                                        'source_nw_x_pixel': -2122898455233889165,
                                        'source_nw_y_pixel': -7017497999035938064,
                                        'source_pixel_width': -538502859983057275,
                                        'source_pixel_height': -6540191685638085628,
                                        'rotation': -3624051880702190916,
                                        'virtual_nw_x_pixel': 433691993,
                                        'virtual_nw_y_pixel': -777167737,
                                        'virtual_width': -1467333652,
                                        'virtual_height': -664581980,
                                    },
                            {
                                        'source_monitor': -731599,
                                        'source_nw_x_pixel': -165752370790042506,
                                        'source_nw_y_pixel': -1649917143904208141,
                                        'source_pixel_width': -7128390775913426230,
                                        'source_pixel_height': -3805695606940844925,
                                        'rotation': -353565298605349920,
                                        'virtual_nw_x_pixel': 1082811010,
                                        'virtual_nw_y_pixel': 1481792768,
                                        'virtual_width': 871031200,
                                        'virtual_height': -815174746,
                                    },
                            {
                                        'source_monitor': 7636146,
                                        'source_nw_x_pixel': -2170721426782044473,
                                        'source_nw_y_pixel': -3931504085979531947,
                                        'source_pixel_width': -4966366502791863932,
                                        'source_pixel_height': -6549181564809493100,
                                        'rotation': -7624595470553491705,
                                        'virtual_nw_x_pixel': -608548766,
                                        'virtual_nw_y_pixel': -1695939502,
                                        'virtual_width': -1200857908,
                                        'virtual_height': -217602946,
                                    },
                        ],
                },
                {
                    'description': 'ӌ҃lͼζʊԛӈӁpɌƛǱԗǺǐƤ{әƂО«ӨӋvƚ@ϔБͽ',
                    'monitors': [
                            {
                                        'identifier': 913535,
                                        'width': -7777109411321864930,
                                        'height': 7115251089713140364,
                                    },
                            {
                                        'identifier': 1354103,
                                        'width': 6794595648278202321,
                                        'height': 1473222725909790652,
                                    },
                            {
                                        'identifier': 9013454,
                                        'width': 6904845059506403620,
                                        'height': -293753383820887497,
                                    },
                            {
                                        'identifier': 2962766,
                                        'width': 3488690251392412621,
                                        'height': -2730387111156128481,
                                    },
                            {
                                        'identifier': 3247563,
                                        'width': -3085199677687357184,
                                        'height': 1410492778093332638,
                                    },
                            {
                                        'identifier': 10036,
                                        'width': 4594561160474963270,
                                        'height': -6493412545123523087,
                                    },
                            {
                                        'identifier': -82914,
                                        'width': -7602083403282523263,
                                        'height': 4583509933826007832,
                                    },
                            {
                                        'identifier': 6025907,
                                        'width': -3603535770023251200,
                                        'height': 7410525736649686857,
                                    },
                            {
                                        'identifier': 2331191,
                                        'width': -2810564691000105133,
                                        'height': -9004697250504416534,
                                    },
                            {
                                        'identifier': 8720371,
                                        'width': 7803696346403534125,
                                        'height': -2473083109696973421,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 820521,
                                        'source_nw_x_pixel': -7483684484258167245,
                                        'source_nw_y_pixel': -5815819338165380601,
                                        'source_pixel_width': -4521193850467174200,
                                        'source_pixel_height': -6278078177165023001,
                                        'rotation': -2296746168562708353,
                                        'virtual_nw_x_pixel': 1344298759,
                                        'virtual_nw_y_pixel': -943593723,
                                        'virtual_width': -1709737465,
                                        'virtual_height': 877128836,
                                    },
                            {
                                        'source_monitor': 7363162,
                                        'source_nw_x_pixel': -8415792680662158817,
                                        'source_nw_y_pixel': -5204119329287292421,
                                        'source_pixel_width': -2735553505000758292,
                                        'source_pixel_height': -9032466831808226782,
                                        'rotation': -4937853868108945099,
                                        'virtual_nw_x_pixel': 1466307597,
                                        'virtual_nw_y_pixel': -832790027,
                                        'virtual_width': -182692051,
                                        'virtual_height': -476318402,
                                    },
                            {
                                        'source_monitor': 6960184,
                                        'source_nw_x_pixel': -6956206269978244406,
                                        'source_nw_y_pixel': -1993749408218111476,
                                        'source_pixel_width': -3861242653240617107,
                                        'source_pixel_height': -8824584149964640977,
                                        'rotation': -5660458462548588530,
                                        'virtual_nw_x_pixel': 433788489,
                                        'virtual_nw_y_pixel': -807639651,
                                        'virtual_width': 1239303849,
                                        'virtual_height': 238068955,
                                    },
                            {
                                        'source_monitor': 657818,
                                        'source_nw_x_pixel': -7730935169140834667,
                                        'source_nw_y_pixel': -8161409202673957912,
                                        'source_pixel_width': -2922065259891834394,
                                        'source_pixel_height': -2038333698514308268,
                                        'rotation': -6217001194805766452,
                                        'virtual_nw_x_pixel': 424527687,
                                        'virtual_nw_y_pixel': 1927984486,
                                        'virtual_width': -638219166,
                                        'virtual_height': 315029403,
                                    },
                            {
                                        'source_monitor': 9777000,
                                        'source_nw_x_pixel': -452430295017777368,
                                        'source_nw_y_pixel': -1269299068375136347,
                                        'source_pixel_width': -1735955173067069751,
                                        'source_pixel_height': -5347423431679304086,
                                        'rotation': -872321458148964208,
                                        'virtual_nw_x_pixel': 211703655,
                                        'virtual_nw_y_pixel': 1653821205,
                                        'virtual_width': 476029423,
                                        'virtual_height': 347722653,
                                    },
                            {
                                        'source_monitor': -91946,
                                        'source_nw_x_pixel': -6575396859524303628,
                                        'source_nw_y_pixel': -5565333564486438700,
                                        'source_pixel_width': -1363119235298140213,
                                        'source_pixel_height': -502183476932338379,
                                        'rotation': -5409958115023391229,
                                        'virtual_nw_x_pixel': -174158606,
                                        'virtual_nw_y_pixel': 66377708,
                                        'virtual_width': 542366440,
                                        'virtual_height': 608112151,
                                    },
                            {
                                        'source_monitor': 2654996,
                                        'source_nw_x_pixel': -6595141378526389144,
                                        'source_nw_y_pixel': -2541659608669645913,
                                        'source_pixel_width': -2566773780641885362,
                                        'source_pixel_height': -279627171068625994,
                                        'rotation': -4893765714409336349,
                                        'virtual_nw_x_pixel': 1060795233,
                                        'virtual_nw_y_pixel': 1945368159,
                                        'virtual_width': 291020678,
                                        'virtual_height': 1612016912,
                                    },
                            {
                                        'source_monitor': 8267441,
                                        'source_nw_x_pixel': -3706568045108810048,
                                        'source_nw_y_pixel': -3241912304608314107,
                                        'source_pixel_width': -8627679469576132577,
                                        'source_pixel_height': -637349173364248415,
                                        'rotation': -6485909848878166689,
                                        'virtual_nw_x_pixel': 840046975,
                                        'virtual_nw_y_pixel': -370441181,
                                        'virtual_width': 1906004836,
                                        'virtual_height': -261537767,
                                    },
                            {
                                        'source_monitor': 190936,
                                        'source_nw_x_pixel': -1777813330597483047,
                                        'source_nw_y_pixel': -748721686861855262,
                                        'source_pixel_width': -6091433796269459015,
                                        'source_pixel_height': -1667492510840430921,
                                        'rotation': -6542660163336315456,
                                        'virtual_nw_x_pixel': -1762756420,
                                        'virtual_nw_y_pixel': -1494147053,
                                        'virtual_width': -1637904968,
                                        'virtual_height': 113187943,
                                    },
                            {
                                        'source_monitor': 4943211,
                                        'source_nw_x_pixel': -4451597609066753932,
                                        'source_nw_y_pixel': -3763631453481305381,
                                        'source_pixel_width': -3264979116948356999,
                                        'source_pixel_height': -3014473846316105768,
                                        'rotation': -8543130753804093479,
                                        'virtual_nw_x_pixel': 1068870366,
                                        'virtual_nw_y_pixel': 1351524972,
                                        'virtual_width': -212383333,
                                        'virtual_height': 70724796,
                                    },
                        ],
                },
                {
                    'description': 'Τӎ˄ȻŦĽќȀιͳʹ\x84ɦʻȨ\x80˭Ϩԙú\x828\x9d˞ԊϗɿѡŰŗ',
                    'monitors': [
                            {
                                        'identifier': 668044,
                                        'width': -812254794412810385,
                                        'height': 6832463823039296867,
                                    },
                            {
                                        'identifier': 9190428,
                                        'width': -2851164786540368403,
                                        'height': 4241165795726619729,
                                    },
                            {
                                        'identifier': 428924,
                                        'width': 4653728039100943645,
                                        'height': -1197874050795919877,
                                    },
                            {
                                        'identifier': 9026977,
                                        'width': -3725147761208069479,
                                        'height': -7286055639525863989,
                                    },
                            {
                                        'identifier': 2872678,
                                        'width': -4414308173129568596,
                                        'height': -5502902634699904099,
                                    },
                            {
                                        'identifier': 9467824,
                                        'width': -1014300159621717866,
                                        'height': -834583425205433865,
                                    },
                            {
                                        'identifier': 8532484,
                                        'width': -8950908220363035260,
                                        'height': -1873433633223990084,
                                    },
                            {
                                        'identifier': 5708821,
                                        'width': 8733427802770838243,
                                        'height': -712251364314164012,
                                    },
                            {
                                        'identifier': 9225345,
                                        'width': 4432253446458511980,
                                        'height': 6881948963386856557,
                                    },
                            {
                                        'identifier': 7850537,
                                        'width': 4364103624791631812,
                                        'height': 911505590397873021,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9243680,
                                        'source_nw_x_pixel': -7993635442116275740,
                                        'source_nw_y_pixel': -2406935750681134015,
                                        'source_pixel_width': -4942223897118808953,
                                        'source_pixel_height': -7125386136811928440,
                                        'rotation': -3128259968014267487,
                                        'virtual_nw_x_pixel': -1172904108,
                                        'virtual_nw_y_pixel': -1153867603,
                                        'virtual_width': 1400429654,
                                        'virtual_height': 189057373,
                                    },
                            {
                                        'source_monitor': 8090791,
                                        'source_nw_x_pixel': -1977610292085572038,
                                        'source_nw_y_pixel': -6029417766432783306,
                                        'source_pixel_width': -9059007762113625639,
                                        'source_pixel_height': -1690096916902038773,
                                        'rotation': -3493318135224906806,
                                        'virtual_nw_x_pixel': 229528741,
                                        'virtual_nw_y_pixel': -1399077764,
                                        'virtual_width': 1955090816,
                                        'virtual_height': 1751613644,
                                    },
                            {
                                        'source_monitor': 225636,
                                        'source_nw_x_pixel': -3074858147249304171,
                                        'source_nw_y_pixel': -5821866653802591591,
                                        'source_pixel_width': -7340054175017914243,
                                        'source_pixel_height': -8501951221256404950,
                                        'rotation': -2817896482580599038,
                                        'virtual_nw_x_pixel': 1559215194,
                                        'virtual_nw_y_pixel': 1661604667,
                                        'virtual_width': -629753226,
                                        'virtual_height': -1459071655,
                                    },
                            {
                                        'source_monitor': 1657763,
                                        'source_nw_x_pixel': -4220733244858935135,
                                        'source_nw_y_pixel': -2285618918458650842,
                                        'source_pixel_width': -6205880599613467157,
                                        'source_pixel_height': -2425848183320736999,
                                        'rotation': -2444831506949129244,
                                        'virtual_nw_x_pixel': 733022119,
                                        'virtual_nw_y_pixel': -380354066,
                                        'virtual_width': -684034559,
                                        'virtual_height': -1874740181,
                                    },
                            {
                                        'source_monitor': -752893,
                                        'source_nw_x_pixel': -2701522659083184134,
                                        'source_nw_y_pixel': -3618519422572912386,
                                        'source_pixel_width': -4193122614222031911,
                                        'source_pixel_height': -2120728723865904529,
                                        'rotation': -5311151267304281225,
                                        'virtual_nw_x_pixel': 1657612211,
                                        'virtual_nw_y_pixel': -398261235,
                                        'virtual_width': -1502281656,
                                        'virtual_height': 363599291,
                                    },
                            {
                                        'source_monitor': 390795,
                                        'source_nw_x_pixel': -7038847794348995671,
                                        'source_nw_y_pixel': -8774753439912145812,
                                        'source_pixel_width': -6010297998812050212,
                                        'source_pixel_height': -6427858864966170796,
                                        'rotation': -7462380395296218230,
                                        'virtual_nw_x_pixel': 218366259,
                                        'virtual_nw_y_pixel': -1884255830,
                                        'virtual_width': -22887842,
                                        'virtual_height': -1054249503,
                                    },
                            {
                                        'source_monitor': 8232359,
                                        'source_nw_x_pixel': -5822243669122613145,
                                        'source_nw_y_pixel': -18216696109254979,
                                        'source_pixel_width': -2930376006875818200,
                                        'source_pixel_height': -2807289183536840112,
                                        'rotation': -3096953365989012544,
                                        'virtual_nw_x_pixel': 660353664,
                                        'virtual_nw_y_pixel': -1866822581,
                                        'virtual_width': 320276550,
                                        'virtual_height': 557308996,
                                    },
                            {
                                        'source_monitor': 3813070,
                                        'source_nw_x_pixel': -1909958568544761580,
                                        'source_nw_y_pixel': -1711973530951427566,
                                        'source_pixel_width': -3095455768186306769,
                                        'source_pixel_height': -5531406631320722265,
                                        'rotation': -1401384946781987067,
                                        'virtual_nw_x_pixel': 23616008,
                                        'virtual_nw_y_pixel': 44573948,
                                        'virtual_width': 1164392668,
                                        'virtual_height': -1212979422,
                                    },
                            {
                                        'source_monitor': 3758646,
                                        'source_nw_x_pixel': -1707682639975784558,
                                        'source_nw_y_pixel': -3290480870621828843,
                                        'source_pixel_width': -4062830711203851956,
                                        'source_pixel_height': -7695941904173618122,
                                        'rotation': -4760827138487514136,
                                        'virtual_nw_x_pixel': -1837177272,
                                        'virtual_nw_y_pixel': 997162888,
                                        'virtual_width': 1629419742,
                                        'virtual_height': -1272594717,
                                    },
                            {
                                        'source_monitor': -818237,
                                        'source_nw_x_pixel': -7409574832611176618,
                                        'source_nw_y_pixel': -6523302299617624302,
                                        'source_pixel_width': -6285020791234379744,
                                        'source_pixel_height': -2768987446638541791,
                                        'rotation': -7158088309042254098,
                                        'virtual_nw_x_pixel': -165782265,
                                        'virtual_nw_y_pixel': 1706750554,
                                        'virtual_width': 1985475509,
                                        'virtual_height': -219992091,
                                    },
                        ],
                },
                {
                    'description': 'ҙ˰\x95íϿƷɲƦťĝȊƞʜϞú҃´Ƿ¹Ԡȱɘ˸Ԅɇłǀȓɇҹ',
                    'monitors': [
                            {
                                        'identifier': 3089926,
                                        'width': -4765885266501933001,
                                        'height': -7010152388780324550,
                                    },
                            {
                                        'identifier': 9347041,
                                        'width': 879143808752121117,
                                        'height': -5138394616662949662,
                                    },
                            {
                                        'identifier': -52196,
                                        'width': 1418309684390117213,
                                        'height': -3807232086231879888,
                                    },
                            {
                                        'identifier': 6507258,
                                        'width': -2523281662652326473,
                                        'height': -6661561844146572976,
                                    },
                            {
                                        'identifier': -354954,
                                        'width': 8750136367121760781,
                                        'height': 1284223613685007155,
                                    },
                            {
                                        'identifier': 3470968,
                                        'width': 8218359386726099249,
                                        'height': 1849707338606180781,
                                    },
                            {
                                        'identifier': 8970050,
                                        'width': 8402335835657665205,
                                        'height': 9013114907987147041,
                                    },
                            {
                                        'identifier': 8501260,
                                        'width': -133694665214118903,
                                        'height': 4006537334321284878,
                                    },
                            {
                                        'identifier': 8356755,
                                        'width': -5034144802327667022,
                                        'height': -6617172157706010174,
                                    },
                            {
                                        'identifier': 8710247,
                                        'width': -9026813852578359769,
                                        'height': 7818388814809073154,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7201075,
                                        'source_nw_x_pixel': -4887024595816463509,
                                        'source_nw_y_pixel': -7507036400669656556,
                                        'source_pixel_width': -2206046687065394771,
                                        'source_pixel_height': -4422449486355702556,
                                        'rotation': -8456391890911075090,
                                        'virtual_nw_x_pixel': 310293464,
                                        'virtual_nw_y_pixel': -359869724,
                                        'virtual_width': 1581789102,
                                        'virtual_height': -932304225,
                                    },
                            {
                                        'source_monitor': 225892,
                                        'source_nw_x_pixel': -4017773549429101650,
                                        'source_nw_y_pixel': -1226036784740597993,
                                        'source_pixel_width': -4314590899998885461,
                                        'source_pixel_height': -7633201661243898081,
                                        'rotation': -564531989464638626,
                                        'virtual_nw_x_pixel': 683211019,
                                        'virtual_nw_y_pixel': -1232181469,
                                        'virtual_width': -843686882,
                                        'virtual_height': 215304982,
                                    },
                            {
                                        'source_monitor': 9512436,
                                        'source_nw_x_pixel': -2616441079768491182,
                                        'source_nw_y_pixel': -2298929004515943255,
                                        'source_pixel_width': -1618828418701840822,
                                        'source_pixel_height': -6978104130586194289,
                                        'rotation': -4579066629907369829,
                                        'virtual_nw_x_pixel': 1163709933,
                                        'virtual_nw_y_pixel': 1352181741,
                                        'virtual_width': 109001596,
                                        'virtual_height': 821258049,
                                    },
                            {
                                        'source_monitor': -52851,
                                        'source_nw_x_pixel': -2687724127937708928,
                                        'source_nw_y_pixel': -4899075932111171416,
                                        'source_pixel_width': -9122605463036376920,
                                        'source_pixel_height': -2152161901768642428,
                                        'rotation': -6281424373791974097,
                                        'virtual_nw_x_pixel': -133624132,
                                        'virtual_nw_y_pixel': 1333513788,
                                        'virtual_width': 687107477,
                                        'virtual_height': -124342175,
                                    },
                            {
                                        'source_monitor': 5693975,
                                        'source_nw_x_pixel': -7658369473398996590,
                                        'source_nw_y_pixel': -715838565375000445,
                                        'source_pixel_width': -7758741789406890670,
                                        'source_pixel_height': -960952261052410572,
                                        'rotation': -943864165177493748,
                                        'virtual_nw_x_pixel': 517014601,
                                        'virtual_nw_y_pixel': 1295906436,
                                        'virtual_width': 228616795,
                                        'virtual_height': -1943917290,
                                    },
                            {
                                        'source_monitor': 5635269,
                                        'source_nw_x_pixel': -8390862848678949556,
                                        'source_nw_y_pixel': -5614957363225646361,
                                        'source_pixel_width': -4054327924537725633,
                                        'source_pixel_height': -1845837251712670231,
                                        'rotation': -5614065256794070326,
                                        'virtual_nw_x_pixel': -1053780566,
                                        'virtual_nw_y_pixel': -861145174,
                                        'virtual_width': 1844025500,
                                        'virtual_height': 1024899455,
                                    },
                            {
                                        'source_monitor': 5728570,
                                        'source_nw_x_pixel': -7553456041397826659,
                                        'source_nw_y_pixel': -8018673623646557961,
                                        'source_pixel_width': -6974599999901325803,
                                        'source_pixel_height': -7107386679103485153,
                                        'rotation': -3204432078769302526,
                                        'virtual_nw_x_pixel': 987175610,
                                        'virtual_nw_y_pixel': -386618170,
                                        'virtual_width': 1736722273,
                                        'virtual_height': 417622694,
                                    },
                            {
                                        'source_monitor': 5324796,
                                        'source_nw_x_pixel': -2725089193172929846,
                                        'source_nw_y_pixel': -4313129574186491589,
                                        'source_pixel_width': -4620537139639746354,
                                        'source_pixel_height': -4247087068442817132,
                                        'rotation': -76551321284592972,
                                        'virtual_nw_x_pixel': -1847728593,
                                        'virtual_nw_y_pixel': 1251008953,
                                        'virtual_width': 1087488353,
                                        'virtual_height': 791843152,
                                    },
                            {
                                        'source_monitor': 4422199,
                                        'source_nw_x_pixel': -134837987211624150,
                                        'source_nw_y_pixel': -8905693928590231162,
                                        'source_pixel_width': -1289065239802987982,
                                        'source_pixel_height': -5241958301210751671,
                                        'rotation': -6804626539722619088,
                                        'virtual_nw_x_pixel': -1390298146,
                                        'virtual_nw_y_pixel': -652820993,
                                        'virtual_width': 1148098233,
                                        'virtual_height': 903375909,
                                    },
                            {
                                        'source_monitor': -81918,
                                        'source_nw_x_pixel': -9196348875069426346,
                                        'source_nw_y_pixel': -8702624238135589106,
                                        'source_pixel_width': -1678817760874269735,
                                        'source_pixel_height': -2396596920059651302,
                                        'rotation': -8703317469250796195,
                                        'virtual_nw_x_pixel': 1220630247,
                                        'virtual_nw_y_pixel': -846647852,
                                        'virtual_width': 1274952803,
                                        'virtual_height': -204798711,
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
                                        'identifier': 6356121,
                                        'width': -6618878853344293148,
                                        'height': -8142317151936025472,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -6076007376513526830,
                                        'source_nw_y_pixel': -3732462964133279308,
                                        'source_pixel_width': -5292059469025878918,
                                        'source_pixel_height': -5101453165173147106,
                                        'rotation': -8822399478306203258,
                                        'virtual_nw_x_pixel': 264466427,
                                        'virtual_nw_y_pixel': -1576442484,
                                        'virtual_width': -209206130,
                                        'virtual_height': 1255134344,
                                    },
                        ],
                },
            ],

        },
    ),
]
