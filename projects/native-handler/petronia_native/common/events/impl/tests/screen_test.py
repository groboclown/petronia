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
            'identifier': 7943506,
            'width': 5333560426430837616,
            'height': 7159373195004910453,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 1300094,

            'width': 2250618861241343033,

            'height': -5019753585938997429,

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
            'source_monitor': 7636800,
            'source_nw_x_pixel': -4432724405805161395,
            'source_nw_y_pixel': -154283859353858017,
            'source_pixel_width': -1966076687535997018,
            'source_pixel_height': -8255057968760424869,
            'rotation': -4489316391073943044,
            'virtual_nw_x_pixel': 1547562201,
            'virtual_nw_y_pixel': -670320979,
            'virtual_width': -522646056,
            'virtual_height': -1395527202,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -3274573814758539694,

            'source_nw_y_pixel': -2916051945256005978,

            'source_pixel_width': -6268259871272958318,

            'source_pixel_height': -236414568797072528,

            'rotation': -7857681434396944720,

            'virtual_nw_x_pixel': 1111577174,

            'virtual_nw_y_pixel': -277632573,

            'virtual_width': 117569037,

            'virtual_height': -563793083,

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
            'description': '҃óUʭɘbѺƔƑԙ˂ƔùƁɵҕɅɻȸĔŨę£ЭϝǅңŮȘ)',
            'monitors': [
                {
                    'identifier': 7210455,
                    'width': -4029834077260532520,
                    'height': -3593887562880888620,
                },
                {
                    'identifier': 6753219,
                    'width': 1922498373630511216,
                    'height': 349242985703634364,
                },
                {
                    'identifier': 2246852,
                    'width': -4692782154449925773,
                    'height': 8481591157423682063,
                },
                {
                    'identifier': 4477785,
                    'width': 5448059668668546137,
                    'height': -7958787076696545312,
                },
                {
                    'identifier': 5884462,
                    'width': -223082288400761824,
                    'height': 6516740200268740219,
                },
                {
                    'identifier': -168780,
                    'width': 1132873645855494607,
                    'height': 8018389383762472671,
                },
                {
                    'identifier': 918928,
                    'width': 1992093816857051225,
                    'height': 2231293348236170622,
                },
                {
                    'identifier': 2774375,
                    'width': 8562811044843469115,
                    'height': 6152950747660767098,
                },
                {
                    'identifier': 8747879,
                    'width': -3149536068280748048,
                    'height': -4948026863423170824,
                },
                {
                    'identifier': 4943788,
                    'width': -5338378651242067218,
                    'height': 8112594928894161589,
                },
            ],
            'screen': [
                {
                    'source_monitor': 9823705,
                    'source_nw_x_pixel': -7990751602259163030,
                    'source_nw_y_pixel': -7423823871909088879,
                    'source_pixel_width': -1468202483384200022,
                    'source_pixel_height': -7315061863593878133,
                    'rotation': -5012662690093173027,
                    'virtual_nw_x_pixel': -839013609,
                    'virtual_nw_y_pixel': 866319620,
                    'virtual_width': -280119165,
                    'virtual_height': -754226653,
                },
                {
                    'source_monitor': 3450440,
                    'source_nw_x_pixel': -8371061802021206113,
                    'source_nw_y_pixel': -2476218563854591303,
                    'source_pixel_width': -8414161476432239509,
                    'source_pixel_height': -1752559960752886633,
                    'rotation': -7687201850559234409,
                    'virtual_nw_x_pixel': -309442979,
                    'virtual_nw_y_pixel': 1806299232,
                    'virtual_width': 690520074,
                    'virtual_height': 1420516010,
                },
                {
                    'source_monitor': 786740,
                    'source_nw_x_pixel': -798134897179057645,
                    'source_nw_y_pixel': -214006829779776831,
                    'source_pixel_width': -2201215011532987212,
                    'source_pixel_height': -6361246700797177565,
                    'rotation': -8310733331013774683,
                    'virtual_nw_x_pixel': -646353801,
                    'virtual_nw_y_pixel': -829518880,
                    'virtual_width': -383129154,
                    'virtual_height': -1621894984,
                },
                {
                    'source_monitor': 6274487,
                    'source_nw_x_pixel': -4815431610266457630,
                    'source_nw_y_pixel': -7651116791432178893,
                    'source_pixel_width': -1924829267088654300,
                    'source_pixel_height': -7634417586160923691,
                    'rotation': -3794133053982518922,
                    'virtual_nw_x_pixel': -868847095,
                    'virtual_nw_y_pixel': -157559087,
                    'virtual_width': 25109386,
                    'virtual_height': 190766414,
                },
                {
                    'source_monitor': 4234079,
                    'source_nw_x_pixel': -3294771359372549605,
                    'source_nw_y_pixel': -3660062802264657611,
                    'source_pixel_width': -6545740806729678090,
                    'source_pixel_height': -7932075279646508708,
                    'rotation': -5527751356348613207,
                    'virtual_nw_x_pixel': 761666830,
                    'virtual_nw_y_pixel': 1254269943,
                    'virtual_width': 1921983421,
                    'virtual_height': 591114644,
                },
                {
                    'source_monitor': 3691327,
                    'source_nw_x_pixel': -6557816304192423601,
                    'source_nw_y_pixel': -5421972412375369212,
                    'source_pixel_width': -3055066597211513,
                    'source_pixel_height': -1054598976818112324,
                    'rotation': -3849784858967913230,
                    'virtual_nw_x_pixel': -320249578,
                    'virtual_nw_y_pixel': -1948561798,
                    'virtual_width': 1782487703,
                    'virtual_height': -1827415877,
                },
                {
                    'source_monitor': 7664300,
                    'source_nw_x_pixel': -253446520278240000,
                    'source_nw_y_pixel': -8335815380696796549,
                    'source_pixel_width': -1017898269728670902,
                    'source_pixel_height': -5472362204537765020,
                    'rotation': -3572536943759104495,
                    'virtual_nw_x_pixel': -1908282696,
                    'virtual_nw_y_pixel': 1282899228,
                    'virtual_width': -381047683,
                    'virtual_height': 1839675024,
                },
                {
                    'source_monitor': 7178954,
                    'source_nw_x_pixel': -6253276538419233499,
                    'source_nw_y_pixel': -3068059347545184798,
                    'source_pixel_width': -9193247717442025893,
                    'source_pixel_height': -8812693170370123447,
                    'rotation': -4720753651937190025,
                    'virtual_nw_x_pixel': 1271833067,
                    'virtual_nw_y_pixel': 1494402632,
                    'virtual_width': 755308269,
                    'virtual_height': 278626889,
                },
                {
                    'source_monitor': -86370,
                    'source_nw_x_pixel': -6007183858082285558,
                    'source_nw_y_pixel': -2061827482215488244,
                    'source_pixel_width': -2323122322635722891,
                    'source_pixel_height': -5090822387270609234,
                    'rotation': -1492423449132291298,
                    'virtual_nw_x_pixel': 1098823226,
                    'virtual_nw_y_pixel': 830420360,
                    'virtual_width': 343498224,
                    'virtual_height': -483309804,
                },
                {
                    'source_monitor': 1595933,
                    'source_nw_x_pixel': -6134343343848040914,
                    'source_nw_y_pixel': -727756909238126457,
                    'source_pixel_width': -3774706623211989540,
                    'source_pixel_height': -4820873422062030385,
                    'rotation': -891528739532628746,
                    'virtual_nw_x_pixel': 97430269,
                    'virtual_nw_y_pixel': 1903296871,
                    'virtual_width': 1561083502,
                    'virtual_height': 1903896631,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 461494,
                    'width': -5965405251993556948,
                    'height': -6737581545029489110,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -5339556120236391612,
                    'source_nw_y_pixel': -7788065025281983137,
                    'source_pixel_width': -7494488586749570226,
                    'source_pixel_height': -8063473151768486788,
                    'rotation': -8090155466802694977,
                    'virtual_nw_x_pixel': -660831929,
                    'virtual_nw_y_pixel': -82902726,
                    'virtual_width': -490505896,
                    'virtual_height': -704211556,
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
            'request_id': 8997329,
            'mapped_screens_by_monitors': [
                {
                    'description': 'ÓĨѕƣğɻȔhҭгЩ´ȫƸԊǂʜӼ?ǚ^ċΐʢĵѶӺĜþ\x9f',
                    'monitors': [
                            {
                                        'identifier': 8234119,
                                        'width': -3673186445175727829,
                                        'height': -164909008030146117,
                                    },
                            {
                                        'identifier': 8736989,
                                        'width': -4293989570646362197,
                                        'height': -4783403464246717353,
                                    },
                            {
                                        'identifier': 5347296,
                                        'width': 8335713387353531139,
                                        'height': -8666023618562995677,
                                    },
                            {
                                        'identifier': 7688794,
                                        'width': -8608768655995415344,
                                        'height': -3539059381614157523,
                                    },
                            {
                                        'identifier': 7465623,
                                        'width': -696185084806568476,
                                        'height': 7097924822782206693,
                                    },
                            {
                                        'identifier': -548216,
                                        'width': 7469365024785447571,
                                        'height': 524408516685585190,
                                    },
                            {
                                        'identifier': 4105433,
                                        'width': -930231720948128519,
                                        'height': 867583244300641025,
                                    },
                            {
                                        'identifier': 3086901,
                                        'width': 1513595187186209724,
                                        'height': -8406453254835996532,
                                    },
                            {
                                        'identifier': 4683713,
                                        'width': 8080732759947760595,
                                        'height': 529412680987755387,
                                    },
                            {
                                        'identifier': 6110927,
                                        'width': -5375691442533030258,
                                        'height': -5401685487385074820,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8362852,
                                        'source_nw_x_pixel': -7769893989548192810,
                                        'source_nw_y_pixel': -115736817849260726,
                                        'source_pixel_width': -8055695013066156895,
                                        'source_pixel_height': -319148598766030661,
                                        'rotation': -3622778421065460171,
                                        'virtual_nw_x_pixel': -1579963944,
                                        'virtual_nw_y_pixel': -880770226,
                                        'virtual_width': 1771352625,
                                        'virtual_height': -745747264,
                                    },
                            {
                                        'source_monitor': 9354796,
                                        'source_nw_x_pixel': -8034071394130519809,
                                        'source_nw_y_pixel': -5274805141937729526,
                                        'source_pixel_width': -5721610610293589216,
                                        'source_pixel_height': -771171646425095168,
                                        'rotation': -1854657493464254426,
                                        'virtual_nw_x_pixel': -1257541686,
                                        'virtual_nw_y_pixel': -1997493959,
                                        'virtual_width': -1403730606,
                                        'virtual_height': -1303970510,
                                    },
                            {
                                        'source_monitor': 2544936,
                                        'source_nw_x_pixel': -751578591830190728,
                                        'source_nw_y_pixel': -8260980619874300298,
                                        'source_pixel_width': -2074428506980065750,
                                        'source_pixel_height': -7966655838268868538,
                                        'rotation': -2825717468105313061,
                                        'virtual_nw_x_pixel': -1766619137,
                                        'virtual_nw_y_pixel': -1354269678,
                                        'virtual_width': 1477042526,
                                        'virtual_height': -1741820660,
                                    },
                            {
                                        'source_monitor': 2073992,
                                        'source_nw_x_pixel': -9209904036447948852,
                                        'source_nw_y_pixel': -7060145640914301965,
                                        'source_pixel_width': -7466583412645334245,
                                        'source_pixel_height': -5973441845549852388,
                                        'rotation': -4105497970458455792,
                                        'virtual_nw_x_pixel': 1882964164,
                                        'virtual_nw_y_pixel': -1663332063,
                                        'virtual_width': 1620366557,
                                        'virtual_height': -140489377,
                                    },
                            {
                                        'source_monitor': 1682869,
                                        'source_nw_x_pixel': -1869397234756320873,
                                        'source_nw_y_pixel': -8809219981110435752,
                                        'source_pixel_width': -709163212784417481,
                                        'source_pixel_height': -8870902840622667684,
                                        'rotation': -4726049772300582000,
                                        'virtual_nw_x_pixel': -60986590,
                                        'virtual_nw_y_pixel': 1777346291,
                                        'virtual_width': -98474412,
                                        'virtual_height': 1927315806,
                                    },
                            {
                                        'source_monitor': 4159414,
                                        'source_nw_x_pixel': -6964057178612273096,
                                        'source_nw_y_pixel': -372782456440734026,
                                        'source_pixel_width': -2578054992942478229,
                                        'source_pixel_height': -2464707255106800864,
                                        'rotation': -2824978345948290338,
                                        'virtual_nw_x_pixel': -515471977,
                                        'virtual_nw_y_pixel': 1640192667,
                                        'virtual_width': 1939911306,
                                        'virtual_height': -1060561374,
                                    },
                            {
                                        'source_monitor': 700316,
                                        'source_nw_x_pixel': -734812371395912782,
                                        'source_nw_y_pixel': -6637337765759318608,
                                        'source_pixel_width': -6321924842942460465,
                                        'source_pixel_height': -7930567537597504840,
                                        'rotation': -7378596099934353098,
                                        'virtual_nw_x_pixel': -1988511973,
                                        'virtual_nw_y_pixel': -1127346938,
                                        'virtual_width': -1747233724,
                                        'virtual_height': -1354124847,
                                    },
                            {
                                        'source_monitor': 4154675,
                                        'source_nw_x_pixel': -894449511379180847,
                                        'source_nw_y_pixel': -5973789873369672990,
                                        'source_pixel_width': -8607940412928539140,
                                        'source_pixel_height': -5682962325772679421,
                                        'rotation': -928994867697476923,
                                        'virtual_nw_x_pixel': -1359643750,
                                        'virtual_nw_y_pixel': 1072921820,
                                        'virtual_width': 1337361235,
                                        'virtual_height': -224858754,
                                    },
                            {
                                        'source_monitor': 2510854,
                                        'source_nw_x_pixel': -5281420273519961532,
                                        'source_nw_y_pixel': -5188376686000289841,
                                        'source_pixel_width': -7101124658163207387,
                                        'source_pixel_height': -7441596927293858877,
                                        'rotation': -4449092837939178403,
                                        'virtual_nw_x_pixel': -1536601030,
                                        'virtual_nw_y_pixel': 896503404,
                                        'virtual_width': -1817974612,
                                        'virtual_height': -907533886,
                                    },
                            {
                                        'source_monitor': 93275,
                                        'source_nw_x_pixel': -8025333486950688215,
                                        'source_nw_y_pixel': -1173166406908861409,
                                        'source_pixel_width': -4249047923798009810,
                                        'source_pixel_height': -877254539331106843,
                                        'rotation': -6763426361110634176,
                                        'virtual_nw_x_pixel': -630668133,
                                        'virtual_nw_y_pixel': 269312503,
                                        'virtual_width': 1140766514,
                                        'virtual_height': 1952116694,
                                    },
                        ],
                },
                {
                    'description': 'ХΰcЖǾЙʞȉ\x84џ\u0379Ӷĝʩӱ%Ҡх˴˦ϥʡ˔ИѪԚɼѓ>ϧ',
                    'monitors': [
                            {
                                        'identifier': 2774705,
                                        'width': 8024384523538975080,
                                        'height': 569912080392072865,
                                    },
                            {
                                        'identifier': 8200778,
                                        'width': 7554060568055344949,
                                        'height': 4041122438937930071,
                                    },
                            {
                                        'identifier': -585085,
                                        'width': -3836603768877035003,
                                        'height': -6301443350580446560,
                                    },
                            {
                                        'identifier': 9077487,
                                        'width': 7162622916946156271,
                                        'height': 3155047789885109176,
                                    },
                            {
                                        'identifier': 6418135,
                                        'width': -8609546835332524078,
                                        'height': 3022932808814036196,
                                    },
                            {
                                        'identifier': -223232,
                                        'width': -5056324729857819742,
                                        'height': -2721296481657384351,
                                    },
                            {
                                        'identifier': 7754802,
                                        'width': -4614859430143374320,
                                        'height': 3829064470541321271,
                                    },
                            {
                                        'identifier': 2229673,
                                        'width': 1542709342316961121,
                                        'height': 1093460349171352410,
                                    },
                            {
                                        'identifier': 7810400,
                                        'width': 929862962536114236,
                                        'height': 6822152969365875835,
                                    },
                            {
                                        'identifier': -190743,
                                        'width': -6227924049481010263,
                                        'height': 8290505252906746596,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6097443,
                                        'source_nw_x_pixel': -1820204442725136801,
                                        'source_nw_y_pixel': -6061955494306654819,
                                        'source_pixel_width': -2507738181813042216,
                                        'source_pixel_height': -6780618069953770577,
                                        'rotation': -6346866101020341590,
                                        'virtual_nw_x_pixel': -547541107,
                                        'virtual_nw_y_pixel': 1272453239,
                                        'virtual_width': -413661740,
                                        'virtual_height': 532860392,
                                    },
                            {
                                        'source_monitor': 1689203,
                                        'source_nw_x_pixel': -7177369350632292642,
                                        'source_nw_y_pixel': -342650684703438758,
                                        'source_pixel_width': -2146561777526917418,
                                        'source_pixel_height': -4470204174740486733,
                                        'rotation': -996554804669320852,
                                        'virtual_nw_x_pixel': -1763198467,
                                        'virtual_nw_y_pixel': -1304876778,
                                        'virtual_width': -421944886,
                                        'virtual_height': 227092565,
                                    },
                            {
                                        'source_monitor': 587165,
                                        'source_nw_x_pixel': -845264795652298343,
                                        'source_nw_y_pixel': -8330978119289101968,
                                        'source_pixel_width': -7935199515873847521,
                                        'source_pixel_height': -7384377922605646205,
                                        'rotation': -965554481942783129,
                                        'virtual_nw_x_pixel': -593600504,
                                        'virtual_nw_y_pixel': -658691991,
                                        'virtual_width': 1511785699,
                                        'virtual_height': 801647832,
                                    },
                            {
                                        'source_monitor': 9812348,
                                        'source_nw_x_pixel': -4332103744072835168,
                                        'source_nw_y_pixel': -7027650467814584215,
                                        'source_pixel_width': -5720299078437342196,
                                        'source_pixel_height': -8056642001517480459,
                                        'rotation': -3671536418517719565,
                                        'virtual_nw_x_pixel': 460375897,
                                        'virtual_nw_y_pixel': -132429573,
                                        'virtual_width': 1628550123,
                                        'virtual_height': 46141088,
                                    },
                            {
                                        'source_monitor': 5555502,
                                        'source_nw_x_pixel': -2734493220986342312,
                                        'source_nw_y_pixel': -7312804541329620196,
                                        'source_pixel_width': -2317437014492949649,
                                        'source_pixel_height': -6314499875242894825,
                                        'rotation': -174128124172843704,
                                        'virtual_nw_x_pixel': 839207851,
                                        'virtual_nw_y_pixel': 1732828854,
                                        'virtual_width': 137095673,
                                        'virtual_height': -508568144,
                                    },
                            {
                                        'source_monitor': 299627,
                                        'source_nw_x_pixel': -2942014603866017704,
                                        'source_nw_y_pixel': -8267011425817207049,
                                        'source_pixel_width': -6223686507919133465,
                                        'source_pixel_height': -618386936878813742,
                                        'rotation': -7981220681728834177,
                                        'virtual_nw_x_pixel': -503386253,
                                        'virtual_nw_y_pixel': -8662780,
                                        'virtual_width': 335944456,
                                        'virtual_height': -1404578707,
                                    },
                            {
                                        'source_monitor': 9518882,
                                        'source_nw_x_pixel': -5028483973263605563,
                                        'source_nw_y_pixel': -1670036809570538748,
                                        'source_pixel_width': -3933056765538911227,
                                        'source_pixel_height': -8233383257033446761,
                                        'rotation': -8995865179462184419,
                                        'virtual_nw_x_pixel': -1552550517,
                                        'virtual_nw_y_pixel': 694031794,
                                        'virtual_width': 661052877,
                                        'virtual_height': 844367526,
                                    },
                            {
                                        'source_monitor': 1672130,
                                        'source_nw_x_pixel': -3238003971280581333,
                                        'source_nw_y_pixel': -73213300469321907,
                                        'source_pixel_width': -3103982006155331001,
                                        'source_pixel_height': -2483269915844546387,
                                        'rotation': -7101538418666044302,
                                        'virtual_nw_x_pixel': -1668221723,
                                        'virtual_nw_y_pixel': -1326929199,
                                        'virtual_width': 1048647776,
                                        'virtual_height': -1699262411,
                                    },
                            {
                                        'source_monitor': 7719566,
                                        'source_nw_x_pixel': -6621253145263993074,
                                        'source_nw_y_pixel': -219698963953032905,
                                        'source_pixel_width': -2305876258531994501,
                                        'source_pixel_height': -6356194117775587479,
                                        'rotation': -369808944569580864,
                                        'virtual_nw_x_pixel': -1681971363,
                                        'virtual_nw_y_pixel': 1046195218,
                                        'virtual_width': -1362521957,
                                        'virtual_height': -1355361716,
                                    },
                            {
                                        'source_monitor': -859436,
                                        'source_nw_x_pixel': -3754473325438296695,
                                        'source_nw_y_pixel': -2270047055679140480,
                                        'source_pixel_width': -4646227195383794955,
                                        'source_pixel_height': -6611622438710960712,
                                        'rotation': -190850282893768721,
                                        'virtual_nw_x_pixel': -941661802,
                                        'virtual_nw_y_pixel': -695220229,
                                        'virtual_width': 961815267,
                                        'virtual_height': -312940307,
                                    },
                        ],
                },
                {
                    'description': 'ȭ҅ñŝȯѫŅǳɮɥ¿ɢȚӰӿьɑöɅ҇įEƪ)ʩлʾΕμǠ',
                    'monitors': [
                            {
                                        'identifier': 4754262,
                                        'width': 2450369847813177740,
                                        'height': 2754948453264380199,
                                    },
                            {
                                        'identifier': 8111319,
                                        'width': 1048567701062876027,
                                        'height': -324459267167611530,
                                    },
                            {
                                        'identifier': 1461787,
                                        'width': -8257011574862060750,
                                        'height': 4413398042127444807,
                                    },
                            {
                                        'identifier': 2807945,
                                        'width': -5369227650845118746,
                                        'height': -6455697383530413953,
                                    },
                            {
                                        'identifier': 8779085,
                                        'width': -5945177612579134290,
                                        'height': -4175064789921588488,
                                    },
                            {
                                        'identifier': 2199928,
                                        'width': -720507823908522116,
                                        'height': -7009718854600569636,
                                    },
                            {
                                        'identifier': 3984761,
                                        'width': -8568188358655202371,
                                        'height': -6251311407459059152,
                                    },
                            {
                                        'identifier': 9998072,
                                        'width': 1110901237100233648,
                                        'height': 5490124607374317151,
                                    },
                            {
                                        'identifier': 3530691,
                                        'width': -7516681442326270443,
                                        'height': -8015313226618123555,
                                    },
                            {
                                        'identifier': 8768231,
                                        'width': -9176399618066530376,
                                        'height': 3658507633833198822,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 490305,
                                        'source_nw_x_pixel': -8804894983542040295,
                                        'source_nw_y_pixel': -4811907974696659493,
                                        'source_pixel_width': -3938552952564367717,
                                        'source_pixel_height': -9141903834677469400,
                                        'rotation': -5332054869208758595,
                                        'virtual_nw_x_pixel': -1935261003,
                                        'virtual_nw_y_pixel': 1962195318,
                                        'virtual_width': -976059891,
                                        'virtual_height': 507329266,
                                    },
                            {
                                        'source_monitor': 3517964,
                                        'source_nw_x_pixel': -4306343296373165606,
                                        'source_nw_y_pixel': -7848261131164077050,
                                        'source_pixel_width': -3187971803022690567,
                                        'source_pixel_height': -2884048943049458632,
                                        'rotation': -5819167540723325251,
                                        'virtual_nw_x_pixel': -1027316788,
                                        'virtual_nw_y_pixel': 1603391172,
                                        'virtual_width': 122603147,
                                        'virtual_height': 1654544289,
                                    },
                            {
                                        'source_monitor': 598790,
                                        'source_nw_x_pixel': -4658810204198992392,
                                        'source_nw_y_pixel': -4102544153756542585,
                                        'source_pixel_width': -6287472518385255080,
                                        'source_pixel_height': -7413691376597980370,
                                        'rotation': -6209818414553785129,
                                        'virtual_nw_x_pixel': -190848985,
                                        'virtual_nw_y_pixel': -1294874866,
                                        'virtual_width': 777850801,
                                        'virtual_height': 130962217,
                                    },
                            {
                                        'source_monitor': 7580858,
                                        'source_nw_x_pixel': -2358086863132645628,
                                        'source_nw_y_pixel': -7319850112773821245,
                                        'source_pixel_width': -5974735427570000869,
                                        'source_pixel_height': -4722414786696176042,
                                        'rotation': -2327321847716534799,
                                        'virtual_nw_x_pixel': 1120520851,
                                        'virtual_nw_y_pixel': -1458621043,
                                        'virtual_width': -1815417574,
                                        'virtual_height': 1101027352,
                                    },
                            {
                                        'source_monitor': 909441,
                                        'source_nw_x_pixel': -6015162853486491788,
                                        'source_nw_y_pixel': -253587292363169826,
                                        'source_pixel_width': -5472074656703104397,
                                        'source_pixel_height': -5136472795810628442,
                                        'rotation': -2368658485356545439,
                                        'virtual_nw_x_pixel': -415391674,
                                        'virtual_nw_y_pixel': -999569861,
                                        'virtual_width': -597745558,
                                        'virtual_height': -496530598,
                                    },
                            {
                                        'source_monitor': 9409370,
                                        'source_nw_x_pixel': -5595585569010224107,
                                        'source_nw_y_pixel': -653007135178262822,
                                        'source_pixel_width': -2132504058375208763,
                                        'source_pixel_height': -9170531587222819513,
                                        'rotation': -1764220372626615916,
                                        'virtual_nw_x_pixel': 289104552,
                                        'virtual_nw_y_pixel': 1997453278,
                                        'virtual_width': -209281919,
                                        'virtual_height': 1372674468,
                                    },
                            {
                                        'source_monitor': 6584621,
                                        'source_nw_x_pixel': -6397958932687711556,
                                        'source_nw_y_pixel': -107875662296020301,
                                        'source_pixel_width': -7692834885554175350,
                                        'source_pixel_height': -6527814925284212840,
                                        'rotation': -8240266842787567973,
                                        'virtual_nw_x_pixel': 1772885912,
                                        'virtual_nw_y_pixel': -113516508,
                                        'virtual_width': -1810622058,
                                        'virtual_height': 507508789,
                                    },
                            {
                                        'source_monitor': 9820950,
                                        'source_nw_x_pixel': -6363387444552981032,
                                        'source_nw_y_pixel': -1795397578412317977,
                                        'source_pixel_width': -7474211311947609711,
                                        'source_pixel_height': -4811190293247407648,
                                        'rotation': -2454957820731973621,
                                        'virtual_nw_x_pixel': 744154458,
                                        'virtual_nw_y_pixel': 314315942,
                                        'virtual_width': -936876613,
                                        'virtual_height': -1706647037,
                                    },
                            {
                                        'source_monitor': 4305212,
                                        'source_nw_x_pixel': -2766683414123475455,
                                        'source_nw_y_pixel': -263640955310085934,
                                        'source_pixel_width': -6482459562648591811,
                                        'source_pixel_height': -123296993636137771,
                                        'rotation': -3804484495710878434,
                                        'virtual_nw_x_pixel': 1389233063,
                                        'virtual_nw_y_pixel': -544240660,
                                        'virtual_width': 932876830,
                                        'virtual_height': 785421649,
                                    },
                            {
                                        'source_monitor': 5428934,
                                        'source_nw_x_pixel': -1205691726283298110,
                                        'source_nw_y_pixel': -752979068454723407,
                                        'source_pixel_width': -4284403081348701537,
                                        'source_pixel_height': -4335809400911032370,
                                        'rotation': -3145540396951386,
                                        'virtual_nw_x_pixel': -16386445,
                                        'virtual_nw_y_pixel': 211802969,
                                        'virtual_width': 1212127049,
                                        'virtual_height': -53148695,
                                    },
                        ],
                },
                {
                    'description': 'ŏʹİ6ӎƽǽϩӵӋǘѶËǙ9ʰ©ҚǌΏƘǸʁʔɤɴĒϴĤЌ',
                    'monitors': [
                            {
                                        'identifier': 2610579,
                                        'width': -4751596079107472231,
                                        'height': 7299906468790244002,
                                    },
                            {
                                        'identifier': -645051,
                                        'width': -3232457122404493217,
                                        'height': 1321756904059770025,
                                    },
                            {
                                        'identifier': 6378893,
                                        'width': -4256715972023508562,
                                        'height': 8080977439981551569,
                                    },
                            {
                                        'identifier': -570214,
                                        'width': 5253273697985175875,
                                        'height': 4645232993717344525,
                                    },
                            {
                                        'identifier': 7059492,
                                        'width': 4480892283796720509,
                                        'height': 3404268157833923742,
                                    },
                            {
                                        'identifier': 2196324,
                                        'width': 2466093765821191417,
                                        'height': 4908710799012587703,
                                    },
                            {
                                        'identifier': -156237,
                                        'width': 7275382944887498991,
                                        'height': -1038020232003464157,
                                    },
                            {
                                        'identifier': 7100199,
                                        'width': 6625742855997741548,
                                        'height': -6023267587214149776,
                                    },
                            {
                                        'identifier': 9901992,
                                        'width': 1222734146606977218,
                                        'height': 8781984515125307684,
                                    },
                            {
                                        'identifier': -693810,
                                        'width': 4162297822651797058,
                                        'height': 6853292087462648997,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1815783,
                                        'source_nw_x_pixel': -7748656134960054952,
                                        'source_nw_y_pixel': -5121031888649502186,
                                        'source_pixel_width': -4929240824127748348,
                                        'source_pixel_height': -2544880333988147425,
                                        'rotation': -3819435654359743852,
                                        'virtual_nw_x_pixel': 201403610,
                                        'virtual_nw_y_pixel': -1280955689,
                                        'virtual_width': 985775607,
                                        'virtual_height': -1294964404,
                                    },
                            {
                                        'source_monitor': 6175948,
                                        'source_nw_x_pixel': -5522985762575492962,
                                        'source_nw_y_pixel': -4388140779869350532,
                                        'source_pixel_width': -3481075824822960967,
                                        'source_pixel_height': -545263632862019946,
                                        'rotation': -8981774235883007022,
                                        'virtual_nw_x_pixel': 416403837,
                                        'virtual_nw_y_pixel': -1613660393,
                                        'virtual_width': -473876174,
                                        'virtual_height': 1497786331,
                                    },
                            {
                                        'source_monitor': 8790193,
                                        'source_nw_x_pixel': -4533467522692980548,
                                        'source_nw_y_pixel': -2982938200834031888,
                                        'source_pixel_width': -6906655864896649267,
                                        'source_pixel_height': -4180143331731302832,
                                        'rotation': -5424534449909310597,
                                        'virtual_nw_x_pixel': -1740661192,
                                        'virtual_nw_y_pixel': -215875831,
                                        'virtual_width': -1386024917,
                                        'virtual_height': 1093760989,
                                    },
                            {
                                        'source_monitor': -296051,
                                        'source_nw_x_pixel': -2969202032364682082,
                                        'source_nw_y_pixel': -327738463862802669,
                                        'source_pixel_width': -6992438978327906881,
                                        'source_pixel_height': -4277150627735973510,
                                        'rotation': -4663089428831658547,
                                        'virtual_nw_x_pixel': 1909490361,
                                        'virtual_nw_y_pixel': 1643344443,
                                        'virtual_width': -477804349,
                                        'virtual_height': -1424279700,
                                    },
                            {
                                        'source_monitor': 5616046,
                                        'source_nw_x_pixel': -886651321783584463,
                                        'source_nw_y_pixel': -1562905982893421480,
                                        'source_pixel_width': -2346846425657023593,
                                        'source_pixel_height': -8936933726486629830,
                                        'rotation': -3928835319716447251,
                                        'virtual_nw_x_pixel': -1527299423,
                                        'virtual_nw_y_pixel': 1470661416,
                                        'virtual_width': 1028698421,
                                        'virtual_height': 1326573237,
                                    },
                            {
                                        'source_monitor': 6586390,
                                        'source_nw_x_pixel': -7540266727747111036,
                                        'source_nw_y_pixel': -5703331962421652475,
                                        'source_pixel_width': -7895363983956203123,
                                        'source_pixel_height': -8292747961729092680,
                                        'rotation': -3698469923801030751,
                                        'virtual_nw_x_pixel': 1468859263,
                                        'virtual_nw_y_pixel': 568332233,
                                        'virtual_width': 1230821819,
                                        'virtual_height': -1961107245,
                                    },
                            {
                                        'source_monitor': 4257716,
                                        'source_nw_x_pixel': -5910214061421259414,
                                        'source_nw_y_pixel': -4075846981964229918,
                                        'source_pixel_width': -4805060886529915576,
                                        'source_pixel_height': -4089451082946294075,
                                        'rotation': -3018651677628564884,
                                        'virtual_nw_x_pixel': -208920591,
                                        'virtual_nw_y_pixel': 470593156,
                                        'virtual_width': -1621516295,
                                        'virtual_height': 1366017726,
                                    },
                            {
                                        'source_monitor': 5873535,
                                        'source_nw_x_pixel': -5484101189012429538,
                                        'source_nw_y_pixel': -3305395282974172824,
                                        'source_pixel_width': -3441861423744900938,
                                        'source_pixel_height': -1672116588632164323,
                                        'rotation': -1832367405681144756,
                                        'virtual_nw_x_pixel': -284349262,
                                        'virtual_nw_y_pixel': -1894619929,
                                        'virtual_width': -717110135,
                                        'virtual_height': -1280987441,
                                    },
                            {
                                        'source_monitor': 9821794,
                                        'source_nw_x_pixel': -512229888122130622,
                                        'source_nw_y_pixel': -85365514731252687,
                                        'source_pixel_width': -5883282412675413999,
                                        'source_pixel_height': -3976745620482672324,
                                        'rotation': -3195009448320485679,
                                        'virtual_nw_x_pixel': 1948113849,
                                        'virtual_nw_y_pixel': -1171635325,
                                        'virtual_width': -209577739,
                                        'virtual_height': -1654989600,
                                    },
                            {
                                        'source_monitor': 9954424,
                                        'source_nw_x_pixel': -2522694179300873578,
                                        'source_nw_y_pixel': -1491058312380267150,
                                        'source_pixel_width': -2825098388918270086,
                                        'source_pixel_height': -2529936164227164305,
                                        'rotation': -7302990061937793367,
                                        'virtual_nw_x_pixel': -206153733,
                                        'virtual_nw_y_pixel': 787847345,
                                        'virtual_width': -916449510,
                                        'virtual_height': 1011874246,
                                    },
                        ],
                },
                {
                    'description': 'ҮeɃ/ʉʽʕѺӵɦĥЭƼ;ʄȎҰѥ҉н\x9d˷ԜhѱȃŰЈŧӞ',
                    'monitors': [
                            {
                                        'identifier': 378236,
                                        'width': 6078938055800485366,
                                        'height': -2136124663120115274,
                                    },
                            {
                                        'identifier': 8637898,
                                        'width': -5615244691386310480,
                                        'height': -5973990188862098013,
                                    },
                            {
                                        'identifier': 3357131,
                                        'width': -7212781332291021813,
                                        'height': 5507932326602933467,
                                    },
                            {
                                        'identifier': 148825,
                                        'width': -6386698940704112531,
                                        'height': -4375370659884112003,
                                    },
                            {
                                        'identifier': -696210,
                                        'width': 1459241689788420571,
                                        'height': -8741899613397348393,
                                    },
                            {
                                        'identifier': 8728015,
                                        'width': -5671905253060060311,
                                        'height': 891159891810047391,
                                    },
                            {
                                        'identifier': 514996,
                                        'width': -2876132406404596925,
                                        'height': 7575150424493958031,
                                    },
                            {
                                        'identifier': 9523605,
                                        'width': -683440235101425423,
                                        'height': -7606364773894164931,
                                    },
                            {
                                        'identifier': -680859,
                                        'width': -8729054328665614288,
                                        'height': 7595500930442374877,
                                    },
                            {
                                        'identifier': 1595886,
                                        'width': -7576177266634161359,
                                        'height': -6093540087805802965,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5831516,
                                        'source_nw_x_pixel': -4636811256498847523,
                                        'source_nw_y_pixel': -9104351379070124013,
                                        'source_pixel_width': -4408237890429462942,
                                        'source_pixel_height': -5092712270567906147,
                                        'rotation': -3249872503764689204,
                                        'virtual_nw_x_pixel': 1502223004,
                                        'virtual_nw_y_pixel': -616704870,
                                        'virtual_width': 581829854,
                                        'virtual_height': 1634466760,
                                    },
                            {
                                        'source_monitor': 6103853,
                                        'source_nw_x_pixel': -3214550145969885535,
                                        'source_nw_y_pixel': -1067423131022796684,
                                        'source_pixel_width': -7550288801317030765,
                                        'source_pixel_height': -4385530215681959576,
                                        'rotation': -8238886591895843623,
                                        'virtual_nw_x_pixel': -590687812,
                                        'virtual_nw_y_pixel': -48280643,
                                        'virtual_width': 1581408583,
                                        'virtual_height': -1109184885,
                                    },
                            {
                                        'source_monitor': 8418953,
                                        'source_nw_x_pixel': -742388577996371923,
                                        'source_nw_y_pixel': -5891164529901332126,
                                        'source_pixel_width': -5204189475900434958,
                                        'source_pixel_height': -6085648640530654652,
                                        'rotation': -7354413772071839789,
                                        'virtual_nw_x_pixel': 563641679,
                                        'virtual_nw_y_pixel': -18035842,
                                        'virtual_width': -320920195,
                                        'virtual_height': 198649200,
                                    },
                            {
                                        'source_monitor': 7618572,
                                        'source_nw_x_pixel': -7711604293051646875,
                                        'source_nw_y_pixel': -6318292005647145211,
                                        'source_pixel_width': -749430143868149803,
                                        'source_pixel_height': -7926891394226737285,
                                        'rotation': -7298488009970345129,
                                        'virtual_nw_x_pixel': -83202955,
                                        'virtual_nw_y_pixel': 661301681,
                                        'virtual_width': 686344669,
                                        'virtual_height': 1019441091,
                                    },
                            {
                                        'source_monitor': 3382823,
                                        'source_nw_x_pixel': -5764036590557013112,
                                        'source_nw_y_pixel': -317639519212498968,
                                        'source_pixel_width': -7769843311274207080,
                                        'source_pixel_height': -2426401296724777646,
                                        'rotation': -672626672139164316,
                                        'virtual_nw_x_pixel': 846831697,
                                        'virtual_nw_y_pixel': 161292232,
                                        'virtual_width': -655181563,
                                        'virtual_height': 661246469,
                                    },
                            {
                                        'source_monitor': 2730090,
                                        'source_nw_x_pixel': -1591830734744869844,
                                        'source_nw_y_pixel': -3334663601038253312,
                                        'source_pixel_width': -5629782987077277921,
                                        'source_pixel_height': -755089918641019035,
                                        'rotation': -6920544651823897236,
                                        'virtual_nw_x_pixel': 1637242056,
                                        'virtual_nw_y_pixel': -1352115550,
                                        'virtual_width': 469325583,
                                        'virtual_height': -143853132,
                                    },
                            {
                                        'source_monitor': 9567335,
                                        'source_nw_x_pixel': -2761614473868231954,
                                        'source_nw_y_pixel': -2394934393360782359,
                                        'source_pixel_width': -2280763227757524813,
                                        'source_pixel_height': -7487235364506846600,
                                        'rotation': -3874735014913028998,
                                        'virtual_nw_x_pixel': -1591127754,
                                        'virtual_nw_y_pixel': 837418698,
                                        'virtual_width': 1472222642,
                                        'virtual_height': -20106757,
                                    },
                            {
                                        'source_monitor': -631207,
                                        'source_nw_x_pixel': -6092251276061800712,
                                        'source_nw_y_pixel': -8767136132265853594,
                                        'source_pixel_width': -9102733746553259042,
                                        'source_pixel_height': -214301306279171378,
                                        'rotation': -7557325873579863442,
                                        'virtual_nw_x_pixel': -382506381,
                                        'virtual_nw_y_pixel': -600638784,
                                        'virtual_width': 622143686,
                                        'virtual_height': 1378054439,
                                    },
                            {
                                        'source_monitor': 6637762,
                                        'source_nw_x_pixel': -5570456759054306072,
                                        'source_nw_y_pixel': -5238145570301828244,
                                        'source_pixel_width': -6577727003665374856,
                                        'source_pixel_height': -3059039210911107015,
                                        'rotation': -371278259713644639,
                                        'virtual_nw_x_pixel': -1991398029,
                                        'virtual_nw_y_pixel': 1179197196,
                                        'virtual_width': 1575304040,
                                        'virtual_height': 577444664,
                                    },
                            {
                                        'source_monitor': 7452977,
                                        'source_nw_x_pixel': -4845487544496844418,
                                        'source_nw_y_pixel': -7955052379236692592,
                                        'source_pixel_width': -9055313309380836091,
                                        'source_pixel_height': -9214980681148506540,
                                        'rotation': -4824340260618269850,
                                        'virtual_nw_x_pixel': -1634498337,
                                        'virtual_nw_y_pixel': -1157010149,
                                        'virtual_width': 513404384,
                                        'virtual_height': 1830262733,
                                    },
                        ],
                },
                {
                    'description': 'ҡό6О˲Čа϶ԈҷҔ҃ӺͿҗO҉Kǟƚķ6zӘÕѽбȸґĘ',
                    'monitors': [
                            {
                                        'identifier': -131418,
                                        'width': -4707402074589104950,
                                        'height': -4196595584024698748,
                                    },
                            {
                                        'identifier': 4113795,
                                        'width': -5302235930178320893,
                                        'height': 7976905193012695385,
                                    },
                            {
                                        'identifier': 2584943,
                                        'width': 1612142572148455067,
                                        'height': -403869233043850055,
                                    },
                            {
                                        'identifier': 4528960,
                                        'width': 2507959066201812634,
                                        'height': 7946521318084538427,
                                    },
                            {
                                        'identifier': 6482608,
                                        'width': 8758704714000060471,
                                        'height': -9177122773380985376,
                                    },
                            {
                                        'identifier': 9352393,
                                        'width': 2768255068162423120,
                                        'height': -5956117787156758202,
                                    },
                            {
                                        'identifier': -505064,
                                        'width': 7561859785097661559,
                                        'height': 3040289189770441300,
                                    },
                            {
                                        'identifier': 5969231,
                                        'width': 2393414211655326835,
                                        'height': 8423210010190228788,
                                    },
                            {
                                        'identifier': 6138062,
                                        'width': -6847327034105991345,
                                        'height': 7170534363649103360,
                                    },
                            {
                                        'identifier': 8043129,
                                        'width': 7387703970700114194,
                                        'height': -5404247960413789447,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8500897,
                                        'source_nw_x_pixel': -8280224743687027648,
                                        'source_nw_y_pixel': -7966958185194971839,
                                        'source_pixel_width': -675029746629339769,
                                        'source_pixel_height': -2851547351336316434,
                                        'rotation': -5134080018943190279,
                                        'virtual_nw_x_pixel': 169326335,
                                        'virtual_nw_y_pixel': -977529347,
                                        'virtual_width': 1019165010,
                                        'virtual_height': -1880649810,
                                    },
                            {
                                        'source_monitor': 6992350,
                                        'source_nw_x_pixel': -6745214294370746980,
                                        'source_nw_y_pixel': -9166173410152621463,
                                        'source_pixel_width': -6083708211735142443,
                                        'source_pixel_height': -7762954018710063320,
                                        'rotation': -7191010379244829249,
                                        'virtual_nw_x_pixel': 325595875,
                                        'virtual_nw_y_pixel': -1983139199,
                                        'virtual_width': 465099973,
                                        'virtual_height': -1964570090,
                                    },
                            {
                                        'source_monitor': 4451407,
                                        'source_nw_x_pixel': -1387951185484057593,
                                        'source_nw_y_pixel': -2575698801400452941,
                                        'source_pixel_width': -2438538896471242,
                                        'source_pixel_height': -5072637182378788700,
                                        'rotation': -1720079784649926094,
                                        'virtual_nw_x_pixel': -1730740795,
                                        'virtual_nw_y_pixel': -99129256,
                                        'virtual_width': 1479933084,
                                        'virtual_height': 397409074,
                                    },
                            {
                                        'source_monitor': 5380591,
                                        'source_nw_x_pixel': -4751944093604541494,
                                        'source_nw_y_pixel': -4324418273372123318,
                                        'source_pixel_width': -6861521460287694437,
                                        'source_pixel_height': -6749095454899249606,
                                        'rotation': -4738008594524504035,
                                        'virtual_nw_x_pixel': -1717237432,
                                        'virtual_nw_y_pixel': 773324280,
                                        'virtual_width': -580726860,
                                        'virtual_height': 778074182,
                                    },
                            {
                                        'source_monitor': 6707491,
                                        'source_nw_x_pixel': -2578186485230869057,
                                        'source_nw_y_pixel': -721492183508594872,
                                        'source_pixel_width': -7973249327338506779,
                                        'source_pixel_height': -6332845206148566525,
                                        'rotation': -6715943004956914580,
                                        'virtual_nw_x_pixel': -869493155,
                                        'virtual_nw_y_pixel': -430411346,
                                        'virtual_width': -1235919639,
                                        'virtual_height': -1932382311,
                                    },
                            {
                                        'source_monitor': -414429,
                                        'source_nw_x_pixel': -2588999073145570220,
                                        'source_nw_y_pixel': -557804810411835089,
                                        'source_pixel_width': -9143076209637498353,
                                        'source_pixel_height': -4090507164403413635,
                                        'rotation': -5858253505070998591,
                                        'virtual_nw_x_pixel': -1071436081,
                                        'virtual_nw_y_pixel': -1439416656,
                                        'virtual_width': -1382128735,
                                        'virtual_height': 1469941880,
                                    },
                            {
                                        'source_monitor': 3864653,
                                        'source_nw_x_pixel': -7539350564821751149,
                                        'source_nw_y_pixel': -1181841805781247799,
                                        'source_pixel_width': -5610412183547996686,
                                        'source_pixel_height': -269735127387222764,
                                        'rotation': -1630997797269856243,
                                        'virtual_nw_x_pixel': 1425313495,
                                        'virtual_nw_y_pixel': 650639371,
                                        'virtual_width': -173674313,
                                        'virtual_height': 1011421391,
                                    },
                            {
                                        'source_monitor': 7996312,
                                        'source_nw_x_pixel': -7147370417537827259,
                                        'source_nw_y_pixel': -254955091090871545,
                                        'source_pixel_width': -1423657381972074672,
                                        'source_pixel_height': -7049759534875600682,
                                        'rotation': -220042678591878343,
                                        'virtual_nw_x_pixel': 916010591,
                                        'virtual_nw_y_pixel': 106299829,
                                        'virtual_width': 986638371,
                                        'virtual_height': 690491517,
                                    },
                            {
                                        'source_monitor': 7377222,
                                        'source_nw_x_pixel': -6324062387542127569,
                                        'source_nw_y_pixel': -5915468026491089141,
                                        'source_pixel_width': -6057456900273361974,
                                        'source_pixel_height': -656097025149265958,
                                        'rotation': -8416597006926841182,
                                        'virtual_nw_x_pixel': 715355624,
                                        'virtual_nw_y_pixel': -1621368730,
                                        'virtual_width': 1881767458,
                                        'virtual_height': -1855324554,
                                    },
                            {
                                        'source_monitor': 5916894,
                                        'source_nw_x_pixel': -934984772820269952,
                                        'source_nw_y_pixel': -5329298291830532972,
                                        'source_pixel_width': -1499252308389013229,
                                        'source_pixel_height': -2314126051340912381,
                                        'rotation': -5578027075149572145,
                                        'virtual_nw_x_pixel': 1740359732,
                                        'virtual_nw_y_pixel': -1535035490,
                                        'virtual_width': -470455593,
                                        'virtual_height': 1599244355,
                                    },
                        ],
                },
                {
                    'description': 'əɋΣƐЖѴпҴȫӕơ@/ЬӕςȕҞҥɶëǅºǃĈβɠщӾŞ',
                    'monitors': [
                            {
                                        'identifier': 8307792,
                                        'width': 1119210770966271189,
                                        'height': 5037202772910814062,
                                    },
                            {
                                        'identifier': 2984630,
                                        'width': 1958015798189292413,
                                        'height': 2185681139028380426,
                                    },
                            {
                                        'identifier': 3052564,
                                        'width': 7621225783377226216,
                                        'height': -6574795116096631198,
                                    },
                            {
                                        'identifier': 1821742,
                                        'width': -5296143833413117085,
                                        'height': 3403776653380431954,
                                    },
                            {
                                        'identifier': 6752555,
                                        'width': 4566300746882659321,
                                        'height': -7048998437199916638,
                                    },
                            {
                                        'identifier': 5697583,
                                        'width': -2776054444658335695,
                                        'height': 7496054887794272768,
                                    },
                            {
                                        'identifier': 5922052,
                                        'width': -6403208477943471916,
                                        'height': -397510572606834740,
                                    },
                            {
                                        'identifier': 3795630,
                                        'width': 2043773653400030818,
                                        'height': -8097253887477413021,
                                    },
                            {
                                        'identifier': 1462296,
                                        'width': -4352278826197076209,
                                        'height': -5381628764676466364,
                                    },
                            {
                                        'identifier': 4572437,
                                        'width': 7089231579255682201,
                                        'height': -7365188229133856720,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7412059,
                                        'source_nw_x_pixel': -7062154424086544439,
                                        'source_nw_y_pixel': -6848810577608592182,
                                        'source_pixel_width': -9176409958186684013,
                                        'source_pixel_height': -4115149397503057838,
                                        'rotation': -5163875361449076298,
                                        'virtual_nw_x_pixel': -1596447956,
                                        'virtual_nw_y_pixel': -235206736,
                                        'virtual_width': 202262454,
                                        'virtual_height': -1593242312,
                                    },
                            {
                                        'source_monitor': 7840396,
                                        'source_nw_x_pixel': -868939222319324982,
                                        'source_nw_y_pixel': -4216028918649857782,
                                        'source_pixel_width': -3941596822155746070,
                                        'source_pixel_height': -7216219982225466138,
                                        'rotation': -2230303885182605269,
                                        'virtual_nw_x_pixel': -453358261,
                                        'virtual_nw_y_pixel': -1999056933,
                                        'virtual_width': -1721164579,
                                        'virtual_height': -1853945012,
                                    },
                            {
                                        'source_monitor': 7942049,
                                        'source_nw_x_pixel': -6986049656263980597,
                                        'source_nw_y_pixel': -2126254421515530628,
                                        'source_pixel_width': -6983603162167681572,
                                        'source_pixel_height': -5686310684413512301,
                                        'rotation': -7860447765438790484,
                                        'virtual_nw_x_pixel': 1011150385,
                                        'virtual_nw_y_pixel': 445140983,
                                        'virtual_width': 1790665155,
                                        'virtual_height': 1107797759,
                                    },
                            {
                                        'source_monitor': 9238417,
                                        'source_nw_x_pixel': -4117305509240873016,
                                        'source_nw_y_pixel': -8763694983114552121,
                                        'source_pixel_width': -8715212351949195138,
                                        'source_pixel_height': -1634311724571621311,
                                        'rotation': -1024799692053535793,
                                        'virtual_nw_x_pixel': -1993960330,
                                        'virtual_nw_y_pixel': -142002947,
                                        'virtual_width': -749764870,
                                        'virtual_height': 1669501960,
                                    },
                            {
                                        'source_monitor': 38000,
                                        'source_nw_x_pixel': -4071345750531018853,
                                        'source_nw_y_pixel': -8009922363736416651,
                                        'source_pixel_width': -4946213311022367440,
                                        'source_pixel_height': -5685102144884753338,
                                        'rotation': -682474545017105893,
                                        'virtual_nw_x_pixel': -1931184117,
                                        'virtual_nw_y_pixel': 804362870,
                                        'virtual_width': -966168501,
                                        'virtual_height': 799509493,
                                    },
                            {
                                        'source_monitor': 5526631,
                                        'source_nw_x_pixel': -6071084462546421838,
                                        'source_nw_y_pixel': -8961677230117687301,
                                        'source_pixel_width': -9198633838321438033,
                                        'source_pixel_height': -3853476205107223365,
                                        'rotation': -6197547225924895840,
                                        'virtual_nw_x_pixel': 700630582,
                                        'virtual_nw_y_pixel': 673491551,
                                        'virtual_width': -1963321280,
                                        'virtual_height': -1514252298,
                                    },
                            {
                                        'source_monitor': 4194961,
                                        'source_nw_x_pixel': -2422601489542276819,
                                        'source_nw_y_pixel': -7702707150093922430,
                                        'source_pixel_width': -4795361336169482408,
                                        'source_pixel_height': -4006711566751318393,
                                        'rotation': -6374381429633103156,
                                        'virtual_nw_x_pixel': 832404198,
                                        'virtual_nw_y_pixel': 1009899219,
                                        'virtual_width': -1248875473,
                                        'virtual_height': -1820241875,
                                    },
                            {
                                        'source_monitor': 3088551,
                                        'source_nw_x_pixel': -8248790672634880648,
                                        'source_nw_y_pixel': -5476943641388596956,
                                        'source_pixel_width': -8094001917457301623,
                                        'source_pixel_height': -7082620400329202998,
                                        'rotation': -7171245532632573575,
                                        'virtual_nw_x_pixel': 1841067181,
                                        'virtual_nw_y_pixel': 1199563528,
                                        'virtual_width': 323942531,
                                        'virtual_height': -655437701,
                                    },
                            {
                                        'source_monitor': 3222086,
                                        'source_nw_x_pixel': -1902769575815774977,
                                        'source_nw_y_pixel': -3749936604919570725,
                                        'source_pixel_width': -776048013335651338,
                                        'source_pixel_height': -1348204188048164703,
                                        'rotation': -6754437907432484650,
                                        'virtual_nw_x_pixel': 1114541199,
                                        'virtual_nw_y_pixel': -623128389,
                                        'virtual_width': -267634606,
                                        'virtual_height': -1500448702,
                                    },
                            {
                                        'source_monitor': 2704405,
                                        'source_nw_x_pixel': -2950388244475629867,
                                        'source_nw_y_pixel': -451425969360423991,
                                        'source_pixel_width': -3723443557988068373,
                                        'source_pixel_height': -409983946793443771,
                                        'rotation': -8729982509417207492,
                                        'virtual_nw_x_pixel': -798930934,
                                        'virtual_nw_y_pixel': -63139609,
                                        'virtual_width': 143660810,
                                        'virtual_height': 1133702330,
                                    },
                        ],
                },
                {
                    'description': 'ŦķɻѓОʛwȥȴҧĀ\x9cϭsˑ\u0381`Š҃ҍŶɴрƘƞēӪԂөԋ',
                    'monitors': [
                            {
                                        'identifier': 1085425,
                                        'width': -2271486445217893676,
                                        'height': 6800687481638411742,
                                    },
                            {
                                        'identifier': 1522940,
                                        'width': -5234860546840451735,
                                        'height': 8775038733242902513,
                                    },
                            {
                                        'identifier': 7083338,
                                        'width': -205407625683291613,
                                        'height': 6886126127141088779,
                                    },
                            {
                                        'identifier': 2761882,
                                        'width': -7907803305181998940,
                                        'height': -2913207152132354338,
                                    },
                            {
                                        'identifier': 4844009,
                                        'width': 1992887694926563187,
                                        'height': -388967370129644180,
                                    },
                            {
                                        'identifier': 4339468,
                                        'width': 8317940013804954388,
                                        'height': -7775688735436357873,
                                    },
                            {
                                        'identifier': 414906,
                                        'width': 8542513984435957439,
                                        'height': 4340378365130843659,
                                    },
                            {
                                        'identifier': 8328381,
                                        'width': -4086985321456082711,
                                        'height': -6188076849534849072,
                                    },
                            {
                                        'identifier': 6570515,
                                        'width': -2579527185013575264,
                                        'height': -7326212708695060669,
                                    },
                            {
                                        'identifier': 6876287,
                                        'width': -3710363766320795220,
                                        'height': 5829250650132780385,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 176514,
                                        'source_nw_x_pixel': -6386874464979242310,
                                        'source_nw_y_pixel': -298686037703079070,
                                        'source_pixel_width': -6235166348103621234,
                                        'source_pixel_height': -1296095127825664746,
                                        'rotation': -1897795003216626728,
                                        'virtual_nw_x_pixel': 1773489273,
                                        'virtual_nw_y_pixel': 233437780,
                                        'virtual_width': -1711267054,
                                        'virtual_height': 1322343806,
                                    },
                            {
                                        'source_monitor': -948163,
                                        'source_nw_x_pixel': -7696740084159136682,
                                        'source_nw_y_pixel': -184842519283819467,
                                        'source_pixel_width': -2460013144721016245,
                                        'source_pixel_height': -2770052338970614218,
                                        'rotation': -3380493768158448012,
                                        'virtual_nw_x_pixel': 1603937509,
                                        'virtual_nw_y_pixel': -1575170628,
                                        'virtual_width': 1820677974,
                                        'virtual_height': -1219497816,
                                    },
                            {
                                        'source_monitor': 3260325,
                                        'source_nw_x_pixel': -1612545819675911435,
                                        'source_nw_y_pixel': -6987606730014875703,
                                        'source_pixel_width': -6712015589206721736,
                                        'source_pixel_height': -4173208862611690162,
                                        'rotation': -8669208088148963077,
                                        'virtual_nw_x_pixel': -1720560180,
                                        'virtual_nw_y_pixel': -366798010,
                                        'virtual_width': 1803680525,
                                        'virtual_height': -578003397,
                                    },
                            {
                                        'source_monitor': 6403125,
                                        'source_nw_x_pixel': -2017754913343210549,
                                        'source_nw_y_pixel': -4358543830236669383,
                                        'source_pixel_width': -3105855195776424580,
                                        'source_pixel_height': -2816594926336846894,
                                        'rotation': -3599040589746046407,
                                        'virtual_nw_x_pixel': -945715538,
                                        'virtual_nw_y_pixel': 260577031,
                                        'virtual_width': 70885069,
                                        'virtual_height': -1031705160,
                                    },
                            {
                                        'source_monitor': 7555512,
                                        'source_nw_x_pixel': -5961420685018577566,
                                        'source_nw_y_pixel': -4541172849224588192,
                                        'source_pixel_width': -6384333353888627048,
                                        'source_pixel_height': -4899310739157225975,
                                        'rotation': -4646068745773053036,
                                        'virtual_nw_x_pixel': -198382574,
                                        'virtual_nw_y_pixel': 1632234107,
                                        'virtual_width': -81199811,
                                        'virtual_height': -1232493312,
                                    },
                            {
                                        'source_monitor': -454803,
                                        'source_nw_x_pixel': -5816138338424476719,
                                        'source_nw_y_pixel': -8466102813506065031,
                                        'source_pixel_width': -4443388258822935937,
                                        'source_pixel_height': -670802045838611750,
                                        'rotation': -1876287416860804814,
                                        'virtual_nw_x_pixel': -1511456888,
                                        'virtual_nw_y_pixel': 1072300324,
                                        'virtual_width': -379591435,
                                        'virtual_height': 83126269,
                                    },
                            {
                                        'source_monitor': 9170773,
                                        'source_nw_x_pixel': -90354002208400372,
                                        'source_nw_y_pixel': -5003988736615117155,
                                        'source_pixel_width': -6155697699811053402,
                                        'source_pixel_height': -7961154765728521459,
                                        'rotation': -2353255447321068140,
                                        'virtual_nw_x_pixel': -1422638978,
                                        'virtual_nw_y_pixel': 713349938,
                                        'virtual_width': 44876464,
                                        'virtual_height': -1737152325,
                                    },
                            {
                                        'source_monitor': 5071508,
                                        'source_nw_x_pixel': -3797111434565235593,
                                        'source_nw_y_pixel': -4401772960223146630,
                                        'source_pixel_width': -4605067462295341933,
                                        'source_pixel_height': -2530310105966392256,
                                        'rotation': -8021158382043516919,
                                        'virtual_nw_x_pixel': 572827390,
                                        'virtual_nw_y_pixel': 198576164,
                                        'virtual_width': 123120316,
                                        'virtual_height': 1545421131,
                                    },
                            {
                                        'source_monitor': 7462957,
                                        'source_nw_x_pixel': -4719937476023639950,
                                        'source_nw_y_pixel': -2845724236591250591,
                                        'source_pixel_width': -848983019582008867,
                                        'source_pixel_height': -3344317693147417333,
                                        'rotation': -6235546512229842615,
                                        'virtual_nw_x_pixel': 1732551789,
                                        'virtual_nw_y_pixel': -1578081696,
                                        'virtual_width': -283796525,
                                        'virtual_height': 725721614,
                                    },
                            {
                                        'source_monitor': 8184995,
                                        'source_nw_x_pixel': -6500634469320023966,
                                        'source_nw_y_pixel': -8250260855489369671,
                                        'source_pixel_width': -33988295676347203,
                                        'source_pixel_height': -6720837682163026207,
                                        'rotation': -5503035191503383116,
                                        'virtual_nw_x_pixel': -744032943,
                                        'virtual_nw_y_pixel': 1066481685,
                                        'virtual_width': -747436280,
                                        'virtual_height': 1291447261,
                                    },
                        ],
                },
                {
                    'description': 'ʫԈтΫԙˬŻ\x92ʮĶPѓŇűuАƟͽɮʱȜβϯ|Ӳǵΐùgî',
                    'monitors': [
                            {
                                        'identifier': 344160,
                                        'width': 5779381154654972722,
                                        'height': -7056179005831932309,
                                    },
                            {
                                        'identifier': 5929995,
                                        'width': 2593394546654318820,
                                        'height': -1830648766819619479,
                                    },
                            {
                                        'identifier': 6961921,
                                        'width': -2912115358631366686,
                                        'height': -8607299899356578538,
                                    },
                            {
                                        'identifier': 1786867,
                                        'width': -1248989735082242481,
                                        'height': -4467746810601753065,
                                    },
                            {
                                        'identifier': 1194145,
                                        'width': 2907032696111745726,
                                        'height': -3567611937615722356,
                                    },
                            {
                                        'identifier': 2318801,
                                        'width': 2512252179626078882,
                                        'height': 4904789824590790947,
                                    },
                            {
                                        'identifier': 2114402,
                                        'width': -1097093336734786700,
                                        'height': -7982340471529448062,
                                    },
                            {
                                        'identifier': -493994,
                                        'width': -5649193934731665101,
                                        'height': 6179846424527508751,
                                    },
                            {
                                        'identifier': 1626567,
                                        'width': -8239950040997964451,
                                        'height': 992117274391539973,
                                    },
                            {
                                        'identifier': 7036964,
                                        'width': -4167900811128225654,
                                        'height': 2648415712139797103,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5570389,
                                        'source_nw_x_pixel': -2659289037907732344,
                                        'source_nw_y_pixel': -8072748962508931805,
                                        'source_pixel_width': -3613656070144221161,
                                        'source_pixel_height': -2498573078906815542,
                                        'rotation': -1621275319408328353,
                                        'virtual_nw_x_pixel': 1050153476,
                                        'virtual_nw_y_pixel': 1651511785,
                                        'virtual_width': -412122714,
                                        'virtual_height': -1828678735,
                                    },
                            {
                                        'source_monitor': 2372148,
                                        'source_nw_x_pixel': -6681796916224070829,
                                        'source_nw_y_pixel': -5461756291040030356,
                                        'source_pixel_width': -3597660296529869223,
                                        'source_pixel_height': -866225218608892971,
                                        'rotation': -1103447332780305572,
                                        'virtual_nw_x_pixel': 1069850869,
                                        'virtual_nw_y_pixel': -765107395,
                                        'virtual_width': -1027707410,
                                        'virtual_height': -869995332,
                                    },
                            {
                                        'source_monitor': 9151513,
                                        'source_nw_x_pixel': -7294066177230073335,
                                        'source_nw_y_pixel': -5572320061485212645,
                                        'source_pixel_width': -8512205115588955253,
                                        'source_pixel_height': -11869903017912391,
                                        'rotation': -3426202679392205984,
                                        'virtual_nw_x_pixel': 865338366,
                                        'virtual_nw_y_pixel': -162849140,
                                        'virtual_width': -1058920499,
                                        'virtual_height': -380442710,
                                    },
                            {
                                        'source_monitor': 8664180,
                                        'source_nw_x_pixel': -5452031547924220011,
                                        'source_nw_y_pixel': -1578033144187811850,
                                        'source_pixel_width': -2496502917607385007,
                                        'source_pixel_height': -38846393142317643,
                                        'rotation': -2546514516736286067,
                                        'virtual_nw_x_pixel': -1350750092,
                                        'virtual_nw_y_pixel': -11573817,
                                        'virtual_width': 25478496,
                                        'virtual_height': -1354425267,
                                    },
                            {
                                        'source_monitor': 8329024,
                                        'source_nw_x_pixel': -1515702453745905180,
                                        'source_nw_y_pixel': -8007843035326142070,
                                        'source_pixel_width': -9210718040108634453,
                                        'source_pixel_height': -2909445723420542016,
                                        'rotation': -6508652745378559045,
                                        'virtual_nw_x_pixel': -1309622548,
                                        'virtual_nw_y_pixel': 1885336383,
                                        'virtual_width': 972219571,
                                        'virtual_height': -324578705,
                                    },
                            {
                                        'source_monitor': 1710982,
                                        'source_nw_x_pixel': -3809484854097524698,
                                        'source_nw_y_pixel': -769843213298548886,
                                        'source_pixel_width': -6685225918046243878,
                                        'source_pixel_height': -1073257820372502552,
                                        'rotation': -7873703104884308556,
                                        'virtual_nw_x_pixel': 838260619,
                                        'virtual_nw_y_pixel': 119366951,
                                        'virtual_width': 714533818,
                                        'virtual_height': 1329911217,
                                    },
                            {
                                        'source_monitor': 4425338,
                                        'source_nw_x_pixel': -5188634266634241080,
                                        'source_nw_y_pixel': -8621351618764404973,
                                        'source_pixel_width': -8309630355514939562,
                                        'source_pixel_height': -3555134217774318477,
                                        'rotation': -1711686672473734427,
                                        'virtual_nw_x_pixel': -793263848,
                                        'virtual_nw_y_pixel': -1093964813,
                                        'virtual_width': 1422051657,
                                        'virtual_height': 1970161826,
                                    },
                            {
                                        'source_monitor': 9984782,
                                        'source_nw_x_pixel': -6625132714105076471,
                                        'source_nw_y_pixel': -4162204203120018191,
                                        'source_pixel_width': -23932346641256099,
                                        'source_pixel_height': -8794467911955333463,
                                        'rotation': -2595571678185280247,
                                        'virtual_nw_x_pixel': -274180450,
                                        'virtual_nw_y_pixel': -1462208978,
                                        'virtual_width': -197402704,
                                        'virtual_height': -1034821949,
                                    },
                            {
                                        'source_monitor': 598961,
                                        'source_nw_x_pixel': -7697575821803112095,
                                        'source_nw_y_pixel': -5578808545181458269,
                                        'source_pixel_width': -8455464414599894007,
                                        'source_pixel_height': -2153942323476885968,
                                        'rotation': -8280636364169053595,
                                        'virtual_nw_x_pixel': -616238030,
                                        'virtual_nw_y_pixel': 654054525,
                                        'virtual_width': 1918668225,
                                        'virtual_height': -450335713,
                                    },
                            {
                                        'source_monitor': 3271872,
                                        'source_nw_x_pixel': -6459516742448945493,
                                        'source_nw_y_pixel': -2562765987535877030,
                                        'source_pixel_width': -163599974065471355,
                                        'source_pixel_height': -2660520710693272798,
                                        'rotation': -3981010705438451819,
                                        'virtual_nw_x_pixel': 778148142,
                                        'virtual_nw_y_pixel': -916174870,
                                        'virtual_width': 1880536040,
                                        'virtual_height': -502616134,
                                    },
                        ],
                },
                {
                    'description': 'ȓѓ\x7fƽПԉʹkŊ\xadзȆͲѨ\x80Ԛ˄;ӯ#ƿȪʛǠ¨˳Ψȃлƭ',
                    'monitors': [
                            {
                                        'identifier': 4719441,
                                        'width': -3343759885403105922,
                                        'height': 5434255486968245776,
                                    },
                            {
                                        'identifier': -739683,
                                        'width': 9010067422557729708,
                                        'height': 7358366759987011736,
                                    },
                            {
                                        'identifier': 8659046,
                                        'width': 5687192059082739967,
                                        'height': -4360260030267176276,
                                    },
                            {
                                        'identifier': 8053380,
                                        'width': -6394801438007195296,
                                        'height': 7895635964483641944,
                                    },
                            {
                                        'identifier': -407074,
                                        'width': 5614128272945874624,
                                        'height': 3730246660519110875,
                                    },
                            {
                                        'identifier': -784852,
                                        'width': 1339941961214963688,
                                        'height': 519260635988191419,
                                    },
                            {
                                        'identifier': 7000235,
                                        'width': 1211057318909231090,
                                        'height': -2283761334955922404,
                                    },
                            {
                                        'identifier': 9556033,
                                        'width': 7892958095873360474,
                                        'height': 5770513361981041119,
                                    },
                            {
                                        'identifier': 2315715,
                                        'width': 304796632991378809,
                                        'height': -6969697819205765104,
                                    },
                            {
                                        'identifier': 6235513,
                                        'width': 8908320287980739067,
                                        'height': 3435608240561310347,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 775736,
                                        'source_nw_x_pixel': -327841277747696660,
                                        'source_nw_y_pixel': -1189482153162901411,
                                        'source_pixel_width': -7404760445590731769,
                                        'source_pixel_height': -6678412380003127927,
                                        'rotation': -2010582609091593963,
                                        'virtual_nw_x_pixel': 595202576,
                                        'virtual_nw_y_pixel': 566731177,
                                        'virtual_width': 1646701761,
                                        'virtual_height': 1774463971,
                                    },
                            {
                                        'source_monitor': 5280240,
                                        'source_nw_x_pixel': -404695247093228955,
                                        'source_nw_y_pixel': -8665763790070144777,
                                        'source_pixel_width': -8978303731916242991,
                                        'source_pixel_height': -1644146475062571548,
                                        'rotation': -116344691503396995,
                                        'virtual_nw_x_pixel': -1920246129,
                                        'virtual_nw_y_pixel': -173404080,
                                        'virtual_width': 983315311,
                                        'virtual_height': -1646022992,
                                    },
                            {
                                        'source_monitor': 4236398,
                                        'source_nw_x_pixel': -2787763645042324913,
                                        'source_nw_y_pixel': -9052999572548140220,
                                        'source_pixel_width': -1755647700501370515,
                                        'source_pixel_height': -4499814524908906935,
                                        'rotation': -370767307123450499,
                                        'virtual_nw_x_pixel': -855614530,
                                        'virtual_nw_y_pixel': 791531795,
                                        'virtual_width': 1374729141,
                                        'virtual_height': -1275647230,
                                    },
                            {
                                        'source_monitor': 8685747,
                                        'source_nw_x_pixel': -2523192125598784701,
                                        'source_nw_y_pixel': -2625934157312950371,
                                        'source_pixel_width': -1072912939601794164,
                                        'source_pixel_height': -6768376514141168688,
                                        'rotation': -7442125468986293368,
                                        'virtual_nw_x_pixel': -1528744339,
                                        'virtual_nw_y_pixel': -921554308,
                                        'virtual_width': 231738763,
                                        'virtual_height': 1655488035,
                                    },
                            {
                                        'source_monitor': 6078946,
                                        'source_nw_x_pixel': -6893162646157507936,
                                        'source_nw_y_pixel': -3973131400753502754,
                                        'source_pixel_width': -4486406533482528161,
                                        'source_pixel_height': -7484115338171473545,
                                        'rotation': -1683600617125139957,
                                        'virtual_nw_x_pixel': -699419258,
                                        'virtual_nw_y_pixel': 230650911,
                                        'virtual_width': 1694156929,
                                        'virtual_height': -1236244227,
                                    },
                            {
                                        'source_monitor': 9474661,
                                        'source_nw_x_pixel': -1127404409974856779,
                                        'source_nw_y_pixel': -8364372196523440366,
                                        'source_pixel_width': -3777110520214491546,
                                        'source_pixel_height': -1045765653492028403,
                                        'rotation': -4011786818019566936,
                                        'virtual_nw_x_pixel': 1988730955,
                                        'virtual_nw_y_pixel': -1467823755,
                                        'virtual_width': -1443158520,
                                        'virtual_height': -973118568,
                                    },
                            {
                                        'source_monitor': -176427,
                                        'source_nw_x_pixel': -2311005844593820101,
                                        'source_nw_y_pixel': -2549014659876593848,
                                        'source_pixel_width': -7313951313482607479,
                                        'source_pixel_height': -8296158433148717575,
                                        'rotation': -3582308886345543396,
                                        'virtual_nw_x_pixel': 1795955628,
                                        'virtual_nw_y_pixel': -1761525437,
                                        'virtual_width': -27378711,
                                        'virtual_height': 1517911269,
                                    },
                            {
                                        'source_monitor': -758231,
                                        'source_nw_x_pixel': -8762898878557903729,
                                        'source_nw_y_pixel': -2288565555103771905,
                                        'source_pixel_width': -157187145763744561,
                                        'source_pixel_height': -7322687942613766152,
                                        'rotation': -259132203193541849,
                                        'virtual_nw_x_pixel': -21556611,
                                        'virtual_nw_y_pixel': -1321907652,
                                        'virtual_width': 1372437675,
                                        'virtual_height': -1116862234,
                                    },
                            {
                                        'source_monitor': 5629687,
                                        'source_nw_x_pixel': -6156782209603520772,
                                        'source_nw_y_pixel': -9182597754836593439,
                                        'source_pixel_width': -6928107421220839223,
                                        'source_pixel_height': -4234269081164206030,
                                        'rotation': -6977262381174412807,
                                        'virtual_nw_x_pixel': -1816797671,
                                        'virtual_nw_y_pixel': -1206523090,
                                        'virtual_width': -1661055589,
                                        'virtual_height': -1589283222,
                                    },
                            {
                                        'source_monitor': 8670786,
                                        'source_nw_x_pixel': -7449973384591045487,
                                        'source_nw_y_pixel': -4981871478308045298,
                                        'source_pixel_width': -8377630597470015213,
                                        'source_pixel_height': -6223903848011456960,
                                        'rotation': -8976925375897859768,
                                        'virtual_nw_x_pixel': -82333034,
                                        'virtual_nw_y_pixel': -966992326,
                                        'virtual_width': 562561224,
                                        'virtual_height': 386800048,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 8652452,

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
            'request_id': 1468886,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 6512534,

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
            '$': 'ҧ÷ʓȢʳΤԕʿƷÇŏʬ;μƑŵiϿҀřʝəүȗ[ÒїŵѸѮ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 5969702288145498067,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 263836.47378972295,
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
            '$': '20211104:182838.825860:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӫŅ҅ǾØԇҢ¹kàû˗ϮyХ£ĝԖε³¢}Åɓя´\x89Łԑԇ',
                'ЁӨϦÄӽˆ˃WϒǭӘƦŦǑłɜĸʑȃоƶƣЋɸϘϷҬ\x83\x8eį',
                'ԕƼϼƃбӤδʝ\x91zȐò0ǁҍǒˠ¹ʫľ\u03a2˩3ӵırśʷӺǠ',
                'ŹұʦȑÁȣ2ҋЧԐˆŽҬˤÉʿѮɴĳļ˲hĖΡ˔ϕв´Ͳϒ',
                'ԬʿԕАӚʶ˵ƮӇ˛ƹÞɌςȏɆŀȥwӫ҂ˆѼɾӧ\x7fşF×˔',
                'ҷɰɫɮ\x7fӡ\x9cӂʥƨϴЎ¦ðĽǩОʁЮОȟ¢ʻĖȑҮŕʚƏť',
                '϶ŀ&ÛˍĈǊǵȘΡƎиřԁȡуðǏӥҏŜΧǸ\u0382ȻцэʄȒӚ',
                'ӸƖӵҊłӎΟԌĈÚΌƲUɛɦ°СΧɵғƨɻp÷ґɘƵkþϼ',
                'ΘҰÞHӥұВÈϙƹГҢԥŤKąÍӍĬʃƯΨʕİćҝǏưï\x97',
                'ȊǯԙǅϫŀċɊ϶hԨĮćªжŇʾхɩȤЯĎĻΠͼ,,Ѓɵ\u0383',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -7655899301890946174,
                -980939852808346710,
                -232639934768322517,
                8368515202482932086,
                6555078757204680400,
                -8899980308252512104,
                583496786769719247,
                932228570986943142,
                4844161011890727571,
                442827016422556678,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                837657.7037857029,
                355167.1866853546,
                463224.81991399324,
                452484.9606801163,
                39284.8221158158,
                751408.2689856743,
                475652.496563707,
                312641.2556386761,
                304814.66029495496,
                829686.1641006522,
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
                False,
                True,
                True,
                True,
                True,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20211104:182839.773439:+0000',
                '20211104:182839.791860:+0000',
                '20211104:182839.810398:+0000',
                '20211104:182839.827511:+0000',
                '20211104:182839.848351:+0000',
                '20211104:182839.869260:+0000',
                '20211104:182839.889021:+0000',
                '20211104:182839.908872:+0000',
                '20211104:182839.926150:+0000',
                '20211104:182839.948262:+0000',
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
            'name': 'ӛƆвƲɺJTȦð\x87ɷӑɳԠӱСЬš÷ãoҘʈHǲ\x8dɵǳΛΝ',
            'value': {
                '^': 'int_list',
                '$': [
                    3809614352625521140,
                    -5850544898490033875,
                    -9108589102456600250,
                    4912657374428106226,
                    -7094276843048791833,
                    -7644756274021480877,
                    7770642035328077359,
                    1974224476668577579,
                    -7430763307476478808,
                    -928854064730831117,
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ԅ',

            'value': {
                '^': 'datetime',
                '$': '20211104:182838.556889:+0000',
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
            'catalog': 'ΎʖӶɚ΅ɘÞwȿŚź˖ԓԓюȻқ҂ǻ҈ȷƺТĔzԎЖˉ',
            'message': 'Ԭ\x8bѸLÊƞӥ¼ɭŶǿɺѼįǩι˴ԋȇѹѠӿүQмĂƹξľӱ',
            'arguments': [
                {
                    'name': 'ϫȳҾǲҙѸӾчӮçћӫʬԩѠԉӖϵɦ',
                    'value': {
                            '^': 'int',
                            '$': -7195958231399455031,
                        },
                },
                {
                    'name': '\x83ҸΊϣʟəСòėĵȩ\x89ɜÊˤǶɫҩи<ĊΓϜӳςļκǃâͽ',
                    'value': {
                            '^': 'int',
                            '$': 8132480376959559651,
                        },
                },
                {
                    'name': 'ѸÿǍɂӇԖӢĝWÅҽƵĎȌΎͽȇг',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ҵʈɨaŀͳӅ\u0380цҘ\x90ѢҥȘВΑ\x8dΨϮþũʮŹƃōʡОˊͲͻ',
                                        'ȃβʖũБʱЧ\x86˰ΙɳÔʙ˩ƤљϨЍÏ³ʛЊӥўĲҢкɊ¡Ӷ',
                                        '+ˌǓǥԏdũ҆Лӯˌʪ´ҒȽ[ѓɋŲћǬ˯ǓͶˢñăξÓʕ',
                                        'čґĠϽҐϫ˞ƧѪǀʟͱʽЇɑȔϥ҂əȣǚʴɑşƚ°ϠˑρӦ',
                                        '\u038bϔ˫ʦZÄ˯ĖˈɺԂĚ˅Ѵ7Ԃ\x92˷/ΣŵSơэμԔˊ^àϱ',
                                        '6ĖˊƦȭƝƟ˃ΗñƭΤϙ˖eњҧʗɒ˷ЈˋǎӽиųɌ\x85ĺǉ',
                                        'ԋ҂ΥԪÿʽȅԫƁ˔=˦²ʙɉɑėЃɍҡϒĉϕʗʶʏщƪȠϑ',
                                        '\x90>ēǳċЈ7˫ͳʱ¼·ϏКſȒȬñįÈӲ˞ĭϻ˸Ѐ¼ҷΜȅ',
                                        'ǆƣŏǕś.͵ɱϨʠKʫlƫėƉԟԖȼФьʀƽδӼѳ˦wƞś',
                                        'җʶǩJΎˊ0\x90ӝϙ˛ӅȽŦ˞JǲìʊrΔП˒ϺьңщϊƱġ',
                                    ],
                        },
                },
                {
                    'name': 'ҦÝ˰',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ґ#µԭӁӧξ˲ƳɍƁ',
                    'value': {
                            '^': 'string',
                            '$': '\x91үвɾҩɥЧľѶԮǴǶǟŬӲуΩçԫŧςɢɞʐʪĐɲȟӍЛ',
                        },
                },
                {
                    'name': 'ĞȬ\x7fmɜŷk˔ƱԭȖ¬ɂŃ\xad-Kԩнӡ҇ќԅԝӟƖǾȃ¼7',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2451950799561636100,
                                        6921670219497992745,
                                        -8412326744124229650,
                                        -5044810666723025,
                                        -1327919881420654663,
                                        5178405592360926486,
                                        -5406271665639632886,
                                        1092679751428473005,
                                        -726346599146370963,
                                        -8602757320327008491,
                                    ],
                        },
                },
                {
                    'name': 'ĤщʳИödэƂÁ҇ƿӡȂʊɣǴΎ˹ǜȣԤ΄ɳƘёßŪϵȟk',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20211104:182837.356620:+0000',
                                        '20211104:182837.376147:+0000',
                                        '20211104:182837.394448:+0000',
                                        '20211104:182837.410619:+0000',
                                        '20211104:182837.429217:+0000',
                                        '20211104:182837.449870:+0000',
                                        '20211104:182837.466610:+0000',
                                        '20211104:182837.483738:+0000',
                                        '20211104:182837.500517:+0000',
                                        '20211104:182837.517811:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ԅӔ˹ЃNȼÃƌњ¸ǖԗΠԫ5Ǚԩ\xad\x94÷ȎǙμʄόɀ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        700477.4002496041,
                                        23800.5778329249,
                                        241450.75872682448,
                                        667364.4002998032,
                                        413437.66185134865,
                                        -49106.834835307556,
                                        739.7308385649376,
                                        668376.3860565407,
                                        992413.8710187187,
                                        383653.542417491,
                                    ],
                        },
                },
                {
                    'name': 'гϜƚӲţƬрʳɝǡŌŽϢĝѲ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                    ],
                        },
                },
                {
                    'name': 'ɓȥ;ˡѪĿ~ʋЇПϑ\x87²άÐŔǕӧãèʂɖzʿΥЃɪȐѴ҇',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        2463540457108415915,
                                        -1957904442654975289,
                                        -2080738422134002139,
                                        8271418001553010121,
                                        -188569359530301667,
                                        2320430465361274237,
                                        458413430083272925,
                                        3095702631907115529,
                                        7601730344672356010,
                                        -3100769996972612168,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ʞӱ',

            'message': 'Ž',

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
            'identifier': 'ѠƷСϠΟǎҠěԟYɆԒʣȪҩ\u0379ФΆǑŷ\u038bðT˹\x90ˆŐʧ(M',
            'categories': [
                'access-restriction',
                'access-restriction',
                'invalid-user-action',
                'invalid-user-action',
                'invalid-user-action',
                'file',
                'configuration',
                'invalid-user-action',
                'access-restriction',
                'internal',
            ],
            'source': 'љҝшɢÍțnĊřǲһőθΏ\x9eϯȴĿ҇ɸŶȑЈƇхѥˏŁȽÛ',
            'messages': [
                {
                    'catalog': 'ɟŶԇ²ƢɬɐђŰ˪үОԘǹȯĮίɂε_ǄͺҔȤΠ҄ҵ˴ƇŠ',
                    'message': 'ċǬҴѣUƳҎ˂ʹһѰ\u038dʭԂ҇ʹʙěÒϾѷŀϧʞԞġțǾ2ξ',
                    'arguments': [
                            {
                                        'name': 'ſӼaԁǔɝþΏƴƨʉȓцʢЅÝͳĒ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԍ\x8eàĠ˧ɕĢ1ƌ҈ƊҊűįÈƤʢòѺ.νĴΝǻʹǬΑÿ©ԗ',
                                                                            'ɬŨŵͰƕǥʮų\x80ÖΉƐΨЁɌɰȟ3ɁƕǐBŷȚӟӪǳȺºύ',
                                                                            'ЍζAǱ*ĭ8?ѰϧŝӇʸӼʘȄʙȞιI\u0379ʲҵŽŕžІ\x9dxʧ',
                                                                            '¦ØƹbŰЁυвɬԠ˃ʖњʦ¡ʮĘʆĝƟȩʜƥҘΚǏȒŊͳȸ',
                                                                            'ϾуӽĐʟƋȳƈδl&W\u0378ȼϙάǴλ\x97ǌлЏѶÀˆӖЫçĚˍ',
                                                                            '˦ëÈĈНϾŶƜþ/ϸѴȊқ_ӲΔïҫYѳȳьЖηƛ˫ķɬƀ',
                                                                            'ϪћӶԣŚ\x8cˍӹÔĲОʼ{ƇŮÁФˊЯАďȀ²є7ͷ\x80Ԋ˴ς',
                                                                            'ɿЕØψî˩ͶͱʸɿЙˮĔΗºʜ)\x82ȾҸӄ_ƦɪǅѾʴѿҟ,',
                                                                            'ϟψϦ˶ɏʧɇӫ5ͻѠɴ\u0381ˢȿŗҪӁΝԁӠ©ãĵFԐбü¿r',
                                                                            'ŷ¾ǭΪôšʏȷ˯ϪŽĝїɛ~ӬӳѷΌӽЭʸҋʨ˧˷Ϯ&Sƭ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӤД¤ϭяRҁȗwĪΌѸƱ¼ҽżŰȃpѵЭΟɧÚѶĠŻõИÒ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8554197767075795591,
                                                                            5829329925990257992,
                                                                            1966297189365610481,
                                                                            -827005353752263204,
                                                                            -2327706698601879711,
                                                                            -5676435060761309191,
                                                                            9109190147358327160,
                                                                            -2948119225679482614,
                                                                            3866399061967116448,
                                                                            -8619177432457025896,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÈѢ˶Ηδ͵ЦάҕʴӳфƧ˔϶˒Өк5ҰˑϊhːΑӆҴ\x8e҂X',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'г¯ƕĽˋV˅ƦRɴҬό«ӣϡɢФÀįďИВΞűļεԄŮ˺Ӛ',
                                                                            'ÛʻʯȢІŘ"žpϵΙЋȞҳţҟϬɬoǝ˙ōȠӵνːǛȄȑ(',
                                                                            'ʠȏХ϶ƎԉɀŔԆğĬŉͼŏÃ.ȿ҄aȕÞĀɲɑ\u038dԩÀĐƴƽ',
                                                                            'ƆđʨæћʰŹ¤ƥʼђÇʖϾĪ?ͼɳæКĔϦζѝYƆ\u038dҔ\x98γ',
                                                                            'ЀɯȝżÚ2Ԟƌ~ÖĺѫȿͰɸǝѠʾʴūΨǱ¸ïҩʃξϵѩʚ',
                                                                            'ҖΰŖŨӖӿðìӋ>S˛ÅЧ,ɇД]˯đѷ˵ŵƶѲӲ0ŕȢȏ',
                                                                            'ҳɥʀȇɳөФ\x90@˰ɰƔ&ʊǙХ˫ÚȳƆѱѳˏõǕƦԒԝƶ\x89',
                                                                            'ӧӎԂßӮɯѷƋļ҆ϑΘʪ\x94ƏØɻűMΓgЩщҢțԃдʢӯǡ',
                                                                            'лEϲьҘҾΈȤȽȮƐǦƯϾņªӘфŠƍУƥĂț\x81ɯð\x96Φň',
                                                                            'şёĽ"ˣӄѷȿϸԧͳĬҠҕгӁȘƵгŐÀĝϠҫ2ϒʸƘψƠ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΣӤŝŊȋƻɾΦƠӽЌűŪĹĎ¶QʨѦǰɰÀ\u038bˎXӈƢҗԪҁ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1789359299624701220,
                                                    },
                                    },
                            {
                                        'name': '\x8bȥξĐìÏƸŐā',
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
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӓžɲѲҊΫͷ\x81ŒΤ҅ӎɮ˔ɞϼxŦ҆ǷΠƐЮĪͼÆάυŤǄ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182826.975223:+0000',
                                                                            '20211104:182826.991646:+0000',
                                                                            '20211104:182827.008857:+0000',
                                                                            '20211104:182827.025061:+0000',
                                                                            '20211104:182827.041459:+0000',
                                                                            '20211104:182827.058504:+0000',
                                                                            '20211104:182827.075254:+0000',
                                                                            '20211104:182827.091831:+0000',
                                                                            '20211104:182827.108549:+0000',
                                                                            '20211104:182827.131411:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɑυɖ\x9būʷ\x93ȍӯƎϣ6ÿРuǋ)ɶƿ:ӴƿɧžìÉЮ\x86Ƴ˯',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7396440003780213878,
                                                                            6640960536053031363,
                                                                            -301429165390715317,
                                                                            -4762489761607210258,
                                                                            1757581816836439584,
                                                                            7325885871454539899,
                                                                            3643808852965354424,
                                                                            5279815967042478495,
                                                                            -2699320797424153789,
                                                                            8819445409622363776,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЕΎӍ1Ϩ\u038bɔљԗǤDρƤʃɭʇŎǂ´ƙȿԅȂħOµɑ҃ёǮ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4812411754965481722,
                                                    },
                                    },
                            {
                                        'name': 'нИƁñφӕʢʧ҃ˁҽƎөmǧϓҦʊҿã,ʣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӼǗUϟωŚӈȲЍ±ЯʱϡƱǲ˦ƶѡЦҰț8ӉτчҢϚ2ÉƠ',
                                                    },
                                    },
                            {
                                        'name': 'ƿԞľԐ˪ΞT҆ʻԁ¥\x91řýғŽ\x99ϨȈģʖħ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˴;Ѓ\u0382ɛӋŰɨѢú\x9dőȚѴĮˤÌιμŢȜƷ\x90+rϗ¸˼Õ\u0378',
                    'message': 'ΊȶǑÆȑΏ£ʭ9ƣϜѽãѻŰÉȔ˲ǱËȷʩɶӍъ7řϷŰԪ',
                    'arguments': [
                            {
                                        'name': 'пԏƣЪĬƠ˸ȳ\x8dǥԒӁľ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -84509.77980973203,
                                                    },
                                    },
                            {
                                        'name': 'ΨǂИԋӈɏŠĊɔьʒʆƺɹƂшϛȼҕĩ[ϫćӠҊʡșǭԣѫ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 438095.69101821375,
                                                    },
                                    },
                            {
                                        'name': 'ǍЄΰƜ\u038dѣͽǿQʓӕ˓ƾ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'чʼɩʷűŗǚҎҜ~ƾʢũBХЄ¹ǞИɡ\\Ǝɠɀ¥ɪɗ´ǭƊ',
                                                                            'ĜǘǊ>ŨÒ(řȫòњǔиȉԃƿšŁХ\x95җԒƊȁ1҆ϥł˞ř',
                                                                            'ǩψɆƱ5ɨΞ\x8aϳӸ¬TɍΡ0ѼȐΗԐ\x94ǃRŭЌìȖєǨŃƥ',
                                                                            'ɞ)ȉҡҕ*tɝǖϋz˫ӾƁƣѕȣйдӸEɟΈ\xadAҩҕѼɨ\x9f',
                                                                            'Ҁҩӗ\x93˫ǓǰiɵåɮġҍҸι˷Ŕɲ¸ʿȢ\x8cTd°Ɏ˯Ÿƪʑ',
                                                                            'ӳƢȇеƸӤǆ\x97Θѯϕʘ´ϲзǽˡԤϯӅ<ƱϱӬʉԆ)ʑҹ\x8c',
                                                                            'ŋƭÊǃȯ$GȿәȆϬ\x9e\x95)ˠɰŖʭԑР9ȸǭбԕ÷Ҽqúŵ',
                                                                            'ȊЖßŃǚԡϕʇһ˓Ȓÿéп^ÒʆҺë±ºàԐʮűŇÎʱͱŅ',
                                                                            'ǦǣoaԅȽÃԌǖҪˠ\xa0ǂѐĕjňΚЗeͻĚ¸ÐΉѓ˳İƥ7',
                                                                            'ШǞŶłǗʤϙΘѱQұ¼ГΌ!âÛß\x95ђξsnʑΥƑįż˝Җ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЪŚ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7856397774210148656,
                                                    },
                                    },
                            {
                                        'name': '÷Πsȡōǥǉȳ˧ʏĢ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ˏӄƁǌȵӵʎÄyϤӬ´ΫҔԔΦ\xadөŦë\x7fɸɋƊѢǅɜ˺ŪЛ',
                                                                            'ŖÐоȹáʛəϐϠӌʬƶ_m΅ơƩĨϻħΊƴˋǵјҀƝѫϗŷ',
                                                                            '?ӦęʎʚvԖǑʖϣȹЎáňιŅ÷tþƫͻCòƖκѣйϠʱ\x9a',
                                                                            'öҕȨΦɧŦʳҨ5ӜǡAæҕөˋƀɏʰįˮÈωІkеǳΡɆĞ',
                                                                            'άϸѴfԣȮʢþЈƷʪϒӮýөūśϻɧςʿYËЁ\x96\x8cȨǭŉŁ',
                                                                            "ʻ/ʜ·ŚμԑјϠȖ¼ϢɦIӂǉԞÐΑɱѴ|'ȠêȣϕɨѓȂ",
                                                                            'Ӫ.ȿѢØƚZŌӇΪɨҸ¹ѾӃǞϹ˪ϊϽŬ˙ĐʔȨһϞĉҥԡ',
                                                                            'Өԃ˂˨ȜſΥђŤđƃzөɮҖѢ\x8fɨρȃ×ҖǐβњŪԐSƽǃ',
                                                                            'lȁʠɳԊѦиҟİŉѩСȚÍİԚьҔ˞ԍǙ˙ʊр ӲщɸɈɑ',
                                                                            'ǌԨ`ȣW\x94ԧǉжԅҩʩĨȝȑƇґ`\x87\x9dÀɇÈҊȵąАξН˝',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϭџлԉ\u0381lƽРξ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'čÅǛӊȫѿћɐӡȝɻΤ\x83DԍhУӒηбƂжШȟԄ¶аЕθ˚',
                                                    },
                                    },
                            {
                                        'name': 'ӟİѨΒȗɫмԀâѽв˽Ä19ȡʨĈӢ˕˄ƝƃûѶԦÑ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 735825.3589132945,
                                                    },
                                    },
                            {
                                        'name': 'ʉPəԪȅɗǀɔӫ[Әң®Æ¤ʗØĭÃÒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҤĪԈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 222605.88832772826,
                                                    },
                                    },
                            {
                                        'name': 'ĺŕʿʯЂœƤӠ;ĒԌɂǚhǒҧǐѪҺˣӀƒļ\x9cюѱʪŷ`͵',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182828.991246:+0000',
                                                                            '20211104:182829.008352:+0000',
                                                                            '20211104:182829.025683:+0000',
                                                                            '20211104:182829.043156:+0000',
                                                                            '20211104:182829.059894:+0000',
                                                                            '20211104:182829.076697:+0000',
                                                                            '20211104:182829.093567:+0000',
                                                                            '20211104:182829.110055:+0000',
                                                                            '20211104:182829.126154:+0000',
                                                                            '20211104:182829.142362:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ώΨē\x85ʲőbǙ~6ŮZȫѰɂŶȝѶѴƻĻƸύö÷ґӝʱɐҩ',
                    'message': 'Ӗ˰§˧˖CŠҗɒ»ѿȔ¨ҔмΦƇѧ7aϭӪΨ\u0378рîáŶǭƭ',
                    'arguments': [
                            {
                                        'name': 'ˏĩ+ʼ˗әӆŚл˛ҍҘưѾнҨǔЊΉƀ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 192333.17855072703,
                                                    },
                                    },
                            {
                                        'name': 'ɑщАʋŚ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'һqǤȯˏ\\§ζͻʻОVúηwÞȟȢÄԅЁȇȊɉɉ|ʈĲŧʔ',
                                                                            'ĐŮŻō\x85ӵΔţÕιǎѵӉŊĠĢʃ;ЈÂķЭBϖ˃·ʬӀѩә',
                                                                            'ʎƘɌԄӶҾ¸ϻQą˜оЖŞȂÖ®ԑШϒMԞǱЩʸѠɣñËω',
                                                                            'ϜʃƆi˒ƄŵФƱΟϪӜϱӍ\x99įͳɒȐҿӴΐƇφҬӭԭAõ˞',
                                                                            '҈ɔфýëɠЬnЂɼĞyƁťȤЮ¢ҡКƅŒĽȄͼ·ːƠ·Őѡ',
                                                                            'ʅј\u038dɒΗȷ˔ʨцǺүʩɦԕͿýÐʏϜóϟΥӧ϶ȍƢҲ-<Г',
                                                                            'ϋĢΎƊĴŊ^äһĔKӦԡƴϫԠԍԈƬʘ˳ŜƔʭÐƭȼųб.',
                                                                            'ˮӂǋƪGǵǜрʎŮĪΊϒԍō˧Ӆŝ\x84¬ȆӰơȀŦTÍßĺІ',
                                                                            'ŐĥЍ˵˽÷˄˘ȂľѼѾŽU\x8cȼӡ7hŁƚưԠ[Ăûѓί4Ӵ',
                                                                            'ȜӜǧĝÿ-ǖҗςΚӹԏȐ¬Ԟҗ˛ӝϓҥũϴѳǭвFōʆXԫ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ηŉэĺě(ɌеƗҤ҄ӔEҠќƐŌʁ}!ӮΝЂĪӆȜĴ˸Ӆю',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1883559715208605844,
                                                                            -5974439495561293375,
                                                                            1040643049417838752,
                                                                            -2233744528418475641,
                                                                            -8225546263024260920,
                                                                            2720705769056453092,
                                                                            6297451315482534907,
                                                                            5362284002800916589,
                                                                            3124128083482505532,
                                                                            2738270374941317356,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӟ´Ɗʆ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɮҖǚвùϜѾ\xa0×¬ũԢЄ˪Ł<Ů˫³ÑŭͽʆÒЯĨӶƾńO',
                                                    },
                                    },
                            {
                                        'name': '3ΐ҅ĈɞǛýϒiҍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ª4MŏƤRŻǈΣ¿ҝɰȞОŠƄǊƆ˩ǖοΚϥĎТʹË¯ė˭',
                                                                            'ɬˬѢȗҐMД˰ȸљҬŨèΪŃǋ\x90˚ƚŐμѵƭʢЃ#Ɠƍˁѡ',
                                                                            '˖ǐЈˉ{ʶ˕ŌǝǙoņȄЄЎǺʰƼ¬_ǿϕѓӂӄǭʟΪÁҌ',
                                                                            'ʑJŲю˧ϜƄĒVƔƝŁŹѯϽǗŦӟɒӜČ˨əНʴ\u038dŕƍŤɭ',
                                                                            'ͷӗȸʻ.ˆȋϿ#ȥѥҷҫżŧːˈȘ!қˑϽΤөЏ\x80ǡԅЭ«',
                                                                            '¦ƈȭԗʄ˶Ǿ˅ĂӲÛŒԠńАѾр˳]ΖϛɹåϭӃʏüùǼŸ',
                                                                            'ŊӟʮȂż\x89ҋο˶ʈ˻ďȝȘȥӣцˑзҬҘƶÝҗүҵxÖʏͰ',
                                                                            'ʀ¶}ЯǛҧƗњԭϞяÎˈmԐñˮԗƢʂĀ±τВКÇˑΖĿБ',
                                                                            'ҐδɣήϿcǔȝ\x95Д\x97ȅƧåԂƊŴʑĢξǉÂԞʦ\x7fΈ˷ԫү҆',
                                                                            'Ӿ҃ӓƢȖʑӱѤz-χȽə\x97θɒĻʄńдԖɒͷɒÒӏԘҨ`ƥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʙƝQϣģŌϟɂʯˢÆ˧WęӲʷƬӣчɂʷȌȡ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3930307165455588120,
                                                    },
                                    },
                            {
                                        'name': 'ĀŝŻˇрҎǔɣˍñȰ\x93řǧѽԎǎʝ˨óӥâƇ9ԭȘɚј¬ɱ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'x˩Қ\xadǔˈӴƹнϔȀϫНǸʚŖ҃ǿԕˬӯŬ¿vĄЦдǒΠΘ',
                                                    },
                                    },
                            {
                                        'name': 'üǮιpģЌԖŖӮ¨˯|кȦĥбèƋɘśȎĄñŉɍý7',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǾΣҫԉʄɝСŚШȳЏѮȈ¥ȰȓđУľȕԌg|˨ˇӗͼѵ\x86Ƙ',
                                                    },
                                    },
                            {
                                        'name': 'ӢѢԈŒөȸƦʨь\x9d/јĠ.Xӳ˶ț\u0378ӟкZäéŵЕԡ¤ī˳',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '}ЀʪϑѰϹſѳİ˙ƙʧȦȎ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'DӓŠˍҨЈȦǼщˀ]эˆЗtFɰƧҿ@Ϊʫȓć҅ǼĿsʪʞ',
                    'message': 'ϣĮ6IƸ˛ͺӃΰԇˊ\x82ҠđЎðґʫŸʸeǧɁЯYɃϢΝȓɪ',
                    'arguments': [
                            {
                                        'name': 'оʃǚέȍӶǄɄlӸˤΟˉĝĮɜƪ\x9eӾ҂ƘхÔњд%ȰsɅȼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 778044.8483265901,
                                                    },
                                    },
                            {
                                        'name': 'ϻʩɛ§ʭɜȞȥҭ$ɅķԙϑçӮ\x84ѝŃ}ʆƕԎδǓӇ˛ʳŇϜ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 44739.05469831792,
                                                    },
                                    },
                            {
                                        'name': '£ƕgĄѸҠ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3934656893619550554,
                                                    },
                                    },
                            {
                                        'name': 'ýӋĞÿçäҟѝ!ԑ«ҷʤЍҠͰG\x96ԤĿɆ=',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            671103.3111235844,
                                                                            993529.0127005524,
                                                                            819572.7451705025,
                                                                            716530.0210921785,
                                                                            94932.34704889759,
                                                                            665375.3662149917,
                                                                            448645.29514047503,
                                                                            65467.14386697704,
                                                                            688593.0781942734,
                                                                            646217.2542942395,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¤ńǙǬȞ#GϮōѨðѬÕȵΥĞϦӺv]ų÷ΈϮŬǗΊΔɘň',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182831.238484:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȧѥ˰κ"þgȵĞб\x88҄ˠ"әȳϗϣϚƂ\'ōPμǬ\x7fǬԟĠø',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6356378229136503284,
                                                    },
                                    },
                            {
                                        'name': 'ɑýèӿƼĤЌ¯ҢҘЋJ_ӱɀ˟҅\u0383ɍуɹ˶ʥ\u038bʕΠǝȘ}Ѥ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\x95¤ȶ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȵʼΪĿӟѢȔȯю҃˵\x8cϗҘĖżˍŲGŕӣҝôΤ˅гζÍǺΜ',
                                                                            '˫ƻT-őɮʩˇŘίӂΥòѮƐΡƨł×žɃȭѐ %ϦƱԀȰʦ',
                                                                            'ÌІЌɔϚωàχȻƖӆ҈ҞǱ\x88ӒǋӛưʷϷ˞\x8cvȖAѿʗхϑ',
                                                                            'ɄɘĤȕľΦKΊdʧǏԦ\x8aϣӈԢЖĉăоόӅÀ<^ɏċƽԔȎ',
                                                                            'ʕƨʪ\x7fї˜Ñ\x8d\x99ӾʮǍÏХ˺ώżο®ţѶЁԟѥӪȞΫŪЬѸ',
                                                                            'Ҷӣмϟ\x86ӇΈʢsì]¦HϾ\u0380ĖɴѮѝŰ\xa0Ӟ"ԁɬӭ ĹƭѶ',
                                                                            '˫¾ɳtĘҁ½ўԣǸſưĿŰѱ³ɿMѫŉȗҪӊʼӓœɁʦǶϗ',
                                                                            'ʚɟҵǫƸӴĨ,ġ˅ԊгĉƏǒšԨ ¹ѣΥơӐƪ@рʊўāǨ',
                                                                            'ԗȉϵȠƉÏǡӕŁʹËоǄʘa\u038dȔµùpӬБĕź¸мˬÍųɀ',
                                                                            '©İɢЕ¤ǙÂʵ&ƃѐʊĸ=ʚçȈѲíĢ$Ʌҭӫ_\x99ʎDˣÓ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '"ԫԡɝǿӂ[Ѵ˔§ǭ˵ϔԅӘä\x8bӨΎԫϕĦěĥhӿѥΟ\u0381ƾ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20211104:182831.881199:+0000',
                                                                            '20211104:182831.897309:+0000',
                                                                            '20211104:182831.913386:+0000',
                                                                            '20211104:182831.929766:+0000',
                                                                            '20211104:182831.945924:+0000',
                                                                            '20211104:182831.962167:+0000',
                                                                            '20211104:182831.978625:+0000',
                                                                            '20211104:182831.994833:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ψ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ԞѾ˷ñϑʍөȴȠѥԆӓãqȼӶ~ɦϰѩϧҜ\x89ԜϠ\u03a2.ŕρ(',
                                                                            "ф˨ãʁUŹ˨ɦĈҲ˳\u0383ʊӟЍԚұΛĭϺo^/ö'ĤѺ=Ǵǜ",
                                                                            'ӆғΣӖɋʬƠ±Ԓǯ"Ł«ģӒ˔ѱǂȝξѠԟ»ˋťŁн/ƥU',
                                                                            'ɁǯÛaͺ˵ŽԐ2țЯЖ˖ђƽ˲ӻцФȏƂáËƬΆǣ?ʸɜȢ',
                                                                            'Σ˦ƐΘԣҧȝӣǐ§*ɶmȿʎȊ[ԧǡɾдőӎђҏҪШҘϞ"',
                                                                            '¡ҖŬ¸ˈНүӜӬǳƅϹˈƨӍюϰҮpΞЈŁrӑĸºҔƽĐЯ',
                                                                            'Ԁ¯ȝǨˍӡǳľĕԋƩЏԙȤЕǰǏǈůƉÔɒ-5ӵΑźѕδϐ',
                                                                            'ǘҝ˶ȖљĪƯ˅ˀ\x9fª˵ªŉϏӉǵûƛϣΆ4ҶђӟӮ˞ԦÀΠ',
                                                                            'ƷԃȷƯæʠ?ӢԃÔǙˋΤƼͺű҇ԬMȅƊĀ³ĵĩӭɐ˴PC',
                                                                            'ȈӊЎȎҙԡ˘ПӶҒìϋōϗɍ8ǬΫ\x88ԏϋүŭadɶĤȎ҆т',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'В×πïҍƻ\u0383ƹǃ¬',
                    'message': 'ƶЕ¨ωρķȴА\x93ú}åȗбϽźHʿӏВЊˆЮɴΫ͵Ɖ˴ÿŧ',
                    'arguments': [
                            {
                                        'name': 'ÐƅǟΙU˼u˺ӔʶƗ҉ǧ˚҇ŞѓƙŪ\x88Ȭ\x80àүҨˊʻƧǷȱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182832.387764:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ќĞʻԖdƏǎ\x8aʝ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1829175682465253588,
                                                                            5237219948161301505,
                                                                            -4113158646295190619,
                                                                            172661533637206136,
                                                                            -4107189270412676005,
                                                                            -1912978046093843043,
                                                                            -4597153778710022392,
                                                                            1470947135602395128,
                                                                            1381090606163370566,
                                                                            -6720351279182878225,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŗϣöīюɚҗÃіǯȬɟȳЩǻфĜԢǁːèЙѪҧŚ҄KÚϷӌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'œϖӣГ˓lΛѽк˴ҋ˷ъǕ˷ʂʐơΆčи\x93τ˘ƩĵQҙÒԄ',
                                                                            'ʖ;ȀЕƪϼЏʖǍğŸϊҡͼԭ¡ϬҔʋјĮſϱԥʾȓѣԩԡϳ',
                                                                            '[һ$ȦMӀàԙѫĢʸϠϴΉʼΜƬwrΔШǯʻЙϾʾƅɧԁȜ',
                                                                            '\x95ǋːɖ8ĪíЗҸĞЂӧЄʼ¯ɤŏȦȬʘҍΏŊϟĞÜò˞{\x80',
                                                                            'ķÃЊԙɌ<ӂņǌ/(ʣӾæ\x99ʔӔԂǸÎѴɽ˾÷ΝӻѻМѲϗ',
                                                                            'ɰԚʦ°óӉȟ҂ȿȋʫүÀǯșҖ\x94ũѪÂţ\u0383ЃԦέӯ˲ǠӃϷ',
                                                                            '-ÞӑĖȧǠЎʗƍϪĦԑǯőԀҊťЃϏãΎЅƖ¨ũԀӁĤ҈α',
                                                                            'ƊȜſb˶ŇƻœԪӻљƕ˞ѱψʈěɺϮѤˋԢǓbÛʂĐԔ˨Ӏ',
                                                                            'ԍӵíқÅ\x8a²ҕʎҟҋϝɀ\x80X\x87ЅπŲȣ˳Ӣȓυč϶¨őĲђ',
                                                                            'ȿǏƏŹņ;ȝǵӘƙħ×Èʠ˾}×é˱CȲ;eЯˆӜʨŬϨó',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'БėǣÂϡБƷƫˁ¯ɩϦ¨џҙ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 187425.89177460974,
                                                    },
                                    },
                            {
                                        'name': 'СŔɖ·ƖƚŁӧΓWñˋǴbńμϔDǬ\x92эǈԢϻЖӫɭԥЙä',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3457458733411267596,
                                                    },
                                    },
                            {
                                        'name': 'ȶιSҢϢ¨хЇĆ˃ʲƙÍĳ\u038bŰˣHĲюӰҿƖӸɱ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182833.147759:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ѧөěͿǄЋ˥ǢǼ^',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Мǂ¿ƌРʬсƺ\x90)ϛǚΒXϊĞӛШèÑůςaΓԗ϶оǎ\x8dŸ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20211104:182833.498813:+0000',
                                                    },
                                    },
                            {
                                        'name': '¯Μ2}ǜˑŕqŞԩe\u0379ƬɲҢȸȧϼӥɆаңȀʎҘΙƩȘɀʇ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¯Ҩ\x95ǥ˶ʯҳȧӦѝϷƷ˝ȎʻӜΞʃЋS҄СŦљҷ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 944955.5961909625,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƊOσŚȸȿ\x94įЎĺÿǍŘʂΩ#ǾϣɶGǦƸǉƣ˽ѯŨĆńЎ',
                    'message': 'ҎʳhʞČĐюÒƌӔҘđʭͺßͺ˼éӒҧҲˡÖˀЬ+ѥԩǤî',
                    'arguments': [
                            {
                                        'name': 'GкeğÔƯb9ΟѳłӔϾƥҨÆ<',
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
                                                                            True,
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӊС˪l\x99ΛƥԂĖлÍњɁȉ[ʸΌϳ±Ӵƻƚ"Hάе«ûˏ\x85',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            388855.306273397,
                                                                            580490.0386930617,
                                                                            342965.53646223183,
                                                                            188921.3519195033,
                                                                            115722.73055813639,
                                                                            929725.7573912053,
                                                                            858821.518997938,
                                                                            96794.5709715414,
                                                                            589192.2934690607,
                                                                            642693.3371490974,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԢƢǳΚÆλºĺͲɊúċҤ˥ʺҏě\u0378',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 934055.0188309549,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǧѪӨΕλɺ0ª1ƉǒϫȐĎØѶѻħɽ§ϬЀʕмљǎhȰˇǁ',
                    'message': 'ȬŌZ:\x85Ε˳ҾɛлΆӦ˞ϑђ½ΫͲƲʺΌӨӽǐģƈĩʑȲҁ',
                    'arguments': [
                            {
                                        'name': 'ɘĉҀȣƂɵӟΖ\x87´τ=ҬҩǩŀưɏŃҤ%yҽ,ʈьoԮÜÅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            95200.83556748083,
                                                                            342689.31012789096,
                                                                            495087.62542049796,
                                                                            29579.07796797836,
                                                                            326014.3336855941,
                                                                            799046.5591848004,
                                                                            743648.1682737838,
                                                                            74495.39525833467,
                                                                            621506.8235473459,
                                                                            801666.1235252413,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'SŞǾҸԒĪѥ¤ǸӐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŽоӨӸ\u0381ǉt˶ԨYпэÕƺˡʸ˒HХũȟԗƇĸͰҦˊ˩\x87҄',
                                                    },
                                    },
                            {
                                        'name': 'ǃԓһvͲӆɮξōҼ\x93ԢѤ\x9fǓԨƩŗҔςŴʤζàNΣιȆ˕ņ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǁΨʎʹԞưʟЏĕгѹɠϭɷɒƫϿƗú΄ЊʇȎό¶Ѭǐǔ°Ϲ',
                                                    },
                                    },
                            {
                                        'name': '˻Ġ¨¿«ԡφʽœъǥР´\x97у\\\x91Čś˽ŇĉÓќǫ˝˰ЌĀú',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            944988.463452982,
                                                                            810159.4419533728,
                                                                            775171.1180593144,
                                                                            271371.62924902944,
                                                                            609800.0677981746,
                                                                            682784.2106146562,
                                                                            206526.3310219813,
                                                                            -77256.19659347252,
                                                                            586714.5230791282,
                                                                            249909.80529787816,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'rǲƚԠ\x89ȍĴȎʢBďƔΉɔȎҁȖČǡˬťʈІNȸӞљԀӋǅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѫżʙ*ƭȢƝq\x83ˋɋɥȘȆџȦ˺αҒɌаȿѦ¿ͰέÒȟӲ¬',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8046027771589858722,
                                                                            6551744082459457000,
                                                                            -3197823686007767517,
                                                                            7728797619863809400,
                                                                            6365131272094833585,
                                                                            -3515201024111801019,
                                                                            -647918033801686887,
                                                                            -240525544005089207,
                                                                            -1453578259435087822,
                                                                            5153361625704126618,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӱч',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɶŰýȁӠƴӯǟɊ˵Ы˘ȵԄǾĢҍIĸ*͵.üÕҳʭӄ6ӎЋ',
                                                    },
                                    },
                            {
                                        'name': 'ŰҲ;ϫͰʕŭʆȌɐʞьɼǡ;ɄϮғԐԑǨ΄,Іү§Пӧӳ¨',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            333488.98149829573,
                                                                            592027.6483298709,
                                                                            905204.6857651218,
                                                                            429559.85092635534,
                                                                            36043.38654140313,
                                                                            692428.9211391399,
                                                                            345501.19592126197,
                                                                            558384.1555137595,
                                                                            876550.4356093782,
                                                                            792837.9869121104,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͺϲòǃǋнѣΘҭΤɱǜѓʆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3992549614558644134,
                                                    },
                                    },
                            {
                                        'name': 'ӝɝˀřĚuͷɿŀτƏɁʨ˳ϊӹǖŦϕԛ´ίϷұѽԄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ї˽ԇµ˘ԏäӔиΕʹ\u0381ȮњţħѫЉƆƒӍȾӡφʚɴYȒϘб',
                                                                            '/ŝñёĝũμĲĐҧɫːŁϏΟɆѽίȴО\u0378ɧέӡϕӔӜЀūƑ',
                                                                            'ȏȜďӂӖȸĖϩʝ˅ĆВˉĦmŧãԊѩҲɸ.ŷΊ˟ŪǐƈǭЯ',
                                                                            'ѤʳǙƊĆΞԆϫʦģǷŉңũÏƏѝʛȳӿьɼ\x86ҜҔ\x9dԨӊʖΑ',
                                                                            'ҷɎ(\x92Ϯ ѨǣЙːǹ\x83ǫǿҙŒɳň˩ѲҮщs\x94ƞnĤĻĀӭ',
                                                                            'Ӆ\x83ȟʶϙΈТқ+іѯӾťkѽǴŅʡƌӃƿҨǖҸѣͽϿɟɯȡ',
                                                                            'ĽŠtcЂĲѸ¥ɯȟŋѨ-ȴɆʑ·ǝ˶}ΧԚӒíŧˠΕӠ5ù',
                                                                            'ŮԪǘҫЅėɬ\u0381Σ&¼σ˺ѪɆқҽƸҖǃǍÈǍ҉ɋђɱйЊ\x84',
                                                                            'hчƚʥʩĝū˴ϼǒѣ¿ȣӱɛӊѽíһǸéʛш+ÑЎǺɷʫf',
                                                                            '\x8eҀɫʎ\x7fŉ˰ƫgɓ˘Ɉ˥AԠ\x8eӼʊӨȓ͵ϡ\x8fϔϸâϵϴ\x93ј',
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

            'identifier': 'ŨːùЭ˼',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'Ԙļ',
                    'message': 'ұ',
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
            'request_id': 1736727,
            'error': {
                'identifier': "ĖӇSuΔʇϏԢ°МǕʦǋэ'ňÛïОΝÌMȿ~ѓΌґχϴϭ",
                'categories': [
                    'invalid-user-action',
                    'network',
                    'configuration',
                    'internal',
                    'configuration',
                    'network',
                    'internal',
                    'configuration',
                    'file',
                    'invalid-user-action',
                ],
                'source': 'þϚΏƸЦПΫ-ЂŮłʞ˾ÙԂʦëԮĊӳӧǾԋϰƖŬҭĹѐǊ',
                'messages': [
                    {
                            'catalog': 'ÐӼǪŪƁ¹ÖфθƀǕǳϿnȂґӂ$č´{ӊrCЙ¾°ǂ(Ҩ',
                            'message': 'љҀɌѣԫɃΖдΫà\x82ѵĲаʂĕљȊ\x80ηжĶUΑƜɅΔdǍǲ',
                            'arguments': [
                                        {
                                                        'name': 'ɱϮlȟϡ˄k˛ĚĮУɱђëʟÖɚɆɵĴʞАѝĉʹȅѭȍǮӦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182818.050663:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȍ˫ˍӘӧő˂ӐЉώƃҩĩƒϠ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'r"ǻĿӨƎ\u0381QħȮӵԌԒƽ˅ǬѽǄҟɍΨ´HӏɡĴі͵4λ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182818.190241:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҙȦæ×¨ԘÀʤϹБʑЅ˝νŢвѿDҕʭԀ\x88Âưÿԑɫэ¥G',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ZēùǶƚǺʹ_θcĳĈĒ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4772633758477676001,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ʋƺ*ųϪȮȕǘͷ±\x7fЀ\x93ϹпƚǑŐҤлэєyÛӬх\x8cȡѓѬ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ȮѮϽѺƏ˒țʎѿɶȯǺǏŊΘÃŦŲŜƆГϤΧǫɑþɨÄpg',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ςҪΚʞҦ˳ÔĶɶǋăҸКɤǨӶӯ\u038bȩӕΩЫŶ˟ΉӬɚÖ&Ǻ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŕƤΗŚ®ҩʂȁӴŒǡƑҠˢɵ\x9fÉφµíùќЄϊПԡΕяћД',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x95;ϴȞӂαȇ$ԕͰcԤҕύɥˀĆǹǪȮȯқēɣ˃˄ɓҙ*\x9c',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӎЎʿ;Ϩŕ¶ʿԄɌԚÖάȽ³ӆЯȓɱыˁј˅ӼɐΩϮưʟΧ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 326104.6756956398,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǪӣӗĎˋǷΙɉŐɐ\x87ąС°ɇFŁˍɕŮ«ΙŖƶҦМ³ϯˤʮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʵŌȷҀ¯Ʌ|ǤɅͻƹ˘ҴwπʚҒʬeЖƥŜԚQҫĒƞèƻԣ',
                            'message': 'Ҋ˵·ɟб΄ǸӍŉҌ°ɮԦƊˉŻӘzɗΘϨȖϵÞɋȓΌϣǸĸ',
                            'arguments': [
                                        {
                                                        'name': 'ѶυəɈŇdР˵Ƚ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 989905.3777154321,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ăǲŦǃӘĩÖГʽÊȅč¾ÔҖ\x9a\u038d',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЛӮԒġͺÝŨԁςі\x82ÿЀŒѶǽʦșǓĩξԮȵɖōfғũӵɎ',
                                                                        },
                                                    },
                                        {
                                                        'name': '͵Ŏʕ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -40054.32911731322,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ѭǣǫ\x8cǱ$ŐҮ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ϗì\x92ǺϐΪ\u0378ԙΆϮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ä',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'hf˰őæώʿ˄?ƠȷÉɾРЁԦӶѴҴɔǬÔФ\u0381ΰԡșϽƞú',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ψŤχȲ·ŔΜԒŌˑɊƇɱɀdϥȔŏϵ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182819.309785:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĻȡѐϿƤȚԚþ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 60187286566937611,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖŌͺmğȓѰͺҍÊʡƹӏÈ҂ʄхìȩң˚[φϡzќǦϏδƞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 617030.430225929,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƺϙΖϥϨÖƵΚÑȂ8ζύƚΝȲӖĩғĆȹoŰÄÿҝԊȺҳʹ',
                            'message': 'ƊɼæȋԩȿԊӼ(4ʈãɭЈњǖǎшʘ˫ǐƾÇ˨ˍЖÆӷȊϺ',
                            'arguments': [
                                        {
                                                        'name': 'Ĥ˧ҍǎţ¹ÅĄӕƌԡΠǺӬˑɍŌς4ԕԫԂӔµĸаKѡÅ\x88',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182819.600279:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǤͻӜҘļYɂ6ɟӈÁž˶\x9b˗ŞǂǕМӁɪЋɝªŎ˳ũȍRϼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʯğѫŘȏ·ӛƑŌșϺŏͱʝ҅ʿƸġĶҾǲίĖƍȖŋ\x81ɦ˨Ŷ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¤ÂʀȵɤƤbνĜŌӟɯǿɵ¯VïΦϏýƦΰ˦ԩöҳ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9e˽ЧʐԔіз',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8770929328804266795,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔĻ\u0381ĹƑ¦¶όdїҔʲҼҕŐǑʎӁƢƶȊɝŪśĊтїԈʀ}',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182819.947432:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'эҫȝȵȀ\x95л',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 646977.2817105765,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҷtʏ\x87ΌļȌМɒǏԆ|ΫűÇХӦ˖ċдăɛ΅QЈϊǒѽς¼',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΏϓǙɀÒȹƣԝˁэӽж',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΞbϸΏǍԚѵѣԝЇҚѡ˙ȻҁЋɦҍК¿ѧΤhĲЍЌɶĎ>ŏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˏƘêǑǚųȐѷҏрԮɶ\x8cӚӛ\x83ҤΙrҁʹʞЩŉ\x96ˎʃӋɘϕ',
                            'message': 'Ȁʯʰľԁŋ˵UÅԉn`ǳGɀƓİ¿ΐȶgԚɃɍӔoâË\u0382ƾ',
                            'arguments': [
                                        {
                                                        'name': 'ɍăǜϲӞоÄӭĩ?җŭ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5230470526500044169,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'àԢτǋʽАXϒȦƃ`ͽ·\xadϑҸӰLέʠÏȅϾǟ\x94ƱH7џe',
                            'message': 'κҒĶѠǲǘͶъɇƆćѰš;đĖΝŴƷŘϬȾȞʃѢУɐǘʯԜ',
                            'arguments': [
                                        {
                                                        'name': 'ӲěǾŪрÒˇÛeĖѶԧҙяәɔԊ\x89Ⱥ˼ӭԃ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȩԄˇњЅϪɘђӷɊҖș',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'șǻҧ\u0382Ƀ×ΘĲпѝѢӮϭɳȘɹƳĎҝƺş²åɳJ°ơьѩŊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѐзƥȋĬó\u03a2ɂŠГȼǌѡʉɊȲϝԨMӷĔ·Ĳǳώɒ˒ǹǲ¸',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'әǦĩàķŨң\x99Ӝ\x9aωŖɓԑНҥɑϷӧύƯͲωѠ©Ƅӏςʴ\x93',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5200251305425579265,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾďзү˄қɒƃ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182820.850656:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɦ\x9bĕ¦ʊϒˬ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ġ¼ɰΉˈ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3701824287764280531,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΪǆӁ×Ĳ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĐƲeβƇӳ˾Ŋřȇ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5246439124641337684,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ĜŎɫ\x9bȴшӈʤӰǜʹˢσʨƣΜЖҽАԪрӣл|ί',
                            'message': '΅őjϏ¤ƳҝŹθ¹Ӝ\x91Ԏ˟ťɸʊƤѿͺϧ<ɔβß˃ϯ϶Дͷ',
                            'arguments': [
                                        {
                                                        'name': '¥ҷüťǏЭѣ\x8eϋȱǒӖӰӻϜІȆϺÙƵdżӅDˌɥЖͿOʅ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '^щͽ¹Ӎǒϗ\x85¶ЏȨ҆ɥʞȝ4ԇƋ8rYMʤ0аӴԂѪӦԩ',
                                                                        },
                                                    },
                                        {
                                                        'name': '>\x83ԡȇÅǸќ\x82hɆ¸Ϛψʷǰƃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѥԗΑͰԅŹʥ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'нǙďМςĊ҄Ƣɑ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˭\x8dɫưŇΝɀc÷ЪŤӋԏϨȹˍуȇ˶ǋνđåƠ`ʬтШɞҫ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӐГƲЯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ίʓԪϜ˵ŎĒӒҶϖ҅ɞѵОȶԔȡĂρː&јΰέѮȢ\x96җ'ê",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӥĘ"ҾȂӎ˻λФéË¿ũ#ʌǡϱ˱ӭcѺǨ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȠĲȘйǛþ(϶ӰԨӬζƊѤþŉѹǳϢ\x99ϓ\x8eǊʏ˂Ě҄ȩǰё',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 63116.32865875529,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʏǗԃΚ˥ЌǇÊþӼϮǟʶƲȤΪкӃˣɩԓҧƛӶ¨϶JɣŰ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 9076809180229557756,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϲƈçǸҕςμԤѧ9\x90џͺиµθΖύǴóȷӎƤǼːƿҥϴ¥ʼ',
                            'message': 'ԍәΥìȺýa˄ǨʑŧʗӵǐƢȔàĚȑĲӁϹı˻ьʼȲXtƲ',
                            'arguments': [
                                        {
                                                        'name': 'ѹƾә¹ξĻȇąҀǍ÷ԤԚϰǛӤˁлқЧ¨Ǡ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϣ~ӊȰϛ˓ҵŢʹ(',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˫ʏȰАϤœΈԍʢȀҲ˦Ӻњ\u0382ʘěϸ˕\x99ʬγєɟΚ\x8egοӤѰ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԙ˔ȉӰňŐFΫϽʜсԑѲɗҞԔȑʠ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'сԀάʰЛY˚ȹ΄ͲƂʰӉΏбԏѣĿɭяЄϧ\x84Þ;ѕɠƈʷ҇',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¡ɒÆóЏEƍїĒ®΄ԎĔŇ\u0383ӈƻҤʐЖʝÆѼŃҽƌ\u0383',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4548365543242576405,
                                                                        },
                                                    },
                                        {
                                                        'name': 'țѬu\u0379\x7fї˫ХԧeϳѣȺЪϫҍnЉԪЅĕżԣҶϧɣ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȺΒÅʀɺE)',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182822.540956:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƽɓ\x88ЃȐ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӂ˥ʡ²Ȃ҈ŸÂѯɂ˾ɱƬФ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'с',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʠ˖ӱKԏȵȠȋ˲¼шӗͻŬФоӵȬ˶ƳαʪĊ`΅Ƥ˩Ɯ&ѱ',
                            'message': '\x9fÃʛʑ\x80¨¹âЊё҄ϤɃ7ɫăȰ@ɈəæġеÙ/\x85ɸȎƔӸ',
                            'arguments': [
                                        {
                                                        'name': 'ÁӇRȟϨΧȏ3ʱѱġĺÕUł¹ԪĞǔ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182822.900122:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɈѸǵ²ŎęȏбíɲԃƕҜɨԀ¨ȉԨԆ!ûԧыȵ\x92β˂ƴӳƼ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'șȣɜɩѹ\x97˗hƏӪ˗ͲѶӃжԮ\x87V',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĝҼ¶ҟяÏ\x96ɣHuéŖͺБ˦ƁϿi%έТ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Η˗ǗȤ»˼ʊѫřðӅˌǁ÷żфưĴϛũŭ]ɼ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 796760.3366736827,
                                                                        },
                                                    },
                                        {
                                                        'name': '˵ӽğ\x90sԣªţɶ˞ΏŽăFzԔϢŸȊʧ«ϘΗ˫{үιԚʐʍ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 591524726900643765,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѠЛȎѢқˠ˳uĨĬ\x83ńƣ˷˩ҳWƠԍõxӟ(ʜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ҐɁҟȪЎŽƷͲɥͷɟĕԧͺóhƚȬĿѺґ϶҈ºȩũƹƄüÊ',
                                                                        },
                                                    },
                                        {
                                                        'name': '»ţμyɮϼөԗ\x88\x9c¾\x80ϱ\x81ƌƧўǤŽҭĊʮ*зȑЇ(ĉˀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\\ĚĝĞƞϰɯϧ:ºǃϯӈѩшĆ·˫ƅdʅjЫηώ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʟЮТǶή˱ЖƇªʹϦȅƒЃȖȱѣ>¼ϊĉˋϩ\x87ÂĬϿÿіʲ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20211104:182823.540780:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ŷƯȷƈˤξÚʵÿъÀ:¤қѮȦɊÇéŕѮчRЍʻҰĻżmɤ',
                            'message': 'ыµъŨҫϰÐӮϼΖťƻқ˵őìß\x8f\x9dѩѩήӴɨǾMӮѠɲǖ',
                            'arguments': [
                                        {
                                                        'name': 'Ҥư˾AąҒ!ʶ4ΤɚӟОŉϣˋɨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ӎϲĸɾɗщ^PƾeȚĔÇɆҷɚ¾\x89кKĦÉ\x8aɒӮϚϕˆЗí',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѢͿѮ$<ʰÑŅЄͽϖǌ>gΤ_Ћ5ƒĚȀЎοǁÈӃӓʗȥʎ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏĆԛΙR\x8fſƖƻǔůȠд|Љφŗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǰțˋʼ˕Ϗ\x96čӠƅϏ΅\xa0DϒƮΟЂԡwŅǬ¤œήťȁҟ˕ɇ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɈѢҗĹϧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '|7ΪòΣƜɯǄμљ˱ͱҳ˵ŧӶȁ\x93ҰʹɓȴšƵ˟NһˡЈΜ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˦Ĩć¨ǐϝ3ҀȢȡ\x8d\x9fǺƽ˽ӸԢϩӪé(ϣӚ¤К\u0378ӲҖśϤ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȞnѦɊ66Ŭƣ®Ğҟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄǫԪĿːԂÈĽâƻηǺҖχ˓ҼӈˆҥɨӈϜʲŨƼ\u0382:İТР',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "Ƀ'ӽЈçʼ",
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʈɫхǑĀɢʾʇwÙĂĆ§ƹЭѤԙ˅ȾҜ_ǳfȜΞ\x94҃ӡąƛ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ÀɖśŢTѦ÷PƉż˰ЖϨқкȸĉЮ\x8dфʻĈǇӳươ\x9fÃÍɻ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\u0383ǛʑlĽΥҐѢɚ˔ȑЩƭAʘιʯƦˀŬс˗ɴŉĽξʁ҄',
                            'message': 'ǣŖʚÁӑѓӜǵͺʀƒϠб2҈ЪʽϖԮ×cϘχʱŤЃĒӄˎң',
                            'arguments': [
                                        {
                                                        'name': 'ʗѫʲǠǂɯȤʊγΜӜԃ¤QȢAɮüѷʍΑȤѲԑѵˋâиɯ҅',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ñ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': "цhµ·žξ˞Ҡѣ'ԅИЋ˴à\\ƠǨǔîϿŁ˝NӶЫϪН;ν",
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3691697508289249534,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǺПžɑʴͲзϼü<υԘ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӽӃмĄӭψźĀӨӽ˹ŀŻЦʌ\x9aˎηŴЛΐʎɞ\x8cԧƍҟ\x98ϯ.',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǰ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӾȁҁTɊ\x9d',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'цʿӭ1ЉѯʖÛʕεЁгà˹ʡgя˄ЧϨ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¢Ɂř·ʛӤԥвщ©ʶҍàÚʢͲϊhȀǢ\\ѣǺѠBвː',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƙЍŶЮǌӳхͷ(ҌʹҖ˓ŴȲɘΦǈʠƃèЦКǮϮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'γСą˄һ˾ѠΘșȗrƱłЮȃҒƇÔгm',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ͼÄĀˡˑԩȍ:ɖåάɎȟЁ˚ҞӷпƫĢрύȈʽ\x8fϋƲΝԜƎ',
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

            'request_id': 1451064,

            'error': {
                'identifier': 'Ѕ²҉Äѽ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'Ͱρ',
                            'message': '҇',
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
            'nw_x_pixel': 1286370845,
            'nw_y_pixel': -63732901,
            'width': -8604309940897666000,
            'height': -6363532075158855156,
            'ratio_x': -1078768199898620137,
            'ratio_y': 6265506379798429680,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -1367969074,

            'nw_y_pixel': -1878376130,

            'width': -4575856582410552425,

            'height': -7045019647573371610,

            'ratio_x': 719821238026849094,

            'ratio_y': 5753377345340717019,

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
                    'nw_x_pixel': 1386460298,
                    'nw_y_pixel': -404135640,
                    'width': -2649802718969024004,
                    'height': -2290366449080625417,
                    'ratio_x': -5050592387297524017,
                    'ratio_y': -5249389366507172205,
                },
                {
                    'nw_x_pixel': 1216981475,
                    'nw_y_pixel': -1140013507,
                    'width': -2462520554370600653,
                    'height': -9091772300253291049,
                    'ratio_x': -7837472953588613020,
                    'ratio_y': 9220174644926358056,
                },
                {
                    'nw_x_pixel': 726273660,
                    'nw_y_pixel': -1535660661,
                    'width': -8511255835912813849,
                    'height': -4284808707064422738,
                    'ratio_x': 6480924489508053304,
                    'ratio_y': -7273433847926123629,
                },
                {
                    'nw_x_pixel': -600963061,
                    'nw_y_pixel': -1456578989,
                    'width': -916450868949954760,
                    'height': -2701570266896346740,
                    'ratio_x': 871497836074285900,
                    'ratio_y': -4858842157286886444,
                },
                {
                    'nw_x_pixel': -1013921207,
                    'nw_y_pixel': 147636245,
                    'width': -3242371499968299871,
                    'height': -7990744853723785914,
                    'ratio_x': -2560958980296309555,
                    'ratio_y': 3349499754417837470,
                },
                {
                    'nw_x_pixel': 1484370421,
                    'nw_y_pixel': -1761565906,
                    'width': -7025676222240967772,
                    'height': -2163570644365698525,
                    'ratio_x': -7400394709258381320,
                    'ratio_y': 1355804161813722193,
                },
                {
                    'nw_x_pixel': -1546946033,
                    'nw_y_pixel': -1522877565,
                    'width': -2163064838093316723,
                    'height': -209067367472937843,
                    'ratio_x': 9057922479288076931,
                    'ratio_y': -3178068107319584074,
                },
                {
                    'nw_x_pixel': 864311010,
                    'nw_y_pixel': 1048183697,
                    'width': -7922571350264632893,
                    'height': -7391366145286488368,
                    'ratio_x': 809896046579568579,
                    'ratio_y': 2733903782869234978,
                },
                {
                    'nw_x_pixel': 1363472688,
                    'nw_y_pixel': 1367136474,
                    'width': -3599403015520017588,
                    'height': -8827439596983487039,
                    'ratio_x': 5329365612831683314,
                    'ratio_y': 8800483861599107681,
                },
                {
                    'nw_x_pixel': 1148394874,
                    'nw_y_pixel': 268049452,
                    'width': -4962193921572999362,
                    'height': -3926311637621113431,
                    'ratio_x': 6341458007481390714,
                    'ratio_y': 8731879213245237876,
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
                    'description': 'Ǉ\x8a=ϺκϭˆĀԅʙɋSЬDÆǮªVθʲ3ͷğНǇј˻ǈğʣ',
                    'monitors': [
                            {
                                        'identifier': 6536358,
                                        'width': -3986662926978055144,
                                        'height': -488273844392354619,
                                    },
                            {
                                        'identifier': 3831459,
                                        'width': 3752446333375641283,
                                        'height': 6133758810160286584,
                                    },
                            {
                                        'identifier': 8285495,
                                        'width': 6920784959348299978,
                                        'height': -3486988949082742642,
                                    },
                            {
                                        'identifier': 8327844,
                                        'width': -3277821990499173408,
                                        'height': -5680760223578549965,
                                    },
                            {
                                        'identifier': 9022385,
                                        'width': 2027568222568913967,
                                        'height': -6692193653205651444,
                                    },
                            {
                                        'identifier': 5548176,
                                        'width': -7416847064656835401,
                                        'height': -4959788218659991415,
                                    },
                            {
                                        'identifier': 2225972,
                                        'width': -2900212951200242768,
                                        'height': -157317511407956856,
                                    },
                            {
                                        'identifier': 2476265,
                                        'width': 6364121599085680548,
                                        'height': -6377382148567132847,
                                    },
                            {
                                        'identifier': 1313495,
                                        'width': 8729077517122817576,
                                        'height': 7865935608706581841,
                                    },
                            {
                                        'identifier': 5745245,
                                        'width': 8115461195190060431,
                                        'height': -4181241451689288480,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1451786,
                                        'source_nw_x_pixel': -3278059598315959596,
                                        'source_nw_y_pixel': -6805094695332223017,
                                        'source_pixel_width': -5391644100698130907,
                                        'source_pixel_height': -5007239446882068102,
                                        'rotation': -2349982303451221069,
                                        'virtual_nw_x_pixel': 1973356068,
                                        'virtual_nw_y_pixel': 1295490408,
                                        'virtual_width': 447502548,
                                        'virtual_height': 1324660734,
                                    },
                            {
                                        'source_monitor': 6586807,
                                        'source_nw_x_pixel': -1787261581840858422,
                                        'source_nw_y_pixel': -8205027302364706053,
                                        'source_pixel_width': -5374519939243585906,
                                        'source_pixel_height': -3631076857990127781,
                                        'rotation': -969005070361037148,
                                        'virtual_nw_x_pixel': -808299771,
                                        'virtual_nw_y_pixel': -1938095942,
                                        'virtual_width': -1250244228,
                                        'virtual_height': -1139128637,
                                    },
                            {
                                        'source_monitor': -463712,
                                        'source_nw_x_pixel': -4029049530362940013,
                                        'source_nw_y_pixel': -162361604512359137,
                                        'source_pixel_width': -1725439025858007320,
                                        'source_pixel_height': -181572080448986853,
                                        'rotation': -4914185893130389552,
                                        'virtual_nw_x_pixel': 495380175,
                                        'virtual_nw_y_pixel': 1990976033,
                                        'virtual_width': -543101224,
                                        'virtual_height': -1030840122,
                                    },
                            {
                                        'source_monitor': 5356131,
                                        'source_nw_x_pixel': -5292701287537928592,
                                        'source_nw_y_pixel': -5755872049521261554,
                                        'source_pixel_width': -1567597549543276408,
                                        'source_pixel_height': -5862956640390345103,
                                        'rotation': -5416528035673977272,
                                        'virtual_nw_x_pixel': 1910221022,
                                        'virtual_nw_y_pixel': -126823019,
                                        'virtual_width': -1406909077,
                                        'virtual_height': 1705231344,
                                    },
                            {
                                        'source_monitor': 1040952,
                                        'source_nw_x_pixel': -4924263426825245581,
                                        'source_nw_y_pixel': -4844496487041890362,
                                        'source_pixel_width': -633075830674363563,
                                        'source_pixel_height': -8455703814723290677,
                                        'rotation': -3541961525427260160,
                                        'virtual_nw_x_pixel': -1620608331,
                                        'virtual_nw_y_pixel': -870309087,
                                        'virtual_width': 1372235314,
                                        'virtual_height': -564917243,
                                    },
                            {
                                        'source_monitor': 8256169,
                                        'source_nw_x_pixel': -4594438629481492045,
                                        'source_nw_y_pixel': -649843308122305649,
                                        'source_pixel_width': -9037874217096053179,
                                        'source_pixel_height': -1059945970192370910,
                                        'rotation': -3515295360223157225,
                                        'virtual_nw_x_pixel': 1809171980,
                                        'virtual_nw_y_pixel': 1810641142,
                                        'virtual_width': -622515776,
                                        'virtual_height': 1127937286,
                                    },
                            {
                                        'source_monitor': 9809378,
                                        'source_nw_x_pixel': -8374476312274687989,
                                        'source_nw_y_pixel': -7634160451963148046,
                                        'source_pixel_width': -2840677380084378330,
                                        'source_pixel_height': -6930720245486532346,
                                        'rotation': -3374753657064677067,
                                        'virtual_nw_x_pixel': 1213223665,
                                        'virtual_nw_y_pixel': 1438272816,
                                        'virtual_width': 1233047015,
                                        'virtual_height': 32837808,
                                    },
                            {
                                        'source_monitor': 183939,
                                        'source_nw_x_pixel': -4554638675112994183,
                                        'source_nw_y_pixel': -8058626239698301172,
                                        'source_pixel_width': -3974676742498082853,
                                        'source_pixel_height': -8080146818923336294,
                                        'rotation': -2120708908380289582,
                                        'virtual_nw_x_pixel': 153219229,
                                        'virtual_nw_y_pixel': -765739068,
                                        'virtual_width': 930909945,
                                        'virtual_height': -465470456,
                                    },
                            {
                                        'source_monitor': 8673533,
                                        'source_nw_x_pixel': -5329232525738365636,
                                        'source_nw_y_pixel': -8418488157064193628,
                                        'source_pixel_width': -5089516856851690191,
                                        'source_pixel_height': -4697820012643187742,
                                        'rotation': -3719245459942055008,
                                        'virtual_nw_x_pixel': 5911151,
                                        'virtual_nw_y_pixel': -886344166,
                                        'virtual_width': 37967886,
                                        'virtual_height': 674891586,
                                    },
                            {
                                        'source_monitor': 6335509,
                                        'source_nw_x_pixel': -5554159007514696658,
                                        'source_nw_y_pixel': -9069034111556695333,
                                        'source_pixel_width': -8034138140155680033,
                                        'source_pixel_height': -6785937144249579200,
                                        'rotation': -5238733676331750420,
                                        'virtual_nw_x_pixel': 1332437408,
                                        'virtual_nw_y_pixel': 233192166,
                                        'virtual_width': 599112931,
                                        'virtual_height': -1937628511,
                                    },
                        ],
                },
                {
                    'description': 'ʿ3ǩřӼȟʮƸҔʋӡʟŪŠɡʄԈƎɥԋŘƨɉˮ˴Ϲ¯æЛЇ',
                    'monitors': [
                            {
                                        'identifier': 5816488,
                                        'width': -1135861225034737641,
                                        'height': 6171398926058501775,
                                    },
                            {
                                        'identifier': 4768388,
                                        'width': 8932453353936510363,
                                        'height': -1483639573247046939,
                                    },
                            {
                                        'identifier': 8214161,
                                        'width': 7878730783497114351,
                                        'height': -7947319723890905507,
                                    },
                            {
                                        'identifier': 278893,
                                        'width': 4466196124084522736,
                                        'height': -1221836835676096033,
                                    },
                            {
                                        'identifier': 5184520,
                                        'width': 8450252914982298422,
                                        'height': 6796165824993605695,
                                    },
                            {
                                        'identifier': 1850752,
                                        'width': 1324510329274757245,
                                        'height': -543905377153309308,
                                    },
                            {
                                        'identifier': 8891025,
                                        'width': 4118985650517207517,
                                        'height': -4234912887908347404,
                                    },
                            {
                                        'identifier': 6658242,
                                        'width': -284478361039127600,
                                        'height': -4587945889911110275,
                                    },
                            {
                                        'identifier': 5259723,
                                        'width': 7272958692118240594,
                                        'height': -3995064132635490578,
                                    },
                            {
                                        'identifier': 9117289,
                                        'width': -5786285934339010493,
                                        'height': -1630044847060672480,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1339342,
                                        'source_nw_x_pixel': -431721425156035319,
                                        'source_nw_y_pixel': -7646691180621153340,
                                        'source_pixel_width': -3224736676785351627,
                                        'source_pixel_height': -7490754229064850149,
                                        'rotation': -925350995160377425,
                                        'virtual_nw_x_pixel': -1199775789,
                                        'virtual_nw_y_pixel': -1577771204,
                                        'virtual_width': 1470792169,
                                        'virtual_height': 1742008772,
                                    },
                            {
                                        'source_monitor': 6963288,
                                        'source_nw_x_pixel': -5924469387858191343,
                                        'source_nw_y_pixel': -8813011280365164414,
                                        'source_pixel_width': -8877954961688101000,
                                        'source_pixel_height': -2201299279268187549,
                                        'rotation': -7209251747854859063,
                                        'virtual_nw_x_pixel': 752822867,
                                        'virtual_nw_y_pixel': 1881495264,
                                        'virtual_width': 1005769968,
                                        'virtual_height': -300004798,
                                    },
                            {
                                        'source_monitor': 235936,
                                        'source_nw_x_pixel': -6501683799627438325,
                                        'source_nw_y_pixel': -2979270110181285616,
                                        'source_pixel_width': -2810345041085074647,
                                        'source_pixel_height': -7363171116741651974,
                                        'rotation': -6522114755408935130,
                                        'virtual_nw_x_pixel': 57892368,
                                        'virtual_nw_y_pixel': 1078164355,
                                        'virtual_width': 414127946,
                                        'virtual_height': 1360150796,
                                    },
                            {
                                        'source_monitor': 1965856,
                                        'source_nw_x_pixel': -2217338107285196869,
                                        'source_nw_y_pixel': -1661088396349434233,
                                        'source_pixel_width': -3344787359297414546,
                                        'source_pixel_height': -7434996805171799216,
                                        'rotation': -7030254031253024389,
                                        'virtual_nw_x_pixel': -1231274454,
                                        'virtual_nw_y_pixel': 637406359,
                                        'virtual_width': -1416457676,
                                        'virtual_height': -991173111,
                                    },
                            {
                                        'source_monitor': 1987909,
                                        'source_nw_x_pixel': -6987218105715972878,
                                        'source_nw_y_pixel': -385329337640502136,
                                        'source_pixel_width': -1243947770277274365,
                                        'source_pixel_height': -3259705890786830299,
                                        'rotation': -8297146108550792189,
                                        'virtual_nw_x_pixel': 974228079,
                                        'virtual_nw_y_pixel': -41226289,
                                        'virtual_width': -1377823996,
                                        'virtual_height': 527480770,
                                    },
                            {
                                        'source_monitor': 1077729,
                                        'source_nw_x_pixel': -1474037767476154377,
                                        'source_nw_y_pixel': -7359481611950701244,
                                        'source_pixel_width': -8267549264329488700,
                                        'source_pixel_height': -464599542429331455,
                                        'rotation': -8494557063299729609,
                                        'virtual_nw_x_pixel': -1081918710,
                                        'virtual_nw_y_pixel': 755813263,
                                        'virtual_width': -808989399,
                                        'virtual_height': -100560674,
                                    },
                            {
                                        'source_monitor': 4914911,
                                        'source_nw_x_pixel': -7346866579458988037,
                                        'source_nw_y_pixel': -90991708377036365,
                                        'source_pixel_width': -2944681110450839351,
                                        'source_pixel_height': -5278306901094452336,
                                        'rotation': -8182662420663031049,
                                        'virtual_nw_x_pixel': -1902010447,
                                        'virtual_nw_y_pixel': 1542937568,
                                        'virtual_width': 1983697446,
                                        'virtual_height': 394184958,
                                    },
                            {
                                        'source_monitor': 8635572,
                                        'source_nw_x_pixel': -6409498679587810738,
                                        'source_nw_y_pixel': -3179595295222121605,
                                        'source_pixel_width': -4716297143279666257,
                                        'source_pixel_height': -4748064241122245795,
                                        'rotation': -4949511319692286516,
                                        'virtual_nw_x_pixel': -96343947,
                                        'virtual_nw_y_pixel': -918299244,
                                        'virtual_width': -143323940,
                                        'virtual_height': -884348822,
                                    },
                            {
                                        'source_monitor': 3059054,
                                        'source_nw_x_pixel': -3908153587106540021,
                                        'source_nw_y_pixel': -681959507648301124,
                                        'source_pixel_width': -2710393901342757182,
                                        'source_pixel_height': -3528037153512464689,
                                        'rotation': -7278139807477815580,
                                        'virtual_nw_x_pixel': -1328340357,
                                        'virtual_nw_y_pixel': -439529859,
                                        'virtual_width': -1458998799,
                                        'virtual_height': 289885141,
                                    },
                            {
                                        'source_monitor': 6048007,
                                        'source_nw_x_pixel': -7764474037150448826,
                                        'source_nw_y_pixel': -3789284827191490598,
                                        'source_pixel_width': -5517346902648090776,
                                        'source_pixel_height': -5544032265729272500,
                                        'rotation': -4148736696253759426,
                                        'virtual_nw_x_pixel': -1414536106,
                                        'virtual_nw_y_pixel': 875632933,
                                        'virtual_width': -1598349174,
                                        'virtual_height': 570944138,
                                    },
                        ],
                },
                {
                    'description': 'ҀԑĂƐȚ\x96κԤҨƛ\x8f˷ʇӒǤLΈ˱ǃaȠηÔH˧ŠʭьɿЈ',
                    'monitors': [
                            {
                                        'identifier': 9643056,
                                        'width': 1403957995003575721,
                                        'height': -425509753655516255,
                                    },
                            {
                                        'identifier': 6567644,
                                        'width': 3184954515727253510,
                                        'height': -8061321437070987960,
                                    },
                            {
                                        'identifier': 4868186,
                                        'width': -1454149238186650411,
                                        'height': 4365820746993630500,
                                    },
                            {
                                        'identifier': 5853476,
                                        'width': 3372065745545764498,
                                        'height': -8054728858224311004,
                                    },
                            {
                                        'identifier': 3489611,
                                        'width': 7962942864650265942,
                                        'height': 1843052277701688110,
                                    },
                            {
                                        'identifier': 1982765,
                                        'width': 5378059412784660709,
                                        'height': -5313368202177708596,
                                    },
                            {
                                        'identifier': 6296864,
                                        'width': 4610890637158579159,
                                        'height': -411860451534257808,
                                    },
                            {
                                        'identifier': 455162,
                                        'width': -8831488919276530587,
                                        'height': -5838916430227789123,
                                    },
                            {
                                        'identifier': 132877,
                                        'width': -1463497331326100403,
                                        'height': -2412749025464954894,
                                    },
                            {
                                        'identifier': 6429244,
                                        'width': -4614925773159277812,
                                        'height': 4027807286243996862,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1918419,
                                        'source_nw_x_pixel': -4262252388181319048,
                                        'source_nw_y_pixel': -4769675804264354571,
                                        'source_pixel_width': -1023323894870711686,
                                        'source_pixel_height': -6777275424768804907,
                                        'rotation': -7973010164030599253,
                                        'virtual_nw_x_pixel': -1638197838,
                                        'virtual_nw_y_pixel': -1430522143,
                                        'virtual_width': -556541107,
                                        'virtual_height': 1437133387,
                                    },
                            {
                                        'source_monitor': 7995853,
                                        'source_nw_x_pixel': -4423993665797873962,
                                        'source_nw_y_pixel': -1855772393913629479,
                                        'source_pixel_width': -3503713222408850239,
                                        'source_pixel_height': -5083546982908458063,
                                        'rotation': -5339819751498949769,
                                        'virtual_nw_x_pixel': 1998069917,
                                        'virtual_nw_y_pixel': 240470675,
                                        'virtual_width': -1951213307,
                                        'virtual_height': -1055916193,
                                    },
                            {
                                        'source_monitor': 3332235,
                                        'source_nw_x_pixel': -493195408881046651,
                                        'source_nw_y_pixel': -7283618803302545497,
                                        'source_pixel_width': -7513780240307433805,
                                        'source_pixel_height': -3963379020816472345,
                                        'rotation': -6808671339058475904,
                                        'virtual_nw_x_pixel': -1151929317,
                                        'virtual_nw_y_pixel': -458518120,
                                        'virtual_width': -1083708120,
                                        'virtual_height': 1019616986,
                                    },
                            {
                                        'source_monitor': 2294946,
                                        'source_nw_x_pixel': -4734241065327235290,
                                        'source_nw_y_pixel': -4838524336520289642,
                                        'source_pixel_width': -5827047190849776217,
                                        'source_pixel_height': -2037184205608789982,
                                        'rotation': -3404773102753103117,
                                        'virtual_nw_x_pixel': 1091022256,
                                        'virtual_nw_y_pixel': 1839757917,
                                        'virtual_width': -1605326191,
                                        'virtual_height': 578479446,
                                    },
                            {
                                        'source_monitor': 244693,
                                        'source_nw_x_pixel': -8925793176831639086,
                                        'source_nw_y_pixel': -6225025172514089709,
                                        'source_pixel_width': -5890730469545421951,
                                        'source_pixel_height': -5905336340611811633,
                                        'rotation': -7844283718216383829,
                                        'virtual_nw_x_pixel': -445720849,
                                        'virtual_nw_y_pixel': 201975171,
                                        'virtual_width': 1471652813,
                                        'virtual_height': 1761778937,
                                    },
                            {
                                        'source_monitor': 5561967,
                                        'source_nw_x_pixel': -7690477527621047012,
                                        'source_nw_y_pixel': -7740648872549876812,
                                        'source_pixel_width': -3852269854837728658,
                                        'source_pixel_height': -1535961710208891935,
                                        'rotation': -3251062146619211354,
                                        'virtual_nw_x_pixel': -1797087012,
                                        'virtual_nw_y_pixel': 1019310696,
                                        'virtual_width': -313952193,
                                        'virtual_height': 218035911,
                                    },
                            {
                                        'source_monitor': 6244799,
                                        'source_nw_x_pixel': -6147528615701173071,
                                        'source_nw_y_pixel': -8823730798262057209,
                                        'source_pixel_width': -564186127730047498,
                                        'source_pixel_height': -8344145963722080615,
                                        'rotation': -1050919884609316790,
                                        'virtual_nw_x_pixel': 1051679995,
                                        'virtual_nw_y_pixel': -184400204,
                                        'virtual_width': 584226647,
                                        'virtual_height': -72880936,
                                    },
                            {
                                        'source_monitor': 1048290,
                                        'source_nw_x_pixel': -6054650903873413238,
                                        'source_nw_y_pixel': -9040899224521450184,
                                        'source_pixel_width': -6761937228756609287,
                                        'source_pixel_height': -5638603294167833635,
                                        'rotation': -3221105666305005975,
                                        'virtual_nw_x_pixel': 610979626,
                                        'virtual_nw_y_pixel': -1283889114,
                                        'virtual_width': -1322224919,
                                        'virtual_height': -1023996911,
                                    },
                            {
                                        'source_monitor': 26185,
                                        'source_nw_x_pixel': -2618279639833834674,
                                        'source_nw_y_pixel': -1749934186706628770,
                                        'source_pixel_width': -1042585441809719888,
                                        'source_pixel_height': -8701657424729563708,
                                        'rotation': -3071411261274497856,
                                        'virtual_nw_x_pixel': 947147915,
                                        'virtual_nw_y_pixel': 1686043042,
                                        'virtual_width': 641370156,
                                        'virtual_height': -1245933216,
                                    },
                            {
                                        'source_monitor': 4122384,
                                        'source_nw_x_pixel': -1526539598806375908,
                                        'source_nw_y_pixel': -3867936952516932800,
                                        'source_pixel_width': -7316423647791298576,
                                        'source_pixel_height': -468242929184794336,
                                        'rotation': -6798434828943435608,
                                        'virtual_nw_x_pixel': -1584229833,
                                        'virtual_nw_y_pixel': 418922065,
                                        'virtual_width': 1502101321,
                                        'virtual_height': 59482572,
                                    },
                        ],
                },
                {
                    'description': 'ʫ\x9c˹ϴ×\x9aůНȐϰ²ʢŔѴ´ǅ\x88Υť7˩һņнџϭɡɴоӰ',
                    'monitors': [
                            {
                                        'identifier': 2108654,
                                        'width': 2900871617563435928,
                                        'height': 7940396610680571903,
                                    },
                            {
                                        'identifier': 121257,
                                        'width': -6020729182315191494,
                                        'height': -6977214456403358771,
                                    },
                            {
                                        'identifier': -69772,
                                        'width': 1714947917185140446,
                                        'height': -6865530059593314782,
                                    },
                            {
                                        'identifier': 4511045,
                                        'width': 4364534535121225166,
                                        'height': -3235889346471569912,
                                    },
                            {
                                        'identifier': 4149707,
                                        'width': 5487646194605658860,
                                        'height': -6075192229488293307,
                                    },
                            {
                                        'identifier': -184434,
                                        'width': 5552027372119081431,
                                        'height': -246596573266580084,
                                    },
                            {
                                        'identifier': 3234854,
                                        'width': -8934455490053257463,
                                        'height': -7514449177874068970,
                                    },
                            {
                                        'identifier': 6895432,
                                        'width': 8212917637816067308,
                                        'height': -2336317675664292104,
                                    },
                            {
                                        'identifier': 3504092,
                                        'width': 4718320462752692579,
                                        'height': 6511938301767409635,
                                    },
                            {
                                        'identifier': 1885033,
                                        'width': 3347936397664300453,
                                        'height': 8118248654671127775,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5970940,
                                        'source_nw_x_pixel': -6018208039285989777,
                                        'source_nw_y_pixel': -1631057814338412913,
                                        'source_pixel_width': -7087909808100699477,
                                        'source_pixel_height': -5388007321657380530,
                                        'rotation': -7829351732452614327,
                                        'virtual_nw_x_pixel': 1049691722,
                                        'virtual_nw_y_pixel': 1589783711,
                                        'virtual_width': -1706654948,
                                        'virtual_height': -866342304,
                                    },
                            {
                                        'source_monitor': 7093732,
                                        'source_nw_x_pixel': -3944334517580710585,
                                        'source_nw_y_pixel': -7390371696743104707,
                                        'source_pixel_width': -3236140798233456041,
                                        'source_pixel_height': -2990823922549348756,
                                        'rotation': -1158536054411843206,
                                        'virtual_nw_x_pixel': -1514675095,
                                        'virtual_nw_y_pixel': -1651748418,
                                        'virtual_width': -1329425520,
                                        'virtual_height': -1991644976,
                                    },
                            {
                                        'source_monitor': 436324,
                                        'source_nw_x_pixel': -8391490693852335165,
                                        'source_nw_y_pixel': -4350835587581040080,
                                        'source_pixel_width': -5119442832359436576,
                                        'source_pixel_height': -455354400519499178,
                                        'rotation': -7682553035926133091,
                                        'virtual_nw_x_pixel': 1734694386,
                                        'virtual_nw_y_pixel': 214957228,
                                        'virtual_width': 1468476532,
                                        'virtual_height': -1251120718,
                                    },
                            {
                                        'source_monitor': 8333780,
                                        'source_nw_x_pixel': -586365333057824330,
                                        'source_nw_y_pixel': -725758691646760439,
                                        'source_pixel_width': -7820996361796992307,
                                        'source_pixel_height': -2554761730189349099,
                                        'rotation': -4166961428824471913,
                                        'virtual_nw_x_pixel': 166952577,
                                        'virtual_nw_y_pixel': -978422029,
                                        'virtual_width': 647794507,
                                        'virtual_height': -1335957373,
                                    },
                            {
                                        'source_monitor': 7002567,
                                        'source_nw_x_pixel': -4525732890879386724,
                                        'source_nw_y_pixel': -5054348332473996886,
                                        'source_pixel_width': -724683187992344638,
                                        'source_pixel_height': -7176810446704759551,
                                        'rotation': -2969518706950992309,
                                        'virtual_nw_x_pixel': 545271582,
                                        'virtual_nw_y_pixel': 1469489319,
                                        'virtual_width': 1367057050,
                                        'virtual_height': 772960202,
                                    },
                            {
                                        'source_monitor': 3069721,
                                        'source_nw_x_pixel': -6632076235589768939,
                                        'source_nw_y_pixel': -1972932473499075489,
                                        'source_pixel_width': -2164301731081341807,
                                        'source_pixel_height': -3384963756736921503,
                                        'rotation': -2163704774400943779,
                                        'virtual_nw_x_pixel': -157679317,
                                        'virtual_nw_y_pixel': 1718853665,
                                        'virtual_width': 1641869854,
                                        'virtual_height': -1194675619,
                                    },
                            {
                                        'source_monitor': 8037534,
                                        'source_nw_x_pixel': -3728297736040047140,
                                        'source_nw_y_pixel': -2427906444860999387,
                                        'source_pixel_width': -2951769801601636516,
                                        'source_pixel_height': -1243625038285473007,
                                        'rotation': -1604150839480862298,
                                        'virtual_nw_x_pixel': 1120233756,
                                        'virtual_nw_y_pixel': -746927361,
                                        'virtual_width': 1215989529,
                                        'virtual_height': 1294566272,
                                    },
                            {
                                        'source_monitor': 9193319,
                                        'source_nw_x_pixel': -2209188980612203264,
                                        'source_nw_y_pixel': -2130655951129627063,
                                        'source_pixel_width': -2249538179786218635,
                                        'source_pixel_height': -2825197515338779301,
                                        'rotation': -2481568421183410414,
                                        'virtual_nw_x_pixel': 446715095,
                                        'virtual_nw_y_pixel': 184870863,
                                        'virtual_width': 207056913,
                                        'virtual_height': -35121286,
                                    },
                            {
                                        'source_monitor': 8012769,
                                        'source_nw_x_pixel': -1714559071831497563,
                                        'source_nw_y_pixel': -3037209249897392408,
                                        'source_pixel_width': -9008260000607852849,
                                        'source_pixel_height': -456085797896170190,
                                        'rotation': -9113035341128263827,
                                        'virtual_nw_x_pixel': -1260784173,
                                        'virtual_nw_y_pixel': -526433803,
                                        'virtual_width': 1589200009,
                                        'virtual_height': 1954709451,
                                    },
                            {
                                        'source_monitor': 1316871,
                                        'source_nw_x_pixel': -349590255779013082,
                                        'source_nw_y_pixel': -6018202411240219244,
                                        'source_pixel_width': -251825064661477163,
                                        'source_pixel_height': -5347789871246011523,
                                        'rotation': -4976433512599655760,
                                        'virtual_nw_x_pixel': -998578523,
                                        'virtual_nw_y_pixel': 224816320,
                                        'virtual_width': -835011799,
                                        'virtual_height': 12255080,
                                    },
                        ],
                },
                {
                    'description': 'Ķ\u0379ʺǬɵҁΌƁ˧ӂԫεɕѳӆƶIӽAɮǧɭ¦ФYƚɌ»Я˒',
                    'monitors': [
                            {
                                        'identifier': 5043979,
                                        'width': -8043928566385995077,
                                        'height': 1371460015642958112,
                                    },
                            {
                                        'identifier': 3754238,
                                        'width': 4712689079407507741,
                                        'height': 229618209411280571,
                                    },
                            {
                                        'identifier': -136191,
                                        'width': 1104181498952051677,
                                        'height': -6739469095058484960,
                                    },
                            {
                                        'identifier': 1027613,
                                        'width': -189997410087165024,
                                        'height': 5464867875534313416,
                                    },
                            {
                                        'identifier': 6766865,
                                        'width': -2175777019543276664,
                                        'height': -1760797196250118938,
                                    },
                            {
                                        'identifier': 4977767,
                                        'width': 6693452014949522028,
                                        'height': 7427848339034145151,
                                    },
                            {
                                        'identifier': 9183848,
                                        'width': 8843791201318397397,
                                        'height': 3244605841056153369,
                                    },
                            {
                                        'identifier': 4221193,
                                        'width': 4013026254793685144,
                                        'height': 7624627612827014405,
                                    },
                            {
                                        'identifier': 8329263,
                                        'width': 6578206058942955834,
                                        'height': 2703766030621153501,
                                    },
                            {
                                        'identifier': 3450041,
                                        'width': 1536134222016172192,
                                        'height': -6406784024643426366,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5632850,
                                        'source_nw_x_pixel': -2780157751648483849,
                                        'source_nw_y_pixel': -380357658147070474,
                                        'source_pixel_width': -3120044972978420817,
                                        'source_pixel_height': -3493647899875491798,
                                        'rotation': -1279693997218480205,
                                        'virtual_nw_x_pixel': 1231774439,
                                        'virtual_nw_y_pixel': -1682714312,
                                        'virtual_width': -855921898,
                                        'virtual_height': 1619325997,
                                    },
                            {
                                        'source_monitor': -67480,
                                        'source_nw_x_pixel': -1201046954933183396,
                                        'source_nw_y_pixel': -5365425088186949542,
                                        'source_pixel_width': -2486333335840076208,
                                        'source_pixel_height': -5074832442594469776,
                                        'rotation': -5499816524442018896,
                                        'virtual_nw_x_pixel': -631063978,
                                        'virtual_nw_y_pixel': -594036453,
                                        'virtual_width': 1025654946,
                                        'virtual_height': -361847975,
                                    },
                            {
                                        'source_monitor': -276663,
                                        'source_nw_x_pixel': -4034763120508947949,
                                        'source_nw_y_pixel': -2877300179828004874,
                                        'source_pixel_width': -7260599209353380744,
                                        'source_pixel_height': -8024129476094816932,
                                        'rotation': -686807379538318113,
                                        'virtual_nw_x_pixel': 1904807529,
                                        'virtual_nw_y_pixel': 1669065370,
                                        'virtual_width': 981067716,
                                        'virtual_height': 430305305,
                                    },
                            {
                                        'source_monitor': 1563455,
                                        'source_nw_x_pixel': -778624798317622189,
                                        'source_nw_y_pixel': -4507306072096294128,
                                        'source_pixel_width': -3969140072151466764,
                                        'source_pixel_height': -1205514855640926273,
                                        'rotation': -7187075770228262802,
                                        'virtual_nw_x_pixel': 1306011129,
                                        'virtual_nw_y_pixel': -747485545,
                                        'virtual_width': -141058238,
                                        'virtual_height': -436605416,
                                    },
                            {
                                        'source_monitor': 4221501,
                                        'source_nw_x_pixel': -6655021574672294653,
                                        'source_nw_y_pixel': -4244642775072336754,
                                        'source_pixel_width': -775103229762673320,
                                        'source_pixel_height': -1008163599412265015,
                                        'rotation': -1328978067335064790,
                                        'virtual_nw_x_pixel': 589153030,
                                        'virtual_nw_y_pixel': -129309271,
                                        'virtual_width': 504950713,
                                        'virtual_height': -34730005,
                                    },
                            {
                                        'source_monitor': 7629859,
                                        'source_nw_x_pixel': -5967321104865934040,
                                        'source_nw_y_pixel': -2780140774397684231,
                                        'source_pixel_width': -3126754903582690058,
                                        'source_pixel_height': -4838019294170946244,
                                        'rotation': -7015520630354135665,
                                        'virtual_nw_x_pixel': -338645205,
                                        'virtual_nw_y_pixel': -944478297,
                                        'virtual_width': 1720706546,
                                        'virtual_height': 197578967,
                                    },
                            {
                                        'source_monitor': 7740289,
                                        'source_nw_x_pixel': -6036490410885637441,
                                        'source_nw_y_pixel': -8401690641530914368,
                                        'source_pixel_width': -7810317762202902178,
                                        'source_pixel_height': -6823527721962810230,
                                        'rotation': -2398346987868357558,
                                        'virtual_nw_x_pixel': 1640548661,
                                        'virtual_nw_y_pixel': 720752840,
                                        'virtual_width': 1010945706,
                                        'virtual_height': -1405092152,
                                    },
                            {
                                        'source_monitor': 1717006,
                                        'source_nw_x_pixel': -7829496717722819413,
                                        'source_nw_y_pixel': -7033047420086202054,
                                        'source_pixel_width': -3761357195743329486,
                                        'source_pixel_height': -4727323728483776030,
                                        'rotation': -1096760179609866564,
                                        'virtual_nw_x_pixel': -940328366,
                                        'virtual_nw_y_pixel': 1137653303,
                                        'virtual_width': 731004652,
                                        'virtual_height': -138632548,
                                    },
                            {
                                        'source_monitor': 1792780,
                                        'source_nw_x_pixel': -999491869265963669,
                                        'source_nw_y_pixel': -297358004561880459,
                                        'source_pixel_width': -3257622790733122521,
                                        'source_pixel_height': -8774098040562329476,
                                        'rotation': -5461115928925729226,
                                        'virtual_nw_x_pixel': -564245871,
                                        'virtual_nw_y_pixel': -1384885292,
                                        'virtual_width': 1878009536,
                                        'virtual_height': 1953802164,
                                    },
                            {
                                        'source_monitor': 8889084,
                                        'source_nw_x_pixel': -2922699244096054639,
                                        'source_nw_y_pixel': -2466180515655278305,
                                        'source_pixel_width': -7776666185336975458,
                                        'source_pixel_height': -5586215780148288108,
                                        'rotation': -1833542377530624278,
                                        'virtual_nw_x_pixel': 1486013507,
                                        'virtual_nw_y_pixel': -1831298328,
                                        'virtual_width': 1312849216,
                                        'virtual_height': 1432906266,
                                    },
                        ],
                },
                {
                    'description': 'ƆϭΏ%ѕΕбºʒӶ]fӽăκӫÒК"ˁĤϵ@ҷ҈Ӵ¢ƵMӰ',
                    'monitors': [
                            {
                                        'identifier': 2033351,
                                        'width': 2054693838061486386,
                                        'height': -4401844284406351928,
                                    },
                            {
                                        'identifier': 5271424,
                                        'width': 262161031371934945,
                                        'height': -6676147682655160164,
                                    },
                            {
                                        'identifier': 6678580,
                                        'width': 8963716025116007804,
                                        'height': -4862563148981332981,
                                    },
                            {
                                        'identifier': 6817993,
                                        'width': 8953218000879689236,
                                        'height': -1493910211590003460,
                                    },
                            {
                                        'identifier': 5006889,
                                        'width': 4608799738954912585,
                                        'height': -2439597678982125831,
                                    },
                            {
                                        'identifier': 3653593,
                                        'width': -1385602656583947409,
                                        'height': 2893168140249961041,
                                    },
                            {
                                        'identifier': 2501360,
                                        'width': -2315108232871481705,
                                        'height': 4387202824927153836,
                                    },
                            {
                                        'identifier': 6096653,
                                        'width': 2885049932108980984,
                                        'height': 7688038371917513810,
                                    },
                            {
                                        'identifier': 7915737,
                                        'width': 5452669832926318892,
                                        'height': -5929643865997793233,
                                    },
                            {
                                        'identifier': 1230014,
                                        'width': 4551669198996915350,
                                        'height': 6847565256691526121,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3862191,
                                        'source_nw_x_pixel': -5444977806921958546,
                                        'source_nw_y_pixel': -8246166950105035468,
                                        'source_pixel_width': -6344724199581075998,
                                        'source_pixel_height': -8353926767095831923,
                                        'rotation': -2029904263662918732,
                                        'virtual_nw_x_pixel': -1974567299,
                                        'virtual_nw_y_pixel': -327892438,
                                        'virtual_width': 369507269,
                                        'virtual_height': 394462320,
                                    },
                            {
                                        'source_monitor': 6861600,
                                        'source_nw_x_pixel': -1085257411282338195,
                                        'source_nw_y_pixel': -1556759914147237824,
                                        'source_pixel_width': -551461364159877972,
                                        'source_pixel_height': -5957040118714270800,
                                        'rotation': -8439596236475411845,
                                        'virtual_nw_x_pixel': -1189884725,
                                        'virtual_nw_y_pixel': -116741973,
                                        'virtual_width': 838683052,
                                        'virtual_height': 104878284,
                                    },
                            {
                                        'source_monitor': 4907748,
                                        'source_nw_x_pixel': -6033149142059969336,
                                        'source_nw_y_pixel': -1878275779605413940,
                                        'source_pixel_width': -2065369686254097600,
                                        'source_pixel_height': -9048650609474698736,
                                        'rotation': -6337623982522445599,
                                        'virtual_nw_x_pixel': -779563688,
                                        'virtual_nw_y_pixel': 386727672,
                                        'virtual_width': 1010822683,
                                        'virtual_height': 1057493877,
                                    },
                            {
                                        'source_monitor': 2073430,
                                        'source_nw_x_pixel': -6745847609098162931,
                                        'source_nw_y_pixel': -3433706496571069277,
                                        'source_pixel_width': -4131281969335978363,
                                        'source_pixel_height': -8546985751667538878,
                                        'rotation': -5151348456037164652,
                                        'virtual_nw_x_pixel': 428658746,
                                        'virtual_nw_y_pixel': 309946595,
                                        'virtual_width': -1349498318,
                                        'virtual_height': 1313532560,
                                    },
                            {
                                        'source_monitor': 7942208,
                                        'source_nw_x_pixel': -735259546527547114,
                                        'source_nw_y_pixel': -2740242801275567384,
                                        'source_pixel_width': -7379882438802973502,
                                        'source_pixel_height': -1569489761322752761,
                                        'rotation': -9188557750274130070,
                                        'virtual_nw_x_pixel': 1552237908,
                                        'virtual_nw_y_pixel': -376639736,
                                        'virtual_width': 212214664,
                                        'virtual_height': -828747238,
                                    },
                            {
                                        'source_monitor': 9044379,
                                        'source_nw_x_pixel': -3439580365079776802,
                                        'source_nw_y_pixel': -2460629414011693899,
                                        'source_pixel_width': -730173517534291161,
                                        'source_pixel_height': -3569704071847036945,
                                        'rotation': -5844590021792843247,
                                        'virtual_nw_x_pixel': -296227567,
                                        'virtual_nw_y_pixel': 112739014,
                                        'virtual_width': -1603492549,
                                        'virtual_height': 347469371,
                                    },
                            {
                                        'source_monitor': 7183879,
                                        'source_nw_x_pixel': -5193584370876220915,
                                        'source_nw_y_pixel': -7667768842854667822,
                                        'source_pixel_width': -5338531681888639441,
                                        'source_pixel_height': -6244536299525205840,
                                        'rotation': -234874007426873553,
                                        'virtual_nw_x_pixel': -441662671,
                                        'virtual_nw_y_pixel': 81831220,
                                        'virtual_width': -551969515,
                                        'virtual_height': -1297543702,
                                    },
                            {
                                        'source_monitor': 7542389,
                                        'source_nw_x_pixel': -947999819349160522,
                                        'source_nw_y_pixel': -6383926154970429649,
                                        'source_pixel_width': -8141564472273733150,
                                        'source_pixel_height': -8059465176063033420,
                                        'rotation': -3856068669303863392,
                                        'virtual_nw_x_pixel': -1720125002,
                                        'virtual_nw_y_pixel': 979416953,
                                        'virtual_width': -424096576,
                                        'virtual_height': 1213238817,
                                    },
                            {
                                        'source_monitor': 7268840,
                                        'source_nw_x_pixel': -5590480248461282265,
                                        'source_nw_y_pixel': -4034690546816209738,
                                        'source_pixel_width': -1588370164396246993,
                                        'source_pixel_height': -2201890216295969943,
                                        'rotation': -7840863023049548122,
                                        'virtual_nw_x_pixel': 1354864253,
                                        'virtual_nw_y_pixel': 570415268,
                                        'virtual_width': -1420396751,
                                        'virtual_height': 517199882,
                                    },
                            {
                                        'source_monitor': 3291519,
                                        'source_nw_x_pixel': -6923242205186141687,
                                        'source_nw_y_pixel': -2609571311780935797,
                                        'source_pixel_width': -8013509280937819482,
                                        'source_pixel_height': -5114590180887474670,
                                        'rotation': -3106516534784662855,
                                        'virtual_nw_x_pixel': -196128578,
                                        'virtual_nw_y_pixel': -1514879001,
                                        'virtual_width': 12584918,
                                        'virtual_height': -877177453,
                                    },
                        ],
                },
                {
                    'description': 'IЈGҿӷɀγЋΨёɎ˥ҪņԭѺкОʤɣіėʆȓȉHΔϯʂĻ',
                    'monitors': [
                            {
                                        'identifier': 8025256,
                                        'width': 73022909893605609,
                                        'height': 4616506084526414148,
                                    },
                            {
                                        'identifier': 7904305,
                                        'width': -2262096530137809578,
                                        'height': 9058184704946564770,
                                    },
                            {
                                        'identifier': 3656476,
                                        'width': -7260509507363431390,
                                        'height': 237085383280666,
                                    },
                            {
                                        'identifier': 7983705,
                                        'width': -1908706889412091810,
                                        'height': 552152358004711696,
                                    },
                            {
                                        'identifier': 7066980,
                                        'width': -254852727878633926,
                                        'height': -4915151240389751589,
                                    },
                            {
                                        'identifier': 9362744,
                                        'width': -776584304864761189,
                                        'height': 2483481681026884163,
                                    },
                            {
                                        'identifier': 8282784,
                                        'width': 4473458057384542897,
                                        'height': 157620950401360317,
                                    },
                            {
                                        'identifier': 7402829,
                                        'width': -6314834193783439506,
                                        'height': -8404062878840064470,
                                    },
                            {
                                        'identifier': 1675008,
                                        'width': 6334314568085439160,
                                        'height': -1180030657504608481,
                                    },
                            {
                                        'identifier': 5787646,
                                        'width': -395332980001552136,
                                        'height': 4548092735042562306,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 576143,
                                        'source_nw_x_pixel': -6744731235067707753,
                                        'source_nw_y_pixel': -6577046168916862930,
                                        'source_pixel_width': -706203582346864894,
                                        'source_pixel_height': -3430240522910949828,
                                        'rotation': -4045597801096775322,
                                        'virtual_nw_x_pixel': 135745733,
                                        'virtual_nw_y_pixel': -288866765,
                                        'virtual_width': 27849447,
                                        'virtual_height': 1822681601,
                                    },
                            {
                                        'source_monitor': 2963625,
                                        'source_nw_x_pixel': -8251722587249085151,
                                        'source_nw_y_pixel': -5167849625666461515,
                                        'source_pixel_width': -4118095560335240394,
                                        'source_pixel_height': -7851822455115604231,
                                        'rotation': -3058713083343847297,
                                        'virtual_nw_x_pixel': 489778145,
                                        'virtual_nw_y_pixel': -1936089713,
                                        'virtual_width': 1386074864,
                                        'virtual_height': 1431129778,
                                    },
                            {
                                        'source_monitor': 8561551,
                                        'source_nw_x_pixel': -6188333658241113585,
                                        'source_nw_y_pixel': -7005079753976605666,
                                        'source_pixel_width': -4818369504646227016,
                                        'source_pixel_height': -5490237337425843267,
                                        'rotation': -1296860500332113233,
                                        'virtual_nw_x_pixel': -1267139583,
                                        'virtual_nw_y_pixel': 477672042,
                                        'virtual_width': -991063620,
                                        'virtual_height': -214277125,
                                    },
                            {
                                        'source_monitor': 7719691,
                                        'source_nw_x_pixel': -2269472673997933504,
                                        'source_nw_y_pixel': -7034231122971887337,
                                        'source_pixel_width': -1214042351123924015,
                                        'source_pixel_height': -7029840645830984188,
                                        'rotation': -1993985215938598688,
                                        'virtual_nw_x_pixel': -565644094,
                                        'virtual_nw_y_pixel': 822914933,
                                        'virtual_width': -1313237614,
                                        'virtual_height': 1987086881,
                                    },
                            {
                                        'source_monitor': 4978841,
                                        'source_nw_x_pixel': -6203733057619760920,
                                        'source_nw_y_pixel': -1706298639823798592,
                                        'source_pixel_width': -1652495102105169432,
                                        'source_pixel_height': -764401971188122065,
                                        'rotation': -8841923286173826715,
                                        'virtual_nw_x_pixel': -1994279640,
                                        'virtual_nw_y_pixel': -1853288317,
                                        'virtual_width': -386539399,
                                        'virtual_height': -1926736641,
                                    },
                            {
                                        'source_monitor': 8396406,
                                        'source_nw_x_pixel': -5517701170116612081,
                                        'source_nw_y_pixel': -6271828838085222346,
                                        'source_pixel_width': -2563841153318863219,
                                        'source_pixel_height': -8671624798773711844,
                                        'rotation': -3817497494009950914,
                                        'virtual_nw_x_pixel': 1669489088,
                                        'virtual_nw_y_pixel': -719401773,
                                        'virtual_width': 1062529460,
                                        'virtual_height': -325161824,
                                    },
                            {
                                        'source_monitor': 278108,
                                        'source_nw_x_pixel': -7349816052722686832,
                                        'source_nw_y_pixel': -2329613396335256210,
                                        'source_pixel_width': -1926910716724112917,
                                        'source_pixel_height': -43654428120707106,
                                        'rotation': -8751884385682239481,
                                        'virtual_nw_x_pixel': -1076776817,
                                        'virtual_nw_y_pixel': -664907565,
                                        'virtual_width': 369974247,
                                        'virtual_height': 1183864140,
                                    },
                            {
                                        'source_monitor': 3910806,
                                        'source_nw_x_pixel': -8769448053900529920,
                                        'source_nw_y_pixel': -1343317916188696561,
                                        'source_pixel_width': -4510048493191925317,
                                        'source_pixel_height': -1710792875272472236,
                                        'rotation': -9218627668900282122,
                                        'virtual_nw_x_pixel': 1372953027,
                                        'virtual_nw_y_pixel': 1646495460,
                                        'virtual_width': -523190239,
                                        'virtual_height': -202903854,
                                    },
                            {
                                        'source_monitor': 3216039,
                                        'source_nw_x_pixel': -3863971760097659608,
                                        'source_nw_y_pixel': -7838895773349581222,
                                        'source_pixel_width': -6247441343309278220,
                                        'source_pixel_height': -8053429290307862874,
                                        'rotation': -9111801069541021078,
                                        'virtual_nw_x_pixel': 1959949021,
                                        'virtual_nw_y_pixel': 218040465,
                                        'virtual_width': 1192707715,
                                        'virtual_height': -1264047343,
                                    },
                            {
                                        'source_monitor': 2089746,
                                        'source_nw_x_pixel': -7728034691392620022,
                                        'source_nw_y_pixel': -2469487181213904708,
                                        'source_pixel_width': -1177001696953656581,
                                        'source_pixel_height': -4337546424980059432,
                                        'rotation': -8279511775671974554,
                                        'virtual_nw_x_pixel': -1519262233,
                                        'virtual_nw_y_pixel': 670834432,
                                        'virtual_width': -1137920977,
                                        'virtual_height': 126264260,
                                    },
                        ],
                },
                {
                    'description': 'хӹŕǂĤҙ˴Äԙ£ҍĝƤԙк%÷нѮҙȬԋȈÃԌ\x9aΪӪ΅ª',
                    'monitors': [
                            {
                                        'identifier': 8231044,
                                        'width': -5928312143393543312,
                                        'height': -3515044686088686784,
                                    },
                            {
                                        'identifier': 4274736,
                                        'width': -4557122753188555466,
                                        'height': 2514210729991970328,
                                    },
                            {
                                        'identifier': 3199035,
                                        'width': 2451067149239990104,
                                        'height': 6743530209642963226,
                                    },
                            {
                                        'identifier': 3676853,
                                        'width': 2277017618839369624,
                                        'height': -3947907096344021972,
                                    },
                            {
                                        'identifier': 3134379,
                                        'width': 4043625454284523731,
                                        'height': -6225868301381186860,
                                    },
                            {
                                        'identifier': -858522,
                                        'width': 5388661197401548371,
                                        'height': -7348471783391465157,
                                    },
                            {
                                        'identifier': 7287463,
                                        'width': -395740235357507441,
                                        'height': 5682799137329929275,
                                    },
                            {
                                        'identifier': 2404524,
                                        'width': -849953015802641114,
                                        'height': 1954145051916434858,
                                    },
                            {
                                        'identifier': 3956478,
                                        'width': 1266143356452103065,
                                        'height': -6700822588490605135,
                                    },
                            {
                                        'identifier': 4296800,
                                        'width': -3163725722904892225,
                                        'height': 8244004458874176994,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8197615,
                                        'source_nw_x_pixel': -3876489028988180641,
                                        'source_nw_y_pixel': -3182833949604108966,
                                        'source_pixel_width': -427226907890922231,
                                        'source_pixel_height': -3738192588333229086,
                                        'rotation': -9110359014708344008,
                                        'virtual_nw_x_pixel': -664035579,
                                        'virtual_nw_y_pixel': 72328849,
                                        'virtual_width': 1666864364,
                                        'virtual_height': 844295477,
                                    },
                            {
                                        'source_monitor': 8346001,
                                        'source_nw_x_pixel': -166356192210884968,
                                        'source_nw_y_pixel': -8556185639881570994,
                                        'source_pixel_width': -1831618774199771384,
                                        'source_pixel_height': -9165898606996474651,
                                        'rotation': -3611187671462161561,
                                        'virtual_nw_x_pixel': -253407494,
                                        'virtual_nw_y_pixel': 1009132943,
                                        'virtual_width': 581224304,
                                        'virtual_height': 1388730991,
                                    },
                            {
                                        'source_monitor': 6074200,
                                        'source_nw_x_pixel': -8586918967310503920,
                                        'source_nw_y_pixel': -1804473731011758467,
                                        'source_pixel_width': -1573436731563614654,
                                        'source_pixel_height': -5378113044800186560,
                                        'rotation': -8204798897521428439,
                                        'virtual_nw_x_pixel': -1634366950,
                                        'virtual_nw_y_pixel': 1886851848,
                                        'virtual_width': 1207415970,
                                        'virtual_height': -622634249,
                                    },
                            {
                                        'source_monitor': 129493,
                                        'source_nw_x_pixel': -669520866186948457,
                                        'source_nw_y_pixel': -422144533065502223,
                                        'source_pixel_width': -6669907347830210944,
                                        'source_pixel_height': -7573400884123561683,
                                        'rotation': -6209215895421584772,
                                        'virtual_nw_x_pixel': -226615722,
                                        'virtual_nw_y_pixel': 1188699597,
                                        'virtual_width': 29358097,
                                        'virtual_height': 149480201,
                                    },
                            {
                                        'source_monitor': 4540342,
                                        'source_nw_x_pixel': -5819873592300841519,
                                        'source_nw_y_pixel': -6962582024446537609,
                                        'source_pixel_width': -8896898836582428662,
                                        'source_pixel_height': -1517110722744422339,
                                        'rotation': -8631369969695438660,
                                        'virtual_nw_x_pixel': 424420685,
                                        'virtual_nw_y_pixel': -825192042,
                                        'virtual_width': -1910288991,
                                        'virtual_height': 1233831703,
                                    },
                            {
                                        'source_monitor': 770935,
                                        'source_nw_x_pixel': -2221196371097087748,
                                        'source_nw_y_pixel': -1445216648558600872,
                                        'source_pixel_width': -6177729368598183873,
                                        'source_pixel_height': -2703020759737506414,
                                        'rotation': -3486382024227531195,
                                        'virtual_nw_x_pixel': -1737838677,
                                        'virtual_nw_y_pixel': -921575461,
                                        'virtual_width': -1999507382,
                                        'virtual_height': -580670185,
                                    },
                            {
                                        'source_monitor': 9451524,
                                        'source_nw_x_pixel': -2583407845568797283,
                                        'source_nw_y_pixel': -5146962066241284718,
                                        'source_pixel_width': -3317556010512551338,
                                        'source_pixel_height': -3086067763498279170,
                                        'rotation': -2122072855569646950,
                                        'virtual_nw_x_pixel': -1260815018,
                                        'virtual_nw_y_pixel': 1148057253,
                                        'virtual_width': 1892316267,
                                        'virtual_height': 1344043972,
                                    },
                            {
                                        'source_monitor': 5677857,
                                        'source_nw_x_pixel': -4608707695325967874,
                                        'source_nw_y_pixel': -5319336973680019893,
                                        'source_pixel_width': -2455823639571286106,
                                        'source_pixel_height': -1213983153334877437,
                                        'rotation': -8230306045258692044,
                                        'virtual_nw_x_pixel': 120029317,
                                        'virtual_nw_y_pixel': -1580233656,
                                        'virtual_width': 1125573759,
                                        'virtual_height': -997912791,
                                    },
                            {
                                        'source_monitor': 3261068,
                                        'source_nw_x_pixel': -6840397231667546033,
                                        'source_nw_y_pixel': -1086307616963332563,
                                        'source_pixel_width': -40759611185653476,
                                        'source_pixel_height': -5318142818656329294,
                                        'rotation': -4089552789926462536,
                                        'virtual_nw_x_pixel': -113453654,
                                        'virtual_nw_y_pixel': 549969480,
                                        'virtual_width': 517612330,
                                        'virtual_height': 1362369531,
                                    },
                            {
                                        'source_monitor': 8333251,
                                        'source_nw_x_pixel': -5273124056645436615,
                                        'source_nw_y_pixel': -8335687588989546471,
                                        'source_pixel_width': -7176492036246057450,
                                        'source_pixel_height': -8802393861854280467,
                                        'rotation': -5350910971546462508,
                                        'virtual_nw_x_pixel': -94461551,
                                        'virtual_nw_y_pixel': 1613710873,
                                        'virtual_width': 1388216839,
                                        'virtual_height': -316165001,
                                    },
                        ],
                },
                {
                    'description': 'ʛɳǡĕÃԣ³ɇ-źϿԅψҹюȯԑʄеё˶ɌÚΩ\x8dҽSӂɬÔ',
                    'monitors': [
                            {
                                        'identifier': 9434162,
                                        'width': -5984880096825626976,
                                        'height': -5201118757300237652,
                                    },
                            {
                                        'identifier': 5504752,
                                        'width': 6429965306305076578,
                                        'height': 5274098620910677965,
                                    },
                            {
                                        'identifier': 8471596,
                                        'width': 4304055228782834177,
                                        'height': 2960749645134681886,
                                    },
                            {
                                        'identifier': 4554843,
                                        'width': 2421953173881148439,
                                        'height': 1879181811228336376,
                                    },
                            {
                                        'identifier': 4863401,
                                        'width': 7576294145821314442,
                                        'height': -4117970402422117174,
                                    },
                            {
                                        'identifier': 9543595,
                                        'width': -2196885853997479045,
                                        'height': -6363342781430824324,
                                    },
                            {
                                        'identifier': -207748,
                                        'width': -7117328475545857760,
                                        'height': 206524025064362434,
                                    },
                            {
                                        'identifier': 8564156,
                                        'width': 5084982279888330110,
                                        'height': -5973315789206068946,
                                    },
                            {
                                        'identifier': 6115192,
                                        'width': 648429974841841760,
                                        'height': -2396351807568647874,
                                    },
                            {
                                        'identifier': 2835473,
                                        'width': -1231255802483647843,
                                        'height': -8832579492297498421,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9901029,
                                        'source_nw_x_pixel': -8359505243719051487,
                                        'source_nw_y_pixel': -2311686660032585021,
                                        'source_pixel_width': -5438167014363608805,
                                        'source_pixel_height': -8611164998786646532,
                                        'rotation': -2963987170871640250,
                                        'virtual_nw_x_pixel': -1683574184,
                                        'virtual_nw_y_pixel': -825865286,
                                        'virtual_width': 536437493,
                                        'virtual_height': -896313398,
                                    },
                            {
                                        'source_monitor': 8926869,
                                        'source_nw_x_pixel': -8321062220063742379,
                                        'source_nw_y_pixel': -3618493245513523396,
                                        'source_pixel_width': -2242752001038804779,
                                        'source_pixel_height': -7546769646365666839,
                                        'rotation': -7552175058592994773,
                                        'virtual_nw_x_pixel': -1587500487,
                                        'virtual_nw_y_pixel': -1723988375,
                                        'virtual_width': 1218305110,
                                        'virtual_height': -1498553062,
                                    },
                            {
                                        'source_monitor': 5157054,
                                        'source_nw_x_pixel': -4180842341068867139,
                                        'source_nw_y_pixel': -669670164765058089,
                                        'source_pixel_width': -2048934189141877539,
                                        'source_pixel_height': -3918004492843971549,
                                        'rotation': -1540980078805590386,
                                        'virtual_nw_x_pixel': -1849356309,
                                        'virtual_nw_y_pixel': 1219796158,
                                        'virtual_width': 983306099,
                                        'virtual_height': -450809474,
                                    },
                            {
                                        'source_monitor': 2628747,
                                        'source_nw_x_pixel': -7491271971795508174,
                                        'source_nw_y_pixel': -3362935955201901546,
                                        'source_pixel_width': -97994307779053819,
                                        'source_pixel_height': -2201467229242003019,
                                        'rotation': -737620194215713348,
                                        'virtual_nw_x_pixel': 1019384225,
                                        'virtual_nw_y_pixel': -55205018,
                                        'virtual_width': 42276630,
                                        'virtual_height': 799169040,
                                    },
                            {
                                        'source_monitor': 9369576,
                                        'source_nw_x_pixel': -7982688159831061098,
                                        'source_nw_y_pixel': -2209056087907118595,
                                        'source_pixel_width': -4432233631313585217,
                                        'source_pixel_height': -7655052564391689696,
                                        'rotation': -6033544914321349007,
                                        'virtual_nw_x_pixel': -1645247170,
                                        'virtual_nw_y_pixel': 548874581,
                                        'virtual_width': 1464068011,
                                        'virtual_height': 1514565406,
                                    },
                            {
                                        'source_monitor': 5531889,
                                        'source_nw_x_pixel': -244174208678285008,
                                        'source_nw_y_pixel': -2752043803102788015,
                                        'source_pixel_width': -1394756303600817030,
                                        'source_pixel_height': -6779785264656791424,
                                        'rotation': -3185170111110141250,
                                        'virtual_nw_x_pixel': 1443766154,
                                        'virtual_nw_y_pixel': -43672442,
                                        'virtual_width': -1716326163,
                                        'virtual_height': 1616292395,
                                    },
                            {
                                        'source_monitor': 4401933,
                                        'source_nw_x_pixel': -6978667728168372038,
                                        'source_nw_y_pixel': -9036731496228702748,
                                        'source_pixel_width': -6608842821859759926,
                                        'source_pixel_height': -2479357134542974235,
                                        'rotation': -1069268145936702097,
                                        'virtual_nw_x_pixel': 957513769,
                                        'virtual_nw_y_pixel': 1689016536,
                                        'virtual_width': 1757848158,
                                        'virtual_height': 609209777,
                                    },
                            {
                                        'source_monitor': 7567766,
                                        'source_nw_x_pixel': -5705995876375855464,
                                        'source_nw_y_pixel': -8921196398482851368,
                                        'source_pixel_width': -6621376796661201616,
                                        'source_pixel_height': -2156727276121420984,
                                        'rotation': -7824326631156845996,
                                        'virtual_nw_x_pixel': -667800436,
                                        'virtual_nw_y_pixel': 646099504,
                                        'virtual_width': -1501822477,
                                        'virtual_height': 1105723339,
                                    },
                            {
                                        'source_monitor': 5773827,
                                        'source_nw_x_pixel': -3784733294818453583,
                                        'source_nw_y_pixel': -1591075723886602387,
                                        'source_pixel_width': -6063334499740630995,
                                        'source_pixel_height': -1515327224813722945,
                                        'rotation': -8628471269763733145,
                                        'virtual_nw_x_pixel': -1113560520,
                                        'virtual_nw_y_pixel': 1554492963,
                                        'virtual_width': 1353010233,
                                        'virtual_height': -1910593906,
                                    },
                            {
                                        'source_monitor': 9236498,
                                        'source_nw_x_pixel': -3171030244733542028,
                                        'source_nw_y_pixel': -6200259766018548733,
                                        'source_pixel_width': -1344930829293281275,
                                        'source_pixel_height': -1720326627875014557,
                                        'rotation': -2571468216249183695,
                                        'virtual_nw_x_pixel': -1761612287,
                                        'virtual_nw_y_pixel': -487576891,
                                        'virtual_width': 393482171,
                                        'virtual_height': 1517984509,
                                    },
                        ],
                },
                {
                    'description': 'ęŀǎԓϲūŧĨϖecӕ',
                    'monitors': [
                            {
                                        'identifier': 7155457,
                                        'width': 926433935702937131,
                                        'height': 2550142767163528775,
                                    },
                            {
                                        'identifier': 7407693,
                                        'width': 491214803127181190,
                                        'height': -8164888797777904322,
                                    },
                            {
                                        'identifier': 4361096,
                                        'width': -799317415192508670,
                                        'height': -5588359370337025048,
                                    },
                            {
                                        'identifier': 4352724,
                                        'width': 7878830352519086523,
                                        'height': -6844330704866804943,
                                    },
                            {
                                        'identifier': 2459338,
                                        'width': 4851104059583654632,
                                        'height': -8146516070516641029,
                                    },
                            {
                                        'identifier': 433754,
                                        'width': 8188003036235759291,
                                        'height': 8571539342710516095,
                                    },
                            {
                                        'identifier': 4702477,
                                        'width': 9188305776843893816,
                                        'height': 360163181446611803,
                                    },
                            {
                                        'identifier': 5270184,
                                        'width': -3185749369513332392,
                                        'height': -8380319473496366871,
                                    },
                            {
                                        'identifier': 1113576,
                                        'width': 7191226958516960896,
                                        'height': -3673301494057068434,
                                    },
                            {
                                        'identifier': 5969542,
                                        'width': -1889953396302461559,
                                        'height': -5615632306017544943,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -543780,
                                        'source_nw_x_pixel': -6064719309136039434,
                                        'source_nw_y_pixel': -704693030777042779,
                                        'source_pixel_width': -4726498660420889529,
                                        'source_pixel_height': -5247491742700792461,
                                        'rotation': -4138851928697897361,
                                        'virtual_nw_x_pixel': -1165893626,
                                        'virtual_nw_y_pixel': 1063987065,
                                        'virtual_width': 1643454369,
                                        'virtual_height': -1066971718,
                                    },
                            {
                                        'source_monitor': 2408195,
                                        'source_nw_x_pixel': -886174206255199300,
                                        'source_nw_y_pixel': -2112443268592365707,
                                        'source_pixel_width': -883029263258660522,
                                        'source_pixel_height': -1701555187961938207,
                                        'rotation': -5316104144221993077,
                                        'virtual_nw_x_pixel': -433799169,
                                        'virtual_nw_y_pixel': 898123057,
                                        'virtual_width': 893013831,
                                        'virtual_height': 1272348171,
                                    },
                            {
                                        'source_monitor': 174346,
                                        'source_nw_x_pixel': -3426566611717134926,
                                        'source_nw_y_pixel': -3301167485522101809,
                                        'source_pixel_width': -5422218931920469040,
                                        'source_pixel_height': -5483871035536277532,
                                        'rotation': -4306073335394203474,
                                        'virtual_nw_x_pixel': 1274906276,
                                        'virtual_nw_y_pixel': 916060693,
                                        'virtual_width': -1546279371,
                                        'virtual_height': -934747468,
                                    },
                            {
                                        'source_monitor': 5782288,
                                        'source_nw_x_pixel': -7965663117068489225,
                                        'source_nw_y_pixel': -2307639591941937590,
                                        'source_pixel_width': -2037746535164029123,
                                        'source_pixel_height': -770383202300359117,
                                        'rotation': -2241809176310770631,
                                        'virtual_nw_x_pixel': -705578540,
                                        'virtual_nw_y_pixel': 586566041,
                                        'virtual_width': 1534033772,
                                        'virtual_height': 1282099642,
                                    },
                            {
                                        'source_monitor': 623152,
                                        'source_nw_x_pixel': -3975405180363417130,
                                        'source_nw_y_pixel': -6005703305192089726,
                                        'source_pixel_width': -5947722402514876809,
                                        'source_pixel_height': -2915512240961159967,
                                        'rotation': -5556192888955657628,
                                        'virtual_nw_x_pixel': -1654490674,
                                        'virtual_nw_y_pixel': -306334911,
                                        'virtual_width': 1603513160,
                                        'virtual_height': -1729192573,
                                    },
                            {
                                        'source_monitor': 8119151,
                                        'source_nw_x_pixel': -8609306519913178298,
                                        'source_nw_y_pixel': -7852333028521575308,
                                        'source_pixel_width': -4908704166986551839,
                                        'source_pixel_height': -7840695170371327750,
                                        'rotation': -7377834005496073344,
                                        'virtual_nw_x_pixel': -747667480,
                                        'virtual_nw_y_pixel': 1694213471,
                                        'virtual_width': -1465650830,
                                        'virtual_height': -301279282,
                                    },
                            {
                                        'source_monitor': 7741389,
                                        'source_nw_x_pixel': -6432554973888660950,
                                        'source_nw_y_pixel': -8546360610646458213,
                                        'source_pixel_width': -7808758995131637165,
                                        'source_pixel_height': -5934447381956379266,
                                        'rotation': -1567476874632818437,
                                        'virtual_nw_x_pixel': 1752919657,
                                        'virtual_nw_y_pixel': -618428329,
                                        'virtual_width': -1951434969,
                                        'virtual_height': -1826583899,
                                    },
                            {
                                        'source_monitor': 7533471,
                                        'source_nw_x_pixel': -3717012346141124705,
                                        'source_nw_y_pixel': -2962093961163637879,
                                        'source_pixel_width': -6277342067337892859,
                                        'source_pixel_height': -4721482071906626757,
                                        'rotation': -190518360238737562,
                                        'virtual_nw_x_pixel': -572889943,
                                        'virtual_nw_y_pixel': -1192020147,
                                        'virtual_width': 362420623,
                                        'virtual_height': -1378406373,
                                    },
                            {
                                        'source_monitor': 1951818,
                                        'source_nw_x_pixel': -290066267745000377,
                                        'source_nw_y_pixel': -8461594242324005499,
                                        'source_pixel_width': -1854563025316493994,
                                        'source_pixel_height': -1648511890434294993,
                                        'rotation': -8192175527119923486,
                                        'virtual_nw_x_pixel': -61355831,
                                        'virtual_nw_y_pixel': 140788949,
                                        'virtual_width': 32564154,
                                        'virtual_height': 455048799,
                                    },
                            {
                                        'source_monitor': 3831764,
                                        'source_nw_x_pixel': -2479441034858534703,
                                        'source_nw_y_pixel': -4306854111708698050,
                                        'source_pixel_width': -1700809974202522780,
                                        'source_pixel_height': -374556751032147301,
                                        'rotation': -672595726905399046,
                                        'virtual_nw_x_pixel': -1119334807,
                                        'virtual_nw_y_pixel': 1412285905,
                                        'virtual_width': 373871284,
                                        'virtual_height': 989441518,
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
                                        'identifier': 5787563,
                                        'width': -8494034295843290906,
                                        'height': -4161364585202146968,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -7328881341231440222,
                                        'source_nw_y_pixel': -3150465430678110407,
                                        'source_pixel_width': -6730044719928153969,
                                        'source_pixel_height': -7645610072325296686,
                                        'rotation': -5422283418203600548,
                                        'virtual_nw_x_pixel': -275681744,
                                        'virtual_nw_y_pixel': -560569613,
                                        'virtual_width': 1731229370,
                                        'virtual_height': 1139436711,
                                    },
                        ],
                },
            ],

        },
    ),
]
