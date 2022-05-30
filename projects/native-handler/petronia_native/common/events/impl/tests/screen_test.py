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
            'identifier': 8952882,
            'width': 3341535059096813718,
            'height': 3322168101156760967,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 7392391,

            'width': -4224459812875413909,

            'height': 382242356805007856,

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
            'source_monitor': 7658702,
            'source_nw_x_pixel': -2553810089337684606,
            'source_nw_y_pixel': -3297053105632242671,
            'source_pixel_width': -1868000439676623999,
            'source_pixel_height': -3227215477476097028,
            'rotation': -5062897157960445893,
            'virtual_nw_x_pixel': -604998818,
            'virtual_nw_y_pixel': -632504532,
            'virtual_width': -720499797,
            'virtual_height': 859052489,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -8432028983619901651,

            'source_nw_y_pixel': -4776721610932337126,

            'source_pixel_width': -5730050140436370121,

            'source_pixel_height': -1857062374558774110,

            'rotation': -1001514037842567806,

            'virtual_nw_x_pixel': -1506866295,

            'virtual_nw_y_pixel': 543254453,

            'virtual_width': -443813066,

            'virtual_height': -1607883770,

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
            'description': 'ңWǨŃævӲŢϔŭÒӅ˜Ҫɱ|άԫő˥ɂһƗ˸ÎҘº;ɁѬ',
            'monitors': [
                {
                    'identifier': 6326083,
                    'width': 5986112176842047655,
                    'height': -7210543285301460766,
                },
                {
                    'identifier': 618871,
                    'width': 4574414531889588738,
                    'height': -4791145073271371381,
                },
                {
                    'identifier': 8607681,
                    'width': -1415855522132766991,
                    'height': -5871037940414348631,
                },
                {
                    'identifier': 1661952,
                    'width': -7551649079585591456,
                    'height': 7384023279069726074,
                },
                {
                    'identifier': 1013723,
                    'width': 4080550247866966853,
                    'height': -4805449605040623635,
                },
                {
                    'identifier': 4472395,
                    'width': -6881016428882580405,
                    'height': 6713903580629696960,
                },
                {
                    'identifier': 5130168,
                    'width': -8072925778023279420,
                    'height': -7113829124448697075,
                },
                {
                    'identifier': 5934986,
                    'width': 8851482330055941593,
                    'height': -2836839344974934408,
                },
                {
                    'identifier': 1894584,
                    'width': -8319630152325929406,
                    'height': 4437794000742488297,
                },
                {
                    'identifier': 8195456,
                    'width': 8550384177351665653,
                    'height': 4779247509905320614,
                },
            ],
            'screen': [
                {
                    'source_monitor': 4121081,
                    'source_nw_x_pixel': -6613382483313179205,
                    'source_nw_y_pixel': -1576491355994216802,
                    'source_pixel_width': -1241258365419151733,
                    'source_pixel_height': -4094462338730503766,
                    'rotation': -7904318586020846147,
                    'virtual_nw_x_pixel': 1120681072,
                    'virtual_nw_y_pixel': -200781104,
                    'virtual_width': 143661813,
                    'virtual_height': -150755179,
                },
                {
                    'source_monitor': 3478139,
                    'source_nw_x_pixel': -8044110802164431403,
                    'source_nw_y_pixel': -5774615619282770607,
                    'source_pixel_width': -2993059353373541077,
                    'source_pixel_height': -394159282167166786,
                    'rotation': -7022313342011489746,
                    'virtual_nw_x_pixel': -509218642,
                    'virtual_nw_y_pixel': -791840838,
                    'virtual_width': 1281961256,
                    'virtual_height': -598893579,
                },
                {
                    'source_monitor': 4141812,
                    'source_nw_x_pixel': -2211167701504456624,
                    'source_nw_y_pixel': -8162350008558128779,
                    'source_pixel_width': -8021949145321414140,
                    'source_pixel_height': -5729002309921914298,
                    'rotation': -6363595910959806388,
                    'virtual_nw_x_pixel': -1247047207,
                    'virtual_nw_y_pixel': 1087274551,
                    'virtual_width': -221625669,
                    'virtual_height': 645832487,
                },
                {
                    'source_monitor': -25288,
                    'source_nw_x_pixel': -3695545556124189182,
                    'source_nw_y_pixel': -3520128131167413847,
                    'source_pixel_width': -6783753170497365237,
                    'source_pixel_height': -3625092026893934590,
                    'rotation': -684746389200628299,
                    'virtual_nw_x_pixel': 228165517,
                    'virtual_nw_y_pixel': 1602569156,
                    'virtual_width': -738048745,
                    'virtual_height': 1679262622,
                },
                {
                    'source_monitor': -673025,
                    'source_nw_x_pixel': -1671529097540403536,
                    'source_nw_y_pixel': -5016867672257521995,
                    'source_pixel_width': -5841866006854662073,
                    'source_pixel_height': -652334267527455920,
                    'rotation': -8332744979182079495,
                    'virtual_nw_x_pixel': 558462748,
                    'virtual_nw_y_pixel': 1857295239,
                    'virtual_width': 1047709269,
                    'virtual_height': 1550763543,
                },
                {
                    'source_monitor': 2921580,
                    'source_nw_x_pixel': -1284957771304239133,
                    'source_nw_y_pixel': -731031286677751893,
                    'source_pixel_width': -1477142903254868779,
                    'source_pixel_height': -8989362121583698841,
                    'rotation': -9199764778466086912,
                    'virtual_nw_x_pixel': 880535924,
                    'virtual_nw_y_pixel': -1928182469,
                    'virtual_width': -1614913057,
                    'virtual_height': 194722281,
                },
                {
                    'source_monitor': 2633529,
                    'source_nw_x_pixel': -1547648251057319076,
                    'source_nw_y_pixel': -4978937419215558799,
                    'source_pixel_width': -4921689041726003773,
                    'source_pixel_height': -6762452492641919745,
                    'rotation': -8549920472245956644,
                    'virtual_nw_x_pixel': -785305032,
                    'virtual_nw_y_pixel': -932136326,
                    'virtual_width': -957330821,
                    'virtual_height': 1738073041,
                },
                {
                    'source_monitor': 3228306,
                    'source_nw_x_pixel': -6565509133395804084,
                    'source_nw_y_pixel': -6705429637241238056,
                    'source_pixel_width': -7128530324946660609,
                    'source_pixel_height': -6890600956399682418,
                    'rotation': -3882948920093424061,
                    'virtual_nw_x_pixel': 1430171655,
                    'virtual_nw_y_pixel': -1369270519,
                    'virtual_width': 1776777347,
                    'virtual_height': 1367567969,
                },
                {
                    'source_monitor': 8724558,
                    'source_nw_x_pixel': -371252414991159247,
                    'source_nw_y_pixel': -1214896815609551475,
                    'source_pixel_width': -4550936668780667789,
                    'source_pixel_height': -9008143998830951985,
                    'rotation': -3693131397656869668,
                    'virtual_nw_x_pixel': 907363296,
                    'virtual_nw_y_pixel': -398238477,
                    'virtual_width': -89254821,
                    'virtual_height': 786192491,
                },
                {
                    'source_monitor': 6467538,
                    'source_nw_x_pixel': -7550819352965073710,
                    'source_nw_y_pixel': -5876774386529666944,
                    'source_pixel_width': -3720791083384890769,
                    'source_pixel_height': -42693922859794947,
                    'rotation': -5073895840046768684,
                    'virtual_nw_x_pixel': 292926345,
                    'virtual_nw_y_pixel': 1778096466,
                    'virtual_width': 1854732652,
                    'virtual_height': -551538895,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 50893,
                    'width': -941075285665074196,
                    'height': 8295007824620578763,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -2896161020761228298,
                    'source_nw_y_pixel': -4434153311912411079,
                    'source_pixel_width': -665881904873565703,
                    'source_pixel_height': -3684219691332884710,
                    'rotation': -8674468892227396934,
                    'virtual_nw_x_pixel': 334233503,
                    'virtual_nw_y_pixel': 1156161103,
                    'virtual_width': -184597316,
                    'virtual_height': 1357852625,
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
            'request_id': 2520423,
            'mapped_screens_by_monitors': [
                {
                    'description': '\x83ыίˍȸØʬɛɽʩȁχΥɚύĽɒ\x94ѭЗƼǅϭϕ˨\x92µǶӱУ',
                    'monitors': [
                            {
                                        'identifier': 9854396,
                                        'width': -4005674413349914937,
                                        'height': -972351284159430320,
                                    },
                            {
                                        'identifier': 6092316,
                                        'width': 9017810846112263822,
                                        'height': -6271034872116629107,
                                    },
                            {
                                        'identifier': -380742,
                                        'width': 5769311698947960642,
                                        'height': -5715197321182366939,
                                    },
                            {
                                        'identifier': 37901,
                                        'width': -4987418829013945051,
                                        'height': -4169840175882253564,
                                    },
                            {
                                        'identifier': 5077176,
                                        'width': -7312141115380237751,
                                        'height': 3292960330113316420,
                                    },
                            {
                                        'identifier': 8114090,
                                        'width': 1728611761019129479,
                                        'height': 1577870276506065487,
                                    },
                            {
                                        'identifier': 4622976,
                                        'width': 2085787279160687419,
                                        'height': -5192059692903587261,
                                    },
                            {
                                        'identifier': 4061869,
                                        'width': -5024197415741510547,
                                        'height': 9147154811675990693,
                                    },
                            {
                                        'identifier': 6213090,
                                        'width': -4106133165035365835,
                                        'height': -8714689043750250317,
                                    },
                            {
                                        'identifier': 3568672,
                                        'width': 1352846412884920487,
                                        'height': -5920378409046161859,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -576780,
                                        'source_nw_x_pixel': -7969623956853561078,
                                        'source_nw_y_pixel': -2517542364226096696,
                                        'source_pixel_width': -1865688039896848802,
                                        'source_pixel_height': -6120547988555396808,
                                        'rotation': -512789760601767382,
                                        'virtual_nw_x_pixel': 576426955,
                                        'virtual_nw_y_pixel': 1303071297,
                                        'virtual_width': 1078635593,
                                        'virtual_height': 1396070020,
                                    },
                            {
                                        'source_monitor': 3126042,
                                        'source_nw_x_pixel': -2932242606419543265,
                                        'source_nw_y_pixel': -7848251047539021555,
                                        'source_pixel_width': -3846799482626705725,
                                        'source_pixel_height': -3047345102054328770,
                                        'rotation': -2131732324185873682,
                                        'virtual_nw_x_pixel': -442704744,
                                        'virtual_nw_y_pixel': 1236005943,
                                        'virtual_width': -1193818635,
                                        'virtual_height': -69967356,
                                    },
                            {
                                        'source_monitor': 6261460,
                                        'source_nw_x_pixel': -3733560466531288591,
                                        'source_nw_y_pixel': -7354705553725459587,
                                        'source_pixel_width': -7021994226081626453,
                                        'source_pixel_height': -6309162680023929364,
                                        'rotation': -3122466731373892008,
                                        'virtual_nw_x_pixel': 1004116768,
                                        'virtual_nw_y_pixel': -71750028,
                                        'virtual_width': 1469630682,
                                        'virtual_height': 1963532517,
                                    },
                            {
                                        'source_monitor': 2138612,
                                        'source_nw_x_pixel': -143032726843604941,
                                        'source_nw_y_pixel': -8486894790570836942,
                                        'source_pixel_width': -4715945021836401241,
                                        'source_pixel_height': -955635164012900138,
                                        'rotation': -8522558042372257654,
                                        'virtual_nw_x_pixel': -1753342275,
                                        'virtual_nw_y_pixel': 1809138180,
                                        'virtual_width': 714795937,
                                        'virtual_height': 163477534,
                                    },
                            {
                                        'source_monitor': 9847715,
                                        'source_nw_x_pixel': -6692815824133977505,
                                        'source_nw_y_pixel': -2306350554219648625,
                                        'source_pixel_width': -4324319654856899678,
                                        'source_pixel_height': -2434198113431836776,
                                        'rotation': -7707841579629856918,
                                        'virtual_nw_x_pixel': 886335316,
                                        'virtual_nw_y_pixel': 15208032,
                                        'virtual_width': -926718714,
                                        'virtual_height': -1272966339,
                                    },
                            {
                                        'source_monitor': 5926904,
                                        'source_nw_x_pixel': -3677381908600887029,
                                        'source_nw_y_pixel': -2940355202139428450,
                                        'source_pixel_width': -3683166457084167710,
                                        'source_pixel_height': -1270986965355089911,
                                        'rotation': -6300350411643804697,
                                        'virtual_nw_x_pixel': 1125391304,
                                        'virtual_nw_y_pixel': -1070303941,
                                        'virtual_width': 86843504,
                                        'virtual_height': -1059736019,
                                    },
                            {
                                        'source_monitor': 8410493,
                                        'source_nw_x_pixel': -8891797810760971934,
                                        'source_nw_y_pixel': -4008358274158350664,
                                        'source_pixel_width': -7744611410339253014,
                                        'source_pixel_height': -6910624844778012216,
                                        'rotation': -8505352750948764489,
                                        'virtual_nw_x_pixel': 1528482345,
                                        'virtual_nw_y_pixel': 695389872,
                                        'virtual_width': -1254970628,
                                        'virtual_height': -1393152193,
                                    },
                            {
                                        'source_monitor': 8984188,
                                        'source_nw_x_pixel': -7491116023849904579,
                                        'source_nw_y_pixel': -3737252509087511584,
                                        'source_pixel_width': -2169229655416666315,
                                        'source_pixel_height': -4649165239571172215,
                                        'rotation': -4995731906853189313,
                                        'virtual_nw_x_pixel': 502017326,
                                        'virtual_nw_y_pixel': -190298046,
                                        'virtual_width': 571152139,
                                        'virtual_height': -1032845565,
                                    },
                            {
                                        'source_monitor': 969536,
                                        'source_nw_x_pixel': -6385548374942508022,
                                        'source_nw_y_pixel': -5774951725764220044,
                                        'source_pixel_width': -760318921822160024,
                                        'source_pixel_height': -2488554612921876226,
                                        'rotation': -3812348734389791644,
                                        'virtual_nw_x_pixel': 405958415,
                                        'virtual_nw_y_pixel': -995432918,
                                        'virtual_width': -1280743305,
                                        'virtual_height': -1539209324,
                                    },
                            {
                                        'source_monitor': -572951,
                                        'source_nw_x_pixel': -4422570788666602199,
                                        'source_nw_y_pixel': -4030135257033805819,
                                        'source_pixel_width': -4421193742668757189,
                                        'source_pixel_height': -4834840044190338581,
                                        'rotation': -6796012828505635970,
                                        'virtual_nw_x_pixel': 343348696,
                                        'virtual_nw_y_pixel': -1223157332,
                                        'virtual_width': -1699151569,
                                        'virtual_height': -1904074543,
                                    },
                        ],
                },
                {
                    'description': 'ϸГз¢½ǝКȖĪE˫ˇȞӐĩ¥ЖƌҜӸ\x9eӱѫɭWӸϺϱĔw',
                    'monitors': [
                            {
                                        'identifier': 2934272,
                                        'width': -6339093721726700756,
                                        'height': -5587136754532971125,
                                    },
                            {
                                        'identifier': 9717711,
                                        'width': 2610007976985350172,
                                        'height': 6148470373925607356,
                                    },
                            {
                                        'identifier': 8205649,
                                        'width': -2575245147492055062,
                                        'height': 1422831121775393692,
                                    },
                            {
                                        'identifier': -740541,
                                        'width': 6559542087662508966,
                                        'height': -89388936093538294,
                                    },
                            {
                                        'identifier': 8396338,
                                        'width': 3205715889538840716,
                                        'height': -6997681320077319061,
                                    },
                            {
                                        'identifier': 5867555,
                                        'width': -2454527317246443140,
                                        'height': -2381825309606179399,
                                    },
                            {
                                        'identifier': 8002845,
                                        'width': -3668485134905496631,
                                        'height': -1061981704904392088,
                                    },
                            {
                                        'identifier': 7675283,
                                        'width': -7783285107839870558,
                                        'height': -1917274331914607010,
                                    },
                            {
                                        'identifier': 8652372,
                                        'width': 6359644067787520867,
                                        'height': 1853414342243501220,
                                    },
                            {
                                        'identifier': 7207490,
                                        'width': -3678874303787838773,
                                        'height': 3730277050637048356,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7180236,
                                        'source_nw_x_pixel': -8538213372646174204,
                                        'source_nw_y_pixel': -9147660785359243084,
                                        'source_pixel_width': -7124272328297364641,
                                        'source_pixel_height': -8617363275372311178,
                                        'rotation': -7752670782751738921,
                                        'virtual_nw_x_pixel': 1098864519,
                                        'virtual_nw_y_pixel': -1979990531,
                                        'virtual_width': 423652367,
                                        'virtual_height': 1013945870,
                                    },
                            {
                                        'source_monitor': 9918832,
                                        'source_nw_x_pixel': -433407931698577265,
                                        'source_nw_y_pixel': -4999150661721056399,
                                        'source_pixel_width': -1167873338925011935,
                                        'source_pixel_height': -5415906720432224777,
                                        'rotation': -1303765036121453099,
                                        'virtual_nw_x_pixel': -673277400,
                                        'virtual_nw_y_pixel': 1186614780,
                                        'virtual_width': -1353187925,
                                        'virtual_height': 1164841621,
                                    },
                            {
                                        'source_monitor': 3763211,
                                        'source_nw_x_pixel': -6429314891704444056,
                                        'source_nw_y_pixel': -707813948708204158,
                                        'source_pixel_width': -6786190227011888083,
                                        'source_pixel_height': -8950909987194506997,
                                        'rotation': -1978953027595395552,
                                        'virtual_nw_x_pixel': 1734941893,
                                        'virtual_nw_y_pixel': 117760905,
                                        'virtual_width': 1094924244,
                                        'virtual_height': -100850375,
                                    },
                            {
                                        'source_monitor': 6004311,
                                        'source_nw_x_pixel': -8219627954930285565,
                                        'source_nw_y_pixel': -21052095756251039,
                                        'source_pixel_width': -4704896253358495546,
                                        'source_pixel_height': -2598047564827191038,
                                        'rotation': -4171878318655512307,
                                        'virtual_nw_x_pixel': 1596603472,
                                        'virtual_nw_y_pixel': -1414790875,
                                        'virtual_width': 462474547,
                                        'virtual_height': -95792352,
                                    },
                            {
                                        'source_monitor': 2810547,
                                        'source_nw_x_pixel': -7740798937447150620,
                                        'source_nw_y_pixel': -6508256713773483754,
                                        'source_pixel_width': -4448904135984540722,
                                        'source_pixel_height': -6240929427034991147,
                                        'rotation': -6777610393493862800,
                                        'virtual_nw_x_pixel': -131227731,
                                        'virtual_nw_y_pixel': 803613624,
                                        'virtual_width': 1183134996,
                                        'virtual_height': -313935621,
                                    },
                            {
                                        'source_monitor': 4399945,
                                        'source_nw_x_pixel': -5737647554181581414,
                                        'source_nw_y_pixel': -3891664495492443859,
                                        'source_pixel_width': -8225758121032502224,
                                        'source_pixel_height': -5137824691458039815,
                                        'rotation': -679650192601111311,
                                        'virtual_nw_x_pixel': -1630495844,
                                        'virtual_nw_y_pixel': 1159466265,
                                        'virtual_width': -359949529,
                                        'virtual_height': -1531606198,
                                    },
                            {
                                        'source_monitor': 632787,
                                        'source_nw_x_pixel': -9105180837832905961,
                                        'source_nw_y_pixel': -2699320204266324903,
                                        'source_pixel_width': -5533662552151427468,
                                        'source_pixel_height': -4112627892966964042,
                                        'rotation': -4677981725952054775,
                                        'virtual_nw_x_pixel': 72486336,
                                        'virtual_nw_y_pixel': -275241885,
                                        'virtual_width': 1490777574,
                                        'virtual_height': -13180200,
                                    },
                            {
                                        'source_monitor': 4728320,
                                        'source_nw_x_pixel': -7945912108253019966,
                                        'source_nw_y_pixel': -7802732555714044866,
                                        'source_pixel_width': -7186528306772977341,
                                        'source_pixel_height': -3054233218183670302,
                                        'rotation': -1958116177048968046,
                                        'virtual_nw_x_pixel': -1157225426,
                                        'virtual_nw_y_pixel': -1897382648,
                                        'virtual_width': -1243400530,
                                        'virtual_height': 1571519476,
                                    },
                            {
                                        'source_monitor': 8495882,
                                        'source_nw_x_pixel': -8032705311630037295,
                                        'source_nw_y_pixel': -3547597643969122376,
                                        'source_pixel_width': -2244014065237071699,
                                        'source_pixel_height': -2588261567130551343,
                                        'rotation': -9055359628709521997,
                                        'virtual_nw_x_pixel': -571672172,
                                        'virtual_nw_y_pixel': 770598188,
                                        'virtual_width': -1679464500,
                                        'virtual_height': 1890794794,
                                    },
                            {
                                        'source_monitor': 4614882,
                                        'source_nw_x_pixel': -2740802991581869474,
                                        'source_nw_y_pixel': -8514316478597658922,
                                        'source_pixel_width': -9071123497353175150,
                                        'source_pixel_height': -3773493472869280659,
                                        'rotation': -608388532877202088,
                                        'virtual_nw_x_pixel': -1072202597,
                                        'virtual_nw_y_pixel': -982652687,
                                        'virtual_width': 1207090228,
                                        'virtual_height': 904442570,
                                    },
                        ],
                },
                {
                    'description': 'ӦСǽԘŕԍƙҍϳËѢĎɜȶŹ¡ňï¬ƃ½\x8eШԞƈɎʁɲώϮ',
                    'monitors': [
                            {
                                        'identifier': -753839,
                                        'width': 5036461711944126620,
                                        'height': 3947948923632570035,
                                    },
                            {
                                        'identifier': 7146096,
                                        'width': 3526474536762886824,
                                        'height': -101814336584766235,
                                    },
                            {
                                        'identifier': 8256830,
                                        'width': -7661874061947396603,
                                        'height': 4873476090866801495,
                                    },
                            {
                                        'identifier': 2308532,
                                        'width': -1483871155581404136,
                                        'height': -8672937786921927538,
                                    },
                            {
                                        'identifier': 9387901,
                                        'width': 730898491793331958,
                                        'height': -913062285712762827,
                                    },
                            {
                                        'identifier': 2447173,
                                        'width': 6935605121936224464,
                                        'height': -1390498833558596417,
                                    },
                            {
                                        'identifier': 5595421,
                                        'width': -4575071647867642399,
                                        'height': 668244970773929621,
                                    },
                            {
                                        'identifier': -933530,
                                        'width': 7430279635025134560,
                                        'height': -3286420660398981436,
                                    },
                            {
                                        'identifier': 1218908,
                                        'width': -4753720013084926126,
                                        'height': 717577458082363012,
                                    },
                            {
                                        'identifier': -987186,
                                        'width': -8359672843483835815,
                                        'height': 2323312140022347973,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 149071,
                                        'source_nw_x_pixel': -6219438353762464539,
                                        'source_nw_y_pixel': -754256234669632645,
                                        'source_pixel_width': -5283748687128181178,
                                        'source_pixel_height': -8768685830792764961,
                                        'rotation': -5279904862376046080,
                                        'virtual_nw_x_pixel': 817187626,
                                        'virtual_nw_y_pixel': -1910199509,
                                        'virtual_width': -1700699277,
                                        'virtual_height': -455190209,
                                    },
                            {
                                        'source_monitor': 8382789,
                                        'source_nw_x_pixel': -669895506129051899,
                                        'source_nw_y_pixel': -2799009478498749150,
                                        'source_pixel_width': -5708369182259421401,
                                        'source_pixel_height': -2863502482263084669,
                                        'rotation': -5564817092276666512,
                                        'virtual_nw_x_pixel': -1817457997,
                                        'virtual_nw_y_pixel': 379399750,
                                        'virtual_width': 66658417,
                                        'virtual_height': 1939062712,
                                    },
                            {
                                        'source_monitor': -596827,
                                        'source_nw_x_pixel': -6026927207697134962,
                                        'source_nw_y_pixel': -2321635622661063268,
                                        'source_pixel_width': -3705418534829387407,
                                        'source_pixel_height': -3805765707467703268,
                                        'rotation': -7196940803204876024,
                                        'virtual_nw_x_pixel': -671025433,
                                        'virtual_nw_y_pixel': -1489796035,
                                        'virtual_width': 733301112,
                                        'virtual_height': -1825251249,
                                    },
                            {
                                        'source_monitor': 7162475,
                                        'source_nw_x_pixel': -7180409549926704769,
                                        'source_nw_y_pixel': -1978309652661412736,
                                        'source_pixel_width': -6917502909355065715,
                                        'source_pixel_height': -3262562557968151450,
                                        'rotation': -6392544449628194486,
                                        'virtual_nw_x_pixel': 374648319,
                                        'virtual_nw_y_pixel': -844129908,
                                        'virtual_width': 253015956,
                                        'virtual_height': 1572545866,
                                    },
                            {
                                        'source_monitor': 4196192,
                                        'source_nw_x_pixel': -603185772403355071,
                                        'source_nw_y_pixel': -5289637853109236919,
                                        'source_pixel_width': -1974164626778492241,
                                        'source_pixel_height': -633718843410289173,
                                        'rotation': -8500523702286573169,
                                        'virtual_nw_x_pixel': 74880160,
                                        'virtual_nw_y_pixel': 659798031,
                                        'virtual_width': -993581835,
                                        'virtual_height': -1436536597,
                                    },
                            {
                                        'source_monitor': 8196245,
                                        'source_nw_x_pixel': -1491706590154740912,
                                        'source_nw_y_pixel': -6508717739838833406,
                                        'source_pixel_width': -2635490165778246783,
                                        'source_pixel_height': -4010612327510607676,
                                        'rotation': -2091015308011736229,
                                        'virtual_nw_x_pixel': -1076036250,
                                        'virtual_nw_y_pixel': 732382796,
                                        'virtual_width': 1783662174,
                                        'virtual_height': -1626781624,
                                    },
                            {
                                        'source_monitor': 5935897,
                                        'source_nw_x_pixel': -823334269965605578,
                                        'source_nw_y_pixel': -2178076217201826973,
                                        'source_pixel_width': -5449667701664621418,
                                        'source_pixel_height': -1095198287326500780,
                                        'rotation': -8178560040168166205,
                                        'virtual_nw_x_pixel': -417945704,
                                        'virtual_nw_y_pixel': -789483053,
                                        'virtual_width': -33105067,
                                        'virtual_height': 1815052693,
                                    },
                            {
                                        'source_monitor': 1039183,
                                        'source_nw_x_pixel': -3743160144795661245,
                                        'source_nw_y_pixel': -5409915528322925666,
                                        'source_pixel_width': -3986155065619232435,
                                        'source_pixel_height': -6800549867081540321,
                                        'rotation': -8872513487354473242,
                                        'virtual_nw_x_pixel': 1111631111,
                                        'virtual_nw_y_pixel': 1070318737,
                                        'virtual_width': -22468672,
                                        'virtual_height': 1433829029,
                                    },
                            {
                                        'source_monitor': 9926433,
                                        'source_nw_x_pixel': -428879472068864893,
                                        'source_nw_y_pixel': -2104339712665873999,
                                        'source_pixel_width': -1830049819940704599,
                                        'source_pixel_height': -7599789896196063099,
                                        'rotation': -1411745210805747362,
                                        'virtual_nw_x_pixel': -1383695960,
                                        'virtual_nw_y_pixel': 1181721539,
                                        'virtual_width': -1398049240,
                                        'virtual_height': 611305631,
                                    },
                            {
                                        'source_monitor': 8341160,
                                        'source_nw_x_pixel': -4307890677930959485,
                                        'source_nw_y_pixel': -5833674565861180141,
                                        'source_pixel_width': -183229619521324374,
                                        'source_pixel_height': -7097427340611248013,
                                        'rotation': -1740530457999956945,
                                        'virtual_nw_x_pixel': -1728581665,
                                        'virtual_nw_y_pixel': -348797177,
                                        'virtual_width': -394267114,
                                        'virtual_height': -1302330247,
                                    },
                        ],
                },
                {
                    'description': 'өżЃ\x9dΏǕʭ\x9fƏɜƢԑǓʛѡѴÃ˓ɶ˻ˏϙĘˉĿϟ&ÎǫŰ',
                    'monitors': [
                            {
                                        'identifier': 716140,
                                        'width': -4404954190746889475,
                                        'height': 2175269884135561941,
                                    },
                            {
                                        'identifier': 7243103,
                                        'width': 3657676901060892040,
                                        'height': 8785945466379565662,
                                    },
                            {
                                        'identifier': 5134596,
                                        'width': 1665760140919842253,
                                        'height': 5728086435988508154,
                                    },
                            {
                                        'identifier': 3119309,
                                        'width': 1629823438570614777,
                                        'height': 496198325403223641,
                                    },
                            {
                                        'identifier': 2837738,
                                        'width': -3431442473638195031,
                                        'height': 1165815405378901456,
                                    },
                            {
                                        'identifier': 7299667,
                                        'width': 5658845151707309273,
                                        'height': -4167532596927141906,
                                    },
                            {
                                        'identifier': 365570,
                                        'width': 6084502753990144025,
                                        'height': 2271872472786856378,
                                    },
                            {
                                        'identifier': 13256,
                                        'width': -1925759651793472788,
                                        'height': 7569814489718453501,
                                    },
                            {
                                        'identifier': 3464364,
                                        'width': -3675887042250386935,
                                        'height': 6863774976410720671,
                                    },
                            {
                                        'identifier': 9877487,
                                        'width': -438461892485268507,
                                        'height': 7119266648382034438,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4504112,
                                        'source_nw_x_pixel': -293776909024425179,
                                        'source_nw_y_pixel': -4621136583443596004,
                                        'source_pixel_width': -3929586761173827842,
                                        'source_pixel_height': -2899142519623414366,
                                        'rotation': -3872478002073806741,
                                        'virtual_nw_x_pixel': 1680251387,
                                        'virtual_nw_y_pixel': -758342298,
                                        'virtual_width': -887669057,
                                        'virtual_height': -904274987,
                                    },
                            {
                                        'source_monitor': 8838683,
                                        'source_nw_x_pixel': -181086410196820616,
                                        'source_nw_y_pixel': -2794885858862220172,
                                        'source_pixel_width': -6954936320564535671,
                                        'source_pixel_height': -5596638958044602311,
                                        'rotation': -4221810515415804264,
                                        'virtual_nw_x_pixel': -783099164,
                                        'virtual_nw_y_pixel': 1478955087,
                                        'virtual_width': 1451512627,
                                        'virtual_height': -1262740025,
                                    },
                            {
                                        'source_monitor': 3363369,
                                        'source_nw_x_pixel': -5334581372881784812,
                                        'source_nw_y_pixel': -5030414108264254784,
                                        'source_pixel_width': -1291870716015982173,
                                        'source_pixel_height': -4204501364449058934,
                                        'rotation': -2776446463720116523,
                                        'virtual_nw_x_pixel': 740478346,
                                        'virtual_nw_y_pixel': -352233213,
                                        'virtual_width': -554464582,
                                        'virtual_height': 1904917018,
                                    },
                            {
                                        'source_monitor': -986629,
                                        'source_nw_x_pixel': -6266055717810401380,
                                        'source_nw_y_pixel': -962212706799802552,
                                        'source_pixel_width': -6282838787661386880,
                                        'source_pixel_height': -2087709850682622816,
                                        'rotation': -3447521497315464885,
                                        'virtual_nw_x_pixel': 1363242224,
                                        'virtual_nw_y_pixel': -1991502889,
                                        'virtual_width': 413617740,
                                        'virtual_height': 1343996023,
                                    },
                            {
                                        'source_monitor': 5247741,
                                        'source_nw_x_pixel': -3402215378201986813,
                                        'source_nw_y_pixel': -1441751128941471693,
                                        'source_pixel_width': -560912142927659486,
                                        'source_pixel_height': -1563059110894049646,
                                        'rotation': -2470052790867742529,
                                        'virtual_nw_x_pixel': 1821745228,
                                        'virtual_nw_y_pixel': 668025040,
                                        'virtual_width': -899597521,
                                        'virtual_height': -72815702,
                                    },
                            {
                                        'source_monitor': 4930115,
                                        'source_nw_x_pixel': -2079182936981136376,
                                        'source_nw_y_pixel': -5897040911255840193,
                                        'source_pixel_width': -161318916116064615,
                                        'source_pixel_height': -8194939796810473838,
                                        'rotation': -3712225926743199698,
                                        'virtual_nw_x_pixel': -1058740125,
                                        'virtual_nw_y_pixel': 1947717975,
                                        'virtual_width': 771526844,
                                        'virtual_height': 1513318925,
                                    },
                            {
                                        'source_monitor': -572458,
                                        'source_nw_x_pixel': -2396444183671785374,
                                        'source_nw_y_pixel': -1545797043876741942,
                                        'source_pixel_width': -7107095708934638178,
                                        'source_pixel_height': -5552111557471224847,
                                        'rotation': -1532499459916288559,
                                        'virtual_nw_x_pixel': 785853341,
                                        'virtual_nw_y_pixel': -1957589303,
                                        'virtual_width': 1242133704,
                                        'virtual_height': -1876579948,
                                    },
                            {
                                        'source_monitor': 5463986,
                                        'source_nw_x_pixel': -7724402503421398,
                                        'source_nw_y_pixel': -5227213242650968305,
                                        'source_pixel_width': -5073325278377580620,
                                        'source_pixel_height': -2458047150459804595,
                                        'rotation': -7209463797128201978,
                                        'virtual_nw_x_pixel': 109883123,
                                        'virtual_nw_y_pixel': 175183263,
                                        'virtual_width': -1944496371,
                                        'virtual_height': -1671302968,
                                    },
                            {
                                        'source_monitor': 7959338,
                                        'source_nw_x_pixel': -5418225947301363285,
                                        'source_nw_y_pixel': -8111710178696075545,
                                        'source_pixel_width': -5984927913758875542,
                                        'source_pixel_height': -2021950845894799348,
                                        'rotation': -4045520938255869118,
                                        'virtual_nw_x_pixel': -368055412,
                                        'virtual_nw_y_pixel': -443732435,
                                        'virtual_width': -1330463485,
                                        'virtual_height': -1010886266,
                                    },
                            {
                                        'source_monitor': 1456515,
                                        'source_nw_x_pixel': -5509179587522113376,
                                        'source_nw_y_pixel': -5619224535180663436,
                                        'source_pixel_width': -8654606216616012609,
                                        'source_pixel_height': -1710300165255392274,
                                        'rotation': -6905970194121669392,
                                        'virtual_nw_x_pixel': -1975915476,
                                        'virtual_nw_y_pixel': -950098432,
                                        'virtual_width': -1818544233,
                                        'virtual_height': -321813018,
                                    },
                        ],
                },
                {
                    'description': 'ȃϥÄ\x97˙ǼԜĮѐœǤԥΐɠ?ͱүԅ\x85ƬͰʳɆ\u0382ϙӆ\x94җȋ¿',
                    'monitors': [
                            {
                                        'identifier': -918301,
                                        'width': -4927192304316753971,
                                        'height': 3416808240132543268,
                                    },
                            {
                                        'identifier': 355085,
                                        'width': 790348570367369470,
                                        'height': 4972467388866004811,
                                    },
                            {
                                        'identifier': 7565693,
                                        'width': -7595435076614418354,
                                        'height': 8289556163362142246,
                                    },
                            {
                                        'identifier': 1425089,
                                        'width': -7422061415006047827,
                                        'height': 1731396482404349611,
                                    },
                            {
                                        'identifier': -401504,
                                        'width': -5709658960579185987,
                                        'height': -7352209094872561780,
                                    },
                            {
                                        'identifier': 5376096,
                                        'width': 3563151345063083448,
                                        'height': -5814273908424502816,
                                    },
                            {
                                        'identifier': 9081832,
                                        'width': 1777273072764291127,
                                        'height': -5373208492591327062,
                                    },
                            {
                                        'identifier': 8791096,
                                        'width': 2933028966351206510,
                                        'height': 29741007557831096,
                                    },
                            {
                                        'identifier': -884096,
                                        'width': -6845700120259275404,
                                        'height': 3514356792672445449,
                                    },
                            {
                                        'identifier': 3588158,
                                        'width': -8536143845130748644,
                                        'height': 5036079064405129646,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2847667,
                                        'source_nw_x_pixel': -1198314162675064954,
                                        'source_nw_y_pixel': -7101466027238722488,
                                        'source_pixel_width': -8280632848264636277,
                                        'source_pixel_height': -2852542556287035903,
                                        'rotation': -3067524068111392767,
                                        'virtual_nw_x_pixel': 319677786,
                                        'virtual_nw_y_pixel': 1760052212,
                                        'virtual_width': 1079720182,
                                        'virtual_height': 760379676,
                                    },
                            {
                                        'source_monitor': 6338259,
                                        'source_nw_x_pixel': -4226899100580574765,
                                        'source_nw_y_pixel': -8740698347357872689,
                                        'source_pixel_width': -5614917609807188609,
                                        'source_pixel_height': -5541548475002469562,
                                        'rotation': -3942160691656311864,
                                        'virtual_nw_x_pixel': -1703434236,
                                        'virtual_nw_y_pixel': -278875401,
                                        'virtual_width': 931756717,
                                        'virtual_height': -1797919578,
                                    },
                            {
                                        'source_monitor': 5775787,
                                        'source_nw_x_pixel': -1491983315007255089,
                                        'source_nw_y_pixel': -6830614141952032465,
                                        'source_pixel_width': -2154352252738787567,
                                        'source_pixel_height': -6659489849582583322,
                                        'rotation': -7221660700954299182,
                                        'virtual_nw_x_pixel': 1033979338,
                                        'virtual_nw_y_pixel': 1173780657,
                                        'virtual_width': 590996848,
                                        'virtual_height': 1493739330,
                                    },
                            {
                                        'source_monitor': 2900801,
                                        'source_nw_x_pixel': -7600124514997134686,
                                        'source_nw_y_pixel': -4236944921003902630,
                                        'source_pixel_width': -7060523859045807277,
                                        'source_pixel_height': -9093513400379980193,
                                        'rotation': -1032377314964949765,
                                        'virtual_nw_x_pixel': -183230222,
                                        'virtual_nw_y_pixel': -1021965184,
                                        'virtual_width': 1137674503,
                                        'virtual_height': -1299525943,
                                    },
                            {
                                        'source_monitor': -796722,
                                        'source_nw_x_pixel': -4219421138432384684,
                                        'source_nw_y_pixel': -8453217031353865925,
                                        'source_pixel_width': -8454122133575867682,
                                        'source_pixel_height': -7856652181094788652,
                                        'rotation': -7743095031687467546,
                                        'virtual_nw_x_pixel': 1824512211,
                                        'virtual_nw_y_pixel': -1713874951,
                                        'virtual_width': 1923873884,
                                        'virtual_height': -1612043802,
                                    },
                            {
                                        'source_monitor': 8003777,
                                        'source_nw_x_pixel': -5263042835757517162,
                                        'source_nw_y_pixel': -7712035077156119469,
                                        'source_pixel_width': -8955967472664751731,
                                        'source_pixel_height': -3916060484815757179,
                                        'rotation': -1282172212860407315,
                                        'virtual_nw_x_pixel': -93997996,
                                        'virtual_nw_y_pixel': 94554010,
                                        'virtual_width': -27313251,
                                        'virtual_height': 216227451,
                                    },
                            {
                                        'source_monitor': 84178,
                                        'source_nw_x_pixel': -9167043877488418759,
                                        'source_nw_y_pixel': -7511569699236539247,
                                        'source_pixel_width': -944314876765769748,
                                        'source_pixel_height': -109019844806897758,
                                        'rotation': -6387332564561620436,
                                        'virtual_nw_x_pixel': -280058305,
                                        'virtual_nw_y_pixel': -888272987,
                                        'virtual_width': 1275509923,
                                        'virtual_height': -440984253,
                                    },
                            {
                                        'source_monitor': 2881426,
                                        'source_nw_x_pixel': -2587949988214758615,
                                        'source_nw_y_pixel': -1199221249692696108,
                                        'source_pixel_width': -3795576654293742588,
                                        'source_pixel_height': -7349439881807607759,
                                        'rotation': -1709239100361831019,
                                        'virtual_nw_x_pixel': 1966128745,
                                        'virtual_nw_y_pixel': 407921121,
                                        'virtual_width': -355644055,
                                        'virtual_height': -1421752486,
                                    },
                            {
                                        'source_monitor': 6892488,
                                        'source_nw_x_pixel': -8982315851743709521,
                                        'source_nw_y_pixel': -5491645235572553741,
                                        'source_pixel_width': -3414896419692521337,
                                        'source_pixel_height': -7328158526502830954,
                                        'rotation': -9113933830696190034,
                                        'virtual_nw_x_pixel': -762399293,
                                        'virtual_nw_y_pixel': -306833969,
                                        'virtual_width': -571130882,
                                        'virtual_height': 308297861,
                                    },
                            {
                                        'source_monitor': 8640810,
                                        'source_nw_x_pixel': -6841441643514260592,
                                        'source_nw_y_pixel': -588367331822961303,
                                        'source_pixel_width': -7043611107973858818,
                                        'source_pixel_height': -5116908535196686859,
                                        'rotation': -895082610717353141,
                                        'virtual_nw_x_pixel': 1502354630,
                                        'virtual_nw_y_pixel': 833777672,
                                        'virtual_width': -768490777,
                                        'virtual_height': 1118178565,
                                    },
                        ],
                },
                {
                    'description': 'ǘΔӴҀţѬҊʚÛξĞʓϮқКǊƩƿĚΦǛſ\x8dͲšϩʽϑψЇ',
                    'monitors': [
                            {
                                        'identifier': 5689558,
                                        'width': 6123007377287047217,
                                        'height': 7020045406017917579,
                                    },
                            {
                                        'identifier': 848026,
                                        'width': 5395273913811704167,
                                        'height': 8500703506051727081,
                                    },
                            {
                                        'identifier': 3630382,
                                        'width': -5517066331113330262,
                                        'height': -8971636775424907578,
                                    },
                            {
                                        'identifier': 5198916,
                                        'width': 4785413825118037104,
                                        'height': -6195005120244742143,
                                    },
                            {
                                        'identifier': 8765145,
                                        'width': -4066636868016658964,
                                        'height': -4885774606735682068,
                                    },
                            {
                                        'identifier': -484312,
                                        'width': 3909338931402954671,
                                        'height': -1257221750337261909,
                                    },
                            {
                                        'identifier': 4087103,
                                        'width': -4289115724340290301,
                                        'height': 5006413360065743806,
                                    },
                            {
                                        'identifier': -787268,
                                        'width': 5766234141188405633,
                                        'height': 6197182117346101946,
                                    },
                            {
                                        'identifier': 4178915,
                                        'width': -6718197804275601084,
                                        'height': 9034116396723214244,
                                    },
                            {
                                        'identifier': 5155218,
                                        'width': -8418856907818950183,
                                        'height': -5000870382890631249,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -333139,
                                        'source_nw_x_pixel': -6854069042138214884,
                                        'source_nw_y_pixel': -515950959763978096,
                                        'source_pixel_width': -2526056555232878612,
                                        'source_pixel_height': -9087554491372762093,
                                        'rotation': -7710022198489018799,
                                        'virtual_nw_x_pixel': 464100268,
                                        'virtual_nw_y_pixel': -1103462646,
                                        'virtual_width': -1372882287,
                                        'virtual_height': 1232091847,
                                    },
                            {
                                        'source_monitor': 2346897,
                                        'source_nw_x_pixel': -6702336089128537756,
                                        'source_nw_y_pixel': -8013982737547024396,
                                        'source_pixel_width': -7295657234904702002,
                                        'source_pixel_height': -7434336619117096901,
                                        'rotation': -8137945275121802722,
                                        'virtual_nw_x_pixel': -1164429182,
                                        'virtual_nw_y_pixel': 1881663685,
                                        'virtual_width': -357838733,
                                        'virtual_height': 753205372,
                                    },
                            {
                                        'source_monitor': 9415860,
                                        'source_nw_x_pixel': -1263829195246744693,
                                        'source_nw_y_pixel': -4134362607783805647,
                                        'source_pixel_width': -9127677552847092615,
                                        'source_pixel_height': -1778595475490944095,
                                        'rotation': -7822442252231394711,
                                        'virtual_nw_x_pixel': -1489617531,
                                        'virtual_nw_y_pixel': -1895304549,
                                        'virtual_width': -139184929,
                                        'virtual_height': -362305485,
                                    },
                            {
                                        'source_monitor': 8419386,
                                        'source_nw_x_pixel': -767189386985814728,
                                        'source_nw_y_pixel': -2671627015636116933,
                                        'source_pixel_width': -2920088465229786995,
                                        'source_pixel_height': -2102867906349718242,
                                        'rotation': -2800345140598254255,
                                        'virtual_nw_x_pixel': 884904757,
                                        'virtual_nw_y_pixel': -4389450,
                                        'virtual_width': -286450229,
                                        'virtual_height': -1428607958,
                                    },
                            {
                                        'source_monitor': 3007021,
                                        'source_nw_x_pixel': -7784799986151032519,
                                        'source_nw_y_pixel': -8879808334065903934,
                                        'source_pixel_width': -6547499517528993222,
                                        'source_pixel_height': -8425582513752418744,
                                        'rotation': -5995460643015422112,
                                        'virtual_nw_x_pixel': -1868166225,
                                        'virtual_nw_y_pixel': -1673754938,
                                        'virtual_width': 1393882344,
                                        'virtual_height': -290753662,
                                    },
                            {
                                        'source_monitor': 6899037,
                                        'source_nw_x_pixel': -2521098079559262699,
                                        'source_nw_y_pixel': -7071779692110365372,
                                        'source_pixel_width': -8838587249330088339,
                                        'source_pixel_height': -4433275879912513987,
                                        'rotation': -2883512089567249314,
                                        'virtual_nw_x_pixel': 30962807,
                                        'virtual_nw_y_pixel': 1656776347,
                                        'virtual_width': 1041683235,
                                        'virtual_height': -1704207880,
                                    },
                            {
                                        'source_monitor': 1214896,
                                        'source_nw_x_pixel': -5988766844767432705,
                                        'source_nw_y_pixel': -4518139589270570787,
                                        'source_pixel_width': -8848805175426708128,
                                        'source_pixel_height': -1527907759754454198,
                                        'rotation': -3568645070605519671,
                                        'virtual_nw_x_pixel': 185085505,
                                        'virtual_nw_y_pixel': 1666195833,
                                        'virtual_width': -1181713300,
                                        'virtual_height': 1953607667,
                                    },
                            {
                                        'source_monitor': 9338854,
                                        'source_nw_x_pixel': -766361571625764657,
                                        'source_nw_y_pixel': -8582351984820093612,
                                        'source_pixel_width': -6035828853706918420,
                                        'source_pixel_height': -3473684828470843905,
                                        'rotation': -444212948971265350,
                                        'virtual_nw_x_pixel': 840844011,
                                        'virtual_nw_y_pixel': -817778816,
                                        'virtual_width': -922593179,
                                        'virtual_height': -1401109443,
                                    },
                            {
                                        'source_monitor': 5789746,
                                        'source_nw_x_pixel': -3944740416184574182,
                                        'source_nw_y_pixel': -7809072323822869915,
                                        'source_pixel_width': -7325143974308239905,
                                        'source_pixel_height': -3640786476817176543,
                                        'rotation': -7620937528248703754,
                                        'virtual_nw_x_pixel': -1336650562,
                                        'virtual_nw_y_pixel': -1821570439,
                                        'virtual_width': -593131382,
                                        'virtual_height': 1237899089,
                                    },
                            {
                                        'source_monitor': 8246536,
                                        'source_nw_x_pixel': -4265129685206909306,
                                        'source_nw_y_pixel': -6290237788937417589,
                                        'source_pixel_width': -297040027627687915,
                                        'source_pixel_height': -4564738234565470517,
                                        'rotation': -9147431155387452079,
                                        'virtual_nw_x_pixel': -1162294389,
                                        'virtual_nw_y_pixel': -1077049963,
                                        'virtual_width': 336509181,
                                        'virtual_height': -701170687,
                                    },
                        ],
                },
                {
                    'description': 'Ĥһ½žƂǷɺıĒΥΖШƹËƥсȬɻԦÝ˩ƔüƋĵϠϥɻĝЏ',
                    'monitors': [
                            {
                                        'identifier': 9056011,
                                        'width': 2262456646389474720,
                                        'height': 3825461291955313198,
                                    },
                            {
                                        'identifier': 3837477,
                                        'width': -2989339723666116325,
                                        'height': -4705820474908504330,
                                    },
                            {
                                        'identifier': 3047522,
                                        'width': -2901217574425039458,
                                        'height': -2222845361827458924,
                                    },
                            {
                                        'identifier': 5191483,
                                        'width': -8197094136282428534,
                                        'height': -9192350244921310597,
                                    },
                            {
                                        'identifier': 537172,
                                        'width': -2428110206235995079,
                                        'height': -622911545851410065,
                                    },
                            {
                                        'identifier': 7569068,
                                        'width': -4818496794239582706,
                                        'height': -2919989457845739400,
                                    },
                            {
                                        'identifier': 939953,
                                        'width': -655072577110404584,
                                        'height': 7159219609075714855,
                                    },
                            {
                                        'identifier': 8072451,
                                        'width': -8783139138375644805,
                                        'height': 5546238192677900800,
                                    },
                            {
                                        'identifier': 7437775,
                                        'width': -2066601066898317947,
                                        'height': 4402398834415438979,
                                    },
                            {
                                        'identifier': 7535574,
                                        'width': 1628992367869267889,
                                        'height': -8963926810459446333,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1719507,
                                        'source_nw_x_pixel': -4100541756198169048,
                                        'source_nw_y_pixel': -5686720424302223436,
                                        'source_pixel_width': -6120848416565244004,
                                        'source_pixel_height': -7868656189075897526,
                                        'rotation': -1050843044460010714,
                                        'virtual_nw_x_pixel': 1900902767,
                                        'virtual_nw_y_pixel': 421239680,
                                        'virtual_width': 1296175769,
                                        'virtual_height': -227894737,
                                    },
                            {
                                        'source_monitor': -821911,
                                        'source_nw_x_pixel': -1915222633500327115,
                                        'source_nw_y_pixel': -2122279673242889794,
                                        'source_pixel_width': -843986484799931874,
                                        'source_pixel_height': -3958885704895838934,
                                        'rotation': -7107345359531499369,
                                        'virtual_nw_x_pixel': 1632129739,
                                        'virtual_nw_y_pixel': -1763225159,
                                        'virtual_width': -1134923235,
                                        'virtual_height': 1041626040,
                                    },
                            {
                                        'source_monitor': 7913161,
                                        'source_nw_x_pixel': -785543505094403464,
                                        'source_nw_y_pixel': -3091550279333364687,
                                        'source_pixel_width': -7950986694459255150,
                                        'source_pixel_height': -6390956173229424018,
                                        'rotation': -859403332692425033,
                                        'virtual_nw_x_pixel': 155182369,
                                        'virtual_nw_y_pixel': 959120083,
                                        'virtual_width': 302374484,
                                        'virtual_height': 1153187703,
                                    },
                            {
                                        'source_monitor': 1090994,
                                        'source_nw_x_pixel': -8918367455345892366,
                                        'source_nw_y_pixel': -5069727857656398248,
                                        'source_pixel_width': -7999644299322533696,
                                        'source_pixel_height': -4072205663948858208,
                                        'rotation': -3912442300078575109,
                                        'virtual_nw_x_pixel': -721762397,
                                        'virtual_nw_y_pixel': 859914122,
                                        'virtual_width': 950428687,
                                        'virtual_height': 1938965612,
                                    },
                            {
                                        'source_monitor': 888672,
                                        'source_nw_x_pixel': -519657575965508347,
                                        'source_nw_y_pixel': -1346099624180603649,
                                        'source_pixel_width': -4477718371063136519,
                                        'source_pixel_height': -6479093665028217679,
                                        'rotation': -2096913674059696615,
                                        'virtual_nw_x_pixel': -1029898309,
                                        'virtual_nw_y_pixel': -854315849,
                                        'virtual_width': -94757873,
                                        'virtual_height': 1504758155,
                                    },
                            {
                                        'source_monitor': 9176892,
                                        'source_nw_x_pixel': -6194969021709316428,
                                        'source_nw_y_pixel': -2932935006231305473,
                                        'source_pixel_width': -6396791250606528931,
                                        'source_pixel_height': -7574457382994292459,
                                        'rotation': -8054627662434365748,
                                        'virtual_nw_x_pixel': 330323503,
                                        'virtual_nw_y_pixel': 458132021,
                                        'virtual_width': 1413187152,
                                        'virtual_height': -714321926,
                                    },
                            {
                                        'source_monitor': 5379857,
                                        'source_nw_x_pixel': -2684774431409724373,
                                        'source_nw_y_pixel': -8332867731787042579,
                                        'source_pixel_width': -8573574195926745913,
                                        'source_pixel_height': -7923071559230630613,
                                        'rotation': -7918555447766144961,
                                        'virtual_nw_x_pixel': -562326249,
                                        'virtual_nw_y_pixel': 885089870,
                                        'virtual_width': -1175698008,
                                        'virtual_height': 774695980,
                                    },
                            {
                                        'source_monitor': -226895,
                                        'source_nw_x_pixel': -1714810543760990607,
                                        'source_nw_y_pixel': -5380120511465633926,
                                        'source_pixel_width': -3757892555538121411,
                                        'source_pixel_height': -2729041557419396418,
                                        'rotation': -8762960945669445062,
                                        'virtual_nw_x_pixel': -788905795,
                                        'virtual_nw_y_pixel': 1468168089,
                                        'virtual_width': 118452069,
                                        'virtual_height': 1443384269,
                                    },
                            {
                                        'source_monitor': 1297698,
                                        'source_nw_x_pixel': -3620083569127466028,
                                        'source_nw_y_pixel': -2806652268698291727,
                                        'source_pixel_width': -40535845401554206,
                                        'source_pixel_height': -1229270814198084115,
                                        'rotation': -8146618912931387549,
                                        'virtual_nw_x_pixel': 355145505,
                                        'virtual_nw_y_pixel': 1542632374,
                                        'virtual_width': 1288867767,
                                        'virtual_height': 820900426,
                                    },
                            {
                                        'source_monitor': 8857019,
                                        'source_nw_x_pixel': -4207879378038876779,
                                        'source_nw_y_pixel': -6236835525418595514,
                                        'source_pixel_width': -547874669316614039,
                                        'source_pixel_height': -1280811599839109688,
                                        'rotation': -7182458796762619323,
                                        'virtual_nw_x_pixel': -1978780693,
                                        'virtual_nw_y_pixel': 1946663149,
                                        'virtual_width': 215685024,
                                        'virtual_height': 356621155,
                                    },
                        ],
                },
                {
                    'description': 'Éˀγδ$ƼѭԝʥřІùƭʯ˰#ƩǻƊøΉҢɮȼɻƯϴūŶʵ',
                    'monitors': [
                            {
                                        'identifier': 793347,
                                        'width': 5430191636144358194,
                                        'height': -4602557708202288754,
                                    },
                            {
                                        'identifier': 453450,
                                        'width': 1806007612833534674,
                                        'height': 628664110025509643,
                                    },
                            {
                                        'identifier': 2293249,
                                        'width': 6747477479402534970,
                                        'height': 664882579167149985,
                                    },
                            {
                                        'identifier': 9870239,
                                        'width': 2789218396384517234,
                                        'height': 785319139983576979,
                                    },
                            {
                                        'identifier': 4794830,
                                        'width': 7253569591061654397,
                                        'height': -4155239016068053278,
                                    },
                            {
                                        'identifier': 4757123,
                                        'width': -2199846418953781120,
                                        'height': -8867246169575839276,
                                    },
                            {
                                        'identifier': 925030,
                                        'width': -3998303980923112779,
                                        'height': -3144320639810853446,
                                    },
                            {
                                        'identifier': 9918928,
                                        'width': -2628765680414664883,
                                        'height': -6039322037973366249,
                                    },
                            {
                                        'identifier': 1754200,
                                        'width': 1503425579446388893,
                                        'height': -3696473192511819767,
                                    },
                            {
                                        'identifier': 8167650,
                                        'width': -4649201322061450416,
                                        'height': -2828733910424802762,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3327760,
                                        'source_nw_x_pixel': -8728938578619334212,
                                        'source_nw_y_pixel': -7094042842143615221,
                                        'source_pixel_width': -3542057107089772635,
                                        'source_pixel_height': -1659354629886700127,
                                        'rotation': -4032081579495886620,
                                        'virtual_nw_x_pixel': 918838674,
                                        'virtual_nw_y_pixel': 693142871,
                                        'virtual_width': -79143930,
                                        'virtual_height': 1619289780,
                                    },
                            {
                                        'source_monitor': 9556055,
                                        'source_nw_x_pixel': -7626023716448546568,
                                        'source_nw_y_pixel': -7393747213686987914,
                                        'source_pixel_width': -4543811419385283494,
                                        'source_pixel_height': -3641308308850725669,
                                        'rotation': -6796192082925638582,
                                        'virtual_nw_x_pixel': -1923487494,
                                        'virtual_nw_y_pixel': -937085926,
                                        'virtual_width': 912071925,
                                        'virtual_height': 1995064996,
                                    },
                            {
                                        'source_monitor': 2839268,
                                        'source_nw_x_pixel': -1885607345860170234,
                                        'source_nw_y_pixel': -7510856909024199818,
                                        'source_pixel_width': -1895186306626699491,
                                        'source_pixel_height': -6746241715006016307,
                                        'rotation': -6233537477969949397,
                                        'virtual_nw_x_pixel': 307312616,
                                        'virtual_nw_y_pixel': -535958384,
                                        'virtual_width': 256897228,
                                        'virtual_height': 1005836880,
                                    },
                            {
                                        'source_monitor': 9855585,
                                        'source_nw_x_pixel': -8138397156371933165,
                                        'source_nw_y_pixel': -840559371564437603,
                                        'source_pixel_width': -8202429456637329247,
                                        'source_pixel_height': -1974362686461761571,
                                        'rotation': -2859509404311605133,
                                        'virtual_nw_x_pixel': 638023515,
                                        'virtual_nw_y_pixel': 1121433241,
                                        'virtual_width': -1983619762,
                                        'virtual_height': -471252466,
                                    },
                            {
                                        'source_monitor': 904014,
                                        'source_nw_x_pixel': -8261736865379045636,
                                        'source_nw_y_pixel': -1904898408172351266,
                                        'source_pixel_width': -192733147873955331,
                                        'source_pixel_height': -1660065903534598649,
                                        'rotation': -6448746174309816652,
                                        'virtual_nw_x_pixel': 1494716675,
                                        'virtual_nw_y_pixel': -1673618695,
                                        'virtual_width': -1833205214,
                                        'virtual_height': 63804851,
                                    },
                            {
                                        'source_monitor': 45305,
                                        'source_nw_x_pixel': -7812251661466708033,
                                        'source_nw_y_pixel': -6973779616826561628,
                                        'source_pixel_width': -5994937306771473690,
                                        'source_pixel_height': -1097321755969018060,
                                        'rotation': -4108108727829727889,
                                        'virtual_nw_x_pixel': 843963940,
                                        'virtual_nw_y_pixel': -1627744824,
                                        'virtual_width': -1773832531,
                                        'virtual_height': -1437173029,
                                    },
                            {
                                        'source_monitor': -276282,
                                        'source_nw_x_pixel': -3676993383091178138,
                                        'source_nw_y_pixel': -6320625148969720910,
                                        'source_pixel_width': -2986051095615882436,
                                        'source_pixel_height': -6464284214110918374,
                                        'rotation': -2312008327033597888,
                                        'virtual_nw_x_pixel': 1212032754,
                                        'virtual_nw_y_pixel': -779651549,
                                        'virtual_width': 117398285,
                                        'virtual_height': 1931541186,
                                    },
                            {
                                        'source_monitor': 7528800,
                                        'source_nw_x_pixel': -2492673206810286353,
                                        'source_nw_y_pixel': -4542657262139868882,
                                        'source_pixel_width': -833309460762750394,
                                        'source_pixel_height': -4444685516353207807,
                                        'rotation': -5882262851627487340,
                                        'virtual_nw_x_pixel': 247462927,
                                        'virtual_nw_y_pixel': -1974175236,
                                        'virtual_width': 1229083153,
                                        'virtual_height': -1258870985,
                                    },
                            {
                                        'source_monitor': 7077602,
                                        'source_nw_x_pixel': -7914460854897544619,
                                        'source_nw_y_pixel': -7692253481045278156,
                                        'source_pixel_width': -9203741477244559518,
                                        'source_pixel_height': -4253523502835095634,
                                        'rotation': -2393458774322749849,
                                        'virtual_nw_x_pixel': 790736438,
                                        'virtual_nw_y_pixel': -1406722774,
                                        'virtual_width': 334271307,
                                        'virtual_height': -126399692,
                                    },
                            {
                                        'source_monitor': 6453380,
                                        'source_nw_x_pixel': -1908229636589088163,
                                        'source_nw_y_pixel': -5182214122718249158,
                                        'source_pixel_width': -7261092035111135431,
                                        'source_pixel_height': -7728067492636336905,
                                        'rotation': -8393300306538827291,
                                        'virtual_nw_x_pixel': 1678738360,
                                        'virtual_nw_y_pixel': -949549271,
                                        'virtual_width': -625276160,
                                        'virtual_height': -213562404,
                                    },
                        ],
                },
                {
                    'description': 'ӫŢ£ϮІȯɆŭǸʃ҃ɏԫʨ§ŨΫӗǅӊƴӱÔ˅ϥԘDѨφο',
                    'monitors': [
                            {
                                        'identifier': 5640056,
                                        'width': 7166181484392069054,
                                        'height': -3604370197307075247,
                                    },
                            {
                                        'identifier': 51708,
                                        'width': -3550529680770314773,
                                        'height': -4427477685217704732,
                                    },
                            {
                                        'identifier': 9529450,
                                        'width': 1070610704204091836,
                                        'height': -4764784159247745177,
                                    },
                            {
                                        'identifier': 541847,
                                        'width': -5654084013085693527,
                                        'height': -9048687283770236290,
                                    },
                            {
                                        'identifier': 993277,
                                        'width': 2799012387999846707,
                                        'height': 6799698741584857539,
                                    },
                            {
                                        'identifier': 6783191,
                                        'width': -4601954774606902823,
                                        'height': 7580494479116216780,
                                    },
                            {
                                        'identifier': 5000182,
                                        'width': 6679202917354512054,
                                        'height': -230572477004990873,
                                    },
                            {
                                        'identifier': 8753653,
                                        'width': 5901533415467601934,
                                        'height': -2817303002364789798,
                                    },
                            {
                                        'identifier': 512854,
                                        'width': -660960422317734681,
                                        'height': -4222261345815602466,
                                    },
                            {
                                        'identifier': 9662660,
                                        'width': 968535521646923188,
                                        'height': 8682331552065802920,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4049158,
                                        'source_nw_x_pixel': -7964943499438616759,
                                        'source_nw_y_pixel': -7609668161249402295,
                                        'source_pixel_width': -8367514126452232787,
                                        'source_pixel_height': -2230045541104191060,
                                        'rotation': -2960565777593935875,
                                        'virtual_nw_x_pixel': -1379933916,
                                        'virtual_nw_y_pixel': -391791974,
                                        'virtual_width': 1852283597,
                                        'virtual_height': -808497185,
                                    },
                            {
                                        'source_monitor': 8621602,
                                        'source_nw_x_pixel': -5869150549819154449,
                                        'source_nw_y_pixel': -2020903531627927428,
                                        'source_pixel_width': -6173185419545671414,
                                        'source_pixel_height': -5659923774111664932,
                                        'rotation': -536454801505390067,
                                        'virtual_nw_x_pixel': -1253051318,
                                        'virtual_nw_y_pixel': -1948370756,
                                        'virtual_width': 1913687563,
                                        'virtual_height': -874345119,
                                    },
                            {
                                        'source_monitor': 823152,
                                        'source_nw_x_pixel': -4960905088951328476,
                                        'source_nw_y_pixel': -2591437345795822421,
                                        'source_pixel_width': -6662459637722618921,
                                        'source_pixel_height': -6045753512121348299,
                                        'rotation': -4859166406591005459,
                                        'virtual_nw_x_pixel': 818017307,
                                        'virtual_nw_y_pixel': 1164326488,
                                        'virtual_width': -1251834021,
                                        'virtual_height': 1154049215,
                                    },
                            {
                                        'source_monitor': 4283512,
                                        'source_nw_x_pixel': -3823904784929113454,
                                        'source_nw_y_pixel': -387308940267200211,
                                        'source_pixel_width': -3532340278274510390,
                                        'source_pixel_height': -7094428819365690494,
                                        'rotation': -3464936447846747733,
                                        'virtual_nw_x_pixel': 888765578,
                                        'virtual_nw_y_pixel': -1479972568,
                                        'virtual_width': 894582231,
                                        'virtual_height': 157504616,
                                    },
                            {
                                        'source_monitor': 1162541,
                                        'source_nw_x_pixel': -7122653106897653001,
                                        'source_nw_y_pixel': -3832066569584952804,
                                        'source_pixel_width': -1738077673800610425,
                                        'source_pixel_height': -5811123732623929277,
                                        'rotation': -8105979004176731158,
                                        'virtual_nw_x_pixel': 1865026826,
                                        'virtual_nw_y_pixel': 983124740,
                                        'virtual_width': 181372269,
                                        'virtual_height': 173955869,
                                    },
                            {
                                        'source_monitor': 3027780,
                                        'source_nw_x_pixel': -329267268739665566,
                                        'source_nw_y_pixel': -1765863857511543709,
                                        'source_pixel_width': -8084751755221646096,
                                        'source_pixel_height': -1927239284629038503,
                                        'rotation': -5612471575146937384,
                                        'virtual_nw_x_pixel': -452976771,
                                        'virtual_nw_y_pixel': -751304987,
                                        'virtual_width': 394936785,
                                        'virtual_height': -1710747746,
                                    },
                            {
                                        'source_monitor': 9819369,
                                        'source_nw_x_pixel': -8976732538176688635,
                                        'source_nw_y_pixel': -4538754098588672876,
                                        'source_pixel_width': -3293943793235170723,
                                        'source_pixel_height': -1995783415606307866,
                                        'rotation': -7099794884266401388,
                                        'virtual_nw_x_pixel': -634668748,
                                        'virtual_nw_y_pixel': -196120777,
                                        'virtual_width': 10342943,
                                        'virtual_height': -979724418,
                                    },
                            {
                                        'source_monitor': 8765010,
                                        'source_nw_x_pixel': -929624835676082298,
                                        'source_nw_y_pixel': -1503199830363200512,
                                        'source_pixel_width': -2712874935172714539,
                                        'source_pixel_height': -1068971622688181869,
                                        'rotation': -8244475211422477497,
                                        'virtual_nw_x_pixel': 827311463,
                                        'virtual_nw_y_pixel': 54503632,
                                        'virtual_width': -1972440320,
                                        'virtual_height': -1812325316,
                                    },
                            {
                                        'source_monitor': 7454318,
                                        'source_nw_x_pixel': -4711374344017834553,
                                        'source_nw_y_pixel': -7396898981533866183,
                                        'source_pixel_width': -8385031211080305763,
                                        'source_pixel_height': -8959491807228230874,
                                        'rotation': -6810955018780208825,
                                        'virtual_nw_x_pixel': -1423830625,
                                        'virtual_nw_y_pixel': -258919162,
                                        'virtual_width': -1306129339,
                                        'virtual_height': -312100222,
                                    },
                            {
                                        'source_monitor': -847950,
                                        'source_nw_x_pixel': -3555597051569505779,
                                        'source_nw_y_pixel': -4973229968205162756,
                                        'source_pixel_width': -7857214561547111418,
                                        'source_pixel_height': -8231649266226934531,
                                        'rotation': -5620114169787107667,
                                        'virtual_nw_x_pixel': -135472977,
                                        'virtual_nw_y_pixel': -158333613,
                                        'virtual_width': -837749084,
                                        'virtual_height': 110214316,
                                    },
                        ],
                },
                {
                    'description': 'ƘʇӪ×ɞҐӳ҇˗҃ÎƾƑϒɒэĠǤʨѡɜяɆıȩơǈϞƁț',
                    'monitors': [
                            {
                                        'identifier': 224892,
                                        'width': 7311393309942532165,
                                        'height': -5318587737588032961,
                                    },
                            {
                                        'identifier': 4778570,
                                        'width': 2713820245917037389,
                                        'height': 2605068890920638319,
                                    },
                            {
                                        'identifier': 8020575,
                                        'width': -115846773971424114,
                                        'height': -1318106923444568608,
                                    },
                            {
                                        'identifier': 7246210,
                                        'width': 6237803224704519310,
                                        'height': 3212010120673691519,
                                    },
                            {
                                        'identifier': 2814533,
                                        'width': -3038847983373166045,
                                        'height': 4420774368552088017,
                                    },
                            {
                                        'identifier': 2674077,
                                        'width': 6323471087396242801,
                                        'height': -1737114297918143514,
                                    },
                            {
                                        'identifier': 7482034,
                                        'width': -3665776343317116270,
                                        'height': -8966526413567595364,
                                    },
                            {
                                        'identifier': 1182296,
                                        'width': -9193216789429222279,
                                        'height': -4325414152363985402,
                                    },
                            {
                                        'identifier': 7563039,
                                        'width': 9059144375032054172,
                                        'height': -516431967616799436,
                                    },
                            {
                                        'identifier': 3698635,
                                        'width': 5897811594498711445,
                                        'height': -3818081711333821716,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8713499,
                                        'source_nw_x_pixel': -1783539509340694181,
                                        'source_nw_y_pixel': -4288787684845081002,
                                        'source_pixel_width': -1257350865904580057,
                                        'source_pixel_height': -1493166942339684447,
                                        'rotation': -2981666304117845970,
                                        'virtual_nw_x_pixel': -345311536,
                                        'virtual_nw_y_pixel': 1775694537,
                                        'virtual_width': 1905930672,
                                        'virtual_height': 465144270,
                                    },
                            {
                                        'source_monitor': 2217246,
                                        'source_nw_x_pixel': -7026484714093177367,
                                        'source_nw_y_pixel': -5838155458607720751,
                                        'source_pixel_width': -4641050426465608593,
                                        'source_pixel_height': -1836046875509159138,
                                        'rotation': -9042221959252300293,
                                        'virtual_nw_x_pixel': 830491658,
                                        'virtual_nw_y_pixel': -705972240,
                                        'virtual_width': 1605778631,
                                        'virtual_height': 1193642163,
                                    },
                            {
                                        'source_monitor': 1472563,
                                        'source_nw_x_pixel': -5052986711701452336,
                                        'source_nw_y_pixel': -3544989300464191469,
                                        'source_pixel_width': -8999113871200844043,
                                        'source_pixel_height': -2915715866024706324,
                                        'rotation': -5991052156009455127,
                                        'virtual_nw_x_pixel': 1494696634,
                                        'virtual_nw_y_pixel': 1164424929,
                                        'virtual_width': 276254801,
                                        'virtual_height': -1071687782,
                                    },
                            {
                                        'source_monitor': -450462,
                                        'source_nw_x_pixel': -1543115536047971744,
                                        'source_nw_y_pixel': -1189352041098647727,
                                        'source_pixel_width': -8322899910782320572,
                                        'source_pixel_height': -7918661551055150449,
                                        'rotation': -2074175464453269071,
                                        'virtual_nw_x_pixel': 1040025480,
                                        'virtual_nw_y_pixel': 932780339,
                                        'virtual_width': -1764321910,
                                        'virtual_height': 709644453,
                                    },
                            {
                                        'source_monitor': 9933262,
                                        'source_nw_x_pixel': -3933326415236415749,
                                        'source_nw_y_pixel': -6289152671029843658,
                                        'source_pixel_width': -6538279849024242870,
                                        'source_pixel_height': -1783340742925660793,
                                        'rotation': -7332597959651774382,
                                        'virtual_nw_x_pixel': 827207708,
                                        'virtual_nw_y_pixel': 1649341570,
                                        'virtual_width': 1536667804,
                                        'virtual_height': -116169806,
                                    },
                            {
                                        'source_monitor': 6085789,
                                        'source_nw_x_pixel': -6458949138478899652,
                                        'source_nw_y_pixel': -3252934062278845327,
                                        'source_pixel_width': -1614414644842538255,
                                        'source_pixel_height': -1487591052772526684,
                                        'rotation': -2018678169015586204,
                                        'virtual_nw_x_pixel': 310553559,
                                        'virtual_nw_y_pixel': 1318838459,
                                        'virtual_width': 1606651159,
                                        'virtual_height': 1896647524,
                                    },
                            {
                                        'source_monitor': 7930715,
                                        'source_nw_x_pixel': -628996068989339602,
                                        'source_nw_y_pixel': -1596750717046068665,
                                        'source_pixel_width': -4921599326449974350,
                                        'source_pixel_height': -7562566690638636768,
                                        'rotation': -5057937714150316063,
                                        'virtual_nw_x_pixel': 1597158405,
                                        'virtual_nw_y_pixel': -854103413,
                                        'virtual_width': -1057326340,
                                        'virtual_height': 986945120,
                                    },
                            {
                                        'source_monitor': 7103209,
                                        'source_nw_x_pixel': -4025774846857251049,
                                        'source_nw_y_pixel': -33059369261557725,
                                        'source_pixel_width': -5851820964490594318,
                                        'source_pixel_height': -8390600784482638115,
                                        'rotation': -4839536277269258625,
                                        'virtual_nw_x_pixel': 1411541095,
                                        'virtual_nw_y_pixel': -449821025,
                                        'virtual_width': -674384462,
                                        'virtual_height': -362104104,
                                    },
                            {
                                        'source_monitor': 5553919,
                                        'source_nw_x_pixel': -7101305329374477655,
                                        'source_nw_y_pixel': -9185749193124823034,
                                        'source_pixel_width': -4846964388811851512,
                                        'source_pixel_height': -8495582920894359762,
                                        'rotation': -2016418373455907310,
                                        'virtual_nw_x_pixel': 398243123,
                                        'virtual_nw_y_pixel': -1462524996,
                                        'virtual_width': 263673287,
                                        'virtual_height': -1320746459,
                                    },
                            {
                                        'source_monitor': 6679850,
                                        'source_nw_x_pixel': -1666104251074538109,
                                        'source_nw_y_pixel': -3982798154633556928,
                                        'source_pixel_width': -6215084807121435411,
                                        'source_pixel_height': -6661751280441400044,
                                        'rotation': -4658401767326749189,
                                        'virtual_nw_x_pixel': 562901941,
                                        'virtual_nw_y_pixel': 884811669,
                                        'virtual_width': -605185845,
                                        'virtual_height': 1318491034,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 237186,

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
            'request_id': -746925,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 6789313,

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
            '$': 'ƞěӏêHƠʮҦȹɎЊΏȮŝΖƨüͼϡªүõˊϼkʪŹΒϤ\x92',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': 329613831397410795,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 128666.7763846961,
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
            '$': '20220530:170407.027037:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ïԟ{ôǿӋϻxзñ×ĻÊVŬäÄɭ\x9d©ĮƾƿĢЕҡŚѵϔҿ',
                'Ҩɾԁѱ˴ʅƑĩԛȤʃȡɼ"ԗԖá\u03a2ќưȟ˷vǴ˹ΜÞƾ*ą',
                'ȘЎ\x81xҵˌԠͱƥ\u0378ѾϋİʒƵ\x8aǝԓ˹ͼҕǄќ˹ņιпÖЂЦ',
                'ɓοŀʽ\x98Þ\u0379¾§âs\x95ƾќȗ\x8dƞ:ˎǢƪˍɜАɾЮ\x81ʌԒˣ',
                'ȈʸλԌɓʦɥαѢ4ΖтǬӬЮЖGϟ˧\u03a2ĤӟǩˉǒɤǡƐȤʻ',
                'aЊɐӞϸКЫԍѡ϶˚ĭӠҍĴAÊ¬ȷʓǱԆŏĴǌɇӢĴ˔ϩ',
                'ʃ¹ѣ1ԦΣºþǱϷͲŗ˲όϷΪ/Ȓȫǌ\u0378ǩԉƝTо£°Ŝȯ',
                'λƒǄɹЙўΎ˟Ȍ&ʷíВǄƨ˰҈\x89\x9bÇĢӪǑŃӊɺȏ6Ҧ´',
                'ɜИ\u03a2εϖǕυťƎaӴ¨Λ¸ӎgғҊόїı҅ќTҀˇϖƌƾŁ',
                '˵Îǯ)ŷΐԭ\x8aŵІºχŬśAȓłк¦\x96ӷˢƄƉΤȩ±DұͲ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -5904630294068311418,
                3514713939464730851,
                -4441436183691870691,
                2427958280694460622,
                687068376976407215,
                7319724014315208763,
                8913368374843363040,
                -4702187271827623864,
                -7182642637370202005,
                2108381136193339195,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                54063.48890410125,
                106546.10787538538,
                166127.2418563359,
                710262.0049960562,
                934380.3915043866,
                305891.0950138794,
                568770.1468822988,
                404566.5367915109,
                323605.8918929388,
                88042.32869020762,
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
                False,
                True,
                True,
                False,
                False,
                False,
                False,
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20220530:170407.032180:+0000',
                '20220530:170407.032272:+0000',
                '20220530:170407.032361:+0000',
                '20220530:170407.032450:+0000',
                '20220530:170407.032538:+0000',
                '20220530:170407.032626:+0000',
                '20220530:170407.032714:+0000',
                '20220530:170407.032802:+0000',
                '20220530:170407.032890:+0000',
                '20220530:170407.032978:+0000',
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
            'name': 'ѱĻӊ¿οЩ°ɧY=¨dð˅˰ˤƑѫӒʳОţ#XŘз',
            'value': {
                '^': 'datetime',
                '$': '20220530:170407.025624:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ș',

            'value': {
                '^': 'float_list',
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
            'catalog': 'ǢёœЋ˽ĖǲѵːѦυ\x95ЗŶҋȖǎ\x87Җ0',
            'message': 'ɖńȴƉȋ҄Џɞ\x92ӅҧæɻӁηѳҽ\x86ô΄kΥǯΈÓԓԎŉ,ɯ',
            'arguments': [
                {
                    'name': '«үƝǎZ@',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'ě΄δԈŨӵWʟǤЊҏ¨Ű',
                    'value': {
                            '^': 'int',
                            '$': -6059696616810765058,
                        },
                },
                {
                    'name': 'ИаxϤɅҤʝȏȹƨα',
                    'value': {
                            '^': 'datetime',
                            '$': '20220530:170407.019939:+0000',
                        },
                },
                {
                    'name': 'Ôѡƞ_ǌʢ\x96BнǰуːɓĆіƂΊȶ˥/Ͼԥ¡ǛώҙΠ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        220907.71664715052,
                                        610353.3530237568,
                                        297498.62160174764,
                                        -70782.11314016723,
                                        557266.6371209318,
                                        234904.8714273972,
                                        234620.2941131711,
                                        436508.81833789055,
                                        -30094.254151846762,
                                        651925.3024084142,
                                    ],
                        },
                },
                {
                    'name': 'ԥOƜξѩ˾ʘ%у\u0383ʀеΧϴƛĝ˃ȓ˅ʢ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'Ԋ@ʛÈчӝȓʍśƒ˨ʬǞ\x9fʓʶөȻҠέŔ',
                    'value': {
                            '^': 'string',
                            '$': 'ǊđѽĊYȷɜϨ£ƳÉυԪȫğβΊϑӪǙuˆӗЧˢưöçϸȽ',
                        },
                },
                {
                    'name': 'ŮɱԮ˦ɶβĔǺ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': 'љâыÈƛɷ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220530:170407.022862:+0000',
                        },
                },
                {
                    'name': 'ЭΎȍ@.ſMɒˣ,',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'œǻɶĪƹŰ\x85ɮұǂЌŋҵ\x91ōͷ1JĴ>ÂèìΏʎ1$҂ɦӞ',
                                        'ˉʱҬԣԥѱăȃʱʋԀ\u0379ӤпģӻÄϸŐÅϦѓБŸȠĶє=ҥ˛',
                                        'ˆō˄ʠGĂϺδȖ¤VƎԈ\x9aӒ,ύǇ°ƧɘsӣâџƣӬʺʕă',
                                        'ѸѳΡȜьıКÝĄäǁÉ¤ɬó6ЈѝsǛҾҎѪúеҬȆǙTӲ',
                                        'ЅȖǻҦʍиM\x92Ͱ˪ȼȁřȠ҈˴ʏƾǙԓXВʪȽήϢnWӑĄ',
                                        'ʻŖųȡģľÒҁõӬŷԜЫɷʿͺrǡҟĦӳ˄Ūѵ\x7fДēμЀӊ',
                                        'ǮƅӖŀľφԡʝϢýˇȲϺƴӹǐȅŌưȜɰϘĲ"ΠÕƉœΆˉ',
                                        'рfϴԏϞħ˥ʮӢƁ˒ůȶʹ:˩ӻĹÉΈɦŜѼ2Τò\x92ßΔĖ',
                                        'ͻϠŁȃсʝČʁҶȕŪсЦҡԤˉ\u0378ԉ\u038d˞Ɩ˞ĮʖaӞύΚϗƏ',
                                        'Ûӊʮâ;ΕЃšƷŸΉƬԬȎ#þƥӚәȪԤҞ˩/ĳȄʿċɜО',
                                    ],
                        },
                },
                {
                    'name': 'ȿȜǌŴNә˃OìŞѣэĴ}Ͷ\u0383ǣ¾£ЭξƬ\x8fˤȤÖ7ѺѳƢ',
                    'value': {
                            '^': 'datetime',
                            '$': '20220530:170407.024706:+0000',
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ǯt',

            'message': 'Ġ',

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
            'identifier': 'ҋΝѦӷϾ҄Õ˦ЕĊɂƻĽӛĘоɎ½İ\x9dV\u0383ʷı¥EϽΔÓ҈',
            'categories': [
                'network',
                'access-restriction',
                'invalid-user-action',
                'file',
                'configuration',
                'invalid-user-action',
                'invalid-user-action',
                'internal',
                'network',
                'os',
            ],
            'source': 'ǞΟӍԝȬѽрȩԚӯƩKŔHŅӜʚ',
            'messages': [
                {
                    'catalog': 'CƛȿѱɕЪӫ=ÁӒ{ӝɟȗԩ|\u03a2ǘòʑǰłӜȼΪ Ɉÿƃ\u0378',
                    'message': 'tôρģêӐԔΧʈÃ˷ŒƯβѿ˸źˑȺjҐЁ/ƴϦ\xa0ʡIƚѠ',
                    'arguments': [
                            {
                                        'name': 'ԅʵӻȉīĦȨˆǴаӉƙɋȏєʭ¶ʸˠZȲƣӎΠ|Ҩ҃(φԭ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.930315:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĎȟѨѥӓљ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4233881030605968012,
                                                    },
                                    },
                            {
                                        'name': 'ûõưȣӂǧԪЌɐɻJІͲɹѶÊϸʫdĎˑĺ҄ʧǚʷɤʭęҙ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ĵ~\x91ȨϘðȳƊͻʚѽȭȘКɍϴãȐѨ˽ʴ!ԌȗӴϢѺʜ˦Ϊ',
                                                                            'ήӃŤŃƃɃѺ±ΩȤʸӐѪԂʓɔтɊȯõұǕȤʅϢԊӴӜЫǮ',
                                                                            'ɎɇĥġƻģɵҭЇ@ͱ©³Žȹ¦ǪԘ)«Řǁбơ¿Τ˯Ԋˏķ',
                                                                            'ϩʈȋ˲Ҝƻā;Ѫµ¾ԬӝǿʖˏϣѕǝӲҔǴЉЖɷįɝȜdà',
                                                                            'ӲԫĶɧЃԜūƶǍɨĉӭǑӳёӤfŤԔƤѼҝÓҊȑ\u0382ΆϤ²{',
                                                                            'ǊØáϙϢѶӭШĚϙpĎѰç¢ľҎŴÑұȋԉǁƧӤpԨ˼ӊ\\',
                                                                            'ԉˈʿ˸ԏɤâκ\x9cʜƚɁГƋςЇӎwǑӍ+ѐ϶ͿПҢȔǭƀˌ',
                                                                            'Ⱥ˱ȉˋƖӼϧėlǧɊŀƺɉí¯\x9eѯɝĴγι3ΏñѡĵɯөҞ',
                                                                            'ҮҜȌԭ҂ǄҪѵ=ҟϥ\x84˫ȣIżɄΨѯʅC\u0382ђĴɔŭŜÈϷ˟',
                                                                            'ɇώƍOşèŠԜѱʴĖƪǨԮ¥Ӿ\x8bDν}ҀóǗιƓȿȀ˕ԤΕ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӿŖһЬҍƘť\xa0ҠѲȃ·ˌĐϰ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            620158.7263926656,
                                                                            925081.7970527946,
                                                                            665379.7122422117,
                                                                            478272.42414063134,
                                                                            356796.30603808217,
                                                                            382496.63586742687,
                                                                            231835.0300502855,
                                                                            573408.2090356358,
                                                                            734442.6153469188,
                                                                            454087.8303735772,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɷӱƒŌοˑ˚ɛ¿҆ӭɄƢϛəĒӉĆмрɐέ\x99H(ΐτȝЛϊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.933758:+0000',
                                                    },
                                    },
                            {
                                        'name': '>µŔɧʱǲϭǶǥʼҦͽɻƬѐŻŝӚɱҷцΕζшːpҘ\x8aǭ϶',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8590393186894354409,
                                                    },
                                    },
                            {
                                        'name': 'ΫāȔ\x89ѮɖʳřӣѨιѬΠεé',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 654078.8710285339,
                                                    },
                                    },
                            {
                                        'name': '¦ёƑɇK҇Ό¤ńǣӪώϜɘĢ˒ȹƜɨ?Ұҙ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -68214.30625786849,
                                                                            154347.7532849282,
                                                                            502491.1901639927,
                                                                            370299.33626803086,
                                                                            381692.55249750125,
                                                                            249875.81543215388,
                                                                            814212.7819905994,
                                                                            699728.2717013338,
                                                                            468864.6874458585,
                                                                            255582.54142288573,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĻȄcϰhԑƞƝʽÿӆɹƥ!ьȨΕŲѢҶȾ£хϚǦӗИшҞҚ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            178787.2427888029,
                                                                            500221.4047674679,
                                                                            759047.3864145883,
                                                                            246937.54083330976,
                                                                            651879.8911867029,
                                                                            289661.49032582995,
                                                                            521925.3793836589,
                                                                            745730.02792989,
                                                                            879721.4795916282,
                                                                            505168.824264187,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʖIӋɸѐҭȨҹϿˑŽ\x9eϣʔō#˭ϢѢҞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220530:170406.937479:+0000',
                                                                            '20220530:170406.937564:+0000',
                                                                            '20220530:170406.937646:+0000',
                                                                            '20220530:170406.937727:+0000',
                                                                            '20220530:170406.937808:+0000',
                                                                            '20220530:170406.937888:+0000',
                                                                            '20220530:170406.937969:+0000',
                                                                            '20220530:170406.938049:+0000',
                                                                            '20220530:170406.938129:+0000',
                                                                            '20220530:170406.938209:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ЖUѤÀŴɚӳВORŝ϶ɡНàɮљЌÃϳʹΊХǝϣhÄ\u0380ΰƴ',
                    'message': '®ʩÉƭǭϡƬɥӈǀ¦ҳɏBєХ˶Ńȭ˕³Êɨ\x97,śѡѸ\x96Ɍ',
                    'arguments': [
                            {
                                        'name': 'èšǓʈ\xadӡҕȤȨȬѷŏȯԡʙVЄмӴɸPũи{Ēʯ£Ѩ\x8fѣ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2112398463611928594,
                                                                            -2107613078944648198,
                                                                            -7593093367410263514,
                                                                            540534492577023194,
                                                                            -8511315597875167278,
                                                                            6659172126339735230,
                                                                            7088645605946801919,
                                                                            8807544733457034110,
                                                                            3011938742415262060,
                                                                            -8423880394879268856,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԯ˙À҉ӛӋȹ\x93ѯȢ/ƟԝƉβÍĆ˖΅8\x92\x9d˱Ş',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            329955.89257981954,
                                                                            938773.5040167335,
                                                                            818389.879170365,
                                                                            319521.94954355725,
                                                                            238199.15155405807,
                                                                            234064.4954505642,
                                                                            -9753.716878178093,
                                                                            14902.888715635956,
                                                                            120916.49236583445,
                                                                            319310.5863082283,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӥ+л',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            409618.2079568803,
                                                                            116338.18531023903,
                                                                            253524.95370067045,
                                                                            215423.0116368701,
                                                                            287140.5606315668,
                                                                            132274.45400911605,
                                                                            214053.02917718905,
                                                                            131170.9552584836,
                                                                            763970.1210218512,
                                                                            811779.6110516953,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '`ҴхŭцʋÙ\u0381ʗȴǺɀӪȐҷӜȤ&ĂӤҽӱĖΌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
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
                                        'name': 'ĥѬкҮ˽ɀǚӻʎӝôϐҀǾ\x90ʓʁ$ԚŒѐʂˍ\u0383Άț',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.944238:+0000',
                                                    },
                                    },
                            {
                                        'name': 'рȭɌMӁȨԖѦ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɨ\x97φķ\x9eή˰ɸĿ\x9bЙ˴вͰγå¹ΛÛе±҅ƘѤΕʈ˺Τĩҵ',
                                                    },
                                    },
                            {
                                        'name': 'ѺGāK±ʈҧΈͱƖҌÖΩԞιӇm϶ŕ\x98\u0380ΜƻǮǔ¿ģS²Ӧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'āɜɡѻˑϲοŜDǐˆΦɛwàǌʬԄˎɾÃȫŲǠ<đԢѦϘϘ',
                                                    },
                                    },
                            {
                                        'name': 'гϏԤäԒƎğrȦ¹ǱɛҤQýĹƷоӄҦcҶΚӕѭǣӬӀ˫æ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            635017.2639458566,
                                                                            -42674.4027531592,
                                                                            737624.3028344314,
                                                                            351402.2996662331,
                                                                            761330.1341183654,
                                                                            799744.8787405076,
                                                                            695317.5605384806,
                                                                            -40957.04387244764,
                                                                            201405.06714480702,
                                                                            646017.3603774466,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'лąÌΕƳ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220530:170406.946710:+0000',
                                                                            '20220530:170406.946795:+0000',
                                                                            '20220530:170406.946877:+0000',
                                                                            '20220530:170406.946958:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҄ϽˉȠЫýѐvɝ(ƸӋнËſŶŹѸΛsǝɠϕ\x8bʔȰĆɺєʶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϫ˜ѳťȠƎЫKκɕȣα˸űoЋѨ˚ҟћĞɽ\x98Ȧі\xadɼП^Ƒ',
                    'message': 'ҧƼҹOͱԣʻŹΨ¸ʂñ*ϼǸҮȯΜØλ]ҕʍňhҁǉ£ϲ»',
                    'arguments': [
                            {
                                        'name': 'ԐȠƶлҸʆѥ0ơѬvȃÂͽƙ\u0380ȋÒǪԖϼƜƄʗ˵ӘΞѹԝα',
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
                                        'name': 'ǵϕґɡБǳɷв˭ќӍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            77761.13409672902,
                                                                            639504.5181399425,
                                                                            755590.9240440641,
                                                                            -70457.40848917217,
                                                                            973088.1432247655,
                                                                            22075.776475214792,
                                                                            742411.4201048693,
                                                                            807057.6254337636,
                                                                            522413.7642159476,
                                                                            450336.68843968655,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˌ҆ɌƀҤԚÜÓ˚',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 539354.759085317,
                                                    },
                                    },
                            {
                                        'name': 'ɭƀԗА\x96ɽÉўzǭѦɇéӔη\x9a',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.951294:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Эĵʻʣ!ЛŽЀČлϕô҃сϯώҬ½ǌ4Ĳ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӳǷȶǌýɑǻҗ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 731847.2493828441,
                                                    },
                                    },
                            {
                                        'name': 'ьƀэȔԡȗsƇӪ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            703607.0105328712,
                                                                            627170.3289367286,
                                                                            134208.02756577445,
                                                                            400967.29719246406,
                                                                            54661.29015440933,
                                                                            729124.4686562052,
                                                                            737177.306261964,
                                                                            806540.9807415926,
                                                                            176943.5827884153,
                                                                            484935.14985855494,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ơǧцүӷ\x96ĢӠɁπřɔĲғѽǌĆʵƋɓŤύƛƗ˾āԆҡИϏ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1655251669044731825,
                                                    },
                                    },
                            {
                                        'name': 'ɚҏ˅íƪɦͱ\x82ξϚv£ÏӑĒÙӗñVϗėřɇѯѧ\x8cĳ°½ŉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 834225.9369916318,
                                                    },
                                    },
                            {
                                        'name': 'ѶԃɹʛŐǇɉ*Řþɾғ΅ĂÞÃ0˳ʖdtȨφĄѮƂϚśӱǦ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220530:170406.955349:+0000',
                                                                            '20220530:170406.955435:+0000',
                                                                            '20220530:170406.955517:+0000',
                                                                            '20220530:170406.955598:+0000',
                                                                            '20220530:170406.955679:+0000',
                                                                            '20220530:170406.955760:+0000',
                                                                            '20220530:170406.955840:+0000',
                                                                            '20220530:170406.955920:+0000',
                                                                            '20220530:170406.956000:+0000',
                                                                            '20220530:170406.956080:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԁӒІɽʋtʒРԘYʌēΊ҆˷ӤʻȖθџӯƸ¿>ӃŨіњ8Μ',
                    'message': 'ŲĠͺńΈԋΘжѤΨЂǵţȣв\x90ŞǼӏŘċÝΔˁќδĊƚǵW',
                    'arguments': [
                            {
                                        'name': 'Ǩǲм"ѥÅWʊɢыȍф*Ή\x95ӣŸƪĽԐĦӶͲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            15030.122260840406,
                                                                            -69901.05848090375,
                                                                            911604.893833738,
                                                                            -96172.06410499904,
                                                                            328889.8547744177,
                                                                            920126.429928091,
                                                                            333362.9861763179,
                                                                            841661.1987826936,
                                                                            130474.10564869316,
                                                                            565919.1616853785,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӭι8Ȱμ˽ӏw¨ԇË.сĥЮŝǻԞʕRėȁѽƱσΛɤŋӐð',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': '҅βä҇qхɥǓԙǷʰ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7791144634596860625,
                                                                            5610274557680265922,
                                                                            473062272997281515,
                                                                            2230697078656186993,
                                                                            -4745960807541904142,
                                                                            -8556939244316873617,
                                                                            104303320680459145,
                                                                            5549671069196518534,
                                                                            -1884020262863128344,
                                                                            -5379772754944838961,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': ']ʅҵȜ҉Гæ˘ƫ¡ˤäӹҤȑľǰϝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.960847:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǀĂmӯɝĶ¡ɂϦˠΜϻӋώ˷\x89ұāȳɜ!*ÕŁƚԋIɋЇ=',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
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
                            {
                                        'name': 'ƥĊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȱǟǿʹȍǻǫҎѪԗL˗ǘкĵΟЀT\x9aήϤʥЯβήĖúKӀҙ',
                                                    },
                                    },
                            {
                                        'name': 'ɾzԄǟΕ³¼ЋлΠЊ˰áϽʈˋѮНƝ[ħχПãƷƷ¡І',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8106595831982785712,
                                                    },
                                    },
                            {
                                        'name': '¾ǀžӃ(»ǥσΎò',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2728523763307252311,
                                                    },
                                    },
                            {
                                        'name': '±ǭ˙ԥƐǴKɕ\x9dʌ˼iџӖӤΥǤÏѼҍVȅЩŀȅɓÐŰȭƏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': '&ʀlʽǛӏOɾģЇǽ»˽ϳʥάϯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 447200.10300634126,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'źȜЊԇϦӋˀǷĩІӂњ&϶g˅B˂ʳԪ˒ԛӊ҆˞YѵĤɾƯ',
                    'message': 'äΏϤɺϱȬɷθǏ(ˀӷƴʩҲʒȄ%ąϹМƬӑҸ·Ï\x81ϕ\x9bˊ',
                    'arguments': [
                            {
                                        'name': 'zз',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            6359.892198671718,
                                                                            304448.6484761832,
                                                                            210716.88372294098,
                                                                            895600.0932774614,
                                                                            796430.6658907057,
                                                                            527826.2355147385,
                                                                            970668.8841019238,
                                                                            949909.3756045147,
                                                                            543413.0259763859,
                                                                            268101.3226118704,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˬЄĒ\x88ºԪǐʾ\x86ʆÈҚˤ:Ȋќҏԛ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ʤɣ˹Ԗǔͳȭ͵ǗйǱ,ƢыЕƩͺʸіԂЀȕŉĽϕίěҚôΌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -390428829104013387,
                                                    },
                                    },
                            {
                                        'name': 'И˞ϋϳˎӣÞƖŰÌ³\x9aiĴʶмҠЍ¡ÔŶϗɲΗƞʝèʛ˚Ó',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            946015.7489630175,
                                                                            91516.99161127125,
                                                                            17347.68473271141,
                                                                            759310.503355301,
                                                                            214900.66102059418,
                                                                            936067.7364731494,
                                                                            763249.3548257047,
                                                                            841299.8197121617,
                                                                            935221.0306576928,
                                                                            669274.4843132234,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͽƵςǵεΐΉÍŒɌŰúĕŦǥŏ©ѫ¥ВɊŸϠǵÜ}ԟҖχˆ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -84097.74268980414,
                                                                            86193.21611319669,
                                                                            599470.8169750326,
                                                                            706484.2315577551,
                                                                            848923.1209147348,
                                                                            902049.3915896129,
                                                                            659709.7177236067,
                                                                            880437.0790719044,
                                                                            664031.7972209987,
                                                                            137615.40860745887,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѢˬʠʀԨTѾҹǾмĽԃȪƟƦˑϻӹĎԕˉӰЈźѴʚæјɋɅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 32682.55587504478,
                                                    },
                                    },
                            {
                                        'name': 'ЈӵåАχМˠƈ]ԏ˽Ӛª<4ˣ˖ƬôΒәή>ƒÙԏʓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'YɁə§{ɰ¸ȯY˴\u038dě˝ĭԥɇѬθKЪ¨|ѐ\u0381Ѹоĵ;ʃϗ',
                                                                            '҆ʖπ˛ɹЗԬĝԑќRÓg,ǪӘ˃đͱgȗʥʻқɴʉ\x86ŵԆű',
                                                                            'ͳǽŵǑϑȨſϑ#ӤйӢɽЖΰБЂ\x8bʝ˘ΙųƷjӓʀϕȉˎè',
                                                                            'ҍƝʘɇ\x84Ǆ=ǻАȀ϶·ǁđΫҮτ˚zϟĻĿҭƬɫȮфĄԉŗ',
                                                                            'ӻȆγԉǩӔ˜ӽĉϏϵȰˤɬӆїӠ7\x86ɎʎпЃʇĈ\x8eɆ\x94;Ԗ',
                                                                            'ʈї¦ҐķȆȡĞЧЎȒрӐѓϰ\x7fӂ\x88ŒяҁʩԝɀĘĉ˶κȺΫ',
                                                                            '\u0380\x98ѡfӯͱЖōǲʰϔȮƏΖŪ˓ͼΐɻʱΆ˯ǸǔʕϠƤɦ2Ҋ',
                                                                            'И=ǵ|<ȃ҄ҟЌĒÜŭǈƦ˜˩ўΞм˺ƪŃFģ½þȾƳНΧ',
                                                                            'g9ǲ˹ѸԪwӿɹǢàʟҀoϏÏҕĪωÅďįӀˤэʅȔĎΨӪ',
                                                                            '£¬ĥԣďг˟˶ԤÇёɿϞѹɜίвȋfΰUźÍ\x91˩ÔȮΊƿҺ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Вfaƾɪʴ˵',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ɲѡɰ6Ȗѿǔťʒ\x96ʔӏΖ͵ɓǞҊɲʙϵЄϑęfȄљć҂ƒΰ',
                                                                            'ζǕʅƴѥцӫǟĤѯϼĠÒĀλŭŁ·ŕȬӓȁΉȍʭѠуϽђι',
                                                                            'ҰɂΔȱЩɱϫŔÃÎʾÄƚуɏpƦ϶ʙӓƭĽĵ;ќơУѥwƋ',
                                                                            'ϕʍ˞юņņϊӕҮǳԮźÏģӁ\x9eǣΐҎů˅ɊƐь,ȎъӋ¡Ϗ',
                                                                            'Ŏȡԛ4ӷÖǮʫ˺˔рӴ˃ѲҨ\u0383ƀ\x86ĒԢѲʔŨЛˉƋîѼpѻ',
                                                                            'ŔÍϳȰ×ϼξԊԕʖјū`˦θɳʬҩŨӗƖʲлξѿѥпа˖Ϙ',
                                                                            'ȩŗкϏ¶ԛͻçɂ64nҠӶˎɾǱΕȿuĦқӸƢÒ¦ƶ\u0379Я[',
                                                                            'ʍʖŲǺɦЩɂҀÕ@ϥԄȉċЬҨΩÄ^ҫťɆtkș˳˦зƯц',
                                                                            'ЛĚȑԭΥ\\ЛʉҼèʎʟϴĦˍԬʹ7ʆȒbϣľĽǿɞ˧Ԣɛэ',
                                                                            'ƬҤФӡǨʵȾƶѧҮѽkŢΛςΗùЙĭͻ"žͿÿ\x9c\x81ѣ\x90ǩñ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƭƈѷүϭьМҎǱʢӈƍĀȆȗʿUĺ±µgʐ;Ӌɉ½ˍě',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǅaЫōɴǳɣǪŃ\u0379ʄπӉʼϯǽŨGʧŧ,˕ėīηӶ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˾ſư2ӲϿɼǺ\x8dʷÊˡ\x96ԜϜҀ¤ɨŘԑʈа\x88',
                    'message': 'ϸɀɳ˻jʴ|ɫ΅ʳşÖdwϐӘʣԅѹПԦЭЦѲ˖ƼҢl\x82ԩ',
                    'arguments': [
                            {
                                        'name': "ϻ˸Ԉà\u0380ɝŷɅϢĿ'öȘĤɝΐХŹΦӓǂyηĠĮ»ěЈËҹ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4864268661086975317,
                                                                            -681210789712939301,
                                                                            2674131929520329308,
                                                                            3351841177337812939,
                                                                            -8308387843324125814,
                                                                            1125583305003991094,
                                                                            94689233450186283,
                                                                            -7630268022342310576,
                                                                            -5634185944583676990,
                                                                            7986064328034214526,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'оβíӗӱʤƻϙőʤόΉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ϦҿȧÞԉ\x8dŷ˱šȎǍԃ§£щhǡʑˁǸ\\¸Ӄ¶ӝĄа-Śϻ',
                                                                            'ƍɨҠś.ƝҋˎƝʡЗːÛźƟyųž҃ґɟԛɏӓǾ϶ϤƋ|Ԡ',
                                                                            'ҳͷǟ\x97\u0380ιҌ˖ƚɐȪχŌрLʨȫˣ˷Ξіɣҥ?øЭϫǿӱѨ',
                                                                            'њΫƣɐѱјŐЂмˋÔȹȱ²ҞmӼŗΰȹШƍƁϤнǇВ\x8eŃЕ',
                                                                            'ŜǰˡЊҰЗԃȏΉФȠƳ˓ǬĈàҁħξЇɓÝӭƥԇȫҝƄҬӳ',
                                                                            'µǕă%ƓƓCҧŪǾˬˍăŢ\x8fƽ˞¼öƀġȺeԄӎEϳ.ƈӗ',
                                                                            'ǄcͶ˘ԔʨѶʓҞƯЫһ˖ҾԍʞȫăƧϛ\x86ƖƉ\x9eńŜ}ӀƬӘ',
                                                                            'ΔɟɳћƱxɳʬnĜӄɷУļӏ2ԊҪǊȒκӌʚԄĨӘƒťͺ\x85',
                                                                            'ƇÔǿԑˌmƣҳʋ\u0379ǎмĮȨɅmЪр\x7fǑĻ3õĞӇ®Ķ\u0378ԫÃ',
                                                                            'Ɖώϗʽ\u0378(ϔưϸ\x7fяɰϳĖЖϢУÁр/Ũ£ҰψƪȌϭԘŁʾ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ҲȶȧğҼͲѵ'ǌ»ЪƑ˒șʟϧǕĶĠпjŊƣƲ҂ȹГҍ\x98ƭ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8605142006145463740,
                                                                            6987295118304936299,
                                                                            -5208060750268642737,
                                                                            4771669947603739095,
                                                                            5058511053601930069,
                                                                            1143129896402058026,
                                                                            -8365573755446428746,
                                                                            -2787036764150843934,
                                                                            2263601256892085036,
                                                                            -4398831281217932709,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ŭȑ\u0379ɷ\u0380\x97(ЏȥΣŔψҡ\u038b˾ƴН+1ʲλEȇă+хɭ\x9eͽ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ͲӦÿΦˊEÞˠ\x92ò\x92řԨƌǨɳϋ°ȿĩôǮ˲ŻEҜӔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            9190.58483291151,
                                                                            969066.1176612417,
                                                                            -52658.99291363273,
                                                                            253894.2800796933,
                                                                            883105.9171266304,
                                                                            863594.0159166519,
                                                                            280910.5031247554,
                                                                            490312.8424056531,
                                                                            74863.62108959697,
                                                                            685911.5256753151,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0382íúϔǔʳ\x95ԓϜȳƇş9ąĲ˼ΥģѤáюҽʙϞΒһͽ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.979565:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ŮɉΉаƄʈ˦εɒΉͿԔɿă϶ə«ʰϐŒ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȉȦԤѢ<Τɩӓ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170406.981174:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ԇϺҙӇϠǫyǰ˕ҥɸmȎ˦ǑɷѪɚĔǄ9ү',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŁƾȔ\x93ɌxˀǬŰΡҙјϦ\x8aїˢĀƇϹƄƛęDвХӵ*9Ʋģ',
                                                                            '\x8díZʆ\u0383ІѿĹƵ\x9cҾƍɹħ¥ėŽďќϥǢþĖґӥɹѨƱǀƆ',
                                                                            'ЏΞғ҈Ÿ[˴ƒ˶}ʐťœ\x98ѺђϐБҜİ¯Ŀ¨ČǳƉǠΜʍЕ',
                                                                            'ҕЊӓЀΒƖǪҟѠ҆ǼφO3ʩ¼ȈŤ҅ʇαƲǹϙƍɊ=Ǻ5Ę',
                                                                            '\x8eěѩ˄ьļɻѶƆĽʟτ*ƐÕŽωĐΊӓϺEǿȿņ¢ţūԫŗ',
                                                                            'ѯУƠǮ´қʫҼʣîϗԫ\u0383Σ[ͱʽгӍBђʈɃŻƠeЄǿΧł',
                                                                            'ǛЊЯѹĜԦ\xadԃЈԟŢɮԠѬԐĘμӢӍMѫ˼7ӻпʴЪȦl˛',
                                                                            'łȰȢήұϩŞѴŅԭΑ¯ƦϳʿϯˋːǜӪʦȢΧƷʲƓФˡ¹Ǉ',
                                                                            '`ԓЕЈ\x8eŇљ˓ʞƟǾӫԪȘͻĚϱ\x9eƚЊśϽ~ΟˊȖ¯ɧʯȐ',
                                                                            'ǽM˖ГʐʧɛȌ˄?ȯƊcΒǾʤԙβ˲˞њĤÌÆҹiʒə\x8aį',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʻ͵ʒԪϔŻѺºѡͰНϋɰςZ˰ʖģƵ˝ɘѝΜ¢ԟN˵Ы',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҙѾчҴļʠÿĀҾ\x8d<ӖʒgӦѓƖɦГˁʜûʅ\x96ЉčʧёŴ΄',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'φԩΠӕόαɊ\x9aƓ\x84;·ѽȟˈ\x86ǨËɉÐ;Ɠ¿ӮǣӗȺǵѮƹ',
                    'message': 'ǰҀόĳɮȩǄЯӣȂ-Ϛs\\ɣŷɄɗȒQ:ʓƨʾ¢Ŀvѡʭʈ',
                    'arguments': [
                            {
                                        'name': '\x87\xadϟƛˉтІϘ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 550356.7801708921,
                                                    },
                                    },
                            {
                                        'name': 'ӺǿϷÂɗi˒ŞØɒѾD˔ğԠɚû.ȳîȽőӿ&\x8bÄɴÕӻ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƫˎªѪƄ\x89ӳ8',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 859969.8647085589,
                                                    },
                                    },
                            {
                                        'name': 'O¦żȞϤŰJǃɢǠóʳίͶūʳ\u0383ȯ˷ѱdҼ\x9aŊĞɧƬŐ\x8aʭ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 3333168232768573197,
                                                    },
                                    },
                            {
                                        'name': '%ɵO\u038dӂɿǬ\x84ӜÞȥжɈӏƆҝѡ²ʵϵҕí',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7849267164960033315,
                                                                            6732436746355401265,
                                                                            -2151363707108312250,
                                                                            -4640722629498880932,
                                                                            -2202132565099954045,
                                                                            -7554171612876116629,
                                                                            -5933547921554787982,
                                                                            -9006311097163422414,
                                                                            -4217698688421941632,
                                                                            4305064236645997610,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǉ!ҭҾ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'їтǠĞˢͳēLŲɿų˔ԓ×Ǵ\u038bё҆ͷ¨НR\x86ʎ»Ԗ˩ʿʴʖ',
                                                    },
                                    },
                            {
                                        'name': 'ĠĀĝȬZ¹\\ĥѸȾƏRάƔԧҞɶӃЈ˨ŮǙʆԡБԝӲͶ\x81ϙ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220530:170406.988012:+0000',
                                                                            '20220530:170406.988097:+0000',
                                                                            '20220530:170406.988179:+0000',
                                                                            '20220530:170406.988260:+0000',
                                                                            '20220530:170406.988341:+0000',
                                                                            '20220530:170406.988421:+0000',
                                                                            '20220530:170406.988502:+0000',
                                                                            '20220530:170406.988582:+0000',
                                                                            '20220530:170406.988669:+0000',
                                                                            '20220530:170406.988750:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӲʘƱ\x7f©ҽüңΦǇӉԒĴ;',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȥĒƗĘŻȮӫɖɚΩ˝ĕƵѿGБӥѣωǲnǀ\xadщŖӑƔΟӦ2',
                                                                            'ȄŶԪ˶ҭώşșƿҾϔƲ\u0381\\њӭîƔɸϺ|ƂυЀΫǤîԐӜÚ',
                                                                            '\x81ɾțˁѯȯɥʖɪOΉʹМĆØȊÆϢÈҗýOɋұȯγ\xadѱӒϺ',
                                                                            ')IŬ˸ԋϱԀȴc"˫ӾĠņӰ\x81ЦέƻɍͻïХ\u038dͺƻșȻ¡\u03a2',
                                                                            'ȲҚьčĩˤĄđͿʫȫɗïЏΚѷȆîӞfҟЇΥňΠύԗѣϹ˞',
                                                                            'ʫ\x9ețƵƒŃоʓȉÎǶÜƟνßƖżОͿӞʣʑĝʱgœϬӄϹТ',
                                                                            '´ȮχɀMԪӴĴˋŅ\u038dʥο˧ҭґʵ\x90¡ӧÌΗŽ˘ƚɰϒыð˜',
                                                                            'ԂW˼ˡƱԭÝϨ\x9cňҝΟ˂ƁӄȝӄėsŉˋҏɌƄԆмФȏƜQ',
                                                                            "\x8cƦðԮɟ\x80˵˶Ѣʦ'ӶȁŔӂԮU˖ǉɐԠƇ˨ҝҌē\u0383ţ\x8fԆ",
                                                                            'Ȧ§ǳƉΫԅϟиñœвƪºĵˬАӁƒƏɹӤƴțмμ¢ӿƽѴz',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЯЧʳΑ˚ŨѺԚɰӄɜϳǓǁŉƃԑ˞ĔȺӦřôë\x94ЃԕҘBӼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 53761.57237806215,
                                                    },
                                    },
                            {
                                        'name': 'ψƅ»ΰЪĶЪϐϰӵ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1314194209255064509,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'юǪǇ\x9eǚҚɍҠǳǢԟѴԡ#\x8bȧΪȏ΅ώɀČΦΦĊӹ˯U7Ȧ',
                    'message': 'ʔӱеԗRцǺŢЧѭſʸ\x8bŠƫ҃¸ȾψԊÀѧǨ\x91н˅ӹ΄ˆȕ',
                    'arguments': [
                            {
                                        'name': 'ƳċŏǸғҟĚ\xadО˃ʉ^ӵpӕQӅɮВйƺӽȬĬԬӈČԓĀҎ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8120901893773659489,
                                                    },
                                    },
                            {
                                        'name': '\u03a2ɀǠѺϝϼłũȥЮ\xa0șǲΕɎ˲(ʭŲà',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ɇǎґď£Ǣ°ĭfɘˢĄөɽОι\u0380ұχǧʞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5896326864436958131,
                                                                            -1981064956065699349,
                                                                            6174958042288178399,
                                                                            2008688856937053585,
                                                                            -1044577061079954767,
                                                                            4190575471237243121,
                                                                            8749974147690111418,
                                                                            -2038419644247690246,
                                                                            5809825436360122720,
                                                                            3057877347049941205,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'μȰԔǷұ΄ԖµǪȢ˞Ê\x7fƆŚӕ`Μū҃ҎЇϠǣͼƕʏԏǶЙ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -945692670888647108,
                                                                            -327481641838634065,
                                                                            -3591955209002229992,
                                                                            1804388869551175201,
                                                                            7518262707470647016,
                                                                            2169296627193172500,
                                                                            -8719055920809792143,
                                                                            -1740347493621202089,
                                                                            476624646796825499,
                                                                            -4652390503216545235,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҘӪǖćΚԢɭŲƐӢ§ʩȁδȫƻ\x9coƕÓ\x81ʛΩʭЇ\x93ԈӉґӢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 446896.83323723264,
                                                    },
                                    },
                            {
                                        'name': 'ЁѼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ѯҰľŭӎΣӕ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ώƱ',
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
                                                                            False,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ħʦ\\ҿȕǴ±ȿöӧҥԓǹŪϙɡ˶ľȕ\x86ЎϐʆқϰÎƦơӇǄ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            945343.676208288,
                                                                            -31807.57553593401,
                                                                            563523.4600454366,
                                                                            150379.30481083062,
                                                                            861936.8989283897,
                                                                            905978.9705516205,
                                                                            815308.7264393517,
                                                                            540830.0179449271,
                                                                            789411.5234875004,
                                                                            431512.82535221905,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƍ˒˲\x8eӮʴңѥҾɥƘˊЇрƛ>ɞ1ΔˤɵԉƟӻҐԃƓҩ˻Π',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 826079.6925561092,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'oȁϨѕˇѶϒӞ¯ǟсоыƘ+ŭÕ~līɰJĎζѵӌɢΜħK',
                    'message': 'ψȯÚȐɸǛϑïȞ64ѰȷǂĶɕϡВɦg˦ʇʧQϤźɑŷw§',
                    'arguments': [
                            {
                                        'name': 'ɎçТŎµȪяŒđǵû\x90˙ȱɩF.˸ȫϮȨΙƈ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '҆ԫɐȩǐļ\x82ˢžƦɿЋҨƪʳtƶ˰ă·ԎmΨ˞ϢŭkΖӞȬ',
                                                                            'ńШʝŞʹûȏҗΜѻ϶ҽǋZҠΪо˷ȻŔɡǠɰԘҮНŕĦъĸ',
                                                                            'ɁPȁӢрќҞQ\x81Šƪэԧ˙ɑДíȣúΔјɏɭΠϑ˧ĬΦЈ˃',
                                                                            '˄[ɻɈÝԔǪҗɒʌɌǒ҇ҐtʞӪĩʆϱӫ\x9bǲĢҭӑȊΈðӈ',
                                                                            'Ўȡ\u038dSÿǐɲVȦpϜügίɛģЙ\x8bǴş^ԘʣүҺ͵ʓԃɻǹ',
                                                                            'ʷ;«ŴѐˆӓϟԕwђɎɉqЭ˜ѥ҅ǍƝɴćбұ²ǮȈͼґƊ',
                                                                            'ˡԋȊШԜËΉӰԟθʣҌǁҹǀʈĐ˕đyȻĻʒÍˇϜ˷ŧ҆µ',
                                                                            'ʝäĝʳѿƘęώȬ»Ňƴķ\x9e®Аθǜ¦ïĖƱ\x82ȯƊΏɰ0Ģɰ',
                                                                            'ȁűǞЈдxű(ȚȷwȶɜcϯȑφȷҎÉʳӵ)СΖĳӠԌǩт',
                                                                            'ҕԀûđόɺϢЎСȆЍұǝȔ÷gqƔϪ½ӮҟɡǪñϿгҎÉԥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӧɁ½ºԛɽӞ͵Вʥӽɍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҐѬÔВѸҍOўȦǷȹǙ˷Ç;Ҟζ1ЙĵƞʘУ\u0380ǝ˭ǢΐΛԍ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ͼĐÅȗXʧǂȝǮϨƔСFŸμѡŹǌȹSəȰʂ˵˜ɂƕηˌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '\x96ŞΩӦԐȠҔӺǓҮͽѝʚ˧ͿkƆɐϪ¢ĀʇӾ¢ĞәˎӇĐа',
                                                                            'īҏ&ΰϏ͵Ɉ˼Ţ˃ԀӬʻ˥µГ˱łîɢbѤαЛІĚӦ\x97τҴ',
                                                                            'ɌЯӤ˅ʓǻ¿VŅлмȼȼ\x99ƝԢĤ:ŪʺcϳǁΆЉԤƐƢɄΌ',
                                                                            'ʽ;;ϔģϟƽęѶʭϯɑσvΝцȳ=ɡύӡǸʵj\x9eӞ/Ёπǰ',
                                                                            'ξԕɟнPʐ)ʀҁLй΅Ѫ·ɡɎŘȈԗфĻЉǧ¬ǕǩɄϧϡĸ',
                                                                            'ɭƋSЮŃĻ˕Əˮ;ԄҚйŚĊȜϬ\x9aʣƜʡǛїɤĜĊҔϊƸÚ',
                                                                            'ӢϗϠĨúǈʾ°ѐ˅εĄњʶtˋȅǺͿʽ˒˦vΦˍxÝəӗӁ',
                                                                            'ȪЂ(ƟмĹ^ɧǦǮͽȓǈŁ¾¤гqɢӵӱIĈ\u038dơƤÉцɖѠ',
                                                                            'Ͷ˩ǰƳ0ΒɝϭǽÒԜŷǦęãξ˝˅ȀNſŅѓ´ϻ{ӡʤǉθ',
                                                                            '\x83ŷͶƑԋѫѩΚÇ\x88ѱѷҮĥΦ˩ʚʝ\x9cͿȿɔĊʡ\x96ƉˡοԋӤ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ВƿϫѓĦ·RϥʻЇ˭ũ˻',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6800683679034701645,
                                                    },
                                    },
                            {
                                        'name': 'ҏˬъϴҵɒαɮʤҶ\x8dUωȲä$҉ѳʲƜк',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
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
                                        'name': 'ɦͿǴҬѼîҲàÿĶѠʯ5ʅ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 560706.1372067998,
                                                    },
                                    },
                            {
                                        'name': 'ʹͱÞƗиfƬĢˮӔ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            42906.76158911979,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'фƗŨ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1334195563545727812,
                                                    },
                                    },
                            {
                                        'name': 'WèЖ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            "Ǿ?çҿӕÏÛƃϺƲċҿѨˋ'ōͼҢ\x80ϗӬϾæʢǅϖӽɚÕő",
                                                                            '\xa0˹źµȖэ\x92͵˃ңȱSǲÓѐΰÃ]˲ΜʤΫԬzӷƖΙ˽тρ',
                                                                            'ȣЀ˃сйӕƪћőԦǖ²ϖOȸƏĊҖĳʫ0uϭǮ@¾ёӅňŬ',
                                                                            'ɀÂЃȢɛÎФƿКɹύȼϘХΝϥʘňêƞӷǦƠ ӋˁÝ˟\x90Ń',
                                                                            'БѱęůтĘϤѝ˜ШǦ´҂aҗŹǵʆӵȅū΅ĤѻÚԙ!ʪѽѺ',
                                                                            'ϗǐͻϛƿͺλӞƗԝƛΨĹ҆ɴÌƓšҚϸșȆ.ЕϾԑÅ¥ġT',
                                                                            'ǀϴғȻЧ!ȐӂԢʊʜЁˎҡѡȈʓȾԔðĉϻʩ6ʴˋԓȤʄƐ',
                                                                            'ϊӤѷʑ ɎîyҨҘğÒѥЕԉŀ¦ǖa¶ȭ\x9b¦ĽǐѕɤΪĻ˼',
                                                                            'ԃϢǴγˍΚǕïҢİѳўƿϋϡIµ+ϛɲфѮϔŰʚӔȫԒ!ʤ',
                                                                            'ԧɜvľªұѪѦsԪɃŇɖHԬʲ(ӈϒː+ˀYʤ~\u0379\x98ɋɽʈ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "ԠͽȟǋɋƐōǤΑŪȒ\u0382ԤɖМʗqԃǱΔÂ˟σ'\u0383Ӿ=ɝΨԥ",
                                        'value': {
                                                        '^': 'int',
                                                        '$': 8260003487023058403,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '7ѼӿʞȘāҊҽˀҼƒɡʓȘʿӫũɈƸҳɹÈˉȘÌ=öŕʊ\x90',
                    'message': 'ʃʙ\u038dɬČϳӣˋɳĖԂ\x93пʫѭƷȱǲʿўȔ\xa0ʨЂŬсјɅdԞ',
                    'arguments': [
                            {
                                        'name': 'Þ?ɄԑȯˈŒɢ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170407.008458:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ȇңȺҋʯhʯʤżɽʢRӿԦ¦Ǜȇjļ˗ѝρĠҾήƴʥǭύԉ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ЖÌɉԓˈϋȯJŲŻ˸ÇӰӯɄѾɃŮϻʆEʏɛσԘǚьʎӫ\u0382',
                                                                            '\x80ŋǞӟȖӪmҥ\x86ÜҎΕ¥ӂы˨˜ͼƢɷĂǷѣԏ\x93Ė¦ЦѤŰ',
                                                                            'Ŕ»Ɏʅ ƯƖ\x97Ο˭Ās\x96йҿзǝğ˷ӰǺKFĂͶğӿ\u0382Ȟȩ',
                                                                            'ąȚͶƛԣȠӪԜò҆ɑǞѿξϨҍɿǂӶϦӧFāӈ^\x90Ӳȸýӡ',
                                                                            '҉ηɄˇ¸ˤЂŁĚ¸ҭϼӒЮӧЭҿǶʥzʴõvȺíʂȜҷ˸ӑ',
                                                                            'ΡʻļβфȵԦíɬцԟ]Єș˷тΈʜƻɀʄ˻ѨǡʨʅˈϺHµ',
                                                                            'ƷөȻñҫ\x97ŸZzpâʞфѦƫ=ӃϦӽZһʶӼХǉ\u0380Ʃό±Ҝ',
                                                                            'ŹИʖɣΞʦѰʤķËų4ѤѰDþѩԕϠƊʠƜɽѮϊμĞ/˥ʐ',
                                                                            'ԎďțƎӄŅÒ˳\x9eώȎрұήą°˩άŞӍέԭϚHԥ$Г˂ľ¦',
                                                                            'ҨѥbΪƄϗʕќʅбϥВӨєԥɟϵ˨ȱÀķÑԗкȇŚŁØӴō',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¢ԠɘӈŢīʆƘźɍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'gјкЩȝςϡœ˅ņÞЖӝϷҖȬҌˈЃÓѷԨlNχА\x8b˼¢Ǐ',
                                                                            'ХЅˡԜΨόƥ˴ǺІϾˋdŬưȯ˳ȈɯǻǓԇѷïì·ϬĘԂǡ',
                                                                            'ɬΥ˓ҸԣAƫ˺òĢġЀѝŋҶfBӎčϝɨőnȸМŸȢӅФҦ',
                                                                            'ҶӽȔљʲɠԘ°ҫÛá_ѕ{ÊρΖǋǄʚҘŝҫϸŅΓʳюԦЊ',
                                                                            'х˘3·ӢԮʏϬɦ\x8eˈÿ\x8b ɯǔɵˋĚ˒ǜӪƕѬҁõӛˁ\x84Ӑ',
                                                                            'БĶӻcІԢ\x88ӥȫ\x92ҁʰȚřȷǝ>ƥ\x88)Ƶȃ˧БԧЖҨʒʬɁ',
                                                                            'ϸƗ¢ѥѯȖǢʜÌԪʑӜѕл˂ȼxζɒǡС®ԁǛʤϡč˖ɻ\x98',
                                                                            '¬ȷдʨΚҏԞƴˎ˹đϏƧŒʄȆɘНɭŀҹźżҝƻ/Ŗ҆ʪɞ',
                                                                            'íԃɿ˯ƌӟÀ҇ƣǧǺĸŇҮ͵ʙϡƖѧбƈcÖɝćɡȵψǰċ',
                                                                            'ɌωuΊǚͶş\u03a2Ⱦƪнԩȿʀȝɋϻ~ӆкΰѮˉҬ\x9bɈU˭·Ȭ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0382ƂƦʝʎѠ\xadƶҡӊ>ǛȁæŮщ˨ȜŜaūѬҽ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 929159.9926761866,
                                                    },
                                    },
                            {
                                        'name': 'Ӡ%:ѻǵǲɎɶˋµӁǏ{ΨΎŪĒåяɵğɵŸˌϬһɌ˲¦ѡ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǢȷӹɶĢљ˺ѐцǋΗӆƷtĖ(˷ª¸ɀʙǑåȀɘәΣƒԆą',
                                                                            'ЬаźАϷë˞ԇĞӆɡ˱ɬǚˣ¦Ƀ{˰ũ\u0381ĿƮŖŃɊΌǙԕl',
                                                                            'аă-§Ŧ҆ǋĒԇʏѺǿҝȷƜȞêgӧĹ\x97έŬϛȧǚǭқΫѺ',
                                                                            'ѝŅˤЈΟLđԩƟĥÿёİȽԄϳ¶ιʺË\x90љVǧΎjԠļĵç',
                                                                            'ЧΐȘǗǱөʹϊԑΛĕŒ«ҨɢrӟĿĿԉȢͶŷϐӟыûȲƶˈ',
                                                                            'ѴȢӖēϢ¤ɗƦ¦ǱѽӿQϮДƕșΤͺΎ\x96ϜɕЉŒΗÑΎǉψ',
                                                                            'ˏÞĜУƕʏӜѩȗӁ}˦ƫԧơÜĥĆѓǹӅўОϤВfӊ˰Ʃԡ',
                                                                            'ʅNӵԩé˛уѱD¢ҽҾѧŷħʰɄȃȸԭѫΡƙІʄӟąƖ*ӭ',
                                                                            'Α{Ͱԁ˴Ҽǭԛ͵˧ӭуѸϷY˽ɎҊʙФŽǁɷҕЬГђѤƩŐ',
                                                                            'ƍfЉĤâȅɎ+ҵ0ψǔƉǅӃҹɺө¾4φ\x8eԗôƩТïїǿΦ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ԣė[α\u038dǻφШԄǎ`мӣŜ˖Ǉҧў_ӘѪěǟÄӄĈϋе,ý',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20220530:170407.013486:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӨŲ\x97ɱOӑɫзΐʣĘъQģɿɨӪļ\x8bҬѓ҅ӘŶδТӰ\x7fȢҿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20220530:170407.013911:+0000',
                                                                            '20220530:170407.013995:+0000',
                                                                            '20220530:170407.014078:+0000',
                                                                            '20220530:170407.014159:+0000',
                                                                            '20220530:170407.014240:+0000',
                                                                            '20220530:170407.014321:+0000',
                                                                            '20220530:170407.014401:+0000',
                                                                            '20220530:170407.014481:+0000',
                                                                            '20220530:170407.014561:+0000',
                                                                            '20220530:170407.014641:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŶŮó[ҋӍʊƭюԟǹЏƯŦĭʡРÅŷҊҍ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ǘʈ*˛ųǰn¸ƫɛƜǈι¢ɊT\x84ǖѓȉӑѶ˔ŌȝǯԄ[ėТ',
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
                                                                            True,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƃÏģѻʐӫͶ˔ƴлȦТC\\ѷŊʓ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
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

            'identifier': 'ϭǪʃкѭ',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'åԌ',
                    'message': '҈',
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
            'request_id': -116039,
            'error': {
                'identifier': 'ȴ>p\x90bѲĶŠǕԘѨĶǷĬÿ˳˷ʧӅì×ȅǩ˜ԚԏƚĨúҥ',
                'categories': [
                    'network',
                    'access-restriction',
                    'os',
                    'invalid-user-action',
                    'configuration',
                    'network',
                    'invalid-user-action',
                    'invalid-user-action',
                    'os',
                    'network',
                ],
                'source': '\u0383\x8dΎԔʝϭʾԌиЙƉјɲ`˂ʾVөжԖǬпϻ˗ǜЗƀ0·Ӛ',
                'messages': [
                    {
                            'catalog': '\x82*AӾʷUϿŸшė{Ҡўрǰ\x99ņɫϿҽƶěǏȪҰƄ',
                            'message': 'ђ3ÛĻɣҜƳǓƣυԈǮĵƍǘУϗњάҿώÎѮԦǀ\x82ăǵÑ«',
                            'arguments': [
                                        {
                                                        'name': 'ίϜӗʭȾҐӵɇ˳ΩϤЙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 701407.5993050588,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΖÖʥɃpϐȔϹȵă\x93īҙ\x8akñąVԈҿΑδҼϜǣH',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7450859232981158415,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˏS˙ʰ˻ǌ˃ϮӤʧ&¾˘ɇ>ìeХұaԁЬťъƵ^Iňxˁ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 964211.5703996101,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ľƝò˧ĞćʂȁýԒ%GјǧԇЇӶ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.883372:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '>ƀГūϏǿɛҚ²ИȋрХŎõŹΔʹÉʣõӫÍȧѳΞ®Θϟо',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ķӻɵĘͺȲɲʳɸĹγEπҀӠƣǇЛԩ÷өбɆìôħȭÅˊƃ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǈĳËŜҢԪˮʖƣĄȂǢȎmУɼƎЋ˼ɘǅʳɒϐŖϔÔ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻÏŦǢ·źřYϮǏҷéѯ0ǻư\xadŐӽϪ\x82δ\x9bуtē˶ƈɐȪ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8452760929368323864,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÏɿɦϧřɿłʾөϜЋУӷĊƵӜҨӲƵϾƂēǰҥ˓р',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 160357.93146931622,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƹǣƣşϟɟŋӱιΟҩϷԙàDʥŲМ˪žĶѵшοŞˉưŜНǋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ô˖ÁÐә|ɵŧȁνѭčĝѳʟΗĎОÁΝȡƌȀЎ˂ɰ\x80¦cλ',
                            'message': '¥6ēƯ˞ӏðЉϮ\x96Ȼ\x97ҜĜȁГϦŦѰQÐŎŐʽńǏϊЃǍҭ',
                            'arguments': [
                                        {
                                                        'name': '˲ЋǇϩτǴ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7414549302623049209,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԦԜоȰύùϴVdѫЫ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǝϦȻ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'λɩ¸ʩųěǐ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɓɑҫԠѸNő+Ұɫ¸ȌҺ҅Ϥxl',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.888429:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȆπĎū',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍΏ͵ÑȋЁÚYԍɠЅǌKǘɘʘŇ[Юú˞ΕȷӃƄԪúĉiˎ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ßԁǏϚҝɜϠͻŮȯ˖\u0382һƳһ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 414203.7751109636,
                                                                        },
                                                    },
                                        {
                                                        'name': '˫û˃ĩҞyǜԇώdãȣΔѺˬĳӷΖҍɈΈÙŜʳ˸ŎΏйɱð',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ǿʰòľˤ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\xadȨÊӃČȧ\u038dѭӌŋ{ӱЭԤΎóǕȘӤӑўµʗΜˇͼͶӥWƚ',
                            'message': 'ԮǼƫҷʫĝŹ˧ǀØѕyԪԗ§\x81ЁѺϫΪԋŀȈҖŎƺǘϦİЁ',
                            'arguments': [
                                        {
                                                        'name': 'ԤΫʮȰȐ˭҈îïԑʒƸȲ˷Ҿ¯[ԎʭƓ϶ɫļүԒɦĭǐґϢ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'qʣWĄΓ©ʓѺXŢŽ\x9cʫʥШŗϕ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȣϹ˦ˊÊǭѶ϶Ѡȑ¡ƉӢεшƥΟ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.892185:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\u038bȑȇқә҉\x8eȐÉHиƜəyԬR',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҳ҆ɿӥ²Ǻ^řƦƗЧϣŅˬMхсć&ʖfHʥÀʌ˳Ɓʚ`Ԥ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĵōȍɩȳҴҚǷŕƋŁĴВүΏƣԠǺӏÇǞa΅a',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѸɵǽÅ\xa0Mйϓϭ˰ӗҪ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x87ћUǯl˞ϸõɮҊɻіÈÞ\x8fȑǰϻн\u038dϟҵ\x81ҨЫÝSÑбѓ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x93Ԃ˨ɱˊʥ}ӴƌͼѮЗMТåŪŖ\u0383®eżӳΔŃŐԩ҉εԒɴ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\xa0ɯΗǣƯё\x99ȩǙȔɔ҈ǫиғϟʛӡɼԝʜКĆϤǷӦq¦Ïo',
                            'message': 'ѫ~ж\u0378ϷѮӍЦϚĬƟӯˠkȁŵΟ\x83έ³ăԟƬӐ1\u0379Ҙ¶νё',
                            'arguments': [
                                        {
                                                        'name': 'ǈԣԐ˾ȝɺħҜĨzšȊŊňӽɦјЀƉ\x8eǙѰǸ҃Ҩ°ȜˇUÑ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Əͳ\x8fЯϝȗг¢ʅǞʥδϏeãƉɛȑʠҘĄFŴГɖɄMYƿǹ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 722364.4729922211,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĥȇǸ±ƗҭȵԦ\x86ɒɭÅĴɗoŎΌƑ˒ł÷ðԠϘɈԬÄ˚ǋǟ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϥҋϜнϼҰ҉ѤϰчǏѧϦҵЅϵǐКԫұȡϿЅǉ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'уǎԡҰѯȬ˲ɕԦ\u03814ҊЗɏȩƖʄаļƖƕǀ*Ӯ˃\u03a2ƕҗˉŝ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΤЖȅǾԇӔԊ¼ɫοғЮюМ¢ѢυȸǓ˹˲љŲԟĀĭӕŴƎ5',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЊҲİέΒƯ|ǚZƯ˓Ȕʿʠˠо\x8eˤʭҧúǕċЋӒӳʾŅñ¦',
                                                                        },
                                                    },
                                        {
                                                        'name': 'нŽ\u038dʗƣĭ˷ɜϜћȝëѵϑ}ΑǨĈ´ľНĲɍΘǓǸʣΌѶ0',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅЗ[',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ' ʡdǅґҿʞ®êҏО+ɼϒʞщæʓѺɄυġʉӖʉƬ҉ñŵӋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƶʤðϿ\u0382ǅӂ[ҢǍǬːѤӢƩЫ}ƛɃЖǭӎθмїɀȼŐЅğ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ўńˠԖ\x9bӝЗЪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.898912:+0000',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˕ƈҽѥ%ԦЀ·ɭгϷљҌʖӶӢЊjŒėΗŴˉЊхÜ˯ƤӽǼ',
                            'message': '˂T~ԇµɆԣɽЇɘҶĕɣiГųηƷӋŘϼőÿȌƁ\x89ԓнѿ˞',
                            'arguments': [
                                        {
                                                        'name': 'öЅЪӤφ˞ϯҚϷԡȾμɹʝьѣʪѰИҿɜҌ¥УƾӬѫΒӹū',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6801216618025972816,
                                                                        },
                                                    },
                                        {
                                                        'name': 'шǬƵõËŚͳӪ¢ļ˩Ηʊϭ\u0379c*5ūƣ9ȽuϸÁĠӬѺ϶ǋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӅӐśǭȄÎϓОδŠв',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u0383ǝĆŘοǣRβHƟόʪǳϿǔεζ\x9eȼτʃȠĖ҄ʰʐȒƙç˴',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.901016:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɛ"ƔÒʈϰϯɹŊƈǂҺϷʩҘïĊʀjɍżҾҬưМҁÓΊϩȪ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʇıεǎеȿƑͿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '˩ɱ6άʔıΊѿȇœϲϚͱƃ˙Ȯ>ūǎǵԒȸΒ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.902229:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'йɩёǓˤˁʵБɋʟȴ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΆӶɁҫ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 3080486500315273183,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '˗Ͷțëаɜˍʌ˩ϙɢϖvéKɸϙүØ˒ԃѦȩίȬǧӺ1Ԑы',
                            'message': 'ǂԍˀwҞԏϖʆһŶƅÈԛʓÈ\x7fũϗЂԊԔɭщϏɰϾƤŀ҇°',
                            'arguments': [
                                        {
                                                        'name': '×ŪçѷàяқVĞAͷуҸ˭҅ŢƏƜӎ.ʷéˁԟɌЧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.904332:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԩԧ_˦ԚԜԎԂоκķ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7883104053140135145,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЬBӥđîͿĿϓȊóԄӻɎӵ҂сĤЀƔмĶΜС˾ӱԬǂǂʟί',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 346418.4797007646,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Üe',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŖӚǦĨʀͶƾӚү',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʺã÷ʟӿÃĖǿΌϮӑңʚЛɱˏҝȹϑ×Ь{ƥѴZÏĹҬˈƚ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ęĭ˱áȿʩǶˠɼʳĦǇƗʩМξ\u0382κɛǟĹьӵ.ξͿϭƶѰ˷',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7817100862772913691,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŪȨˁʓ҃ιϳ£¹ТԪϳŃįϖԪ˺Ҵ ǶʟƭXƈȂʥ#ɞƽѓ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'őÌɟĵȂԆѾӕêŜǇԈи҈ΊԇϭΞΓˉǗѰЃѰԉǔЫҳΕÈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ſçΕˈӛѼʴӄл҂ҐͽŁϿËʇĿıϾ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'YǷӜǑl\x84ġяǮʄӦɜЈǋӖƧӻƾ\u0378MǛѦWkɍѫϠÄžϨ',
                            'message': 'ȵЬԢҹȊŅǼӞеόԬ²ѯәӣùőyѷŘǢ^\x96Ϙʛ˫Çҝˮr',
                            'arguments': [
                                        {
                                                        'name': 'ҜҸҷˈnΝ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 623304.4989921328,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҍO˥÷ξɛ\x98ô',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x9cцȘ˳ª˸ЖҽЪΰƌѧЂ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÒӜʾԁɟ|϶є9ĀΞ\x97GыΘĪҫĸãˇƝƳԫȭ8ġĿşʵM',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 424672.97010067257,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЋѰeԧņϏ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '{Ԧpʵ<ΪΟжćΖǮƍΌĊʦǀĶιŬΉÓȡBʇЂ҄Ɖæɡj',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ёҙɥȳΞǸӄϟJǍ\x8cҘӞѠĜɅдǊoɿĻυʋǩдƠŃ\x7f\u0380ʴ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʙʻ\x91˾ʅʆç¡',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -20173.52168432057,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȵ\x9dΔӵďá¿pǠ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 841228.0377795132,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԆɉΔѦĞΜʕȊŔŕȐϊǷŃШǀ˘вyʮ/ВҖǨʓɕƆǾa\u038b',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 502400.24447225826,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ȩž͵ˉĚ\x82ϫРĎƻôǾŋ²ɜƤτȚʨӴμ˫ԛϪΕ®ϒUȉк',
                            'message': 'ιɶȧũӔΩǰeƄ\x97Қ_ĀӝȝϙȅǶʏΣư˒[#\xa0ơƓѠóē',
                            'arguments': [
                                        {
                                                        'name': 'ѺԆÿќΖɪÔb҃˺ϼţȻˮ\x86ΟˋӺŕбſąɀǋТƙ·ȑǡ϶',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŗҽӖǡϙΪǸüŮ¢χУϧϸԮΓȣ+ϢŭςɌɜǽԔωB?үԋ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'bƿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -6675420936721880564,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʽˡĕdÕ˷BĨʞϘƠüÍǲˮώԮѧ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ηƘŷļԕϯѦ=\u03a2è˅Ԝ\x8bаӅԉĝɨ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 794090.0014889544,
                                                                        },
                                                    },
                                        {
                                                        'name': '%ˈ\\ʾÀʬϸʴ?',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϑÁЙʍȜ˓',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԢԨД\x88ԛʑɼʆ×ҪŃ\u0381ӡФ·ïɍ˓ϺɨҽԥҡҲò ԊɀĕӤ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 11198.30807145148,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǒǇÙɡϫп6ǒҒȨҕηŅ҈\x8eҷƊПžtҶĜхƜĔ¥\x88fтl',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳҗΣϬʲŔ$ԣʲʝʝȢ¸рμѢԌɆ҃δǜȝǼʉȮOɓȈ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '@ÏȨϧӁІϦѦʞǵ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'űʏЪ΄ҿԙ˺Ȓ˘λωȓĈe\x82ˢӏ˵)϶īɧùѤчȆҸЪŎÛ',
                            'message': 'ˊʻʢΪѴ(ǀbɃӈВƒGȫʩӆæō˷ǺўϤ3ԪЩĲÕӞФĎ',
                            'arguments': [
                                        {
                                                        'name': '0fͺЇ\x85Ɇ˳ȐȷƓɽх·#˕˶ʾӻҔǼɸůԍČȡԂ«ӭĪԉ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈêǼˇͼǢPњ´ԁҜĔ½ӾԜɩȒόǽУҗѲϫ\x95ϪlɥI҅ʐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 47800.97339437503,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĳҗ˧ȑŘӄùϾÙ×δ\xa0ȢϣįɁѼӍǯĎ*аӒɡǇƕːĞȆč',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɛӸҝЭ˚ƱԊ\x9eǺ\x99ȑļɻȡɥцXRӾΖ҈ŜЩȜ\x8dњԄÒћЍ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.919186:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˖ģ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƆǕċ\x85ȑöˤÿҬƞʐěƦ\x8cЍɛқИ҇҈ѓž',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɖKƕӅїсϹɻȮϑ\x90ôř˯\x91ăз-ʢŘŸrχгͷ8ӒϾŽđ',
                                                                        },
                                                    },
                                        {
                                                        'name': '˽ĔҋĈ:ĈйΫȟɢͳȃӭѰ.ųZŖȝǇŒƣρ\x88϶ϑӻɕӣƥ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϊĪӽԒéҎǹlΌƭϬǠμԓǯĎƊʡˁPUȲȿԮWò·ό',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ȋ8ΕɀĬδʬΚȠˉʃŨĳцňһϚƩ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 606185.9065413123,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Γˍж҇уΏҀǱŻ\x9bćΐǹʣļӈǴǌĽґѽƼǽǕӁæʯÃpү',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2216103976810082387,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ůѦ\x83ǟ˧ӋħÊ\x8eãǋ;Г"¹ɩÓŎΗ5ЮΧƒӼk_ɑā˶ˢ',
                            'message': '\u03a2ϲϗϜȭé"ɫҢєʔ´ѽ҄ȸȢÌ϶ԌұѰőԃƾβƑĥѴԝʄ',
                            'arguments': [
                                        {
                                                        'name': 'ϜӾ4ˢѸç',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϳƕӍӔͿĲВʡːƇ°ȬϿĝφǨΚćxӉX6\x99ÿĴǯɎǶλҪ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20220530:170406.922954:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԪӑǱı0ɛʟ҂εҖ˛ļ˛ώĕτ˧NɒƉѿʶĄqҝʰyc',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨċɜѪ®ҍҢϨìԮǆѾЩ˞ԨʽpO\x8cҪЦ˶¹qÄ*ƳŊғ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǊƁŀϫŵƆПεīԎPɐΐˊΪЂʉ˗ʗĨǫӣȸƔʼΏģѺ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕˡԊϿ±˅¾ҍİԭàеœʸϖAύş}ŔȣӁҿȀЖŞBĨŹԞ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 868502.400852951,
                                                                        },
                                                    },
                                        {
                                                        'name': '˼Ƚӊԍ®ÑϫȴrЋàƓԗΑʋ\x9bϪǑȎĸϚʇ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ġ\x97ġћӟӸЄɬ;ʝΕЌŤĂӦtƈҸѮȪƚфtİςɷЊʾϖл',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ԧă®ρŐϪǐӍŒ\x81ŎѲ<ѹĎɳԄ¾˘',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЋЩԀ˅˂Ӡ˻ϔǵ´˪\x95Ǒ¤ҖœмϫÛ_àӷңƕȠŰŖǡ',
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

            'request_id': -196014,

            'error': {
                'identifier': 'ˢүҵϸ#',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': 'ɯΓ',
                            'message': '½',
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
            'nw_x_pixel': -1462549973,
            'nw_y_pixel': 708958829,
            'width': -3659124552397879529,
            'height': -3278660187800969163,
            'ratio_x': -1868442343199715395,
            'ratio_y': -7605994717348994530,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 568097149,

            'nw_y_pixel': -373780638,

            'width': -8855696548944699525,

            'height': -8112086974406568662,

            'ratio_x': -4326086870399039721,

            'ratio_y': 8513827237202813151,

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
                    'nw_x_pixel': 1373463171,
                    'nw_y_pixel': 1935532536,
                    'width': -3845279542026316963,
                    'height': -8653879491985620158,
                    'ratio_x': -7151724300224017955,
                    'ratio_y': 3065602185868066362,
                },
                {
                    'nw_x_pixel': -919393347,
                    'nw_y_pixel': -544617457,
                    'width': -8317197989337210435,
                    'height': -1482867582454500217,
                    'ratio_x': 2582834679568115716,
                    'ratio_y': 3775343542014491296,
                },
                {
                    'nw_x_pixel': 1833370481,
                    'nw_y_pixel': -776275490,
                    'width': -3534719896527979101,
                    'height': -8238951966349606783,
                    'ratio_x': -5469182768711231848,
                    'ratio_y': -8756282226890459484,
                },
                {
                    'nw_x_pixel': 509161167,
                    'nw_y_pixel': -616269093,
                    'width': -9110954207393513654,
                    'height': -1969054554133978009,
                    'ratio_x': -2017965059096098225,
                    'ratio_y': 4064889050880467130,
                },
                {
                    'nw_x_pixel': -1002364188,
                    'nw_y_pixel': 883839532,
                    'width': -2686718279297697536,
                    'height': -8255699503662020213,
                    'ratio_x': -7166222485862660903,
                    'ratio_y': 1158895880717277943,
                },
                {
                    'nw_x_pixel': 1130879368,
                    'nw_y_pixel': 110387770,
                    'width': -9080357044165388454,
                    'height': -4271879473237897539,
                    'ratio_x': -4893084976131205550,
                    'ratio_y': -6363169908272653197,
                },
                {
                    'nw_x_pixel': 974138098,
                    'nw_y_pixel': 1077321659,
                    'width': -692445974026631942,
                    'height': -5855829667113932254,
                    'ratio_x': 4856052105898238536,
                    'ratio_y': -2522950976880144040,
                },
                {
                    'nw_x_pixel': -1799052202,
                    'nw_y_pixel': -1604209946,
                    'width': -6189651801745785610,
                    'height': -3003281037941910775,
                    'ratio_x': 4728648754602145429,
                    'ratio_y': -5486742258148994965,
                },
                {
                    'nw_x_pixel': -738497158,
                    'nw_y_pixel': -86863520,
                    'width': -6404227463901209156,
                    'height': -3665283558366211451,
                    'ratio_x': 6655756162396252673,
                    'ratio_y': 5729520506246637799,
                },
                {
                    'nw_x_pixel': -1439001744,
                    'nw_y_pixel': -431074757,
                    'width': -3921588133560569066,
                    'height': -8086474628117551976,
                    'ratio_x': 1919421083878454931,
                    'ratio_y': 1786755323763644568,
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
                    'description': 'ɹҒΝӯòĳɖɆҨ4ɛŕüğрŎʗСʅԆ½ǮėЬɦψҚϴMӌ',
                    'monitors': [
                            {
                                        'identifier': 8946072,
                                        'width': -5903732383745171240,
                                        'height': -960175325333113144,
                                    },
                            {
                                        'identifier': 3007297,
                                        'width': -2376547510564853604,
                                        'height': -405945502070583796,
                                    },
                            {
                                        'identifier': 5326539,
                                        'width': 5611852435761057201,
                                        'height': 8731220286800903273,
                                    },
                            {
                                        'identifier': 4130114,
                                        'width': -4697474048719898254,
                                        'height': 9151768955563172361,
                                    },
                            {
                                        'identifier': -48667,
                                        'width': -5010862487297168997,
                                        'height': -7056683009661558876,
                                    },
                            {
                                        'identifier': 8917097,
                                        'width': -1293726204362922733,
                                        'height': 357200843575574682,
                                    },
                            {
                                        'identifier': 2794561,
                                        'width': 1966682283002323096,
                                        'height': 7086945539636205973,
                                    },
                            {
                                        'identifier': 6722398,
                                        'width': -3652647726914816850,
                                        'height': -6305127457965668474,
                                    },
                            {
                                        'identifier': 7966789,
                                        'width': 1042111684726194072,
                                        'height': 2859412611496831951,
                                    },
                            {
                                        'identifier': 6086901,
                                        'width': -6710636058613339073,
                                        'height': -136826774326311468,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1965007,
                                        'source_nw_x_pixel': -8813973787687098044,
                                        'source_nw_y_pixel': -3631066536586716943,
                                        'source_pixel_width': -6939873783407777566,
                                        'source_pixel_height': -7175984764600291217,
                                        'rotation': -7475530120900124571,
                                        'virtual_nw_x_pixel': 1498742734,
                                        'virtual_nw_y_pixel': -1084090555,
                                        'virtual_width': 382991018,
                                        'virtual_height': -536131962,
                                    },
                            {
                                        'source_monitor': 4989533,
                                        'source_nw_x_pixel': -9179750903683244226,
                                        'source_nw_y_pixel': -2463344992639632297,
                                        'source_pixel_width': -2772064503943812721,
                                        'source_pixel_height': -7287304762947567784,
                                        'rotation': -5318598283200984062,
                                        'virtual_nw_x_pixel': 972060812,
                                        'virtual_nw_y_pixel': 1823691216,
                                        'virtual_width': -51237027,
                                        'virtual_height': -447483827,
                                    },
                            {
                                        'source_monitor': 6138871,
                                        'source_nw_x_pixel': -5389251364848414478,
                                        'source_nw_y_pixel': -4310126358597909950,
                                        'source_pixel_width': -39268302875567448,
                                        'source_pixel_height': -422017129944248190,
                                        'rotation': -8526079676302918540,
                                        'virtual_nw_x_pixel': -220035236,
                                        'virtual_nw_y_pixel': 474820858,
                                        'virtual_width': -1153874322,
                                        'virtual_height': 446119469,
                                    },
                            {
                                        'source_monitor': 2401743,
                                        'source_nw_x_pixel': -7685941324239434616,
                                        'source_nw_y_pixel': -7827962920590023022,
                                        'source_pixel_width': -73634317983223582,
                                        'source_pixel_height': -2204140611430267057,
                                        'rotation': -914823440349305359,
                                        'virtual_nw_x_pixel': -213492536,
                                        'virtual_nw_y_pixel': 1677859082,
                                        'virtual_width': -683886393,
                                        'virtual_height': 490814106,
                                    },
                            {
                                        'source_monitor': 9783041,
                                        'source_nw_x_pixel': -8223472641872650478,
                                        'source_nw_y_pixel': -1470839604488921766,
                                        'source_pixel_width': -7943112334469207816,
                                        'source_pixel_height': -3012852933723741371,
                                        'rotation': -6484520548521355210,
                                        'virtual_nw_x_pixel': 1076019205,
                                        'virtual_nw_y_pixel': -1890989701,
                                        'virtual_width': -1824142156,
                                        'virtual_height': -74209303,
                                    },
                            {
                                        'source_monitor': 7942558,
                                        'source_nw_x_pixel': -660756897811846675,
                                        'source_nw_y_pixel': -6484924396659787482,
                                        'source_pixel_width': -2963735540994201964,
                                        'source_pixel_height': -7079176877499108501,
                                        'rotation': -2936751528445414899,
                                        'virtual_nw_x_pixel': 1404881193,
                                        'virtual_nw_y_pixel': -1862125788,
                                        'virtual_width': 1193058240,
                                        'virtual_height': -496631977,
                                    },
                            {
                                        'source_monitor': 1197727,
                                        'source_nw_x_pixel': -1722304224605620165,
                                        'source_nw_y_pixel': -1417270062563474834,
                                        'source_pixel_width': -2070569726896530928,
                                        'source_pixel_height': -7556381580337591330,
                                        'rotation': -867140764053557817,
                                        'virtual_nw_x_pixel': -771673128,
                                        'virtual_nw_y_pixel': 708669422,
                                        'virtual_width': 901146425,
                                        'virtual_height': -173283355,
                                    },
                            {
                                        'source_monitor': 7472020,
                                        'source_nw_x_pixel': -2394483613962978215,
                                        'source_nw_y_pixel': -5236713245117078672,
                                        'source_pixel_width': -5477399570584571121,
                                        'source_pixel_height': -1173062716678027921,
                                        'rotation': -2836440977444641860,
                                        'virtual_nw_x_pixel': -926456298,
                                        'virtual_nw_y_pixel': -62766812,
                                        'virtual_width': 611840248,
                                        'virtual_height': 1721445247,
                                    },
                            {
                                        'source_monitor': 733827,
                                        'source_nw_x_pixel': -4554273654519959289,
                                        'source_nw_y_pixel': -6634002681073256712,
                                        'source_pixel_width': -8009585146266760576,
                                        'source_pixel_height': -993117603317442978,
                                        'rotation': -3142242711946604714,
                                        'virtual_nw_x_pixel': 1474421124,
                                        'virtual_nw_y_pixel': 1430351602,
                                        'virtual_width': -776786362,
                                        'virtual_height': 1907502830,
                                    },
                            {
                                        'source_monitor': 2010646,
                                        'source_nw_x_pixel': -126364605767264567,
                                        'source_nw_y_pixel': -3905147899105214893,
                                        'source_pixel_width': -6558493368313333243,
                                        'source_pixel_height': -1712817592317200760,
                                        'rotation': -5993929022884022724,
                                        'virtual_nw_x_pixel': -1678023427,
                                        'virtual_nw_y_pixel': 1376410938,
                                        'virtual_width': 986539288,
                                        'virtual_height': 994204028,
                                    },
                        ],
                },
                {
                    'description': 'л±ϕÑƟКªӯŦ҄§Ҽ9иƾȁÄ$ƋǽŢϑʋŻɍȆ|ŝRξ',
                    'monitors': [
                            {
                                        'identifier': -847368,
                                        'width': -2661193160278271955,
                                        'height': -2707348759458131466,
                                    },
                            {
                                        'identifier': -361185,
                                        'width': 8533291913299974823,
                                        'height': 535766858581230326,
                                    },
                            {
                                        'identifier': 7368961,
                                        'width': -5288038031085063560,
                                        'height': -4773441152066533846,
                                    },
                            {
                                        'identifier': 1601335,
                                        'width': -4665079168710551490,
                                        'height': -8372796102133183797,
                                    },
                            {
                                        'identifier': 6273427,
                                        'width': 7471093598896445929,
                                        'height': -6670551680168659757,
                                    },
                            {
                                        'identifier': 6908148,
                                        'width': -3634570603072386061,
                                        'height': 4947451021730622411,
                                    },
                            {
                                        'identifier': 6711783,
                                        'width': -237885304311968347,
                                        'height': -5257926492027599995,
                                    },
                            {
                                        'identifier': 9861175,
                                        'width': 2177026328266619061,
                                        'height': 8587191593809992028,
                                    },
                            {
                                        'identifier': 9757301,
                                        'width': -1127274450993935054,
                                        'height': -8033019481164867379,
                                    },
                            {
                                        'identifier': 1414911,
                                        'width': -1809483842616156967,
                                        'height': -7106189661961030433,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2853444,
                                        'source_nw_x_pixel': -2272013055998236294,
                                        'source_nw_y_pixel': -5850847907004145203,
                                        'source_pixel_width': -6037645854813033760,
                                        'source_pixel_height': -6100966550434626947,
                                        'rotation': -4507120708917183142,
                                        'virtual_nw_x_pixel': 1500707261,
                                        'virtual_nw_y_pixel': 1600268019,
                                        'virtual_width': 1760292413,
                                        'virtual_height': -970861777,
                                    },
                            {
                                        'source_monitor': 4424301,
                                        'source_nw_x_pixel': -5004908404564687817,
                                        'source_nw_y_pixel': -5134297343865582134,
                                        'source_pixel_width': -7716790212565259926,
                                        'source_pixel_height': -967366709544909201,
                                        'rotation': -7399044103576950573,
                                        'virtual_nw_x_pixel': 827204784,
                                        'virtual_nw_y_pixel': -353580157,
                                        'virtual_width': 72605110,
                                        'virtual_height': -1550412288,
                                    },
                            {
                                        'source_monitor': 8014219,
                                        'source_nw_x_pixel': -5035358768483180210,
                                        'source_nw_y_pixel': -6758133707159153555,
                                        'source_pixel_width': -8527451624198146645,
                                        'source_pixel_height': -8832085892420045935,
                                        'rotation': -4293214633666749732,
                                        'virtual_nw_x_pixel': 1238865000,
                                        'virtual_nw_y_pixel': -551171187,
                                        'virtual_width': 342652638,
                                        'virtual_height': 1269041376,
                                    },
                            {
                                        'source_monitor': 5809413,
                                        'source_nw_x_pixel': -3663201671147240885,
                                        'source_nw_y_pixel': -2192443743761560460,
                                        'source_pixel_width': -4984449772197175457,
                                        'source_pixel_height': -3491131216709781081,
                                        'rotation': -225638083822651991,
                                        'virtual_nw_x_pixel': 786548486,
                                        'virtual_nw_y_pixel': -1766175059,
                                        'virtual_width': -1608963729,
                                        'virtual_height': -1228494050,
                                    },
                            {
                                        'source_monitor': 1092365,
                                        'source_nw_x_pixel': -1525502113273126465,
                                        'source_nw_y_pixel': -4769590086352631409,
                                        'source_pixel_width': -1392148447277322870,
                                        'source_pixel_height': -1560071063653466075,
                                        'rotation': -5357886241607511463,
                                        'virtual_nw_x_pixel': -1714407837,
                                        'virtual_nw_y_pixel': 1213893318,
                                        'virtual_width': 1196493186,
                                        'virtual_height': -258071566,
                                    },
                            {
                                        'source_monitor': 632454,
                                        'source_nw_x_pixel': -1970574281321732955,
                                        'source_nw_y_pixel': -7195547301499832997,
                                        'source_pixel_width': -1674626255493812420,
                                        'source_pixel_height': -3528805511890144950,
                                        'rotation': -4219420807608040801,
                                        'virtual_nw_x_pixel': 1334454310,
                                        'virtual_nw_y_pixel': -683350925,
                                        'virtual_width': -1495987505,
                                        'virtual_height': 855597359,
                                    },
                            {
                                        'source_monitor': 6126689,
                                        'source_nw_x_pixel': -1342392840442732939,
                                        'source_nw_y_pixel': -1402866712075493154,
                                        'source_pixel_width': -3021884382416398469,
                                        'source_pixel_height': -2846402613579026796,
                                        'rotation': -5482502477957796967,
                                        'virtual_nw_x_pixel': -1742780484,
                                        'virtual_nw_y_pixel': 1716308973,
                                        'virtual_width': 1405441536,
                                        'virtual_height': 143767290,
                                    },
                            {
                                        'source_monitor': 5753380,
                                        'source_nw_x_pixel': -2384974596214417660,
                                        'source_nw_y_pixel': -7788403046646335583,
                                        'source_pixel_width': -3583051745106346518,
                                        'source_pixel_height': -7134337405119195967,
                                        'rotation': -4439072548398014500,
                                        'virtual_nw_x_pixel': -720114775,
                                        'virtual_nw_y_pixel': 1249098332,
                                        'virtual_width': -968199313,
                                        'virtual_height': -471918603,
                                    },
                            {
                                        'source_monitor': 7611651,
                                        'source_nw_x_pixel': -3440450457705603482,
                                        'source_nw_y_pixel': -1213787843512800961,
                                        'source_pixel_width': -2968098371235673304,
                                        'source_pixel_height': -8957845780380347117,
                                        'rotation': -6608696798308336566,
                                        'virtual_nw_x_pixel': -900659278,
                                        'virtual_nw_y_pixel': 894392212,
                                        'virtual_width': 1707556396,
                                        'virtual_height': 1375847374,
                                    },
                            {
                                        'source_monitor': 2143618,
                                        'source_nw_x_pixel': -3667032678188506933,
                                        'source_nw_y_pixel': -5109728502425533056,
                                        'source_pixel_width': -9209860984706931833,
                                        'source_pixel_height': -1443518964137828372,
                                        'rotation': -911944858471107122,
                                        'virtual_nw_x_pixel': 1671084167,
                                        'virtual_nw_y_pixel': -312055783,
                                        'virtual_width': 961639787,
                                        'virtual_height': 828393558,
                                    },
                        ],
                },
                {
                    'description': 'a\x9bµжЭ`өʀΠűȦǏȄɰ\u0381ҷĈėИҹҰıȽǱĐ<5Ƚʩԉ',
                    'monitors': [
                            {
                                        'identifier': 6801083,
                                        'width': -5846214877860627052,
                                        'height': -4573163258193436118,
                                    },
                            {
                                        'identifier': 7107660,
                                        'width': -4500365765853948921,
                                        'height': -7607021565601269104,
                                    },
                            {
                                        'identifier': 4108349,
                                        'width': 2855377366457635454,
                                        'height': 2116484047325881961,
                                    },
                            {
                                        'identifier': 3161683,
                                        'width': 5412832499649703915,
                                        'height': 5173555934514155091,
                                    },
                            {
                                        'identifier': 2583815,
                                        'width': 8291669226594870285,
                                        'height': -6007575140023253139,
                                    },
                            {
                                        'identifier': 4674141,
                                        'width': -1624843555025724074,
                                        'height': -2173584483682476592,
                                    },
                            {
                                        'identifier': 8126879,
                                        'width': 1859341529191797364,
                                        'height': 6927140934439153840,
                                    },
                            {
                                        'identifier': 5962807,
                                        'width': 4362996932092885734,
                                        'height': -3410065513137206791,
                                    },
                            {
                                        'identifier': 7536525,
                                        'width': -8291382782284412689,
                                        'height': 2476549784388689005,
                                    },
                            {
                                        'identifier': 8574512,
                                        'width': -6299931057936235301,
                                        'height': -4214359639146927553,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8058071,
                                        'source_nw_x_pixel': -3866086583378825439,
                                        'source_nw_y_pixel': -738018934894333911,
                                        'source_pixel_width': -1077896560576270418,
                                        'source_pixel_height': -6998034076754168586,
                                        'rotation': -5032654078515170277,
                                        'virtual_nw_x_pixel': 1675840489,
                                        'virtual_nw_y_pixel': 1107441834,
                                        'virtual_width': 265519403,
                                        'virtual_height': 1955366933,
                                    },
                            {
                                        'source_monitor': 6315434,
                                        'source_nw_x_pixel': -1957955768487957675,
                                        'source_nw_y_pixel': -4925601984372916349,
                                        'source_pixel_width': -8939339594142027381,
                                        'source_pixel_height': -3542007540723576096,
                                        'rotation': -1822413307670445030,
                                        'virtual_nw_x_pixel': 528190000,
                                        'virtual_nw_y_pixel': -1008343210,
                                        'virtual_width': -1423382198,
                                        'virtual_height': 1746886842,
                                    },
                            {
                                        'source_monitor': 6302609,
                                        'source_nw_x_pixel': -12565068752133512,
                                        'source_nw_y_pixel': -134621879129323151,
                                        'source_pixel_width': -8085320085380496263,
                                        'source_pixel_height': -60567753726042876,
                                        'rotation': -1637716084554727322,
                                        'virtual_nw_x_pixel': -1961524145,
                                        'virtual_nw_y_pixel': 184274202,
                                        'virtual_width': -27754011,
                                        'virtual_height': -1427838272,
                                    },
                            {
                                        'source_monitor': 2288133,
                                        'source_nw_x_pixel': -4862233054571283721,
                                        'source_nw_y_pixel': -3210972151015526472,
                                        'source_pixel_width': -5411650975135236437,
                                        'source_pixel_height': -1611782501843927737,
                                        'rotation': -1043664705521194506,
                                        'virtual_nw_x_pixel': -695630353,
                                        'virtual_nw_y_pixel': 557561962,
                                        'virtual_width': 485088253,
                                        'virtual_height': 1362266459,
                                    },
                            {
                                        'source_monitor': 2747936,
                                        'source_nw_x_pixel': -263084906316127100,
                                        'source_nw_y_pixel': -1315581383783478994,
                                        'source_pixel_width': -6536566262399305272,
                                        'source_pixel_height': -4151871612169128496,
                                        'rotation': -6101953675596501085,
                                        'virtual_nw_x_pixel': -1438965612,
                                        'virtual_nw_y_pixel': 1816945915,
                                        'virtual_width': 810018184,
                                        'virtual_height': 1390853491,
                                    },
                            {
                                        'source_monitor': 6944591,
                                        'source_nw_x_pixel': -3616471723575773667,
                                        'source_nw_y_pixel': -5652014601499589850,
                                        'source_pixel_width': -8350735226142178147,
                                        'source_pixel_height': -1590771646343413964,
                                        'rotation': -4193569312057814729,
                                        'virtual_nw_x_pixel': -242717561,
                                        'virtual_nw_y_pixel': 1149261933,
                                        'virtual_width': 605283808,
                                        'virtual_height': -1840495431,
                                    },
                            {
                                        'source_monitor': 3140915,
                                        'source_nw_x_pixel': -1885215726402121419,
                                        'source_nw_y_pixel': -7090334861999471692,
                                        'source_pixel_width': -1033686547391498929,
                                        'source_pixel_height': -4986678386781090591,
                                        'rotation': -7310125047573454674,
                                        'virtual_nw_x_pixel': 823144634,
                                        'virtual_nw_y_pixel': 1406096173,
                                        'virtual_width': 1348763580,
                                        'virtual_height': -757465082,
                                    },
                            {
                                        'source_monitor': 4751593,
                                        'source_nw_x_pixel': -2938140909721814512,
                                        'source_nw_y_pixel': -6291148470798244413,
                                        'source_pixel_width': -2653009578595059415,
                                        'source_pixel_height': -2365270651814073591,
                                        'rotation': -4164087841377879950,
                                        'virtual_nw_x_pixel': 1884054227,
                                        'virtual_nw_y_pixel': -752461283,
                                        'virtual_width': -145136166,
                                        'virtual_height': 1677831189,
                                    },
                            {
                                        'source_monitor': 2140359,
                                        'source_nw_x_pixel': -7899153015471483641,
                                        'source_nw_y_pixel': -9085764108415836037,
                                        'source_pixel_width': -2217038565188426477,
                                        'source_pixel_height': -80393215549889788,
                                        'rotation': -3577431389045893918,
                                        'virtual_nw_x_pixel': -661992831,
                                        'virtual_nw_y_pixel': 1371897154,
                                        'virtual_width': 599690366,
                                        'virtual_height': -1927963744,
                                    },
                            {
                                        'source_monitor': 2959742,
                                        'source_nw_x_pixel': -298740778925465769,
                                        'source_nw_y_pixel': -6159504771175393904,
                                        'source_pixel_width': -8900286550560119237,
                                        'source_pixel_height': -6231756347236103722,
                                        'rotation': -4088204398379920910,
                                        'virtual_nw_x_pixel': 560732834,
                                        'virtual_nw_y_pixel': 853766106,
                                        'virtual_width': -1680458651,
                                        'virtual_height': -563000372,
                                    },
                        ],
                },
                {
                    'description': 'Ƒ\x9aÜǉӾӔҳӢʔ˸\u0381ѬԄҧϢ˅ΤͷιŔæԭžхѭƚŽΗ˵Ҝ',
                    'monitors': [
                            {
                                        'identifier': 3527319,
                                        'width': 6430858246879660444,
                                        'height': 5209311187632487927,
                                    },
                            {
                                        'identifier': -442143,
                                        'width': 5850864525774797165,
                                        'height': 3659774861973490696,
                                    },
                            {
                                        'identifier': 4728083,
                                        'width': -8549242138432377076,
                                        'height': -3071755502021752376,
                                    },
                            {
                                        'identifier': 9835384,
                                        'width': 2131472281860527171,
                                        'height': -6411333569516818135,
                                    },
                            {
                                        'identifier': 5024429,
                                        'width': 2034736194997142740,
                                        'height': 7110551897177599041,
                                    },
                            {
                                        'identifier': 5824003,
                                        'width': 8222172739347611388,
                                        'height': -2295358708361000627,
                                    },
                            {
                                        'identifier': 8105240,
                                        'width': 162585834753658574,
                                        'height': -8734888896029339112,
                                    },
                            {
                                        'identifier': 8914231,
                                        'width': -1623860378614300120,
                                        'height': -6197483621955692845,
                                    },
                            {
                                        'identifier': 304264,
                                        'width': -753787025804312260,
                                        'height': 3815029890584269528,
                                    },
                            {
                                        'identifier': 2649599,
                                        'width': -6537280046124292657,
                                        'height': 7895073723657596277,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 763815,
                                        'source_nw_x_pixel': -4065311883274352270,
                                        'source_nw_y_pixel': -2032651590626380370,
                                        'source_pixel_width': -6208002182581346268,
                                        'source_pixel_height': -8590175751803892889,
                                        'rotation': -3987739823792402896,
                                        'virtual_nw_x_pixel': 1648310270,
                                        'virtual_nw_y_pixel': 1072727880,
                                        'virtual_width': 347694693,
                                        'virtual_height': 747346560,
                                    },
                            {
                                        'source_monitor': 5510210,
                                        'source_nw_x_pixel': -2213364687530322299,
                                        'source_nw_y_pixel': -2423856033881954661,
                                        'source_pixel_width': -5893453460681873333,
                                        'source_pixel_height': -5630765033229653889,
                                        'rotation': -2373816939223026836,
                                        'virtual_nw_x_pixel': -1205600426,
                                        'virtual_nw_y_pixel': 483092120,
                                        'virtual_width': 1021582583,
                                        'virtual_height': -1971217981,
                                    },
                            {
                                        'source_monitor': 4242340,
                                        'source_nw_x_pixel': -2954329177920282497,
                                        'source_nw_y_pixel': -686001350178080412,
                                        'source_pixel_width': -3144908938000219964,
                                        'source_pixel_height': -7568399426004539109,
                                        'rotation': -4594049896446075097,
                                        'virtual_nw_x_pixel': -442879482,
                                        'virtual_nw_y_pixel': 1483385795,
                                        'virtual_width': -1189173978,
                                        'virtual_height': -1712337577,
                                    },
                            {
                                        'source_monitor': 9497293,
                                        'source_nw_x_pixel': -5046296430087951234,
                                        'source_nw_y_pixel': -4853466442185780994,
                                        'source_pixel_width': -7673831429456567392,
                                        'source_pixel_height': -7190902679459028988,
                                        'rotation': -4943713174328355544,
                                        'virtual_nw_x_pixel': -539604017,
                                        'virtual_nw_y_pixel': -894755938,
                                        'virtual_width': -1120318050,
                                        'virtual_height': 469082470,
                                    },
                            {
                                        'source_monitor': 5451957,
                                        'source_nw_x_pixel': -3348436035857018191,
                                        'source_nw_y_pixel': -8975502584277536107,
                                        'source_pixel_width': -1568729160670202424,
                                        'source_pixel_height': -1163630729934272292,
                                        'rotation': -7990681648632029171,
                                        'virtual_nw_x_pixel': 1312678118,
                                        'virtual_nw_y_pixel': -172774764,
                                        'virtual_width': -288686639,
                                        'virtual_height': 497651984,
                                    },
                            {
                                        'source_monitor': 182750,
                                        'source_nw_x_pixel': -4115209682351265333,
                                        'source_nw_y_pixel': -2198795325272399192,
                                        'source_pixel_width': -2480711382286925583,
                                        'source_pixel_height': -2968400327851673807,
                                        'rotation': -8956389300672952862,
                                        'virtual_nw_x_pixel': -601364489,
                                        'virtual_nw_y_pixel': 1226707874,
                                        'virtual_width': -520122682,
                                        'virtual_height': -872243228,
                                    },
                            {
                                        'source_monitor': 6229543,
                                        'source_nw_x_pixel': -4666322934023674043,
                                        'source_nw_y_pixel': -2763326143888314633,
                                        'source_pixel_width': -1868637245042827274,
                                        'source_pixel_height': -2433922583323814195,
                                        'rotation': -2358231869284214612,
                                        'virtual_nw_x_pixel': 1586559973,
                                        'virtual_nw_y_pixel': -1246773194,
                                        'virtual_width': -959476330,
                                        'virtual_height': -1682105621,
                                    },
                            {
                                        'source_monitor': 2890107,
                                        'source_nw_x_pixel': -3436188098844977434,
                                        'source_nw_y_pixel': -1423342295617691337,
                                        'source_pixel_width': -5255255542166149599,
                                        'source_pixel_height': -643441655457523267,
                                        'rotation': -5921509955590919182,
                                        'virtual_nw_x_pixel': -1401744308,
                                        'virtual_nw_y_pixel': 536905417,
                                        'virtual_width': 837051944,
                                        'virtual_height': 756225403,
                                    },
                            {
                                        'source_monitor': 3795906,
                                        'source_nw_x_pixel': -3116196580769588084,
                                        'source_nw_y_pixel': -7841130134265050060,
                                        'source_pixel_width': -1485005857190023419,
                                        'source_pixel_height': -4986414817463962997,
                                        'rotation': -1044112738712375851,
                                        'virtual_nw_x_pixel': 895106233,
                                        'virtual_nw_y_pixel': -401718511,
                                        'virtual_width': 1673788328,
                                        'virtual_height': -584461789,
                                    },
                            {
                                        'source_monitor': 2245647,
                                        'source_nw_x_pixel': -5505196745391161188,
                                        'source_nw_y_pixel': -8694648402399150460,
                                        'source_pixel_width': -1442158298579239197,
                                        'source_pixel_height': -4097688204447391543,
                                        'rotation': -1893207757100206290,
                                        'virtual_nw_x_pixel': -292128243,
                                        'virtual_nw_y_pixel': -120447069,
                                        'virtual_width': 745823279,
                                        'virtual_height': -1204501173,
                                    },
                        ],
                },
                {
                    'description': '¸ȵȺɏ¦ǰцñҸɶӜ"ћ\x8eУͻҽҔнѱΕȭh\x9evҘҰäɣϱ',
                    'monitors': [
                            {
                                        'identifier': 2488148,
                                        'width': -7717167329339317359,
                                        'height': -4179119754693317533,
                                    },
                            {
                                        'identifier': 3440543,
                                        'width': -1306469576532071349,
                                        'height': -7732275353543951395,
                                    },
                            {
                                        'identifier': 5939699,
                                        'width': -2458815166927359953,
                                        'height': 7687398466868195089,
                                    },
                            {
                                        'identifier': 3526618,
                                        'width': -6976348189512517105,
                                        'height': -9036427872501942972,
                                    },
                            {
                                        'identifier': 8289180,
                                        'width': 1002461600756373025,
                                        'height': 1487689685455350448,
                                    },
                            {
                                        'identifier': 2711406,
                                        'width': 4176744189609379001,
                                        'height': 221371006215624410,
                                    },
                            {
                                        'identifier': 3291929,
                                        'width': -6925147908113236404,
                                        'height': -7156880682698217108,
                                    },
                            {
                                        'identifier': 2334863,
                                        'width': 5458663774910068485,
                                        'height': -8854518633857102846,
                                    },
                            {
                                        'identifier': 4563548,
                                        'width': 1646502882721056535,
                                        'height': 5093545388352389528,
                                    },
                            {
                                        'identifier': 2836815,
                                        'width': -1882562970670915891,
                                        'height': 6557943732421261564,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4571601,
                                        'source_nw_x_pixel': -4149809096675677290,
                                        'source_nw_y_pixel': -1928580872947875005,
                                        'source_pixel_width': -213077123187948521,
                                        'source_pixel_height': -423381257563473301,
                                        'rotation': -3459876460813923477,
                                        'virtual_nw_x_pixel': -1035699475,
                                        'virtual_nw_y_pixel': -613146378,
                                        'virtual_width': -655249276,
                                        'virtual_height': 1718091802,
                                    },
                            {
                                        'source_monitor': 1946407,
                                        'source_nw_x_pixel': -1888214766998203039,
                                        'source_nw_y_pixel': -1090119958066227060,
                                        'source_pixel_width': -8085691403641753468,
                                        'source_pixel_height': -5424403927342909972,
                                        'rotation': -5289803876769804368,
                                        'virtual_nw_x_pixel': -97682388,
                                        'virtual_nw_y_pixel': -1142468728,
                                        'virtual_width': -661933745,
                                        'virtual_height': 1637250078,
                                    },
                            {
                                        'source_monitor': 4042412,
                                        'source_nw_x_pixel': -2513577361906707009,
                                        'source_nw_y_pixel': -8653132507087094798,
                                        'source_pixel_width': -1093940106389909358,
                                        'source_pixel_height': -4354732252529034410,
                                        'rotation': -7706767160871545370,
                                        'virtual_nw_x_pixel': -350283015,
                                        'virtual_nw_y_pixel': -775772689,
                                        'virtual_width': -114147907,
                                        'virtual_height': -496177959,
                                    },
                            {
                                        'source_monitor': 7186498,
                                        'source_nw_x_pixel': -4378642931095079810,
                                        'source_nw_y_pixel': -2352007382153557390,
                                        'source_pixel_width': -2969051152143919642,
                                        'source_pixel_height': -173069852405750288,
                                        'rotation': -7231361532070071133,
                                        'virtual_nw_x_pixel': 1177490490,
                                        'virtual_nw_y_pixel': -1524906235,
                                        'virtual_width': 1860009357,
                                        'virtual_height': 1239693232,
                                    },
                            {
                                        'source_monitor': 4023515,
                                        'source_nw_x_pixel': -621947483254593989,
                                        'source_nw_y_pixel': -6902562206908033868,
                                        'source_pixel_width': -7134755041034123657,
                                        'source_pixel_height': -1614301670927414931,
                                        'rotation': -4537495181109855061,
                                        'virtual_nw_x_pixel': 768062788,
                                        'virtual_nw_y_pixel': 705363785,
                                        'virtual_width': -1819638848,
                                        'virtual_height': 1768050331,
                                    },
                            {
                                        'source_monitor': 6987918,
                                        'source_nw_x_pixel': -2160738593931812416,
                                        'source_nw_y_pixel': -4404775794227606106,
                                        'source_pixel_width': -6980404542751805147,
                                        'source_pixel_height': -5685528566256239461,
                                        'rotation': -840748673066369339,
                                        'virtual_nw_x_pixel': 725317624,
                                        'virtual_nw_y_pixel': 822187965,
                                        'virtual_width': 1097917026,
                                        'virtual_height': -328181257,
                                    },
                            {
                                        'source_monitor': 2914822,
                                        'source_nw_x_pixel': -7223429371259329996,
                                        'source_nw_y_pixel': -4115937187894268769,
                                        'source_pixel_width': -7606456873689903954,
                                        'source_pixel_height': -8867723468024141140,
                                        'rotation': -7900573298579095710,
                                        'virtual_nw_x_pixel': 1790005368,
                                        'virtual_nw_y_pixel': -1285497069,
                                        'virtual_width': 441723252,
                                        'virtual_height': 1910667263,
                                    },
                            {
                                        'source_monitor': 5169492,
                                        'source_nw_x_pixel': -6563283370863143153,
                                        'source_nw_y_pixel': -1776475948589584345,
                                        'source_pixel_width': -2822264586389688167,
                                        'source_pixel_height': -24477342372324406,
                                        'rotation': -6278027854531780521,
                                        'virtual_nw_x_pixel': 180067755,
                                        'virtual_nw_y_pixel': 1401531246,
                                        'virtual_width': 1764975500,
                                        'virtual_height': 1514060543,
                                    },
                            {
                                        'source_monitor': 8884554,
                                        'source_nw_x_pixel': -8566401159215326642,
                                        'source_nw_y_pixel': -7977507826586394823,
                                        'source_pixel_width': -7193950372958558916,
                                        'source_pixel_height': -8170254146745740393,
                                        'rotation': -7900498381892204984,
                                        'virtual_nw_x_pixel': -149002447,
                                        'virtual_nw_y_pixel': 1569305419,
                                        'virtual_width': 1526829961,
                                        'virtual_height': -1271244863,
                                    },
                            {
                                        'source_monitor': 1921469,
                                        'source_nw_x_pixel': -5990660248917836966,
                                        'source_nw_y_pixel': -8669246832033889151,
                                        'source_pixel_width': -6127468613817820448,
                                        'source_pixel_height': -2088463301618364203,
                                        'rotation': -6337799982605070610,
                                        'virtual_nw_x_pixel': -767854189,
                                        'virtual_nw_y_pixel': -102714775,
                                        'virtual_width': -1280418051,
                                        'virtual_height': 1613781119,
                                    },
                        ],
                },
                {
                    'description': 'ʪĤˈ\x93ΦɷӸщűŖƠϢό˞ϩİ\x80ϠLҚ˰ȼŻǂҩԀӥŃɼɹ',
                    'monitors': [
                            {
                                        'identifier': 9998988,
                                        'width': -5118072251959659030,
                                        'height': 3709564145078747543,
                                    },
                            {
                                        'identifier': 4562270,
                                        'width': -489740740385173380,
                                        'height': -298204191602668797,
                                    },
                            {
                                        'identifier': 9644953,
                                        'width': 3968662613103062273,
                                        'height': -2188447406815289603,
                                    },
                            {
                                        'identifier': 1004097,
                                        'width': 2601776052428213773,
                                        'height': -6634218854172954191,
                                    },
                            {
                                        'identifier': 5789155,
                                        'width': 3294564840038187021,
                                        'height': 8527962317790390405,
                                    },
                            {
                                        'identifier': 9586027,
                                        'width': 4910876631756610384,
                                        'height': -6214104873331566466,
                                    },
                            {
                                        'identifier': -686131,
                                        'width': 5178331947224797899,
                                        'height': -4517464334421780066,
                                    },
                            {
                                        'identifier': 4001010,
                                        'width': 1411190951071050339,
                                        'height': 773748541755328646,
                                    },
                            {
                                        'identifier': 4799984,
                                        'width': 1398820661576539474,
                                        'height': 389358648674168781,
                                    },
                            {
                                        'identifier': 5643746,
                                        'width': -3413248919325165075,
                                        'height': 9154285422180726802,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -122617,
                                        'source_nw_x_pixel': -7643770969528217783,
                                        'source_nw_y_pixel': -2385666881486688112,
                                        'source_pixel_width': -3439202660755173543,
                                        'source_pixel_height': -6157365062849474315,
                                        'rotation': -3554337984540572929,
                                        'virtual_nw_x_pixel': -362639874,
                                        'virtual_nw_y_pixel': -1628809753,
                                        'virtual_width': -729095088,
                                        'virtual_height': 480522419,
                                    },
                            {
                                        'source_monitor': 2110367,
                                        'source_nw_x_pixel': -495928426379809346,
                                        'source_nw_y_pixel': -4639155101725911134,
                                        'source_pixel_width': -7975081685809100162,
                                        'source_pixel_height': -6932850221042693964,
                                        'rotation': -6053923587156016177,
                                        'virtual_nw_x_pixel': -1747874542,
                                        'virtual_nw_y_pixel': -641021722,
                                        'virtual_width': -447823665,
                                        'virtual_height': -1456385783,
                                    },
                            {
                                        'source_monitor': 7443757,
                                        'source_nw_x_pixel': -317595833479788729,
                                        'source_nw_y_pixel': -7201766526255457756,
                                        'source_pixel_width': -1260202418169300372,
                                        'source_pixel_height': -4166990404424675310,
                                        'rotation': -1763286781417945176,
                                        'virtual_nw_x_pixel': -559702613,
                                        'virtual_nw_y_pixel': 1619827943,
                                        'virtual_width': 1416920418,
                                        'virtual_height': 346604826,
                                    },
                            {
                                        'source_monitor': 6705552,
                                        'source_nw_x_pixel': -7163015326337546079,
                                        'source_nw_y_pixel': -142924636979290411,
                                        'source_pixel_width': -6386274259989695256,
                                        'source_pixel_height': -19252484977418397,
                                        'rotation': -318066531415085559,
                                        'virtual_nw_x_pixel': -912892288,
                                        'virtual_nw_y_pixel': 1967712034,
                                        'virtual_width': 152098861,
                                        'virtual_height': 1799811878,
                                    },
                            {
                                        'source_monitor': 7457837,
                                        'source_nw_x_pixel': -9161009693326528418,
                                        'source_nw_y_pixel': -9219648596392550091,
                                        'source_pixel_width': -7325293647217175316,
                                        'source_pixel_height': -570097575189666409,
                                        'rotation': -9202480418626137176,
                                        'virtual_nw_x_pixel': -270404431,
                                        'virtual_nw_y_pixel': 574853760,
                                        'virtual_width': 1737253661,
                                        'virtual_height': -122252328,
                                    },
                            {
                                        'source_monitor': 6952637,
                                        'source_nw_x_pixel': -8780641480750877024,
                                        'source_nw_y_pixel': -3856538153384892056,
                                        'source_pixel_width': -792300213733262963,
                                        'source_pixel_height': -3612347663716718453,
                                        'rotation': -7418743154050607066,
                                        'virtual_nw_x_pixel': -1670119966,
                                        'virtual_nw_y_pixel': -889366202,
                                        'virtual_width': -28996188,
                                        'virtual_height': -786982116,
                                    },
                            {
                                        'source_monitor': 9804201,
                                        'source_nw_x_pixel': -7051189205634913997,
                                        'source_nw_y_pixel': -6002747692036514661,
                                        'source_pixel_width': -6984322609176628485,
                                        'source_pixel_height': -1820503942152095306,
                                        'rotation': -3238549812687141185,
                                        'virtual_nw_x_pixel': -77923669,
                                        'virtual_nw_y_pixel': -1373529957,
                                        'virtual_width': -1401441452,
                                        'virtual_height': -747216840,
                                    },
                            {
                                        'source_monitor': 3048423,
                                        'source_nw_x_pixel': -7302231069377778731,
                                        'source_nw_y_pixel': -2654204186985722574,
                                        'source_pixel_width': -7612217973427339130,
                                        'source_pixel_height': -2064128099449462042,
                                        'rotation': -532737556349281915,
                                        'virtual_nw_x_pixel': 877094800,
                                        'virtual_nw_y_pixel': -1233347720,
                                        'virtual_width': -1434616447,
                                        'virtual_height': -977025878,
                                    },
                            {
                                        'source_monitor': -395662,
                                        'source_nw_x_pixel': -8546169579606207656,
                                        'source_nw_y_pixel': -6853776505090728479,
                                        'source_pixel_width': -7902032849166083739,
                                        'source_pixel_height': -4449519707394416102,
                                        'rotation': -8667364999516789331,
                                        'virtual_nw_x_pixel': -476958072,
                                        'virtual_nw_y_pixel': 224195713,
                                        'virtual_width': 1384853262,
                                        'virtual_height': 389496411,
                                    },
                            {
                                        'source_monitor': 2084247,
                                        'source_nw_x_pixel': -8413136353889889000,
                                        'source_nw_y_pixel': -3286119198723708843,
                                        'source_pixel_width': -845652624538673602,
                                        'source_pixel_height': -9149034644658088536,
                                        'rotation': -5043222400685248684,
                                        'virtual_nw_x_pixel': -1963061740,
                                        'virtual_nw_y_pixel': 1031167743,
                                        'virtual_width': 1886781522,
                                        'virtual_height': 1347437272,
                                    },
                        ],
                },
                {
                    'description': 'ƼȫƺʩΗςҽDӇвх҂ϜƋЪ=ĢøҸӆ<тΙƔҵ˞Ӧ±\u038dο',
                    'monitors': [
                            {
                                        'identifier': 7152412,
                                        'width': 5422481895601378401,
                                        'height': -498244441370645009,
                                    },
                            {
                                        'identifier': 2549027,
                                        'width': -3429587310614677675,
                                        'height': 465461423930052219,
                                    },
                            {
                                        'identifier': 6352050,
                                        'width': -2060903773458451840,
                                        'height': -1069671449271104405,
                                    },
                            {
                                        'identifier': 1594907,
                                        'width': -8746613977600637674,
                                        'height': 9174811258053375927,
                                    },
                            {
                                        'identifier': 8291185,
                                        'width': -2036206805477464627,
                                        'height': -4853391763721245713,
                                    },
                            {
                                        'identifier': 7559537,
                                        'width': -3901959687820764442,
                                        'height': -2172395815886930927,
                                    },
                            {
                                        'identifier': 2066433,
                                        'width': -7138525751878579073,
                                        'height': 2914262232302927507,
                                    },
                            {
                                        'identifier': 4692421,
                                        'width': -5149551922046666515,
                                        'height': 792943854488247886,
                                    },
                            {
                                        'identifier': 4470379,
                                        'width': 6747730521748068335,
                                        'height': 5918846403961538508,
                                    },
                            {
                                        'identifier': 106625,
                                        'width': 5971024219421768901,
                                        'height': -2624947545108580625,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -570692,
                                        'source_nw_x_pixel': -8180616524087362865,
                                        'source_nw_y_pixel': -7890995807867042665,
                                        'source_pixel_width': -2130178030841440810,
                                        'source_pixel_height': -4370620895013915968,
                                        'rotation': -7910931633510805825,
                                        'virtual_nw_x_pixel': 1049907596,
                                        'virtual_nw_y_pixel': 1730724420,
                                        'virtual_width': 1394436359,
                                        'virtual_height': 622099760,
                                    },
                            {
                                        'source_monitor': -531288,
                                        'source_nw_x_pixel': -4467229110662604518,
                                        'source_nw_y_pixel': -4298478645471051448,
                                        'source_pixel_width': -5868497793853414119,
                                        'source_pixel_height': -2284509283988117616,
                                        'rotation': -6959371311306811630,
                                        'virtual_nw_x_pixel': 1742953964,
                                        'virtual_nw_y_pixel': 515184473,
                                        'virtual_width': -1747535699,
                                        'virtual_height': -1581241066,
                                    },
                            {
                                        'source_monitor': 715088,
                                        'source_nw_x_pixel': -5882348305302846908,
                                        'source_nw_y_pixel': -4663713994680823351,
                                        'source_pixel_width': -1566674795810580053,
                                        'source_pixel_height': -6014972847790296390,
                                        'rotation': -8621937351628560301,
                                        'virtual_nw_x_pixel': 1172085534,
                                        'virtual_nw_y_pixel': 1026390104,
                                        'virtual_width': 925867989,
                                        'virtual_height': -522436117,
                                    },
                            {
                                        'source_monitor': 9098995,
                                        'source_nw_x_pixel': -100337807702169162,
                                        'source_nw_y_pixel': -7929623538153466363,
                                        'source_pixel_width': -3418284669025523077,
                                        'source_pixel_height': -2416856408899199214,
                                        'rotation': -5609791264545853937,
                                        'virtual_nw_x_pixel': 1784230049,
                                        'virtual_nw_y_pixel': 1839004556,
                                        'virtual_width': 239609765,
                                        'virtual_height': 1802637989,
                                    },
                            {
                                        'source_monitor': 7904884,
                                        'source_nw_x_pixel': -7659667384211604776,
                                        'source_nw_y_pixel': -1288069199045527969,
                                        'source_pixel_width': -2488689379291931940,
                                        'source_pixel_height': -1047505683584883221,
                                        'rotation': -1656533256868319659,
                                        'virtual_nw_x_pixel': 1408901399,
                                        'virtual_nw_y_pixel': -454999493,
                                        'virtual_width': -1260344037,
                                        'virtual_height': 1538199257,
                                    },
                            {
                                        'source_monitor': 3010019,
                                        'source_nw_x_pixel': -1891925098040154067,
                                        'source_nw_y_pixel': -6699852835704912469,
                                        'source_pixel_width': -1863662071706638660,
                                        'source_pixel_height': -2130838603161326037,
                                        'rotation': -6987667327292010837,
                                        'virtual_nw_x_pixel': -1263986797,
                                        'virtual_nw_y_pixel': 392551290,
                                        'virtual_width': -1293835559,
                                        'virtual_height': 579697672,
                                    },
                            {
                                        'source_monitor': 1980193,
                                        'source_nw_x_pixel': -2467554934754477278,
                                        'source_nw_y_pixel': -2395254800844380253,
                                        'source_pixel_width': -5119960896234786282,
                                        'source_pixel_height': -2003347443504879143,
                                        'rotation': -1507641951780281916,
                                        'virtual_nw_x_pixel': -1396760526,
                                        'virtual_nw_y_pixel': -249026503,
                                        'virtual_width': -1620862698,
                                        'virtual_height': -1676103859,
                                    },
                            {
                                        'source_monitor': 4451429,
                                        'source_nw_x_pixel': -1911250474168156765,
                                        'source_nw_y_pixel': -6732065452231103713,
                                        'source_pixel_width': -6626335061557510087,
                                        'source_pixel_height': -6129308787702798386,
                                        'rotation': -5097920425906957988,
                                        'virtual_nw_x_pixel': -1142394394,
                                        'virtual_nw_y_pixel': -1514820686,
                                        'virtual_width': -1196634091,
                                        'virtual_height': 760223632,
                                    },
                            {
                                        'source_monitor': 7852759,
                                        'source_nw_x_pixel': -5181449787777311069,
                                        'source_nw_y_pixel': -4170462495340447833,
                                        'source_pixel_width': -8129509075749917863,
                                        'source_pixel_height': -8360714106873905244,
                                        'rotation': -7423813422949164840,
                                        'virtual_nw_x_pixel': 1422327733,
                                        'virtual_nw_y_pixel': 307407478,
                                        'virtual_width': -1177194052,
                                        'virtual_height': 791744978,
                                    },
                            {
                                        'source_monitor': 7555147,
                                        'source_nw_x_pixel': -7937769157033191790,
                                        'source_nw_y_pixel': -8734525629049534586,
                                        'source_pixel_width': -8669908345161385054,
                                        'source_pixel_height': -8446371608504606339,
                                        'rotation': -5079067060282244780,
                                        'virtual_nw_x_pixel': -180097718,
                                        'virtual_nw_y_pixel': 1296308601,
                                        'virtual_width': 668210044,
                                        'virtual_height': 1878042714,
                                    },
                        ],
                },
                {
                    'description': '*ʑ\x9cȍǬÎîҨΩʵӹËˬ¾ӛφМеƛħƽІǎƼ\x80Ͼǁδӫҍ',
                    'monitors': [
                            {
                                        'identifier': 9698253,
                                        'width': -6783627064427835513,
                                        'height': -1142360643563768638,
                                    },
                            {
                                        'identifier': 316891,
                                        'width': 1729836592026685717,
                                        'height': -5748522581736180185,
                                    },
                            {
                                        'identifier': 9538780,
                                        'width': 2973722799181537700,
                                        'height': 1356700649502885633,
                                    },
                            {
                                        'identifier': 9072749,
                                        'width': 6578049217184256487,
                                        'height': 1364857493141797313,
                                    },
                            {
                                        'identifier': 3813431,
                                        'width': 537838516613048808,
                                        'height': 5214792879300246004,
                                    },
                            {
                                        'identifier': 7616775,
                                        'width': -2388507283599080822,
                                        'height': 9105281228914202639,
                                    },
                            {
                                        'identifier': 803802,
                                        'width': -271771734813497882,
                                        'height': -3151130756518300406,
                                    },
                            {
                                        'identifier': 3309067,
                                        'width': 8259608600147759182,
                                        'height': -8176541427592016223,
                                    },
                            {
                                        'identifier': 8621758,
                                        'width': 4137405105842653080,
                                        'height': -1774023355905129033,
                                    },
                            {
                                        'identifier': 8195430,
                                        'width': 1877398243165098272,
                                        'height': 8722233223119930056,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 583413,
                                        'source_nw_x_pixel': -1882606374662414472,
                                        'source_nw_y_pixel': -8979418859480346341,
                                        'source_pixel_width': -1328918579002299851,
                                        'source_pixel_height': -6535529505675532436,
                                        'rotation': -5707490874699152889,
                                        'virtual_nw_x_pixel': 1827182229,
                                        'virtual_nw_y_pixel': -1050390815,
                                        'virtual_width': -1764267766,
                                        'virtual_height': 1272991217,
                                    },
                            {
                                        'source_monitor': 31338,
                                        'source_nw_x_pixel': -2535177118448797350,
                                        'source_nw_y_pixel': -6827701453457183713,
                                        'source_pixel_width': -4827398052515988047,
                                        'source_pixel_height': -441468132623956797,
                                        'rotation': -350923994435962303,
                                        'virtual_nw_x_pixel': -1684572094,
                                        'virtual_nw_y_pixel': -562723208,
                                        'virtual_width': 1466392647,
                                        'virtual_height': -1273044501,
                                    },
                            {
                                        'source_monitor': 2027947,
                                        'source_nw_x_pixel': -7812274295390375104,
                                        'source_nw_y_pixel': -1571833661825990192,
                                        'source_pixel_width': -6748232370306743156,
                                        'source_pixel_height': -6942367873723447996,
                                        'rotation': -7735425197507664351,
                                        'virtual_nw_x_pixel': -816434459,
                                        'virtual_nw_y_pixel': 1676330954,
                                        'virtual_width': -910526446,
                                        'virtual_height': -1496780537,
                                    },
                            {
                                        'source_monitor': 6551027,
                                        'source_nw_x_pixel': -447410037990275920,
                                        'source_nw_y_pixel': -1300456891119460687,
                                        'source_pixel_width': -519638569125425550,
                                        'source_pixel_height': -2189060741413138206,
                                        'rotation': -7773070199589683166,
                                        'virtual_nw_x_pixel': 1788034033,
                                        'virtual_nw_y_pixel': 207747438,
                                        'virtual_width': -1255179447,
                                        'virtual_height': -50534504,
                                    },
                            {
                                        'source_monitor': 1909177,
                                        'source_nw_x_pixel': -6522313798779378250,
                                        'source_nw_y_pixel': -7955377705665716066,
                                        'source_pixel_width': -8427930875549855903,
                                        'source_pixel_height': -7819602726846937762,
                                        'rotation': -3135104430424139095,
                                        'virtual_nw_x_pixel': 537387625,
                                        'virtual_nw_y_pixel': 188820952,
                                        'virtual_width': 163091154,
                                        'virtual_height': -208829120,
                                    },
                            {
                                        'source_monitor': 4924582,
                                        'source_nw_x_pixel': -1406038203741531073,
                                        'source_nw_y_pixel': -2722484090690597660,
                                        'source_pixel_width': -501780354523940759,
                                        'source_pixel_height': -8280425385109199754,
                                        'rotation': -8388824648026816388,
                                        'virtual_nw_x_pixel': 813895692,
                                        'virtual_nw_y_pixel': -1923448078,
                                        'virtual_width': 1587594630,
                                        'virtual_height': 236044859,
                                    },
                            {
                                        'source_monitor': 1791685,
                                        'source_nw_x_pixel': -6017525445819868854,
                                        'source_nw_y_pixel': -5296841136143465296,
                                        'source_pixel_width': -2058447999547156237,
                                        'source_pixel_height': -7381531403564994702,
                                        'rotation': -1398007123991437106,
                                        'virtual_nw_x_pixel': -1456635134,
                                        'virtual_nw_y_pixel': -1987536676,
                                        'virtual_width': 975009080,
                                        'virtual_height': -894723903,
                                    },
                            {
                                        'source_monitor': 2913861,
                                        'source_nw_x_pixel': -1439312842353406773,
                                        'source_nw_y_pixel': -5504619748152156236,
                                        'source_pixel_width': -2966446759874058934,
                                        'source_pixel_height': -2808690135910193681,
                                        'rotation': -503497805400735316,
                                        'virtual_nw_x_pixel': 1378470384,
                                        'virtual_nw_y_pixel': -1801593817,
                                        'virtual_width': 787099621,
                                        'virtual_height': -1362884967,
                                    },
                            {
                                        'source_monitor': -740082,
                                        'source_nw_x_pixel': -3670255996939909428,
                                        'source_nw_y_pixel': -1504317491577288247,
                                        'source_pixel_width': -4955465072367453087,
                                        'source_pixel_height': -178689908573057473,
                                        'rotation': -8425159470159995047,
                                        'virtual_nw_x_pixel': 638679095,
                                        'virtual_nw_y_pixel': -682298077,
                                        'virtual_width': -75227713,
                                        'virtual_height': -954282016,
                                    },
                            {
                                        'source_monitor': -930967,
                                        'source_nw_x_pixel': -3372144906224386409,
                                        'source_nw_y_pixel': -1849402711041279003,
                                        'source_pixel_width': -3153149917297523381,
                                        'source_pixel_height': -2934822297533407314,
                                        'rotation': -2498909284772815328,
                                        'virtual_nw_x_pixel': -1590566578,
                                        'virtual_nw_y_pixel': -980044493,
                                        'virtual_width': 1842603738,
                                        'virtual_height': -334722962,
                                    },
                        ],
                },
                {
                    'description': 'ӴӀǍ˺ĺÜѴԚ\x9aɅnҨÇŴŏǔΐϺÛҵˍ˨ƀѿĊǴZϤҋµ',
                    'monitors': [
                            {
                                        'identifier': 1942861,
                                        'width': 5260350670108303800,
                                        'height': -8327988188262602146,
                                    },
                            {
                                        'identifier': 722913,
                                        'width': 4785015595772478889,
                                        'height': 3677291120346609741,
                                    },
                            {
                                        'identifier': 5223254,
                                        'width': -4311286036516089417,
                                        'height': 1439862955391467132,
                                    },
                            {
                                        'identifier': 7225598,
                                        'width': 4448050546751330657,
                                        'height': -1023001977669170890,
                                    },
                            {
                                        'identifier': 7212607,
                                        'width': -7709233587158069262,
                                        'height': 4202857652608097624,
                                    },
                            {
                                        'identifier': 356295,
                                        'width': 4887034871602171156,
                                        'height': -7194223273978241815,
                                    },
                            {
                                        'identifier': 9258219,
                                        'width': 3300786492755355316,
                                        'height': -7733681714640050548,
                                    },
                            {
                                        'identifier': 8103183,
                                        'width': 7720766327431878269,
                                        'height': -2099781373740349027,
                                    },
                            {
                                        'identifier': 5651031,
                                        'width': -1681863754415681751,
                                        'height': 6394834832453444563,
                                    },
                            {
                                        'identifier': 3747482,
                                        'width': 7027819564413548826,
                                        'height': -7503223110824458830,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1003109,
                                        'source_nw_x_pixel': -7423279692518714287,
                                        'source_nw_y_pixel': -7415048827349828867,
                                        'source_pixel_width': -3712944961571345149,
                                        'source_pixel_height': -1380233048227119378,
                                        'rotation': -5475621498334106820,
                                        'virtual_nw_x_pixel': -1529986748,
                                        'virtual_nw_y_pixel': -1986002983,
                                        'virtual_width': 1899533525,
                                        'virtual_height': -814081067,
                                    },
                            {
                                        'source_monitor': 6057175,
                                        'source_nw_x_pixel': -6140988207195978063,
                                        'source_nw_y_pixel': -8208391635591896009,
                                        'source_pixel_width': -293380358420184552,
                                        'source_pixel_height': -7379348555815195628,
                                        'rotation': -6065059943816430534,
                                        'virtual_nw_x_pixel': -1364282750,
                                        'virtual_nw_y_pixel': 1698131545,
                                        'virtual_width': -598288826,
                                        'virtual_height': -1208906896,
                                    },
                            {
                                        'source_monitor': 7448144,
                                        'source_nw_x_pixel': -5537410690166461830,
                                        'source_nw_y_pixel': -8704764834838706752,
                                        'source_pixel_width': -1546699271521570565,
                                        'source_pixel_height': -7292692605725468365,
                                        'rotation': -8897605701069843151,
                                        'virtual_nw_x_pixel': 877420344,
                                        'virtual_nw_y_pixel': 178872192,
                                        'virtual_width': -73488659,
                                        'virtual_height': -1542930943,
                                    },
                            {
                                        'source_monitor': 213913,
                                        'source_nw_x_pixel': -5364166151262119891,
                                        'source_nw_y_pixel': -3735723467117609402,
                                        'source_pixel_width': -1069871980912423775,
                                        'source_pixel_height': -8701237631843427985,
                                        'rotation': -7444541354340712513,
                                        'virtual_nw_x_pixel': -1273966789,
                                        'virtual_nw_y_pixel': 1894900999,
                                        'virtual_width': 1287050956,
                                        'virtual_height': 289640750,
                                    },
                            {
                                        'source_monitor': 4950341,
                                        'source_nw_x_pixel': -6105238526093958374,
                                        'source_nw_y_pixel': -7984829845146621827,
                                        'source_pixel_width': -9125152012973029648,
                                        'source_pixel_height': -2891184968682426647,
                                        'rotation': -4251151070283353971,
                                        'virtual_nw_x_pixel': 1128723119,
                                        'virtual_nw_y_pixel': 1585534236,
                                        'virtual_width': -759400695,
                                        'virtual_height': 1533547292,
                                    },
                            {
                                        'source_monitor': 4108483,
                                        'source_nw_x_pixel': -367139547670677241,
                                        'source_nw_y_pixel': -2952310243683144007,
                                        'source_pixel_width': -1118984543351234,
                                        'source_pixel_height': -3184410071581450356,
                                        'rotation': -6190219916290948583,
                                        'virtual_nw_x_pixel': 1428482197,
                                        'virtual_nw_y_pixel': -206982500,
                                        'virtual_width': 1219684769,
                                        'virtual_height': -81618991,
                                    },
                            {
                                        'source_monitor': -959385,
                                        'source_nw_x_pixel': -4568065416092885919,
                                        'source_nw_y_pixel': -2248828445402242890,
                                        'source_pixel_width': -8812241379007062406,
                                        'source_pixel_height': -4332825862541425568,
                                        'rotation': -2316108821300768026,
                                        'virtual_nw_x_pixel': 1324102577,
                                        'virtual_nw_y_pixel': 676121549,
                                        'virtual_width': 1299519853,
                                        'virtual_height': 613169127,
                                    },
                            {
                                        'source_monitor': 3634217,
                                        'source_nw_x_pixel': -5406893540541890528,
                                        'source_nw_y_pixel': -1309976556210217672,
                                        'source_pixel_width': -8991758037765390324,
                                        'source_pixel_height': -4367580202234409332,
                                        'rotation': -4998278853005755121,
                                        'virtual_nw_x_pixel': 1301448691,
                                        'virtual_nw_y_pixel': 1303926874,
                                        'virtual_width': -778981327,
                                        'virtual_height': -1995985830,
                                    },
                            {
                                        'source_monitor': 8591968,
                                        'source_nw_x_pixel': -3221076042079978042,
                                        'source_nw_y_pixel': -3781100370293591987,
                                        'source_pixel_width': -6814608520760400278,
                                        'source_pixel_height': -1859106702819207202,
                                        'rotation': -3562109218536243840,
                                        'virtual_nw_x_pixel': 56361584,
                                        'virtual_nw_y_pixel': 1170863512,
                                        'virtual_width': 1709318648,
                                        'virtual_height': 1167100721,
                                    },
                            {
                                        'source_monitor': 1814677,
                                        'source_nw_x_pixel': -7239395862694256587,
                                        'source_nw_y_pixel': -3527757325383226505,
                                        'source_pixel_width': -8256082032506983563,
                                        'source_pixel_height': -5723686051768139615,
                                        'rotation': -7004725074836689580,
                                        'virtual_nw_x_pixel': -1086612167,
                                        'virtual_nw_y_pixel': -816423689,
                                        'virtual_width': 440729438,
                                        'virtual_height': 770484285,
                                    },
                        ],
                },
                {
                    'description': 'СƎύMʫĐȬʖʑϑZˈԊ\x95ϋ΄ƇØӪçЭ)ӪƸȃǗѭ\x8aɗ!',
                    'monitors': [
                            {
                                        'identifier': 4062787,
                                        'width': 8718470912661000982,
                                        'height': -4321431545080342643,
                                    },
                            {
                                        'identifier': 1151939,
                                        'width': -2462705604251172402,
                                        'height': -5210340439631768043,
                                    },
                            {
                                        'identifier': 6396807,
                                        'width': -3768926603565822779,
                                        'height': -1012580727722871254,
                                    },
                            {
                                        'identifier': 5651390,
                                        'width': 6499492804002115508,
                                        'height': -134107308139814079,
                                    },
                            {
                                        'identifier': 3386422,
                                        'width': 703162799163088040,
                                        'height': -5614184007176655284,
                                    },
                            {
                                        'identifier': 6725289,
                                        'width': -7662789987662712537,
                                        'height': 5221673363918313774,
                                    },
                            {
                                        'identifier': 3554469,
                                        'width': 7392453769990847616,
                                        'height': 7250499407318597988,
                                    },
                            {
                                        'identifier': 1103028,
                                        'width': -598962077746786793,
                                        'height': -1754739774097483189,
                                    },
                            {
                                        'identifier': 8190635,
                                        'width': 3832144604237836231,
                                        'height': 5447931547445678385,
                                    },
                            {
                                        'identifier': 5169359,
                                        'width': 437702768837977011,
                                        'height': -1592797248796881125,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -398301,
                                        'source_nw_x_pixel': -9133147769770464062,
                                        'source_nw_y_pixel': -123601268693564570,
                                        'source_pixel_width': -6043183101721426839,
                                        'source_pixel_height': -6909787106921648903,
                                        'rotation': -3342885571848400424,
                                        'virtual_nw_x_pixel': 1728352923,
                                        'virtual_nw_y_pixel': -1011737412,
                                        'virtual_width': -3321715,
                                        'virtual_height': -1666898238,
                                    },
                            {
                                        'source_monitor': 9480571,
                                        'source_nw_x_pixel': -1892456520219686841,
                                        'source_nw_y_pixel': -7369337990071415987,
                                        'source_pixel_width': -2214838047592088137,
                                        'source_pixel_height': -4417242569422699219,
                                        'rotation': -3976485230319194974,
                                        'virtual_nw_x_pixel': -1074972885,
                                        'virtual_nw_y_pixel': -1765121136,
                                        'virtual_width': -1333878890,
                                        'virtual_height': -195735661,
                                    },
                            {
                                        'source_monitor': 6372908,
                                        'source_nw_x_pixel': -4439030461061437525,
                                        'source_nw_y_pixel': -8360324851750397906,
                                        'source_pixel_width': -476693526580347669,
                                        'source_pixel_height': -1734094272844437034,
                                        'rotation': -5096881499482444744,
                                        'virtual_nw_x_pixel': -945757303,
                                        'virtual_nw_y_pixel': 1376797869,
                                        'virtual_width': 1291191139,
                                        'virtual_height': 1023426165,
                                    },
                            {
                                        'source_monitor': 1390600,
                                        'source_nw_x_pixel': -5249852254189071328,
                                        'source_nw_y_pixel': -6467577729234410755,
                                        'source_pixel_width': -3122448023244127938,
                                        'source_pixel_height': -7195201678858993842,
                                        'rotation': -3843136411719171223,
                                        'virtual_nw_x_pixel': 443617260,
                                        'virtual_nw_y_pixel': -1561838573,
                                        'virtual_width': 790298607,
                                        'virtual_height': -1823865092,
                                    },
                            {
                                        'source_monitor': -656891,
                                        'source_nw_x_pixel': -8579782724200137943,
                                        'source_nw_y_pixel': -2168562547151625071,
                                        'source_pixel_width': -1635076644878818424,
                                        'source_pixel_height': -1521098721207354522,
                                        'rotation': -8225167362420952481,
                                        'virtual_nw_x_pixel': -1285476480,
                                        'virtual_nw_y_pixel': 262272069,
                                        'virtual_width': -124398178,
                                        'virtual_height': 1862834036,
                                    },
                            {
                                        'source_monitor': 7801285,
                                        'source_nw_x_pixel': -1048304858663896555,
                                        'source_nw_y_pixel': -5487673264569673011,
                                        'source_pixel_width': -4517582806176960786,
                                        'source_pixel_height': -7016599499506216413,
                                        'rotation': -7108991097785771736,
                                        'virtual_nw_x_pixel': 73823352,
                                        'virtual_nw_y_pixel': 1310659175,
                                        'virtual_width': -59993883,
                                        'virtual_height': -287323816,
                                    },
                            {
                                        'source_monitor': 9695368,
                                        'source_nw_x_pixel': -1908009327242151987,
                                        'source_nw_y_pixel': -7738408502340293617,
                                        'source_pixel_width': -315603042842833992,
                                        'source_pixel_height': -620659743542216633,
                                        'rotation': -8542573711553698730,
                                        'virtual_nw_x_pixel': -993765829,
                                        'virtual_nw_y_pixel': -1686069612,
                                        'virtual_width': 281583954,
                                        'virtual_height': 768702340,
                                    },
                            {
                                        'source_monitor': 8835571,
                                        'source_nw_x_pixel': -8582752697839687065,
                                        'source_nw_y_pixel': -6458988694482455066,
                                        'source_pixel_width': -5941091587337178224,
                                        'source_pixel_height': -9175063961654031153,
                                        'rotation': -1458468385524577074,
                                        'virtual_nw_x_pixel': 1018446674,
                                        'virtual_nw_y_pixel': -672682593,
                                        'virtual_width': -962916469,
                                        'virtual_height': -620805383,
                                    },
                            {
                                        'source_monitor': 3534696,
                                        'source_nw_x_pixel': -5351372621806884242,
                                        'source_nw_y_pixel': -4736060142542459127,
                                        'source_pixel_width': -7552831323633596175,
                                        'source_pixel_height': -541131864286121341,
                                        'rotation': -2826239395803827156,
                                        'virtual_nw_x_pixel': -1416323630,
                                        'virtual_nw_y_pixel': -1246245478,
                                        'virtual_width': -754181973,
                                        'virtual_height': -1857660490,
                                    },
                            {
                                        'source_monitor': 129173,
                                        'source_nw_x_pixel': -4736494053899368767,
                                        'source_nw_y_pixel': -2044211254742544476,
                                        'source_pixel_width': -1095262285233424919,
                                        'source_pixel_height': -500994667257128834,
                                        'rotation': -4130680084669350275,
                                        'virtual_nw_x_pixel': 1947323546,
                                        'virtual_nw_y_pixel': -1047129489,
                                        'virtual_width': 923600716,
                                        'virtual_height': 264202790,
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
                                        'identifier': 2781222,
                                        'width': 5945597875016110599,
                                        'height': -6484250229024473052,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -4059155631972252338,
                                        'source_nw_y_pixel': -3177639478103822289,
                                        'source_pixel_width': -1224685649736434503,
                                        'source_pixel_height': -8346813006728212201,
                                        'rotation': -3456785386609452353,
                                        'virtual_nw_x_pixel': -1248184748,
                                        'virtual_nw_y_pixel': -1372187341,
                                        'virtual_width': -1637057271,
                                        'virtual_height': 1122923204,
                                    },
                        ],
                },
            ],

        },
    ),
]
