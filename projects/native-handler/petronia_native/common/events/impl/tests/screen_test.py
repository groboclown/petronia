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
            'identifier': 260707,
            'width': -5156798082681216835,
            'height': 6941384639918461411,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': -282900,

            'width': -9015027638505568725,

            'height': 6899284271540124581,

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
            'source_monitor': 3804514,
            'source_nw_x_pixel': -2719206082613105093,
            'source_nw_y_pixel': -6779825793996812142,
            'source_pixel_width': -8380904997913768743,
            'source_pixel_height': -8252545778139319024,
            'rotation': -5629298133906385396,
            'virtual_nw_x_pixel': 1870291270,
            'virtual_nw_y_pixel': -883282109,
            'virtual_width': -503275389,
            'virtual_height': -738514467,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -356422078550466520,

            'source_nw_y_pixel': -3279406049542704726,

            'source_pixel_width': -3484786407132497010,

            'source_pixel_height': -5307729006378535950,

            'rotation': -7059757898262089129,

            'virtual_nw_x_pixel': -738858088,

            'virtual_nw_y_pixel': 1483894021,

            'virtual_width': -1771324288,

            'virtual_height': 385949130,

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
            'description': 'þϽæ!˵Ћϔ4ƁËӀӅΦʱĜ\x99ÚϤ\x87Ѫbˊǫç?ѺДΐŵĚ',
            'monitors': [
                {
                    'identifier': 2892249,
                    'width': 5295077353720567377,
                    'height': -6192403817535546879,
                },
                {
                    'identifier': 3646241,
                    'width': 2374851235496751529,
                    'height': 2327655516498204454,
                },
                {
                    'identifier': 6900110,
                    'width': 1366459874266512259,
                    'height': -6335968658130737823,
                },
                {
                    'identifier': 4907575,
                    'width': 6423903183858056142,
                    'height': -1949636178311922052,
                },
                {
                    'identifier': 5817682,
                    'width': 3894828508472719152,
                    'height': -2136198224165358887,
                },
                {
                    'identifier': 2847029,
                    'width': -7899503075249235197,
                    'height': 8892393736415439633,
                },
                {
                    'identifier': 9672421,
                    'width': -3747835205036955856,
                    'height': 3071150301428973962,
                },
                {
                    'identifier': 6300825,
                    'width': 8353639077739110266,
                    'height': -7659368574791599031,
                },
                {
                    'identifier': 7555109,
                    'width': 1783711559195840693,
                    'height': 5843236670661833595,
                },
                {
                    'identifier': -375054,
                    'width': 2697498262188970101,
                    'height': -1791884905912184071,
                },
            ],
            'screen': [
                {
                    'source_monitor': 7804701,
                    'source_nw_x_pixel': -314124881520040963,
                    'source_nw_y_pixel': -3232811291386317248,
                    'source_pixel_width': -5023720243212347226,
                    'source_pixel_height': -3941692058982655128,
                    'rotation': -4402002031108237330,
                    'virtual_nw_x_pixel': 183999875,
                    'virtual_nw_y_pixel': -1679372697,
                    'virtual_width': 93978656,
                    'virtual_height': 262229443,
                },
                {
                    'source_monitor': 131061,
                    'source_nw_x_pixel': -8465448978892614605,
                    'source_nw_y_pixel': -3413890490048401995,
                    'source_pixel_width': -7852855341320780052,
                    'source_pixel_height': -7784770572289680461,
                    'rotation': -2940014002506444857,
                    'virtual_nw_x_pixel': 1195768947,
                    'virtual_nw_y_pixel': -301942388,
                    'virtual_width': -582484789,
                    'virtual_height': 252574156,
                },
                {
                    'source_monitor': 8761653,
                    'source_nw_x_pixel': -6559503527557231905,
                    'source_nw_y_pixel': -8103118692671790967,
                    'source_pixel_width': -2015819997995446691,
                    'source_pixel_height': -667393862599018661,
                    'rotation': -418521785186153338,
                    'virtual_nw_x_pixel': -93712754,
                    'virtual_nw_y_pixel': 1294474545,
                    'virtual_width': 1499836162,
                    'virtual_height': -475665570,
                },
                {
                    'source_monitor': -3653,
                    'source_nw_x_pixel': -7423712200648867100,
                    'source_nw_y_pixel': -6193832021844035790,
                    'source_pixel_width': -8081323349145115165,
                    'source_pixel_height': -7622468661191717683,
                    'rotation': -1857437700600430993,
                    'virtual_nw_x_pixel': 1330420353,
                    'virtual_nw_y_pixel': 283083951,
                    'virtual_width': -1734894500,
                    'virtual_height': 1602767823,
                },
                {
                    'source_monitor': 2954537,
                    'source_nw_x_pixel': -5217310383145287696,
                    'source_nw_y_pixel': -119834773782286201,
                    'source_pixel_width': -1654982492787038918,
                    'source_pixel_height': -5713649890446014191,
                    'rotation': -873183804243140604,
                    'virtual_nw_x_pixel': 995765415,
                    'virtual_nw_y_pixel': 298763405,
                    'virtual_width': -1409423550,
                    'virtual_height': 990572113,
                },
                {
                    'source_monitor': 2763150,
                    'source_nw_x_pixel': -1654070055074206489,
                    'source_nw_y_pixel': -4868237697919385777,
                    'source_pixel_width': -6267914140591307429,
                    'source_pixel_height': -7196696715934012637,
                    'rotation': -6659517679865924780,
                    'virtual_nw_x_pixel': -933526845,
                    'virtual_nw_y_pixel': 721377232,
                    'virtual_width': 553818860,
                    'virtual_height': 707035760,
                },
                {
                    'source_monitor': 4158747,
                    'source_nw_x_pixel': -3311231393315772601,
                    'source_nw_y_pixel': -3877016579002471307,
                    'source_pixel_width': -5664862064957975031,
                    'source_pixel_height': -1614374808117048470,
                    'rotation': -5206622151512498290,
                    'virtual_nw_x_pixel': 1147576991,
                    'virtual_nw_y_pixel': 1584239399,
                    'virtual_width': 657321465,
                    'virtual_height': 757449833,
                },
                {
                    'source_monitor': 5295335,
                    'source_nw_x_pixel': -4103643665404542479,
                    'source_nw_y_pixel': -6294249956025135251,
                    'source_pixel_width': -8757794512383206979,
                    'source_pixel_height': -7033906771096291906,
                    'rotation': -1727486778593012874,
                    'virtual_nw_x_pixel': 153854600,
                    'virtual_nw_y_pixel': -713366320,
                    'virtual_width': 410720849,
                    'virtual_height': 641876357,
                },
                {
                    'source_monitor': 3721705,
                    'source_nw_x_pixel': -7440385075396559245,
                    'source_nw_y_pixel': -6437906280102767088,
                    'source_pixel_width': -2876703544487833978,
                    'source_pixel_height': -2060935645753100529,
                    'rotation': -7004656536516451196,
                    'virtual_nw_x_pixel': 1481305384,
                    'virtual_nw_y_pixel': 195275155,
                    'virtual_width': 431119418,
                    'virtual_height': 68421588,
                },
                {
                    'source_monitor': 3823570,
                    'source_nw_x_pixel': -2151001141782285457,
                    'source_nw_y_pixel': -6993281813660640428,
                    'source_pixel_width': -4436450357134626739,
                    'source_pixel_height': -5059261712686425860,
                    'rotation': -6831386712510835999,
                    'virtual_nw_x_pixel': -1385665536,
                    'virtual_nw_y_pixel': -681213590,
                    'virtual_width': 187575462,
                    'virtual_height': -563964634,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 1446830,
                    'width': 618040709201896786,
                    'height': -2435681487241705675,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -6064317347762337092,
                    'source_nw_y_pixel': -6436626295917503513,
                    'source_pixel_width': -492524765999501079,
                    'source_pixel_height': -5992188197281514853,
                    'rotation': -3860850641290258104,
                    'virtual_nw_x_pixel': 1310139818,
                    'virtual_nw_y_pixel': -1874207024,
                    'virtual_width': 738422889,
                    'virtual_height': 779226348,
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
            'request_id': 1335289,
            'mapped_screens_by_monitors': [
                {
                    'description': 'ЏΚʦǕ\x87ЇşŘқɉŞvҾŧʎаԩʩƻƀ͵ŤˏӨ˔ʑџƄГț',
                    'monitors': [
                            {
                                        'identifier': 636526,
                                        'width': 1840721852744463280,
                                        'height': 4432606684870008837,
                                    },
                            {
                                        'identifier': -508632,
                                        'width': 5694369308631355465,
                                        'height': -8475485387733497200,
                                    },
                            {
                                        'identifier': 9211968,
                                        'width': 6893704081379169558,
                                        'height': -5149916461544072529,
                                    },
                            {
                                        'identifier': -861290,
                                        'width': -2684026537143652699,
                                        'height': 4087097558404608816,
                                    },
                            {
                                        'identifier': 9662192,
                                        'width': 4411428815634215722,
                                        'height': 2795823328430097510,
                                    },
                            {
                                        'identifier': 790560,
                                        'width': 1166047430577161309,
                                        'height': 7402328985382539787,
                                    },
                            {
                                        'identifier': 7369406,
                                        'width': -4090818132109274812,
                                        'height': 8583304169871905010,
                                    },
                            {
                                        'identifier': 4740719,
                                        'width': 4027988104594228224,
                                        'height': -4883976232721428577,
                                    },
                            {
                                        'identifier': 1371540,
                                        'width': -3915951555930096058,
                                        'height': -236477626551600822,
                                    },
                            {
                                        'identifier': 597934,
                                        'width': 3722098821345711494,
                                        'height': -8952832043621675996,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5092275,
                                        'source_nw_x_pixel': -4547030272393566699,
                                        'source_nw_y_pixel': -5914736594430761565,
                                        'source_pixel_width': -2024728087581400240,
                                        'source_pixel_height': -4153405746973840917,
                                        'rotation': -6623875476914195561,
                                        'virtual_nw_x_pixel': -349705981,
                                        'virtual_nw_y_pixel': 1164239621,
                                        'virtual_width': -447273397,
                                        'virtual_height': 1235864132,
                                    },
                            {
                                        'source_monitor': 5869728,
                                        'source_nw_x_pixel': -934406562359469980,
                                        'source_nw_y_pixel': -1930229314944434273,
                                        'source_pixel_width': -6899639431530378694,
                                        'source_pixel_height': -5255846712960530734,
                                        'rotation': -8416494968793425545,
                                        'virtual_nw_x_pixel': -193180237,
                                        'virtual_nw_y_pixel': 210425827,
                                        'virtual_width': -550379246,
                                        'virtual_height': 415780751,
                                    },
                            {
                                        'source_monitor': 7989610,
                                        'source_nw_x_pixel': -4600682721806579880,
                                        'source_nw_y_pixel': -6174357791655662814,
                                        'source_pixel_width': -6887342874373450074,
                                        'source_pixel_height': -1156092536175161542,
                                        'rotation': -734994025776730289,
                                        'virtual_nw_x_pixel': -364553828,
                                        'virtual_nw_y_pixel': 1847153238,
                                        'virtual_width': 1607192821,
                                        'virtual_height': -1685848290,
                                    },
                            {
                                        'source_monitor': 8026850,
                                        'source_nw_x_pixel': -7584802216928343462,
                                        'source_nw_y_pixel': -2833064689175552681,
                                        'source_pixel_width': -7341962795315500219,
                                        'source_pixel_height': -6704252780891110511,
                                        'rotation': -4563104218892422995,
                                        'virtual_nw_x_pixel': -449062138,
                                        'virtual_nw_y_pixel': 1051147273,
                                        'virtual_width': -833904720,
                                        'virtual_height': -40583359,
                                    },
                            {
                                        'source_monitor': 5823184,
                                        'source_nw_x_pixel': -7656771615263532176,
                                        'source_nw_y_pixel': -6922168193003196362,
                                        'source_pixel_width': -8383377181571427456,
                                        'source_pixel_height': -1151391611184610017,
                                        'rotation': -2599214817071371620,
                                        'virtual_nw_x_pixel': 1202411076,
                                        'virtual_nw_y_pixel': 1838692864,
                                        'virtual_width': -594453838,
                                        'virtual_height': 182559304,
                                    },
                            {
                                        'source_monitor': 9337131,
                                        'source_nw_x_pixel': -6139533982852773574,
                                        'source_nw_y_pixel': -4939234347416817452,
                                        'source_pixel_width': -1737484589528756609,
                                        'source_pixel_height': -5023934130775616806,
                                        'rotation': -8132483279760215557,
                                        'virtual_nw_x_pixel': 356104608,
                                        'virtual_nw_y_pixel': -1589629635,
                                        'virtual_width': 705609833,
                                        'virtual_height': -1192533133,
                                    },
                            {
                                        'source_monitor': -730862,
                                        'source_nw_x_pixel': -2881029896379145213,
                                        'source_nw_y_pixel': -3287791000313873641,
                                        'source_pixel_width': -1800046380489446810,
                                        'source_pixel_height': -7624125031176446466,
                                        'rotation': -8649683803951091962,
                                        'virtual_nw_x_pixel': 10999394,
                                        'virtual_nw_y_pixel': -374553716,
                                        'virtual_width': -870865784,
                                        'virtual_height': 882124583,
                                    },
                            {
                                        'source_monitor': 4325051,
                                        'source_nw_x_pixel': -8231916489277015817,
                                        'source_nw_y_pixel': -7819967969585550171,
                                        'source_pixel_width': -8408311841967863694,
                                        'source_pixel_height': -4560645967972887299,
                                        'rotation': -8207359103795954594,
                                        'virtual_nw_x_pixel': 799588308,
                                        'virtual_nw_y_pixel': -833839347,
                                        'virtual_width': -858411467,
                                        'virtual_height': 1920658021,
                                    },
                            {
                                        'source_monitor': -992398,
                                        'source_nw_x_pixel': -5971426072907545663,
                                        'source_nw_y_pixel': -2638978654876653240,
                                        'source_pixel_width': -6383686556416853246,
                                        'source_pixel_height': -4943182124411317983,
                                        'rotation': -5821524023778325967,
                                        'virtual_nw_x_pixel': -250924396,
                                        'virtual_nw_y_pixel': 569777690,
                                        'virtual_width': -869852099,
                                        'virtual_height': 473787263,
                                    },
                            {
                                        'source_monitor': 2856807,
                                        'source_nw_x_pixel': -7956686512639040980,
                                        'source_nw_y_pixel': -6478813656679545991,
                                        'source_pixel_width': -28738587844148875,
                                        'source_pixel_height': -4953925555608868984,
                                        'rotation': -8712459545450364142,
                                        'virtual_nw_x_pixel': 1719613751,
                                        'virtual_nw_y_pixel': -242666482,
                                        'virtual_width': -919872752,
                                        'virtual_height': 1878543397,
                                    },
                        ],
                },
                {
                    'description': 'źҭϞ½ВƁ˅ԧЄβҲʅŰЧǐƤɰʻ˩ò\x7fɓŕĠВˉ\x95ӦȾѼ',
                    'monitors': [
                            {
                                        'identifier': 7914966,
                                        'width': 8344876929911225253,
                                        'height': 7639942862640166039,
                                    },
                            {
                                        'identifier': 143262,
                                        'width': -3887843680715653107,
                                        'height': 6404825536896602908,
                                    },
                            {
                                        'identifier': -959474,
                                        'width': 4702293762095262776,
                                        'height': -5056472068541950141,
                                    },
                            {
                                        'identifier': 4756264,
                                        'width': -208372583300539800,
                                        'height': 2932742288216224584,
                                    },
                            {
                                        'identifier': 2869043,
                                        'width': -3705437595968969087,
                                        'height': -9184614212637246619,
                                    },
                            {
                                        'identifier': 6385830,
                                        'width': -8179054106349626754,
                                        'height': 4446513278087850964,
                                    },
                            {
                                        'identifier': -872647,
                                        'width': -3466901682635656678,
                                        'height': -691194484064650077,
                                    },
                            {
                                        'identifier': 7265225,
                                        'width': 2412485852592240821,
                                        'height': -5969408157194815959,
                                    },
                            {
                                        'identifier': 589869,
                                        'width': 8875623454013816820,
                                        'height': -3322275976285809836,
                                    },
                            {
                                        'identifier': 2971132,
                                        'width': -6057099939718911182,
                                        'height': -5196882152397279176,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5939416,
                                        'source_nw_x_pixel': -5437516504783853220,
                                        'source_nw_y_pixel': -1673759816728294738,
                                        'source_pixel_width': -1168996109228340254,
                                        'source_pixel_height': -3312171807466669063,
                                        'rotation': -8457989394084101601,
                                        'virtual_nw_x_pixel': 58035360,
                                        'virtual_nw_y_pixel': -706694113,
                                        'virtual_width': 1260095954,
                                        'virtual_height': -102247616,
                                    },
                            {
                                        'source_monitor': 4081468,
                                        'source_nw_x_pixel': -5798554465300760128,
                                        'source_nw_y_pixel': -7841823172332926796,
                                        'source_pixel_width': -3862722298188853402,
                                        'source_pixel_height': -2638740343866266944,
                                        'rotation': -7534968106310643459,
                                        'virtual_nw_x_pixel': -1186414736,
                                        'virtual_nw_y_pixel': 698828482,
                                        'virtual_width': -198734695,
                                        'virtual_height': 417207283,
                                    },
                            {
                                        'source_monitor': 3388043,
                                        'source_nw_x_pixel': -3549073093515633040,
                                        'source_nw_y_pixel': -8273987072901814429,
                                        'source_pixel_width': -175974867855768331,
                                        'source_pixel_height': -9077190285073174220,
                                        'rotation': -3789755479367330551,
                                        'virtual_nw_x_pixel': -1989948116,
                                        'virtual_nw_y_pixel': -1017953624,
                                        'virtual_width': -1718106809,
                                        'virtual_height': 1822245151,
                                    },
                            {
                                        'source_monitor': 5175763,
                                        'source_nw_x_pixel': -1297200294467119115,
                                        'source_nw_y_pixel': -7743416207648393083,
                                        'source_pixel_width': -6329869586134772846,
                                        'source_pixel_height': -5524615771426921268,
                                        'rotation': -6351652873593166095,
                                        'virtual_nw_x_pixel': 405969513,
                                        'virtual_nw_y_pixel': -1068705809,
                                        'virtual_width': 1113656612,
                                        'virtual_height': 531221515,
                                    },
                            {
                                        'source_monitor': 5602226,
                                        'source_nw_x_pixel': -2201904427788979041,
                                        'source_nw_y_pixel': -7428412236454086548,
                                        'source_pixel_width': -2996632653150121635,
                                        'source_pixel_height': -4420552394614478715,
                                        'rotation': -2019428198896652086,
                                        'virtual_nw_x_pixel': 493296277,
                                        'virtual_nw_y_pixel': 1639488066,
                                        'virtual_width': 1817259306,
                                        'virtual_height': 1067361987,
                                    },
                            {
                                        'source_monitor': 2854766,
                                        'source_nw_x_pixel': -2844201865527410033,
                                        'source_nw_y_pixel': -1718674573278418437,
                                        'source_pixel_width': -6472439590423959870,
                                        'source_pixel_height': -3905440489868704564,
                                        'rotation': -3193954329390617858,
                                        'virtual_nw_x_pixel': -924597301,
                                        'virtual_nw_y_pixel': -56045963,
                                        'virtual_width': 640070541,
                                        'virtual_height': 862617547,
                                    },
                            {
                                        'source_monitor': -736873,
                                        'source_nw_x_pixel': -3469925680248948707,
                                        'source_nw_y_pixel': -4643495351295729733,
                                        'source_pixel_width': -1058776997496678669,
                                        'source_pixel_height': -8134496629182337124,
                                        'rotation': -2530671900984083883,
                                        'virtual_nw_x_pixel': 1148966953,
                                        'virtual_nw_y_pixel': 1615674092,
                                        'virtual_width': 1964017010,
                                        'virtual_height': 740709610,
                                    },
                            {
                                        'source_monitor': 4695893,
                                        'source_nw_x_pixel': -3505503313448163824,
                                        'source_nw_y_pixel': -643108401438969649,
                                        'source_pixel_width': -5528231408344526615,
                                        'source_pixel_height': -5351249743900298757,
                                        'rotation': -2991533290664218650,
                                        'virtual_nw_x_pixel': 589385354,
                                        'virtual_nw_y_pixel': -970810476,
                                        'virtual_width': -296957521,
                                        'virtual_height': 1044559583,
                                    },
                            {
                                        'source_monitor': 3252118,
                                        'source_nw_x_pixel': -626330551824859835,
                                        'source_nw_y_pixel': -8333218571833293492,
                                        'source_pixel_width': -5310191817550452693,
                                        'source_pixel_height': -3584546788409196545,
                                        'rotation': -3447016227254484212,
                                        'virtual_nw_x_pixel': 1494707957,
                                        'virtual_nw_y_pixel': -819726263,
                                        'virtual_width': 320809110,
                                        'virtual_height': 47761743,
                                    },
                            {
                                        'source_monitor': 9060829,
                                        'source_nw_x_pixel': -5763187641839810318,
                                        'source_nw_y_pixel': -7409553810482602881,
                                        'source_pixel_width': -2921474972648952471,
                                        'source_pixel_height': -6958065828921128511,
                                        'rotation': -4405804401806993999,
                                        'virtual_nw_x_pixel': -1359814833,
                                        'virtual_nw_y_pixel': 912737055,
                                        'virtual_width': 1064980405,
                                        'virtual_height': -1050831631,
                                    },
                        ],
                },
                {
                    'description': '\x9aÃÝơƀԥ ƹƑ˕ĪԝµΗѯōĹƵõ҅ԛэĦR\x8fϹ\x97ˆkҘ',
                    'monitors': [
                            {
                                        'identifier': 9156640,
                                        'width': 1570110452633622337,
                                        'height': -5484163662980141951,
                                    },
                            {
                                        'identifier': 4430773,
                                        'width': 1518688846049605787,
                                        'height': -2172674020421711851,
                                    },
                            {
                                        'identifier': 1979662,
                                        'width': -3054217116132995343,
                                        'height': 521372372787759214,
                                    },
                            {
                                        'identifier': 4778666,
                                        'width': -4441391567062656323,
                                        'height': -886551913396713754,
                                    },
                            {
                                        'identifier': 1149605,
                                        'width': -5147040789292444094,
                                        'height': 1107939220540770382,
                                    },
                            {
                                        'identifier': 1726593,
                                        'width': 4075573818684064421,
                                        'height': 6189213987258832321,
                                    },
                            {
                                        'identifier': 6651357,
                                        'width': -2014154646003442797,
                                        'height': -3699468976297914645,
                                    },
                            {
                                        'identifier': 3787960,
                                        'width': -9057724600449832456,
                                        'height': -401644094327524845,
                                    },
                            {
                                        'identifier': 5535893,
                                        'width': 3433797464289992539,
                                        'height': -7709705422179153851,
                                    },
                            {
                                        'identifier': 4096753,
                                        'width': 3090081872474770265,
                                        'height': 7019533317566918210,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1122071,
                                        'source_nw_x_pixel': -1231609772975586612,
                                        'source_nw_y_pixel': -5473672439899455798,
                                        'source_pixel_width': -1574673440402657603,
                                        'source_pixel_height': -8576301014257285621,
                                        'rotation': -188494775625877785,
                                        'virtual_nw_x_pixel': -41451932,
                                        'virtual_nw_y_pixel': 730771659,
                                        'virtual_width': -57659920,
                                        'virtual_height': -1695232967,
                                    },
                            {
                                        'source_monitor': -574172,
                                        'source_nw_x_pixel': -8494819419897237926,
                                        'source_nw_y_pixel': -3129543497076998726,
                                        'source_pixel_width': -3293049655552268410,
                                        'source_pixel_height': -1353942319329495868,
                                        'rotation': -6012643552719251429,
                                        'virtual_nw_x_pixel': -9755076,
                                        'virtual_nw_y_pixel': -1139450085,
                                        'virtual_width': 1309812106,
                                        'virtual_height': 1304163356,
                                    },
                            {
                                        'source_monitor': 515008,
                                        'source_nw_x_pixel': -7371799461217187730,
                                        'source_nw_y_pixel': -1282855102023436056,
                                        'source_pixel_width': -7009642480836706422,
                                        'source_pixel_height': -4028853768864603572,
                                        'rotation': -8280846570193735542,
                                        'virtual_nw_x_pixel': 1292138976,
                                        'virtual_nw_y_pixel': 134443082,
                                        'virtual_width': 1130928564,
                                        'virtual_height': 1859048617,
                                    },
                            {
                                        'source_monitor': 3219257,
                                        'source_nw_x_pixel': -3391931909961249864,
                                        'source_nw_y_pixel': -7466573173527077286,
                                        'source_pixel_width': -7447958961314705532,
                                        'source_pixel_height': -7060125310027046027,
                                        'rotation': -3521188782734943337,
                                        'virtual_nw_x_pixel': -1312563889,
                                        'virtual_nw_y_pixel': 34421903,
                                        'virtual_width': -1839194703,
                                        'virtual_height': 1925222471,
                                    },
                            {
                                        'source_monitor': 417984,
                                        'source_nw_x_pixel': -6685552078990404743,
                                        'source_nw_y_pixel': -5347845500845835659,
                                        'source_pixel_width': -3571714424995261196,
                                        'source_pixel_height': -8794239913491788603,
                                        'rotation': -96792303609476504,
                                        'virtual_nw_x_pixel': 192445836,
                                        'virtual_nw_y_pixel': 1667745517,
                                        'virtual_width': 845331820,
                                        'virtual_height': 576602375,
                                    },
                            {
                                        'source_monitor': 2232422,
                                        'source_nw_x_pixel': -4693076792601479003,
                                        'source_nw_y_pixel': -267300302267985906,
                                        'source_pixel_width': -4386121120119139357,
                                        'source_pixel_height': -2603308838770023835,
                                        'rotation': -4359277530961599943,
                                        'virtual_nw_x_pixel': 1864470517,
                                        'virtual_nw_y_pixel': 168296566,
                                        'virtual_width': -205001533,
                                        'virtual_height': 1195184775,
                                    },
                            {
                                        'source_monitor': 4391858,
                                        'source_nw_x_pixel': -6943663278981102664,
                                        'source_nw_y_pixel': -869893736282999331,
                                        'source_pixel_width': -2139889700888964919,
                                        'source_pixel_height': -7519127177742616297,
                                        'rotation': -4783274242538326978,
                                        'virtual_nw_x_pixel': -521565566,
                                        'virtual_nw_y_pixel': 148807107,
                                        'virtual_width': 471810704,
                                        'virtual_height': 36044013,
                                    },
                            {
                                        'source_monitor': -980697,
                                        'source_nw_x_pixel': -1583871660860487041,
                                        'source_nw_y_pixel': -5492603005435356078,
                                        'source_pixel_width': -8101178116225994922,
                                        'source_pixel_height': -8711285381623759729,
                                        'rotation': -3008537977382884206,
                                        'virtual_nw_x_pixel': 1264813748,
                                        'virtual_nw_y_pixel': 353672844,
                                        'virtual_width': -5983163,
                                        'virtual_height': 71515519,
                                    },
                            {
                                        'source_monitor': 9132503,
                                        'source_nw_x_pixel': -446520596999456726,
                                        'source_nw_y_pixel': -7455135571521416617,
                                        'source_pixel_width': -9130049042275391060,
                                        'source_pixel_height': -4572568293615086457,
                                        'rotation': -6770333696940885273,
                                        'virtual_nw_x_pixel': -1767563269,
                                        'virtual_nw_y_pixel': 1211224456,
                                        'virtual_width': -1541666754,
                                        'virtual_height': 4608001,
                                    },
                            {
                                        'source_monitor': 5673693,
                                        'source_nw_x_pixel': -5004275460814929744,
                                        'source_nw_y_pixel': -4857329093448860915,
                                        'source_pixel_width': -4357265663456447767,
                                        'source_pixel_height': -6485428680642950113,
                                        'rotation': -6906328727749942570,
                                        'virtual_nw_x_pixel': -1195281500,
                                        'virtual_nw_y_pixel': -1935397162,
                                        'virtual_width': -702707008,
                                        'virtual_height': 832382966,
                                    },
                        ],
                },
                {
                    'description': '\x9dɉʕʯĪѧưʗïʎõq˅˕ԜǭˌLɾʶђIНЂǹӥӺѣɟœ',
                    'monitors': [
                            {
                                        'identifier': 3411385,
                                        'width': 80061211465889453,
                                        'height': -1147368517960521251,
                                    },
                            {
                                        'identifier': 5708667,
                                        'width': 4344724270184523765,
                                        'height': -2794913644218981609,
                                    },
                            {
                                        'identifier': 1265377,
                                        'width': 8997355033993184594,
                                        'height': 1217630107923487054,
                                    },
                            {
                                        'identifier': -679472,
                                        'width': 8735155984764236443,
                                        'height': 6369219979412951685,
                                    },
                            {
                                        'identifier': 6342264,
                                        'width': 2930889388459337331,
                                        'height': 1725133551182046183,
                                    },
                            {
                                        'identifier': 5644098,
                                        'width': 3523781168563253772,
                                        'height': -721359936980720935,
                                    },
                            {
                                        'identifier': 4687532,
                                        'width': -7324257447579923715,
                                        'height': 5860780441482212666,
                                    },
                            {
                                        'identifier': 9602453,
                                        'width': -7047470818319944587,
                                        'height': -2824834928326713248,
                                    },
                            {
                                        'identifier': 6439660,
                                        'width': -5592295173524487826,
                                        'height': 7737641570044443136,
                                    },
                            {
                                        'identifier': 4818502,
                                        'width': 3677281808107752268,
                                        'height': -4297439767103764035,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2510614,
                                        'source_nw_x_pixel': -7217057339046674364,
                                        'source_nw_y_pixel': -3852884955472494674,
                                        'source_pixel_width': -806833200138379279,
                                        'source_pixel_height': -7562100439783882524,
                                        'rotation': -1815211133025552020,
                                        'virtual_nw_x_pixel': 167894038,
                                        'virtual_nw_y_pixel': 428517464,
                                        'virtual_width': -270779504,
                                        'virtual_height': -693570102,
                                    },
                            {
                                        'source_monitor': 4578401,
                                        'source_nw_x_pixel': -8153244184855642366,
                                        'source_nw_y_pixel': -4822728700737357780,
                                        'source_pixel_width': -5842268158933728418,
                                        'source_pixel_height': -5243249010783939306,
                                        'rotation': -3667490323041509172,
                                        'virtual_nw_x_pixel': -1049069532,
                                        'virtual_nw_y_pixel': -88248557,
                                        'virtual_width': -1346684959,
                                        'virtual_height': 916358304,
                                    },
                            {
                                        'source_monitor': 8412735,
                                        'source_nw_x_pixel': -7308781653900551474,
                                        'source_nw_y_pixel': -1743585623883247016,
                                        'source_pixel_width': -781952076758249310,
                                        'source_pixel_height': -2756179816117469407,
                                        'rotation': -510709454386008341,
                                        'virtual_nw_x_pixel': 842237139,
                                        'virtual_nw_y_pixel': -92248390,
                                        'virtual_width': -1730472545,
                                        'virtual_height': -739578182,
                                    },
                            {
                                        'source_monitor': 1645632,
                                        'source_nw_x_pixel': -850879832124836811,
                                        'source_nw_y_pixel': -1205823187748712124,
                                        'source_pixel_width': -7300957913162167649,
                                        'source_pixel_height': -1533066860636857562,
                                        'rotation': -2398048855813406690,
                                        'virtual_nw_x_pixel': -1583405815,
                                        'virtual_nw_y_pixel': 1406103010,
                                        'virtual_width': 719384110,
                                        'virtual_height': 1166886485,
                                    },
                            {
                                        'source_monitor': 3412473,
                                        'source_nw_x_pixel': -7260418368073418621,
                                        'source_nw_y_pixel': -9020247346080170320,
                                        'source_pixel_width': -5219821961058801255,
                                        'source_pixel_height': -4542516551802270906,
                                        'rotation': -7584520594986699849,
                                        'virtual_nw_x_pixel': -1844781175,
                                        'virtual_nw_y_pixel': -439864691,
                                        'virtual_width': 1206692773,
                                        'virtual_height': -1780858201,
                                    },
                            {
                                        'source_monitor': 7749521,
                                        'source_nw_x_pixel': -4423826219759952632,
                                        'source_nw_y_pixel': -7582653256944690704,
                                        'source_pixel_width': -903872254195048151,
                                        'source_pixel_height': -5082843736116187805,
                                        'rotation': -3846687165170117708,
                                        'virtual_nw_x_pixel': 880410667,
                                        'virtual_nw_y_pixel': 74398423,
                                        'virtual_width': -355329956,
                                        'virtual_height': -358078401,
                                    },
                            {
                                        'source_monitor': -97140,
                                        'source_nw_x_pixel': -2706741132772799501,
                                        'source_nw_y_pixel': -8947354409820005690,
                                        'source_pixel_width': -838019320333352682,
                                        'source_pixel_height': -6440316879539517804,
                                        'rotation': -8457761777219193020,
                                        'virtual_nw_x_pixel': 752226530,
                                        'virtual_nw_y_pixel': 1466627346,
                                        'virtual_width': 495065022,
                                        'virtual_height': 523835266,
                                    },
                            {
                                        'source_monitor': 1116946,
                                        'source_nw_x_pixel': -5255002662716763410,
                                        'source_nw_y_pixel': -7288287383705551760,
                                        'source_pixel_width': -2712993649128312706,
                                        'source_pixel_height': -6172139059652034246,
                                        'rotation': -7525050206201337020,
                                        'virtual_nw_x_pixel': 183007529,
                                        'virtual_nw_y_pixel': -1043687151,
                                        'virtual_width': -242804022,
                                        'virtual_height': 324193850,
                                    },
                            {
                                        'source_monitor': 1731029,
                                        'source_nw_x_pixel': -239653561417292751,
                                        'source_nw_y_pixel': -7607278634072993154,
                                        'source_pixel_width': -3969969500350160270,
                                        'source_pixel_height': -1599684758891099571,
                                        'rotation': -6510661920838241275,
                                        'virtual_nw_x_pixel': 622893675,
                                        'virtual_nw_y_pixel': -1201706607,
                                        'virtual_width': 1742404914,
                                        'virtual_height': 968992722,
                                    },
                            {
                                        'source_monitor': 3380150,
                                        'source_nw_x_pixel': -8114656438436992839,
                                        'source_nw_y_pixel': -1543141936449447146,
                                        'source_pixel_width': -7415528316117031217,
                                        'source_pixel_height': -7662219590041407154,
                                        'rotation': -3491879319735467777,
                                        'virtual_nw_x_pixel': -305817913,
                                        'virtual_nw_y_pixel': 704211884,
                                        'virtual_width': 356043816,
                                        'virtual_height': 293859878,
                                    },
                        ],
                },
                {
                    'description': 'ưɏRҐÅϭ,ňЛΟȧΨɎУѸȼϓüǧιȚ˨ЭȻˊӄ˒ȧă\u0379',
                    'monitors': [
                            {
                                        'identifier': 7518312,
                                        'width': 8831599557830018613,
                                        'height': -3518110891111856691,
                                    },
                            {
                                        'identifier': 9120575,
                                        'width': -7893263036305909958,
                                        'height': 2602403007058873090,
                                    },
                            {
                                        'identifier': 1703151,
                                        'width': -8550226995685084631,
                                        'height': -8587057666864596609,
                                    },
                            {
                                        'identifier': 4517239,
                                        'width': -7142373249583372359,
                                        'height': 1762124064615463012,
                                    },
                            {
                                        'identifier': 4040659,
                                        'width': -5570799816678974327,
                                        'height': -3180341007890405539,
                                    },
                            {
                                        'identifier': 9875087,
                                        'width': 1117286880800595893,
                                        'height': 4546651260278856352,
                                    },
                            {
                                        'identifier': -324480,
                                        'width': 2758206704043491309,
                                        'height': -1766822089876358891,
                                    },
                            {
                                        'identifier': 3730223,
                                        'width': -7079142333930563317,
                                        'height': 4606897815291906628,
                                    },
                            {
                                        'identifier': 9077433,
                                        'width': -8942659917188491271,
                                        'height': -7244240990741105156,
                                    },
                            {
                                        'identifier': 3789977,
                                        'width': 2970708673291236188,
                                        'height': -3529914445199673179,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2377271,
                                        'source_nw_x_pixel': -7788081087789936539,
                                        'source_nw_y_pixel': -3710262150826918953,
                                        'source_pixel_width': -6790441259157389558,
                                        'source_pixel_height': -7572841257602782587,
                                        'rotation': -2228381730887161244,
                                        'virtual_nw_x_pixel': 717823499,
                                        'virtual_nw_y_pixel': -1436676433,
                                        'virtual_width': -325218883,
                                        'virtual_height': 1494208888,
                                    },
                            {
                                        'source_monitor': 1637580,
                                        'source_nw_x_pixel': -112157006933795372,
                                        'source_nw_y_pixel': -4673427956379351939,
                                        'source_pixel_width': -3768011792335643621,
                                        'source_pixel_height': -1781488608589041306,
                                        'rotation': -3852824005933243332,
                                        'virtual_nw_x_pixel': 344961578,
                                        'virtual_nw_y_pixel': -1065935036,
                                        'virtual_width': -60489497,
                                        'virtual_height': 750055726,
                                    },
                            {
                                        'source_monitor': 9836185,
                                        'source_nw_x_pixel': -6035683287588059489,
                                        'source_nw_y_pixel': -5053799836619605973,
                                        'source_pixel_width': -4548197023462082375,
                                        'source_pixel_height': -274527636773814729,
                                        'rotation': -2221416329892400880,
                                        'virtual_nw_x_pixel': 1681605588,
                                        'virtual_nw_y_pixel': 850837770,
                                        'virtual_width': -1275983582,
                                        'virtual_height': 1604353183,
                                    },
                            {
                                        'source_monitor': 7368475,
                                        'source_nw_x_pixel': -1778412184659644434,
                                        'source_nw_y_pixel': -4294500648010633179,
                                        'source_pixel_width': -950825068420993812,
                                        'source_pixel_height': -3098760101783790527,
                                        'rotation': -1299246893921502022,
                                        'virtual_nw_x_pixel': -1079526289,
                                        'virtual_nw_y_pixel': -106318800,
                                        'virtual_width': 1852537958,
                                        'virtual_height': 948761869,
                                    },
                            {
                                        'source_monitor': 5174541,
                                        'source_nw_x_pixel': -8974245916793789018,
                                        'source_nw_y_pixel': -2605532436488704787,
                                        'source_pixel_width': -6628343350978064121,
                                        'source_pixel_height': -6092471069313203393,
                                        'rotation': -1200343726351350466,
                                        'virtual_nw_x_pixel': 1640586544,
                                        'virtual_nw_y_pixel': 1338971289,
                                        'virtual_width': 508609850,
                                        'virtual_height': -521815141,
                                    },
                            {
                                        'source_monitor': 6226099,
                                        'source_nw_x_pixel': -4391095962825984269,
                                        'source_nw_y_pixel': -6626353068843799839,
                                        'source_pixel_width': -4549151167347413295,
                                        'source_pixel_height': -7204780341723041987,
                                        'rotation': -4395110893450642240,
                                        'virtual_nw_x_pixel': -1641400707,
                                        'virtual_nw_y_pixel': -1713691682,
                                        'virtual_width': -793978108,
                                        'virtual_height': -1829810571,
                                    },
                            {
                                        'source_monitor': 4495212,
                                        'source_nw_x_pixel': -6022403765253926734,
                                        'source_nw_y_pixel': -8344231480019349363,
                                        'source_pixel_width': -4283507880283558735,
                                        'source_pixel_height': -6184028276626634138,
                                        'rotation': -2342618482008468521,
                                        'virtual_nw_x_pixel': -1895808378,
                                        'virtual_nw_y_pixel': 975037699,
                                        'virtual_width': -2402171,
                                        'virtual_height': -200306086,
                                    },
                            {
                                        'source_monitor': 3531764,
                                        'source_nw_x_pixel': -5102269040423541103,
                                        'source_nw_y_pixel': -4522491110435096417,
                                        'source_pixel_width': -363359973678043665,
                                        'source_pixel_height': -7254339986736044004,
                                        'rotation': -2086234410973705277,
                                        'virtual_nw_x_pixel': -1948573737,
                                        'virtual_nw_y_pixel': -1315769955,
                                        'virtual_width': 245966845,
                                        'virtual_height': 1031217574,
                                    },
                            {
                                        'source_monitor': 2858324,
                                        'source_nw_x_pixel': -4247186182939370159,
                                        'source_nw_y_pixel': -4069615808896352885,
                                        'source_pixel_width': -6278132441823704227,
                                        'source_pixel_height': -2686443198706452614,
                                        'rotation': -7013063814954371760,
                                        'virtual_nw_x_pixel': -455193720,
                                        'virtual_nw_y_pixel': 1287157632,
                                        'virtual_width': -1637105036,
                                        'virtual_height': 205154087,
                                    },
                            {
                                        'source_monitor': 8535824,
                                        'source_nw_x_pixel': -5316928928394363892,
                                        'source_nw_y_pixel': -2700221993034416006,
                                        'source_pixel_width': -6615468489153683555,
                                        'source_pixel_height': -8650955097727185478,
                                        'rotation': -5274928445167526986,
                                        'virtual_nw_x_pixel': 387252129,
                                        'virtual_nw_y_pixel': 419848834,
                                        'virtual_width': -127704951,
                                        'virtual_height': -1024374215,
                                    },
                        ],
                },
                {
                    'description': 'ԭӸ҅ʾϡʟȅʻӅӔfԏ˘җъԜÅʩȡϯĄˋĨqɸҵŜɫӁѥ',
                    'monitors': [
                            {
                                        'identifier': 5709012,
                                        'width': 2542786497837804195,
                                        'height': -2126232177837838652,
                                    },
                            {
                                        'identifier': 2320440,
                                        'width': -442088425675511837,
                                        'height': 1740786248742600774,
                                    },
                            {
                                        'identifier': 7969601,
                                        'width': -1904898064844101325,
                                        'height': 5283370771078027910,
                                    },
                            {
                                        'identifier': -923087,
                                        'width': 8076524568079763813,
                                        'height': 8025181271974512550,
                                    },
                            {
                                        'identifier': 9991739,
                                        'width': 3310262669508856187,
                                        'height': 8965572149592984614,
                                    },
                            {
                                        'identifier': 6572301,
                                        'width': 5170656101136461406,
                                        'height': -6583558173583758981,
                                    },
                            {
                                        'identifier': 9934134,
                                        'width': 4366202334445507690,
                                        'height': 8639001428928736012,
                                    },
                            {
                                        'identifier': 5449566,
                                        'width': 8074853878144265929,
                                        'height': 6273051735680958624,
                                    },
                            {
                                        'identifier': -351352,
                                        'width': 3745874058761733054,
                                        'height': -8262898635477361086,
                                    },
                            {
                                        'identifier': 4011539,
                                        'width': -6721115710817351752,
                                        'height': -675872406333674129,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1464980,
                                        'source_nw_x_pixel': -8604857846475382738,
                                        'source_nw_y_pixel': -2705336316958946784,
                                        'source_pixel_width': -5949783895362266133,
                                        'source_pixel_height': -4462718682286247851,
                                        'rotation': -3851192609320922360,
                                        'virtual_nw_x_pixel': -484919460,
                                        'virtual_nw_y_pixel': 118298943,
                                        'virtual_width': 536563631,
                                        'virtual_height': -1786590808,
                                    },
                            {
                                        'source_monitor': 4957032,
                                        'source_nw_x_pixel': -5575402184935969779,
                                        'source_nw_y_pixel': -5068898323634442936,
                                        'source_pixel_width': -5162063652460385756,
                                        'source_pixel_height': -3796355311949443123,
                                        'rotation': -4207662498657371005,
                                        'virtual_nw_x_pixel': -1306091066,
                                        'virtual_nw_y_pixel': 469661588,
                                        'virtual_width': 1198007965,
                                        'virtual_height': 739481506,
                                    },
                            {
                                        'source_monitor': 8801529,
                                        'source_nw_x_pixel': -2801505343234143335,
                                        'source_nw_y_pixel': -7410932145084249414,
                                        'source_pixel_width': -3878159912470274908,
                                        'source_pixel_height': -6963838282385922039,
                                        'rotation': -4615882153190317117,
                                        'virtual_nw_x_pixel': 1331370342,
                                        'virtual_nw_y_pixel': -753877214,
                                        'virtual_width': -783718264,
                                        'virtual_height': -969844298,
                                    },
                            {
                                        'source_monitor': 9665337,
                                        'source_nw_x_pixel': -6746328604905998414,
                                        'source_nw_y_pixel': -7767420839752878296,
                                        'source_pixel_width': -670624961909193038,
                                        'source_pixel_height': -7903788634998645279,
                                        'rotation': -9097741208275063563,
                                        'virtual_nw_x_pixel': 1546570442,
                                        'virtual_nw_y_pixel': -1108890588,
                                        'virtual_width': 1449797813,
                                        'virtual_height': -1524330752,
                                    },
                            {
                                        'source_monitor': 4800597,
                                        'source_nw_x_pixel': -4689403523585601527,
                                        'source_nw_y_pixel': -8030531431560442541,
                                        'source_pixel_width': -1273005849177610685,
                                        'source_pixel_height': -2123736916359801339,
                                        'rotation': -899547452584604059,
                                        'virtual_nw_x_pixel': -444591809,
                                        'virtual_nw_y_pixel': -1565335813,
                                        'virtual_width': 1938141554,
                                        'virtual_height': -1620954111,
                                    },
                            {
                                        'source_monitor': 90305,
                                        'source_nw_x_pixel': -8353122839923434778,
                                        'source_nw_y_pixel': -8142727705210351480,
                                        'source_pixel_width': -2911777421757001404,
                                        'source_pixel_height': -986071597801956985,
                                        'rotation': -2909306850001657366,
                                        'virtual_nw_x_pixel': 1172491685,
                                        'virtual_nw_y_pixel': -379433765,
                                        'virtual_width': 1798020419,
                                        'virtual_height': 1606091957,
                                    },
                            {
                                        'source_monitor': -250242,
                                        'source_nw_x_pixel': -4238288044388632000,
                                        'source_nw_y_pixel': -8914748209057453773,
                                        'source_pixel_width': -2814646375943530050,
                                        'source_pixel_height': -5742108118018067264,
                                        'rotation': -2085191449539958167,
                                        'virtual_nw_x_pixel': 179242498,
                                        'virtual_nw_y_pixel': -1519826066,
                                        'virtual_width': -1200155104,
                                        'virtual_height': 1804148955,
                                    },
                            {
                                        'source_monitor': 8566563,
                                        'source_nw_x_pixel': -8644410442935666062,
                                        'source_nw_y_pixel': -4602302367504722508,
                                        'source_pixel_width': -4110325768877445906,
                                        'source_pixel_height': -4025786198302000963,
                                        'rotation': -6802460821023749217,
                                        'virtual_nw_x_pixel': -834158520,
                                        'virtual_nw_y_pixel': -1883427541,
                                        'virtual_width': 63336249,
                                        'virtual_height': 1097189409,
                                    },
                            {
                                        'source_monitor': 9984849,
                                        'source_nw_x_pixel': -593388088692695805,
                                        'source_nw_y_pixel': -2642628404292164158,
                                        'source_pixel_width': -2541506492519350061,
                                        'source_pixel_height': -6658328454768146320,
                                        'rotation': -4879704177116174279,
                                        'virtual_nw_x_pixel': -680349092,
                                        'virtual_nw_y_pixel': -1681458295,
                                        'virtual_width': -144514235,
                                        'virtual_height': 1189546361,
                                    },
                            {
                                        'source_monitor': 6774588,
                                        'source_nw_x_pixel': -5651242450391346656,
                                        'source_nw_y_pixel': -3512839340928004604,
                                        'source_pixel_width': -8007490061179920228,
                                        'source_pixel_height': -4359564679849614826,
                                        'rotation': -5325281579466324815,
                                        'virtual_nw_x_pixel': -944760708,
                                        'virtual_nw_y_pixel': -833077301,
                                        'virtual_width': 283929751,
                                        'virtual_height': -1098103491,
                                    },
                        ],
                },
                {
                    'description': '\x83ŀƋǟυÐҘ°ʆă¿!Ȝȼΰʗ6ҴɪøɐνřōîԎчψƂǞ',
                    'monitors': [
                            {
                                        'identifier': 9432930,
                                        'width': 4907735694122303199,
                                        'height': 4429452839783718246,
                                    },
                            {
                                        'identifier': 681561,
                                        'width': -6636448475431192384,
                                        'height': 1772651436775348900,
                                    },
                            {
                                        'identifier': 4772486,
                                        'width': -3869007727975218329,
                                        'height': 750394629181560745,
                                    },
                            {
                                        'identifier': 5157657,
                                        'width': 2715726758659294557,
                                        'height': -7721928245823156755,
                                    },
                            {
                                        'identifier': 9345396,
                                        'width': 7066726979115821349,
                                        'height': -5571860894199722492,
                                    },
                            {
                                        'identifier': 2797734,
                                        'width': -3442491640806019353,
                                        'height': -904111576262079301,
                                    },
                            {
                                        'identifier': 8863711,
                                        'width': 8192256040442656151,
                                        'height': -7720767073127958116,
                                    },
                            {
                                        'identifier': 4923139,
                                        'width': 748282495088774674,
                                        'height': 6441664993697188766,
                                    },
                            {
                                        'identifier': 5441988,
                                        'width': -4202070429022096117,
                                        'height': 8262245607546451677,
                                    },
                            {
                                        'identifier': 1436449,
                                        'width': -1641694963288233941,
                                        'height': -8490246268739865906,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -824953,
                                        'source_nw_x_pixel': -2443635989507722806,
                                        'source_nw_y_pixel': -5076827620914716941,
                                        'source_pixel_width': -6401806100004746721,
                                        'source_pixel_height': -2590490486088470241,
                                        'rotation': -636133871107227181,
                                        'virtual_nw_x_pixel': -1560267972,
                                        'virtual_nw_y_pixel': 667499664,
                                        'virtual_width': -1031715657,
                                        'virtual_height': 1102012467,
                                    },
                            {
                                        'source_monitor': 3473371,
                                        'source_nw_x_pixel': -5906581766073604693,
                                        'source_nw_y_pixel': -4840543277365492672,
                                        'source_pixel_width': -4578940773556949091,
                                        'source_pixel_height': -1546148920364603672,
                                        'rotation': -2360733178304948060,
                                        'virtual_nw_x_pixel': -717522890,
                                        'virtual_nw_y_pixel': 1039205236,
                                        'virtual_width': -74426191,
                                        'virtual_height': -234102137,
                                    },
                            {
                                        'source_monitor': 3325393,
                                        'source_nw_x_pixel': -3821109659841563585,
                                        'source_nw_y_pixel': -5845789798793337591,
                                        'source_pixel_width': -4798610326458119123,
                                        'source_pixel_height': -605406859950805177,
                                        'rotation': -556018220326842127,
                                        'virtual_nw_x_pixel': -199592885,
                                        'virtual_nw_y_pixel': -65053456,
                                        'virtual_width': 1358733036,
                                        'virtual_height': 178211350,
                                    },
                            {
                                        'source_monitor': 1865164,
                                        'source_nw_x_pixel': -1993522592342120116,
                                        'source_nw_y_pixel': -7527044412158383468,
                                        'source_pixel_width': -4871590029966792831,
                                        'source_pixel_height': -566422055074224773,
                                        'rotation': -2333305564931121827,
                                        'virtual_nw_x_pixel': -1135868786,
                                        'virtual_nw_y_pixel': -1334419294,
                                        'virtual_width': 1013868341,
                                        'virtual_height': -1767730307,
                                    },
                            {
                                        'source_monitor': 7862753,
                                        'source_nw_x_pixel': -8493099331038224809,
                                        'source_nw_y_pixel': -7248848089452009463,
                                        'source_pixel_width': -6922322906671639525,
                                        'source_pixel_height': -1927694883373233105,
                                        'rotation': -6413064186795675345,
                                        'virtual_nw_x_pixel': 712569396,
                                        'virtual_nw_y_pixel': -1355499239,
                                        'virtual_width': -1615568025,
                                        'virtual_height': -1991166427,
                                    },
                            {
                                        'source_monitor': 5815951,
                                        'source_nw_x_pixel': -8338369151471754238,
                                        'source_nw_y_pixel': -5411539155375619757,
                                        'source_pixel_width': -149445358032497448,
                                        'source_pixel_height': -115389631823234059,
                                        'rotation': -1719066543868166798,
                                        'virtual_nw_x_pixel': -682455591,
                                        'virtual_nw_y_pixel': 735726901,
                                        'virtual_width': 1337082279,
                                        'virtual_height': 1460592614,
                                    },
                            {
                                        'source_monitor': -521291,
                                        'source_nw_x_pixel': -1662264869006883694,
                                        'source_nw_y_pixel': -1793597015631027376,
                                        'source_pixel_width': -6963012395336746131,
                                        'source_pixel_height': -3525304667227237420,
                                        'rotation': -5527513749095151133,
                                        'virtual_nw_x_pixel': 434758887,
                                        'virtual_nw_y_pixel': 837147478,
                                        'virtual_width': -1191289722,
                                        'virtual_height': -1655045344,
                                    },
                            {
                                        'source_monitor': 4372196,
                                        'source_nw_x_pixel': -2313208513995682997,
                                        'source_nw_y_pixel': -1540745129750351100,
                                        'source_pixel_width': -6763398417017039436,
                                        'source_pixel_height': -1485540418558378769,
                                        'rotation': -3376573580944017599,
                                        'virtual_nw_x_pixel': -255597192,
                                        'virtual_nw_y_pixel': -1895307216,
                                        'virtual_width': -516247137,
                                        'virtual_height': -1348143312,
                                    },
                            {
                                        'source_monitor': 5231492,
                                        'source_nw_x_pixel': -2793007393198113750,
                                        'source_nw_y_pixel': -6271425300835137845,
                                        'source_pixel_width': -6938377056930455151,
                                        'source_pixel_height': -7899508659298969207,
                                        'rotation': -8329139419076958048,
                                        'virtual_nw_x_pixel': 1424073244,
                                        'virtual_nw_y_pixel': 1655854786,
                                        'virtual_width': -1687580521,
                                        'virtual_height': -59573276,
                                    },
                            {
                                        'source_monitor': -803852,
                                        'source_nw_x_pixel': -1956758320701658567,
                                        'source_nw_y_pixel': -6839637526002491230,
                                        'source_pixel_width': -3069385919599432475,
                                        'source_pixel_height': -4446534233248243108,
                                        'rotation': -2052691714313212957,
                                        'virtual_nw_x_pixel': 955243211,
                                        'virtual_nw_y_pixel': -1016135016,
                                        'virtual_width': 1327481679,
                                        'virtual_height': 1027745377,
                                    },
                        ],
                },
                {
                    'description': 'ӏЊҺӥǆЀцΉԤ\u0379ǵϠ҅ПѨǷʞȘĲğҶǟ˲ǿĊ³ëƀǎë',
                    'monitors': [
                            {
                                        'identifier': 9370791,
                                        'width': -9010550208541731233,
                                        'height': -8505016967268353749,
                                    },
                            {
                                        'identifier': 7509078,
                                        'width': 8249492654475764683,
                                        'height': 4719144600149442848,
                                    },
                            {
                                        'identifier': -77842,
                                        'width': 8449479372737907669,
                                        'height': 887766190334323675,
                                    },
                            {
                                        'identifier': 4150311,
                                        'width': 2994920702902892558,
                                        'height': 3022525881269649018,
                                    },
                            {
                                        'identifier': 2969893,
                                        'width': 3969552857562930602,
                                        'height': 672472549797196910,
                                    },
                            {
                                        'identifier': -824955,
                                        'width': 1299695580455325802,
                                        'height': 7538311251597162496,
                                    },
                            {
                                        'identifier': -367179,
                                        'width': -773954414679364194,
                                        'height': 9217631862540312380,
                                    },
                            {
                                        'identifier': 9189262,
                                        'width': 3048192936362004979,
                                        'height': -7154364079301347657,
                                    },
                            {
                                        'identifier': 7298751,
                                        'width': 7023963107241348462,
                                        'height': -4661957083272728072,
                                    },
                            {
                                        'identifier': 9304146,
                                        'width': 9083977459054203351,
                                        'height': -976922499691386798,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4055584,
                                        'source_nw_x_pixel': -3097312593699757886,
                                        'source_nw_y_pixel': -5774270915130823106,
                                        'source_pixel_width': -8060370976012606211,
                                        'source_pixel_height': -8743058820450007390,
                                        'rotation': -6109550608687264267,
                                        'virtual_nw_x_pixel': 1947224264,
                                        'virtual_nw_y_pixel': 189545837,
                                        'virtual_width': 956836951,
                                        'virtual_height': 696764047,
                                    },
                            {
                                        'source_monitor': 2501697,
                                        'source_nw_x_pixel': -5529503058384890477,
                                        'source_nw_y_pixel': -6691903534581451771,
                                        'source_pixel_width': -2897704411878483984,
                                        'source_pixel_height': -2311963237594452424,
                                        'rotation': -5051765465800038729,
                                        'virtual_nw_x_pixel': -1196384399,
                                        'virtual_nw_y_pixel': 375803895,
                                        'virtual_width': 1377443310,
                                        'virtual_height': -675555254,
                                    },
                            {
                                        'source_monitor': 6490291,
                                        'source_nw_x_pixel': -1717627958281197487,
                                        'source_nw_y_pixel': -2981967588896459076,
                                        'source_pixel_width': -7768373906673899554,
                                        'source_pixel_height': -5798937872238045320,
                                        'rotation': -1608324617520302319,
                                        'virtual_nw_x_pixel': -1938612925,
                                        'virtual_nw_y_pixel': -1947845515,
                                        'virtual_width': -171413271,
                                        'virtual_height': 989977525,
                                    },
                            {
                                        'source_monitor': 9180999,
                                        'source_nw_x_pixel': -7504031951845979610,
                                        'source_nw_y_pixel': -2209024618816173502,
                                        'source_pixel_width': -8997577574783557711,
                                        'source_pixel_height': -5178218675089474195,
                                        'rotation': -3839807791375750575,
                                        'virtual_nw_x_pixel': 1105233406,
                                        'virtual_nw_y_pixel': -362541903,
                                        'virtual_width': -932749943,
                                        'virtual_height': 1239830012,
                                    },
                            {
                                        'source_monitor': 559395,
                                        'source_nw_x_pixel': -5467265871646601609,
                                        'source_nw_y_pixel': -2355049984234923594,
                                        'source_pixel_width': -3644011494414440603,
                                        'source_pixel_height': -7748322667905139396,
                                        'rotation': -6189008706630604436,
                                        'virtual_nw_x_pixel': -883672724,
                                        'virtual_nw_y_pixel': 247927485,
                                        'virtual_width': 1616699135,
                                        'virtual_height': 936493495,
                                    },
                            {
                                        'source_monitor': 7145235,
                                        'source_nw_x_pixel': -7476824814792854067,
                                        'source_nw_y_pixel': -8822124476079187668,
                                        'source_pixel_width': -7997494193939594766,
                                        'source_pixel_height': -8748871951775600000,
                                        'rotation': -4669898578796708258,
                                        'virtual_nw_x_pixel': 1613132444,
                                        'virtual_nw_y_pixel': -1995478871,
                                        'virtual_width': 284222787,
                                        'virtual_height': -913650392,
                                    },
                            {
                                        'source_monitor': 7117090,
                                        'source_nw_x_pixel': -8735439584731904566,
                                        'source_nw_y_pixel': -2179462271222629921,
                                        'source_pixel_width': -9027499896128204883,
                                        'source_pixel_height': -617357069452334239,
                                        'rotation': -2252476994733482172,
                                        'virtual_nw_x_pixel': 317895710,
                                        'virtual_nw_y_pixel': 1797821320,
                                        'virtual_width': -715835402,
                                        'virtual_height': -1684578799,
                                    },
                            {
                                        'source_monitor': 8690691,
                                        'source_nw_x_pixel': -591675432894210915,
                                        'source_nw_y_pixel': -6684088329607530161,
                                        'source_pixel_width': -569775249835016697,
                                        'source_pixel_height': -5695779460047114579,
                                        'rotation': -9210956920643532348,
                                        'virtual_nw_x_pixel': -754755501,
                                        'virtual_nw_y_pixel': 965715929,
                                        'virtual_width': -729682217,
                                        'virtual_height': 275279168,
                                    },
                            {
                                        'source_monitor': 4048770,
                                        'source_nw_x_pixel': -5146853238480789548,
                                        'source_nw_y_pixel': -2020568695501455344,
                                        'source_pixel_width': -6969479582864981739,
                                        'source_pixel_height': -6993037408251768353,
                                        'rotation': -5989187536357546302,
                                        'virtual_nw_x_pixel': 101383098,
                                        'virtual_nw_y_pixel': -838803667,
                                        'virtual_width': 1942224565,
                                        'virtual_height': 1672808740,
                                    },
                            {
                                        'source_monitor': -496749,
                                        'source_nw_x_pixel': -8570600726009462967,
                                        'source_nw_y_pixel': -8240643283773746666,
                                        'source_pixel_width': -8363294806783510686,
                                        'source_pixel_height': -5606941961194892987,
                                        'rotation': -1306458276139793203,
                                        'virtual_nw_x_pixel': 1526886149,
                                        'virtual_nw_y_pixel': -1008745075,
                                        'virtual_width': 546939006,
                                        'virtual_height': 364576185,
                                    },
                        ],
                },
                {
                    'description': '£Ϛ϶Ѧ҉ƉǱǓ\u038bˀŵtŭїƈӍѩüχǮђŠȤñ£4˼A3Ȩ',
                    'monitors': [
                            {
                                        'identifier': 4475753,
                                        'width': 4742640141821175711,
                                        'height': -2086759331873296710,
                                    },
                            {
                                        'identifier': 384892,
                                        'width': -5811293813709054744,
                                        'height': 1227647842762690994,
                                    },
                            {
                                        'identifier': 1186080,
                                        'width': 7821863368407045176,
                                        'height': -8921992419483647922,
                                    },
                            {
                                        'identifier': 8346007,
                                        'width': 4629442113755120248,
                                        'height': 4679900225153520697,
                                    },
                            {
                                        'identifier': 7258541,
                                        'width': 6396855492696746850,
                                        'height': 7362657441029904130,
                                    },
                            {
                                        'identifier': -706303,
                                        'width': 1295202705037768588,
                                        'height': 531388146367848957,
                                    },
                            {
                                        'identifier': -7524,
                                        'width': 140819687396722488,
                                        'height': 7882574453782597657,
                                    },
                            {
                                        'identifier': 2727548,
                                        'width': 4916374361342389575,
                                        'height': 4040605790748073984,
                                    },
                            {
                                        'identifier': 1276582,
                                        'width': -6976584024032649540,
                                        'height': -4647620000877955865,
                                    },
                            {
                                        'identifier': 9214395,
                                        'width': 2238383449843405799,
                                        'height': -70423081374201881,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1242860,
                                        'source_nw_x_pixel': -4416303890987529632,
                                        'source_nw_y_pixel': -4013830299169139671,
                                        'source_pixel_width': -1353352817273745246,
                                        'source_pixel_height': -2674656035739983105,
                                        'rotation': -3826077527147295654,
                                        'virtual_nw_x_pixel': 1031040365,
                                        'virtual_nw_y_pixel': -192441543,
                                        'virtual_width': 822730679,
                                        'virtual_height': -1079220356,
                                    },
                            {
                                        'source_monitor': 3492249,
                                        'source_nw_x_pixel': -876731467302281990,
                                        'source_nw_y_pixel': -933435919883926233,
                                        'source_pixel_width': -8222585918125890945,
                                        'source_pixel_height': -2309824362017796993,
                                        'rotation': -8797993913696991910,
                                        'virtual_nw_x_pixel': -1611873709,
                                        'virtual_nw_y_pixel': -1900301431,
                                        'virtual_width': -1277607618,
                                        'virtual_height': -409341857,
                                    },
                            {
                                        'source_monitor': 3916862,
                                        'source_nw_x_pixel': -1714161571823058701,
                                        'source_nw_y_pixel': -4398153431478887961,
                                        'source_pixel_width': -8345809535934399698,
                                        'source_pixel_height': -645326827505459733,
                                        'rotation': -6043115335312299535,
                                        'virtual_nw_x_pixel': 1664258151,
                                        'virtual_nw_y_pixel': 67408304,
                                        'virtual_width': -368500861,
                                        'virtual_height': 458180846,
                                    },
                            {
                                        'source_monitor': 4197937,
                                        'source_nw_x_pixel': -1897645549963517138,
                                        'source_nw_y_pixel': -8560225497201895018,
                                        'source_pixel_width': -4975587030355516719,
                                        'source_pixel_height': -7656987462982825039,
                                        'rotation': -4796811262840279183,
                                        'virtual_nw_x_pixel': -44710560,
                                        'virtual_nw_y_pixel': -823327096,
                                        'virtual_width': -876375271,
                                        'virtual_height': -1411274895,
                                    },
                            {
                                        'source_monitor': 1095147,
                                        'source_nw_x_pixel': -7175164296304675415,
                                        'source_nw_y_pixel': -2329607815622630379,
                                        'source_pixel_width': -3351582869693197684,
                                        'source_pixel_height': -9057028792665074639,
                                        'rotation': -1857050979758649351,
                                        'virtual_nw_x_pixel': 1223953956,
                                        'virtual_nw_y_pixel': -450400134,
                                        'virtual_width': -1095010788,
                                        'virtual_height': -1747433901,
                                    },
                            {
                                        'source_monitor': 5440793,
                                        'source_nw_x_pixel': -2015023620910757448,
                                        'source_nw_y_pixel': -368138605495874174,
                                        'source_pixel_width': -4239091453681159833,
                                        'source_pixel_height': -5018033750929325316,
                                        'rotation': -4583862026787015141,
                                        'virtual_nw_x_pixel': 740278279,
                                        'virtual_nw_y_pixel': -211215280,
                                        'virtual_width': -137672226,
                                        'virtual_height': -1570481668,
                                    },
                            {
                                        'source_monitor': 3807178,
                                        'source_nw_x_pixel': -2872892275054466573,
                                        'source_nw_y_pixel': -2649047079023113803,
                                        'source_pixel_width': -606283457854213942,
                                        'source_pixel_height': -8217020985285671054,
                                        'rotation': -8788415855496440049,
                                        'virtual_nw_x_pixel': -579012285,
                                        'virtual_nw_y_pixel': -1942258514,
                                        'virtual_width': -1249510867,
                                        'virtual_height': 125790232,
                                    },
                            {
                                        'source_monitor': 8592620,
                                        'source_nw_x_pixel': -7006530184076122241,
                                        'source_nw_y_pixel': -3397461733779285185,
                                        'source_pixel_width': -5203568554240130386,
                                        'source_pixel_height': -3523524673410455255,
                                        'rotation': -4167086329848974130,
                                        'virtual_nw_x_pixel': 804489739,
                                        'virtual_nw_y_pixel': -32623749,
                                        'virtual_width': 190369812,
                                        'virtual_height': -14097679,
                                    },
                            {
                                        'source_monitor': 2143024,
                                        'source_nw_x_pixel': -4262293165712048880,
                                        'source_nw_y_pixel': -3043102220522473490,
                                        'source_pixel_width': -104969631738590767,
                                        'source_pixel_height': -551593282399834775,
                                        'rotation': -2822338162732999236,
                                        'virtual_nw_x_pixel': -1245508277,
                                        'virtual_nw_y_pixel': -983902502,
                                        'virtual_width': 1260836160,
                                        'virtual_height': 571117621,
                                    },
                            {
                                        'source_monitor': 9968944,
                                        'source_nw_x_pixel': -325351733678211235,
                                        'source_nw_y_pixel': -8224324848225977194,
                                        'source_pixel_width': -3222785546074691451,
                                        'source_pixel_height': -7055225083325703903,
                                        'rotation': -6109862182669484888,
                                        'virtual_nw_x_pixel': 1977530360,
                                        'virtual_nw_y_pixel': -55207311,
                                        'virtual_width': -788250644,
                                        'virtual_height': -1090991613,
                                    },
                        ],
                },
                {
                    'description': 'Ǻ¦Ĕ%ņÜҮ\x8cӵҩӜг҉ďÛDˉCÁȜҌɃ¾ĹƻɋԗŧӃγ',
                    'monitors': [
                            {
                                        'identifier': 2889335,
                                        'width': 8340598543815314369,
                                        'height': 5235236922196589424,
                                    },
                            {
                                        'identifier': -875709,
                                        'width': 523920814411696637,
                                        'height': -8262986074541259775,
                                    },
                            {
                                        'identifier': 918248,
                                        'width': 6336732705592093783,
                                        'height': 3600845920905908306,
                                    },
                            {
                                        'identifier': -104847,
                                        'width': -6224165141612149476,
                                        'height': -5549277025930352136,
                                    },
                            {
                                        'identifier': 9444703,
                                        'width': -906503044334518805,
                                        'height': 9149322297140948588,
                                    },
                            {
                                        'identifier': 7864946,
                                        'width': 8218376629216958513,
                                        'height': 1806856329769736679,
                                    },
                            {
                                        'identifier': 5244435,
                                        'width': 9059297283615581100,
                                        'height': -3539427080903983660,
                                    },
                            {
                                        'identifier': 4513704,
                                        'width': -3331643702344177667,
                                        'height': -7352564661678806147,
                                    },
                            {
                                        'identifier': 9308545,
                                        'width': -3728816814497499669,
                                        'height': 6978891918351993078,
                                    },
                            {
                                        'identifier': 9041625,
                                        'width': -640507752857945104,
                                        'height': 7038413134319567456,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2547476,
                                        'source_nw_x_pixel': -4546521945202098599,
                                        'source_nw_y_pixel': -7081238636360903909,
                                        'source_pixel_width': -7681933183151899755,
                                        'source_pixel_height': -7431115989502837752,
                                        'rotation': -7466720472018929620,
                                        'virtual_nw_x_pixel': -1408565078,
                                        'virtual_nw_y_pixel': -393287662,
                                        'virtual_width': 46187115,
                                        'virtual_height': -1775613507,
                                    },
                            {
                                        'source_monitor': 6229368,
                                        'source_nw_x_pixel': -1880591763670804044,
                                        'source_nw_y_pixel': -6918182512749508755,
                                        'source_pixel_width': -5522509834349603652,
                                        'source_pixel_height': -6328809957260082142,
                                        'rotation': -3727064752347420031,
                                        'virtual_nw_x_pixel': 1669761069,
                                        'virtual_nw_y_pixel': 37682079,
                                        'virtual_width': -182832261,
                                        'virtual_height': -82638095,
                                    },
                            {
                                        'source_monitor': 6180045,
                                        'source_nw_x_pixel': -6058373986817315286,
                                        'source_nw_y_pixel': -4157040075572570902,
                                        'source_pixel_width': -5397636668026269399,
                                        'source_pixel_height': -3513759672926134981,
                                        'rotation': -7451328428780092826,
                                        'virtual_nw_x_pixel': 1005293416,
                                        'virtual_nw_y_pixel': -530062836,
                                        'virtual_width': -1302861249,
                                        'virtual_height': 61067877,
                                    },
                            {
                                        'source_monitor': 5213864,
                                        'source_nw_x_pixel': -1272320890611416388,
                                        'source_nw_y_pixel': -4307020444560763594,
                                        'source_pixel_width': -5904749597120712014,
                                        'source_pixel_height': -8035418179687623068,
                                        'rotation': -8509222149388691705,
                                        'virtual_nw_x_pixel': 1804599238,
                                        'virtual_nw_y_pixel': -1518425368,
                                        'virtual_width': -1895336177,
                                        'virtual_height': 157465666,
                                    },
                            {
                                        'source_monitor': 670434,
                                        'source_nw_x_pixel': -6424250993918088614,
                                        'source_nw_y_pixel': -7019733520767676321,
                                        'source_pixel_width': -7200694455722267379,
                                        'source_pixel_height': -1162827148722813859,
                                        'rotation': -5161449975645992609,
                                        'virtual_nw_x_pixel': -1218974387,
                                        'virtual_nw_y_pixel': 703611666,
                                        'virtual_width': -199713339,
                                        'virtual_height': 1247956524,
                                    },
                            {
                                        'source_monitor': 8941505,
                                        'source_nw_x_pixel': -5017892433986197594,
                                        'source_nw_y_pixel': -7812795548047770408,
                                        'source_pixel_width': -5654690833836625539,
                                        'source_pixel_height': -131629722753374371,
                                        'rotation': -7083264466806243419,
                                        'virtual_nw_x_pixel': -388433973,
                                        'virtual_nw_y_pixel': 871031165,
                                        'virtual_width': 1067684173,
                                        'virtual_height': -1314876625,
                                    },
                            {
                                        'source_monitor': 6030332,
                                        'source_nw_x_pixel': -6385536472463776654,
                                        'source_nw_y_pixel': -3571874278899822250,
                                        'source_pixel_width': -2831587323093033443,
                                        'source_pixel_height': -7150569720824213721,
                                        'rotation': -4760837390833653740,
                                        'virtual_nw_x_pixel': -1616687166,
                                        'virtual_nw_y_pixel': 1237191198,
                                        'virtual_width': 1056918435,
                                        'virtual_height': 544443575,
                                    },
                            {
                                        'source_monitor': 8979135,
                                        'source_nw_x_pixel': -9185193758088615604,
                                        'source_nw_y_pixel': -5992577816258056316,
                                        'source_pixel_width': -6347460357343905006,
                                        'source_pixel_height': -6280817256567647910,
                                        'rotation': -3024291816648469421,
                                        'virtual_nw_x_pixel': 1807169250,
                                        'virtual_nw_y_pixel': -1557416800,
                                        'virtual_width': -1078899864,
                                        'virtual_height': -988641219,
                                    },
                            {
                                        'source_monitor': 8007742,
                                        'source_nw_x_pixel': -2809316784129558805,
                                        'source_nw_y_pixel': -3320068979401759181,
                                        'source_pixel_width': -7873040632019688899,
                                        'source_pixel_height': -6615399290095393858,
                                        'rotation': -5409396493744359057,
                                        'virtual_nw_x_pixel': 1408297878,
                                        'virtual_nw_y_pixel': -1140326915,
                                        'virtual_width': 230504933,
                                        'virtual_height': -1520136942,
                                    },
                            {
                                        'source_monitor': 5402836,
                                        'source_nw_x_pixel': -3754975391519283417,
                                        'source_nw_y_pixel': -3952503239853696609,
                                        'source_pixel_width': -7017011472384897202,
                                        'source_pixel_height': -7392138586876280139,
                                        'rotation': -7384842383424985496,
                                        'virtual_nw_x_pixel': 1587032146,
                                        'virtual_nw_y_pixel': -480541856,
                                        'virtual_width': 214270655,
                                        'virtual_height': 38155717,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 1035704,

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
            'request_id': 4615889,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 1723302,

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
            '$': 'ʀŝϏ^ĨƯгӇЁ+ϢêĊȒǰҮȇɭӰѻq΄ƘӶʛҰÌǌǔΐ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -1737024688252254766,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 710067.1817665182,
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
            '$': '20210327:034418.243275:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'Ě҉˗ͽmӱԤĘζ϶ӶˀɿϋҊśèǜʊʻªӦǍêɄσƞȱ˼ί',
                'ȗϭI\u0379ͳʆ_ŅҒ\x83å$Ɍԙʰ˦ͰʊǶùʯΕЪΦƖʖIĕЮČ',
                'α1ϋȒӓģÝƻ\x9fż|ԭάΐčŞӢȏΓOϥѝƫìXəԬs˽Ȝ',
                '˦ȃѻzü2ңҩĦ\x92ʞӢȆĢ&έÒЁ\u0382ƤƎʬЪľћͳӴҮεԋ',
                'ô\u0383ϓҳɷ.¿ŨԉŒȶıʧüvѼҹÆĞѐΒЎ˄ƥјȂǞſ\x99ҏ',
                '˻ԝγόɞχȖŖӞҧ҈˭ūϲԛTѺ˛ӝȣȭů$6џӝΑұ¢Ɛ',
                'ŴŭɎʙǚ9ȶ\x84²ɏɗԄτ^ȦʌÁŊϋԋǒưȞъǺʓэşҼD',
                'ƽԚ҄ɁωѻäӓňȰНѿ˷ӻbɊҠĂжιсңÌΥɝǫ\x95˻ŕä',
                '\x85Әј˅ʑԦӐι,Ѱ˼ʜќҬũ²ѐ\x9b˖\x92ƚԞΚĀсϬΘŧĿҡ',
                '!Ñ\u0382ǑƆƁ҆ʄǮ˱ƹԜҹΠŷӨџѠŽ\x98ϼϦ¾ҍçȃ\x8cȳɥˋ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -2870038870921413176,
                -5766896079197329279,
                -758069481820239130,
                2991245841179747886,
                -5599781660170297782,
                -1331932947075830999,
                -1742456624805568060,
                -6329620331363292544,
                -9090214109324577771,
                -7418735857912269292,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                250588.9968975461,
                -68807.55479489524,
                761202.4430256068,
                948707.430072851,
                100207.96267266976,
                990056.109397498,
                184192.74001460476,
                957376.4697805124,
                -95410.10141664062,
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
                False,
                False,
                True,
                False,
                True,
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
                '20210327:034419.169078:+0000',
                '20210327:034419.191370:+0000',
                '20210327:034419.212059:+0000',
                '20210327:034419.232862:+0000',
                '20210327:034419.258246:+0000',
                '20210327:034419.278308:+0000',
                '20210327:034419.297475:+0000',
                '20210327:034419.317724:+0000',
                '20210327:034419.336331:+0000',
                '20210327:034419.352984:+0000',
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
            'name': '°Ԗщ\u0382ϾƕˠʓИɜŘĘnˉǣҊϑɹɃυļÍ&ɒƵϐɶ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210327:034417.745946:+0000',
                    '20210327:034417.768326:+0000',
                    '20210327:034417.794224:+0000',
                    '20210327:034417.817073:+0000',
                    '20210327:034417.838201:+0000',
                    '20210327:034417.857694:+0000',
                    '20210327:034417.877570:+0000',
                    '20210327:034417.898689:+0000',
                    '20210327:034417.919265:+0000',
                    '20210327:034417.940444:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': '3',

            'value': {
                '^': 'int',
                '$': 4186183480767632731,
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
            'catalog': 'ʂĢѠГưūɺФЮѮʍЛɷǚΐȗļ˱żΥˮΔѮŌԘҸӹǓί\x93',
            'message': 'ȚȩӆʠsʛıɧÉȍɳҿ\x7fľƫ҃)ͻÑˉҞ¼ҼŬҸĦƐԅǉЯ',
            'arguments': [
                {
                    'name': 'ǊҙЌŘԛҢО×ǌPÀҶК',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        -2479735947437654175,
                                        -7377776447811124663,
                                        5758568196726867815,
                                        3530383856917723891,
                                        3855270671613197075,
                                        6045313175165088347,
                                        2064471771132409167,
                                        3904078468452694197,
                                        -1689149986207146706,
                                        7207448987004432434,
                                    ],
                        },
                },
                {
                    'name': 'ԋоԍϸИxѐЊŨWϛҾџґňuȊ˱˔ɠǎ#ëÿϤҮŗҎº³',
                    'value': {
                            '^': 'int',
                            '$': 3170813656966938073,
                        },
                },
                {
                    'name': 'ƱѸ¾»±ӂ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        117369.83984075472,
                                        829605.8688479915,
                                        350634.8197001386,
                                        285650.79239119607,
                                        903005.3177662134,
                                        773723.3579375198,
                                        293689.4087176789,
                                        235303.30129600439,
                                        590599.7869855633,
                                        644703.511038984,
                                    ],
                        },
                },
                {
                    'name': 'ĺȫϳǂưБ5ǇƮǒɼűǏȯҐҸѤʻӾ˄Ƥё˳;\x94ӛßÍǥǉ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:034416.669457:+0000',
                                        '20210327:034416.687858:+0000',
                                        '20210327:034416.706365:+0000',
                                        '20210327:034416.725939:+0000',
                                        '20210327:034416.743385:+0000',
                                        '20210327:034416.760509:+0000',
                                        '20210327:034416.775101:+0000',
                                        '20210327:034416.789583:+0000',
                                        '20210327:034416.805442:+0000',
                                        '20210327:034416.821838:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ˍĘĪΉʹȇϖʢηːɨɬ\u0379Ҁ¦ΨOϜŲŤŞńñʦӔƷѭįпҗ',
                    'value': {
                            '^': 'bool',
                            '$': False,
                        },
                },
                {
                    'name': '\x9eǊĪşÏȻҩϕʉTĺɥòȆ͵ǧð',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ǱԧӚȐtѻæƵĲ<æǂ%Ȫ˺Ԋ\xadҵƋ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:034417.046654:+0000',
                                        '20210327:034417.064091:+0000',
                                        '20210327:034417.081214:+0000',
                                        '20210327:034417.098131:+0000',
                                        '20210327:034417.115073:+0000',
                                        '20210327:034417.132045:+0000',
                                        '20210327:034417.148822:+0000',
                                        '20210327:034417.165341:+0000',
                                        '20210327:034417.182358:+0000',
                                        '20210327:034417.199225:+0000',
                                    ],
                        },
                },
                {
                    'name': 'ҝ˚ƧҁйɃ',
                    'value': {
                            '^': 'int',
                            '$': 3090072321954835429,
                        },
                },
                {
                    'name': 'ĿkϖʣƱɠ§ɴ\x92һˏƆ\x98ȭӋ\x92ө/\xadɆ ¤ȝŪµ;ѵԉŠҥ',
                    'value': {
                            '^': 'string',
                            '$': 'ĚȾ\x9aНƢɎʷѬβгʾѻìB϶ΧүΨϠϚ}ԬőͰʏě=ҜŭȆ',
                        },
                },
                {
                    'name': 'ƸāΗƎJȜÀȵЖēΔĉˡҼϢȿѬӵý',
                    'value': {
                            '^': 'int_list',
                            '$': [
                                        696491801554491164,
                                        5376495313971819226,
                                        3259575795109953202,
                                        -5365533482686505773,
                                        -7054894859150721466,
                                        -6598110641870671475,
                                        -8210034895123610793,
                                        -3729374992552873735,
                                        -2318155430663848117,
                                        -7990803705672908945,
                                    ],
                        },
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': 'ʃ\x81',

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
            'identifier': 'ɝ\u0383ҌǗӝPŬ˯\x8f˩ɕƃǞЂѨı҄˙ȝ²Эȗ¦οϷǃʣѕԫЮ',
            'categories': [
                'os',
                'internal',
                'invalid-user-action',
                'access-restriction',
                'internal',
                'configuration',
                'os',
                'os',
                'os',
                'access-restriction',
            ],
            'source': 'җИϡЌʱǷʠèʔχǈʠɳͲϠмʘӸͰ²Ԫя\x98ɟѾ\x9dĞЦтҚ',
            'messages': [
                {
                    'catalog': 'тϩТӮ\x92ѪѣрţÍҚŝNǲǊʺÖʕʽǂɍÖоТШɱϱģȔ\x96',
                    'message': 'ǴˏͷѫÌҀȬ˽ǵƭ"˞ǸԤʠèyРǗζFЈɜǽԣЛΈe˜Ț',
                    'arguments': [
                            {
                                        'name': 'ʤϻɊȤϲж\x9a#Җ$$ҥǱļ@ҺÑ<ҭӧ˄҃Ƞ»ѦˈЈΦʆӖ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҔҕѳԧĲɤZȎɊƄ¥m\x83\x80ХľϻѪ9ӻ`˅ĩҳʙɟҧƉ\x9dҬ',
                                                    },
                                    },
                            {
                                        'name': 'ȤǱ^њӿŷ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҸʍԜӅĐİˠҗɧǥǍ\u038dȒ´ɦѝйŌγ˩gæщΙŷʞ҄ȟθŰ',
                                                    },
                                    },
                            {
                                        'name': 'ˊguҝÃEɷÀǆ\u038dʟ.ԪzǢċÆǎ\x9aªl{ƺΛȱ΅ĈɭѡŇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -6910819168505382654,
                                                    },
                                    },
                            {
                                        'name': 'ǭӁ½ӌѫǏΓÊ˱˨ƭȆˑˍΉҙ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӧĖΊϴCNđ\x89ǤêΠ\u038bGʸЂćҟÇƦΞГȡԓƜɠѵӺɹCН',
                                                    },
                                    },
                            {
                                        'name': 'ӣ+τĺĚϸSХӿЈƬ¢ʣɛѨȉЃ\x88ǨФϦçӋƚƎтԋѤ£»',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            767373.9910403978,
                                                                            280639.0820529758,
                                                                            233143.23476983502,
                                                                            590221.5092767301,
                                                                            7885.0729331003095,
                                                                            762276.5726665526,
                                                                            314839.3971328146,
                                                                            218871.22560648358,
                                                                            377377.3772330198,
                                                                            143008.2250245586,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Пƴˇʈ£ӇʹǠϡǈѷˣ϶Ξɨđ·yɯɄOĤ\x9dӃŰШϙÚū)',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034401.936520:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƸêΥҌΙѫʽ˛ĥѿΙѸȼΓΕƖh\xadˀ˛ʈǊѧǳŔоʺҝb\u0380',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034402.009608:+0000',
                                                                            '20210327:034402.026717:+0000',
                                                                            '20210327:034402.043735:+0000',
                                                                            '20210327:034402.060576:+0000',
                                                                            '20210327:034402.077744:+0000',
                                                                            '20210327:034402.100639:+0000',
                                                                            '20210327:034402.120070:+0000',
                                                                            '20210327:034402.139929:+0000',
                                                                            '20210327:034402.156584:+0000',
                                                                            '20210327:034402.173854:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ѽцȌΑÿʏƷαΚKтТçƳˁ\x98Ιȿǐ2ӊҸξþŒžˡŗФ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ӄʙНԞ\x9dÝҿХ˞ңҸљшЮβǦ÷ƒLŷƗµδȹ½Υʈιб¡',
                                                                            'Ēďɜǘ\x96ȍԣʐ˹ДЌȽҙϲƝǏʝЎîŧԙǸӞ9ıÕƥ˅ҸҢ',
                                                                            'ʖ®ŵ\\ƯƧ˷Ӏ\x99ȾŮˮ˥óЋμўƭČǀÒМ˄Ӑҁǲ˳ñ§ξ',
                                                                            'Ы˄΄ϲɵȲӸ©ΞқΜ\\ȀϱӅШŌԥʭԟӷϳҟɦԄƨ˂ƩȦʗ',
                                                                            'ȜŨDηΠ\x91ʫӑν}˲ȋԂʭÛƨϋфùʯ¬Ԕɟ``ǚĹ(ƾß',
                                                                            'ȪȬзƆԒgǫ>ÄЏ\x80зѲÝǵ¬ˠƀѼãγΟӿшЌ\x93\x8f]Ģɦ',
                                                                            'ȇѥ˦Яԑ)шǧϧȁȲɜǙÍԪrʑԕřǈ˩юˡҒŘҨʷı\x8dΠ',
                                                                            'FȐȚâ\x9aȑ<ī ˓ƟѩOƪʞÅç˫цџúΡ¤¼ɦѺԚԝАƘ',
                                                                            'ɟΕǐŧ\x94\x9dȜʘcʌ\\Ê\x8díĥĳę˒ѦĳВҡ¡њͳͼйÅÐ˵',
                                                                            'ȃӻӐȤɗϋʵԉɩ)ɂʉΆӠǈɇG\x91Őǖ˻Ȁ3ϣɩ˭ǤĖү\x8b',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'pǍʔ\x9eГΥ\x86Åˇ˭ѽҤʇӚԎʃ˩ϚЂǹԖ\x99ιԬƍđŒ˫ƮҀ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ώ˙ɵ¢·їǿǥϕѥϓɄɕŜA~ΒȮ˙µƷȇáжė\x9f-ǸǴϨ',
                                                                            'Еґ¤ȓѰзóќŒ\x80\u0379ðĺɷķʧņȲІːИŎҳеѶѪԍµĀτ',
                                                                            'ӳćøĴϕ\x8bȏǘҴіĸĭƇʰЯFЗӧȽȑųҜ˾\x8bȠÉѻŧӺӿ',
                                                                            'ʢǑУϮΏȅԬŇʷ;іhMʫԜȥҢϥԑчСцĄ\x8aˢȘШҏӈA',
                                                                            'ЄӦ\u0382ǭÏƀҤŅзĞș\x80ҶΛöʬϖeҏʘXĳύѦǧ¡\x8fzΉ˘',
                                                                            'лŰ/Ӕ¿3ДϔɌѲǋêʷ΄Ҏу.«нԢϷӘȤǚ\\˞ʖÛǫĮ',
                                                                            'ŃĽʱϹcɀDӋʵv\u0381JϗÄɳǦӒ˺ȠЬϥŅʦɖРӲJϒĦ˫',
                                                                            '˙ɇњ\x8fƵŁŐŭϰ˧ыӉ«xЛğÔͺϘщұ¦ƘПϓӣ£Ѿıc',
                                                                            'ȤQŗҥ´πĽѐPкѨϜƮϘʷӼéĻщ{ŬȎjɏďμɩE¥A',
                                                                            'Ϟ˕ӿȶҋƝѲˀ\x91ÎĐΘԈ˕ʑȬîͷ#ЅΨɦYʮĪĊɊ`Æͼ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '΅ԀТƦŬĐĩ˪ƶŕDҵq҇ϙŔċЖρ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 314035.09795645345,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'źĢȗȄƤÚʆЊԇTƜƪȳƂӨ}iŶ=ɛͰӶҏĠͶƕԥƬӷʷ',
                    'message': 'ҏpʿǈÑ\x8d4ʹ\u0379ʊпέηАɘĈӱɱƇѿҥˀà¼ǒӝяǯ\u0381Ӛ',
                    'arguments': [
                            {
                                        'name': 'ΫĞмªԍƓӬbԕЀӘ\u0378´\x7fĶ҃όʷˡš',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʝ˨ǡŚщԌІêPƷïчĜίˀƅƃè3Þ҃ȎXėµð˥ĶŮƩ',
                                                    },
                                    },
                            {
                                        'name': 'ҒӋԈԢ\u0378ʌϱ˃ÇɦѢӛȣӃŮǇŕƟмґ\x9fǱīȼ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ŁҐơҘ\x92Џņҏ\x88˃ϷԥɩɈԦƏő°NɬѶϛÕɬΐȦѤӨԄΫ',
                                                    },
                                    },
                            {
                                        'name': 'иŜī˭Ĺɸ\x9b',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2719612946543469382,
                                                                            -5602931567765155034,
                                                                            -4072596854251863253,
                                                                            -8764107829034125207,
                                                                            2617789266353641689,
                                                                            8041335047591445222,
                                                                            6052556135124870752,
                                                                            8289268944982718496,
                                                                            -2979935358042869141,
                                                                            -5350027043429879313,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\u0379ҿȞϿʈʍϑιȓĞƍé\xadČɎɚÿʺƙϘʂɔϗȰ\x9fŋÏʨɯԅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ΤҢƸǺӀŦɽϛ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -14813.114297481647,
                                                                            812303.0910131227,
                                                                            176523.57977312303,
                                                                            438583.7217378635,
                                                                            475512.0004797997,
                                                                            218638.51723183197,
                                                                            718544.9446796167,
                                                                            480110.67357228976,
                                                                            -6183.644589428557,
                                                                            699455.1945374708,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Өȁ˾Ǵ˝ЍȻʖķɸ]ȲͺʸʀǧѸǻƹҟű^ӶТHì˞ҏΊύ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 294810.11975562986,
                                                    },
                                    },
                            {
                                        'name': 'ɛƻȩīȕø^ņшhˀǃĸмġ˪pʧ˅ЏͿԃϿΘȲǣŠѥū1',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034403.646070:+0000',
                                                    },
                                    },
                            {
                                        'name': 'чj×ʫҝϣɸѽɒԓǙȅӄԠĖǞ\x8dҐɲǉˈϵ¢ΩДӐФϋǴƍ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÄȞźĥĚ˴УҮȹуĘŤͲɍKԨȖȵɡě4˅ѕ΄ԦΌʮÏƠИ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҞǍʗȬÙ´Ψ\x95Ӄ7ҰƋццгҸʐ\x8eηȒ˲ˆüȫўʒȞхтϚ',
                                                                            'ԊԠЫåΐƽɒȯЭƇκŏɕɪ1ǻĥĮ˔ϓҎóǫБεɪμ\x96˛Ҝ',
                                                                            'ѱǱŻ˰żɏɧȚԥ´ŋцԤǒ_ӾҌēÇҨСԦʞȕʺ\x95:ɩЯƝ',
                                                                            "'СԪś˺ϧϓѮ˔\x8aǰȧà\u0380υǚҿʵŚɡoϫφƺȇƑɏùѵë",
                                                                            'ɬӐСʋδŻ0ЬåΘνұʏґȱʹΪƌɶĲӜе҉ĚʢƪѤă¶¢',
                                                                            'ƙŁϤƻ˭ĈШШăʁˍɀπƔΖȌ?ǲƶΚðƻҖήɮȽƽȬǩѡ',
                                                                            '\x7fҗùȚ\x8cҼӮԜ˃Э\x96ӢӿȏφĹԃ\x8dѿɓšяҖӀйˡҫ˻þέ',
                                                                            'ϊĒϜȇĜΉͽζіѧȻGЕǋÕʫ҉ȦԛǦѤЂÅεͰпԫɿȇʼ',
                                                                            'ŀ\x90ӠԦÈЄф˞ȍ˹ŤȧҊӖøȎГȜȜƾƧ\x8eɨӭ\u0380ϋЫд\x9f»',
                                                                            '\x8bŴЋóϹΩ\x92ŷϮӸTČʶВϒϑѶҾ,äа\x8cȇϯϺңĬŒĂΥ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӬβĲȠ¾Ė΅ˊͻ˴ǃņȂɨКɥњĿ˔˥Әǆ\u0382ɩό҈&*čЩ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034404.228933:+0000',
                                                                            '20210327:034404.249566:+0000',
                                                                            '20210327:034404.269047:+0000',
                                                                            '20210327:034404.287337:+0000',
                                                                            '20210327:034404.307344:+0000',
                                                                            '20210327:034404.327731:+0000',
                                                                            '20210327:034404.348874:+0000',
                                                                            '20210327:034404.367193:+0000',
                                                                            '20210327:034404.386174:+0000',
                                                                            '20210327:034404.404444:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '¬δöŢƬɅͺԤӴɿήɁ\x86Ͷƭгŋ˗ԍyζˋљêˆĔàҗìʐ',
                    'message': '4ŋ¨ԎѼˆТʃuϛыĚ\x9aɒƉ#\x85Ԝîòӗʻ%Ŧ˦\x93ƯнǴɪ',
                    'arguments': [
                            {
                                        'name': 'ǮǌKҥԑOƂ¸ԘӱZξʫЄÜ²˰А',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034404.552580:+0000',
                                                                            '20210327:034404.569327:+0000',
                                                                            '20210327:034404.586131:+0000',
                                                                            '20210327:034404.604641:+0000',
                                                                            '20210327:034404.621566:+0000',
                                                                            '20210327:034404.638640:+0000',
                                                                            '20210327:034404.655390:+0000',
                                                                            '20210327:034404.672506:+0000',
                                                                            '20210327:034404.689596:+0000',
                                                                            '20210327:034404.707791:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϜԁҺĨʠʺɂτчԘFΧˈɤƔҲƔиƮWƃȟѫʍάͽˮʃȤӅ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ËΑѺϹΥӠȰӐ¸ѤнυřǊģƕɬ˹ԗÿєƣ\u038dҰOɠМËϝҾ',
                                                    },
                                    },
                            {
                                        'name': 'Δ˩ŁгӌσғҘǸ\x8eʼѡƗԞɂęŬÁĸӌЖʕͱƔȊ˔ҞŴDЖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 369724.0663018057,
                                                    },
                                    },
                            {
                                        'name': 'οǻЂ͵ϞħƅbǗřȨѥ\x94Ě\x81˼ œӱҠʥǏʶξͶǗˠ¸ʸԐ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1105879816432093465,
                                                    },
                                    },
                            {
                                        'name': 'vӏɶ˺ȷ$ŃПͺˀҺμÄ˶ҍʆӫ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -432278780140301410,
                                                    },
                                    },
                            {
                                        'name': 'ʬ(Ԗ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ˑŞщƹ\x9cͻ\x97\x9bӫǀȡ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҪϜŶ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034405.231229:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ϧғɜǅ\x89ĄőϑyÃt\x8dɢӲѿȇͳΒάƧɪУҒˡõǕǑ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '¦ƸѦƿ\x9dȦ\x84ЪCзˀЌ˰ʑƫѰ\x96ǁӪҤĤ¥ˉͱΧѻ0',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʏĖ(ʿ\x8dœӦЏ\x87ӍőЙđŧΒԪƴӱ϶ƌӤӀɦˎǈԃЛaШʧ',
                    'message': 'шϕ҉ʹʺƴ˨Ø\x8aсІзȪӁѲǵɀñқ˵ǺϭԞҁʧƁЅΡȇ˩',
                    'arguments': [
                            {
                                        'name': 'ÚƐ˄ĕӂȃȻůΠʦÀǙɦˤңӃ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 462457.86499980255,
                                                    },
                                    },
                            {
                                        'name': 'ƌlƋљƈԍλ[ãԨƺĖϸyOɍɡҋϳѪɣϼԓаСёsЖɀѵ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034405.586278:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ːҚѩƙǘƽβƙєӿȫȮOЉѓƎТπǐǿωóцǎтʩȶҶ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -4836515622534752724,
                                                                            1756399541078819677,
                                                                            5735241050589830279,
                                                                            6421553589110823642,
                                                                            824178716913470808,
                                                                            1942411622099216684,
                                                                            6573305814771210334,
                                                                            -394398725211744696,
                                                                            -3787512531982574802,
                                                                            -7288314447389297570,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'əńӜ˝ǀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034405.912802:+0000',
                                                                            '20210327:034405.930300:+0000',
                                                                            '20210327:034405.948585:+0000',
                                                                            '20210327:034405.966645:+0000',
                                                                            '20210327:034405.985649:+0000',
                                                                            '20210327:034406.002609:+0000',
                                                                            '20210327:034406.019722:+0000',
                                                                            '20210327:034406.036664:+0000',
                                                                            '20210327:034406.053238:+0000',
                                                                            '20210327:034406.069847:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƗȪȂ҄ȡӃЕ\x8f\u038dӯԦԦƺ˟˒ɏʹɖҊȕҨΎԡ;5ʹšΞaƜ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1544070627323079612,
                                                                            3863097262576206152,
                                                                            -7064703681749002758,
                                                                            3650749994721865278,
                                                                            3271433500709084633,
                                                                            -6483895079258958090,
                                                                            7892076959191113103,
                                                                            9024644621358575467,
                                                                            9181511172670404559,
                                                                            -4106280790837641129,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԬĐξǟӊέ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ВǐѣǟӕЮɇ\x8aǳµϛмҬûÀrӫƜʉαÖӶɫÚɭēӊţ΅ѻ',
                                                    },
                                    },
                            {
                                        'name': 'ýZŸЄǔʻѝǇȝŸΨÊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            403587.77513183514,
                                                                            570324.9476005586,
                                                                            850487.0328295287,
                                                                            34827.23423831616,
                                                                            152778.15959527678,
                                                                            407434.476132592,
                                                                            418139.4154928436,
                                                                            584019.7858235522,
                                                                            546651.3938610047,
                                                                            934769.8755309841,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '+ӄ\u0383ӧʪǞЯǬǯЎ,ҳѧΖϛӛΫƿ\u0381Ô˼ʢʑШѪǕŘǌҒŨ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '*˹ɂåȈlļΥZѧҳŝмΒҊԢɮԏСӬӝʌˎȢӖԉϑЛ˷І',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            912389.9242694658,
                                                                            -18333.895058466704,
                                                                            369582.36444215145,
                                                                            -71610.07298932817,
                                                                            -61306.25876879192,
                                                                            933649.7620681874,
                                                                            362180.1603509236,
                                                                            388780.2410019245,
                                                                            720478.6662124605,
                                                                            128814.25944615246,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԣЩɧıӤĔëȒϛѾnŘĎ˺Ũ\u0382ʃʲ\x98ɡǔɔÒɚ2¹еH·Û',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '҈YͺνÐʒˉ\x7fΘʰɱƁΟģΧϬЉ˾ľƮОǉ¬ΡԆɻ\x8cϑʝп',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˘\x88ӎ˂ΗƏĻЀ\x86\x9aѩƖ˳цԭɻȕҜőȏǝϫрŒˡʌ9ŀñɢ',
                    'message': 'ğˈȀ˕ǼԠɅ҂Ʀ3ĒҵǧqîɚӱǦȤΝφϰǧ¨äһѠҁ®ŗ',
                    'arguments': [
                            {
                                        'name': 'ѝϩƀӌŐ~ɎЁ=ђЦɟȜ[҇ȿǉeӤӆwΡΖmƳѿƤʸİӇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2391188964706535811,
                                                    },
                                    },
                            {
                                        'name': 'ĆɄȇήԩʼҏǔĀʸǊѷ5iÎ\x9alѠűŜѱJ\u0380ǠҝȄΑӎƮп',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            714775.3863313755,
                                                                            35455.03501632533,
                                                                            751941.5253732394,
                                                                            574501.9266182175,
                                                                            921634.3328438394,
                                                                            762673.5748573965,
                                                                            418413.6813462807,
                                                                            401199.38249750366,
                                                                            630680.5589340569,
                                                                            433784.203361335,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԑԫϹҝȥĤЈȶǷuŊĞνԛ4ѲѰϟj͵ŞΥȢχЦvӴƥӌɞ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034407.527069:+0000',
                                                                            '20210327:034407.544003:+0000',
                                                                            '20210327:034407.561172:+0000',
                                                                            '20210327:034407.578167:+0000',
                                                                            '20210327:034407.595667:+0000',
                                                                            '20210327:034407.612963:+0000',
                                                                            '20210327:034407.630163:+0000',
                                                                            '20210327:034407.649916:+0000',
                                                                            '20210327:034407.669244:+0000',
                                                                            '20210327:034407.690424:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'М\u0383ж˵ȇ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            133305.5705442916,
                                                                            360304.37136876007,
                                                                            236537.56783302774,
                                                                            888011.0899830032,
                                                                            981279.454726408,
                                                                            250593.3926831924,
                                                                            670522.7922396256,
                                                                            445071.2286880533,
                                                                            603471.9428166734,
                                                                            634375.7067134985,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ΣOɽɜǢϊÁɟ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -86715.62743345287,
                                                                            250402.03724702116,
                                                                            -43989.17830827393,
                                                                            218871.15636914497,
                                                                            486443.2189629935,
                                                                            994002.0200894489,
                                                                            858917.73793513,
                                                                            633124.2239601158,
                                                                            55454.624112108606,
                                                                            798526.9307559042,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԫŝΔьŨÛȀ\x7fƀӸƘtҁϋϮҫӶƧҴÀȡ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ÅʍҢșѧӻěˉΓθɂ_ӱϦӴïӋԂΎƞ˩\x97þВŻңŧ\xa0Үӑ',
                                                    },
                                    },
                            {
                                        'name': 'ɃБјΙΑ˨Ȝǩ´ʘɳƾɹͺΎιέƹƄҊȑu',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 173563171887741404,
                                                    },
                                    },
                            {
                                        'name': 'фǦȖҾ\u0380ͲЋM˧Ȁ',
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
                                        'name': 'ɤʮÉQ+ΚЙɎʮΕHΟǠϩʄʝLƺƋɍѡcvªƋŴ˨Ѵӏϻ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -3561853990809147232,
                                                    },
                                    },
                            {
                                        'name': 'ƩӶ*ϊǍϠŁɞǴԜˉǥԮǑ[ͺF',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "Ѱ˝ƈƫhӐ¨'ӰßԪԅƘEϟӅ´úϢǕýϞĈŠǹ҃Ҽе\xa0ɵ",
                    'message': '\\ʿЦѩƵŚσӛнҞЬĕŏšѡ˂ºˆGȏáҮрȑѯźӇ³Ѭϣ',
                    'arguments': [
                            {
                                        'name': 'χӢЛяӨҵȰъʙǴϿÅGËԩɧʲʫҒȫ\u0383ŹʄώǘԑΦˑӕǩ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2152838022707130206,
                                                    },
                                    },
                            {
                                        'name': 'MɇӆϭƉЩĤӗ˦ÅņǑǧ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'лΌ҃ҲÛɁʡ¶ÊʩҠԣ9ȢǞԧϔΆ§ðǙπʓԗԎԥȦӎǱɜ',
                                                    },
                                    },
                            {
                                        'name': 'ΌĥǠ¡WЙȣԛыȵьщ\u03a2ǟԗǥʀҌѽαοɖвɢP҈ӄ¢ɫZ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1816992626141590830,
                                                    },
                                    },
                            {
                                        'name': 'ҷ˲ƉǂъƤ®˙ԟϼĂǥ҃˛ŞцӹȡҸƤ£ΖԖ7ьŧ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -5866239094174994257,
                                                    },
                                    },
                            {
                                        'name': 'ѭӖ¼ƇʑǆǨяðīȬȽ\x88ЯҜ·\x84żŞ\x98΄MЭҵĥˍУ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': 'ȲІŎτΨY˞?ƏԄҋʱȑіΨ҉ɇɪĲˀ˔ЩdɜƒҎʘƍĤȓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7615626838320338501,
                                                                            7354931876276143935,
                                                                            8886385339679382415,
                                                                            -8527861902437488736,
                                                                            3448799185238538720,
                                                                            3819807206377742294,
                                                                            8143366160394138540,
                                                                            6650495271983231026,
                                                                            -2402354444157202042,
                                                                            8885132321537478076,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʨӬлJ\x8dʘ¶ºǅ\x92ǴѭóЪ΅£ҢάǿÞɸҺ\x9fçϳԘʘЄӡÓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -65406.21585348234,
                                                    },
                                    },
                            {
                                        'name': 'ȱƤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -50884.483863230664,
                                                                            351184.36813737947,
                                                                            509213.39156949753,
                                                                            138660.07012563976,
                                                                            472474.2607373139,
                                                                            47600.04166260298,
                                                                            557735.2346269562,
                                                                            -81587.4162389499,
                                                                            461421.0388788722,
                                                                            515739.88526187,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'şԤϋgƎ˰ɴȵ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'тśǒ˱ϣ\x93ήҽ\x94ǜŪXƿΉә˚˰ƌu/ǴϟÍƞ¿íϨρҨω',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "\x90δͱӴΩùщaçǐJɤ\x7fȍĨø'ѿɃŒƥʍŖӷņѷΟȀѻP",
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ԋŒыɎ{ʋЃΓ¦чҼКɆɜˇҿϸˣʖѳν&ʧЍťѳԋ¿ɶ˟',
                    'message': 'ӑοώÌǺɷĹňǰ˯ҸɇѡĔЁǪкѧ\x8dõҖԓѰ6ѣӵ\x93ʶ!ė',
                    'arguments': [
                            {
                                        'name': 'Ѥ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -55153.348135921864,
                                                    },
                                    },
                            {
                                        'name': '±*ʰʫɧДçÇȪrҰҤ˖ͻǘ˙ìͿ˯ӆ©ǵГȼ',
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
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǊʥǁǫVŢԙɳŕϋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            465409.52311052615,
                                                                            -18906.111938540125,
                                                                            596886.1182871374,
                                                                            -43822.411115780065,
                                                                            545873.311388241,
                                                                            360882.5402332847,
                                                                            287761.90874652483,
                                                                            629410.143002287,
                                                                            259026.2943710576,
                                                                            363088.80514643935,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¨ɇɜĔԎŖɓ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ͷӖɿ˕ϔvÄũӡѱјаѧѲŁ¹ɜÆ\xadIįèŻ\x9fÛûƭĐ2-',
                                                                            'φ˴ʨēŨœH˙ӚԜPǕƴԔțƚȝėʉȍҩNɹӾ%ҏφбӞʦ',
                                                                            'YĞԗԤƶèƚʳɇӑԩԇťҐЫǎ\x97тȘÔЋΙ\x8eǠϓĨÕеǇɿ',
                                                                            'е²Ԃ?ƬřȗźѢİǡžɔŽîȷ˼Ũ\x94}әƾΔЇǮNͶɾЪ~',
                                                                            'ɉѬӣӄаӣέәӢɦϗϥЊҋ#ƄʨϮ«ǰң\x8cĶÀЉτˉӯʧϪ',
                                                                            'Ҹ&ʳͲÇήʹοǧ\x9aрԚ˄ƴĸəҫϜʉcʽЖѯɀҏĥѐȴҏʵ',
                                                                            'ȜƖʇМ˖ŸàТ҆dʞӁӂɆ\x87ӌƲт\x92ș˯ΊȳưîǧˤʠǊɐ',
                                                                            'бѠʊԁǔˤʐȶѵӨƵȵӟyuf/Љ&ƕİϯΠVҏ\u0382δɱ˽Β',
                                                                            'lИě]7ıцԖбʠϮǹτÖγеɚΫǷŴ]ΚȓēȍǗͳЭвƪ',
                                                                            'ѭǃȘΊàƒϦā˹ϞӶȜѠЗ·ҨǠˍmƉŜȼŔˬíӤΎԓkS',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˸϶ʔԮƲχʛӈˊ8YĬκŋьƀȴѓBɛȸԔЌϝҐȠ\u0380\x91ϗö',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ӾԤ^ʎǸƺ®',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ȳʱ©Ҽ˗ԊӗζǻϥԎǌW8ς¢Ǚ¶ƽĈOÎėΌΪ¡ÖѱƮʹ',
                                                                            'ĤҶӀƴǻɀϚҬΖХџ<ʐ˖µηнΆ\x9bѺзςҪҶҳѮБΓҥĲ',
                                                                            'ɍѻśñΓÈɠõԕėȣԔɇĺҮѽđϿʱƵƣʢќ˕cӴήΰǉг',
                                                                            'ǻəӫțɾ~"ŜВµĿαĮάÖȽɻĨпщȦγ¾ҌʐʽӡΤ\x9fƥ',
                                                                            'đӯ!:ȧɞӶ˯ӛӢЏЩɐǺɅƩ˻ȥǻіǜҀûĊɓƝǧ˵л\\',
                                                                            'Ʈ˲¨ǼϘúľԌ\u0383ǞČԘɉБӜԧųǻ2ʑƩǁ¿уǖρǂ¬\u0383Ĭ',
                                                                            'ƾüώԊ\x88.ϾͲЋ˓аĆƺĢŕǤȝϵѺ҆ԑǣ҉ӞӠţEgϤN',
                                                                            'ğăˎɌůȃĞ˚TłДӠ¸ʧĮ˹ƋgǨμѓјKǒŃâЭVõШ',
                                                                            'ʵɱĆÔɓđƿÎοȫƮȳӯԞɐfҀж+ҍćȰϱҍԧ˺ƑɸƋƖ',
                                                                            'Wƫ¥ͷОЦУӘɷНӏüмҮëӳТŎSϺВ\x9cƶpʡìӲɃҿθ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɄΟűȔa2ȭźӀƂĀǭҏӘӷ͵\xa0Ӄ¸Ʀи',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8894987074078445682,
                                                                            -3909969836788197999,
                                                                            622948750487715911,
                                                                            -1275542219149133602,
                                                                            8596987285087072363,
                                                                            -9095011032408187113,
                                                                            -3085958736419458936,
                                                                            4496277459930511449,
                                                                            -8929372396616996895,
                                                                            -1317576890134048879,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ð\u03a2˖ğȤƤǘЯȉǛȬǾтӒϊϮӟԎСƾ\x81ΕҦԊłȼʓÚĎҢ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -29492.91378053544,
                                                    },
                                    },
                            {
                                        'name': "ȌØż^sƲDɝǐF˘Άԓ\u0381ѿєѱcǅń'Ŵȋ",
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -6993136934204638945,
                                                                            -1273527254683551573,
                                                                            1943572888089268074,
                                                                            7083146983665829943,
                                                                            2076862911842286787,
                                                                            3090737517502883127,
                                                                            4449002867218792289,
                                                                            802419330752401994,
                                                                            8561233097504459349,
                                                                            7152781618203112541,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'όҪȿȀӴƯìº¦kϯǾԨW:Ɏ\u038dÕԘʎȤңƕҊŃЌАӖyǌ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2394084802219083960,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ī\x9dŽЌ҈ɠ]ŉʙ˴ɆǿπʔƚЅɬǥ^ĎE·ǖΧȤЄöѵҘй',
                    'message': 'уϜ\u038dmǐȷ˱\x97ġӝч©ҐϪ҅ǲ7Ф҈hжˡ˳ȁσЗʎЪϽŬ',
                    'arguments': [
                            {
                                        'name': 'ϱӇ\u0383ÓƤϤӃȦғфԘǬҡЇ\x94ǡ΅ɊËįɳŸʎ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'гԕѪƥñһB9ϗȕҥ8ĒԉȗːéйˢПƦĒѳöѪĐƭΐʤҶ',
                                                    },
                                    },
                            {
                                        'name': 'ƴ˜Ҏˈåŧ˵ҟlòäԦŜԥZʓѶĆœĭ˛ˏ¯ΠϙȄэ¯Ҍɑ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034412.283200:+0000',
                                                                            '20210327:034412.304576:+0000',
                                                                            '20210327:034412.323690:+0000',
                                                                            '20210327:034412.342573:+0000',
                                                                            '20210327:034412.363251:+0000',
                                                                            '20210327:034412.383745:+0000',
                                                                            '20210327:034412.404350:+0000',
                                                                            '20210327:034412.423752:+0000',
                                                                            '20210327:034412.440308:+0000',
                                                                            '20210327:034412.457754:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'fƪƃ\u0381ǃȐĠәѱʭß\x8csƔϊĹԟϟȯɇҢvˡΌȈÌǹɖȕҘ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034412.554464:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ӡɊҀ `ήц˺ʢѴӼϼƟΙŚӷәӯ˸ɀɐăƥRҮʀʇǔČʣ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            121382.65336145947,
                                                                            152448.22139730593,
                                                                            -39125.46123513092,
                                                                            213882.59418796567,
                                                                            42174.12822005106,
                                                                            878455.8154866787,
                                                                            592163.1129272503,
                                                                            788081.2787976194,
                                                                            -98406.0649459129,
                                                                            721312.7665374402,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƿÀ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034412.872866:+0000',
                                                                            '20210327:034412.890644:+0000',
                                                                            '20210327:034412.907678:+0000',
                                                                            '20210327:034412.924416:+0000',
                                                                            '20210327:034412.941174:+0000',
                                                                            '20210327:034412.957897:+0000',
                                                                            '20210327:034412.975024:+0000',
                                                                            '20210327:034412.996651:+0000',
                                                                            '20210327:034413.015857:+0000',
                                                                            '20210327:034413.033794:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ȋ\x81ǵĬÛƝЭɘæƗӺĚˀˤӋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 111103.22541701765,
                                                    },
                                    },
                            {
                                        'name': 'ǻ˟F~åΞͶ˾',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            272916.9989042114,
                                                                            177011.16972318263,
                                                                            957452.6230717236,
                                                                            356782.2621966674,
                                                                            984815.7884297706,
                                                                            598566.0913716347,
                                                                            442718.1492202409,
                                                                            594618.9484588901,
                                                                            709868.6620221488,
                                                                            752675.2782930954,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '҈ԫĪӑǹǻʹ2γý\x8bƋɛǲ\xadӾ\x9dǃƽ˃',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ʀ¤ǨϏѕɉɝȕүΩҨˌűǂβʜěňΤ˸ǔʚò˸фdƋϴţǨ',
                                                    },
                                    },
                            {
                                        'name': 'хпƁɆʣˊǉťĺԟÃW\u0378ήϜƃȎҨéćͼƝBŠȝΫǋ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǌԔ˼ǈΈȺΣѮÉFɹɭӐũĩŶʔèůʎǘƘӘʥӫҲĨǉ(ԙ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2000583280196060891,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϟgʆ\x89çϲϊ˦Y\x90ȫΦǮΡǖÃœȦеЇ^=Ԙμҗ\u0383ǶӶԐѣ',
                    'message': '΅ĈǳӍƞЄśӾмʛǬʌŬǅҋǲηѪˇɥɼÐԞΗÜÁ\x8dͰ˧Ҷ',
                    'arguments': [
                            {
                                        'name': 'ÂŹО·˩ȎˑϢΛʹȎyċÓ»9ԟҨǽƥmαˮǕ\u0383ĥȘϵӤʚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ˎҨɏǽӮˋÝώκːcȔʄӹʓӖνΆʄҸmİǺȑҩ\x87VҵsԄ',
                                                    },
                                    },
                            {
                                        'name': 'ҷӮŉРÌ·ԌƋξǫԎρОXºӓáӗΖМʆˀвǯɹ¥',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'їÓԠňϕć ːȿĉΙØƤ\u038bÚԠό\x86eϚ£Ҁò˛;ӆαǐµǍ',
                                                    },
                                    },
                            {
                                        'name': '3ҒĄҐˎеǥəӿǜ\x7fѷĀӚŽХ«',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
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
                                        'name': 'ƹā3Ĺ_ƷҾϨǗϳǽŝªґ±ʲ©ø˟ŘҴĸǋ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɲˬɑȈԦΫυƊgŒǧϦŦ\u0382кˁ¨љԣƋʊƌɘĸ°ǨȲßʺȹ',
                                                    },
                                    },
                            {
                                        'name': 'ȸʪƶ6ϝ˰OƹͷIϳȗ\u0382ȏȬƵϸǽьyʝkƭѻΘ\x7fȱԝ®˟',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǯ\x9bϻӸr*ȫŘ\x85\x93ȔЛĀųͻЯёДŅ_ƯÁßɀɝ¸ǆƝʢǞ',
                                                                            'ӂġǂ2īӽԍ˂A½@IӴďͻƉѢƏʴþʖжЛŚǝ¥\xa0Ӳϗą',
                                                                            'ѴʈԧӋhƳƎ˾Ȗ҆Ƀˣńϛ¿ƥǬЭʀӢǈҒ΄ԫӞϹĮ\x93ҳΦ',
                                                                            'ʆЛЯɺȮ˔îȆôӈĜѶ©ÞƫţЦȼǣΞȄǂˎ¯Ǒɂɮʿ¥Ӊ',
                                                                            'ƬeͰч\x9e˓ίţ¯ŀӏ\xadŐЍŌӴԟ\x81ԬѰÒͽʟЩĄďŴÖӦv',
                                                                            'Ѐ&ӊʯ˸\x9dӦzώʵȪϨôʥͰİѝÚҖӍ`ҞţȖςŮŁǬҨș',
                                                                            'ĶŹQ`ЄУǆȔơЗÞӚҴϔŞ\x87ǎYc«ԂϤƤС©љǟϋ¤ƺ',
                                                                            "ŸǟϷϓDǉȿÅї˶У͵θɕǺmƐȦЦʶƗÔŭѲǫĸǈ'ϑͼ",
                                                                            'ΨԩЩŨΞǀȶϠ\x87ԁʗџɗɴƳǔЄɦɷƿǁȦϸӂɴöʦʹɴƠ',
                                                                            'ІƘǼ\x8fϱҵzǔǯɆ¾˜@ƩΨЮňƸ¼ѺȗѺљʨԥêεǧȮѯ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': "\x8dɓAjκɚ²=˪ѪέєŅɀΓԎ¦'цԈѲǿԢĤ΅Ё\xadēӷǪ",
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:034414.661011:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ҺХȐϙUΒ÷Ӛ§,ŎǔԜɒǈ\x8aŖρƞϐӠЧɣȎӐѧ˟Τ˚ͻ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            183857.41509244748,
                                                                            495439.3700579383,
                                                                            40923.54687065061,
                                                                            386519.8022647243,
                                                                            12107.239191268774,
                                                                            -35132.63717376518,
                                                                            316848.895562899,
                                                                            713712.3967313027,
                                                                            183957.97526929656,
                                                                            23744.224519256022,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӂЀХɥ\x80ʏҺιǸʉͶŀҺȀƯ\u03a2ʿɧuŶ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӎOїСCё˼ѭƸʹǫν`ҚÄȩ@˧ƒϸǚϺǰȩэşʥǝʣ˔',
                                                    },
                                    },
                            {
                                        'name': 'қΙьǳQqŇ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2345278787528780705,
                                                    },
                                    },
                            {
                                        'name': 'ȣй˙ӌЎ΅ƠΩ²˲ɕЄʭϐɨԁȞȒłĀӌ\x81KĩƸЮөƪŭЃ',
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
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ʘǨǗЃŊĪнͺΛϺѭNϚϘħćǼ)ѿρŹѺƾϓԥϬӰЛ˦ȡ',
                    'message': 'ǙɩѰɻǂԄϱӁǝΧԖȒaˉɾ¦ЇĊĝƀєěԁɤĚԫțÏɉȸ',
                    'arguments': [
                            {
                                        'name': 'Л>5ύΛӍӢª?ńǼȊҸȱ¾Ŀ+ÛɥʦНĤ҇ͶғѮяúÍә',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Ӻ˨ƟΆÜǿҋѺìԗĈѶʦ&˝*җƚ\x96ϸdʹ`ƇȏƆ«ĘҹÑ',
                                                                            "ȴúˇҊȬё˷˕oQ҅\u038dВ#¶ȵàуӇӪΒҞƴ'ǵΏжIñԧ",
                                                                            'ǖԐˉãɒșӒôÇӱϝƉ\x7fəЦƻЗӊɥʰҘΌűпƀÔUǱԫȇ',
                                                                            "˅ƬËÍԫcȧΙΚK\x97QWƘΏ'\x953Öғ³Ο\u03a2ʾˁԖʛɕΎ҆",
                                                                            'Ȥÿæ\x9fй΄āԊ¤ηìǛǝgϚӺ˝˪ӌӁκΟPʨWcԁɊʜǤ',
                                                                            'ő˰ÖϧŀϠšԁХǕĬҒȭɳɖɦҌRӭȆŔʩĺʱʱĸϪǣǫŝ',
                                                                            'ƟҌп¾ӒǏӅԕŨʺӟчș\x988ʐ¹ɮėʛLϽӋņñӁźǾʊѣ',
                                                                            'ԔЯˎ˙ƦͷèɕʭɊѱěΦҮӄ«ʠҘƢѵɃӣʙΑҕ˝ΐԩԞӼ',
                                                                            'ǰŷԋˢǒ\xadʄҿ˸ʡDĶȺpT|Ă¿т˓ɻ:Шѿϗџҡrʿô',
                                                                            'ìΠҠˡӚʓϾʈrʆǘһ$˘ӯͻĝǠĆYŶȌľУɕɃĻ˽҆є',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ӓΟϝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:034415.644944:+0000',
                                                                            '20210327:034415.662090:+0000',
                                                                            '20210327:034415.679537:+0000',
                                                                            '20210327:034415.697142:+0000',
                                                                            '20210327:034415.714086:+0000',
                                                                            '20210327:034415.730941:+0000',
                                                                            '20210327:034415.746056:+0000',
                                                                            '20210327:034415.760219:+0000',
                                                                            '20210327:034415.773239:+0000',
                                                                            '20210327:034415.786390:+0000',
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

            'identifier': 'ũǪљќư',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ÒƘ',
                    'message': 'ϝ',
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
            'request_id': -29996,
            'error': {
                'identifier': 'ŽԟòȍǊЫ3șƥǼʵ҃\u038b\x99wÿɇӢ˗ќĨǣɓƶĸʤżҷŤˀ',
                'categories': [
                    'configuration',
                    'network',
                    'file',
                    'file',
                    'network',
                    'network',
                    'file',
                    'configuration',
                    'file',
                    'invalid-user-action',
                ],
                'source': 'ƼҫŏԂćVOѺҝϙt˖\u038b@ŒϝϑŌϟɄҖОʱǶïϬϷÕľ*',
                'messages': [
                    {
                            'catalog': '˘Pěʝпρӛ˒Ѱѣ÷θ\u0378ʞĥʖʞͿʱıȱƪϔϰ\x8aʛѪѕΛ\x9d',
                            'message': 'ˣʭőйɾʞѬѮɴPԋȻҗιА¡i˙μĆǺԭ×-ļʆʞƷáӈ',
                            'arguments': [
                                        {
                                                        'name': 'ɹ«˄Œâјǎ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѮŲ/ɻШĲΧʜǽœВԊ˙',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 757963.231542835,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ňŉȈϞʂ$=И',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӓȁӰ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҆ɿüʇдȝʉʧϠϷί/ϓjĔǆP2ʧ˟ʽȢɲĿгϐ\x9běȝô',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'δѻΪȉҘˡȬ¯ЛˢͺұѶъÂɝӞԫҦЎŻцѻ³ѷҎėǱI\x99',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8921410016136368705,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԅçкοēǟϤϣƎŐҺο;\x99ǷʣȺƫǶϗѐʭȈ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 309521.22843666916,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņɮѧҖЅβeӠӆǷҾĂțǎƛƃzǥȭԚùƈƓĽuƜǳ$ʝ˝',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '»ϫŧɬ/\x80;Ũɝ]Jůňεɏ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΈМȫ¿ԚԚćёҚ\x7fȭ\u038b>ÂˈҁƠ©Ҟ˨ŘΆȴϺ˯ЌΘһ\u0381ý',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ˠяʏϋĝòmǜЍюGύӤÍʥήфĂƒǢĩҒʖϵĆõ҄μȺԕ',
                            'message': 'ς͵ÃɇѡŞCL§ћäӤ\xa0U$ԟԅűӐůԬ\x82НˣƞƘÅˆƹϧ',
                            'arguments': [
                                        {
                                                        'name': 'ŨĮŉλķμȏϾŋʳԕÁͰčƺɺĨĻѳԄ#ŪԖĖ±PĦ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 387317.809917412,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʨƿӰǚѤʔҭӈĎκӦşͲëȓIȶɵĝȒƸłˡȣȈΑɭζēϻ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '˯ɏÝƴȡԏӥԣҤȼӾeʍʄЙƞӂƅ®ˎ˫ņǱíèďÞϼ§ԡ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѿѷşȫοϓʅǍ˦ÆɜԊƲҜёҠũм¹ЇʙϗЕªαΐϥĀȊň',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -2075020876876906011,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƊķіɩЙŐĖɔӪѴ˲ʯ\x9c˄ŸǍȶqԟљƽÏ˹Ҿ\u03a2Ġ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЂĸäͷԩƇɅțȭϱŋҋХƤǚ˸BƠʗʟҧӤėĒљ©ɻúŞ]',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034355.016256:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϓʖȿӟƎ˃Ɗʔԗ˽ѴȕɖŬѾ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΣуϏ¬ʥȆơ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÝƉЬʹÖΗϬFɣ\x9eʯσ¼ϚχʎȞêƈίǍʨƔёԟ˗ІЭԞԍ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7169600959802195916,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨǚѩȎΑѸ\x9avˤϪ(Ľpǵ˭>ҎӴŌΦɭȇϩΝ˅Ǣſƾľ¨',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 1761027179451816913,
                                                                        },
                                                    },
                                        {
                                                        'name': '8Ψ˹',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 479473.5614770509,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϷҰҖɎȭӆæԣH÷ЃƧƚȻFǟң',
                            'message': '˪ӾП˚ӞǌȦаұȤʠċƖˢÝǮήҽУ\x82СóϷƩ,ķűȼaϙ',
                            'arguments': [
                                    ],
                        },
                    {
                            'catalog': 'ҭӓӴЁӏɕÔ<ȗýʰù\x81в˒ΏͽƚͱжϗҒήɢǥΪӦ˕6ҷ',
                            'message': 'ӠɁɒПѫyˈ\x95ēΝνɞ\xadĖǬХӢЇьǢѴȆӗ˫ҿЀpԠѳб',
                            'arguments': [
                                        {
                                                        'name': 'ȐʅrƇc˳ˤ!ǀԫ\x9aʻψ×҂ȷ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x92ӍĨҬ®ӪľǚџǗíʤʬ<Ҿ\x80\x9dΑмƑĊTǛԎßƕƣ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͺȸéρӨԢӼʲɝĐ¥ѡӯǽͼʀԁΦӆʘ³ԖωőϚΈԉĸõӢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x90ЄŚ˺ĲǱХKʾʫ\x9bϊùƽǓҿά˝҉˯əūɔʦȆɊɰCȓɳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĨѺΆЦ÷Ù˛ΪǅFĨ,˥\x80ӃϔκǤМɟοӴҋgΏԓɢҁёʁ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'әñ\x99ѸàМЕ΄Û\u0383Ô\x88ŴҀĥōԑψ9òԣʔұЀĶjіǭѾã',
                            'message': '\x8eˀЄɁę҈ŌΛаΕΛ-Δӥɘ\u038dҌɑ,}ŏÌƲфҎҍǮǢӘҼ',
                            'arguments': [
                                        {
                                                        'name': '4',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÁȃЊяΙć³ǼɵϨĮˬҊ8ϟUѷłʌƔΓҺђѝȱѰэƍΣɾ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ªϋʑȑҘɮǾҐƂʬʌǄǐΚ=ϢĂŪćƕЧ3ӸǠːɶƫŬΖ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѯҴĽ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΒǂȏǼBAºʔŀѥєОɦ·',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ύƩр˳ʠƊԔÔԝѦφΈŝғ{дǅəŤӴ˽@äЈBΧɆʻҚМ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĥҭǱҽЮϕҿΘ@ԥ¹ȶҌΓƸĤ*ɺΟǺr',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 674142.403961882,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѕψ|ΐă±ſʆғβĹԅюsˍÇˢ{с҉ÓҁʶϵÁӛǈƖ҉μ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŀÄȖіЗѱЇǗĈū',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 289242.2459649174,
                                                                        },
                                                    },
                                        {
                                                        'name': "ǢɄ˞V˓ȈҊþȟǖ¬ˁ'ӳѐԧҽ˟ĮȢ^ĝϗ\x9cɕʸʖԚˠʦ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȋҁͶ\x96ȧ˳ҧҐȤ¯',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ԧśƇÙȨѭϭėʐϗѭɪɯƂӾ˙ȚǁăӚĕ=ǢүϥԦӱԧ΅ˬ',
                            'message': "ǪќȜ\x9a҈Ӵ˫,ʙЙҋҠ>'ѾфɩĨ\xa0ǄӤ¸ȦσӹԣCˇʉо",
                            'arguments': [
                                        {
                                                        'name': 'ӛ˺ĆϥӃĺŖы\x9bćaΰHȋ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '&ȉœɿʶΚюɿЀсŅюӖξԦҿ\x9féyĊϬӓʶԀԏïҘǬˊª',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034356.772800:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȯǊɵ?ΖȋȟŁèҳËһIѲŤҗ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 901585.8087067816,
                                                                        },
                                                    },
                                        {
                                                        'name': '˳ϸɵNӿ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØӊĤ҉G\x8aϟԨʪЃ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 940853.4178361065,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȫѧTӽƻϟҰϤһ\x96¸µѤƦӴ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034357.069808:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȥǀѪĀɦȉȓğԛţ?мєиԓƃ^*ýӭœ\u038b',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƿďЍƧā$Ƿü_ϵȹȸԡǒĻˤРξСҼƘ]ȊAԭΞЬĆԛЖ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 7270468296789363738,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǬʼъǸӱϼҘ˶ŨҿѡȮ[ұnϗοԋӓƪ\x9ałκԙņǱҐŪƚ=',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034357.309565:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɝǑqȚîϣ҃ˏ*©ǈϜŽɦ\u038dԊÒәԤ\x9cã\u0380ȳǡȢ˭ų˖тɰ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɁJɻԘǇӞοźĪԅÂ^ǢųĄɥÑƑȆÃìˑʾщŻfʧ˳ßϙ',
                            'message': 'ʴ\x80ЭĥTӠKʲɞăzŘ0į®ǀɧʂǾеʋȸ˼ɞʹʹīΆЯѩ',
                            'arguments': [
                                        {
                                                        'name': 'ˎӞԍӚϬ\x81ɯƗд@ɗůЃѳĊ\x80ɁŸЦŨЄˀҷѨƮ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɡΊѳ˻ˁÃј˶Πıҳŧʝŗ˯ɕûƼȘ\x9fŉȈĩ?ĴϹtɦ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034357.616976:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȉҢɬӵ\u0381ȫєŁȿΈίϜÙ҃ԬίѤʫξ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŜɆɀθҕ\x99ϿԤȂˆʬɑȧ\x9f҈Ӈǂʿц҈\u0383ƈż˴ʑŀΟ©Ɨδ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɕӃ\x8c\u0383эôŷǢ{ιӱ\x9fԅƧǸςԄΧˑːϔʘ϶ƐǤѴӨԈ±ѿ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԄʽƤȱξˌϟƅςҹΚ˨ĉ˄\x8eѤҭ*ȔҥʚÞҞ3ñoϷ]ǒҀ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'åƺΉ\xa0ʄϸzŭɢɼʗӽѹӚԤȭƟˉϛӫĦ˛ЌЛǯϟЃ9ǩɒ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʠұӤÖұ\x80£шПʓĿɣҭɇ`Ѩǻɤ?%ƌī\xa0ӃćʿĐ³',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϭįӾ϶їФ\\²ȓȸɫ˄ɯʶˣΣӎΠŴɋѭɇòʹŹӳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'BӪªԫɦԙǺΝ4ρř7ҟvԣϷřӒŎɴЂӛKӴќȈӁːӾɧ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ņɌŸǙρѥ\x9aҞˮȪǪǈ5\x84',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034358.091553:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÍȗˣϢŤʞ_ϱȷʭɔšɳɎɷǕǩϑϹČŨЭ˸ƒςŋРŦԫG',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 456191.5176226818,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǙǪԋ`ȢW³ͽ˽ӁŊŵˇͻƷİψ´ӄ\x8e[Ƙ΄ńȠȻВĐαë',
                            'message': 'ͳԃ˗ˡ˪ǻӞɫ˙ҀѢǟϛÄɫĹƈђԪžĜ\x94ƤӦƄǗȃțǟɲ',
                            'arguments': [
                                        {
                                                        'name': 'ʨҥŪΕ˃ƦʯăÞʦϾŸþǠǒԖśБͷЌҌԪ¥',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 454958.9283693092,
                                                                        },
                                                    },
                                        {
                                                        'name': 'yʕ\x9crԁÄ˙ƢɡĒϨĜƪҔҞş=˴ЉȂɊҰĖÌ˫\x9aÈ7rɬ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŴíǺ\x81сːƙиòĹ.ǥʹЮһłƵˏƟӏ§ƠӘǾ҆ƘËľƛȚ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѿǢӡΚ\x81©Ĵ½ůҿ±ίx˛ĩȨXƫ˓ԜĩұƂťτʣʷˮʅĩ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˡ\xadͶŦȾǭǐďӔҢ\x9dϯψûԦʞȠqοқЎăǙėæёƮѕɰƗ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ϽԢŢϯψɴѪŵ˷ɮ¢ßƁĘ¬ ǜÐǂϚdĄʱЊϯоȿµŃϳ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʄȠˑϒƮǍɮÝğӀǴŏԜƒ÷=jjφѳ9Ƒ\x9fФǹԆɗȢьņ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 508384.36640842236,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʼśºˣǫΜʱҠʇĽɤО?¾ѳĢϾ҂ΤǨIθп*ԉàʾ\x9dƚX',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -735902760736468847,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄӌ\x95ϫӻ)AБuȒϻɽǊȶƊɿΎ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЉÎ҆ϗ{ʈқӁΕƽӶҝ5ѷXŸԀːÅ¦ʂ#',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʩԑǹ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5401047343331926356,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ſȐÎȹAʘˌȌɽÀ˪ƇJȠφȕĭοʢîȆ>Kǌ\u0382ƋÖ&Ϲ®',
                            'message': 'ԉþĮԤԭҷТZʫľƹʓˡȰʠȂǝҠ\x98ɟοуέĠ5ǁƀ\x90Őк',
                            'arguments': [
                                        {
                                                        'name': 'ǥƞɖɦԧƩ*βæFъΗa˂ԜȯϰěŭҴЦ\x8aѳO\x8aҁľ\x83ƦΙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 265038.85600483534,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϴӝФŒǽěʕŐȿ\x87ΝƆƤԟɻǨǪqǬăƈєϓ҅ќ\xa0ȱ˓ñˏ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΖѨҊ҃ҥȓǈΓɖ˟ҰŮҚԪΫƍЊŘƣФɎȸ\x91ԪԉΆÍɧ©g',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʜǿˠЗЗȲЧǏǁЛµü,ǭýʮĤŉ˟χǒ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'í\x94ßԋΘΪТϵѲǺʄƺ\x92ȔҩǉϚϏώŹŅȩʮŜХǧφгȵ+',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϋҷϼӡlɅĤeŻϓӿԞѴʪʚҴЬʆȂ*ƔǗқ;ԁ^ҁÜ˓º',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'EӴ˻AӜƳMΟќҘɔƠ˦E˓Οӕˈʀ©',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ͻ\x8dÑЁŲɴǗĉŏGнЭƼƦȼçbԖΊĺķņŊǘФćЁҹpɼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '΄C҄ϑȚΦŚŌʟ\x8fȐϾ\x8bɪŎΙ$ĭ\x95сǳŝȺШŎ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ɛ¡Fţɛ\x88ΎȴϥxϹȱɶѰ˕ԒҷӑԛL5ø!ѳǓЛϛ͵ĶΥ',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x7fkŇJԍǛϨF\x8bӲүʶҧĶъƩΆɀϴР\x8aЃǏˣžğĄҘªҊ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǐȒD\u038dò|ɌǀП/ҵ´1ԠҥʽΰѵԃˏϡŠϨ¾\u0379ӷȟʞ˖Ӯ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '·Јԁ\u0381ɅԐʢΒԅƠζĶԁ\x9cȀҐВэΓɴрȊŋΕОƆ˺Ѝrӥ',
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɿƞɦÁOŰè\x9dòmǣʏѱǣ˼ˤˡȶðgćŗ$ҍҢŔԬɨ҃Ϧ',
                            'message': '˹˄ĎƵŮʷDҤ·ŲÉKɧ¶ќȨǺĳϑãäˤŪǺȟΝɼʶʵ©',
                            'arguments': [
                                        {
                                                        'name': 'Æʪœɧ\u0379ΪӺĵʒȾȂφyɫоҨ\u038d˻]ɓŚҿɷȷҚ\x8eƫx\x8aӜ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 954488.4530751905,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧ\x8fĸɬȿSԀ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƀ\x8dдŁRԅЊºϐƚ˗¦Zѥ{íƊĞ\x96ȆԮ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:034400.079314:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹ˂ӻɬėӓɘЦńȔϹȰ҃ҿlҰЋѲŅϖŮΕȱD(ʂǠƪʢҶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȸԐэíδĂǽΜȖĊɕÉ\x99ЍÿӢɝȷʺг˶ǬiɍlфІ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Κͺѓ˻ϹŬïѱɋƟέѱ˺Ō\u0378úƒӭĥǽѯ˹\x89æʡʉ Sβń',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʻʳƯԚС\x8aaȮ҅\x8dȕ\x9eƓȟԚҐˁÕ2«Ҝ8ʌ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ê¢ӛʒͰ˟ʻ\u0378ɊϞĸÝħνȊ΅ӹь\x9fƲϖ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '!ϥƋҪDфЖ5ʄËBŁвɯϖƉKиɨ.À\x8d',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ĠȤ¤Чӟ˱ѹƋ˸ԣШƫԂʬƌϰԅяǮĲǽŇȔˠÍȤѹˊұʃ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'π˔зҒ',
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

            'request_id': -39283,

            'error': {
                'identifier': 'ԌСͷRɏ',
                'categories': [
                    'configuration',
                ],
                'messages': [
                    {
                            'catalog': 'Ɨɺ',
                            'message': 'ǹ',
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
            'nw_x_pixel': 1812919113,
            'nw_y_pixel': 138506795,
            'width': -649471520780036152,
            'height': -8292013038179628774,
            'ratio_x': 5018869480804938111,
            'ratio_y': -341902345429050461,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': -1984885362,

            'nw_y_pixel': 1013326293,

            'width': -3763888165335614365,

            'height': -9093704036244948325,

            'ratio_x': -8686479239818767017,

            'ratio_y': 174148574282353391,

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
                    'nw_x_pixel': 1008360373,
                    'nw_y_pixel': 1464950093,
                    'width': -4614406806413341212,
                    'height': -3142897123614461513,
                    'ratio_x': -6757286244942731540,
                    'ratio_y': -4529429411418366692,
                },
                {
                    'nw_x_pixel': 1745006597,
                    'nw_y_pixel': -1663609163,
                    'width': -6693102562978334250,
                    'height': -6351285846684400285,
                    'ratio_x': 6936009388924601123,
                    'ratio_y': 3969677946875196589,
                },
                {
                    'nw_x_pixel': 1936230395,
                    'nw_y_pixel': 1845826487,
                    'width': -150418963320255113,
                    'height': -4880500742777611422,
                    'ratio_x': 7944401474669284950,
                    'ratio_y': 4699817622671496077,
                },
                {
                    'nw_x_pixel': 885852218,
                    'nw_y_pixel': 1956645958,
                    'width': -3521324820385295486,
                    'height': -6116099899606254937,
                    'ratio_x': -4768408655129741984,
                    'ratio_y': -3448434202290339717,
                },
                {
                    'nw_x_pixel': -1809658204,
                    'nw_y_pixel': 462164526,
                    'width': -8243699479519824818,
                    'height': -3860366487569733145,
                    'ratio_x': -7475671265002908840,
                    'ratio_y': -5172919705459469276,
                },
                {
                    'nw_x_pixel': -834821840,
                    'nw_y_pixel': -1911581879,
                    'width': -1243629179459305960,
                    'height': -9157433664009704972,
                    'ratio_x': 1752735537865770409,
                    'ratio_y': -6766873683172957715,
                },
                {
                    'nw_x_pixel': -1746573320,
                    'nw_y_pixel': 264405226,
                    'width': -101199057863539815,
                    'height': -4971613143349911873,
                    'ratio_x': 4542488186803927560,
                    'ratio_y': -7222717436787890873,
                },
                {
                    'nw_x_pixel': -1685483959,
                    'nw_y_pixel': -1944487072,
                    'width': -6950555258545670984,
                    'height': -3589988300632422750,
                    'ratio_x': 8297436347681975093,
                    'ratio_y': 1778034447218713093,
                },
                {
                    'nw_x_pixel': 568532174,
                    'nw_y_pixel': 1227577267,
                    'width': -6659192797713879159,
                    'height': -8270228213865482038,
                    'ratio_x': -6841810306535685065,
                    'ratio_y': -6463175472413307258,
                },
                {
                    'nw_x_pixel': 1088569349,
                    'nw_y_pixel': 957460593,
                    'width': -2352062652357698532,
                    'height': -5183329286298416206,
                    'ratio_x': -6393443410399200518,
                    'ratio_y': 8090754120194892068,
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
                    'description': 'пĈԪŬŰθǈӷɰеӏë{ǚЫIʯƼiǠŢʰţӪóғƱĲƛȱ',
                    'monitors': [
                            {
                                        'identifier': 2781135,
                                        'width': -8511932943391134775,
                                        'height': 5831909515581967854,
                                    },
                            {
                                        'identifier': 6709224,
                                        'width': -4234496056141231119,
                                        'height': 8634549041232617381,
                                    },
                            {
                                        'identifier': 4019962,
                                        'width': -5679520962722254237,
                                        'height': 1440538433168553066,
                                    },
                            {
                                        'identifier': 7350180,
                                        'width': 4686129918758094750,
                                        'height': 7856597580329309466,
                                    },
                            {
                                        'identifier': -554307,
                                        'width': 2018346532969979634,
                                        'height': -1970540837518491390,
                                    },
                            {
                                        'identifier': -784696,
                                        'width': -3701031101709130723,
                                        'height': -7100341467907428850,
                                    },
                            {
                                        'identifier': 4331977,
                                        'width': -2195084812415095743,
                                        'height': 7334342152941123021,
                                    },
                            {
                                        'identifier': 8678310,
                                        'width': -7498811660347757231,
                                        'height': -930838979851948043,
                                    },
                            {
                                        'identifier': 2611163,
                                        'width': 1386465600378392620,
                                        'height': -7651939284580791137,
                                    },
                            {
                                        'identifier': -392408,
                                        'width': -3904730884509967486,
                                        'height': -2969378652713871755,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -835458,
                                        'source_nw_x_pixel': -684768109934241273,
                                        'source_nw_y_pixel': -5829497056357467461,
                                        'source_pixel_width': -8062687178031770318,
                                        'source_pixel_height': -3419926252257298832,
                                        'rotation': -3570539952714662587,
                                        'virtual_nw_x_pixel': -1674005933,
                                        'virtual_nw_y_pixel': 1671654516,
                                        'virtual_width': -1529226465,
                                        'virtual_height': 245913345,
                                    },
                            {
                                        'source_monitor': 8357374,
                                        'source_nw_x_pixel': -1343674043483495663,
                                        'source_nw_y_pixel': -6749455075156063689,
                                        'source_pixel_width': -8451892626609684185,
                                        'source_pixel_height': -6877143440365282656,
                                        'rotation': -5169282549326355097,
                                        'virtual_nw_x_pixel': -713253220,
                                        'virtual_nw_y_pixel': 451286167,
                                        'virtual_width': 830969936,
                                        'virtual_height': 280459500,
                                    },
                            {
                                        'source_monitor': -282800,
                                        'source_nw_x_pixel': -8983174874392857532,
                                        'source_nw_y_pixel': -8495317927368238574,
                                        'source_pixel_width': -4222995165975045101,
                                        'source_pixel_height': -5970346253281101702,
                                        'rotation': -1146134514174946332,
                                        'virtual_nw_x_pixel': -1012705174,
                                        'virtual_nw_y_pixel': 230954135,
                                        'virtual_width': 1655989929,
                                        'virtual_height': -1014827330,
                                    },
                            {
                                        'source_monitor': 4014534,
                                        'source_nw_x_pixel': -4318414829612913082,
                                        'source_nw_y_pixel': -4730783676820254293,
                                        'source_pixel_width': -2651321057328348108,
                                        'source_pixel_height': -3382006403078632131,
                                        'rotation': -3725701769236193191,
                                        'virtual_nw_x_pixel': -300878401,
                                        'virtual_nw_y_pixel': -546530320,
                                        'virtual_width': -844863636,
                                        'virtual_height': 933330397,
                                    },
                            {
                                        'source_monitor': 5086938,
                                        'source_nw_x_pixel': -377445769209277480,
                                        'source_nw_y_pixel': -588827021911428186,
                                        'source_pixel_width': -8727803954620737973,
                                        'source_pixel_height': -1532402628855963869,
                                        'rotation': -2134571382696301149,
                                        'virtual_nw_x_pixel': 1190283180,
                                        'virtual_nw_y_pixel': 911945333,
                                        'virtual_width': 1418411843,
                                        'virtual_height': 999607946,
                                    },
                            {
                                        'source_monitor': 6231151,
                                        'source_nw_x_pixel': -1079887223530409468,
                                        'source_nw_y_pixel': -7922523598696983287,
                                        'source_pixel_width': -9052468354483912488,
                                        'source_pixel_height': -6684915768749568793,
                                        'rotation': -416977405516398074,
                                        'virtual_nw_x_pixel': 1646257323,
                                        'virtual_nw_y_pixel': -1093394642,
                                        'virtual_width': -1845887901,
                                        'virtual_height': 1332659708,
                                    },
                            {
                                        'source_monitor': 5936787,
                                        'source_nw_x_pixel': -8006633968818675165,
                                        'source_nw_y_pixel': -9011393526501425387,
                                        'source_pixel_width': -582756705906663906,
                                        'source_pixel_height': -6281645495660080122,
                                        'rotation': -2164017370770888862,
                                        'virtual_nw_x_pixel': 1145574400,
                                        'virtual_nw_y_pixel': 773200947,
                                        'virtual_width': 1898221272,
                                        'virtual_height': -1007337575,
                                    },
                            {
                                        'source_monitor': 7256398,
                                        'source_nw_x_pixel': -5300775478919058431,
                                        'source_nw_y_pixel': -6331988222713478912,
                                        'source_pixel_width': -8258295215181911266,
                                        'source_pixel_height': -6838039935765985564,
                                        'rotation': -3559961322770735495,
                                        'virtual_nw_x_pixel': -1819435890,
                                        'virtual_nw_y_pixel': 1831422583,
                                        'virtual_width': -164336164,
                                        'virtual_height': -33682266,
                                    },
                            {
                                        'source_monitor': 1315450,
                                        'source_nw_x_pixel': -4160630608901886699,
                                        'source_nw_y_pixel': -8374652891062461490,
                                        'source_pixel_width': -3619497037163100358,
                                        'source_pixel_height': -6748080497484819073,
                                        'rotation': -664767573369788364,
                                        'virtual_nw_x_pixel': 72428038,
                                        'virtual_nw_y_pixel': -1985051019,
                                        'virtual_width': -1738757522,
                                        'virtual_height': 1350615458,
                                    },
                            {
                                        'source_monitor': 199706,
                                        'source_nw_x_pixel': -7889453407948503313,
                                        'source_nw_y_pixel': -8067918550235552597,
                                        'source_pixel_width': -7552418402709810804,
                                        'source_pixel_height': -5956319590616673488,
                                        'rotation': -1049843160617368191,
                                        'virtual_nw_x_pixel': 1900738739,
                                        'virtual_nw_y_pixel': -1320157530,
                                        'virtual_width': -160221927,
                                        'virtual_height': -481132441,
                                    },
                        ],
                },
                {
                    'description': '˳ӉͿӿϽɧǑͱ\x9b\x99ҩSЍ_Ң\x82ɤeĞԞĜӾǽԨɋɢӳҭÌЩ',
                    'monitors': [
                            {
                                        'identifier': 8611006,
                                        'width': 1983545371541316774,
                                        'height': 6823268729196855178,
                                    },
                            {
                                        'identifier': 9587687,
                                        'width': 1277728121299329804,
                                        'height': 4733702754902656234,
                                    },
                            {
                                        'identifier': 8660470,
                                        'width': 247025161186755341,
                                        'height': 3093698974970286580,
                                    },
                            {
                                        'identifier': 3818717,
                                        'width': -5102543434564240832,
                                        'height': -1315684531529720562,
                                    },
                            {
                                        'identifier': -110976,
                                        'width': 1189785082567539979,
                                        'height': -6013197728731363922,
                                    },
                            {
                                        'identifier': 9798073,
                                        'width': 3288952815152100696,
                                        'height': -1444566870058550092,
                                    },
                            {
                                        'identifier': 7206072,
                                        'width': 275858290077498863,
                                        'height': 5539451965921283940,
                                    },
                            {
                                        'identifier': 8380546,
                                        'width': -4514487996993842833,
                                        'height': 3521868651298924716,
                                    },
                            {
                                        'identifier': 2510041,
                                        'width': 6298936741139940699,
                                        'height': -9205068824955067684,
                                    },
                            {
                                        'identifier': 327096,
                                        'width': -96046808748137161,
                                        'height': -7033749853902532195,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6358877,
                                        'source_nw_x_pixel': -2804546434273840470,
                                        'source_nw_y_pixel': -4319095677331549219,
                                        'source_pixel_width': -9179304600784610352,
                                        'source_pixel_height': -8915354344438501857,
                                        'rotation': -2519517667928598678,
                                        'virtual_nw_x_pixel': -1291162917,
                                        'virtual_nw_y_pixel': -1416196161,
                                        'virtual_width': -1248015503,
                                        'virtual_height': 1771034599,
                                    },
                            {
                                        'source_monitor': 7344672,
                                        'source_nw_x_pixel': -1090153133329486533,
                                        'source_nw_y_pixel': -8949259895170842988,
                                        'source_pixel_width': -5316002899989526126,
                                        'source_pixel_height': -498914312478307981,
                                        'rotation': -863005883680212809,
                                        'virtual_nw_x_pixel': 1260700560,
                                        'virtual_nw_y_pixel': -1434364009,
                                        'virtual_width': 283357126,
                                        'virtual_height': 1723428033,
                                    },
                            {
                                        'source_monitor': 5785084,
                                        'source_nw_x_pixel': -5814914193279165194,
                                        'source_nw_y_pixel': -2585673667048925628,
                                        'source_pixel_width': -792284954935217096,
                                        'source_pixel_height': -898779881009406429,
                                        'rotation': -8297301628380226541,
                                        'virtual_nw_x_pixel': -1504088583,
                                        'virtual_nw_y_pixel': 1133872355,
                                        'virtual_width': 643045070,
                                        'virtual_height': -734164849,
                                    },
                            {
                                        'source_monitor': 4638459,
                                        'source_nw_x_pixel': -2350613591292517991,
                                        'source_nw_y_pixel': -9078714616445296732,
                                        'source_pixel_width': -2884963673833113994,
                                        'source_pixel_height': -1073738549225680163,
                                        'rotation': -7379663267200812271,
                                        'virtual_nw_x_pixel': 986015632,
                                        'virtual_nw_y_pixel': -690106821,
                                        'virtual_width': -286445064,
                                        'virtual_height': 1527353994,
                                    },
                            {
                                        'source_monitor': 6345041,
                                        'source_nw_x_pixel': -5677187737639013539,
                                        'source_nw_y_pixel': -2451497785293495926,
                                        'source_pixel_width': -2846748066591272859,
                                        'source_pixel_height': -7546136242188253220,
                                        'rotation': -6575817328051155096,
                                        'virtual_nw_x_pixel': -1888096163,
                                        'virtual_nw_y_pixel': -683544326,
                                        'virtual_width': 156156540,
                                        'virtual_height': 1673234165,
                                    },
                            {
                                        'source_monitor': 8216581,
                                        'source_nw_x_pixel': -4749447322371707949,
                                        'source_nw_y_pixel': -6235580497264791249,
                                        'source_pixel_width': -6869025124725877258,
                                        'source_pixel_height': -320329835191155112,
                                        'rotation': -2505736277239665804,
                                        'virtual_nw_x_pixel': 1745158968,
                                        'virtual_nw_y_pixel': 948824884,
                                        'virtual_width': 1425908746,
                                        'virtual_height': 883269329,
                                    },
                            {
                                        'source_monitor': 2592361,
                                        'source_nw_x_pixel': -6802196010069700532,
                                        'source_nw_y_pixel': -6394796148284830483,
                                        'source_pixel_width': -7325814545290405986,
                                        'source_pixel_height': -5070813491774768118,
                                        'rotation': -2977887207537335228,
                                        'virtual_nw_x_pixel': -1971787988,
                                        'virtual_nw_y_pixel': -1358985514,
                                        'virtual_width': -1173260837,
                                        'virtual_height': 460256658,
                                    },
                            {
                                        'source_monitor': 2462069,
                                        'source_nw_x_pixel': -1850783690119703870,
                                        'source_nw_y_pixel': -9132407727086333160,
                                        'source_pixel_width': -4577401410343366304,
                                        'source_pixel_height': -3400216215175379992,
                                        'rotation': -7770996322284841585,
                                        'virtual_nw_x_pixel': -718445139,
                                        'virtual_nw_y_pixel': -627234980,
                                        'virtual_width': -867904729,
                                        'virtual_height': 1197922302,
                                    },
                            {
                                        'source_monitor': 418902,
                                        'source_nw_x_pixel': -759437190863918212,
                                        'source_nw_y_pixel': -8673795455122652375,
                                        'source_pixel_width': -3729714196027240638,
                                        'source_pixel_height': -7048973166274797681,
                                        'rotation': -10278679684690342,
                                        'virtual_nw_x_pixel': 215718490,
                                        'virtual_nw_y_pixel': -1564754569,
                                        'virtual_width': 966490284,
                                        'virtual_height': 1703673474,
                                    },
                            {
                                        'source_monitor': 4953638,
                                        'source_nw_x_pixel': -1069819032817415595,
                                        'source_nw_y_pixel': -4409167184331137429,
                                        'source_pixel_width': -5964704972190976654,
                                        'source_pixel_height': -3410366000004155516,
                                        'rotation': -1552168629689484195,
                                        'virtual_nw_x_pixel': 1288033701,
                                        'virtual_nw_y_pixel': 829860243,
                                        'virtual_width': -1577765252,
                                        'virtual_height': -301864849,
                                    },
                        ],
                },
                {
                    'description': 'ĘȪşԢ)Ɨ˻ИǸsʸȽ;λœɵЭϋǲʔƹºưEӊÉхǶӻɕ',
                    'monitors': [
                            {
                                        'identifier': 5722824,
                                        'width': 6132188790189556242,
                                        'height': 7170257489379023246,
                                    },
                            {
                                        'identifier': 2140131,
                                        'width': 7744333224747450129,
                                        'height': -5743566775804867061,
                                    },
                            {
                                        'identifier': 7455167,
                                        'width': -5401812874864615683,
                                        'height': 488709970323139386,
                                    },
                            {
                                        'identifier': 8647715,
                                        'width': 6540079155843154719,
                                        'height': -6113570639125365277,
                                    },
                            {
                                        'identifier': 9250832,
                                        'width': -8860240212449100032,
                                        'height': 837288586177634007,
                                    },
                            {
                                        'identifier': 4946565,
                                        'width': 1184716576392283481,
                                        'height': -6478983354298699296,
                                    },
                            {
                                        'identifier': 4977594,
                                        'width': -2743839200815685993,
                                        'height': -7960888206893788027,
                                    },
                            {
                                        'identifier': 5742984,
                                        'width': 1052975170340832304,
                                        'height': 4685469794426045367,
                                    },
                            {
                                        'identifier': 2845073,
                                        'width': -9034862286502189479,
                                        'height': 5043678303365173940,
                                    },
                            {
                                        'identifier': -923870,
                                        'width': 8934208551760122038,
                                        'height': -6091877868838576598,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9572379,
                                        'source_nw_x_pixel': -7929246565290116979,
                                        'source_nw_y_pixel': -24201800410471294,
                                        'source_pixel_width': -2229241569335208593,
                                        'source_pixel_height': -373767359646493091,
                                        'rotation': -4649285757292483106,
                                        'virtual_nw_x_pixel': -635985653,
                                        'virtual_nw_y_pixel': -1126254362,
                                        'virtual_width': -1084456417,
                                        'virtual_height': -1344056908,
                                    },
                            {
                                        'source_monitor': 9891386,
                                        'source_nw_x_pixel': -4907315441477718381,
                                        'source_nw_y_pixel': -4545790980214822311,
                                        'source_pixel_width': -1282508282969015763,
                                        'source_pixel_height': -5497796863279207316,
                                        'rotation': -5111690604688365346,
                                        'virtual_nw_x_pixel': 795264060,
                                        'virtual_nw_y_pixel': -1643028150,
                                        'virtual_width': -914116327,
                                        'virtual_height': -226406276,
                                    },
                            {
                                        'source_monitor': 58678,
                                        'source_nw_x_pixel': -5585716432815416555,
                                        'source_nw_y_pixel': -6351710033810303963,
                                        'source_pixel_width': -8527412668981559941,
                                        'source_pixel_height': -733762146478849753,
                                        'rotation': -292953884923274533,
                                        'virtual_nw_x_pixel': 997815811,
                                        'virtual_nw_y_pixel': -1797266694,
                                        'virtual_width': 200826962,
                                        'virtual_height': 370535054,
                                    },
                            {
                                        'source_monitor': 5226676,
                                        'source_nw_x_pixel': -127795559447801715,
                                        'source_nw_y_pixel': -88818055713710508,
                                        'source_pixel_width': -7258910227303516871,
                                        'source_pixel_height': -7374584999628756978,
                                        'rotation': -8009352483076374407,
                                        'virtual_nw_x_pixel': 875327385,
                                        'virtual_nw_y_pixel': 198594768,
                                        'virtual_width': 1674495419,
                                        'virtual_height': -198494293,
                                    },
                            {
                                        'source_monitor': 6549815,
                                        'source_nw_x_pixel': -7633240565428003902,
                                        'source_nw_y_pixel': -3240244516580085484,
                                        'source_pixel_width': -5116893352619521466,
                                        'source_pixel_height': -1677100729392033084,
                                        'rotation': -1430726206047537653,
                                        'virtual_nw_x_pixel': -1600135741,
                                        'virtual_nw_y_pixel': 930559119,
                                        'virtual_width': 1803009118,
                                        'virtual_height': -1529958784,
                                    },
                            {
                                        'source_monitor': 2655638,
                                        'source_nw_x_pixel': -555732219406056215,
                                        'source_nw_y_pixel': -938377609551455514,
                                        'source_pixel_width': -4151365749184753043,
                                        'source_pixel_height': -6640689736400503027,
                                        'rotation': -6025610381579888903,
                                        'virtual_nw_x_pixel': 397471153,
                                        'virtual_nw_y_pixel': 1950149980,
                                        'virtual_width': 1437167041,
                                        'virtual_height': 1662518724,
                                    },
                            {
                                        'source_monitor': 8513791,
                                        'source_nw_x_pixel': -5454933745826320452,
                                        'source_nw_y_pixel': -7572297421478663061,
                                        'source_pixel_width': -7441977597705512250,
                                        'source_pixel_height': -2775303969743848950,
                                        'rotation': -7245166204658969138,
                                        'virtual_nw_x_pixel': -1913660833,
                                        'virtual_nw_y_pixel': -825937123,
                                        'virtual_width': 352715562,
                                        'virtual_height': -1132435971,
                                    },
                            {
                                        'source_monitor': 1095398,
                                        'source_nw_x_pixel': -8078128735111111164,
                                        'source_nw_y_pixel': -5852677023870999232,
                                        'source_pixel_width': -1797768946582564394,
                                        'source_pixel_height': -7361008270351456104,
                                        'rotation': -5045403691255605108,
                                        'virtual_nw_x_pixel': 397385526,
                                        'virtual_nw_y_pixel': 115142119,
                                        'virtual_width': -473713921,
                                        'virtual_height': -1526646643,
                                    },
                            {
                                        'source_monitor': 4611889,
                                        'source_nw_x_pixel': -8953844478563496026,
                                        'source_nw_y_pixel': -5543846536345412161,
                                        'source_pixel_width': -3137938773378902457,
                                        'source_pixel_height': -4624241053083520667,
                                        'rotation': -1249399152580619927,
                                        'virtual_nw_x_pixel': -479475727,
                                        'virtual_nw_y_pixel': 1806610516,
                                        'virtual_width': 1669366280,
                                        'virtual_height': 674173964,
                                    },
                            {
                                        'source_monitor': 8171885,
                                        'source_nw_x_pixel': -8710670171806364848,
                                        'source_nw_y_pixel': -6769063856883568349,
                                        'source_pixel_width': -6204116648153110060,
                                        'source_pixel_height': -7587201648471905090,
                                        'rotation': -8370473325677840722,
                                        'virtual_nw_x_pixel': -1810333579,
                                        'virtual_nw_y_pixel': 739464731,
                                        'virtual_width': 1554023484,
                                        'virtual_height': 1964815013,
                                    },
                        ],
                },
                {
                    'description': 'ižΚҁэƥʯԠɍԖʻ°ȏ¯ȗͷɌʆВӶ¸ƘS.ȾŨθQΛя',
                    'monitors': [
                            {
                                        'identifier': 828489,
                                        'width': 781194926915487013,
                                        'height': -4311023693764760616,
                                    },
                            {
                                        'identifier': 7312378,
                                        'width': -654605949186140133,
                                        'height': -96515569388046559,
                                    },
                            {
                                        'identifier': 1652917,
                                        'width': 7353863173845418352,
                                        'height': -5239586069932950350,
                                    },
                            {
                                        'identifier': 6670692,
                                        'width': -4018605394818705117,
                                        'height': -3866783082585198397,
                                    },
                            {
                                        'identifier': 6641392,
                                        'width': 5000857545192365299,
                                        'height': -5781139782948343951,
                                    },
                            {
                                        'identifier': 635570,
                                        'width': -8651158963881326554,
                                        'height': -3296078156738047422,
                                    },
                            {
                                        'identifier': 3903541,
                                        'width': -3847475661209068428,
                                        'height': -5440310882147949238,
                                    },
                            {
                                        'identifier': 7865686,
                                        'width': -4737270123309113560,
                                        'height': 8166684394110708485,
                                    },
                            {
                                        'identifier': 1136825,
                                        'width': 5696187937545871698,
                                        'height': 8029500495348673809,
                                    },
                            {
                                        'identifier': 5850037,
                                        'width': -6149824018370426279,
                                        'height': -2870681546150710836,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5504215,
                                        'source_nw_x_pixel': -2793677525069803304,
                                        'source_nw_y_pixel': -2012092073017275800,
                                        'source_pixel_width': -1407789630494051548,
                                        'source_pixel_height': -315957427788801586,
                                        'rotation': -5849864112764966887,
                                        'virtual_nw_x_pixel': -799120310,
                                        'virtual_nw_y_pixel': 556740922,
                                        'virtual_width': -1129603820,
                                        'virtual_height': 1775267171,
                                    },
                            {
                                        'source_monitor': 4397279,
                                        'source_nw_x_pixel': -8702141846874659706,
                                        'source_nw_y_pixel': -2478760742780756292,
                                        'source_pixel_width': -6739901700804544020,
                                        'source_pixel_height': -4369591311632732479,
                                        'rotation': -291505287523301936,
                                        'virtual_nw_x_pixel': -1629400931,
                                        'virtual_nw_y_pixel': -210714133,
                                        'virtual_width': 403655502,
                                        'virtual_height': -696148980,
                                    },
                            {
                                        'source_monitor': 7979938,
                                        'source_nw_x_pixel': -2364940013721734794,
                                        'source_nw_y_pixel': -1332557360575719244,
                                        'source_pixel_width': -1244189044966892567,
                                        'source_pixel_height': -3287443486672637218,
                                        'rotation': -714474640647090804,
                                        'virtual_nw_x_pixel': -1335541303,
                                        'virtual_nw_y_pixel': -1801917395,
                                        'virtual_width': 896643605,
                                        'virtual_height': -1540881875,
                                    },
                            {
                                        'source_monitor': 903251,
                                        'source_nw_x_pixel': -644411952582909806,
                                        'source_nw_y_pixel': -6482252477278256683,
                                        'source_pixel_width': -7977499155821203431,
                                        'source_pixel_height': -1641024901025253707,
                                        'rotation': -7884071621171024058,
                                        'virtual_nw_x_pixel': -1685001757,
                                        'virtual_nw_y_pixel': -1927884413,
                                        'virtual_width': 1369470745,
                                        'virtual_height': -1408524429,
                                    },
                            {
                                        'source_monitor': 3741888,
                                        'source_nw_x_pixel': -8758135720026477902,
                                        'source_nw_y_pixel': -3023540270939785061,
                                        'source_pixel_width': -4272363119434650867,
                                        'source_pixel_height': -2668570979505639208,
                                        'rotation': -7379988242424090972,
                                        'virtual_nw_x_pixel': 521342507,
                                        'virtual_nw_y_pixel': -1742147281,
                                        'virtual_width': 1029215941,
                                        'virtual_height': -1364840061,
                                    },
                            {
                                        'source_monitor': 1099806,
                                        'source_nw_x_pixel': -1674300976152350268,
                                        'source_nw_y_pixel': -2539547812533045690,
                                        'source_pixel_width': -5427279609936937462,
                                        'source_pixel_height': -1435339098253993563,
                                        'rotation': -7233007046409120137,
                                        'virtual_nw_x_pixel': 892159975,
                                        'virtual_nw_y_pixel': -1806237297,
                                        'virtual_width': 1164497549,
                                        'virtual_height': 1305100122,
                                    },
                            {
                                        'source_monitor': 8076430,
                                        'source_nw_x_pixel': -1286609354804591380,
                                        'source_nw_y_pixel': -4235984734325439917,
                                        'source_pixel_width': -770104922070799718,
                                        'source_pixel_height': -7405709035661578667,
                                        'rotation': -7595327235817245505,
                                        'virtual_nw_x_pixel': -1053782521,
                                        'virtual_nw_y_pixel': -1615778613,
                                        'virtual_width': 1653996750,
                                        'virtual_height': 1686479614,
                                    },
                            {
                                        'source_monitor': 4696748,
                                        'source_nw_x_pixel': -353673092880508434,
                                        'source_nw_y_pixel': -1586713044119610748,
                                        'source_pixel_width': -7356251885977194373,
                                        'source_pixel_height': -6186216002475396630,
                                        'rotation': -5533591802681121283,
                                        'virtual_nw_x_pixel': -666516932,
                                        'virtual_nw_y_pixel': 196701083,
                                        'virtual_width': 1502297998,
                                        'virtual_height': -789273907,
                                    },
                            {
                                        'source_monitor': 1287672,
                                        'source_nw_x_pixel': -3485527655759994017,
                                        'source_nw_y_pixel': -6459014624561723482,
                                        'source_pixel_width': -351157466090070180,
                                        'source_pixel_height': -6912257883600624502,
                                        'rotation': -3610951134684678373,
                                        'virtual_nw_x_pixel': 1404695790,
                                        'virtual_nw_y_pixel': 1697123072,
                                        'virtual_width': 1550837476,
                                        'virtual_height': 1291080252,
                                    },
                            {
                                        'source_monitor': 3654273,
                                        'source_nw_x_pixel': -5615997212224558779,
                                        'source_nw_y_pixel': -8376300955651274200,
                                        'source_pixel_width': -3767344717695994717,
                                        'source_pixel_height': -8021565910384878469,
                                        'rotation': -2663447702186789391,
                                        'virtual_nw_x_pixel': 281315490,
                                        'virtual_nw_y_pixel': 39829712,
                                        'virtual_width': 1669506105,
                                        'virtual_height': 845316356,
                                    },
                        ],
                },
                {
                    'description': 'ɈñʗжӽKŶӕң˻ˁŶØçǃÆ҃żįĸʮɷʖ7êɑƅĄӼƣ',
                    'monitors': [
                            {
                                        'identifier': 8470143,
                                        'width': 9124516878113320021,
                                        'height': -3824163592414086046,
                                    },
                            {
                                        'identifier': 7685121,
                                        'width': 8445758039399723257,
                                        'height': -5484656508460015987,
                                    },
                            {
                                        'identifier': 1498947,
                                        'width': 1701003740506431911,
                                        'height': 7978072071947907182,
                                    },
                            {
                                        'identifier': 6889849,
                                        'width': 5869563602611470520,
                                        'height': 7033468698834976971,
                                    },
                            {
                                        'identifier': -878689,
                                        'width': 5251419067531929856,
                                        'height': 1541836754819414144,
                                    },
                            {
                                        'identifier': 7196831,
                                        'width': 2840453805562821460,
                                        'height': -6742557574850249022,
                                    },
                            {
                                        'identifier': 9844169,
                                        'width': 2750295113038698789,
                                        'height': -7611819829196598128,
                                    },
                            {
                                        'identifier': 4756836,
                                        'width': -8761753836409805988,
                                        'height': 4730796541331817068,
                                    },
                            {
                                        'identifier': 2320548,
                                        'width': -4749490337160964208,
                                        'height': 7273651119491242872,
                                    },
                            {
                                        'identifier': 3398657,
                                        'width': -3769368848747551541,
                                        'height': -3631563068242233046,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3246465,
                                        'source_nw_x_pixel': -3481447213166805387,
                                        'source_nw_y_pixel': -555380716349815816,
                                        'source_pixel_width': -5149208047398593579,
                                        'source_pixel_height': -7043811890170595369,
                                        'rotation': -1130129340456272057,
                                        'virtual_nw_x_pixel': -1955538755,
                                        'virtual_nw_y_pixel': 302380969,
                                        'virtual_width': -1354263170,
                                        'virtual_height': -604153198,
                                    },
                            {
                                        'source_monitor': 1299474,
                                        'source_nw_x_pixel': -5628743257401695813,
                                        'source_nw_y_pixel': -4699602622030320833,
                                        'source_pixel_width': -476620539399748028,
                                        'source_pixel_height': -3826200621018915821,
                                        'rotation': -897223259851594311,
                                        'virtual_nw_x_pixel': 1688690060,
                                        'virtual_nw_y_pixel': -689539824,
                                        'virtual_width': 1703399526,
                                        'virtual_height': -1034271964,
                                    },
                            {
                                        'source_monitor': 6598343,
                                        'source_nw_x_pixel': -360672090474944694,
                                        'source_nw_y_pixel': -7269509498109391562,
                                        'source_pixel_width': -4737470528262079782,
                                        'source_pixel_height': -7886582917290351841,
                                        'rotation': -8141024364022338250,
                                        'virtual_nw_x_pixel': -965401971,
                                        'virtual_nw_y_pixel': 358834381,
                                        'virtual_width': -593304071,
                                        'virtual_height': -160179956,
                                    },
                            {
                                        'source_monitor': 9837774,
                                        'source_nw_x_pixel': -5443454269098378467,
                                        'source_nw_y_pixel': -8873731875737466696,
                                        'source_pixel_width': -7208040174774275849,
                                        'source_pixel_height': -2317948582553921631,
                                        'rotation': -5925046280002750836,
                                        'virtual_nw_x_pixel': -1055866691,
                                        'virtual_nw_y_pixel': -1320474082,
                                        'virtual_width': 1729311938,
                                        'virtual_height': -402241971,
                                    },
                            {
                                        'source_monitor': -590956,
                                        'source_nw_x_pixel': -1953354156434598088,
                                        'source_nw_y_pixel': -6141356650495557390,
                                        'source_pixel_width': -8873336231519127854,
                                        'source_pixel_height': -3410948364151260110,
                                        'rotation': -8725634546012916701,
                                        'virtual_nw_x_pixel': -965051957,
                                        'virtual_nw_y_pixel': -981171361,
                                        'virtual_width': 1466012763,
                                        'virtual_height': -1940090457,
                                    },
                            {
                                        'source_monitor': 7641703,
                                        'source_nw_x_pixel': -5576862573269188121,
                                        'source_nw_y_pixel': -2364336949304441364,
                                        'source_pixel_width': -2010539495265217796,
                                        'source_pixel_height': -6036259645162381197,
                                        'rotation': -3482219052410534713,
                                        'virtual_nw_x_pixel': -113659263,
                                        'virtual_nw_y_pixel': 297248040,
                                        'virtual_width': 58600812,
                                        'virtual_height': -612690423,
                                    },
                            {
                                        'source_monitor': 727194,
                                        'source_nw_x_pixel': -4912295242846904078,
                                        'source_nw_y_pixel': -5718581109808743678,
                                        'source_pixel_width': -8700257157378898181,
                                        'source_pixel_height': -4888668866671845952,
                                        'rotation': -7735953148953618691,
                                        'virtual_nw_x_pixel': 1002566793,
                                        'virtual_nw_y_pixel': -397422117,
                                        'virtual_width': -143235864,
                                        'virtual_height': 1610421937,
                                    },
                            {
                                        'source_monitor': 1333268,
                                        'source_nw_x_pixel': -7773603446619208613,
                                        'source_nw_y_pixel': -3191811172330839349,
                                        'source_pixel_width': -8430567387412578299,
                                        'source_pixel_height': -4252845158028685055,
                                        'rotation': -4019235834664961400,
                                        'virtual_nw_x_pixel': -1370372085,
                                        'virtual_nw_y_pixel': -1263171962,
                                        'virtual_width': -990989899,
                                        'virtual_height': -1594565335,
                                    },
                            {
                                        'source_monitor': 6404449,
                                        'source_nw_x_pixel': -8013385016772646159,
                                        'source_nw_y_pixel': -8782297889407831009,
                                        'source_pixel_width': -4629863000114628887,
                                        'source_pixel_height': -7301794051264715506,
                                        'rotation': -2292591970713009756,
                                        'virtual_nw_x_pixel': -1430309375,
                                        'virtual_nw_y_pixel': -235333867,
                                        'virtual_width': 604753550,
                                        'virtual_height': 1285179648,
                                    },
                            {
                                        'source_monitor': 8536147,
                                        'source_nw_x_pixel': -7842114212211093994,
                                        'source_nw_y_pixel': -1318354773913611817,
                                        'source_pixel_width': -5568860000837376406,
                                        'source_pixel_height': -3768286495267317889,
                                        'rotation': -8590366375076949668,
                                        'virtual_nw_x_pixel': -755000287,
                                        'virtual_nw_y_pixel': -479928807,
                                        'virtual_width': 1605387486,
                                        'virtual_height': -864036973,
                                    },
                        ],
                },
                {
                    'description': 'ѝƳ,ʠɃÏӑɓɳЀʺҺFєљƵǝϫ˸ĝԪȀđҳɑòωc˂Ӳ',
                    'monitors': [
                            {
                                        'identifier': 130863,
                                        'width': -7995267531186075234,
                                        'height': -5193063789106138285,
                                    },
                            {
                                        'identifier': -660999,
                                        'width': 3377203581556156533,
                                        'height': 6445424150416191022,
                                    },
                            {
                                        'identifier': 9915744,
                                        'width': -7192908558951914802,
                                        'height': -1231200576253246830,
                                    },
                            {
                                        'identifier': 4354260,
                                        'width': 8253424973945858931,
                                        'height': -6575794861755174219,
                                    },
                            {
                                        'identifier': 1435811,
                                        'width': -5313704190235875340,
                                        'height': 2630046109107712406,
                                    },
                            {
                                        'identifier': 2340944,
                                        'width': 4551068310416266833,
                                        'height': -4610639733229792115,
                                    },
                            {
                                        'identifier': 6268888,
                                        'width': 2389296035605867038,
                                        'height': -3535325182436080481,
                                    },
                            {
                                        'identifier': -820079,
                                        'width': 8997960682406552044,
                                        'height': -3545637592634297251,
                                    },
                            {
                                        'identifier': 7578331,
                                        'width': -1380226293722681866,
                                        'height': 6754769561300196942,
                                    },
                            {
                                        'identifier': 9842196,
                                        'width': -2086736402939887966,
                                        'height': -5817551546266682443,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5268835,
                                        'source_nw_x_pixel': -3340707362568690926,
                                        'source_nw_y_pixel': -4802307956635120518,
                                        'source_pixel_width': -2485399694802209500,
                                        'source_pixel_height': -3138861135352534331,
                                        'rotation': -4912891701691023964,
                                        'virtual_nw_x_pixel': -1763600979,
                                        'virtual_nw_y_pixel': 1851044480,
                                        'virtual_width': 1670116706,
                                        'virtual_height': -1525231702,
                                    },
                            {
                                        'source_monitor': 6271285,
                                        'source_nw_x_pixel': -7831216951705983944,
                                        'source_nw_y_pixel': -6843020063834506700,
                                        'source_pixel_width': -3134662675519942952,
                                        'source_pixel_height': -5297626101391540760,
                                        'rotation': -5202988238619557634,
                                        'virtual_nw_x_pixel': 1362163231,
                                        'virtual_nw_y_pixel': 134272355,
                                        'virtual_width': -557492429,
                                        'virtual_height': -1021260670,
                                    },
                            {
                                        'source_monitor': 9012105,
                                        'source_nw_x_pixel': -8786966794259387614,
                                        'source_nw_y_pixel': -7252737639137580765,
                                        'source_pixel_width': -8275781578672497473,
                                        'source_pixel_height': -353040226365671568,
                                        'rotation': -7357228518145903462,
                                        'virtual_nw_x_pixel': 751584426,
                                        'virtual_nw_y_pixel': 867885839,
                                        'virtual_width': -1060452790,
                                        'virtual_height': 1431361040,
                                    },
                            {
                                        'source_monitor': 6690344,
                                        'source_nw_x_pixel': -650491212421691563,
                                        'source_nw_y_pixel': -4722377414415845658,
                                        'source_pixel_width': -6448948413274729879,
                                        'source_pixel_height': -5898364987878071720,
                                        'rotation': -8633768303252729382,
                                        'virtual_nw_x_pixel': 1393381181,
                                        'virtual_nw_y_pixel': 166767748,
                                        'virtual_width': -1948449488,
                                        'virtual_height': -266394293,
                                    },
                            {
                                        'source_monitor': 7644574,
                                        'source_nw_x_pixel': -4612474319989525095,
                                        'source_nw_y_pixel': -1493093708921923658,
                                        'source_pixel_width': -3342912905029298896,
                                        'source_pixel_height': -2826232894749283637,
                                        'rotation': -1417411005730506957,
                                        'virtual_nw_x_pixel': 1211280184,
                                        'virtual_nw_y_pixel': 1001268535,
                                        'virtual_width': 434081870,
                                        'virtual_height': 577813359,
                                    },
                            {
                                        'source_monitor': 9252994,
                                        'source_nw_x_pixel': -5717226185470591738,
                                        'source_nw_y_pixel': -6456484570948520965,
                                        'source_pixel_width': -3585299491974751756,
                                        'source_pixel_height': -6129130405743215547,
                                        'rotation': -6460330946843525917,
                                        'virtual_nw_x_pixel': 1133911020,
                                        'virtual_nw_y_pixel': -687078080,
                                        'virtual_width': 932868869,
                                        'virtual_height': 1771661370,
                                    },
                            {
                                        'source_monitor': 4168857,
                                        'source_nw_x_pixel': -5342441037670861465,
                                        'source_nw_y_pixel': -3207997811848275363,
                                        'source_pixel_width': -1751461164614008159,
                                        'source_pixel_height': -5231895031714393199,
                                        'rotation': -7046840076666860638,
                                        'virtual_nw_x_pixel': -1637744446,
                                        'virtual_nw_y_pixel': -1764446394,
                                        'virtual_width': 1963866122,
                                        'virtual_height': 1486980791,
                                    },
                            {
                                        'source_monitor': 8525152,
                                        'source_nw_x_pixel': -2831864601668981178,
                                        'source_nw_y_pixel': -7493807057159442070,
                                        'source_pixel_width': -3126715267215453052,
                                        'source_pixel_height': -4292685037756596463,
                                        'rotation': -3842356509405144442,
                                        'virtual_nw_x_pixel': 1230938056,
                                        'virtual_nw_y_pixel': -1783861114,
                                        'virtual_width': 814367374,
                                        'virtual_height': -1010906132,
                                    },
                            {
                                        'source_monitor': 9566832,
                                        'source_nw_x_pixel': -1803748477816793568,
                                        'source_nw_y_pixel': -6409629545306482738,
                                        'source_pixel_width': -471275404375684982,
                                        'source_pixel_height': -2287005385747635186,
                                        'rotation': -640805786358845745,
                                        'virtual_nw_x_pixel': -1082741374,
                                        'virtual_nw_y_pixel': 812822497,
                                        'virtual_width': -1515583037,
                                        'virtual_height': 1149967562,
                                    },
                            {
                                        'source_monitor': 5722107,
                                        'source_nw_x_pixel': -4502175680398268554,
                                        'source_nw_y_pixel': -2382665048220308487,
                                        'source_pixel_width': -3393709461612990619,
                                        'source_pixel_height': -5712915528920812332,
                                        'rotation': -2718315789332065457,
                                        'virtual_nw_x_pixel': 1337806021,
                                        'virtual_nw_y_pixel': -780307361,
                                        'virtual_width': 200375878,
                                        'virtual_height': -380517362,
                                    },
                        ],
                },
                {
                    'description': 'ŀď\x84ӐŭńǓÑļȪδʰïˋȷҔөāȝĝϣǃzˣВȶfнБG',
                    'monitors': [
                            {
                                        'identifier': 4419950,
                                        'width': -4124807128799057853,
                                        'height': -9099277812557183959,
                                    },
                            {
                                        'identifier': 6576085,
                                        'width': -1196473546319133600,
                                        'height': 874023125315745357,
                                    },
                            {
                                        'identifier': 7116004,
                                        'width': 5640646993541762361,
                                        'height': -3054225158228768139,
                                    },
                            {
                                        'identifier': 6066067,
                                        'width': -7226165404902775939,
                                        'height': -1823751359298805854,
                                    },
                            {
                                        'identifier': 3924568,
                                        'width': -6861188010669276475,
                                        'height': -807366193722645496,
                                    },
                            {
                                        'identifier': 1234920,
                                        'width': 8210378843202731987,
                                        'height': -2797626032674066905,
                                    },
                            {
                                        'identifier': 1082788,
                                        'width': 3014261163027487971,
                                        'height': -7856685298018724576,
                                    },
                            {
                                        'identifier': 8024081,
                                        'width': -1182859234188373442,
                                        'height': 4221283963555781538,
                                    },
                            {
                                        'identifier': 4547363,
                                        'width': 1817540395814686375,
                                        'height': -2228342510656026880,
                                    },
                            {
                                        'identifier': 9886900,
                                        'width': 5270588220830094835,
                                        'height': 4191149228680191028,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1279461,
                                        'source_nw_x_pixel': -1033065365733176134,
                                        'source_nw_y_pixel': -4355163825084833007,
                                        'source_pixel_width': -2764931886159550035,
                                        'source_pixel_height': -3181291845383764683,
                                        'rotation': -7956527738625036288,
                                        'virtual_nw_x_pixel': 383336210,
                                        'virtual_nw_y_pixel': -1306645489,
                                        'virtual_width': -754221936,
                                        'virtual_height': 1742287111,
                                    },
                            {
                                        'source_monitor': 5790018,
                                        'source_nw_x_pixel': -4351881238769055085,
                                        'source_nw_y_pixel': -4786158038713288621,
                                        'source_pixel_width': -5108583319987518569,
                                        'source_pixel_height': -4110040626716627690,
                                        'rotation': -5009404663875302151,
                                        'virtual_nw_x_pixel': -1474382523,
                                        'virtual_nw_y_pixel': 304070296,
                                        'virtual_width': 1163012426,
                                        'virtual_height': 1689297957,
                                    },
                            {
                                        'source_monitor': 2711918,
                                        'source_nw_x_pixel': -2733360658310695052,
                                        'source_nw_y_pixel': -8825832003425996533,
                                        'source_pixel_width': -5739216553873406059,
                                        'source_pixel_height': -5391658351652475216,
                                        'rotation': -374203264867650753,
                                        'virtual_nw_x_pixel': 653763918,
                                        'virtual_nw_y_pixel': 1526578308,
                                        'virtual_width': 653664083,
                                        'virtual_height': -286846402,
                                    },
                            {
                                        'source_monitor': 2700502,
                                        'source_nw_x_pixel': -2606796150406934920,
                                        'source_nw_y_pixel': -8198226809506657934,
                                        'source_pixel_width': -5700294490931807079,
                                        'source_pixel_height': -3216186345321054141,
                                        'rotation': -1881569332566642675,
                                        'virtual_nw_x_pixel': -1352884771,
                                        'virtual_nw_y_pixel': -37812790,
                                        'virtual_width': -485419905,
                                        'virtual_height': -409661663,
                                    },
                            {
                                        'source_monitor': 2362082,
                                        'source_nw_x_pixel': -6402194272628201236,
                                        'source_nw_y_pixel': -4822198846841400760,
                                        'source_pixel_width': -7052257711580658608,
                                        'source_pixel_height': -5199158382611333947,
                                        'rotation': -8297904186466793383,
                                        'virtual_nw_x_pixel': 1064834632,
                                        'virtual_nw_y_pixel': -1542142480,
                                        'virtual_width': -1145610566,
                                        'virtual_height': 559542426,
                                    },
                            {
                                        'source_monitor': 9934488,
                                        'source_nw_x_pixel': -5463891176227858665,
                                        'source_nw_y_pixel': -6908606439239516601,
                                        'source_pixel_width': -5480811292755175611,
                                        'source_pixel_height': -6122377191626781155,
                                        'rotation': -2045578328402634088,
                                        'virtual_nw_x_pixel': -169336850,
                                        'virtual_nw_y_pixel': -1832845713,
                                        'virtual_width': 1146915451,
                                        'virtual_height': 468983187,
                                    },
                            {
                                        'source_monitor': 910777,
                                        'source_nw_x_pixel': -2525061896629370989,
                                        'source_nw_y_pixel': -4261762626342807237,
                                        'source_pixel_width': -8558946774200974493,
                                        'source_pixel_height': -8405111487649991335,
                                        'rotation': -153028530289856798,
                                        'virtual_nw_x_pixel': -1484718219,
                                        'virtual_nw_y_pixel': 1088607319,
                                        'virtual_width': 581775171,
                                        'virtual_height': 1143465557,
                                    },
                            {
                                        'source_monitor': 3772697,
                                        'source_nw_x_pixel': -8710416540997773086,
                                        'source_nw_y_pixel': -7580515772364640608,
                                        'source_pixel_width': -7233974094560842470,
                                        'source_pixel_height': -9097234653723465227,
                                        'rotation': -3758329453577573936,
                                        'virtual_nw_x_pixel': -1027533623,
                                        'virtual_nw_y_pixel': 815592923,
                                        'virtual_width': -1287183496,
                                        'virtual_height': 835614770,
                                    },
                            {
                                        'source_monitor': 1394977,
                                        'source_nw_x_pixel': -7935246617749969157,
                                        'source_nw_y_pixel': -5241041068795395875,
                                        'source_pixel_width': -79935460607239666,
                                        'source_pixel_height': -6409234426680164655,
                                        'rotation': -2571072312610286898,
                                        'virtual_nw_x_pixel': 394635414,
                                        'virtual_nw_y_pixel': -293710905,
                                        'virtual_width': 1585993366,
                                        'virtual_height': 898459858,
                                    },
                            {
                                        'source_monitor': 7520545,
                                        'source_nw_x_pixel': -1635693806855606266,
                                        'source_nw_y_pixel': -315269738983703107,
                                        'source_pixel_width': -371237777026027746,
                                        'source_pixel_height': -6970603896490821506,
                                        'rotation': -913758325011434737,
                                        'virtual_nw_x_pixel': -1110885625,
                                        'virtual_nw_y_pixel': -865678040,
                                        'virtual_width': 1675870053,
                                        'virtual_height': -309874912,
                                    },
                        ],
                },
                {
                    'description': 'ζ}ȡǮaɩԌҽɀѴ˄қPƎʇƏşНˎʅęц\x80ɚФČЋѴѨĿ',
                    'monitors': [
                            {
                                        'identifier': -932667,
                                        'width': 8713242334670043288,
                                        'height': 1527664706098601790,
                                    },
                            {
                                        'identifier': 199118,
                                        'width': 3928417600917762478,
                                        'height': 8935163570692729154,
                                    },
                            {
                                        'identifier': -329285,
                                        'width': -6846565461661876366,
                                        'height': 4490128105329319999,
                                    },
                            {
                                        'identifier': 872384,
                                        'width': -8211214015456454807,
                                        'height': 5736465400842421643,
                                    },
                            {
                                        'identifier': 7062902,
                                        'width': 4292383245995933428,
                                        'height': -5986590794850360305,
                                    },
                            {
                                        'identifier': 9414457,
                                        'width': 4975438276413807787,
                                        'height': -1071435753325770145,
                                    },
                            {
                                        'identifier': 6992658,
                                        'width': 2446713819283275665,
                                        'height': 1652664096107784067,
                                    },
                            {
                                        'identifier': -815822,
                                        'width': -4824188812196108214,
                                        'height': -7604710829321126947,
                                    },
                            {
                                        'identifier': -494176,
                                        'width': 6504478427367855257,
                                        'height': -4140596763326088057,
                                    },
                            {
                                        'identifier': 7562089,
                                        'width': -8011822112970016709,
                                        'height': 3157499664855796096,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3087504,
                                        'source_nw_x_pixel': -61221588486336466,
                                        'source_nw_y_pixel': -4963471411620756833,
                                        'source_pixel_width': -1001015357048245388,
                                        'source_pixel_height': -4794722823389323155,
                                        'rotation': -5863709525669046679,
                                        'virtual_nw_x_pixel': -1429990539,
                                        'virtual_nw_y_pixel': 662661244,
                                        'virtual_width': -1083476254,
                                        'virtual_height': 1632836335,
                                    },
                            {
                                        'source_monitor': 9725855,
                                        'source_nw_x_pixel': -2237421060852645215,
                                        'source_nw_y_pixel': -4553393295640480748,
                                        'source_pixel_width': -6852261141267015095,
                                        'source_pixel_height': -2653529145797255572,
                                        'rotation': -7868609575872429400,
                                        'virtual_nw_x_pixel': -1624844046,
                                        'virtual_nw_y_pixel': 1019628394,
                                        'virtual_width': 1841021928,
                                        'virtual_height': 575959228,
                                    },
                            {
                                        'source_monitor': -970267,
                                        'source_nw_x_pixel': -6102276565604408759,
                                        'source_nw_y_pixel': -1402479644583073359,
                                        'source_pixel_width': -1489155433427757353,
                                        'source_pixel_height': -899913276711229405,
                                        'rotation': -4286389439203390565,
                                        'virtual_nw_x_pixel': 1512797814,
                                        'virtual_nw_y_pixel': 1596761466,
                                        'virtual_width': -1683632114,
                                        'virtual_height': -1888894563,
                                    },
                            {
                                        'source_monitor': 5197006,
                                        'source_nw_x_pixel': -7660886459492596288,
                                        'source_nw_y_pixel': -6358662229950269482,
                                        'source_pixel_width': -3286986772463166310,
                                        'source_pixel_height': -2680418253264647720,
                                        'rotation': -5819659725645691935,
                                        'virtual_nw_x_pixel': -1875538596,
                                        'virtual_nw_y_pixel': 820315636,
                                        'virtual_width': 1863138625,
                                        'virtual_height': 1609191876,
                                    },
                            {
                                        'source_monitor': 4738941,
                                        'source_nw_x_pixel': -3157515381097502706,
                                        'source_nw_y_pixel': -1360238743397954270,
                                        'source_pixel_width': -3949605124173619513,
                                        'source_pixel_height': -7246286431337167237,
                                        'rotation': -1779875011593004121,
                                        'virtual_nw_x_pixel': 1454247110,
                                        'virtual_nw_y_pixel': -153325528,
                                        'virtual_width': 780564331,
                                        'virtual_height': 813020261,
                                    },
                            {
                                        'source_monitor': 8192968,
                                        'source_nw_x_pixel': -951337785710706756,
                                        'source_nw_y_pixel': -879893602911101327,
                                        'source_pixel_width': -8415065530122427728,
                                        'source_pixel_height': -8564230549990852530,
                                        'rotation': -3543627514598527329,
                                        'virtual_nw_x_pixel': 1990316347,
                                        'virtual_nw_y_pixel': 388062933,
                                        'virtual_width': 348654066,
                                        'virtual_height': 926898861,
                                    },
                            {
                                        'source_monitor': 4616336,
                                        'source_nw_x_pixel': -4628299379652215264,
                                        'source_nw_y_pixel': -882424937974134992,
                                        'source_pixel_width': -3735771554693383930,
                                        'source_pixel_height': -3747837721103592125,
                                        'rotation': -6926520387724950951,
                                        'virtual_nw_x_pixel': 246781545,
                                        'virtual_nw_y_pixel': -1898250719,
                                        'virtual_width': 51930548,
                                        'virtual_height': -1236465714,
                                    },
                            {
                                        'source_monitor': 4244069,
                                        'source_nw_x_pixel': -3063634674372773358,
                                        'source_nw_y_pixel': -985111663319023559,
                                        'source_pixel_width': -5070051578809591258,
                                        'source_pixel_height': -4170374912104658552,
                                        'rotation': -8446143461312117521,
                                        'virtual_nw_x_pixel': -1369708784,
                                        'virtual_nw_y_pixel': -75165261,
                                        'virtual_width': 1096118118,
                                        'virtual_height': -1449779083,
                                    },
                            {
                                        'source_monitor': 8113063,
                                        'source_nw_x_pixel': -2241258809262243697,
                                        'source_nw_y_pixel': -465688628915068000,
                                        'source_pixel_width': -7843135161166189800,
                                        'source_pixel_height': -7776329280690069875,
                                        'rotation': -4969337035772023035,
                                        'virtual_nw_x_pixel': -538295347,
                                        'virtual_nw_y_pixel': 183681570,
                                        'virtual_width': -401983792,
                                        'virtual_height': -1119047433,
                                    },
                            {
                                        'source_monitor': 4303919,
                                        'source_nw_x_pixel': -6765792100163313930,
                                        'source_nw_y_pixel': -2957375843695444630,
                                        'source_pixel_width': -9095300509539568577,
                                        'source_pixel_height': -5717533331971402358,
                                        'rotation': -470606129278338704,
                                        'virtual_nw_x_pixel': 811220571,
                                        'virtual_nw_y_pixel': -454217951,
                                        'virtual_width': -1204998454,
                                        'virtual_height': 1293391387,
                                    },
                        ],
                },
                {
                    'description': 'ԍÐÒʾ˩ÌΓɌŶ˺ȮҹӺҚĹɾϓȓςЭǟÅ\u0380wϴЋԑ˅ĳʄ',
                    'monitors': [
                            {
                                        'identifier': 8955266,
                                        'width': 1522286371487296824,
                                        'height': 7026193131818012881,
                                    },
                            {
                                        'identifier': 5958420,
                                        'width': -3325005427104408938,
                                        'height': -8520173818762637518,
                                    },
                            {
                                        'identifier': 5331437,
                                        'width': 756103049724246295,
                                        'height': 2741694868687922713,
                                    },
                            {
                                        'identifier': 466322,
                                        'width': -7705356500263379399,
                                        'height': -6225883681319842082,
                                    },
                            {
                                        'identifier': 4697005,
                                        'width': -8715987630238214036,
                                        'height': -3247458189673592465,
                                    },
                            {
                                        'identifier': -870115,
                                        'width': -3209950353300079508,
                                        'height': -8872677382903586282,
                                    },
                            {
                                        'identifier': 2769965,
                                        'width': 2649844905065789483,
                                        'height': 4207614714981981931,
                                    },
                            {
                                        'identifier': 9503370,
                                        'width': -5281659270133280241,
                                        'height': -1404031935207553335,
                                    },
                            {
                                        'identifier': 7382238,
                                        'width': 7427400155771510124,
                                        'height': -5059861379206306206,
                                    },
                            {
                                        'identifier': 8931442,
                                        'width': -5274689786932985720,
                                        'height': -5302523486664548391,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9664935,
                                        'source_nw_x_pixel': -1972581885691974794,
                                        'source_nw_y_pixel': -3181403328600984164,
                                        'source_pixel_width': -4207408453595307873,
                                        'source_pixel_height': -2250277675500326305,
                                        'rotation': -4837200957343542610,
                                        'virtual_nw_x_pixel': -1437884029,
                                        'virtual_nw_y_pixel': 436961140,
                                        'virtual_width': -884451027,
                                        'virtual_height': 1764952312,
                                    },
                            {
                                        'source_monitor': 297066,
                                        'source_nw_x_pixel': -1868178046466307852,
                                        'source_nw_y_pixel': -5389407314673546904,
                                        'source_pixel_width': -4545941604396980792,
                                        'source_pixel_height': -2376915973966689449,
                                        'rotation': -9081397846118603254,
                                        'virtual_nw_x_pixel': 164144717,
                                        'virtual_nw_y_pixel': 921615389,
                                        'virtual_width': -1324707308,
                                        'virtual_height': -204293758,
                                    },
                            {
                                        'source_monitor': 4717132,
                                        'source_nw_x_pixel': -3651797687618696755,
                                        'source_nw_y_pixel': -9012214311767223324,
                                        'source_pixel_width': -4751008641143294289,
                                        'source_pixel_height': -7674877801736763337,
                                        'rotation': -6284575339281930750,
                                        'virtual_nw_x_pixel': 123250278,
                                        'virtual_nw_y_pixel': 1439803059,
                                        'virtual_width': -1277361366,
                                        'virtual_height': 1585124163,
                                    },
                            {
                                        'source_monitor': 3125731,
                                        'source_nw_x_pixel': -5276125246600402369,
                                        'source_nw_y_pixel': -6556788350209968677,
                                        'source_pixel_width': -6919754035003129779,
                                        'source_pixel_height': -1999994145095258082,
                                        'rotation': -6810987217202670624,
                                        'virtual_nw_x_pixel': -834819235,
                                        'virtual_nw_y_pixel': -1892185381,
                                        'virtual_width': 1529986204,
                                        'virtual_height': -461165137,
                                    },
                            {
                                        'source_monitor': 6970227,
                                        'source_nw_x_pixel': -5101130718099796424,
                                        'source_nw_y_pixel': -4888633580966134625,
                                        'source_pixel_width': -7830575085066825708,
                                        'source_pixel_height': -3481641371309389503,
                                        'rotation': -7091054974651235014,
                                        'virtual_nw_x_pixel': 340531363,
                                        'virtual_nw_y_pixel': -1700419541,
                                        'virtual_width': 1995843241,
                                        'virtual_height': -134683049,
                                    },
                            {
                                        'source_monitor': 5851849,
                                        'source_nw_x_pixel': -2743146286260619452,
                                        'source_nw_y_pixel': -5856637392596452329,
                                        'source_pixel_width': -1270088092022283305,
                                        'source_pixel_height': -176960556979801671,
                                        'rotation': -2808846946366464942,
                                        'virtual_nw_x_pixel': 1448496676,
                                        'virtual_nw_y_pixel': -1336986365,
                                        'virtual_width': 1033578420,
                                        'virtual_height': -233785136,
                                    },
                            {
                                        'source_monitor': 4155154,
                                        'source_nw_x_pixel': -3595119425746757085,
                                        'source_nw_y_pixel': -3922148086836442126,
                                        'source_pixel_width': -212807114805634847,
                                        'source_pixel_height': -3066154069108940880,
                                        'rotation': -5789977735517568645,
                                        'virtual_nw_x_pixel': -1583512271,
                                        'virtual_nw_y_pixel': -383077635,
                                        'virtual_width': -467265188,
                                        'virtual_height': 177697314,
                                    },
                            {
                                        'source_monitor': 2123040,
                                        'source_nw_x_pixel': -1744746031207153153,
                                        'source_nw_y_pixel': -2057260517517051403,
                                        'source_pixel_width': -7926579449604317910,
                                        'source_pixel_height': -5449673350260481522,
                                        'rotation': -5764990582985838120,
                                        'virtual_nw_x_pixel': -1140755409,
                                        'virtual_nw_y_pixel': 1035837827,
                                        'virtual_width': 438028269,
                                        'virtual_height': 1288623156,
                                    },
                            {
                                        'source_monitor': 3424919,
                                        'source_nw_x_pixel': -2918082069767812122,
                                        'source_nw_y_pixel': -2464149137879684337,
                                        'source_pixel_width': -4420404616113469550,
                                        'source_pixel_height': -2029502057491113892,
                                        'rotation': -2886349963223627446,
                                        'virtual_nw_x_pixel': -667901414,
                                        'virtual_nw_y_pixel': 334402603,
                                        'virtual_width': 1661540763,
                                        'virtual_height': 1039275955,
                                    },
                            {
                                        'source_monitor': 5209083,
                                        'source_nw_x_pixel': -3630780902932326451,
                                        'source_nw_y_pixel': -612621790560052078,
                                        'source_pixel_width': -7801013533918578415,
                                        'source_pixel_height': -906808137232424577,
                                        'rotation': -4548930489220011607,
                                        'virtual_nw_x_pixel': 255612164,
                                        'virtual_nw_y_pixel': -1963389085,
                                        'virtual_width': -1521290226,
                                        'virtual_height': -1069042161,
                                    },
                        ],
                },
                {
                    'description': 'ԊɸξӀʝʈ˯ȄɺĞ˒ȫžЉǣѺ}ԍЊѷȭ˙āϬ˲ԭƋ϶Өî',
                    'monitors': [
                            {
                                        'identifier': 3483651,
                                        'width': 278976084146489179,
                                        'height': -4409081965100271294,
                                    },
                            {
                                        'identifier': 1445451,
                                        'width': -7293111355730622541,
                                        'height': -1639489582501103934,
                                    },
                            {
                                        'identifier': 9268235,
                                        'width': -5340655592259059573,
                                        'height': 6146487671760926763,
                                    },
                            {
                                        'identifier': 7611897,
                                        'width': 1201707004550414755,
                                        'height': 5159395826723550785,
                                    },
                            {
                                        'identifier': 9867162,
                                        'width': 7541598590227061884,
                                        'height': -5763813557812154591,
                                    },
                            {
                                        'identifier': 1666079,
                                        'width': 2999310263837598581,
                                        'height': -5229118488261194877,
                                    },
                            {
                                        'identifier': 3565060,
                                        'width': -2739076663262316918,
                                        'height': 6220700823591882100,
                                    },
                            {
                                        'identifier': -964564,
                                        'width': 2878478529673979220,
                                        'height': 7028378969121038086,
                                    },
                            {
                                        'identifier': 6564416,
                                        'width': 2239824155709827254,
                                        'height': 874891071795944126,
                                    },
                            {
                                        'identifier': 2988412,
                                        'width': 8088682199783336438,
                                        'height': -8683939470072183728,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6076211,
                                        'source_nw_x_pixel': -7734916607338916818,
                                        'source_nw_y_pixel': -3243213054573003515,
                                        'source_pixel_width': -4485885656641040470,
                                        'source_pixel_height': -6415013826892240492,
                                        'rotation': -2553373022499106786,
                                        'virtual_nw_x_pixel': -1322192317,
                                        'virtual_nw_y_pixel': 1956559893,
                                        'virtual_width': 1554099913,
                                        'virtual_height': 1064540722,
                                    },
                            {
                                        'source_monitor': 3414565,
                                        'source_nw_x_pixel': -2227403108825142563,
                                        'source_nw_y_pixel': -1890355078962255629,
                                        'source_pixel_width': -6852539734855533291,
                                        'source_pixel_height': -2194279736139181907,
                                        'rotation': -2717630505843969359,
                                        'virtual_nw_x_pixel': 1745067944,
                                        'virtual_nw_y_pixel': -44282512,
                                        'virtual_width': -1073832180,
                                        'virtual_height': -309563447,
                                    },
                            {
                                        'source_monitor': 2783819,
                                        'source_nw_x_pixel': -3148652696874771519,
                                        'source_nw_y_pixel': -4468643172880159078,
                                        'source_pixel_width': -8133888007496080761,
                                        'source_pixel_height': -1266099158702550928,
                                        'rotation': -3791982304190392617,
                                        'virtual_nw_x_pixel': -1881465655,
                                        'virtual_nw_y_pixel': 1562526578,
                                        'virtual_width': -1606647161,
                                        'virtual_height': 1440253777,
                                    },
                            {
                                        'source_monitor': 3155594,
                                        'source_nw_x_pixel': -6581684883669287097,
                                        'source_nw_y_pixel': -4192772866074834930,
                                        'source_pixel_width': -5320720027428121665,
                                        'source_pixel_height': -5626562112512994460,
                                        'rotation': -2801776330074725730,
                                        'virtual_nw_x_pixel': -1315281192,
                                        'virtual_nw_y_pixel': -1516224900,
                                        'virtual_width': -518531321,
                                        'virtual_height': -895448784,
                                    },
                            {
                                        'source_monitor': 1346992,
                                        'source_nw_x_pixel': -5275962055576444078,
                                        'source_nw_y_pixel': -538667782602212248,
                                        'source_pixel_width': -1779238573523610217,
                                        'source_pixel_height': -8204416349691362612,
                                        'rotation': -4396444439227625252,
                                        'virtual_nw_x_pixel': 730604938,
                                        'virtual_nw_y_pixel': 1177400974,
                                        'virtual_width': -1716531246,
                                        'virtual_height': 145342798,
                                    },
                            {
                                        'source_monitor': -214280,
                                        'source_nw_x_pixel': -8436377414421595890,
                                        'source_nw_y_pixel': -5046385847155473841,
                                        'source_pixel_width': -2337503319701419209,
                                        'source_pixel_height': -3333336875132898457,
                                        'rotation': -5513510366307320190,
                                        'virtual_nw_x_pixel': 1829781444,
                                        'virtual_nw_y_pixel': 1287411460,
                                        'virtual_width': 1150361784,
                                        'virtual_height': 76756429,
                                    },
                            {
                                        'source_monitor': 7746465,
                                        'source_nw_x_pixel': -9217440600563541765,
                                        'source_nw_y_pixel': -3346817973961546558,
                                        'source_pixel_width': -2466260436487548729,
                                        'source_pixel_height': -8250635411174324109,
                                        'rotation': -6956186741135974717,
                                        'virtual_nw_x_pixel': -15773060,
                                        'virtual_nw_y_pixel': 500635299,
                                        'virtual_width': -1438823830,
                                        'virtual_height': 164196862,
                                    },
                            {
                                        'source_monitor': 2390454,
                                        'source_nw_x_pixel': -3455074815469315415,
                                        'source_nw_y_pixel': -9184616469887028923,
                                        'source_pixel_width': -6808532434666109106,
                                        'source_pixel_height': -5644378786651259969,
                                        'rotation': -6310766958684258897,
                                        'virtual_nw_x_pixel': -492512249,
                                        'virtual_nw_y_pixel': -1305052175,
                                        'virtual_width': 1875752203,
                                        'virtual_height': -1876394440,
                                    },
                            {
                                        'source_monitor': 6407167,
                                        'source_nw_x_pixel': -6583575566089917335,
                                        'source_nw_y_pixel': -8554500005786729596,
                                        'source_pixel_width': -7769945993837762424,
                                        'source_pixel_height': -7581825784134317027,
                                        'rotation': -7908374466485229007,
                                        'virtual_nw_x_pixel': 882668929,
                                        'virtual_nw_y_pixel': -1004222907,
                                        'virtual_width': 514516849,
                                        'virtual_height': -1566973381,
                                    },
                            {
                                        'source_monitor': 5983139,
                                        'source_nw_x_pixel': -6369396257902233024,
                                        'source_nw_y_pixel': -8874708329536752332,
                                        'source_pixel_width': -6533830559242086935,
                                        'source_pixel_height': -3608031994696606359,
                                        'rotation': -108690609459404432,
                                        'virtual_nw_x_pixel': -906381563,
                                        'virtual_nw_y_pixel': 539487444,
                                        'virtual_width': -422619041,
                                        'virtual_height': 881506736,
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
                                        'identifier': 3283123,
                                        'width': -3499909286317344383,
                                        'height': 6833538744589757121,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -6091587045180995228,
                                        'source_nw_y_pixel': -2215548461691848616,
                                        'source_pixel_width': -1674118264307866588,
                                        'source_pixel_height': -6178220799714532661,
                                        'rotation': -8367211035707766722,
                                        'virtual_nw_x_pixel': -429092908,
                                        'virtual_nw_y_pixel': 814797085,
                                        'virtual_width': 1388569735,
                                        'virtual_height': -337671235,
                                    },
                        ],
                },
            ],

        },
    ),
]
