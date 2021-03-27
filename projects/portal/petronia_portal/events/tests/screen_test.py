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
            'identifier': 6309892,
            'width': -8813319328513234102,
            'height': 4142961512998153583,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 9319139,

            'width': -619607060981323467,

            'height': -3165053347060351728,

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
            'source_monitor': 2020321,
            'source_nw_x_pixel': -7589422764267610592,
            'source_nw_y_pixel': -8759300115531384500,
            'source_pixel_width': -1706135727397257323,
            'source_pixel_height': -1901245004978749818,
            'rotation': -8262856883775095333,
            'virtual_nw_x_pixel': -1099143033,
            'virtual_nw_y_pixel': 322215132,
            'virtual_width': 305114512,
            'virtual_height': -1126865679,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -6075518110235750903,

            'source_nw_y_pixel': -8659135704638407582,

            'source_pixel_width': -2992961449098952188,

            'source_pixel_height': -1773739432513026165,

            'rotation': -8668027473918753574,

            'virtual_nw_x_pixel': -1274727746,

            'virtual_nw_y_pixel': -389161213,

            'virtual_width': 1366644944,

            'virtual_height': 923694650,

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
            'description': 'ʳƸӽ?·kŰυǊͽώɫĨӪ˶hȾŢɛÿЕїĞƽńϋɚgӬʪ',
            'monitors': [
                {
                    'identifier': 6327915,
                    'width': -712768800887033513,
                    'height': 354308904757020809,
                },
                {
                    'identifier': -723251,
                    'width': -7082139563631972499,
                    'height': -8640019535290109536,
                },
                {
                    'identifier': 9060047,
                    'width': -6343707467864279268,
                    'height': -1300187854801204094,
                },
                {
                    'identifier': 2271851,
                    'width': -8008933283335937280,
                    'height': 7751608854221667595,
                },
                {
                    'identifier': 1188910,
                    'width': -4853974535890741350,
                    'height': -8751788266366242670,
                },
                {
                    'identifier': -111895,
                    'width': -7023523531394774278,
                    'height': -7622738048319041159,
                },
                {
                    'identifier': 5777734,
                    'width': -325352641690140807,
                    'height': -8427528923707892598,
                },
                {
                    'identifier': 7411345,
                    'width': -8959892138062207113,
                    'height': -8877724183148203229,
                },
                {
                    'identifier': 3591702,
                    'width': -1800910426294321033,
                    'height': -9889089453285402,
                },
                {
                    'identifier': 7584530,
                    'width': -8622100949679768695,
                    'height': -2177596780588187724,
                },
            ],
            'screen': [
                {
                    'source_monitor': 442655,
                    'source_nw_x_pixel': -3730417166032225901,
                    'source_nw_y_pixel': -4578955847496425471,
                    'source_pixel_width': -1137497529965698980,
                    'source_pixel_height': -5483662213160863719,
                    'rotation': -1146339615793144445,
                    'virtual_nw_x_pixel': 149648835,
                    'virtual_nw_y_pixel': -787530449,
                    'virtual_width': -1878439160,
                    'virtual_height': -1623481836,
                },
                {
                    'source_monitor': 9975515,
                    'source_nw_x_pixel': -4665190132378902280,
                    'source_nw_y_pixel': -1422721169047869903,
                    'source_pixel_width': -4617742659704235380,
                    'source_pixel_height': -2765088829756715259,
                    'rotation': -5035381093997699600,
                    'virtual_nw_x_pixel': -51310112,
                    'virtual_nw_y_pixel': 1147370819,
                    'virtual_width': 534066995,
                    'virtual_height': 1238060903,
                },
                {
                    'source_monitor': 4770121,
                    'source_nw_x_pixel': -129878938144748652,
                    'source_nw_y_pixel': -4694149882086972061,
                    'source_pixel_width': -162384927638284587,
                    'source_pixel_height': -7668756723133840118,
                    'rotation': -8173038661037962475,
                    'virtual_nw_x_pixel': -348671147,
                    'virtual_nw_y_pixel': 782663145,
                    'virtual_width': -806935149,
                    'virtual_height': -739029009,
                },
                {
                    'source_monitor': 5582938,
                    'source_nw_x_pixel': -490801267500634125,
                    'source_nw_y_pixel': -4219091521206486948,
                    'source_pixel_width': -8721210247813260325,
                    'source_pixel_height': -8774069505936630949,
                    'rotation': -2629997136885874369,
                    'virtual_nw_x_pixel': 229448588,
                    'virtual_nw_y_pixel': 652240457,
                    'virtual_width': 570673471,
                    'virtual_height': -1996651528,
                },
                {
                    'source_monitor': 1620293,
                    'source_nw_x_pixel': -6626644728800140410,
                    'source_nw_y_pixel': -6536316985731026044,
                    'source_pixel_width': -5192637184255958898,
                    'source_pixel_height': -3501923755641194354,
                    'rotation': -3012416273608680851,
                    'virtual_nw_x_pixel': -1516950040,
                    'virtual_nw_y_pixel': 1278069580,
                    'virtual_width': -1870847399,
                    'virtual_height': 892463982,
                },
                {
                    'source_monitor': 7925107,
                    'source_nw_x_pixel': -3717828248891247183,
                    'source_nw_y_pixel': -5516587063566362035,
                    'source_pixel_width': -5963150535246454171,
                    'source_pixel_height': -1474776555368213238,
                    'rotation': -1306211179913914497,
                    'virtual_nw_x_pixel': -422808096,
                    'virtual_nw_y_pixel': -986842616,
                    'virtual_width': -698737876,
                    'virtual_height': -432211779,
                },
                {
                    'source_monitor': 6597177,
                    'source_nw_x_pixel': -3748977900752194136,
                    'source_nw_y_pixel': -8979389281955305553,
                    'source_pixel_width': -5639847821810783162,
                    'source_pixel_height': -7222262108205936936,
                    'rotation': -5860378823131649560,
                    'virtual_nw_x_pixel': -791860133,
                    'virtual_nw_y_pixel': -1240991283,
                    'virtual_width': -1779433569,
                    'virtual_height': 798984036,
                },
                {
                    'source_monitor': 2683622,
                    'source_nw_x_pixel': -6113061690766002032,
                    'source_nw_y_pixel': -7998123986677787458,
                    'source_pixel_width': -7776594709613422336,
                    'source_pixel_height': -2560120254887581774,
                    'rotation': -4568553273699911288,
                    'virtual_nw_x_pixel': 1516781189,
                    'virtual_nw_y_pixel': 793340962,
                    'virtual_width': -996895464,
                    'virtual_height': -1820047762,
                },
                {
                    'source_monitor': 9840372,
                    'source_nw_x_pixel': -143020786276324288,
                    'source_nw_y_pixel': -489236086244840188,
                    'source_pixel_width': -2766782632223274128,
                    'source_pixel_height': -1787737413557967027,
                    'rotation': -987649587098658198,
                    'virtual_nw_x_pixel': -1244089881,
                    'virtual_nw_y_pixel': -1990416834,
                    'virtual_width': 87902248,
                    'virtual_height': 270105607,
                },
                {
                    'source_monitor': 9771283,
                    'source_nw_x_pixel': -5427362105990693231,
                    'source_nw_y_pixel': -7964030685721244232,
                    'source_pixel_width': -8608421612352632264,
                    'source_pixel_height': -4409133241088562689,
                    'rotation': -459169391008349601,
                    'virtual_nw_x_pixel': -318624306,
                    'virtual_nw_y_pixel': -1029441408,
                    'virtual_width': -286392357,
                    'virtual_height': 540863334,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 4193247,
                    'width': 7438715902130330875,
                    'height': -6235371622474881895,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -4083282043390616473,
                    'source_nw_y_pixel': -2827075224369162690,
                    'source_pixel_width': -2596992849283762525,
                    'source_pixel_height': -4478606849202081461,
                    'rotation': -2481172941554459866,
                    'virtual_nw_x_pixel': -873059204,
                    'virtual_nw_y_pixel': 1603365926,
                    'virtual_width': -216688445,
                    'virtual_height': -867798428,
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
            'request_id': 7099940,
            'mapped_screens_by_monitors': [
                {
                    'description': '˝ν´әƅ˱ъТЂɵśϲϸɁe΄ÁäÖǨɏΘķР\x9a\x9eҗs1ŧ',
                    'monitors': [
                            {
                                        'identifier': 7146909,
                                        'width': -301005121184712211,
                                        'height': 893599340029013510,
                                    },
                            {
                                        'identifier': 7169863,
                                        'width': 8626953906907697962,
                                        'height': -48884442638482275,
                                    },
                            {
                                        'identifier': 9186289,
                                        'width': -4991735892017669737,
                                        'height': 728412352168163997,
                                    },
                            {
                                        'identifier': 2888165,
                                        'width': 4361865162874278118,
                                        'height': 5041061425740769577,
                                    },
                            {
                                        'identifier': 5928173,
                                        'width': 534665796047987831,
                                        'height': 3640410391579744191,
                                    },
                            {
                                        'identifier': 5114766,
                                        'width': 8792788187733131081,
                                        'height': 27068891952010144,
                                    },
                            {
                                        'identifier': 7058553,
                                        'width': -3401962040403759717,
                                        'height': 7277675112787647455,
                                    },
                            {
                                        'identifier': 4380301,
                                        'width': 3573417797310821684,
                                        'height': -9088019156896316629,
                                    },
                            {
                                        'identifier': 9786662,
                                        'width': 674885782471631806,
                                        'height': -7111158075082056473,
                                    },
                            {
                                        'identifier': 7487489,
                                        'width': 6146883518758207994,
                                        'height': 3423913686547087521,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5280834,
                                        'source_nw_x_pixel': -4129219780897249641,
                                        'source_nw_y_pixel': -2412411878225206169,
                                        'source_pixel_width': -663607705862540546,
                                        'source_pixel_height': -306217631594844495,
                                        'rotation': -2230277592414694737,
                                        'virtual_nw_x_pixel': 504532527,
                                        'virtual_nw_y_pixel': -1693345402,
                                        'virtual_width': 1815449096,
                                        'virtual_height': 384279786,
                                    },
                            {
                                        'source_monitor': 7455276,
                                        'source_nw_x_pixel': -4209865324536354330,
                                        'source_nw_y_pixel': -2667829341331088253,
                                        'source_pixel_width': -4132138314137300631,
                                        'source_pixel_height': -1015677522824512108,
                                        'rotation': -8814687689743667547,
                                        'virtual_nw_x_pixel': -271755000,
                                        'virtual_nw_y_pixel': 499439274,
                                        'virtual_width': -1383493574,
                                        'virtual_height': 285679259,
                                    },
                            {
                                        'source_monitor': 8537018,
                                        'source_nw_x_pixel': -6701919315514658968,
                                        'source_nw_y_pixel': -1326722286003053521,
                                        'source_pixel_width': -3284019035396459111,
                                        'source_pixel_height': -2889833498022419699,
                                        'rotation': -2232249437977572139,
                                        'virtual_nw_x_pixel': 1929746416,
                                        'virtual_nw_y_pixel': -733284818,
                                        'virtual_width': -406047240,
                                        'virtual_height': -709807251,
                                    },
                            {
                                        'source_monitor': 52751,
                                        'source_nw_x_pixel': -8914401437914100004,
                                        'source_nw_y_pixel': -4705732485409292254,
                                        'source_pixel_width': -4792659438514074084,
                                        'source_pixel_height': -149354412817387705,
                                        'rotation': -8118297661828043902,
                                        'virtual_nw_x_pixel': 1014945960,
                                        'virtual_nw_y_pixel': 313065705,
                                        'virtual_width': 1277629968,
                                        'virtual_height': -593303076,
                                    },
                            {
                                        'source_monitor': 1238661,
                                        'source_nw_x_pixel': -30819188755085997,
                                        'source_nw_y_pixel': -8556742918580615817,
                                        'source_pixel_width': -7004862303748941425,
                                        'source_pixel_height': -525217714650903664,
                                        'rotation': -8952366049658545514,
                                        'virtual_nw_x_pixel': 70770399,
                                        'virtual_nw_y_pixel': 849329152,
                                        'virtual_width': -1554581669,
                                        'virtual_height': -652475788,
                                    },
                            {
                                        'source_monitor': 5140908,
                                        'source_nw_x_pixel': -1983843284552719297,
                                        'source_nw_y_pixel': -61350673199239376,
                                        'source_pixel_width': -3184744289065076416,
                                        'source_pixel_height': -2084095457692667475,
                                        'rotation': -7373587232584360941,
                                        'virtual_nw_x_pixel': 565081572,
                                        'virtual_nw_y_pixel': -317753472,
                                        'virtual_width': 480643884,
                                        'virtual_height': 1335659812,
                                    },
                            {
                                        'source_monitor': 148130,
                                        'source_nw_x_pixel': -1349294549019311286,
                                        'source_nw_y_pixel': -4439891087904444862,
                                        'source_pixel_width': -880322903279135566,
                                        'source_pixel_height': -4821332354015189775,
                                        'rotation': -7510093435951494942,
                                        'virtual_nw_x_pixel': -274282968,
                                        'virtual_nw_y_pixel': -534636023,
                                        'virtual_width': 1644881444,
                                        'virtual_height': -1864406871,
                                    },
                            {
                                        'source_monitor': 446127,
                                        'source_nw_x_pixel': -2847907840949767003,
                                        'source_nw_y_pixel': -9518664713496512,
                                        'source_pixel_width': -7938744181790982168,
                                        'source_pixel_height': -4145427436655167420,
                                        'rotation': -741954716130226056,
                                        'virtual_nw_x_pixel': 217939283,
                                        'virtual_nw_y_pixel': -1003766362,
                                        'virtual_width': -1292654301,
                                        'virtual_height': 77538642,
                                    },
                            {
                                        'source_monitor': 2796370,
                                        'source_nw_x_pixel': -7822710516418101526,
                                        'source_nw_y_pixel': -5839682203600705302,
                                        'source_pixel_width': -3846440657619680445,
                                        'source_pixel_height': -3415287443089681062,
                                        'rotation': -4360238906882135313,
                                        'virtual_nw_x_pixel': -1899640752,
                                        'virtual_nw_y_pixel': 395987451,
                                        'virtual_width': -860986645,
                                        'virtual_height': 1350647596,
                                    },
                            {
                                        'source_monitor': 3724023,
                                        'source_nw_x_pixel': -6470565571308818784,
                                        'source_nw_y_pixel': -8971575034730023902,
                                        'source_pixel_width': -8830579390315902980,
                                        'source_pixel_height': -544764843939815486,
                                        'rotation': -3304711856490462057,
                                        'virtual_nw_x_pixel': 1277832905,
                                        'virtual_nw_y_pixel': -393423084,
                                        'virtual_width': 985936792,
                                        'virtual_height': 1890010405,
                                    },
                        ],
                },
                {
                    'description': 'pΨԕԓρҒũ',
                    'monitors': [
                            {
                                        'identifier': 7655859,
                                        'width': -126402064235498550,
                                        'height': 1748589630325802153,
                                    },
                            {
                                        'identifier': 6307113,
                                        'width': -1778630812778574331,
                                        'height': -5344699855385300443,
                                    },
                            {
                                        'identifier': 4936363,
                                        'width': 3825883270662889091,
                                        'height': 1818556235402171088,
                                    },
                            {
                                        'identifier': 2726687,
                                        'width': 2709152778637069987,
                                        'height': -3446680742904578186,
                                    },
                            {
                                        'identifier': 3661946,
                                        'width': 7014484479852684437,
                                        'height': 5304206283476195688,
                                    },
                            {
                                        'identifier': 8175050,
                                        'width': -4027023912310336559,
                                        'height': 7869511145607826533,
                                    },
                            {
                                        'identifier': 5643467,
                                        'width': 4509863737805218286,
                                        'height': -3105153324720923467,
                                    },
                            {
                                        'identifier': 3814396,
                                        'width': 8250931639489344451,
                                        'height': -7576527326348610681,
                                    },
                            {
                                        'identifier': 9533554,
                                        'width': -1085621103484578811,
                                        'height': 8960180359224568849,
                                    },
                            {
                                        'identifier': 5743474,
                                        'width': 2283098520824412843,
                                        'height': -7321034389276621215,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8145219,
                                        'source_nw_x_pixel': -1628319678359700295,
                                        'source_nw_y_pixel': -2098420422534885166,
                                        'source_pixel_width': -1469604597672888590,
                                        'source_pixel_height': -8831348833047831993,
                                        'rotation': -2737560697110055715,
                                        'virtual_nw_x_pixel': -1612970530,
                                        'virtual_nw_y_pixel': -771503202,
                                        'virtual_width': -367378522,
                                        'virtual_height': 1877393983,
                                    },
                            {
                                        'source_monitor': 5683898,
                                        'source_nw_x_pixel': -1470959022404898243,
                                        'source_nw_y_pixel': -6098136666409086959,
                                        'source_pixel_width': -534933136747583892,
                                        'source_pixel_height': -8764064529933389885,
                                        'rotation': -6489399493402924769,
                                        'virtual_nw_x_pixel': -1229011075,
                                        'virtual_nw_y_pixel': -1834474600,
                                        'virtual_width': -60550072,
                                        'virtual_height': -1976276606,
                                    },
                            {
                                        'source_monitor': 3022315,
                                        'source_nw_x_pixel': -4898585810516914396,
                                        'source_nw_y_pixel': -1252396240463720202,
                                        'source_pixel_width': -4167148540965069679,
                                        'source_pixel_height': -423789608771337633,
                                        'rotation': -2735140351579907615,
                                        'virtual_nw_x_pixel': -732690368,
                                        'virtual_nw_y_pixel': 1556031602,
                                        'virtual_width': -1895436772,
                                        'virtual_height': 1108403278,
                                    },
                            {
                                        'source_monitor': 6678015,
                                        'source_nw_x_pixel': -351475055869641105,
                                        'source_nw_y_pixel': -8136390600556256936,
                                        'source_pixel_width': -5958298152003118383,
                                        'source_pixel_height': -1560031130816939109,
                                        'rotation': -933969350449842145,
                                        'virtual_nw_x_pixel': -881467585,
                                        'virtual_nw_y_pixel': -1692715952,
                                        'virtual_width': 1811850188,
                                        'virtual_height': -305904278,
                                    },
                            {
                                        'source_monitor': 7314475,
                                        'source_nw_x_pixel': -3650358349977152015,
                                        'source_nw_y_pixel': -65218679376139973,
                                        'source_pixel_width': -8140998892520979341,
                                        'source_pixel_height': -7522763158020165808,
                                        'rotation': -2552837240324827152,
                                        'virtual_nw_x_pixel': 1130418244,
                                        'virtual_nw_y_pixel': -508375678,
                                        'virtual_width': 1429461870,
                                        'virtual_height': -779676686,
                                    },
                            {
                                        'source_monitor': 8400534,
                                        'source_nw_x_pixel': -6128446120109332551,
                                        'source_nw_y_pixel': -413763477434336210,
                                        'source_pixel_width': -976369332558296621,
                                        'source_pixel_height': -3545986427628800597,
                                        'rotation': -5271291900316712515,
                                        'virtual_nw_x_pixel': -331230279,
                                        'virtual_nw_y_pixel': -66748179,
                                        'virtual_width': -1110424507,
                                        'virtual_height': -1264580859,
                                    },
                            {
                                        'source_monitor': 1168942,
                                        'source_nw_x_pixel': -68168723193958983,
                                        'source_nw_y_pixel': -7354291500587762081,
                                        'source_pixel_width': -9075800924883147813,
                                        'source_pixel_height': -3306378855765729942,
                                        'rotation': -1435998226801072930,
                                        'virtual_nw_x_pixel': -759496156,
                                        'virtual_nw_y_pixel': 752014544,
                                        'virtual_width': 266933131,
                                        'virtual_height': 246404929,
                                    },
                            {
                                        'source_monitor': 6306845,
                                        'source_nw_x_pixel': -847131791496273494,
                                        'source_nw_y_pixel': -6709760543273758199,
                                        'source_pixel_width': -6799581397109167946,
                                        'source_pixel_height': -9005730443354538799,
                                        'rotation': -8748356421367874765,
                                        'virtual_nw_x_pixel': 1416668293,
                                        'virtual_nw_y_pixel': -1309415573,
                                        'virtual_width': -1348241723,
                                        'virtual_height': 837429344,
                                    },
                            {
                                        'source_monitor': 7533994,
                                        'source_nw_x_pixel': -7683656642824368293,
                                        'source_nw_y_pixel': -1411047955441750061,
                                        'source_pixel_width': -6068849961605258660,
                                        'source_pixel_height': -1790778653272936964,
                                        'rotation': -4131084765982659577,
                                        'virtual_nw_x_pixel': -433599086,
                                        'virtual_nw_y_pixel': 1593180443,
                                        'virtual_width': 1812984676,
                                        'virtual_height': -44645317,
                                    },
                            {
                                        'source_monitor': 8439519,
                                        'source_nw_x_pixel': -8407293882977016477,
                                        'source_nw_y_pixel': -6480879600748854295,
                                        'source_pixel_width': -4050156249365483113,
                                        'source_pixel_height': -5057497632498271890,
                                        'rotation': -5521497831231534662,
                                        'virtual_nw_x_pixel': -1181992812,
                                        'virtual_nw_y_pixel': 1503035015,
                                        'virtual_width': 664851097,
                                        'virtual_height': -1009855955,
                                    },
                        ],
                },
                {
                    'description': 'ұ҉ƹӸʼбƖӓѴԓƇȖʶLĵѵÑɆҭ8ŝͺǮєʶ¿Óҫýq',
                    'monitors': [
                            {
                                        'identifier': 6415912,
                                        'width': 7304628210698125901,
                                        'height': 4026948012833239049,
                                    },
                            {
                                        'identifier': 2507684,
                                        'width': -8543530982352396580,
                                        'height': -6137803775575744712,
                                    },
                            {
                                        'identifier': 3446658,
                                        'width': -8673573139385376253,
                                        'height': 2116401899771293445,
                                    },
                            {
                                        'identifier': 8272602,
                                        'width': 5528500708752299471,
                                        'height': 2829195333407075237,
                                    },
                            {
                                        'identifier': 6338783,
                                        'width': 9060705301677149945,
                                        'height': 7173545536217796585,
                                    },
                            {
                                        'identifier': 6932885,
                                        'width': 4559192421899176561,
                                        'height': -2483141576594352089,
                                    },
                            {
                                        'identifier': 97467,
                                        'width': -8625578583303907902,
                                        'height': 8934705493880535037,
                                    },
                            {
                                        'identifier': 8046593,
                                        'width': -8859028515287557022,
                                        'height': 3840654092082887669,
                                    },
                            {
                                        'identifier': 2546062,
                                        'width': -1072829912159155327,
                                        'height': 1846946313121489323,
                                    },
                            {
                                        'identifier': 5903577,
                                        'width': -3197577473593490658,
                                        'height': -6498656850419060655,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4543925,
                                        'source_nw_x_pixel': -2026196078167437068,
                                        'source_nw_y_pixel': -541527230129856184,
                                        'source_pixel_width': -1414158269977935939,
                                        'source_pixel_height': -3657928163073004947,
                                        'rotation': -6447176418853986629,
                                        'virtual_nw_x_pixel': -1642090881,
                                        'virtual_nw_y_pixel': -1034362622,
                                        'virtual_width': 981107621,
                                        'virtual_height': 1633737758,
                                    },
                            {
                                        'source_monitor': 5870733,
                                        'source_nw_x_pixel': -6395809988893095697,
                                        'source_nw_y_pixel': -4583059455678682210,
                                        'source_pixel_width': -7461130741909015132,
                                        'source_pixel_height': -5958928697415742666,
                                        'rotation': -1228338928750871627,
                                        'virtual_nw_x_pixel': 1188897966,
                                        'virtual_nw_y_pixel': 1598284294,
                                        'virtual_width': -1070765724,
                                        'virtual_height': 361366855,
                                    },
                            {
                                        'source_monitor': 2661828,
                                        'source_nw_x_pixel': -7675658751323798766,
                                        'source_nw_y_pixel': -3171152880060651400,
                                        'source_pixel_width': -1695622973461537196,
                                        'source_pixel_height': -4666307151350808914,
                                        'rotation': -7273356867154641748,
                                        'virtual_nw_x_pixel': 850929687,
                                        'virtual_nw_y_pixel': -1697047088,
                                        'virtual_width': -726194973,
                                        'virtual_height': -1234716622,
                                    },
                            {
                                        'source_monitor': 8665809,
                                        'source_nw_x_pixel': -1241023999941085046,
                                        'source_nw_y_pixel': -4853032507538685085,
                                        'source_pixel_width': -3960161287927278119,
                                        'source_pixel_height': -716489832801043732,
                                        'rotation': -7402412045259874518,
                                        'virtual_nw_x_pixel': 1237762853,
                                        'virtual_nw_y_pixel': 275518393,
                                        'virtual_width': -1909201433,
                                        'virtual_height': 1247853945,
                                    },
                            {
                                        'source_monitor': 6477190,
                                        'source_nw_x_pixel': -8073949951840168037,
                                        'source_nw_y_pixel': -7647299856287337546,
                                        'source_pixel_width': -689573276109003734,
                                        'source_pixel_height': -3277502649148835839,
                                        'rotation': -8691155471999081031,
                                        'virtual_nw_x_pixel': 1175037917,
                                        'virtual_nw_y_pixel': -337725351,
                                        'virtual_width': -252213483,
                                        'virtual_height': 636001126,
                                    },
                            {
                                        'source_monitor': 8140626,
                                        'source_nw_x_pixel': -335323244287854982,
                                        'source_nw_y_pixel': -6571134128105546589,
                                        'source_pixel_width': -8554560330954111244,
                                        'source_pixel_height': -2690984825923797503,
                                        'rotation': -8400470511904405156,
                                        'virtual_nw_x_pixel': -580788476,
                                        'virtual_nw_y_pixel': 1610459353,
                                        'virtual_width': -1060960025,
                                        'virtual_height': 1397247690,
                                    },
                            {
                                        'source_monitor': 6260900,
                                        'source_nw_x_pixel': -2251350351226965074,
                                        'source_nw_y_pixel': -4105256308090209526,
                                        'source_pixel_width': -517512602585115318,
                                        'source_pixel_height': -361598073759043815,
                                        'rotation': -9085282910904727852,
                                        'virtual_nw_x_pixel': -1810851996,
                                        'virtual_nw_y_pixel': 829892057,
                                        'virtual_width': -1357086147,
                                        'virtual_height': -35272689,
                                    },
                            {
                                        'source_monitor': 1099070,
                                        'source_nw_x_pixel': -7150138269240332760,
                                        'source_nw_y_pixel': -6043055846207203557,
                                        'source_pixel_width': -8228910251373753945,
                                        'source_pixel_height': -2280802785712393520,
                                        'rotation': -3037720524183350894,
                                        'virtual_nw_x_pixel': 1923608983,
                                        'virtual_nw_y_pixel': 1175109783,
                                        'virtual_width': 148258736,
                                        'virtual_height': -1626465544,
                                    },
                            {
                                        'source_monitor': 5569706,
                                        'source_nw_x_pixel': -8419960928162799098,
                                        'source_nw_y_pixel': -3960403001084418977,
                                        'source_pixel_width': -6404506879370164203,
                                        'source_pixel_height': -1232305313292367275,
                                        'rotation': -5900717668881970434,
                                        'virtual_nw_x_pixel': -1232869213,
                                        'virtual_nw_y_pixel': 1112045222,
                                        'virtual_width': 1929046178,
                                        'virtual_height': -644758797,
                                    },
                            {
                                        'source_monitor': 7906107,
                                        'source_nw_x_pixel': -4144456765557566558,
                                        'source_nw_y_pixel': -5665832097798076910,
                                        'source_pixel_width': -6181368409358927459,
                                        'source_pixel_height': -7248029993807580565,
                                        'rotation': -3264438814303781379,
                                        'virtual_nw_x_pixel': 1551242975,
                                        'virtual_nw_y_pixel': -1679695986,
                                        'virtual_width': -110978038,
                                        'virtual_height': -1817018782,
                                    },
                        ],
                },
                {
                    'description': 'ÏɕʪѾĤ{ӥŭ˚ˣԀӟȚªѳπʁќͻҍ¾ȃѩƫΔϼƀɏ¨ӳ',
                    'monitors': [
                            {
                                        'identifier': 7524656,
                                        'width': -5089317051252079504,
                                        'height': 2769687284147966896,
                                    },
                            {
                                        'identifier': 632829,
                                        'width': -3976241439193610164,
                                        'height': -5555701854726630635,
                                    },
                            {
                                        'identifier': 6032070,
                                        'width': -251660577908581077,
                                        'height': 7210094810183642540,
                                    },
                            {
                                        'identifier': -267322,
                                        'width': -8170906110560517365,
                                        'height': -6224221570262498744,
                                    },
                            {
                                        'identifier': 5747279,
                                        'width': 9010023771446539920,
                                        'height': 6309824482356790825,
                                    },
                            {
                                        'identifier': 857817,
                                        'width': 791446756788034207,
                                        'height': 2795145820429195415,
                                    },
                            {
                                        'identifier': 3295056,
                                        'width': 54572034615925136,
                                        'height': 8370566983672182793,
                                    },
                            {
                                        'identifier': 6697868,
                                        'width': -8043058106442557166,
                                        'height': -9091782923257765878,
                                    },
                            {
                                        'identifier': 495625,
                                        'width': -1251288323289171262,
                                        'height': 5677277997647680400,
                                    },
                            {
                                        'identifier': 5987207,
                                        'width': 712117440685713853,
                                        'height': 71702344667179978,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8865924,
                                        'source_nw_x_pixel': -3708652930151610913,
                                        'source_nw_y_pixel': -334382325955246659,
                                        'source_pixel_width': -521906050376753019,
                                        'source_pixel_height': -3971413843545527628,
                                        'rotation': -3403896916989311405,
                                        'virtual_nw_x_pixel': -25364301,
                                        'virtual_nw_y_pixel': 1765297788,
                                        'virtual_width': -1492279083,
                                        'virtual_height': -1782858343,
                                    },
                            {
                                        'source_monitor': 5323624,
                                        'source_nw_x_pixel': -1883963083630909528,
                                        'source_nw_y_pixel': -4006996390325473782,
                                        'source_pixel_width': -2969194576361782999,
                                        'source_pixel_height': -5335110908262812002,
                                        'rotation': -2318696866297427875,
                                        'virtual_nw_x_pixel': 98837830,
                                        'virtual_nw_y_pixel': 1794483040,
                                        'virtual_width': 1480432749,
                                        'virtual_height': -227582962,
                                    },
                            {
                                        'source_monitor': 1117725,
                                        'source_nw_x_pixel': -4789881751684932848,
                                        'source_nw_y_pixel': -7873944582965776356,
                                        'source_pixel_width': -2992959566718086547,
                                        'source_pixel_height': -4115651807004790516,
                                        'rotation': -8997526737624312394,
                                        'virtual_nw_x_pixel': -429201286,
                                        'virtual_nw_y_pixel': -1639746620,
                                        'virtual_width': 1530355838,
                                        'virtual_height': 187597156,
                                    },
                            {
                                        'source_monitor': 146679,
                                        'source_nw_x_pixel': -2995571617745755740,
                                        'source_nw_y_pixel': -2295138156624914902,
                                        'source_pixel_width': -9085552110057129583,
                                        'source_pixel_height': -3639158650065569720,
                                        'rotation': -6236305086470401321,
                                        'virtual_nw_x_pixel': -1862926144,
                                        'virtual_nw_y_pixel': 1807800410,
                                        'virtual_width': 702186441,
                                        'virtual_height': -1157538753,
                                    },
                            {
                                        'source_monitor': 6005193,
                                        'source_nw_x_pixel': -562480821302171069,
                                        'source_nw_y_pixel': -2653712293703871239,
                                        'source_pixel_width': -6568967415410665894,
                                        'source_pixel_height': -4321489221760950542,
                                        'rotation': -8121009037109102557,
                                        'virtual_nw_x_pixel': -383126874,
                                        'virtual_nw_y_pixel': 1842960800,
                                        'virtual_width': 281704561,
                                        'virtual_height': 268729340,
                                    },
                            {
                                        'source_monitor': 6818282,
                                        'source_nw_x_pixel': -2414779495160271773,
                                        'source_nw_y_pixel': -3489368949037120886,
                                        'source_pixel_width': -6768391508829861760,
                                        'source_pixel_height': -8111946075281590984,
                                        'rotation': -4847205655908757833,
                                        'virtual_nw_x_pixel': 229051656,
                                        'virtual_nw_y_pixel': -1258167331,
                                        'virtual_width': 1820859267,
                                        'virtual_height': 1616157074,
                                    },
                            {
                                        'source_monitor': 7655480,
                                        'source_nw_x_pixel': -5436265415849446506,
                                        'source_nw_y_pixel': -8982600984948569931,
                                        'source_pixel_width': -5471860607768101462,
                                        'source_pixel_height': -2865619481610304396,
                                        'rotation': -6668368581827689329,
                                        'virtual_nw_x_pixel': -322324574,
                                        'virtual_nw_y_pixel': -1366742048,
                                        'virtual_width': 1401729058,
                                        'virtual_height': 834535779,
                                    },
                            {
                                        'source_monitor': 3732131,
                                        'source_nw_x_pixel': -3423446196609649821,
                                        'source_nw_y_pixel': -4360522082655583033,
                                        'source_pixel_width': -3242356269076646540,
                                        'source_pixel_height': -8029491046246103284,
                                        'rotation': -3600513443107923520,
                                        'virtual_nw_x_pixel': 1126780073,
                                        'virtual_nw_y_pixel': -781344271,
                                        'virtual_width': 1196080512,
                                        'virtual_height': -1051287401,
                                    },
                            {
                                        'source_monitor': 3813132,
                                        'source_nw_x_pixel': -4956613557422892694,
                                        'source_nw_y_pixel': -614416378182145815,
                                        'source_pixel_width': -8250419435159066343,
                                        'source_pixel_height': -6243311359114546765,
                                        'rotation': -2734937164724182422,
                                        'virtual_nw_x_pixel': -45520313,
                                        'virtual_nw_y_pixel': 1280195815,
                                        'virtual_width': 364638875,
                                        'virtual_height': -219541610,
                                    },
                            {
                                        'source_monitor': 8585174,
                                        'source_nw_x_pixel': -5571343525461189805,
                                        'source_nw_y_pixel': -7253143365507967889,
                                        'source_pixel_width': -9056677988609879438,
                                        'source_pixel_height': -875645453664158534,
                                        'rotation': -5463236304528721769,
                                        'virtual_nw_x_pixel': -944164291,
                                        'virtual_nw_y_pixel': 253172299,
                                        'virtual_width': 1524281483,
                                        'virtual_height': 920049858,
                                    },
                        ],
                },
                {
                    'description': '#nљӷūиģǠʀӓԍŮ:{ɻŸółüĥ\x92Řϟȉҵ¸ɜɞŇ\\',
                    'monitors': [
                            {
                                        'identifier': 7396019,
                                        'width': 591396647725560204,
                                        'height': 3483963468823878065,
                                    },
                            {
                                        'identifier': 2432135,
                                        'width': 8510963112089361850,
                                        'height': -5177958459745020464,
                                    },
                            {
                                        'identifier': 8633336,
                                        'width': -6718101294461861012,
                                        'height': -8532651114037306120,
                                    },
                            {
                                        'identifier': -886548,
                                        'width': -9040979957179991804,
                                        'height': 186810349512261774,
                                    },
                            {
                                        'identifier': 4641658,
                                        'width': 961629766679890902,
                                        'height': 7468238086061274865,
                                    },
                            {
                                        'identifier': 8332180,
                                        'width': 1784859033164709883,
                                        'height': 8628407690755729989,
                                    },
                            {
                                        'identifier': 8296513,
                                        'width': -2645011039609486466,
                                        'height': -8665484055362727909,
                                    },
                            {
                                        'identifier': 1926146,
                                        'width': -2598355916619041936,
                                        'height': -447541286428864143,
                                    },
                            {
                                        'identifier': 1081334,
                                        'width': 1815225376919732807,
                                        'height': 1760270484623091923,
                                    },
                            {
                                        'identifier': 9567946,
                                        'width': 7145958525514240811,
                                        'height': 5416183835563861047,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5324744,
                                        'source_nw_x_pixel': -2240203288547244147,
                                        'source_nw_y_pixel': -8371923740652410394,
                                        'source_pixel_width': -3417447672153159057,
                                        'source_pixel_height': -2879458750940882305,
                                        'rotation': -6351817436403270363,
                                        'virtual_nw_x_pixel': 199107864,
                                        'virtual_nw_y_pixel': -1230119719,
                                        'virtual_width': -61677135,
                                        'virtual_height': -768209136,
                                    },
                            {
                                        'source_monitor': 7071623,
                                        'source_nw_x_pixel': -4834521880419525402,
                                        'source_nw_y_pixel': -8385542265664339795,
                                        'source_pixel_width': -1050918779666338341,
                                        'source_pixel_height': -5546951173114450885,
                                        'rotation': -7449396250824306701,
                                        'virtual_nw_x_pixel': -1115135356,
                                        'virtual_nw_y_pixel': -1352438444,
                                        'virtual_width': 280198157,
                                        'virtual_height': -773196321,
                                    },
                            {
                                        'source_monitor': 5842286,
                                        'source_nw_x_pixel': -1885213170709124311,
                                        'source_nw_y_pixel': -7793061836396266653,
                                        'source_pixel_width': -8012044825274159213,
                                        'source_pixel_height': -6213627019127207033,
                                        'rotation': -8038903486091829460,
                                        'virtual_nw_x_pixel': -1368002388,
                                        'virtual_nw_y_pixel': -1632333591,
                                        'virtual_width': 167115692,
                                        'virtual_height': -1485290241,
                                    },
                            {
                                        'source_monitor': 2963649,
                                        'source_nw_x_pixel': -5767408661557475106,
                                        'source_nw_y_pixel': -3321577297367419672,
                                        'source_pixel_width': -5170511747565084921,
                                        'source_pixel_height': -2006531220230937047,
                                        'rotation': -7620253874707266704,
                                        'virtual_nw_x_pixel': 1078429636,
                                        'virtual_nw_y_pixel': 818241257,
                                        'virtual_width': -1600190904,
                                        'virtual_height': 235389034,
                                    },
                            {
                                        'source_monitor': 312218,
                                        'source_nw_x_pixel': -7956750712332947319,
                                        'source_nw_y_pixel': -8786133457571141533,
                                        'source_pixel_width': -2341484546218709945,
                                        'source_pixel_height': -8971445279036294855,
                                        'rotation': -3643122451597404560,
                                        'virtual_nw_x_pixel': 1796651274,
                                        'virtual_nw_y_pixel': -1643465254,
                                        'virtual_width': 1800283011,
                                        'virtual_height': -796486847,
                                    },
                            {
                                        'source_monitor': 9773120,
                                        'source_nw_x_pixel': -3216734273556091789,
                                        'source_nw_y_pixel': -8582562261934401665,
                                        'source_pixel_width': -3057674565301412096,
                                        'source_pixel_height': -1403305399713684558,
                                        'rotation': -3004411241959140055,
                                        'virtual_nw_x_pixel': -373595105,
                                        'virtual_nw_y_pixel': 14744563,
                                        'virtual_width': 1308690345,
                                        'virtual_height': 1304116811,
                                    },
                            {
                                        'source_monitor': 1170422,
                                        'source_nw_x_pixel': -2863561166476191221,
                                        'source_nw_y_pixel': -7365441531059838644,
                                        'source_pixel_width': -6239058731251345760,
                                        'source_pixel_height': -985844431785228702,
                                        'rotation': -9037781154746490416,
                                        'virtual_nw_x_pixel': 631272105,
                                        'virtual_nw_y_pixel': -166990068,
                                        'virtual_width': 24018530,
                                        'virtual_height': 1737704207,
                                    },
                            {
                                        'source_monitor': 3108403,
                                        'source_nw_x_pixel': -6755866563936408640,
                                        'source_nw_y_pixel': -4595734981907181741,
                                        'source_pixel_width': -6602733075675723756,
                                        'source_pixel_height': -1979108331673703506,
                                        'rotation': -4230727569381844605,
                                        'virtual_nw_x_pixel': -736628584,
                                        'virtual_nw_y_pixel': 420085936,
                                        'virtual_width': 1711635868,
                                        'virtual_height': 175162078,
                                    },
                            {
                                        'source_monitor': 3267079,
                                        'source_nw_x_pixel': -4643177554633158472,
                                        'source_nw_y_pixel': -2449138959800833073,
                                        'source_pixel_width': -7519944112923001801,
                                        'source_pixel_height': -1893629391658176392,
                                        'rotation': -657174263550885757,
                                        'virtual_nw_x_pixel': -419847960,
                                        'virtual_nw_y_pixel': 991768839,
                                        'virtual_width': 448780698,
                                        'virtual_height': -1231672877,
                                    },
                            {
                                        'source_monitor': 447026,
                                        'source_nw_x_pixel': -3455369366101046628,
                                        'source_nw_y_pixel': -3228323104695787223,
                                        'source_pixel_width': -5756714020470547901,
                                        'source_pixel_height': -2546778492641397153,
                                        'rotation': -6790621579327235719,
                                        'virtual_nw_x_pixel': -1767527382,
                                        'virtual_nw_y_pixel': -1652663420,
                                        'virtual_width': -1862106110,
                                        'virtual_height': -922406834,
                                    },
                        ],
                },
                {
                    'description': 'υҒΤȊƢӿųIεаΕʺЗɷǷǇДƗǽƬǺÖѐȊПųʒүǎd',
                    'monitors': [
                            {
                                        'identifier': 9785000,
                                        'width': 4123733199736499001,
                                        'height': -5736536405849356483,
                                    },
                            {
                                        'identifier': 5294630,
                                        'width': -5545197433133826182,
                                        'height': -5734378333823547706,
                                    },
                            {
                                        'identifier': 1319956,
                                        'width': 5486296957721734444,
                                        'height': -7580569893657231985,
                                    },
                            {
                                        'identifier': 9248743,
                                        'width': 7854107773354143706,
                                        'height': -4453053037007117475,
                                    },
                            {
                                        'identifier': 3868017,
                                        'width': 1202605648773327428,
                                        'height': 6646816843628800424,
                                    },
                            {
                                        'identifier': 3785268,
                                        'width': 7980331716590464545,
                                        'height': 9138982241424407487,
                                    },
                            {
                                        'identifier': 2770346,
                                        'width': -4252168035888699751,
                                        'height': 1328359203046845242,
                                    },
                            {
                                        'identifier': 3726772,
                                        'width': -8482821064790921101,
                                        'height': -5978289539382870761,
                                    },
                            {
                                        'identifier': 9342176,
                                        'width': -3393576731410616182,
                                        'height': 5586063330043071375,
                                    },
                            {
                                        'identifier': 5892261,
                                        'width': 2531255141211485907,
                                        'height': -2711750614123237309,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -895321,
                                        'source_nw_x_pixel': -9154639985969404579,
                                        'source_nw_y_pixel': -6042150939964259325,
                                        'source_pixel_width': -938061419864484602,
                                        'source_pixel_height': -710436760975665804,
                                        'rotation': -8796273835941532916,
                                        'virtual_nw_x_pixel': -1994538881,
                                        'virtual_nw_y_pixel': 608389415,
                                        'virtual_width': -1131145841,
                                        'virtual_height': 1719780444,
                                    },
                            {
                                        'source_monitor': 8843010,
                                        'source_nw_x_pixel': -340375386779317240,
                                        'source_nw_y_pixel': -5080836938401736179,
                                        'source_pixel_width': -2707310395986293871,
                                        'source_pixel_height': -6593290103208157370,
                                        'rotation': -5981977966589790927,
                                        'virtual_nw_x_pixel': 1416054564,
                                        'virtual_nw_y_pixel': 1058091023,
                                        'virtual_width': 684924551,
                                        'virtual_height': 612642995,
                                    },
                            {
                                        'source_monitor': 2684973,
                                        'source_nw_x_pixel': -7828320566963301788,
                                        'source_nw_y_pixel': -6918203790674927485,
                                        'source_pixel_width': -8968042388044537634,
                                        'source_pixel_height': -2691814936239343586,
                                        'rotation': -1045862179551106036,
                                        'virtual_nw_x_pixel': 687453302,
                                        'virtual_nw_y_pixel': -1283977295,
                                        'virtual_width': 439870536,
                                        'virtual_height': 280159665,
                                    },
                            {
                                        'source_monitor': 8647546,
                                        'source_nw_x_pixel': -4046966019045547006,
                                        'source_nw_y_pixel': -2989645123094475415,
                                        'source_pixel_width': -6633033912399079422,
                                        'source_pixel_height': -2511943472891390736,
                                        'rotation': -6059048628203263422,
                                        'virtual_nw_x_pixel': 91317473,
                                        'virtual_nw_y_pixel': -1975841789,
                                        'virtual_width': -20471139,
                                        'virtual_height': -1237954335,
                                    },
                            {
                                        'source_monitor': 9387012,
                                        'source_nw_x_pixel': -6483117492118535829,
                                        'source_nw_y_pixel': -4483816818209195966,
                                        'source_pixel_width': -1503730468879958339,
                                        'source_pixel_height': -8991698175743337750,
                                        'rotation': -5391198755389957247,
                                        'virtual_nw_x_pixel': -321818756,
                                        'virtual_nw_y_pixel': 26825467,
                                        'virtual_width': -1137014669,
                                        'virtual_height': -72874341,
                                    },
                            {
                                        'source_monitor': 9386220,
                                        'source_nw_x_pixel': -7222159546046069015,
                                        'source_nw_y_pixel': -3750867049459560148,
                                        'source_pixel_width': -4254296635858906081,
                                        'source_pixel_height': -2393632621184575565,
                                        'rotation': -3670518142688377571,
                                        'virtual_nw_x_pixel': 1513739135,
                                        'virtual_nw_y_pixel': -382999423,
                                        'virtual_width': -415433796,
                                        'virtual_height': -1532930024,
                                    },
                            {
                                        'source_monitor': 2811860,
                                        'source_nw_x_pixel': -9141013200220323306,
                                        'source_nw_y_pixel': -861497637593479146,
                                        'source_pixel_width': -1209606158546405282,
                                        'source_pixel_height': -835380535537406215,
                                        'rotation': -1746689212303446473,
                                        'virtual_nw_x_pixel': 1891949710,
                                        'virtual_nw_y_pixel': -745813113,
                                        'virtual_width': -1163100848,
                                        'virtual_height': -1946803339,
                                    },
                            {
                                        'source_monitor': 8567707,
                                        'source_nw_x_pixel': -1639124247887554432,
                                        'source_nw_y_pixel': -2095020941588105498,
                                        'source_pixel_width': -4815304676588327535,
                                        'source_pixel_height': -915004870292896287,
                                        'rotation': -5920372362622683964,
                                        'virtual_nw_x_pixel': 11459893,
                                        'virtual_nw_y_pixel': -1549041456,
                                        'virtual_width': -253940116,
                                        'virtual_height': -806961509,
                                    },
                            {
                                        'source_monitor': 954146,
                                        'source_nw_x_pixel': -4551259225180930197,
                                        'source_nw_y_pixel': -2801564303952718760,
                                        'source_pixel_width': -5509150706643239664,
                                        'source_pixel_height': -7522175009654729524,
                                        'rotation': -2623420303180268819,
                                        'virtual_nw_x_pixel': -1330200974,
                                        'virtual_nw_y_pixel': -1465757775,
                                        'virtual_width': 460185647,
                                        'virtual_height': -118673940,
                                    },
                            {
                                        'source_monitor': 3368788,
                                        'source_nw_x_pixel': -2519962831509830636,
                                        'source_nw_y_pixel': -8794589119119505915,
                                        'source_pixel_width': -8791903886548419058,
                                        'source_pixel_height': -2657134699867525821,
                                        'rotation': -8932878385305729755,
                                        'virtual_nw_x_pixel': 695750888,
                                        'virtual_nw_y_pixel': 1368851779,
                                        'virtual_width': -1845165255,
                                        'virtual_height': -222625674,
                                    },
                        ],
                },
                {
                    'description': 'їʁͷƺǬӼϘӭƗőҞԠƼƃǺĲŉƆɀҩʺ4ÒñĈάȎ҈ċǒ',
                    'monitors': [
                            {
                                        'identifier': 8622526,
                                        'width': -4505538679139998440,
                                        'height': -8683987573811421198,
                                    },
                            {
                                        'identifier': 9000757,
                                        'width': -4127060663144227781,
                                        'height': 1652491517991976250,
                                    },
                            {
                                        'identifier': 2090439,
                                        'width': 4459374374296379044,
                                        'height': 6657426662281102354,
                                    },
                            {
                                        'identifier': 3095955,
                                        'width': 2944547273962734565,
                                        'height': 1106519992913618536,
                                    },
                            {
                                        'identifier': 4836015,
                                        'width': 6088490822601668874,
                                        'height': -5359616996134123534,
                                    },
                            {
                                        'identifier': 5155032,
                                        'width': -972406181782035844,
                                        'height': 5181071946655380193,
                                    },
                            {
                                        'identifier': 3747765,
                                        'width': 7571750249399039727,
                                        'height': 9214185643026730137,
                                    },
                            {
                                        'identifier': 8085853,
                                        'width': 4905893807034809461,
                                        'height': -3899425368608107215,
                                    },
                            {
                                        'identifier': 3382078,
                                        'width': 8154176284539483974,
                                        'height': -4565879404520039849,
                                    },
                            {
                                        'identifier': 9445515,
                                        'width': -1912726358940019310,
                                        'height': -7040632132130762235,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5166261,
                                        'source_nw_x_pixel': -4274984867671558410,
                                        'source_nw_y_pixel': -4552609432297886679,
                                        'source_pixel_width': -5797613578751059612,
                                        'source_pixel_height': -6650133059594544503,
                                        'rotation': -297075791909419652,
                                        'virtual_nw_x_pixel': -794173795,
                                        'virtual_nw_y_pixel': 1055785458,
                                        'virtual_width': 619898902,
                                        'virtual_height': 1267646308,
                                    },
                            {
                                        'source_monitor': 2444657,
                                        'source_nw_x_pixel': -4967337413222556873,
                                        'source_nw_y_pixel': -6493736000347821307,
                                        'source_pixel_width': -4378496121815939959,
                                        'source_pixel_height': -7268439777965614987,
                                        'rotation': -5073077846287033776,
                                        'virtual_nw_x_pixel': -1406137635,
                                        'virtual_nw_y_pixel': 148579392,
                                        'virtual_width': -1059112692,
                                        'virtual_height': 1153357571,
                                    },
                            {
                                        'source_monitor': 7335569,
                                        'source_nw_x_pixel': -4551043243436383802,
                                        'source_nw_y_pixel': -4848263087918777192,
                                        'source_pixel_width': -7834069128549174539,
                                        'source_pixel_height': -7853040261183668970,
                                        'rotation': -2953209800501280375,
                                        'virtual_nw_x_pixel': -1986714380,
                                        'virtual_nw_y_pixel': -1193814148,
                                        'virtual_width': -1297088242,
                                        'virtual_height': -538672342,
                                    },
                            {
                                        'source_monitor': 8972063,
                                        'source_nw_x_pixel': -8335742275358007544,
                                        'source_nw_y_pixel': -255263464908704238,
                                        'source_pixel_width': -997618553997188582,
                                        'source_pixel_height': -2133505122731920359,
                                        'rotation': -6366106996588561086,
                                        'virtual_nw_x_pixel': -1218571088,
                                        'virtual_nw_y_pixel': -952136822,
                                        'virtual_width': -679772379,
                                        'virtual_height': 1836307763,
                                    },
                            {
                                        'source_monitor': 7543996,
                                        'source_nw_x_pixel': -3933587244167735552,
                                        'source_nw_y_pixel': -6334959813891773176,
                                        'source_pixel_width': -213092025768119669,
                                        'source_pixel_height': -1961897386670385905,
                                        'rotation': -4847773617209684662,
                                        'virtual_nw_x_pixel': 1851405165,
                                        'virtual_nw_y_pixel': 279460766,
                                        'virtual_width': 1856133653,
                                        'virtual_height': 1105865719,
                                    },
                            {
                                        'source_monitor': 5029986,
                                        'source_nw_x_pixel': -5013917737207940945,
                                        'source_nw_y_pixel': -5021640359654705765,
                                        'source_pixel_width': -2926935445464588771,
                                        'source_pixel_height': -8426523447144231906,
                                        'rotation': -3801665783701631567,
                                        'virtual_nw_x_pixel': -1150970859,
                                        'virtual_nw_y_pixel': -337168053,
                                        'virtual_width': -853663314,
                                        'virtual_height': 1233984895,
                                    },
                            {
                                        'source_monitor': 1334660,
                                        'source_nw_x_pixel': -3326862675441350200,
                                        'source_nw_y_pixel': -2526571060741304574,
                                        'source_pixel_width': -1166731238227710110,
                                        'source_pixel_height': -2540770211857279064,
                                        'rotation': -7637860997989317504,
                                        'virtual_nw_x_pixel': 1620884019,
                                        'virtual_nw_y_pixel': 1917865041,
                                        'virtual_width': 1594681455,
                                        'virtual_height': 830711696,
                                    },
                            {
                                        'source_monitor': 7798224,
                                        'source_nw_x_pixel': -8394547292296842690,
                                        'source_nw_y_pixel': -274977844795559235,
                                        'source_pixel_width': -7644756226984578211,
                                        'source_pixel_height': -1477796871039481612,
                                        'rotation': -9016736135823144013,
                                        'virtual_nw_x_pixel': 19964651,
                                        'virtual_nw_y_pixel': -159145301,
                                        'virtual_width': 333071991,
                                        'virtual_height': -721082538,
                                    },
                            {
                                        'source_monitor': 6884897,
                                        'source_nw_x_pixel': -4380156668974381859,
                                        'source_nw_y_pixel': -4307000410917521248,
                                        'source_pixel_width': -6081997954646185538,
                                        'source_pixel_height': -4085566745998964437,
                                        'rotation': -7207501672795620310,
                                        'virtual_nw_x_pixel': 859440764,
                                        'virtual_nw_y_pixel': 1782927655,
                                        'virtual_width': -366147962,
                                        'virtual_height': -1155922829,
                                    },
                            {
                                        'source_monitor': 3827627,
                                        'source_nw_x_pixel': -8332911453908141531,
                                        'source_nw_y_pixel': -4921258092764460346,
                                        'source_pixel_width': -1769239892519827644,
                                        'source_pixel_height': -43945065369436200,
                                        'rotation': -5618585135697254626,
                                        'virtual_nw_x_pixel': 4625963,
                                        'virtual_nw_y_pixel': 196539688,
                                        'virtual_width': 1781474556,
                                        'virtual_height': -1709568399,
                                    },
                        ],
                },
                {
                    'description': 'ťɻɚӖӼΟǺҾșҐƶŀÜХȽэѡʃăҼʂòñÏ\x91Ѯ°Ŕъč',
                    'monitors': [
                            {
                                        'identifier': 3791756,
                                        'width': 6060076053653990596,
                                        'height': -4442665323996838647,
                                    },
                            {
                                        'identifier': 5802668,
                                        'width': 8323130492391902174,
                                        'height': 5932193715059468567,
                                    },
                            {
                                        'identifier': 1009382,
                                        'width': 2699887392653889330,
                                        'height': 2072343706974383944,
                                    },
                            {
                                        'identifier': 6813245,
                                        'width': 3327516080662760955,
                                        'height': -7513672696863800127,
                                    },
                            {
                                        'identifier': 4122759,
                                        'width': -4948509988003376229,
                                        'height': -8026271782540883962,
                                    },
                            {
                                        'identifier': 3998264,
                                        'width': -2389099117405395182,
                                        'height': -7905527403577789996,
                                    },
                            {
                                        'identifier': 9452515,
                                        'width': -1710102248141134122,
                                        'height': 6895650666937303706,
                                    },
                            {
                                        'identifier': 649220,
                                        'width': -281524699407273753,
                                        'height': -4272270797128883598,
                                    },
                            {
                                        'identifier': -522829,
                                        'width': 2862619863616143908,
                                        'height': -2720121841737296865,
                                    },
                            {
                                        'identifier': 341531,
                                        'width': -883954190474645649,
                                        'height': -8579747371686360490,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8462174,
                                        'source_nw_x_pixel': -7943936084055864841,
                                        'source_nw_y_pixel': -8347453039331850495,
                                        'source_pixel_width': -2615556869680377027,
                                        'source_pixel_height': -3837028818535530398,
                                        'rotation': -3145287452254317858,
                                        'virtual_nw_x_pixel': 1865417181,
                                        'virtual_nw_y_pixel': -653039930,
                                        'virtual_width': -1009751135,
                                        'virtual_height': 1301289408,
                                    },
                            {
                                        'source_monitor': 2570298,
                                        'source_nw_x_pixel': -1717815750112390806,
                                        'source_nw_y_pixel': -6827998441296081766,
                                        'source_pixel_width': -7937402585842925595,
                                        'source_pixel_height': -6752704502623473617,
                                        'rotation': -8367428477957392004,
                                        'virtual_nw_x_pixel': -1982016028,
                                        'virtual_nw_y_pixel': -750541534,
                                        'virtual_width': 1030396926,
                                        'virtual_height': -719463783,
                                    },
                            {
                                        'source_monitor': 4377715,
                                        'source_nw_x_pixel': -5396331816915226958,
                                        'source_nw_y_pixel': -7105468240675454815,
                                        'source_pixel_width': -8909610096819992686,
                                        'source_pixel_height': -4194136049296225844,
                                        'rotation': -4412473798211371361,
                                        'virtual_nw_x_pixel': 623445237,
                                        'virtual_nw_y_pixel': 1066291349,
                                        'virtual_width': -65045377,
                                        'virtual_height': 781277288,
                                    },
                            {
                                        'source_monitor': 3390016,
                                        'source_nw_x_pixel': -7303540641366013794,
                                        'source_nw_y_pixel': -3660513810344072551,
                                        'source_pixel_width': -1363124661894788648,
                                        'source_pixel_height': -7550910351734264569,
                                        'rotation': -7711071218052761968,
                                        'virtual_nw_x_pixel': -1144006821,
                                        'virtual_nw_y_pixel': -1722072851,
                                        'virtual_width': -1014309720,
                                        'virtual_height': -322199714,
                                    },
                            {
                                        'source_monitor': 1619603,
                                        'source_nw_x_pixel': -1318039090294901150,
                                        'source_nw_y_pixel': -7620630010518115255,
                                        'source_pixel_width': -3078767245805119360,
                                        'source_pixel_height': -4384060284190362844,
                                        'rotation': -7685779091180093446,
                                        'virtual_nw_x_pixel': -783815118,
                                        'virtual_nw_y_pixel': -677815151,
                                        'virtual_width': 1347109120,
                                        'virtual_height': -1403131227,
                                    },
                            {
                                        'source_monitor': 190909,
                                        'source_nw_x_pixel': -6489313460801337789,
                                        'source_nw_y_pixel': -4726359045481485030,
                                        'source_pixel_width': -3897340343048247423,
                                        'source_pixel_height': -44675521328713164,
                                        'rotation': -6044043381115717670,
                                        'virtual_nw_x_pixel': 839945150,
                                        'virtual_nw_y_pixel': -253292001,
                                        'virtual_width': 330282072,
                                        'virtual_height': 17383676,
                                    },
                            {
                                        'source_monitor': 7314877,
                                        'source_nw_x_pixel': -7835986685642940641,
                                        'source_nw_y_pixel': -3555864200299321622,
                                        'source_pixel_width': -7882102513351586131,
                                        'source_pixel_height': -5738432531090929846,
                                        'rotation': -1967378986384130486,
                                        'virtual_nw_x_pixel': -436721443,
                                        'virtual_nw_y_pixel': 1576198247,
                                        'virtual_width': 1096693037,
                                        'virtual_height': -290609639,
                                    },
                            {
                                        'source_monitor': 2559384,
                                        'source_nw_x_pixel': -4817680656618536718,
                                        'source_nw_y_pixel': -713259352374459421,
                                        'source_pixel_width': -352014177138920417,
                                        'source_pixel_height': -809842824823883432,
                                        'rotation': -5201452931248823995,
                                        'virtual_nw_x_pixel': -235599064,
                                        'virtual_nw_y_pixel': -1688554972,
                                        'virtual_width': 1125546283,
                                        'virtual_height': -1800911226,
                                    },
                            {
                                        'source_monitor': 4213658,
                                        'source_nw_x_pixel': -4615161079340535945,
                                        'source_nw_y_pixel': -7553686369452527923,
                                        'source_pixel_width': -4970387628590932084,
                                        'source_pixel_height': -6319447691433515683,
                                        'rotation': -1438516526037093321,
                                        'virtual_nw_x_pixel': 1002494026,
                                        'virtual_nw_y_pixel': -682984236,
                                        'virtual_width': -711886519,
                                        'virtual_height': 56111779,
                                    },
                            {
                                        'source_monitor': -683074,
                                        'source_nw_x_pixel': -3978992013347042070,
                                        'source_nw_y_pixel': -4417979039863597603,
                                        'source_pixel_width': -453061924521947656,
                                        'source_pixel_height': -4680244155780027320,
                                        'rotation': -7659358189928853264,
                                        'virtual_nw_x_pixel': 730034068,
                                        'virtual_nw_y_pixel': 710849694,
                                        'virtual_width': -155705360,
                                        'virtual_height': 275173916,
                                    },
                        ],
                },
                {
                    'description': 'μѤgÁҳÓѼԙoʑǅ\x9b:ӖϱΡСԗɣɟ˟ϜʬƐ&ĹŭԤǦџ',
                    'monitors': [
                            {
                                        'identifier': 2377972,
                                        'width': -7040225885467066348,
                                        'height': 7675407538956698858,
                                    },
                            {
                                        'identifier': 8510230,
                                        'width': 3850792056269799688,
                                        'height': -1812215472778991882,
                                    },
                            {
                                        'identifier': 6590221,
                                        'width': -8879530881128591425,
                                        'height': 6949553513082755958,
                                    },
                            {
                                        'identifier': 8517867,
                                        'width': -8041686687955479642,
                                        'height': -4965821292639163547,
                                    },
                            {
                                        'identifier': 401449,
                                        'width': 9111482626220956046,
                                        'height': -1538555753055242643,
                                    },
                            {
                                        'identifier': 7828803,
                                        'width': 7369755084809886087,
                                        'height': -967168780467951823,
                                    },
                            {
                                        'identifier': -310530,
                                        'width': -6659720564780022090,
                                        'height': 2760021500184005402,
                                    },
                            {
                                        'identifier': 2631910,
                                        'width': -1587086761562987997,
                                        'height': -4469448785847207109,
                                    },
                            {
                                        'identifier': 3767749,
                                        'width': 3940289197068894314,
                                        'height': 1718127359131044656,
                                    },
                            {
                                        'identifier': 5271474,
                                        'width': -1893874037112590095,
                                        'height': -8250849746079576667,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9676042,
                                        'source_nw_x_pixel': -8585055237931536811,
                                        'source_nw_y_pixel': -8048536307429559416,
                                        'source_pixel_width': -6241349312771308788,
                                        'source_pixel_height': -2605724103540567140,
                                        'rotation': -3928989034985824858,
                                        'virtual_nw_x_pixel': -164415851,
                                        'virtual_nw_y_pixel': 181117021,
                                        'virtual_width': 1027845066,
                                        'virtual_height': 805282766,
                                    },
                            {
                                        'source_monitor': 1726407,
                                        'source_nw_x_pixel': -4170361995957571410,
                                        'source_nw_y_pixel': -8532816590489360089,
                                        'source_pixel_width': -6884584723313194799,
                                        'source_pixel_height': -2947699348590503323,
                                        'rotation': -7288471618349105827,
                                        'virtual_nw_x_pixel': -1064342097,
                                        'virtual_nw_y_pixel': -1776965032,
                                        'virtual_width': 1454818685,
                                        'virtual_height': 1989974181,
                                    },
                            {
                                        'source_monitor': 801715,
                                        'source_nw_x_pixel': -8913071982521528191,
                                        'source_nw_y_pixel': -2376900942432938708,
                                        'source_pixel_width': -4230212000549930306,
                                        'source_pixel_height': -6796250994985912023,
                                        'rotation': -6943052778089397261,
                                        'virtual_nw_x_pixel': -278917759,
                                        'virtual_nw_y_pixel': -622505184,
                                        'virtual_width': 1275404352,
                                        'virtual_height': -495041962,
                                    },
                            {
                                        'source_monitor': 787227,
                                        'source_nw_x_pixel': -2175417665203934204,
                                        'source_nw_y_pixel': -3590795348046258501,
                                        'source_pixel_width': -2448033860862262773,
                                        'source_pixel_height': -2107291290825908743,
                                        'rotation': -4237532737316547171,
                                        'virtual_nw_x_pixel': 110858298,
                                        'virtual_nw_y_pixel': -1245031028,
                                        'virtual_width': 1383827811,
                                        'virtual_height': -1917687980,
                                    },
                            {
                                        'source_monitor': 423603,
                                        'source_nw_x_pixel': -4172082155645052616,
                                        'source_nw_y_pixel': -6949110129986310608,
                                        'source_pixel_width': -7229651060971841244,
                                        'source_pixel_height': -8390296109659455665,
                                        'rotation': -5014579436547503256,
                                        'virtual_nw_x_pixel': -1520712580,
                                        'virtual_nw_y_pixel': -730245930,
                                        'virtual_width': 1808046290,
                                        'virtual_height': 1179102866,
                                    },
                            {
                                        'source_monitor': 8282289,
                                        'source_nw_x_pixel': -9167361224826854778,
                                        'source_nw_y_pixel': -2666671916729781366,
                                        'source_pixel_width': -2111569813851226205,
                                        'source_pixel_height': -8501941052495630282,
                                        'rotation': -503026763776955129,
                                        'virtual_nw_x_pixel': 671772252,
                                        'virtual_nw_y_pixel': -1153579895,
                                        'virtual_width': -1601596134,
                                        'virtual_height': 1984810208,
                                    },
                            {
                                        'source_monitor': 2885422,
                                        'source_nw_x_pixel': -2964872937263357264,
                                        'source_nw_y_pixel': -5299991668374650819,
                                        'source_pixel_width': -6411210020664745676,
                                        'source_pixel_height': -2188038325260218588,
                                        'rotation': -907402871088772368,
                                        'virtual_nw_x_pixel': -865935112,
                                        'virtual_nw_y_pixel': 1888576938,
                                        'virtual_width': -1394432577,
                                        'virtual_height': -761879790,
                                    },
                            {
                                        'source_monitor': 6945026,
                                        'source_nw_x_pixel': -5589003183407022838,
                                        'source_nw_y_pixel': -1309633275772880316,
                                        'source_pixel_width': -2255206091215011526,
                                        'source_pixel_height': -2991083674799440483,
                                        'rotation': -6259461425764518760,
                                        'virtual_nw_x_pixel': 1648452612,
                                        'virtual_nw_y_pixel': 738628513,
                                        'virtual_width': -1193738147,
                                        'virtual_height': 658865872,
                                    },
                            {
                                        'source_monitor': 7184038,
                                        'source_nw_x_pixel': -5028798032648274726,
                                        'source_nw_y_pixel': -553594603200686013,
                                        'source_pixel_width': -1583155655426687876,
                                        'source_pixel_height': -4802741936236320049,
                                        'rotation': -9026907468892648771,
                                        'virtual_nw_x_pixel': 216158895,
                                        'virtual_nw_y_pixel': -1292684642,
                                        'virtual_width': 1422338813,
                                        'virtual_height': -905897024,
                                    },
                            {
                                        'source_monitor': 3434862,
                                        'source_nw_x_pixel': -7607682517200604245,
                                        'source_nw_y_pixel': -3995799127393213680,
                                        'source_pixel_width': -6866521503980939938,
                                        'source_pixel_height': -7758285182828402934,
                                        'rotation': -4000424059870566255,
                                        'virtual_nw_x_pixel': -564135104,
                                        'virtual_nw_y_pixel': -1059809166,
                                        'virtual_width': 775479230,
                                        'virtual_height': 696173350,
                                    },
                        ],
                },
                {
                    'description': 'ȌʔϧэӣӯЀǧ±ӇІά҇źȐ\x86ïіҴɦӭȒϢҳŸǁĤϯͻҞ',
                    'monitors': [
                            {
                                        'identifier': 5541448,
                                        'width': 1447037850755778470,
                                        'height': 8774771272694081850,
                                    },
                            {
                                        'identifier': 2146248,
                                        'width': -9208592535210474849,
                                        'height': 534088615962994343,
                                    },
                            {
                                        'identifier': 5140524,
                                        'width': -5653396934646878767,
                                        'height': -3132603557939373417,
                                    },
                            {
                                        'identifier': 7684630,
                                        'width': 8261408628538906978,
                                        'height': 1152455699498802723,
                                    },
                            {
                                        'identifier': 3693684,
                                        'width': 5865436308573844076,
                                        'height': 519354799619362571,
                                    },
                            {
                                        'identifier': 9872953,
                                        'width': 1702065900250379941,
                                        'height': -332890765870574728,
                                    },
                            {
                                        'identifier': 1097684,
                                        'width': 2529598955151510525,
                                        'height': 4154150814772730278,
                                    },
                            {
                                        'identifier': 6491277,
                                        'width': 4999545887965618796,
                                        'height': -4949493896252762324,
                                    },
                            {
                                        'identifier': 1266110,
                                        'width': -7565848009758678772,
                                        'height': 7366877271881124298,
                                    },
                            {
                                        'identifier': -998506,
                                        'width': -6118093472972275126,
                                        'height': 6087750949384011503,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2818980,
                                        'source_nw_x_pixel': -2654380531617594549,
                                        'source_nw_y_pixel': -7866972311470769468,
                                        'source_pixel_width': -2390012110022909825,
                                        'source_pixel_height': -7587424327815809291,
                                        'rotation': -532198601907449850,
                                        'virtual_nw_x_pixel': 1162133029,
                                        'virtual_nw_y_pixel': -1615180535,
                                        'virtual_width': -1733376457,
                                        'virtual_height': 1255199575,
                                    },
                            {
                                        'source_monitor': 6996004,
                                        'source_nw_x_pixel': -2748724100381554202,
                                        'source_nw_y_pixel': -6210317120570240896,
                                        'source_pixel_width': -4497867215997055399,
                                        'source_pixel_height': -5972194909352497805,
                                        'rotation': -2847887985294045976,
                                        'virtual_nw_x_pixel': 510250107,
                                        'virtual_nw_y_pixel': -1744177668,
                                        'virtual_width': 417719311,
                                        'virtual_height': 1814346758,
                                    },
                            {
                                        'source_monitor': 5237397,
                                        'source_nw_x_pixel': -3364698875467100678,
                                        'source_nw_y_pixel': -3490876538324749946,
                                        'source_pixel_width': -2314715753856608141,
                                        'source_pixel_height': -3557664030579611881,
                                        'rotation': -6538865461041734290,
                                        'virtual_nw_x_pixel': -1427891162,
                                        'virtual_nw_y_pixel': 1667750674,
                                        'virtual_width': -1480259657,
                                        'virtual_height': -358213380,
                                    },
                            {
                                        'source_monitor': -465878,
                                        'source_nw_x_pixel': -548927382889496737,
                                        'source_nw_y_pixel': -7522155157595241942,
                                        'source_pixel_width': -3083556505513227795,
                                        'source_pixel_height': -3667825626383143690,
                                        'rotation': -7232295488411983982,
                                        'virtual_nw_x_pixel': -1858703222,
                                        'virtual_nw_y_pixel': -1232028785,
                                        'virtual_width': -1644521059,
                                        'virtual_height': 186824433,
                                    },
                            {
                                        'source_monitor': 4902337,
                                        'source_nw_x_pixel': -163671671084685965,
                                        'source_nw_y_pixel': -5003910355927845236,
                                        'source_pixel_width': -2170282432773020681,
                                        'source_pixel_height': -4369384388546270445,
                                        'rotation': -127770479671093479,
                                        'virtual_nw_x_pixel': -1240890190,
                                        'virtual_nw_y_pixel': -1289906906,
                                        'virtual_width': 319503846,
                                        'virtual_height': 34854124,
                                    },
                            {
                                        'source_monitor': 7672886,
                                        'source_nw_x_pixel': -6331939299845688456,
                                        'source_nw_y_pixel': -8025315641895580182,
                                        'source_pixel_width': -4103483415089237153,
                                        'source_pixel_height': -4289700132405941925,
                                        'rotation': -3561042697994047370,
                                        'virtual_nw_x_pixel': -1231460736,
                                        'virtual_nw_y_pixel': 1804882934,
                                        'virtual_width': 1248040088,
                                        'virtual_height': 127067222,
                                    },
                            {
                                        'source_monitor': 7544497,
                                        'source_nw_x_pixel': -8767151849827126739,
                                        'source_nw_y_pixel': -3149985131484892437,
                                        'source_pixel_width': -122760849671809023,
                                        'source_pixel_height': -359114848541832882,
                                        'rotation': -5948175745934147905,
                                        'virtual_nw_x_pixel': 1692209724,
                                        'virtual_nw_y_pixel': 1461941833,
                                        'virtual_width': -634726123,
                                        'virtual_height': -646128163,
                                    },
                            {
                                        'source_monitor': 3701424,
                                        'source_nw_x_pixel': -2487247621333243663,
                                        'source_nw_y_pixel': -2284337110586179005,
                                        'source_pixel_width': -2449765773584775844,
                                        'source_pixel_height': -2059014833703270159,
                                        'rotation': -8513013771298529497,
                                        'virtual_nw_x_pixel': 1526630694,
                                        'virtual_nw_y_pixel': 1160956950,
                                        'virtual_width': -230285517,
                                        'virtual_height': -1079801518,
                                    },
                            {
                                        'source_monitor': 8408012,
                                        'source_nw_x_pixel': -518747601157098024,
                                        'source_nw_y_pixel': -51101435258277082,
                                        'source_pixel_width': -5085035694190147189,
                                        'source_pixel_height': -2216773501156134740,
                                        'rotation': -6709488282656575299,
                                        'virtual_nw_x_pixel': 1094644929,
                                        'virtual_nw_y_pixel': 535997444,
                                        'virtual_width': -673581760,
                                        'virtual_height': -1830472609,
                                    },
                            {
                                        'source_monitor': 3530249,
                                        'source_nw_x_pixel': -1304748389043758852,
                                        'source_nw_y_pixel': -6362350976083078691,
                                        'source_pixel_width': -6614428520584961968,
                                        'source_pixel_height': -2129617492047600649,
                                        'rotation': -3752876841082557867,
                                        'virtual_nw_x_pixel': 541454502,
                                        'virtual_nw_y_pixel': 998895639,
                                        'virtual_width': 473921879,
                                        'virtual_height': -685614803,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 2458974,

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
            'request_id': 1466157,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 651077,

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
            '$': 'ӊ˂ҽЛǢѣãѠʉɻœϯɀ\x86ǤʏņоΨʍđăѬĳ(\x97Ѯ`ԏЬ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -8790941642779222766,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 847326.635382949,
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
            '$': '20210327:033245.107414:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ӖчDőϹ$VɋÞЗ8]Ҏ\u0381õƀѫҮгğҸũľӌΜϥǞʪƹɝ',
                'ѸɉμҴŕΣѶƶʝȜŞĬĝ˰ҴÎԦ\\ȳԌɔîBĊʧƷɜөγª',
                'ӲƞΤӅ/`҈ͳɇӕʛ|ƶϩɍǗРǀͰƋτ¼Ȁԉ"ϽӨӄЍ\u038b',
                'ő¢ëǔӤŏʽE\x9dǢȳӸȆȯĺƅȒқҜγчĖϰɖ҇ˊцąȁʌ',
                ';ȐЩɏƣӼĮ\x86ťȍӅƭÆҾρɾϘвʹǲʶ˖ϩчżӜÖӅ¢£',
                '\x9a\x92ΦͰȶӻƯ˺ǌƗѥÒː˒R°ϟŤӷɫ˹ˏɱƮҴȇǣпČɰ',
                'ʼWë\x93ƺ\x95vƋъŊþĘʷӆѼ+˭îӼ\x8c4ºɍðFȱϛ\u0383ƭР',
                'Ѩ®ԗђďи\u038bʟԏĮѽȊǞ˶όęʰӵӨŏӎ4ϢԥԤʪοɘɎЈ',
                'ӏŅ@ƗƞӤ\u0379ӅβÃĮʕϚPϿ˦șʘˋ«ѤˎͶ÷°ԚȓМ\u0381Μ',
                'Ӣ>ψ%;Å\x81\x97ƬŋʂңϜǃӼ\x91Ņ˝ҥ\u038bҨƯȡðDɀǣǴǛʅ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -6658204624849255247,
                8280477512346668942,
                -3321698899027108962,
                9060464659959662178,
                5922830765566177097,
                -2211520914173093029,
                1044628389262790461,
                -8498037508387103959,
                5718315227407564006,
                201136867385071836,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                828741.7532060273,
                -73948.75475726213,
                681911.4230713048,
                624986.4453124603,
                385372.4018399832,
                224810.59601406555,
                800748.192429286,
                767264.8087204536,
                317386.89512188017,
                243227.56248512387,
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
                False,
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
                '20210327:033245.973400:+0000',
                '20210327:033245.990916:+0000',
                '20210327:033246.008393:+0000',
                '20210327:033246.025788:+0000',
                '20210327:033246.043266:+0000',
                '20210327:033246.062635:+0000',
                '20210327:033246.080645:+0000',
                '20210327:033246.100026:+0000',
                '20210327:033246.118180:+0000',
                '20210327:033246.135843:+0000',
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
            'name': 'ã\x92҉',
            'value': {
                '^': 'datetime',
                '$': '20210327:033244.814564:+0000',
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ǖ',

            'value': {
                '^': 'int',
                '$': -4503710990355905891,
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
            'catalog': 'ǨɃĠ҉ǌùϕťͶĚϥáѤīƣёȤƣλ',
            'message': '¹Ӥ\u03a2ʡȜ×шүŘˢİщРӅĖςɼӌѲĬːξǌӶúƨǉȁƽã',
            'arguments': [
                {
                    'name': 'ķӭӞѽʿ[ΚҴɟ˓\x97ȇԘ\x8fӁɧƕǒňԫωȓǼ#Ʋǟ©īҠԇ',
                    'value': {
                            '^': 'float',
                            '$': -77550.42446431678,
                        },
                },
                {
                    'name': 'ıˬѐϒCŞ%ŚϏcΤɾǁҢ¬žԀØ7£Oʐ҂³',
                    'value': {
                            '^': 'int',
                            '$': 2570940730156259977,
                        },
                },
                {
                    'name': 'σ\x8fāэϾŵºʮʄ%ЉςҮ\u0382ѭ\x8bВҁҟӵÜқîüơй¯ƪčЋ',
                    'value': {
                            '^': 'float_list',
                            '$': [
                                        772568.6645496525,
                                        346380.24428823433,
                                        693468.6161828273,
                                        167997.75164660247,
                                        955296.9027258204,
                                        367821.6311305997,
                                        516658.4488309118,
                                        415100.7698477097,
                                        946952.623317735,
                                        -30413.278180853784,
                                    ],
                        },
                },
                {
                    'name': '˖ƛϗ҄Ѫϊ#ƒ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:033243.706435:+0000',
                                        '20210327:033243.721549:+0000',
                                        '20210327:033243.736954:+0000',
                                        '20210327:033243.751874:+0000',
                                        '20210327:033243.769654:+0000',
                                        '20210327:033243.787405:+0000',
                                        '20210327:033243.805611:+0000',
                                        '20210327:033243.822773:+0000',
                                        '20210327:033243.840200:+0000',
                                        '20210327:033243.858603:+0000',
                                    ],
                        },
                },
                {
                    'name': 'жȦ\x96<ŋԡʻӖӧѲ)Ăˌ5ЗÊˉƮщɍͷȌϤĶ0ŮˇƵԫƝ',
                    'value': {
                            '^': 'string',
                            '$': 'ʭ҄ʐʤϜԝÏ\x8dŶͽѱїΣͱǻĝŵƥϭъщхY·ʀÖHԀƴ҉',
                        },
                },
                {
                    'name': 'ҋԠԣѯ\xa0',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        True,
                                        False,
                                        True,
                                        True,
                                        True,
                                        False,
                                        True,
                                        True,
                                        False,
                                        False,
                                    ],
                        },
                },
                {
                    'name': 'ЪŐÔѤѱǜáͿĭŎѐϱŤКĴҊǄʩːƝӆ',
                    'value': {
                            '^': 'float',
                            '$': 987172.6461835925,
                        },
                },
                {
                    'name': 'βȞĿM˨Ęĩ\u0380',
                    'value': {
                            '^': 'string',
                            '$': 'ȒжÚϕƪƝӨǚǟ_ԥȢʸѦҩҁӭξ¼¹ΉÓ¤ˎƤŘ\x90ԛԨѦ',
                        },
                },
                {
                    'name': 'ҠŁΙĆʘ\x82ÈʎԟʍǪԡɒǹÉ',
                    'value': {
                            '^': 'int',
                            '$': 397026842008560416,
                        },
                },
                {
                    'name': 'ŵ\x8f',
                    'value': {
                            '^': 'bool_list',
                            '$': [
                                        False,
                                        False,
                                        False,
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
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'catalog': '-ѭ',

            'message': 'Ų',

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
            'identifier': '˘Џǽȶɾϻȱѡ×dʚġNΜɊŷЪΞŠ҂ӻēбӳ\x99ƷƭǔǳȮ',
            'categories': [
                'internal',
                'os',
                'network',
                'os',
                'invalid-user-action',
                'access-restriction',
                'configuration',
                'invalid-user-action',
                'invalid-user-action',
                'file',
            ],
            'source': 'Ͼ˫Ƭԩ҇Ͳ҄ĶǗ~ôÿ\x94ķáĸǞ˔vĉԎ\u0381ɀã˜ǣǜѴŏʠ',
            'messages': [
                {
                    'catalog': 'ʃɒл(ǽʶҟҤ˄˭˱ԞΖϕЦҩΘ\u038bɸˑʳҸԏұȞBĠÐɯҦ',
                    'message': '˻ȁьʦѼóŮǂҖВñΒШѠԕňN%ʇñˁų®ɨЀĈԇǶɒˉ',
                    'arguments': [
                            {
                                        'name': '˄ԒǑʌęĊЛѸУȉãȃĶz\x9aɉ\x92ŧªȜϧœҤ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033226.730915:+0000',
                                                                            '20210327:033226.747775:+0000',
                                                                            '20210327:033226.768155:+0000',
                                                                            '20210327:033226.788929:+0000',
                                                                            '20210327:033226.806923:+0000',
                                                                            '20210327:033226.825123:+0000',
                                                                            '20210327:033226.843490:+0000',
                                                                            '20210327:033226.862276:+0000',
                                                                            '20210327:033226.882093:+0000',
                                                                            '20210327:033226.898730:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԭžˎεΗŊƟˬS˽\u0382å\u0380ӰəĖŧ<ǚΦϋΘΗћУnʭʞҺŉ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -60758.54115620372,
                                                                            934799.0415662013,
                                                                            439216.0199421139,
                                                                            109460.10226462776,
                                                                            -66955.14019898557,
                                                                            675111.8058152793,
                                                                            465643.33787600114,
                                                                            467257.11021881166,
                                                                            89782.79867936441,
                                                                            875782.6219201229,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϕ˼ŲǗϿбØқɔҘΰÆɓĥɗ%¢¤ûОԧȀϊìӫҰƔɉȹԅ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            644623.6996114142,
                                                                            594806.7628823923,
                                                                            373722.2141257843,
                                                                            774963.6070041854,
                                                                            217377.07064922823,
                                                                            466550.49450269714,
                                                                            136654.80249551515,
                                                                            281490.92857389833,
                                                                            882854.1884599625,
                                                                            260498.2092837777,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʹǚÿǢԋǻԟ˟НΘöǯПΟ˵ЙΡɟ҇Ͻ¯',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5967576940620173495,
                                                                            451259692628905079,
                                                                            7308495842192824524,
                                                                            7863248894142770046,
                                                                            3112448957722786581,
                                                                            -4604946279278907233,
                                                                            1340158714265386208,
                                                                            -3324375239334455246,
                                                                            -8275117713219830781,
                                                                            8985602171616974231,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ң°ƆУHIɐÜ-Ϣӝ|іҝłÄЉêЈҁǮǵʹɞ˚ƼƚПњҤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            721673.8210840628,
                                                                            242571.2495614271,
                                                                            193372.32218100812,
                                                                            532404.415026172,
                                                                            299607.480244217,
                                                                            958009.5752372371,
                                                                            983179.6529451129,
                                                                            313237.7251581468,
                                                                            140436.11741549178,
                                                                            325840.32952225883,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ЈώvȕїЫҠ¡ƔͼϬӮѿͱōѦҤ˵ӱļϵß\x80ʼǏUúҨʿȣ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ɜ\x9dƭʝӀ\x84şУ˨ˉϗƴMӜѽа/ˢÈҌÙ˅ίʷҳ˳ȵɘ҆ȡ',
                                                                            'ΕИΟ˥ξӎĳ˄\x8fπТ\x9bàǡϟԃÓʝƆԩ҄ѧˌ˥\x80\x86ԣØʹɏ',
                                                                            'ʊEѐɻ˘áӰ҄ыʻţ ˧ʾƗư˧ĚȊѯĹӫȻǲöĚϻӜƱŁ',
                                                                            'ǓȈŒ˛Ҕƽά\u0380ʍѯϫĨѤҠ3˙ąưȨμʩѼҰѥ^ίĕЌѯ±',
                                                                            'ɓ˽ǊćɄέ¾΄Ϫ\x89ŐŋϱȠԣӛˡ\x7fīџ˜úϧÏӶˋҺδɠƍ',
                                                                            'ÂҪ[ʘϡȣоӭÜϊȣӏĬΞ%ȬΌ΅ˍȨȣǣӨ-ǷõӠƦҮә',
                                                                            '˒ԞѫҁéǢʷӳ\u0382у.ƛЬɇɫţ\x92ԌmϏ\x96ř˟˵Ұ\u0380\xa0Ѯєԙ',
                                                                            'Ǣʻ˝ԀҩӂȦƒĶϗѺɧɓMĈОӜ\x7foÖǡ˕ΜR\x9aŦɃ@AÑ',
                                                                            ' Ǝ҇ΡԏǂӻҥȏϒǚÒȚѲϊºŸϢ<ҁ<\x89ʳʬοÝɹȺšп',
                                                                            'ȱ˥ŃƉŨĻΪčч8ȗEϮǯɲӠ)ƻȄ˒ŚΔԘBɀӭāɎԬg',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȩʼɭŽ˼ҿΝȑNé.ЅǕњĤƕŷԎ;Űѵԗì×ƪѿӇnɯǗ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -845226413535747329,
                                                                            2147055425362956940,
                                                                            -910351303243153641,
                                                                            -5588574976735518191,
                                                                            4880468993443289693,
                                                                            -2058636726086432119,
                                                                            4103292382152330486,
                                                                            219959226903020160,
                                                                            -1575650278131832453,
                                                                            1217763076142848376,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'μ˳˶',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033228.574055:+0000',
                                                    },
                                    },
                            {
                                        'name': '\x86ɁԥúΠЊǆѣԀðҽԜϜʚąАяɏʖΔҚĕƴʘǽҗRȱ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ҘʵӯŀñʇΛě'\x8bȦƕϙЇԂϡҬȴƂƽ°Ϭӽɼȍ)Ɉʥʐż",
                                                    },
                                    },
                            {
                                        'name': '˗sˀҶԍΦҿɥǍƆςĒϤϹ.hȶϺĂ;\x970ѣˮδҠϜӞˏԠ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033228.726824:+0000',
                                                                            '20210327:033228.748060:+0000',
                                                                            '20210327:033228.767790:+0000',
                                                                            '20210327:033228.789095:+0000',
                                                                            '20210327:033228.808121:+0000',
                                                                            '20210327:033228.826485:+0000',
                                                                            '20210327:033228.847407:+0000',
                                                                            '20210327:033228.867390:+0000',
                                                                            '20210327:033228.889357:+0000',
                                                                            '20210327:033228.914145:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ƀΏӖӰдĴľɹˇϿšĽȵѕ`Ăѷԡ˶ϓǡ\x98ѠӕʶŻʊԣ4˘',
                    'message': '\x9eϑȡѱвϱӒˈϾтӠ:ӝȰΫDПԢ\xadƻӹпʵóԁŻӧÕ˼à',
                    'arguments': [
                            {
                                        'name': 'żԒŠąʴȻѽŻˀМҖȦ2ɄăҤĆ\x95AϛȼΰӴӎĸʈ\x9cʚοɥ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ğёûǞ\xad`ϬͺҚΜƸͶøЎŻϦ\x98ɪԞÆʂɃ\x8aţˁȪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'әԒÆĀпӔɵИψǐѝϷĿ³¶sҰ\x91ȅЂuŔ\x91қňːϽ҅ҋª',
                                                    },
                                    },
                            {
                                        'name': 'ϧʧƦĂ˳ȩӶόϻnëƮЏƬȾүċąǒ˔ӿΘңɜҲǶs',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1939767946933892427,
                                                                            4206757804154091276,
                                                                            5955133922721814271,
                                                                            1926728942165966623,
                                                                            -8087773961589183060,
                                                                            -2325759269711443633,
                                                                            7254043878826132030,
                                                                            -3776700832979463794,
                                                                            474612940042512390,
                                                                            7936474068782238375,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '1ÑʿԋȂłоŔБuϤɨѮ¼ϙ.ɴӔϲƐё˹ȹDȠ3ϩ2ҰZ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҫȰͲԃԘҀöΛÚhòαRóʩƻȦʬɽϙϟʁěϮƀNѥơѱԘ',
                                                                            'WĜ\x82ÆƩĜҠŉˮӲɱ˅ʅφÐϓͷ¨yʼѩЂǛ·¡ǪĩȮ˖Ⱥ',
                                                                            '0˧GˑϰûͲԍӽġïõůҲͻЂĖČΐUɯԇļˉˌĞfѵԔϗ',
                                                                            'ŨɇʲѰːĜҎʏūӻĬӕϠÕѳ\u0380ˌиԪʅɫlƘԕmΰƓ©?V',
                                                                            'ǭғȧːѭ˨üĊ˰ĿҞԟӽǗӈʼϞͲҲOʦĬŇ˼ù²¨ƘʳҒ',
                                                                            'ˎϜϸɱ"˜ѽʮơ\x8dӬЈΡOҬǃΩóҾзèӈȅΘǓ¬ɓΫĐǝ',
                                                                            'ъћͳѢɨ˄țʴȩƎǓɅŎӊúΦóʺèƋ\x99íɃˉ¶ЉÓϰӛΥ',
                                                                            'θΝǧών×҉ӾҒjɤӖȬҲύǟаȱ_˕ʍŅΐ˳ʑɦ˃MԖΡ',
                                                                            'Åˣ˻ӬǆȡǨǓƑ\x92ӺЎħѦÃϙ\x85\u0379ǿ϶ĽҌƇā\x83āЛϑúϠ',
                                                                            'à\x8bΆÜЀѪ;\x97\xa0ĸ˝Kȭ\x8cɽƞ˨ęРƵŲšȮĺˎǓŲɲƵͶ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԘϘˋœÇЈǰɁz>Ț',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            4925479969891484556,
                                                                            8114266479560604897,
                                                                            -8730895732161215741,
                                                                            -764988396027023515,
                                                                            -6500529866272811699,
                                                                            4889832560807253577,
                                                                            5218819652733537581,
                                                                            62240536392109951,
                                                                            8614697025110036786,
                                                                            -8921183920469779427,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ǆȥ¤ŻϨΈЌXκǺƗºȭјĕӔԜNθ\x87Ʌę',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033230.039225:+0000',
                                                                            '20210327:033230.059624:+0000',
                                                                            '20210327:033230.079513:+0000',
                                                                            '20210327:033230.100997:+0000',
                                                                            '20210327:033230.118639:+0000',
                                                                            '20210327:033230.137375:+0000',
                                                                            '20210327:033230.154708:+0000',
                                                                            '20210327:033230.173619:+0000',
                                                                            '20210327:033230.191303:+0000',
                                                                            '20210327:033230.209244:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǧǤϠӜUƐʏ«łÛȹßēǵ\x96Ļ7Șϧ˄ҲҁŲԝ\\ԜĥĉѲә',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ģԩǀƈѡ˫˜ȻķʩӘu',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -7843126941069512301,
                                                                            3922609747697259795,
                                                                            -492790153004869211,
                                                                            -2849465538624634876,
                                                                            8497390248839696312,
                                                                            -7600469827491439052,
                                                                            8232556319305647940,
                                                                            7569679855918476791,
                                                                            2271449913581440514,
                                                                            6823696130068582610,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˠҕŴϰÄǌϺĚϑҷ˚+ǓƸ·ǈȅļµҒʙϤҧÂ',
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
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬ʴCџŪŀтɌ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'σϋθӁӴǞ\x8bНҨƧЄӉȝѢΔ҇0ǸÂ\x86ĚԛȚэɜɡěΫѝʢ',
                                                                            'нɤŃ϶ċĎѦʹԟӆĕǬ?\u0379ŧÝѰҨǬ˶ЁĮÅɧʰΦӶΝʹλ',
                                                                            '©ƈŁàƠϯϖý°\x89ƁÞĺкϯεĕ˄ƶӷɹΩЪ˼ƞХԥѭԖǎ',
                                                                            'ǬżɣłŴÿԂѡŏџđӴ@îĵӅΒʀαđҴСʲҶʳȀɄƧɫÒ',
                                                                            'ΉÃѮȱлƾȵѾϞ_ϹΤʪфͱʥҘō÷Ua±эƶʬӗ\x92ÕųɊ',
                                                                            'ʟϖǝϯӴ\x94ȧÉԜԜѫǾȏϔԣʈÚЈйяҝ3`ԠύęÃʋʌљ',
                                                                            'ɷѾӒӢƄuʐҮԮƤCȱӴʭéѤΝJǤvѫӶŚ˻ʾžǒΐƨğ',
                                                                            '˪źʠҲжЬԭʾÙŵȫхǡȼǈɉчźɠӵʰÝzɌļǏˈҪʘĈ',
                                                                            'IТģԟgÉѹρɂˑΣO˥ɩϕŰʳˏ\x9fӝƕFÑԀзʸλµȡŌ',
                                                                            'ҺӰȟǫʭȩŪвʝλɊˬΤ˚ΉØȭɌҍ˨ňȐ[ɈЍƉшª˪ɓ',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϩˢ6ʉԅ\x96үĻʔʒǘȒ\x83ǦϢǠIK;ӝµǏԖ¯άҎԔϟÅņ',
                    'message': '?ȜѣоϣсѾτџyŸȴсΠƁТќԦѭуȩ϶Ҝ±҉ЋΈʇ΄˩',
                    'arguments': [
                            {
                                        'name': "½Ţʫlεɬ'ѺӧƤŜԟpǊ{Ņԫĕɮ{ŶԋЙз",
                                        'value': {
                                                        '^': 'float',
                                                        '$': -22135.27505000557,
                                                    },
                                    },
                            {
                                        'name': 'Xįɭ)әΚ¤§QЂ\x97íԜȒǅҟʏ˕ŵEΘϘʏҕNˠȤƾʞƳ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7786289670027871885,
                                                                            2806683349818817813,
                                                                            4241949639822016492,
                                                                            -536835326790652685,
                                                                            -2483748523067199344,
                                                                            -1139586843003330133,
                                                                            -1033173719487377270,
                                                                            -3761438006440828784,
                                                                            822249599593125690,
                                                                            5304757108079376816,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ϗîoь\x8aΌƥ&čō_˰ҋϝǜǈ4ӡȸʱȷǰԪȸθ«ЖɄпŏ',
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
                                                                            False,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɚ˛ÂцÇǲҺϾƧǿ}\x92őɿÎɭƴΦЎƓˣxǟ˪',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5894965550376096416,
                                                    },
                                    },
                            {
                                        'name': 'ӳѾʪэЍ?\x9bȗōыÂʌӍȀѺξǞ˴΅ĘŨ&\x96ȶ΅ʈˑȱiԪ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ѧͶѶʋІӇцĶǲԧĔöѽȗĊɭҍԍƘԍһрɥВԓӻ4Щ¨ѽ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'əǣƗŝLǏ˯\x95Ĥͼγ\x93ѣąԃXšʿȡƏǷĹɕяĹĳѶ҇ӵΈ',
                                                                            'βπƴđņÆÃ˥сȯϣ\u0378ОҚţŔɋ˷ɘϣӜɄӵƤħмȓЌЅϟ',
                                                                            'ˇˀԄѓƶҵҁњ˂YҬԍŬæϊԫӜғȠ\u038bčͼϟǋӲɁԬ\x8dϢ˞',
                                                                            'ѠnʽƾJ`˼ӀԅkӔȈǐȕѰʿ\x88Ԫι˾ǉӫАˁ¸ēίΧԙW',
                                                                            'Ԯ˯ι·\x88ƺŹ;ǜȪƴƟ˺ε˂еǟɞχЃӲÓλĐĭΝ.źţr',
                                                                            'ƊÚVмϹɧǫͶ´ǎӀԐȉЈʓԞҋ³νǥøԏǓʲҦ͵ϧƭôƤ',
                                                                            'ȽѷÌ÷>Ͷ÷ҾȓϳƬҋΡȱѢвҔɔɊ\u0378ȷѓԠȼˡƋ\xadîəʎ',
                                                                            'łЪɢ\x7f\x93ӌŦǗϮÝʥϣ©πѶŖηбċо;ħвϾКɀˈбõķ',
                                                                            'ԁΔȧѣɽý=Ѕ\x95ęΩĥԠΘʲôӑŅĠѝ@˕ɬʐđɇǅŹθʚ',
                                                                            'őBģжʜɅ¸\u03a2ʯ˛Ǜ˄¿Ԉ)ǱŅɊ\x80ʼϨԑǇϚïѕҟͼǊт',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӎԓзб\x81ӘȚ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'oˣȖдϵҵѽȏǃђŏBΆϹΑ˪ΉŶϤƣKɆ\x97ҽǕÆЍʀŸИ',
                                                    },
                                    },
                            {
                                        'name': 'ƧуÜсɞɸ¾ʙȹã',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ˇԙӁ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 704160.98524251,
                                                    },
                                    },
                            {
                                        'name': 'ÿΧľƔφƧͷÐɺ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            5121068957566030950,
                                                                            -2511329930203447291,
                                                                            -9030754561735961087,
                                                                            2989133805772762460,
                                                                            8244969313787865730,
                                                                            8739962680314870578,
                                                                            -5838127802727494790,
                                                                            7329574668260200581,
                                                                            -7481595649563458049,
                                                                            4816491116470109994,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ϵǲČĴѕӺǟǮ\u0380\\Ƅê\x94ȓеќǻӚԉʘĚϫʕ"ІƊƠѩ2ė',
                    'message': 'Ӆě˰ǑȊŗȝуɥȶўϘħñ£ŊϏ¡ӔҠвЃϫ¶ĦƍѬ˥qŮ',
                    'arguments': [
                            {
                                        'name': 'áКʋ½ΆǖҼà²ʘʊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            504604.36112342565,
                                                                            28835.487398892976,
                                                                            395760.28733040637,
                                                                            270077.9746651363,
                                                                            619627.3074209305,
                                                                            679258.4717390442,
                                                                            863442.7706408127,
                                                                            559599.9641478615,
                                                                            -71470.64770047793,
                                                                            84808.01088131082,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ãҋҦϩ˘ȬȷȫŴϼф\u0382ŉ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӹ˅Ԏþï;ǬǎӳʇҔyѕΕÖӴԉʥхƯŰ˺ʫΌĞɰǳċˮϖ',
                                                    },
                                    },
                            {
                                        'name': 'úÃΡϏцÁϙΘѹĸ\x8fŤĪİÐӡЋǉͿ³ӐɢĚѲЍ҈ϱȸĶϮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033233.892859:+0000',
                                                    },
                                    },
                            {
                                        'name': '¡ĔԢǹƏ·҄ǰɪʼƉϱҪ˪¬ԊвˋțΰůʹʚFԩҮɓȴʣϖ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 468120.4369843375,
                                                    },
                                    },
                            {
                                        'name': 'ѵăұ{©˓ҺԜԒɑ\x80ˮÒʲԖӕΟԆАȗ҈ѤЖҘ\x92ÐͳԩϧΕ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'ԉԥĿʛĒŀŮƵŚϦĻǳʀȞv¶źƈёϤŎȭƥɏǣъπÞҘΤ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            655566.8769849772,
                                                                            866584.8730873831,
                                                                            825489.6154191747,
                                                                            137465.48949496626,
                                                                            460368.63314925216,
                                                                            59762.13356216176,
                                                                            495871.2852326323,
                                                                            705961.0337043087,
                                                                            771233.4136172269,
                                                                            402467.9426062191,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'юˤŬҲˊщ΄',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '͵ēԕÄlόĀȃǛ\x7fǎҨ\x86ӭɡÿ\x8fнԌЮӀ&ҹ\u0379ƫ˵ȘŻûЂ',
                                                                            'Ñȟ',
                                                                            'ƅԞñӍѤ\u0381ļМƳɉʶŘʓ\x8cǬÈųÈӑʎΒȼ¸ӴƗ\\ɞХ·θ',
                                                                            'ўȃÍӡė\x9döĔԎШłЎ\x92ŐѴ\x90Ɇ8ŒɧʝÎɵӄϭůϚʘĀВ',
                                                                            '\x8dȋkň҃˯ˑâҼǃʯԏżΨɄҪǫÕ@єԝϲӲȗEɼ]ЇƦа',
                                                                            'hålϐ³ξȋàƓÓ÷˴ħb˷ǾÑԋ¢АĥƑþǜϓԓʒuĖª',
                                                                            'QɰŁԖ˯ϟоûǘŇӕԮѧʰάǟɤ҆ѰEǅџKʢѳǎ6ƞśǎ',
                                                                            '\x7fѸҧɩ ōΕfăЖƏ\x99˷Ńύ\u0378˴ȁÕ˩~ƒҐÒөʚėǎʒϺ',
                                                                            '϶ʮ5ǲϕϽŨĪҊäӕȩŴ\\Ͷͻ\x8bǼҜξȊͺµΠЙaӽұƂҿ',
                                                                            'ɺΧԦ«ěÃĽòԌǟņǹϝuȂʚХȲKʋɧȗSνʋγ\u0381ƣέɖ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'аɯÑʽ˒/пrӡϯ΄6ɑΠǬƥ˲²-ҘӞԢǩҴʅĀșɱȞϺ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '#˸ώƣƪљ%˅ǹʬӘʐİѻūηĀţҼʱӑĦčщ\u0382ΦȟΦʽπ',
                                                    },
                                    },
                            {
                                        'name': 'ɊŞ˶ђ+ЗӧΝŦΓ\x99ȿҺԂWß3ϰɳƾ˂ǯΟҸƚПҍÈŬΌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -5922801538994351856,
                                                                            -7794057754642624651,
                                                                            177974834371700791,
                                                                            7648394114464360010,
                                                                            4091561125607099295,
                                                                            -5601717008678085170,
                                                                            -3457021278661316558,
                                                                            -2384801144190170622,
                                                                            1051501544498740165,
                                                                            6527099230089739591,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ͽųėėԁ¤˝ǈVȞȬΰǒĹɝҦ҆М΅Ǽ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8328070044054172308,
                                                                            -6204087837439937102,
                                                                            -4624341496007732237,
                                                                            117100321531959657,
                                                                            7508337157878641511,
                                                                            1586268795430864269,
                                                                            -3049481088790515186,
                                                                            -6926398449729489111,
                                                                            -2458533182928150180,
                                                                            -7717928541747337634,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'H-ʢuΚʽԟŭҀÄƄƱGŒÛӨYŦԮʳɫуԤɐЦϰlöǂŪ',
                    'message': 'ʬȓϾ\xadл·ɔ\x81ӝ\xa0ƑιЈNϘїѩɉЄɩȲӿnȪëӉʁӳTè',
                    'arguments': [
                            {
                                        'name': 'ĢșҖ\x9dǨǁþѰЖӳ¢ϒǷ˜9ϟiͶΧЊӭԒӔ-ɛԥӰӲʣ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -8360390970393643427,
                                                    },
                                    },
                            {
                                        'name': 'ϠͳȕŪϢΖ]ѥя˾бҦʤ˸²ĳźȦҦлƶҶƝ˳Ӊ\x81ȑǇʡИ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -2729191293582682779,
                                                    },
                                    },
                            {
                                        'name': '\x93ԄҔí˚ɛӜˡѸӸԊЄ[ѱπŪmȬѰŻêʪȫҾ=ɪЁƻɉĪ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033235.648712:+0000',
                                                                            '20210327:033235.666420:+0000',
                                                                            '20210327:033235.683464:+0000',
                                                                            '20210327:033235.701249:+0000',
                                                                            '20210327:033235.717054:+0000',
                                                                            '20210327:033235.731993:+0000',
                                                                            '20210327:033235.746621:+0000',
                                                                            '20210327:033235.761536:+0000',
                                                                            '20210327:033235.776234:+0000',
                                                                            '20210327:033235.791504:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϋX˅ӡϟϑԒYϫηͼήǮŗ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ҩʥ\u0380όҸӃƧǴљūi˭˰ѨԈūǡЯˌˌŘɻЪōѧɾc\x83Ч˯',
                                                    },
                                    },
                            {
                                        'name': 'şΗʹɪάǡŔӠμԧЦ^˯ņ\x95ƴ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5509379636139013011,
                                                    },
                                    },
                            {
                                        'name': 'ϠӁԠïФǺáѠ|pϋ˗ǸЭŉİό.ϐί\x93Ş˟ЮΪȊƙƏЁú',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ȠŗΞҿɻʤŹŢϊџ˭\x9dńǊɞĨWαɨҟʤˁәŰ<ōŸOnʰ',
                                                    },
                                    },
                            {
                                        'name': 'Ѧɑї҄ſƍ˙ˇƸcňǂͺƦˆŪǟmʔʰȽΞΉSĢӦɛ^ԊǴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033236.107026:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ƫ4ɉǠŏļŏҫŃϵȠΐв>ϡƅȏȡÌĄƷjȅԊ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            926189.6220459583,
                                                                            766403.5864659298,
                                                                            40471.759275611344,
                                                                            -77275.24167723292,
                                                                            349468.4868242745,
                                                                            909922.0588719028,
                                                                            376262.5925883924,
                                                                            602450.2221283156,
                                                                            235590.21561268123,
                                                                            885725.034442881,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'W\x96˸ϒӈˇӔeĶѥ+ńʕ_ԐӉƙԝэüĄŮϵȯơȭӅɖҜɧ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1201943583184570934,
                                                                            8757121673747592943,
                                                                            6270900752163839453,
                                                                            -7434217806872852953,
                                                                            8360111087570727833,
                                                                            2190203125360274074,
                                                                            9034797380503324390,
                                                                            -4371585060816197603,
                                                                            -6313163747374975487,
                                                                            2812056981242422182,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǰg÷ϵԨH ×NėТΌűƖȹĒƄʏώлɽɊǫƱ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '˭ƞ˭ɇƳͻϰçÃƀHȰѡ˄+ŌųȈѓð&ЏēǭŐБˋųӡī',
                    'message': 'ѻύɌ?cгĒ_ԩȴà|МԢΐԫžĻѱ\u0383wþъӠӄǁPζюę',
                    'arguments': [
                            {
                                        'name': '\x9a ƎƯϵˑR˺ŋšǡŁ*ɘȷΔѻҕќɞĸʺЛЊʴҺŰ¬ұӜ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ǳȔʲ˓ȼҬʒЍηɈБԏҩwε\x9aЃЇӈZʋŎΧ£ĎȠ-ŭ\x86Ǉ',
                                                    },
                                    },
                            {
                                        'name': '$P˼ǐȽĪŗӑţ9ϪņǙòƏ\u0381£ß5ɎЬԅμ´įǘʪΥ΄í',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ǉăØęƆȈƋʥДǬğýʵʖB³LҿҰÆ5ϴʇƜʞTƅŀƀώ',
                                                                            '¦įƸʾRɭʟȩÌRŌӌӟӳû˕ǥÄŔД\u038dӪsŖŅŲƋÊӤŊ',
                                                                            'Ҫϥˆ˟Éō\u0378Ɣ҄эŞԕҁαȏ\x9e\x8fҒΤћ\x81ǓŌ{ϏΫɄɶθʡ',
                                                                            'ӘǆŃŨѽĬĞјôŤφ¿ʷïϑ˞ɰ°ԫʊÈѻĳʄŐϩƞĀȼd',
                                                                            '˹Ǎӕǩҹ\x83ǬЯʚļ@ƶϓʱЍ)ƥhѩɚ*Ɏˊ˩L˽ӨjӾς',
                                                                            '\u038dFԩ\x90ʲ·éώǊӬPXĻʑ:ę\x9aɬΡβkӿŽИʼƩŬϡѷǣ',
                                                                            'ȿë\xadƥВĖĨƊȲ¦ӿɭлɸź}ӟͻκʥŶР1ȡ\x86ƌ\x9cɈċà',
                                                                            "ǣˉҸҿ'БșÙǰɿӪ˸ɠ\x90ťǐҙαԒδєԦԢԖɪԒĺ϶ǘ\\",
                                                                            'ѐZҝˁɪɺĺΩ\x95ӢĨʙ\x9bѾƋʩʝψ˾ҚN\u0383æ§ϼҠӅ҂3γ',
                                                                            'ɽѓС˞ћѹ\x9bФǺƴюΝȪȏƎ\u03a2ʆˏʄŕҾɗǖˀԕӻӶèҿδ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҳѡùҍøĖƼӿùϏiˀVΏȸʒ\\ͼ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 391594.7454525194,
                                                    },
                                    },
                            {
                                        'name': 'ƹӥ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'DÚѳ˧ʺґȒˇŐ˩#ӪθÇѣǪZƨέяάįӭņпĥέ£~ń',
                                                    },
                                    },
                            {
                                        'name': 'ҎǁԂϨӚØЦǰΰɠþǀ҄˝ǂÚŗӶĺşåșпȒӦȴӡ¥#˾',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 1049673442524930098,
                                                    },
                                    },
                            {
                                        'name': 'ʐD\xadʹō=ўǸɌgοћǖϓĄȫŔ΄7ȵѢƚ\u03a2џŢƇӭΉӮΊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033237.452096:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Ӣȧʫżɞπ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'З',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1934385035531037898,
                                                    },
                                    },
                            {
                                        'name': '3ʐɱӿ\x82,{ŴȦѼЁҡW^\u038bϼҤō\x83ǢӨǻҞɝͱΦȘǋ¦ė',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҏÙԏĞԀӯǏ\x95ёʰs ýˇÍʄҳ#ƷѮρΕ˳ϙΓƔYęδʀ',
                                                                            'ůѼϽƀBǶġ,Éд\x92GÜ:NƗѐ<ŬĎа\x9bӈ\u0381Í¼ǎÄŦĨ',
                                                                            'ƕԠƠӁɬIȫ*ġӂʝѶĖЁ"ʹ˙\u03a2Ǥ˟ĒĠĸϱĶӐϜΫхē',
                                                                            'ǕѴҽXмѱȼ!ҜϔԇК˹˺ϡȐϷ\x95ûčȤȕӻЎǘĺӲƺČϹ',
                                                                            'ŉϔԞчљЬ¢ŏӍƗԜñŠԃȨјӕż¾¨ŌȔĠȷӘȐǟʉÜǆ',
                                                                            'ΡLˈ\x89ÿӧŊàӼíτůƨxķ©ƥԕˌǽȊ˂ʨΪсSѶҊŢã',
                                                                            'ʀҋɀӼʚ@aФʥҙ˪Ѳŏ4Ӳԏ8ţĥɀϕԝ˶ȠͼԢԢńҀϿ',
                                                                            'ſɜ˘ǍƽȒϚW\\҆ѿӉѤʌt;Ӱů˃ŚԇʹəŭǒΞõˀίҽ',
                                                                            'ήƣƽӰЛǈŘԆнҷӑŴ\x9bΝXԁ˔ŅǟʜͶѴJьЂҊƮßôь',
                                                                            'ЁЊпЫзƼǝЎѦÔȶƦ]řƄþѺȰӝлͽŘ¨ԅҶõΫҷʐȮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÇɺӪƇűϥĳĤĢǘЌʊЏb\x9eƻʄʿʲĺιҪôǟ\x8cɌѭOԖȓ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 256942.2181524291,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "ԅϿˠȍӖԠǬƎɝUΟ0üȊƫŉŕɫŗǏˀǘ'áāŇŌѩˣΓ",
                    'message': 'ʓӵŏŇˇǶZɧªωҬȦӯ҇ñҼǡƲˇΑҹөͳˑҋӍә\xadͿΫ',
                    'arguments': [
                            {
                                        'name': 'ɹΏˤ˧ǰ.ҒĄңƆʁ˴ϊҭԬđ÷ǝ\x91ϐ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ýȟßɛÈȸɋƮċɢɦΖ¹ųźòŉβĠȷĳ¸ѰєǹdȌ˪ĢѸ',
                                                    },
                                    },
                            {
                                        'name': '҆\u0381\x9a',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033238.030801:+0000',
                                                                            '20210327:033238.044405:+0000',
                                                                            '20210327:033238.059264:+0000',
                                                                            '20210327:033238.076233:+0000',
                                                                            '20210327:033238.093480:+0000',
                                                                            '20210327:033238.110166:+0000',
                                                                            '20210327:033238.128826:+0000',
                                                                            '20210327:033238.145940:+0000',
                                                                            '20210327:033238.163090:+0000',
                                                                            '20210327:033238.180051:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'pˌΐɺő',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 637505.4352976204,
                                                    },
                                    },
                            {
                                        'name': 'ѵ/ǤÛƌ6ɭ[QʾŃƩɸсěГɒȯÆÌ©Ҵ˞ƥɈыĸʛӍԏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'śœҺÐӖӎѭ\u038dĭȓŔѠÝȶį²ͰŘǽµÄ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'úЄӊbdȐzνҜΖǬЫƯ]8ԥΛѽŧ˧ύQȃϥǩҷҾçЪӁ',
                                                                            'ѯϳǽĕ˝ɢʯƮɏ҈ʓѷОŮĔɺғȾԇϸЅϛΊœžɖt˙I\u038d',
                                                                            'ɼKțΘ˗ÓɰԥРɛƄέɗçʯԔȆԂ\x87iӑ\x8e\x97ɤĸʘзɧҡϞ',
                                                                            'Ӟ˰ԊŊӴņҁƷʿ×ґ˨ғ×ǏʠӻоϪБѨсӂԣΖňǒ|ˁÄ',
                                                                            'ĂuiĴǂɰʫYƞԮ҉ԠśáºƗȅǫʍŜPοŉÌίϜ-\x83Ί\x8f',
                                                                            'εвЍʐƼАBɑeԢǪǬ¬lƗϤԩÒЈxҜYƠlɂȻøDɄу',
                                                                            'ɦŀӚǂϥ5ΕНрƊǀ\u0383¬҇ӣϤѱɳ҆ƏѲgZΩяѯóѱнӷ',
                                                                            '\u038dɻҾθÆɳбȓϵұȳӃ\x87ŒŴ˵ȹºәˤȕѧɫ9ʬȽӲӨǿΖ',
                                                                            'ʏ\x8d¢еŸŐ˅KсâЇ<ʸ˖Ϝ\x8eӚėмѹεgȃŅ˩ɊǑȯòҌ',
                                                                            'ѝɈƩ7żĕɊмԜΰɕ҈ҙǑΖӄ¤ҷ?ϓĀϸƮύ˻ґƛҤҺϮ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ϧˆŐǰѩYɇΤ\x9dͶĕ˺\x80,ùˌʸòӒ˂˓ʹƕƂ˳ȑǲƐӹˮ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033238.670580:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ʶȘԍЌӤ\x8eƸě',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
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
                                    },
                            {
                                        'name': 'ЌºȀ«ҁϱЈ˾õȽȈǑнXӘÞƖ@ùŴɄ\x94Ҋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:033238.969926:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǳˀҔϿ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'БʭͿȔЂҼıȧoȾȠơϫtɅ\x82ĳƈɱ;҅ˁǴʳƓŝ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ŕԛ\u0382^NЛ²мơҽìӽȕmΪɆ?ʚ˨Ǯˌ²ðҢʽɳǿԐɲѩ',
                                                                            'ɫ˘\x8bȚŧԭ˨ҜûЋӆǯйԒȵmЌ҄ƪʋŭΑȊѤӟǆŊц˂Ƃ',
                                                                            'ԑɹ½Ƨ6ͰпԮҾȏˤƽđĀʦϒҡɯщëœy˻Ϧ*ƈZōǵԗ',
                                                                            'ρįӒÞЀǝÆ]ïͼ½ǜЭѣ˘ΦфѱɾѳϲǽȥÌüΒ}ĘԘÙ',
                                                                            'ҳęö˔[ӬRɍmҟ\x868WϩčɈǜƧ˩8Öѵ\x96˳ĶѲ_£ÔϨ',
                                                                            'ƝUϪ´\x84ǂǜӲϏȽLӗʜı˱˴ѯ§ʜЉïʬŌϻÉ;ǢΘʸе',
                                                                            'Υɣҩ°ϰǁϦќԚǍǫФďƔʂє\x93Ȟï-ȮƤŧȉϘηÖԀʇ\x8d',
                                                                            '˘ŲζǣИԐȘ˜\x95РҐǑБΙƛҼѻ\x8dɮ΄ʗӥϠ~ЇɚȺTʊҳ',
                                                                            'уǄηΛÈ˯є\x99ɀɓйЂцҿ˹egGͽƄ\u038bʚŦΤ\x90ĄˑȲʹϓ',
                                                                            'ÔŏѳēʴƁӑ\x80®\u0378Ԗʓπ§щѿƻ˫ʻҲȚťσ|Ŀ\x9cɝѤѓů',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '(дβʘХ"ÆǜʬŤFȺȴΙǽŵɶѴƵǋƍȼ˗˓ҸȔËκҭԪ',
                    'message': 'ҐУƲřԡ~ˀʱϤʌ;ıӢϮȕƨƠȂģcëЯŵȌƯʭǣЫϧ\x84',
                    'arguments': [
                            {
                                        'name': '\u038bԢīМ¦ǵKM}ƍĆʏ¥АҴәǗɱɟ\x8bëĮą˵ǉƂˏ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '®ɪҟÕ-ʭ ưQҜĳΖѤÔЩ¦ΈȮl\x97NȏȃҮőǰǵȋø\u0382',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033239.499806:+0000',
                                                                            '20210327:033239.516568:+0000',
                                                                            '20210327:033239.533574:+0000',
                                                                            '20210327:033239.551049:+0000',
                                                                            '20210327:033239.570060:+0000',
                                                                            '20210327:033239.588166:+0000',
                                                                            '20210327:033239.605222:+0000',
                                                                            '20210327:033239.622526:+0000',
                                                                            '20210327:033239.639972:+0000',
                                                                            '20210327:033239.657242:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԗҭӃґKʹĝZŖӎΟʹƚө҃',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -8848071699887737613,
                                                                            -4707709266532756599,
                                                                            3582436282281605048,
                                                                            -7193431623883490836,
                                                                            2804520696859895971,
                                                                            -832735613735014703,
                                                                            -8061509010367394798,
                                                                            -9161265620103093325,
                                                                            -1908745937367407780,
                                                                            7005437208431072878,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƁԆtӝƨ÷Ȟ©ȨҵǦЛӖ¼ļΐɺѬǰʉɩȔҴ\x7fʸjǚ¶ɻq',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1058370429799738718,
                                                    },
                                    },
                            {
                                        'name': 'ŅășΌΊ\x9aȺƸ!ιҢěʙɉѷ\x7fҬǁ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3681515116856551558,
                                                                            3287323972981296293,
                                                                            -8414448203636238415,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƳǵҼȂӷ¨ɀìâЃϡѢ:ԍȻъĆÕ×ΨҧĹϜԔȲԌɎˁȠӒ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            608595.3236484998,
                                                                            624186.8288871674,
                                                                            135689.9284399824,
                                                                            47695.18719713678,
                                                                            320186.0336713154,
                                                                            -32282.912950434024,
                                                                            85472.36680871312,
                                                                            297320.4343109531,
                                                                            555299.0722902304,
                                                                            284892.1004427458,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ѯϼ˗ÝЩȥäγʛǄѶĲƑЀˡѼ˙ʘeãУƭ=Гļ˼zÕˡ¯',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033240.474175:+0000',
                                                                            '20210327:033240.492920:+0000',
                                                                            '20210327:033240.510974:+0000',
                                                                            '20210327:033240.529748:+0000',
                                                                            '20210327:033240.545301:+0000',
                                                                            '20210327:033240.563473:+0000',
                                                                            '20210327:033240.579491:+0000',
                                                                            '20210327:033240.599377:+0000',
                                                                            '20210327:033240.615611:+0000',
                                                                            '20210327:033240.631906:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'УȓʓKˈʟԃΰ˃λПѻśЬЙǿϜȿ˸ʉ°10îϨƩϨɓı\x98',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            333492.12006040785,
                                                                            -26658.39303523676,
                                                                            945219.16105639,
                                                                            979381.7492330046,
                                                                            310007.1168580459,
                                                                            9890.86994689508,
                                                                            947670.5191973577,
                                                                            619402.6576705484,
                                                                            537523.5426863579,
                                                                            -80310.13874107235,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɡϼҘӁƁŰǸҿԍ˺4ӆ÷ϢЄʖǀˮ\x89ƋѩԐƂԢČβȚå˾ԥ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            469642.0295498974,
                                                                            925129.4387524967,
                                                                            262570.62945609743,
                                                                            293773.32477147144,
                                                                            -47330.756851508726,
                                                                            213860.58057520585,
                                                                            504114.10168500256,
                                                                            -62646.42477507957,
                                                                            667613.6495490248,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '+3Ĥ˞ʕǖ˻óɚӆο\u0383УƒɤΓȍ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -47042.89796318565,
                                                                            496751.3737598752,
                                                                            283255.6402077084,
                                                                            317039.5273238817,
                                                                            -10411.212853269259,
                                                                            661866.9758081145,
                                                                            125398.1710146729,
                                                                            575656.0928028345,
                                                                            -69027.42419064387,
                                                                            819993.6794252244,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ÙʔΩΗɢǹȆҒЛȟÏđĩh˖Ӥο˾ɷȠсĠŢҵΫτʾПÅ˩',
                    'message': 'óƤŢЪƓѽΥŒNƆʢҮ$ҼéŐщĕϷǬўſʕԨԄĊ\x86ȷӇҦ',
                    'arguments': [
                            {
                                        'name': '¤ÎĜ˚ћˮӚƪǐлËǂoŽ\u0379ҕʀƨʔӼťӐƠӭ˒Ое',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'eÂ҆ʥ\x94ЖƦEɀǰϜԧӶʙƼŲΎɻԬĵǖϻǧĻǊˋkƻ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033241.558655:+0000',
                                                                            '20210327:033241.576977:+0000',
                                                                            '20210327:033241.596658:+0000',
                                                                            '20210327:033241.617954:+0000',
                                                                            '20210327:033241.636784:+0000',
                                                                            '20210327:033241.656223:+0000',
                                                                            '20210327:033241.678033:+0000',
                                                                            '20210327:033241.700547:+0000',
                                                                            '20210327:033241.719359:+0000',
                                                                            '20210327:033241.738386:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '¬0',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:033241.839387:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '~Ї΅Ƽʍӭ\x9fǪȑґǾƵάbÂ&ƺқĚŻˊĘWlʾ˛țɅʠԆ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 2138423865688292648,
                                                    },
                                    },
                            {
                                        'name': 'üҐʏġ҇ѐBԨĢΊͺƫʹΨáӔʴîˍйϣκʡǽɱКJñԄǒ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -50426.14249687157,
                                                    },
                                    },
                            {
                                        'name': 'ʎȽϩȤыѹПћ)ҮͳûƥϰȗӣŦƓˬӕԜĸʾȗ3ӳҷ\x9dԘԅ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ҭѐƾˊŖǒʥЖԓύÙΈώнӒȫ˫ʦ҈ҒǓ˸ńŒ\x7fˉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 119992.25088600637,
                                                    },
                                    },
                            {
                                        'name': '˘ʨǋԂŅȍӇȦЁ\x9bʌЋʳŎǫɿνѡұǵ\x82Є˴ӊǦњћ\x9fэʞ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3896706645141480835,
                                                                            1948551427312322503,
                                                                            39978043217716146,
                                                                            -8196026154217738627,
                                                                            -3045870970065640126,
                                                                            4565665008286254361,
                                                                            -2774816973061050251,
                                                                            758792671855776321,
                                                                            -7589839553348279911,
                                                                            755871673466533478,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɘͺɇsԬŹԐԦ("Ɉ¯ȅƖ±0ҩ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            655027.7734143544,
                                                                            556781.0403581343,
                                                                            978243.6998312746,
                                                                            678747.4777285845,
                                                                            749990.9719024636,
                                                                            248186.28891074227,
                                                                            818227.0855101155,
                                                                            128360.2611489929,
                                                                            576707.308451488,
                                                                            394603.04296337767,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ġŝԚɪƧѪǴԐ҅ϔԅŬѓʿ{ʝӼʒǥɡΪπĥΤϱΊˢҜόJ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ƱӀʊ4ŭиҧ®ðƯȢԨáԣ&ȃÃɨɹʶĳŠ\x83ϸѲѡҰˢ£˯',
                                                                            'äӓʤŲŽɧϩΰɕ˜хӚćхřΟθμʃЁµŭ˲©ǫɤşϙΜѠ',
                                                                            'ҩçȱѶνИǭЬѰƕ\x8fϡƞ\x93ԪȰȕĒʱǞ˪ǪǞȉéȼΛєļƵ',
                                                                            '®ԆĕϙԓАҶŢɵφȉӘҥĹͳЙ˩ӂƓЬͳƄĈɣƷˁȮştˮ',
                                                                            'ĜЦÃȵØ+Ӭ˻ȽͱʾӋЫКˌ<ό¸XԑΣӲˮϡΥЦŅ¥ƶЌ',
                                                                            'ØʄņşΏǎўр҆ϓƉϭˍǺÈý9ɛßӳҕSǯγ$ҨTѡļӀ',
                                                                            'τ÷ʣϖɉ«ԟΥƱWЖӂюϭӠҙŵΉҠǉyΝþƺ˅?Ӂ`ˌЬ',
                                                                            'ŇưӸĀ3ŰңϜ˭ĄҬĝľЋзҺǕԈʯһԋȊϟ˟ΏYġӦл4',
                                                                            'ԑʽčśƦѶɡ©ǮGБĴȐϧϸθőϭŦΔǯƹʰ\xa0ŶӦҕ˃Ԗζ',
                                                                            "Ԅ˖ÿϦψƖӝƗΑ½˘ŉѹӣéĚŵmöƢ˥<ʊ'ɌȾáȧРΘ",
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

            'identifier': 'ЫаɁǞͳ',

            'categories': [
                'access-restriction',
            ],

            'messages': [
                {
                    'catalog': 'ƟԖ',
                    'message': 'Ћ',
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
            'request_id': 3129305,
            'error': {
                'identifier': 'љҹŕϿȒßӘҊɲȓÜ}ɮ5ǻʽʽю1Ӱʤ˩Ǩъ˛ӥǵąǧ¡',
                'categories': [
                    'network',
                    'network',
                    'file',
                ],
                'source': 'ȲϢĿ~҄Ъ§ǿĭøѪѯƸҾͺSЄÇ;ĊʔʾԆΞǈ8рΘзÝ',
                'messages': [
                    {
                            'catalog': '\x80҆ŧɭ˕:ÂϨƄ',
                            'message': 'ТϏүǛÞʼː6ɢԐȗȂʭȼŢŵǯӂÃҖƬȎÝуˢƛѢбHƨ',
                            'arguments': [
                                        {
                                                        'name': 'ʾ\u0383şзƊǟ˓ǽȫԀYȞʧҲЀǭ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ı\u03a2Ţˇ˥Ɨ\xa0ԘƧ¬śĚʺáȟɎíë}ǕңȆŜӜЕȔÐİñ˞',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x80ɩAўÁӯɤϙ\x81ʬˊСƲΆ?ȒҚșԞŋAĄӳƙɂƩ2ӽȲĒ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋÁÚŶӗ#EӢǥŊ´ǅȋ!ÿ<ʱ.Тҭ\u0383΅ǭґϦʍӸäʵ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4074295082216400054,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǏƇʊӣԮhåƊ¹ѿԕǂƟńǈСӕīȦΐϲщʫąƅʕҘѹӜǈ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'FϽΖɝĠ(˰҆Ǜіp\x9c2\x92',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŇРĊԇӳљɖĻÏѽʰĚАȎԏοþƎԃþǈʗɷõǋʱŒȗȍɹ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'щҮĳɎ҃˾ĖӺϳƻСɕӷќҺɅʐ]bɧҿʞгΗǐȝҋҜ\x8aĎ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'чϖӖɯǼ\x8cΞ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033217.584175:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɧɩǎʔˣǌąѩήӺϖ˒ϫʜҌ҆ȟńҍ\x85ȬѥэųƿήņЇЃѠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033217.660526:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ïǲǺȤҔĄƞӱΪͺ«ʍԞʨϏϸБэ\x86ĕʐ˰ō˸ӬφДƌưϡ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ъρoЌlgʜͰǚǵѾżˍӰèŐȧ·gɀ˧\u0378ƾ͵ӉɾĐʘĸѢ',
                            'message': 'ƨʋŻǽ\x80ӽƫɉӸƍѽ\x89шàɄ0ňϫʶ¡ѠqɣЊŖɠʻĒžӅ',
                            'arguments': [
                                        {
                                                        'name': 'RͳaɩˍǔӺςÇaƃ˫҃',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7554091096619405856,
                                                                        },
                                                    },
                                        {
                                                        'name': 'жҹķþ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʤϑҟÏӍΑÁÊΏԞȌԜǣ\x9bҧŗ˄Ё\x9a˞ɨҶ¾ƨǆ5Βɖȇ^',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 851677733410959070,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ќȿǖʐƎɸĸ`ӌǬбҿǩXкҀʯΪRǶӖюѱЯѥ´ΡжҗȢ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӡİɧ)ͽʝ\u0381ԃƔΧωѣЗǛȏмг˺ȧ\x8eԬӪƼӅŇˇ7ɥǺ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҼЌѦëϒÈ!ʄɚ;ӻԤԫʂŏˌԭ϶ԥэ\x82ŜӕҤɲȈʐ҆ɲΔ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Єԣϴ»ʙǔȾʖԔĞ`\u0378ȇŽĦεʫɳΏϋɤχΟ\x9eӊŉr',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ИѠǘĊğҤô½ʙѢvTөŸҚҖŊ°ɶĉèȬӛɆӔȡϷʧǮӊ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Žʨ=ΏϴƬӌӈƖ¬ɳȔIԫɉӜ˜bӅʥԨ\x94ȡπЃυԂ\x876Ҽ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Αɽ%\x90r·ăŗԢňƪΎђ\x8aȼЛƼќÖǮĸÁҟgşċʂʉŏʐ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 974979.2824921857,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ƈȶų\u0383˝ҜŜʓҜ¥ˡ\x9dȟƇǣҡř϶\x9fΣЁԓƘҢȗůԞА\x8aЏ',
                            'message': 'ϞˮŕĐRƤѕǔЯ˖įľĻɒȞПǈҠӗқ×ҠЅɼЍV˔;Ԗ;',
                            'arguments': [
                                        {
                                                        'name': 'ӘǰŚЃŠѠŬƽ\x90ԚӜ϶҉ӣ\x89˟ȃƑƄˊDĝȞƇĬ)ё{ӴȾ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ъɩƳͻЪͼе`ɪƋȎÌŔџŅǧЪɒJǈƽšƿʣΆћâ˲Ҁә',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6274343992180736337,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉ˂[Ͳ˥ΧɻǊ\x95ϔ\x8e2ƟąźƬҤŽȉǪñԋÅӐƦПΪÒÎс',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 858012.630697099,
                                                                        },
                                                    },
                                        {
                                                        'name': '҄҂ѦwƓƻ\xa0ԛĄ˕ϥĥѣè',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '͵ıΪаȡbК²ӦÝkʒӾűʬĵMƸ˟ˇίӴɰɍ˧ɽ¨ԌʆŶ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˀҊΐɓ҉Ǥ˱ИʕҬьГŅТɺJˆoȅԖҨǺʔɃоƾ\x7fȲтʢ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Łʭ/ԂĻƠŝʔǏĳɁ7ԟԩҴʐ²ɣȠϸ±ÄΟʋXŘѸƗʍà',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ьӛĎԅԕԥѭZϯәԐe',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȿYǗԆƈϿţˌÿ8ģё˛ЉЇßҎʗʪ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʭҸϓƔʙ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 596245.14892656,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ºϠŅˊȉҒёɩºĨʾĹʩCϔԬȻ{˦{ªkǥ\x9f`ҀβΚԐǙ',
                            'message': "ɯˋи'\x99ȀӂΘçʸΜȔĠΠԡʌʦ'ӓyЧȻłοȎɿҙUϰŸ",
                            'arguments': [
                                        {
                                                        'name': 'Țυȶ˱ƛȦxϮșЮVhΎȩˁȉȹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȧƪȱŁɤşĖ·ԜŶΙ*ȓ˺Ǖ҉ӥЁѵ.oȽƥΤϢ˒¯\x8fԖˮ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ǰîɅ˰ʓʏŦVўыtǟϖίĳɬƵуѹʱǧƤ\u0382ѸĴʸҥƲʰχ',
                                                                        },
                                                    },
                                        {
                                                        'name': '6@ǣ%ҊƃҵºĶӼʵŉй˂8Őĝ˟ӥѣ҈ƅ˓rdȞˣӘĶć',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 888349.2113810084,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˇʢùȩĘΐǑЕѳ£\u03a2ΙΆΨԬ6ǳĥ˘ƋӽԅɎǑˋǖ\x8b7þҌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĶѷʭԄĪѠˎҝƃɿԥɿҲ˵\x9aȖĮӊѲіЍÀЃ&ӷɕЬӨ˭ӝ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 4076885461650813160,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ÐѝʧӟťЂǱΓWӗǁí¦тԐϟ˫ќҹӑ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ΕɶɆ¼ʻ҃Ǐżӥϭҥiӗ҃ѫҙƼǍ\u03a2ςƀӪƯɆǗɣɎǳ¨҆',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƭȻ«ʝOΐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЃȨүԐφȚƳ\u0378ġʚЏϺɈӊήˁԕėĉҬϞǸéđćÙѪƷɡњ',
                                                                        },
                                                    },
                                        {
                                                        'name': "'ŤɓɌƧӝќԁƂʴ",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѳӋˡ¡ξɶƸҥͷļ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǍӻӨÅśƐҳ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 674038.2008437021,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'КĔҧAɢУŹ£ÞXʳʸƶť˯çӸԡщԓҺ¥ƆҒʫ*ɮϸѾҒ',
                            'message': 'ȖбҞʀʹ˄ӒζôȜϢʜȱώőГԟҭΓò=ųΜÅƆͰǄǉƬȹ',
                            'arguments': [
                                        {
                                                        'name': '\x94ķȅηƘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ØǵɳνˀӝǪȴȂƃԑђ?ȁD˖JϪңũͿɻȼÕĒ}ÁѨŕѺ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 450468.6185416364,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ψ\x8f\x8dÉϝԚǟY˦øɟȉɄƄʸǄʱ\x91\x8cɆMЖĸ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Õ϶ѺӶтț|ԂȀԩЗń˾Ӱõ/8ҘɒҀϓϞǩŏÈȟȻӂ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033220.901832:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΗʞӵϤϼϤGϥëà&Ь\\яȦȴ\x81í',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˻Æ˜˖`аŸӻ҂źĚԧʡӧ5ǵǹοƅҏԞͽͰ8˅ƜČѨƙą',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Y˫ҥƫʬĈ˜ƾÄχхӥ\x89ƘĕȵfãǈS\x9fΥǸӻԆˡżĤ¾Ӭ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǕҎӿҶřȚǁ˷ɹʣŽøӢԑŝ\xadÃͶ«ĲҍǑƀȵ҃N±Ȝʔѹ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 332879.0357076653,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɵQǧϐÕӲɥǲˆĹуÓԝʋΒЊӋΤYЎϓΉj',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x86zľӁ\x84',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ůʫ҅˭Ģѱўӕүɸǉİх˭\x8cŏȬ\xa0ӭ˙ƵtřEĮȋύԋ˯ˠ',
                            'message': 'ƖӫȰʨӚɥéʸчҽ˩ԅĂƓʺƐˉɼԆƷūɎ҆ÁƧϺЈǨӞѧ',
                            'arguments': [
                                        {
                                                        'name': '˴ˍМĵӵ&ё×˰Ҁ2ВǤÒ¶ńȷԚˠәȪˈѫ\x90ʍЏŮXÞɽ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ӻgŭϑƛʠȲҽèҳó³ǗϞȧǃШƧҡ\x81Oϋϣɶϱƍ'Ұ˼ŝ",
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x93ѕ˕śŰ˵ЀƟšΨʛD\x9fҐʹųοB$ԋʵŮʽ:ŔúÆȴ˒ԁ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҵɀĉʅµ˧ƦӆʙΡλOȏ@ſқοϞıȯΕǼмǸÓɅƳ˲¥š',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'τΚǁμ;ӤԤˊҥțʖˡĊΩΗ\u038dѺӅ;ӨĶҝϥίŔӝ˷ɹ;ѝ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϽƑàɫаԚšʕ\x87ӻňΐ`ΚɷүȞҚӕϪԐƮѤѣɀʷ\x9c¬Юʷ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҨƐǧӲˀ5<ʡĞƆҲ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '҅(ǬӁϕҹВϪҥϩǤȋЩҮ\x87єӦ˰ȐХɹȧƗèƑɃđ˗˭°',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'EӋȦЦѯ҆žwŋкʗύѥƫ͵ҐśкĳŅɌϼǨȷ΅ҏƄ˗ӛɜ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѬҏΔďɴδѐɑЍ˔ªʁ\u03a2ɫŕżǨñт\x8aӣZ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3552012635527161194,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʪÈȑɴɰ˓ÝϭúŗϔͳɛǚтɤŧԆΣƇœ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ʊǄѧԠҖÐƽӧoͲ\x81Ͱǭưε\u0383`ƐƚήƨÆµѭРƾҞԖ¾ȱ',
                            'message': 'Ʊ\x92ˮİίЊЮǻfɘĲÓэ҉ļýȀ2ʳěʹμПȕǰϊыſӶ˰',
                            'arguments': [
                                        {
                                                        'name': 'ǣʬјçɳƴǋLˍƉΤі˗Ǩƙϑɐѧӆϔԍ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЯŒģ˱ɥŭ@Eҗӭƽ~ɪ1нǯ¤ѡŴĲ˰Ş\u038dYƬ_Ԟ\x8c\u0379ȳ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʴŨɰԗөȨĥԝĔňiʝŰBяё',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѭÇǄŵϺѠǼујѮ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ťǻȣҕ¸ϥʸƸβ\x9cU÷6ɼɮö\u0381îДҬσԊх³ԩʉҭɶУʽ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033222.852674:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'а\u038bɔє ήвЖП˅ɪɢYΜҋɢğˠќҚ|ęÉËN˵Þɐŵp',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ҝȓ˩ĐɾČKПΩӤȠź˼ҽǩϤϫŕӯƻΣrÛϠƊӇÚϴŔˢ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ěX\x8ft¥Ėρʹ˸ʌĸ˛±ϱɉĜ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ґӧθˢy~ӖɿsáεцϵņюǉнǑ˼',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 5457109187195515597,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЧƂԅq϶Əˁž>ɺ\x85ԡʸfŉиȅ\x9dĜҟάԍЊ®\x9fĘƠqтÌ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ɸДҲӀЍѨΕ϶фǬ=ԡϩnĜ\x8fсƼͳӪӉғΚƯč˗ͼjΜы',
                            'message': 'Ҫ_ȲŘȑȻҧÒʤhЖѠЈŋ˔Ξdµ҆ƠɅΏΊʜŦP\xa0į΄ȴ',
                            'arguments': [
                                        {
                                                        'name': 'ΟͺѫеԫýЗθԪƯԛǦ҉',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '¢ˎ\x9b\x94ͶӰԏԑыӏ¹ǷvņțWǐƜɔԙǎd˳ÇЈѝǩҝ˟Ń',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'őͶƓӬў\u038bƵ˓4ѧ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033223.588798:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӯҞť\x96ǲɚĢȍƣҷǹҗ\u0381οФȀʡӳԊº*Ă˝ÜґˍВŝ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'φɨӧ˧дЌĂѼҞȨҧ˶ɞʄˎÁΒӝƆʒϞК\x9cу',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033223.763591:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '\x91ʺɏԪΝ\x9bʎ·ǟzYʜϘʱƕƌӄԋƦ¯Л',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': -31290.92716895965,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋJҼȩʱƽπЀԫCЧтɅʿŴİ\x99ÕӈʶƦȓͷӔȝĜfĝșɈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԌҡԞƔɄƽŽеʎ\x8cǶbωȾĢϻӾʚуˡϡԁĦĄѪęҋЗ_ŝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ԅ\u0381ҚϡϝʳԜЫќɮцʼȚΫơ\u0382ȆΆƋʣʯˋ\x80Ǥż\x88ğDƲή',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ıӘҾƤȦɫƩӐĢˬɈӝʤǄЙʥťȿ˫ЀӺ(ɰ˜ӤҮɃGǄu',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': "Ƕ·ɉ\x84ÊáűɊǯ'",
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': '\x80θΞÔҮţѩ§CԈ\u038dƺԔȢɨȯԭӃć]ɈЮůѡ\u0379ʻҹғǀó',
                            'message': 'ŕƆËѬ҅|ĭѐθłnƻəÇӫ?ƣƣãɺƣʶϱ=έȻͽʅΨü',
                            'arguments': [
                                        {
                                                        'name': 'ɄǞJ9ȁ˱ˏΉǣ\xa0дӲ˶\x9aǕӕͶīƤǈ=Ҹǹǂǭΰ˾ω[Ë',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҌΒƭ\x8aԅԩ\x9aȎҬǃϱǉ¯фѕх\x8cЈǕɃѣ˷ӴȡgҖ\x93ȝſĆ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -8584883068100783910,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ζȤ·ыȇˆŦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŨҮЬvϏɜąөΏθ¬˥\xadÊϮΡƶʗ+H',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԩϮҀϝ҉ǹʨӅФʞǯƭ҇ǋџÊԋǺɘя¸ůȤǎҧńӈвÀǝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'тƼҋ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033224.894045:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѽ×ŝ\x84ЃЄfȴ\x9eҩʷ˵ԓхȭԣϚȷϙʭÁǦԑϲʵōɁìϲʨ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'θпɠłҭǻÑ÷ł¥ơłȾʎ˟ѪŦÀΈï˼Aǭđ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ýĵВþŁ\x98ʘцƃҽʼӺѷ\x98ƘĵϛôΓˍʣ\x86ˮſӑƹÖŤӝɋ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϠЧɱŹ҄ĬφţбҤ\x95DеŉIßѻʛԒ˲ΈâÎɆĈĬĄ˥ҲϜ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'φԜ҅Υȩ¦ğЦƷȘ\x95˝ɩ҇',
                            'message': 'ӠwӨȒÌžИԅʰϞʭŝǔΤϙɏ\x9dǘϣȓϐԋĂІkόуɽɷŖ',
                            'arguments': [
                                        {
                                                        'name': 'PĴï"ѯϓEǧЈϗοҿВвȑy[ʰПӳʆ\u03a2ЪķΛȕͿϺӠҀ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŃʺŻԎŋũAѷҴӾϦЧҁŠϸ§\xa0ԔFМΎ²ηϸŐΘϊ˞eʠ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:033225.401834:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЛԈԓĬěŤªѪ˦Ѝ,ЃͶˢɓĿm.±éҵρΒƮ`θȃԧάƁ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': ':ɺQ˅ϖҎƿо˴ð§ÀϮɆԉĉ\x85҆ɆĲȤ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЫȺ]ΪɨˬȸǥΊΨ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ѝƍɲ\u0382ɞ\x95\x8aóӊŊŰҮöÓЍLҘĠwʲģʯưXЌʄҸ\x8cŒԏ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԉŶ¯ǑϪ˱ʁĞĮԡÒιƶǘԑũɶèҦĢ\x9eԈ\x9aį˥ʚѳ-ëҎ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -7031744745558792431,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƾȡǔПʳҦΣΟЊ³ӥіΪ_ӜҐƖџ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ŲƵíξȖˆӀŔǗŰΦѪˠăҦϠȿТſƹŽϷŽҔԞɠұ?ƛҢ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŠΡҳðҪμÔъǯϖʾKɬΔ3ŽÓξԡԛįξ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6278807986472164721,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǌʝφ ȗΖγ¬ӧеƸ˦ʐϱӉˁφ΄ËѓҖƩήӼéʼyɹ\x80ӱ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǵʁPάųƨԏѬː˞ŧϱVaϤһƛёԂԢǍĻќҸĳ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ă\x8fůˤ˔ƥǱҧԝ|юʻԫƦӼɶġŹĵ5ɺиɳ˓ΟĴюȖʠԚ',
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

            'request_id': 1147805,

            'error': {
                'identifier': 'ϘľΒNЎ',
                'categories': [
                    'invalid-user-action',
                ],
                'messages': [
                    {
                            'catalog': 'Œˬ',
                            'message': 'δ',
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
            'nw_x_pixel': 1546941659,
            'nw_y_pixel': -1128050158,
            'width': -3718468237052128328,
            'height': -4465577207971022710,
            'ratio_x': 6615317803671026936,
            'ratio_y': 8364180077910684968,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 973215663,

            'nw_y_pixel': 473734503,

            'width': -4596067894319175870,

            'height': -1368130691485834387,

            'ratio_x': 3939286619880995952,

            'ratio_y': -7180952748888711487,

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
                    'nw_x_pixel': -1031985314,
                    'nw_y_pixel': 1320107171,
                    'width': -7090159212394710857,
                    'height': -5989170595316394861,
                    'ratio_x': 4528638821983757200,
                    'ratio_y': 8980964736581121680,
                },
                {
                    'nw_x_pixel': -1251665969,
                    'nw_y_pixel': 480718515,
                    'width': -2634261094675818844,
                    'height': -8916036164536991194,
                    'ratio_x': -858515174972360060,
                    'ratio_y': 3145259020757622405,
                },
                {
                    'nw_x_pixel': -1211587553,
                    'nw_y_pixel': -640178124,
                    'width': -7186065722256543074,
                    'height': -5691681934796378993,
                    'ratio_x': 1078886703283100714,
                    'ratio_y': 3127213129578202835,
                },
                {
                    'nw_x_pixel': 995891658,
                    'nw_y_pixel': -68662655,
                    'width': -2696491311213113605,
                    'height': -3550744199490386363,
                    'ratio_x': -588761221310975643,
                    'ratio_y': 2202141306708089477,
                },
                {
                    'nw_x_pixel': 839050231,
                    'nw_y_pixel': -1327956238,
                    'width': -4170210042833865829,
                    'height': -9074150349387004498,
                    'ratio_x': 4282505612719568039,
                    'ratio_y': 3074732418344129667,
                },
                {
                    'nw_x_pixel': 936063169,
                    'nw_y_pixel': -610485380,
                    'width': -3595913817147180816,
                    'height': -6777267197900787400,
                    'ratio_x': -6692453579300795895,
                    'ratio_y': 6727642053312991228,
                },
                {
                    'nw_x_pixel': 628457867,
                    'nw_y_pixel': -1042075667,
                    'width': -6586351670396771419,
                    'height': -4794272211838625403,
                    'ratio_x': -3000978893271129645,
                    'ratio_y': -756953166149243215,
                },
                {
                    'nw_x_pixel': -264754444,
                    'nw_y_pixel': 751445695,
                    'width': -990820404607363311,
                    'height': -1087500540158207973,
                    'ratio_x': -7431758082059914119,
                    'ratio_y': -5977932237250699838,
                },
                {
                    'nw_x_pixel': 1976899643,
                    'nw_y_pixel': 1438314732,
                    'width': -1706703149897677523,
                    'height': -5586227045157368077,
                    'ratio_x': -1223118110151143082,
                    'ratio_y': 2229219451332707147,
                },
                {
                    'nw_x_pixel': -888419452,
                    'nw_y_pixel': -1711025539,
                    'width': -4194144183473206931,
                    'height': -7714634399646233068,
                    'ratio_x': -3617678329851188802,
                    'ratio_y': -5899431401449516539,
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
                    'description': 'ǎĵȴѴ¿ŽΣ˹ԀŊ\u0383ǥȚǛӔԩ¥ќ˔6m]ҿϏȺϪ\x9fԕˎψ',
                    'monitors': [
                            {
                                        'identifier': 4625910,
                                        'width': -313947371232988117,
                                        'height': 5272758891261905137,
                                    },
                            {
                                        'identifier': 6736757,
                                        'width': 2964668273557068003,
                                        'height': -3599364138639992679,
                                    },
                            {
                                        'identifier': 9822850,
                                        'width': -3537468079060216030,
                                        'height': -1093099110964398232,
                                    },
                            {
                                        'identifier': 9024503,
                                        'width': 8441621408708176938,
                                        'height': -7849151676665343521,
                                    },
                            {
                                        'identifier': 5988745,
                                        'width': -2392103454568610167,
                                        'height': -6787969429883464376,
                                    },
                            {
                                        'identifier': 6939631,
                                        'width': -1499501690987853058,
                                        'height': 779814365909068897,
                                    },
                            {
                                        'identifier': 2786385,
                                        'width': 6343014652577379266,
                                        'height': 8702730766475451620,
                                    },
                            {
                                        'identifier': 4211455,
                                        'width': -3941723776983589821,
                                        'height': 5382588051897072,
                                    },
                            {
                                        'identifier': 3065276,
                                        'width': -7746807282905750658,
                                        'height': -5155630304788897269,
                                    },
                            {
                                        'identifier': 6995986,
                                        'width': -362406607552713787,
                                        'height': 4102836486906715637,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7257815,
                                        'source_nw_x_pixel': -5797430672632913142,
                                        'source_nw_y_pixel': -6464607995618660529,
                                        'source_pixel_width': -5652976128349105688,
                                        'source_pixel_height': -2868223480039287808,
                                        'rotation': -8117794581469870561,
                                        'virtual_nw_x_pixel': -783715443,
                                        'virtual_nw_y_pixel': -1704341432,
                                        'virtual_width': -5157766,
                                        'virtual_height': -1951353446,
                                    },
                            {
                                        'source_monitor': 28340,
                                        'source_nw_x_pixel': -392978675122361779,
                                        'source_nw_y_pixel': -5392417087313547654,
                                        'source_pixel_width': -8057160627269311864,
                                        'source_pixel_height': -1523022201302406652,
                                        'rotation': -3001131744154523427,
                                        'virtual_nw_x_pixel': -473229667,
                                        'virtual_nw_y_pixel': 858409648,
                                        'virtual_width': 342600215,
                                        'virtual_height': -930311280,
                                    },
                            {
                                        'source_monitor': 5383212,
                                        'source_nw_x_pixel': -1884889364544207240,
                                        'source_nw_y_pixel': -1380507420193797013,
                                        'source_pixel_width': -8000544703954775637,
                                        'source_pixel_height': -1286790235830493687,
                                        'rotation': -8649346711298797750,
                                        'virtual_nw_x_pixel': 878180084,
                                        'virtual_nw_y_pixel': -1580616198,
                                        'virtual_width': 1775744377,
                                        'virtual_height': -923016292,
                                    },
                            {
                                        'source_monitor': 5773690,
                                        'source_nw_x_pixel': -7142252486826883278,
                                        'source_nw_y_pixel': -2805119596960800379,
                                        'source_pixel_width': -2163854636091380927,
                                        'source_pixel_height': -6425171140635035446,
                                        'rotation': -5475076012940896084,
                                        'virtual_nw_x_pixel': 1442430320,
                                        'virtual_nw_y_pixel': 854346015,
                                        'virtual_width': -1930418573,
                                        'virtual_height': -1947292154,
                                    },
                            {
                                        'source_monitor': 2519977,
                                        'source_nw_x_pixel': -1264553199481004039,
                                        'source_nw_y_pixel': -565226067351276295,
                                        'source_pixel_width': -6753872669358620089,
                                        'source_pixel_height': -3005973174297171131,
                                        'rotation': -3693527744970510510,
                                        'virtual_nw_x_pixel': -901856411,
                                        'virtual_nw_y_pixel': 1315086038,
                                        'virtual_width': -1149077957,
                                        'virtual_height': -1888040952,
                                    },
                            {
                                        'source_monitor': 7322402,
                                        'source_nw_x_pixel': -2337605783379967452,
                                        'source_nw_y_pixel': -5018736711444678972,
                                        'source_pixel_width': -6692157497873488625,
                                        'source_pixel_height': -3321093567532777487,
                                        'rotation': -5605063417309822877,
                                        'virtual_nw_x_pixel': -636295403,
                                        'virtual_nw_y_pixel': -374391286,
                                        'virtual_width': -1270473878,
                                        'virtual_height': 902313213,
                                    },
                            {
                                        'source_monitor': 6364741,
                                        'source_nw_x_pixel': -105934648790836436,
                                        'source_nw_y_pixel': -6279511466005665722,
                                        'source_pixel_width': -8272057615078597554,
                                        'source_pixel_height': -1692127704370194240,
                                        'rotation': -3930846236374330062,
                                        'virtual_nw_x_pixel': 321878188,
                                        'virtual_nw_y_pixel': 1736494970,
                                        'virtual_width': 269345385,
                                        'virtual_height': 459847283,
                                    },
                            {
                                        'source_monitor': 2718730,
                                        'source_nw_x_pixel': -4530576047197118336,
                                        'source_nw_y_pixel': -7368098098458146263,
                                        'source_pixel_width': -6545009545926107771,
                                        'source_pixel_height': -7544407080237977553,
                                        'rotation': -2379271836117277396,
                                        'virtual_nw_x_pixel': -1735797876,
                                        'virtual_nw_y_pixel': 879302710,
                                        'virtual_width': -683115680,
                                        'virtual_height': -441292974,
                                    },
                            {
                                        'source_monitor': 6306786,
                                        'source_nw_x_pixel': -7633593951127998079,
                                        'source_nw_y_pixel': -2364627969854583998,
                                        'source_pixel_width': -7601545505916889109,
                                        'source_pixel_height': -3339335549552747390,
                                        'rotation': -7234243572864099697,
                                        'virtual_nw_x_pixel': 139653123,
                                        'virtual_nw_y_pixel': 478176923,
                                        'virtual_width': 1152517995,
                                        'virtual_height': 1792288189,
                                    },
                            {
                                        'source_monitor': -184397,
                                        'source_nw_x_pixel': -3408341250255639363,
                                        'source_nw_y_pixel': -196520091114521980,
                                        'source_pixel_width': -1790213399789095549,
                                        'source_pixel_height': -14253553981826277,
                                        'rotation': -3922996671904241335,
                                        'virtual_nw_x_pixel': -884092310,
                                        'virtual_nw_y_pixel': 1960759241,
                                        'virtual_width': 11597387,
                                        'virtual_height': 247012244,
                                    },
                        ],
                },
                {
                    'description': 'şɛϨчиҰвȌŢǌɟ¹ɵŮɓɆüƶeЍ΅˝ǽĵúCЄƻ¥ǒ',
                    'monitors': [
                            {
                                        'identifier': 393165,
                                        'width': -5756228148483075482,
                                        'height': 6648419013143202729,
                                    },
                            {
                                        'identifier': 5654621,
                                        'width': 6769897825815294536,
                                        'height': -2362183729099450869,
                                    },
                            {
                                        'identifier': 3002461,
                                        'width': 343591906117011178,
                                        'height': -5206773662236661684,
                                    },
                            {
                                        'identifier': 8119750,
                                        'width': -1248766213940814942,
                                        'height': -7982246892099240859,
                                    },
                            {
                                        'identifier': 3962225,
                                        'width': 3777404927095479685,
                                        'height': 4446934613196882782,
                                    },
                            {
                                        'identifier': -548993,
                                        'width': 7899689922957136575,
                                        'height': 8249477157332055529,
                                    },
                            {
                                        'identifier': -747312,
                                        'width': -4600180593094783210,
                                        'height': -7543265205006837153,
                                    },
                            {
                                        'identifier': 8842219,
                                        'width': -52740826827150933,
                                        'height': -8872472182844256747,
                                    },
                            {
                                        'identifier': 6482556,
                                        'width': 8607932750909271238,
                                        'height': -5914335383567111909,
                                    },
                            {
                                        'identifier': 6189878,
                                        'width': -5382492466131431299,
                                        'height': -2691356370330298444,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1297558,
                                        'source_nw_x_pixel': -7221465518832015221,
                                        'source_nw_y_pixel': -2744407720148693832,
                                        'source_pixel_width': -8672908230671310650,
                                        'source_pixel_height': -7693561861274492937,
                                        'rotation': -1396590611389694329,
                                        'virtual_nw_x_pixel': -647318699,
                                        'virtual_nw_y_pixel': 1899901887,
                                        'virtual_width': -768982846,
                                        'virtual_height': 1710878274,
                                    },
                            {
                                        'source_monitor': 154828,
                                        'source_nw_x_pixel': -7232809271553028329,
                                        'source_nw_y_pixel': -8701989161903702623,
                                        'source_pixel_width': -4893719130703596511,
                                        'source_pixel_height': -3857012523235205156,
                                        'rotation': -6111359673511651938,
                                        'virtual_nw_x_pixel': 1173669141,
                                        'virtual_nw_y_pixel': 238311049,
                                        'virtual_width': 1522004877,
                                        'virtual_height': 1521775116,
                                    },
                            {
                                        'source_monitor': 216165,
                                        'source_nw_x_pixel': -8401284724435598677,
                                        'source_nw_y_pixel': -1946933997006914472,
                                        'source_pixel_width': -1411594302977182339,
                                        'source_pixel_height': -4111113883978390698,
                                        'rotation': -6124123070409800069,
                                        'virtual_nw_x_pixel': 1274448396,
                                        'virtual_nw_y_pixel': 431901411,
                                        'virtual_width': 443644355,
                                        'virtual_height': 1968388471,
                                    },
                            {
                                        'source_monitor': 5983920,
                                        'source_nw_x_pixel': -6348858251953839290,
                                        'source_nw_y_pixel': -8985519957836834306,
                                        'source_pixel_width': -1743308117468187121,
                                        'source_pixel_height': -2357906004071554388,
                                        'rotation': -4342396055199140070,
                                        'virtual_nw_x_pixel': -506376571,
                                        'virtual_nw_y_pixel': -1728190430,
                                        'virtual_width': 1101919443,
                                        'virtual_height': -554676414,
                                    },
                            {
                                        'source_monitor': 7446663,
                                        'source_nw_x_pixel': -2771627978491967039,
                                        'source_nw_y_pixel': -2198774343511311600,
                                        'source_pixel_width': -6430689253353507237,
                                        'source_pixel_height': -8232060511361288000,
                                        'rotation': -2495447543010227107,
                                        'virtual_nw_x_pixel': -1378781511,
                                        'virtual_nw_y_pixel': 1797812035,
                                        'virtual_width': 1738664590,
                                        'virtual_height': 1968395199,
                                    },
                            {
                                        'source_monitor': 8709786,
                                        'source_nw_x_pixel': -960779957351760070,
                                        'source_nw_y_pixel': -8520427344651886288,
                                        'source_pixel_width': -2528832304023766129,
                                        'source_pixel_height': -117408707832806787,
                                        'rotation': -4971011305755228914,
                                        'virtual_nw_x_pixel': 1901165480,
                                        'virtual_nw_y_pixel': -1447649715,
                                        'virtual_width': 1886658464,
                                        'virtual_height': -1899656729,
                                    },
                            {
                                        'source_monitor': 3986393,
                                        'source_nw_x_pixel': -4259559521782108354,
                                        'source_nw_y_pixel': -2394497104248061781,
                                        'source_pixel_width': -4553280987626132485,
                                        'source_pixel_height': -8112998122406698100,
                                        'rotation': -2445918152166497299,
                                        'virtual_nw_x_pixel': -807697399,
                                        'virtual_nw_y_pixel': -1101202776,
                                        'virtual_width': -801730381,
                                        'virtual_height': 1793884055,
                                    },
                            {
                                        'source_monitor': 2576133,
                                        'source_nw_x_pixel': -726589170278626615,
                                        'source_nw_y_pixel': -7172855852303267067,
                                        'source_pixel_width': -2618496362672956523,
                                        'source_pixel_height': -7849138946690049948,
                                        'rotation': -3475183080183814087,
                                        'virtual_nw_x_pixel': 248887504,
                                        'virtual_nw_y_pixel': -1184323382,
                                        'virtual_width': -1154393456,
                                        'virtual_height': -1518624462,
                                    },
                            {
                                        'source_monitor': 6466977,
                                        'source_nw_x_pixel': -7349089625153319129,
                                        'source_nw_y_pixel': -6215748409442767314,
                                        'source_pixel_width': -1980475464899961850,
                                        'source_pixel_height': -8308172332667569934,
                                        'rotation': -9006643734594391567,
                                        'virtual_nw_x_pixel': 1636321604,
                                        'virtual_nw_y_pixel': -359707249,
                                        'virtual_width': -149051797,
                                        'virtual_height': -1339471287,
                                    },
                            {
                                        'source_monitor': -166343,
                                        'source_nw_x_pixel': -2492345238754953423,
                                        'source_nw_y_pixel': -7002996852964795840,
                                        'source_pixel_width': -6513215047898490957,
                                        'source_pixel_height': -6201655854550827471,
                                        'rotation': -5040535002488815279,
                                        'virtual_nw_x_pixel': -951094146,
                                        'virtual_nw_y_pixel': 1029901005,
                                        'virtual_width': 1532199778,
                                        'virtual_height': 1644940211,
                                    },
                        ],
                },
                {
                    'description': '҈ůҡĖлеҦɊƖ˯λƁ#ʅƅө˩Ӌʈ¿˞ѫʓІαLǒ˻xԣ',
                    'monitors': [
                            {
                                        'identifier': 4489169,
                                        'width': 5314083056501090186,
                                        'height': -3363788286083212772,
                                    },
                            {
                                        'identifier': 3291332,
                                        'width': 5467263288690138436,
                                        'height': 2941006721091414773,
                                    },
                            {
                                        'identifier': 5933766,
                                        'width': -732633116221365288,
                                        'height': 7668362883658477318,
                                    },
                            {
                                        'identifier': 3475479,
                                        'width': 2280217251609285334,
                                        'height': -654294500344044165,
                                    },
                            {
                                        'identifier': 457332,
                                        'width': 5967636127500089445,
                                        'height': 724637198645513570,
                                    },
                            {
                                        'identifier': 3782962,
                                        'width': -4318881932748752386,
                                        'height': -3246952902970567657,
                                    },
                            {
                                        'identifier': 1777463,
                                        'width': -3683331693706242835,
                                        'height': -6872072530639356763,
                                    },
                            {
                                        'identifier': 255995,
                                        'width': -774014339620997411,
                                        'height': -7664321940385882136,
                                    },
                            {
                                        'identifier': -892949,
                                        'width': 1145436417161900805,
                                        'height': -4953026336684272338,
                                    },
                            {
                                        'identifier': 1408091,
                                        'width': -4635958172699633641,
                                        'height': -9059423160344391509,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 1192124,
                                        'source_nw_x_pixel': -8540324004000136591,
                                        'source_nw_y_pixel': -6336501244798334385,
                                        'source_pixel_width': -626958762852556494,
                                        'source_pixel_height': -4049122681727464058,
                                        'rotation': -5950095662969466937,
                                        'virtual_nw_x_pixel': -1817626272,
                                        'virtual_nw_y_pixel': -1942351317,
                                        'virtual_width': 577830526,
                                        'virtual_height': -1568161665,
                                    },
                            {
                                        'source_monitor': 8392666,
                                        'source_nw_x_pixel': -4718561280437511830,
                                        'source_nw_y_pixel': -8433627729429945708,
                                        'source_pixel_width': -6420613372558169306,
                                        'source_pixel_height': -2086595702731634051,
                                        'rotation': -1981043443520463774,
                                        'virtual_nw_x_pixel': 1951864296,
                                        'virtual_nw_y_pixel': -1743286014,
                                        'virtual_width': 110897500,
                                        'virtual_height': -1288759918,
                                    },
                            {
                                        'source_monitor': -666333,
                                        'source_nw_x_pixel': -8167214944083276839,
                                        'source_nw_y_pixel': -6159099759875132218,
                                        'source_pixel_width': -31981728583531360,
                                        'source_pixel_height': -5133860632447226056,
                                        'rotation': -5155427057932934431,
                                        'virtual_nw_x_pixel': -40644867,
                                        'virtual_nw_y_pixel': -954423816,
                                        'virtual_width': -1496688500,
                                        'virtual_height': 80754868,
                                    },
                            {
                                        'source_monitor': 7140568,
                                        'source_nw_x_pixel': -2852732406563657316,
                                        'source_nw_y_pixel': -7315327434282735489,
                                        'source_pixel_width': -3620471451964593565,
                                        'source_pixel_height': -6898855539448965926,
                                        'rotation': -4727031749609429321,
                                        'virtual_nw_x_pixel': -1813128279,
                                        'virtual_nw_y_pixel': 661353926,
                                        'virtual_width': -48273614,
                                        'virtual_height': -1751938173,
                                    },
                            {
                                        'source_monitor': 3742131,
                                        'source_nw_x_pixel': -5107167928043939983,
                                        'source_nw_y_pixel': -3806095008416406332,
                                        'source_pixel_width': -4870351870457095015,
                                        'source_pixel_height': -8917322227866832410,
                                        'rotation': -7339511275530614847,
                                        'virtual_nw_x_pixel': -1582614170,
                                        'virtual_nw_y_pixel': 824986557,
                                        'virtual_width': 1339294855,
                                        'virtual_height': 288780030,
                                    },
                            {
                                        'source_monitor': 765101,
                                        'source_nw_x_pixel': -64559275306503105,
                                        'source_nw_y_pixel': -4584123404320052685,
                                        'source_pixel_width': -4663158517209025619,
                                        'source_pixel_height': -6907192273854339272,
                                        'rotation': -858576766491011322,
                                        'virtual_nw_x_pixel': 699770290,
                                        'virtual_nw_y_pixel': 140801108,
                                        'virtual_width': 444261330,
                                        'virtual_height': -1080867285,
                                    },
                            {
                                        'source_monitor': 2194360,
                                        'source_nw_x_pixel': -8149607125263029978,
                                        'source_nw_y_pixel': -8865600096591094174,
                                        'source_pixel_width': -3664959072981861847,
                                        'source_pixel_height': -4957210035076857724,
                                        'rotation': -5924706129639406457,
                                        'virtual_nw_x_pixel': -1539193685,
                                        'virtual_nw_y_pixel': -484584980,
                                        'virtual_width': -1527856150,
                                        'virtual_height': -558365254,
                                    },
                            {
                                        'source_monitor': 6293276,
                                        'source_nw_x_pixel': -6437770499515988749,
                                        'source_nw_y_pixel': -1028151395769152743,
                                        'source_pixel_width': -8591435223695066983,
                                        'source_pixel_height': -435010289936101921,
                                        'rotation': -8098583166903610318,
                                        'virtual_nw_x_pixel': -890725171,
                                        'virtual_nw_y_pixel': 798096043,
                                        'virtual_width': -266937911,
                                        'virtual_height': 247441939,
                                    },
                            {
                                        'source_monitor': 2869965,
                                        'source_nw_x_pixel': -8396756161084121000,
                                        'source_nw_y_pixel': -2100193133790369673,
                                        'source_pixel_width': -8349106515707387652,
                                        'source_pixel_height': -907950968405030993,
                                        'rotation': -3726289953225150923,
                                        'virtual_nw_x_pixel': -1763672403,
                                        'virtual_nw_y_pixel': -65035013,
                                        'virtual_width': -705299262,
                                        'virtual_height': -1270917454,
                                    },
                            {
                                        'source_monitor': 7574132,
                                        'source_nw_x_pixel': -5170841298100238491,
                                        'source_nw_y_pixel': -9207389671010938160,
                                        'source_pixel_width': -967474329755807775,
                                        'source_pixel_height': -753989747435164759,
                                        'rotation': -5741422478904192607,
                                        'virtual_nw_x_pixel': 583622012,
                                        'virtual_nw_y_pixel': 1350353056,
                                        'virtual_width': -563139978,
                                        'virtual_height': -1289689322,
                                    },
                        ],
                },
                {
                    'description': 'dϫȭ¯ĿĿԎ½ʗêɚϵǤ\x8dӣήʌ˞ɳ\xa0Ўώ*þuґЁѳ5ǣ',
                    'monitors': [
                            {
                                        'identifier': 2660252,
                                        'width': -377001931912131185,
                                        'height': -3984498266987255223,
                                    },
                            {
                                        'identifier': 5931359,
                                        'width': 589644552780740224,
                                        'height': -6472000244733501851,
                                    },
                            {
                                        'identifier': 5621125,
                                        'width': -1176122817791796395,
                                        'height': 7183047315028930732,
                                    },
                            {
                                        'identifier': 9738462,
                                        'width': -8034505469076870830,
                                        'height': 7373616295470440501,
                                    },
                            {
                                        'identifier': 9075104,
                                        'width': -4987422508141044046,
                                        'height': 1058703548219819184,
                                    },
                            {
                                        'identifier': 7417382,
                                        'width': 5032338503631789143,
                                        'height': 5160448182018515903,
                                    },
                            {
                                        'identifier': 5850616,
                                        'width': -3451521728824873368,
                                        'height': -6479882527365532254,
                                    },
                            {
                                        'identifier': 9641147,
                                        'width': 2509011234439986930,
                                        'height': 5319494306985135864,
                                    },
                            {
                                        'identifier': 4757467,
                                        'width': 5859232713981502623,
                                        'height': 6650386587885493968,
                                    },
                            {
                                        'identifier': 7979485,
                                        'width': -1450532767333187857,
                                        'height': -3824639576154484022,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 7800233,
                                        'source_nw_x_pixel': -4108025685951737826,
                                        'source_nw_y_pixel': -6256865248485533474,
                                        'source_pixel_width': -6939748830112147947,
                                        'source_pixel_height': -2309539637518999410,
                                        'rotation': -6511735084815552576,
                                        'virtual_nw_x_pixel': 1707966506,
                                        'virtual_nw_y_pixel': 1807984037,
                                        'virtual_width': -486827883,
                                        'virtual_height': -715722417,
                                    },
                            {
                                        'source_monitor': 8290439,
                                        'source_nw_x_pixel': -8961907805108110778,
                                        'source_nw_y_pixel': -6897060280833169062,
                                        'source_pixel_width': -9136982822582082522,
                                        'source_pixel_height': -5159626512443375823,
                                        'rotation': -5743990863848636359,
                                        'virtual_nw_x_pixel': -890956462,
                                        'virtual_nw_y_pixel': 356772398,
                                        'virtual_width': 522868381,
                                        'virtual_height': -785001220,
                                    },
                            {
                                        'source_monitor': 7368556,
                                        'source_nw_x_pixel': -8849453595576419927,
                                        'source_nw_y_pixel': -4930791628565419513,
                                        'source_pixel_width': -616204273213462244,
                                        'source_pixel_height': -4141471850837105917,
                                        'rotation': -1965091015260249898,
                                        'virtual_nw_x_pixel': -46949880,
                                        'virtual_nw_y_pixel': 1886348198,
                                        'virtual_width': -216356831,
                                        'virtual_height': 447303615,
                                    },
                            {
                                        'source_monitor': 1948213,
                                        'source_nw_x_pixel': -7609683087057901965,
                                        'source_nw_y_pixel': -6393939552683453827,
                                        'source_pixel_width': -5470847797706910853,
                                        'source_pixel_height': -4849339057801882266,
                                        'rotation': -1770767900979984559,
                                        'virtual_nw_x_pixel': 848724583,
                                        'virtual_nw_y_pixel': 1722481409,
                                        'virtual_width': 1167974679,
                                        'virtual_height': -323505919,
                                    },
                            {
                                        'source_monitor': 9179889,
                                        'source_nw_x_pixel': -4478559975964140112,
                                        'source_nw_y_pixel': -6594808457116831333,
                                        'source_pixel_width': -9213162524869056448,
                                        'source_pixel_height': -5582810752114469675,
                                        'rotation': -2601101806077326417,
                                        'virtual_nw_x_pixel': 590024595,
                                        'virtual_nw_y_pixel': -259950610,
                                        'virtual_width': -750921588,
                                        'virtual_height': -1498139877,
                                    },
                            {
                                        'source_monitor': 1276963,
                                        'source_nw_x_pixel': -7491888243538744636,
                                        'source_nw_y_pixel': -5699219323092032377,
                                        'source_pixel_width': -3914531785922503918,
                                        'source_pixel_height': -6245613008250391071,
                                        'rotation': -6550258083260080190,
                                        'virtual_nw_x_pixel': -967956436,
                                        'virtual_nw_y_pixel': -155957359,
                                        'virtual_width': -1871544280,
                                        'virtual_height': 1374717323,
                                    },
                            {
                                        'source_monitor': 9681516,
                                        'source_nw_x_pixel': -129843256876613480,
                                        'source_nw_y_pixel': -3741979435684764189,
                                        'source_pixel_width': -9022556594718995534,
                                        'source_pixel_height': -4584488718895733433,
                                        'rotation': -8029655626537670319,
                                        'virtual_nw_x_pixel': -645378821,
                                        'virtual_nw_y_pixel': -681401801,
                                        'virtual_width': 274075104,
                                        'virtual_height': -619435424,
                                    },
                            {
                                        'source_monitor': 6539274,
                                        'source_nw_x_pixel': -8245954188455086507,
                                        'source_nw_y_pixel': -3484443771978299606,
                                        'source_pixel_width': -3496404391298196164,
                                        'source_pixel_height': -1676754125276660156,
                                        'rotation': -2256032642536565074,
                                        'virtual_nw_x_pixel': -887489618,
                                        'virtual_nw_y_pixel': -914630585,
                                        'virtual_width': -196158972,
                                        'virtual_height': 26225102,
                                    },
                            {
                                        'source_monitor': 7813256,
                                        'source_nw_x_pixel': -8404202303011158429,
                                        'source_nw_y_pixel': -1508650655201796114,
                                        'source_pixel_width': -6156807594302058123,
                                        'source_pixel_height': -1591398927015752607,
                                        'rotation': -3847502132139913060,
                                        'virtual_nw_x_pixel': -1991018989,
                                        'virtual_nw_y_pixel': 1468284916,
                                        'virtual_width': 1995477845,
                                        'virtual_height': 1409126022,
                                    },
                            {
                                        'source_monitor': 6475639,
                                        'source_nw_x_pixel': -313615857405898311,
                                        'source_nw_y_pixel': -6548664539086828362,
                                        'source_pixel_width': -1094092487739419941,
                                        'source_pixel_height': -4192195994410561743,
                                        'rotation': -5108837128694901185,
                                        'virtual_nw_x_pixel': -1348565407,
                                        'virtual_nw_y_pixel': 601768366,
                                        'virtual_width': 1370296145,
                                        'virtual_height': -950512093,
                                    },
                        ],
                },
                {
                    'description': 'ͽ˞ҫϗƓѕʝӲӓșΊԕπӭ˧ɨѤтӧÏԦ_χͿȳӶ°Үƹ©',
                    'monitors': [
                            {
                                        'identifier': 1681342,
                                        'width': 7621277716488861682,
                                        'height': 3908056315886764775,
                                    },
                            {
                                        'identifier': 4645137,
                                        'width': 5909536542371824272,
                                        'height': -3497735513122801849,
                                    },
                            {
                                        'identifier': 7704760,
                                        'width': 7038341821848898870,
                                        'height': -6361243187240514668,
                                    },
                            {
                                        'identifier': 6573616,
                                        'width': -5800901233360647354,
                                        'height': 3548746803018718038,
                                    },
                            {
                                        'identifier': 494813,
                                        'width': -4291626542595602173,
                                        'height': 3778429724220033966,
                                    },
                            {
                                        'identifier': 6612481,
                                        'width': -2974745652079615273,
                                        'height': 3186819132158601821,
                                    },
                            {
                                        'identifier': 5349353,
                                        'width': 174376127727603437,
                                        'height': 5189296538674336341,
                                    },
                            {
                                        'identifier': 7904978,
                                        'width': -472300329071458627,
                                        'height': -2260170338333885639,
                                    },
                            {
                                        'identifier': 5058305,
                                        'width': -2215210612282513300,
                                        'height': 879216584370925819,
                                    },
                            {
                                        'identifier': 2974501,
                                        'width': -5839180832235389225,
                                        'height': 3658762105231075860,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 3715289,
                                        'source_nw_x_pixel': -707298605036595137,
                                        'source_nw_y_pixel': -1885049822032019701,
                                        'source_pixel_width': -1062407466025080385,
                                        'source_pixel_height': -5374267036375732239,
                                        'rotation': -746006745184097385,
                                        'virtual_nw_x_pixel': -1419711528,
                                        'virtual_nw_y_pixel': 1737419699,
                                        'virtual_width': -337597563,
                                        'virtual_height': 1085221762,
                                    },
                            {
                                        'source_monitor': 2937527,
                                        'source_nw_x_pixel': -2429007071108117329,
                                        'source_nw_y_pixel': -8910954281670062064,
                                        'source_pixel_width': -6227524060372078567,
                                        'source_pixel_height': -5787314991869507526,
                                        'rotation': -6247350060089275074,
                                        'virtual_nw_x_pixel': 348058959,
                                        'virtual_nw_y_pixel': -692974004,
                                        'virtual_width': 429122697,
                                        'virtual_height': -1590626182,
                                    },
                            {
                                        'source_monitor': 4949829,
                                        'source_nw_x_pixel': -2358028302127989463,
                                        'source_nw_y_pixel': -2544009870645039693,
                                        'source_pixel_width': -3111598912542553896,
                                        'source_pixel_height': -2614178837562480448,
                                        'rotation': -5254846020027940489,
                                        'virtual_nw_x_pixel': 993687859,
                                        'virtual_nw_y_pixel': 873771441,
                                        'virtual_width': -838457998,
                                        'virtual_height': -1095713139,
                                    },
                            {
                                        'source_monitor': 6918697,
                                        'source_nw_x_pixel': -5599154134316876396,
                                        'source_nw_y_pixel': -3666193822144935182,
                                        'source_pixel_width': -7494994758155005730,
                                        'source_pixel_height': -3487305946129944698,
                                        'rotation': -7803649348982568647,
                                        'virtual_nw_x_pixel': -559061713,
                                        'virtual_nw_y_pixel': -1932036521,
                                        'virtual_width': -663540508,
                                        'virtual_height': -372265939,
                                    },
                            {
                                        'source_monitor': 3246285,
                                        'source_nw_x_pixel': -536029832823751369,
                                        'source_nw_y_pixel': -777496974590877863,
                                        'source_pixel_width': -4786994436549639881,
                                        'source_pixel_height': -3526827173715886754,
                                        'rotation': -5860491670990795999,
                                        'virtual_nw_x_pixel': 1383775009,
                                        'virtual_nw_y_pixel': -1526756055,
                                        'virtual_width': 339127766,
                                        'virtual_height': -1777993549,
                                    },
                            {
                                        'source_monitor': 2307853,
                                        'source_nw_x_pixel': -6023154520681593399,
                                        'source_nw_y_pixel': -8263771192669111833,
                                        'source_pixel_width': -196602196216254083,
                                        'source_pixel_height': -4755664976686251253,
                                        'rotation': -8986094166178509592,
                                        'virtual_nw_x_pixel': 1379773693,
                                        'virtual_nw_y_pixel': -1604639176,
                                        'virtual_width': -395008148,
                                        'virtual_height': -285620166,
                                    },
                            {
                                        'source_monitor': 2590846,
                                        'source_nw_x_pixel': -7454729976482225473,
                                        'source_nw_y_pixel': -8918198896079020936,
                                        'source_pixel_width': -8755901614261270741,
                                        'source_pixel_height': -6716136871073012933,
                                        'rotation': -148049764012974737,
                                        'virtual_nw_x_pixel': -933066460,
                                        'virtual_nw_y_pixel': 1101963614,
                                        'virtual_width': 1959983943,
                                        'virtual_height': -1610327146,
                                    },
                            {
                                        'source_monitor': -247987,
                                        'source_nw_x_pixel': -8469660732708194474,
                                        'source_nw_y_pixel': -7219638182083550066,
                                        'source_pixel_width': -4478671732203665248,
                                        'source_pixel_height': -4394619657343982814,
                                        'rotation': -94274168127215136,
                                        'virtual_nw_x_pixel': 151252352,
                                        'virtual_nw_y_pixel': 1508122775,
                                        'virtual_width': -505826413,
                                        'virtual_height': 956679974,
                                    },
                            {
                                        'source_monitor': -628299,
                                        'source_nw_x_pixel': -5335442670692696941,
                                        'source_nw_y_pixel': -1401202589742176209,
                                        'source_pixel_width': -8940088513488431130,
                                        'source_pixel_height': -7911507903302046,
                                        'rotation': -4232044896280676818,
                                        'virtual_nw_x_pixel': -245077552,
                                        'virtual_nw_y_pixel': -1794758430,
                                        'virtual_width': 1860487787,
                                        'virtual_height': -134063970,
                                    },
                            {
                                        'source_monitor': 8934597,
                                        'source_nw_x_pixel': -7484833945273095406,
                                        'source_nw_y_pixel': -1369724533001227507,
                                        'source_pixel_width': -3319392561897505763,
                                        'source_pixel_height': -2214551068016573562,
                                        'rotation': -5916092002907867662,
                                        'virtual_nw_x_pixel': -67146891,
                                        'virtual_nw_y_pixel': 1722702943,
                                        'virtual_width': 377094029,
                                        'virtual_height': 289552944,
                                    },
                        ],
                },
                {
                    'description': '\u038bǶ΅ĐѝѬѩįҔϏұȻɺʢƆcνӚZΦӏƋüӬҼ¸ċɗңé',
                    'monitors': [
                            {
                                        'identifier': 6373972,
                                        'width': -8303277591385131574,
                                        'height': -3983860736486613075,
                                    },
                            {
                                        'identifier': 7218909,
                                        'width': -2329665904503062657,
                                        'height': 6829154713017080207,
                                    },
                            {
                                        'identifier': 5813791,
                                        'width': 5314624407685640920,
                                        'height': -5690267798215267061,
                                    },
                            {
                                        'identifier': 8093240,
                                        'width': -157152570839923395,
                                        'height': 8775425216449280805,
                                    },
                            {
                                        'identifier': 8478881,
                                        'width': -6515302314136026161,
                                        'height': 5595845938951279775,
                                    },
                            {
                                        'identifier': 4151178,
                                        'width': 9120535362530674890,
                                        'height': -5548500701628938468,
                                    },
                            {
                                        'identifier': 170781,
                                        'width': -2522778289262643611,
                                        'height': -3931949954695625887,
                                    },
                            {
                                        'identifier': -552187,
                                        'width': 2282006251913717428,
                                        'height': -4660739744099249627,
                                    },
                            {
                                        'identifier': -988613,
                                        'width': -5461666248581413893,
                                        'height': -8978072244484175722,
                                    },
                            {
                                        'identifier': 888099,
                                        'width': -62846978994636347,
                                        'height': -4022109684873178990,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -932692,
                                        'source_nw_x_pixel': -3027803401221758248,
                                        'source_nw_y_pixel': -1234927051136181469,
                                        'source_pixel_width': -6041115706210077935,
                                        'source_pixel_height': -3984226402973036784,
                                        'rotation': -5225365073487106430,
                                        'virtual_nw_x_pixel': -1230378295,
                                        'virtual_nw_y_pixel': -127725035,
                                        'virtual_width': 899217502,
                                        'virtual_height': -17771400,
                                    },
                            {
                                        'source_monitor': -823250,
                                        'source_nw_x_pixel': -2826365556244671553,
                                        'source_nw_y_pixel': -6331033632457264976,
                                        'source_pixel_width': -3117495543188098513,
                                        'source_pixel_height': -8272151109230874031,
                                        'rotation': -1934902350089767041,
                                        'virtual_nw_x_pixel': 1617491646,
                                        'virtual_nw_y_pixel': -1243940651,
                                        'virtual_width': 103093062,
                                        'virtual_height': -980750431,
                                    },
                            {
                                        'source_monitor': 7045873,
                                        'source_nw_x_pixel': -1925025683196679020,
                                        'source_nw_y_pixel': -3737772051340040670,
                                        'source_pixel_width': -170933000734268282,
                                        'source_pixel_height': -5123751516378076243,
                                        'rotation': -7428367835206827052,
                                        'virtual_nw_x_pixel': -1095744923,
                                        'virtual_nw_y_pixel': -649630152,
                                        'virtual_width': -845247472,
                                        'virtual_height': -983123939,
                                    },
                            {
                                        'source_monitor': 4316820,
                                        'source_nw_x_pixel': -5082983006823231035,
                                        'source_nw_y_pixel': -8482282552460643290,
                                        'source_pixel_width': -3652631641946798284,
                                        'source_pixel_height': -7274981901053352505,
                                        'rotation': -2440063360460800936,
                                        'virtual_nw_x_pixel': -1986431435,
                                        'virtual_nw_y_pixel': 1341655961,
                                        'virtual_width': -1636735604,
                                        'virtual_height': -1524564890,
                                    },
                            {
                                        'source_monitor': 8836674,
                                        'source_nw_x_pixel': -5890644139415494437,
                                        'source_nw_y_pixel': -4776928325665676240,
                                        'source_pixel_width': -3696360120661333026,
                                        'source_pixel_height': -3736676464498067561,
                                        'rotation': -1931896462221166698,
                                        'virtual_nw_x_pixel': 600947959,
                                        'virtual_nw_y_pixel': 1481985230,
                                        'virtual_width': -1712683495,
                                        'virtual_height': -89121498,
                                    },
                            {
                                        'source_monitor': 352348,
                                        'source_nw_x_pixel': -3629906961704164151,
                                        'source_nw_y_pixel': -725901018240657729,
                                        'source_pixel_width': -4600579159685251655,
                                        'source_pixel_height': -686796840816018726,
                                        'rotation': -976339873950206172,
                                        'virtual_nw_x_pixel': -1677319748,
                                        'virtual_nw_y_pixel': 1424090268,
                                        'virtual_width': -1526063237,
                                        'virtual_height': 1251712541,
                                    },
                            {
                                        'source_monitor': 5884272,
                                        'source_nw_x_pixel': -909221750501528481,
                                        'source_nw_y_pixel': -1624752378799756827,
                                        'source_pixel_width': -3558903862460413826,
                                        'source_pixel_height': -8634602870142026422,
                                        'rotation': -8800768616141473864,
                                        'virtual_nw_x_pixel': -1312184056,
                                        'virtual_nw_y_pixel': -1862699996,
                                        'virtual_width': 477114171,
                                        'virtual_height': -1339637089,
                                    },
                            {
                                        'source_monitor': 4664197,
                                        'source_nw_x_pixel': -8550871814155787494,
                                        'source_nw_y_pixel': -1321685082684733892,
                                        'source_pixel_width': -3826551969806372428,
                                        'source_pixel_height': -1356162634675460427,
                                        'rotation': -429193502175657770,
                                        'virtual_nw_x_pixel': 1595161567,
                                        'virtual_nw_y_pixel': 534966589,
                                        'virtual_width': 874176569,
                                        'virtual_height': -1229655060,
                                    },
                            {
                                        'source_monitor': 1024457,
                                        'source_nw_x_pixel': -7508224485523838720,
                                        'source_nw_y_pixel': -3060653254607454482,
                                        'source_pixel_width': -1988215713957573825,
                                        'source_pixel_height': -4066978564565171974,
                                        'rotation': -6565231622647223814,
                                        'virtual_nw_x_pixel': -238021022,
                                        'virtual_nw_y_pixel': -670111586,
                                        'virtual_width': 1468722901,
                                        'virtual_height': -165119714,
                                    },
                            {
                                        'source_monitor': 1626050,
                                        'source_nw_x_pixel': -7611953164675489336,
                                        'source_nw_y_pixel': -3819607828821718825,
                                        'source_pixel_width': -8181692525981777432,
                                        'source_pixel_height': -2769577804155510047,
                                        'rotation': -5311614397428696078,
                                        'virtual_nw_x_pixel': 1878780057,
                                        'virtual_nw_y_pixel': -1392988404,
                                        'virtual_width': 985002176,
                                        'virtual_height': -721525304,
                                    },
                        ],
                },
                {
                    'description': 'ҙ[\x96Ūʥ\x94ʔ˱ѥЁӈNмϕǬcʾɲϣʡЮȿǏŠʣƤӯĿXđ',
                    'monitors': [
                            {
                                        'identifier': 9114013,
                                        'width': 7584795536061807436,
                                        'height': 175487733761887449,
                                    },
                            {
                                        'identifier': 9539249,
                                        'width': 6371682850071142459,
                                        'height': 3430034837060601956,
                                    },
                            {
                                        'identifier': 9366651,
                                        'width': -9201484198673165687,
                                        'height': 8344202877018468649,
                                    },
                            {
                                        'identifier': 1206087,
                                        'width': -1750944161609217194,
                                        'height': -8926520830630272326,
                                    },
                            {
                                        'identifier': 6831781,
                                        'width': -6652109058254459398,
                                        'height': 1051634472783155635,
                                    },
                            {
                                        'identifier': 7460956,
                                        'width': -2039229660122182507,
                                        'height': 1332759483122144777,
                                    },
                            {
                                        'identifier': 5292170,
                                        'width': 4084404354057133673,
                                        'height': 5880340144179715699,
                                    },
                            {
                                        'identifier': 1385953,
                                        'width': -7111686420141035535,
                                        'height': -5542675170025178199,
                                    },
                            {
                                        'identifier': 585211,
                                        'width': -4630061684029513216,
                                        'height': -5151111584071725872,
                                    },
                            {
                                        'identifier': 4159088,
                                        'width': 3008621222771954564,
                                        'height': -4542175930628238010,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 623243,
                                        'source_nw_x_pixel': -8703404192873147853,
                                        'source_nw_y_pixel': -3244867309824104881,
                                        'source_pixel_width': -2555282217148774200,
                                        'source_pixel_height': -5460506850437240668,
                                        'rotation': -1606563731457584060,
                                        'virtual_nw_x_pixel': -188786937,
                                        'virtual_nw_y_pixel': 1359933841,
                                        'virtual_width': -577607406,
                                        'virtual_height': -345565082,
                                    },
                            {
                                        'source_monitor': 5735062,
                                        'source_nw_x_pixel': -1339969228197231568,
                                        'source_nw_y_pixel': -6527128723492794207,
                                        'source_pixel_width': -2028164102216806799,
                                        'source_pixel_height': -3536535851411575997,
                                        'rotation': -9122442838020915628,
                                        'virtual_nw_x_pixel': -938529803,
                                        'virtual_nw_y_pixel': -356509812,
                                        'virtual_width': 1398902681,
                                        'virtual_height': -105873831,
                                    },
                            {
                                        'source_monitor': 4138544,
                                        'source_nw_x_pixel': -4697702865360768088,
                                        'source_nw_y_pixel': -9050897611102446857,
                                        'source_pixel_width': -1308324710738855301,
                                        'source_pixel_height': -7725321666557592109,
                                        'rotation': -675373439303191366,
                                        'virtual_nw_x_pixel': -911675274,
                                        'virtual_nw_y_pixel': -1652696541,
                                        'virtual_width': -1123247948,
                                        'virtual_height': 1076477011,
                                    },
                            {
                                        'source_monitor': 6158855,
                                        'source_nw_x_pixel': -4459422002709614225,
                                        'source_nw_y_pixel': -926394015068453159,
                                        'source_pixel_width': -3961703214885382890,
                                        'source_pixel_height': -7561222839811361500,
                                        'rotation': -1908442910030042055,
                                        'virtual_nw_x_pixel': 561981714,
                                        'virtual_nw_y_pixel': -464243746,
                                        'virtual_width': 1744194318,
                                        'virtual_height': 412412417,
                                    },
                            {
                                        'source_monitor': 9474664,
                                        'source_nw_x_pixel': -8077437303315394925,
                                        'source_nw_y_pixel': -3846733075231807010,
                                        'source_pixel_width': -3477327256617457096,
                                        'source_pixel_height': -8252145299889075948,
                                        'rotation': -6501930124743416533,
                                        'virtual_nw_x_pixel': 1626385451,
                                        'virtual_nw_y_pixel': 1298882314,
                                        'virtual_width': 365058589,
                                        'virtual_height': -1221148261,
                                    },
                            {
                                        'source_monitor': 4485772,
                                        'source_nw_x_pixel': -2939475258672920904,
                                        'source_nw_y_pixel': -6968121660514015697,
                                        'source_pixel_width': -3455196338449651384,
                                        'source_pixel_height': -6735471378773881764,
                                        'rotation': -1459481745586528617,
                                        'virtual_nw_x_pixel': -741387745,
                                        'virtual_nw_y_pixel': -1519186252,
                                        'virtual_width': -914506391,
                                        'virtual_height': 387291787,
                                    },
                            {
                                        'source_monitor': 2467871,
                                        'source_nw_x_pixel': -6818268260737724584,
                                        'source_nw_y_pixel': -8692171603570074774,
                                        'source_pixel_width': -5214553226198121328,
                                        'source_pixel_height': -4535328830812957873,
                                        'rotation': -3987931059211158989,
                                        'virtual_nw_x_pixel': -998664692,
                                        'virtual_nw_y_pixel': -282275698,
                                        'virtual_width': 788574881,
                                        'virtual_height': -1889218855,
                                    },
                            {
                                        'source_monitor': 3757919,
                                        'source_nw_x_pixel': -3897263337252391259,
                                        'source_nw_y_pixel': -2209470754637201126,
                                        'source_pixel_width': -6098497240190972750,
                                        'source_pixel_height': -7508613399664224708,
                                        'rotation': -8615453466224254377,
                                        'virtual_nw_x_pixel': -1590272612,
                                        'virtual_nw_y_pixel': -383855233,
                                        'virtual_width': -838967412,
                                        'virtual_height': 260468150,
                                    },
                            {
                                        'source_monitor': 699802,
                                        'source_nw_x_pixel': -4569726208385129610,
                                        'source_nw_y_pixel': -2531917586078186591,
                                        'source_pixel_width': -6953215767445983072,
                                        'source_pixel_height': -8792918362151039529,
                                        'rotation': -8647181454427184943,
                                        'virtual_nw_x_pixel': 1133406521,
                                        'virtual_nw_y_pixel': 70946756,
                                        'virtual_width': 1136038119,
                                        'virtual_height': -431766895,
                                    },
                            {
                                        'source_monitor': -673852,
                                        'source_nw_x_pixel': -8601017206265957845,
                                        'source_nw_y_pixel': -1389076952929578465,
                                        'source_pixel_width': -231036421682543931,
                                        'source_pixel_height': -3986588631059912151,
                                        'rotation': -4231316624823905845,
                                        'virtual_nw_x_pixel': -338647181,
                                        'virtual_nw_y_pixel': 512074747,
                                        'virtual_width': 496270073,
                                        'virtual_height': 641321321,
                                    },
                        ],
                },
                {
                    'description': 'eнȥĭăƛʓĄҠΩȫĤңÄŇãĵȚӰD\x95Ӓ\x8eı£ϔʶīǑϷ',
                    'monitors': [
                            {
                                        'identifier': 5837091,
                                        'width': -8485712635304800268,
                                        'height': -3776764743172406475,
                                    },
                            {
                                        'identifier': 9629826,
                                        'width': -980074329436725472,
                                        'height': 8989594720340276862,
                                    },
                            {
                                        'identifier': 2308003,
                                        'width': 554155954144915615,
                                        'height': 521799404192972357,
                                    },
                            {
                                        'identifier': 2529866,
                                        'width': -7254864474032336974,
                                        'height': -4258668402708791991,
                                    },
                            {
                                        'identifier': 3684801,
                                        'width': -5197956084480030984,
                                        'height': -7509632368575984682,
                                    },
                            {
                                        'identifier': 2579796,
                                        'width': -3105909415421406355,
                                        'height': -4334124029886522751,
                                    },
                            {
                                        'identifier': 9798898,
                                        'width': -3309643590726817532,
                                        'height': -4021883467429494770,
                                    },
                            {
                                        'identifier': 4559958,
                                        'width': 7652238331670544709,
                                        'height': -9218788260637430479,
                                    },
                            {
                                        'identifier': 3450922,
                                        'width': 2968614198537687093,
                                        'height': 8075921795827962116,
                                    },
                            {
                                        'identifier': 9216944,
                                        'width': 3921366688569894645,
                                        'height': 4550280876191557251,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 57806,
                                        'source_nw_x_pixel': -6713452169977224437,
                                        'source_nw_y_pixel': -7529400733441532722,
                                        'source_pixel_width': -510188508709845914,
                                        'source_pixel_height': -5317787153824266843,
                                        'rotation': -7937142789714634603,
                                        'virtual_nw_x_pixel': 1256409579,
                                        'virtual_nw_y_pixel': 999754811,
                                        'virtual_width': 1492269061,
                                        'virtual_height': -1810815722,
                                    },
                            {
                                        'source_monitor': 7683680,
                                        'source_nw_x_pixel': -4496771528988059192,
                                        'source_nw_y_pixel': -5898576341618005627,
                                        'source_pixel_width': -4579992076446246671,
                                        'source_pixel_height': -5927658036160705042,
                                        'rotation': -6622189694381542156,
                                        'virtual_nw_x_pixel': 1445189599,
                                        'virtual_nw_y_pixel': 1201322109,
                                        'virtual_width': 1294371047,
                                        'virtual_height': -1387815372,
                                    },
                            {
                                        'source_monitor': 2740804,
                                        'source_nw_x_pixel': -1122408289582132737,
                                        'source_nw_y_pixel': -1227696948903922245,
                                        'source_pixel_width': -6012829325301107352,
                                        'source_pixel_height': -5345066092043115773,
                                        'rotation': -3364928888437935468,
                                        'virtual_nw_x_pixel': -913456421,
                                        'virtual_nw_y_pixel': -110706562,
                                        'virtual_width': 1708030062,
                                        'virtual_height': -899592074,
                                    },
                            {
                                        'source_monitor': 9744892,
                                        'source_nw_x_pixel': -4178793840377806091,
                                        'source_nw_y_pixel': -7890558602206510062,
                                        'source_pixel_width': -7479113939178277372,
                                        'source_pixel_height': -2259726887922806373,
                                        'rotation': -6619325911462823632,
                                        'virtual_nw_x_pixel': 1548695239,
                                        'virtual_nw_y_pixel': 845847777,
                                        'virtual_width': -1006376566,
                                        'virtual_height': -1746966216,
                                    },
                            {
                                        'source_monitor': 5655249,
                                        'source_nw_x_pixel': -3357059705926452870,
                                        'source_nw_y_pixel': -4345595618684745626,
                                        'source_pixel_width': -7445926484796273864,
                                        'source_pixel_height': -5308348629738816282,
                                        'rotation': -1953485934639918387,
                                        'virtual_nw_x_pixel': -1596200121,
                                        'virtual_nw_y_pixel': -711947356,
                                        'virtual_width': -159257490,
                                        'virtual_height': -1636687760,
                                    },
                            {
                                        'source_monitor': 8757858,
                                        'source_nw_x_pixel': -368794373873912005,
                                        'source_nw_y_pixel': -2216727334675606272,
                                        'source_pixel_width': -8976476113425894144,
                                        'source_pixel_height': -6468593172025795614,
                                        'rotation': -736706428322219462,
                                        'virtual_nw_x_pixel': 70705662,
                                        'virtual_nw_y_pixel': -1364329507,
                                        'virtual_width': -1511654975,
                                        'virtual_height': 394939756,
                                    },
                            {
                                        'source_monitor': 7545743,
                                        'source_nw_x_pixel': -962740923938517581,
                                        'source_nw_y_pixel': -7156844661721076048,
                                        'source_pixel_width': -2273595517693156220,
                                        'source_pixel_height': -3782573231329730381,
                                        'rotation': -517366546496048567,
                                        'virtual_nw_x_pixel': -1495470283,
                                        'virtual_nw_y_pixel': 4704750,
                                        'virtual_width': 472679934,
                                        'virtual_height': 1255929418,
                                    },
                            {
                                        'source_monitor': 5679347,
                                        'source_nw_x_pixel': -8595130752840315697,
                                        'source_nw_y_pixel': -4131864287078678832,
                                        'source_pixel_width': -6074425635228422001,
                                        'source_pixel_height': -678593810546173811,
                                        'rotation': -2661067419005158530,
                                        'virtual_nw_x_pixel': 217959147,
                                        'virtual_nw_y_pixel': 373363903,
                                        'virtual_width': 736814751,
                                        'virtual_height': -1474782832,
                                    },
                            {
                                        'source_monitor': 3154890,
                                        'source_nw_x_pixel': -7928601750661071310,
                                        'source_nw_y_pixel': -6847773576220977652,
                                        'source_pixel_width': -364379100848021919,
                                        'source_pixel_height': -7988837527995554240,
                                        'rotation': -7414305935796172379,
                                        'virtual_nw_x_pixel': 1505398774,
                                        'virtual_nw_y_pixel': -1996593741,
                                        'virtual_width': 578493887,
                                        'virtual_height': 569329053,
                                    },
                            {
                                        'source_monitor': 1733596,
                                        'source_nw_x_pixel': -4765470621803425856,
                                        'source_nw_y_pixel': -8162409603459901553,
                                        'source_pixel_width': -6799285695104730058,
                                        'source_pixel_height': -7792733423069975210,
                                        'rotation': -6822681342477074519,
                                        'virtual_nw_x_pixel': 510802218,
                                        'virtual_nw_y_pixel': -404985828,
                                        'virtual_width': -1305887144,
                                        'virtual_height': 16543066,
                                    },
                        ],
                },
                {
                    'description': 'ʾzӟҸċηҳԧľӧ\x8fȟƵƪĕʶƭɄxǃψ(ŻŉįӤŅҳÈǸ',
                    'monitors': [
                            {
                                        'identifier': 7467685,
                                        'width': 2155133376550010195,
                                        'height': -5166805494540528131,
                                    },
                            {
                                        'identifier': 4277841,
                                        'width': -437001959456356665,
                                        'height': -6924792023549838251,
                                    },
                            {
                                        'identifier': 4994385,
                                        'width': -8426550737264887262,
                                        'height': -1293377766535649696,
                                    },
                            {
                                        'identifier': 3780186,
                                        'width': 8993018622316461202,
                                        'height': -113707877107363461,
                                    },
                            {
                                        'identifier': 5014862,
                                        'width': -4440803482611528388,
                                        'height': -7053797627205907686,
                                    },
                            {
                                        'identifier': 9252440,
                                        'width': -3650931557734517214,
                                        'height': 6064304492146816877,
                                    },
                            {
                                        'identifier': 4743048,
                                        'width': 5154910252891026271,
                                        'height': 3732489275999259382,
                                    },
                            {
                                        'identifier': 2074629,
                                        'width': -1202696862879712061,
                                        'height': -1029302859560051664,
                                    },
                            {
                                        'identifier': 4932442,
                                        'width': -6422777775318755203,
                                        'height': -6298456405118044084,
                                    },
                            {
                                        'identifier': 9357792,
                                        'width': -7882890565579619730,
                                        'height': 9169555378941985565,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6410226,
                                        'source_nw_x_pixel': -3217940737240906084,
                                        'source_nw_y_pixel': -5165931098879671944,
                                        'source_pixel_width': -8390848182908017230,
                                        'source_pixel_height': -9136770607082486987,
                                        'rotation': -8426474551588898734,
                                        'virtual_nw_x_pixel': 1846023416,
                                        'virtual_nw_y_pixel': -1536543148,
                                        'virtual_width': -1884276840,
                                        'virtual_height': -1067627795,
                                    },
                            {
                                        'source_monitor': 9571080,
                                        'source_nw_x_pixel': -4792612490375154244,
                                        'source_nw_y_pixel': -412668141263208881,
                                        'source_pixel_width': -474381349671283757,
                                        'source_pixel_height': -6118177350718864654,
                                        'rotation': -4173193136921931494,
                                        'virtual_nw_x_pixel': 408634554,
                                        'virtual_nw_y_pixel': 1220931050,
                                        'virtual_width': 1693149832,
                                        'virtual_height': 1862310054,
                                    },
                            {
                                        'source_monitor': 9188076,
                                        'source_nw_x_pixel': -1290433386011543211,
                                        'source_nw_y_pixel': -3270184012534575933,
                                        'source_pixel_width': -1907866945139565308,
                                        'source_pixel_height': -8792792747710130947,
                                        'rotation': -1682020310744084618,
                                        'virtual_nw_x_pixel': 640995207,
                                        'virtual_nw_y_pixel': 1291797222,
                                        'virtual_width': -38548866,
                                        'virtual_height': 1506472263,
                                    },
                            {
                                        'source_monitor': -321416,
                                        'source_nw_x_pixel': -671521335931667603,
                                        'source_nw_y_pixel': -4089794381169529541,
                                        'source_pixel_width': -1203341403532727808,
                                        'source_pixel_height': -762958411237095338,
                                        'rotation': -8051381707740721223,
                                        'virtual_nw_x_pixel': 444123141,
                                        'virtual_nw_y_pixel': 490328849,
                                        'virtual_width': 1974043270,
                                        'virtual_height': -277093591,
                                    },
                            {
                                        'source_monitor': 1922938,
                                        'source_nw_x_pixel': -5287904722204527040,
                                        'source_nw_y_pixel': -4498038286181966079,
                                        'source_pixel_width': -7446032338223104275,
                                        'source_pixel_height': -7077150021220373110,
                                        'rotation': -8278093942487529279,
                                        'virtual_nw_x_pixel': -1454417523,
                                        'virtual_nw_y_pixel': 1590481540,
                                        'virtual_width': -642157924,
                                        'virtual_height': -446787770,
                                    },
                            {
                                        'source_monitor': 8372956,
                                        'source_nw_x_pixel': -1691639614581471867,
                                        'source_nw_y_pixel': -5862856681185425523,
                                        'source_pixel_width': -5775636745803523884,
                                        'source_pixel_height': -5992243576940754474,
                                        'rotation': -2730101056352210069,
                                        'virtual_nw_x_pixel': -951511287,
                                        'virtual_nw_y_pixel': 652649430,
                                        'virtual_width': 988503645,
                                        'virtual_height': 281382205,
                                    },
                            {
                                        'source_monitor': 4008506,
                                        'source_nw_x_pixel': -1689151892984521090,
                                        'source_nw_y_pixel': -9177741301118226851,
                                        'source_pixel_width': -975725903694093045,
                                        'source_pixel_height': -4743895766492009026,
                                        'rotation': -6963558074436980934,
                                        'virtual_nw_x_pixel': -1849841745,
                                        'virtual_nw_y_pixel': 448116425,
                                        'virtual_width': 1036975154,
                                        'virtual_height': -842863595,
                                    },
                            {
                                        'source_monitor': 396603,
                                        'source_nw_x_pixel': -9136392738987428475,
                                        'source_nw_y_pixel': -3635340170234408396,
                                        'source_pixel_width': -6796085599224556828,
                                        'source_pixel_height': -6308284530923281529,
                                        'rotation': -6554320784219364956,
                                        'virtual_nw_x_pixel': -370927175,
                                        'virtual_nw_y_pixel': 1743157086,
                                        'virtual_width': -809900218,
                                        'virtual_height': -976296180,
                                    },
                            {
                                        'source_monitor': -170868,
                                        'source_nw_x_pixel': -3829359319103267285,
                                        'source_nw_y_pixel': -2735983990753060120,
                                        'source_pixel_width': -8775512267224120766,
                                        'source_pixel_height': -710042636943604608,
                                        'rotation': -6483062135950118543,
                                        'virtual_nw_x_pixel': 945808028,
                                        'virtual_nw_y_pixel': -1996101504,
                                        'virtual_width': -250617269,
                                        'virtual_height': 1582747997,
                                    },
                            {
                                        'source_monitor': 7459576,
                                        'source_nw_x_pixel': -8305130634043103682,
                                        'source_nw_y_pixel': -3442749471226225167,
                                        'source_pixel_width': -5415017318467452145,
                                        'source_pixel_height': -8610716216863270010,
                                        'rotation': -1715274852390678588,
                                        'virtual_nw_x_pixel': -1602053137,
                                        'virtual_nw_y_pixel': -1545456324,
                                        'virtual_width': 1591605741,
                                        'virtual_height': 1324934804,
                                    },
                        ],
                },
                {
                    'description': '\xa0_ýΩϮȍΙǩʵ·МӢĉҬåĠ˘˭ј˚ρ@ȮΩǀĎʆxрд',
                    'monitors': [
                            {
                                        'identifier': 8024174,
                                        'width': 6361556393939106758,
                                        'height': -1170457378614888642,
                                    },
                            {
                                        'identifier': 800442,
                                        'width': 4217603197865605473,
                                        'height': -7585370224503655900,
                                    },
                            {
                                        'identifier': 2298246,
                                        'width': -6933895361941050415,
                                        'height': 6285056643411985314,
                                    },
                            {
                                        'identifier': -867078,
                                        'width': 4526234297517505438,
                                        'height': 6957134175826184800,
                                    },
                            {
                                        'identifier': 9541183,
                                        'width': 4352380874179022136,
                                        'height': 6614838843384118311,
                                    },
                            {
                                        'identifier': 6691196,
                                        'width': 3101504382713001862,
                                        'height': -7000867095645182063,
                                    },
                            {
                                        'identifier': 7592807,
                                        'width': 2529414702535435328,
                                        'height': 5194268885624779040,
                                    },
                            {
                                        'identifier': 4199161,
                                        'width': 4743409624046992624,
                                        'height': 5083319706974560762,
                                    },
                            {
                                        'identifier': -705965,
                                        'width': 2633607387697594977,
                                        'height': -5061404852316883980,
                                    },
                            {
                                        'identifier': 9405469,
                                        'width': 337670114357059718,
                                        'height': -3051803082694930776,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': -962049,
                                        'source_nw_x_pixel': -1128991212484504854,
                                        'source_nw_y_pixel': -5290485839064287063,
                                        'source_pixel_width': -4736044211338924965,
                                        'source_pixel_height': -8690303428675758042,
                                        'rotation': -3182609426544085492,
                                        'virtual_nw_x_pixel': 676251992,
                                        'virtual_nw_y_pixel': -1135645256,
                                        'virtual_width': 375575959,
                                        'virtual_height': -1365344246,
                                    },
                            {
                                        'source_monitor': -577950,
                                        'source_nw_x_pixel': -4853278302083539057,
                                        'source_nw_y_pixel': -3569490904324551315,
                                        'source_pixel_width': -2532679205736495339,
                                        'source_pixel_height': -8183627621114321406,
                                        'rotation': -2573244628805047203,
                                        'virtual_nw_x_pixel': 1031583187,
                                        'virtual_nw_y_pixel': 385617557,
                                        'virtual_width': 1099731315,
                                        'virtual_height': -1252818930,
                                    },
                            {
                                        'source_monitor': -664704,
                                        'source_nw_x_pixel': -8109212833424183286,
                                        'source_nw_y_pixel': -1355676527196693332,
                                        'source_pixel_width': -1206572674736271016,
                                        'source_pixel_height': -8210064365095604111,
                                        'rotation': -3177789661353783402,
                                        'virtual_nw_x_pixel': 912499827,
                                        'virtual_nw_y_pixel': -1227722363,
                                        'virtual_width': 28168985,
                                        'virtual_height': -989623082,
                                    },
                            {
                                        'source_monitor': 5354854,
                                        'source_nw_x_pixel': -8663587213112271327,
                                        'source_nw_y_pixel': -3235404872934746311,
                                        'source_pixel_width': -5880249016047771243,
                                        'source_pixel_height': -911502858514276468,
                                        'rotation': -1415242501807693184,
                                        'virtual_nw_x_pixel': 100233713,
                                        'virtual_nw_y_pixel': -1968333966,
                                        'virtual_width': 165179290,
                                        'virtual_height': 1614751558,
                                    },
                            {
                                        'source_monitor': 2047237,
                                        'source_nw_x_pixel': -8214078103278553480,
                                        'source_nw_y_pixel': -319528115617890728,
                                        'source_pixel_width': -9071402984524146312,
                                        'source_pixel_height': -2154543781982119928,
                                        'rotation': -5562017986609421821,
                                        'virtual_nw_x_pixel': -95022833,
                                        'virtual_nw_y_pixel': -1653109599,
                                        'virtual_width': 813554440,
                                        'virtual_height': -321776875,
                                    },
                            {
                                        'source_monitor': 2478742,
                                        'source_nw_x_pixel': -2525808725926372293,
                                        'source_nw_y_pixel': -8820514170734191529,
                                        'source_pixel_width': -5015440886572171195,
                                        'source_pixel_height': -8205286035570624751,
                                        'rotation': -164075461132633857,
                                        'virtual_nw_x_pixel': -854966663,
                                        'virtual_nw_y_pixel': 425350661,
                                        'virtual_width': 718824658,
                                        'virtual_height': 464041552,
                                    },
                            {
                                        'source_monitor': 5303206,
                                        'source_nw_x_pixel': -8105982128792122584,
                                        'source_nw_y_pixel': -3327515836961388538,
                                        'source_pixel_width': -9162135914245844560,
                                        'source_pixel_height': -929783741380165902,
                                        'rotation': -953131698844029627,
                                        'virtual_nw_x_pixel': 1761756978,
                                        'virtual_nw_y_pixel': 1680989988,
                                        'virtual_width': 522733679,
                                        'virtual_height': 564568017,
                                    },
                            {
                                        'source_monitor': 6955222,
                                        'source_nw_x_pixel': -2730200407245037088,
                                        'source_nw_y_pixel': -6353677391280714784,
                                        'source_pixel_width': -584714985009792602,
                                        'source_pixel_height': -4584322419203624645,
                                        'rotation': -2639579940190019187,
                                        'virtual_nw_x_pixel': -64279512,
                                        'virtual_nw_y_pixel': -1458251641,
                                        'virtual_width': -383728414,
                                        'virtual_height': 786599027,
                                    },
                            {
                                        'source_monitor': 4050749,
                                        'source_nw_x_pixel': -6454935442489447866,
                                        'source_nw_y_pixel': -923135995918570085,
                                        'source_pixel_width': -8254529505383513931,
                                        'source_pixel_height': -5276578525992185853,
                                        'rotation': -9145431288852656547,
                                        'virtual_nw_x_pixel': -193950841,
                                        'virtual_nw_y_pixel': 1540965892,
                                        'virtual_width': 117944053,
                                        'virtual_height': 30292812,
                                    },
                            {
                                        'source_monitor': 990493,
                                        'source_nw_x_pixel': -7645978078058530593,
                                        'source_nw_y_pixel': -1311892287897930779,
                                        'source_pixel_width': -2100042477036399830,
                                        'source_pixel_height': -8225788033582669909,
                                        'rotation': -368545294878735509,
                                        'virtual_nw_x_pixel': -1694381566,
                                        'virtual_nw_y_pixel': 1856985804,
                                        'virtual_width': -573793454,
                                        'virtual_height': 828130649,
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
                                        'identifier': 5715009,
                                        'width': -5777554657519349104,
                                        'height': 5529288779029312098,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -6493892030182776324,
                                        'source_nw_y_pixel': -6618616385661563320,
                                        'source_pixel_width': -5662211848442905017,
                                        'source_pixel_height': -3318706687078382231,
                                        'rotation': -5001720156218568290,
                                        'virtual_nw_x_pixel': 1214061001,
                                        'virtual_nw_y_pixel': -1280524452,
                                        'virtual_width': -15255833,
                                        'virtual_height': 386799693,
                                    },
                        ],
                },
            ],

        },
    ),
]
