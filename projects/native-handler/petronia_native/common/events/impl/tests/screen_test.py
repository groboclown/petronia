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
            'identifier': 6349780,
            'width': 5340058489510335492,
            'height': 1428530330224062428,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 738010,

            'width': -5241832595910527654,

            'height': -3323438057759120167,

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
            'source_monitor': 9017641,
            'source_nw_x_pixel': -6439286002375969643,
            'source_nw_y_pixel': -3137260858084600704,
            'source_pixel_width': -7641661216109599241,
            'source_pixel_height': -5760605454922750353,
            'rotation': -5338516451831230071,
            'virtual_nw_x_pixel': 14446276,
            'virtual_nw_y_pixel': 1356487727,
            'virtual_width': 1998466018,
            'virtual_height': -1290584723,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'source_nw_x_pixel': -303365169244662350,

            'source_nw_y_pixel': -3426754220154068600,

            'source_pixel_width': -2483165770653855613,

            'source_pixel_height': -6939456465844619817,

            'rotation': -5615802888451927640,

            'virtual_nw_x_pixel': -1556554402,

            'virtual_nw_y_pixel': -377286819,

            'virtual_width': 1974105701,

            'virtual_height': 1244792406,

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
            'description': 'ɥС\x92ƫƒԥніӓҰӾѥѷėаŕЫʒYΟɏ\u0380Ɩѵ¼ӁԊϺͷȷ',
            'monitors': [
                {
                    'identifier': 7498762,
                    'width': -5765016715337570480,
                    'height': 473517605022175937,
                },
                {
                    'identifier': -875564,
                    'width': 380810439937516317,
                    'height': 3705932168145268071,
                },
                {
                    'identifier': 2217290,
                    'width': 3934356759988526236,
                    'height': -1661222535614847188,
                },
                {
                    'identifier': 79696,
                    'width': -1505289598349337299,
                    'height': -3964123939611885638,
                },
                {
                    'identifier': 2477593,
                    'width': -5838164048719554519,
                    'height': 1369522911896841513,
                },
                {
                    'identifier': 8771160,
                    'width': 888845156863835049,
                    'height': 8641932848086692007,
                },
                {
                    'identifier': 7789062,
                    'width': 7684135417749908246,
                    'height': 8710479954287647733,
                },
                {
                    'identifier': 9373992,
                    'width': -7774949695168808029,
                    'height': 4500506439483562731,
                },
                {
                    'identifier': 7666332,
                    'width': -8598617907682515505,
                    'height': -4574236723051953959,
                },
                {
                    'identifier': 4099100,
                    'width': 1878525540116120198,
                    'height': -3747044885262201444,
                },
            ],
            'screen': [
                {
                    'source_monitor': 7461730,
                    'source_nw_x_pixel': -7254766749752681235,
                    'source_nw_y_pixel': -3160006669850294461,
                    'source_pixel_width': -5252770466297812711,
                    'source_pixel_height': -1772064031265394534,
                    'rotation': -4005403124602081033,
                    'virtual_nw_x_pixel': 1956926014,
                    'virtual_nw_y_pixel': -1072119341,
                    'virtual_width': -1021232571,
                    'virtual_height': 1229066712,
                },
                {
                    'source_monitor': 2254874,
                    'source_nw_x_pixel': -7158942403082831537,
                    'source_nw_y_pixel': -449465143244161178,
                    'source_pixel_width': -8529337183392852011,
                    'source_pixel_height': -590958553673568180,
                    'rotation': -2566973072551298516,
                    'virtual_nw_x_pixel': -1032067794,
                    'virtual_nw_y_pixel': 1963686566,
                    'virtual_width': -409405827,
                    'virtual_height': 1352510162,
                },
                {
                    'source_monitor': 6545946,
                    'source_nw_x_pixel': -7291217943187189303,
                    'source_nw_y_pixel': -2488127940486058510,
                    'source_pixel_width': -1731269433482056996,
                    'source_pixel_height': -4572115573843838491,
                    'rotation': -6784220630342937590,
                    'virtual_nw_x_pixel': 827565714,
                    'virtual_nw_y_pixel': -1620640919,
                    'virtual_width': 1581475769,
                    'virtual_height': -740078064,
                },
                {
                    'source_monitor': -274888,
                    'source_nw_x_pixel': -7380665361520172424,
                    'source_nw_y_pixel': -6627745172226347584,
                    'source_pixel_width': -3384765001500595529,
                    'source_pixel_height': -7780459273442354909,
                    'rotation': -1064299567636551747,
                    'virtual_nw_x_pixel': -1310525616,
                    'virtual_nw_y_pixel': -1817795444,
                    'virtual_width': -838344430,
                    'virtual_height': 1803302013,
                },
                {
                    'source_monitor': 8117651,
                    'source_nw_x_pixel': -7455459351650638382,
                    'source_nw_y_pixel': -2843701278724544486,
                    'source_pixel_width': -2974217656145515684,
                    'source_pixel_height': -141360476823758540,
                    'rotation': -2228462456542034297,
                    'virtual_nw_x_pixel': -242134991,
                    'virtual_nw_y_pixel': -301569817,
                    'virtual_width': 5011703,
                    'virtual_height': -1873413620,
                },
                {
                    'source_monitor': 746789,
                    'source_nw_x_pixel': -7784388508372552610,
                    'source_nw_y_pixel': -131711996044153016,
                    'source_pixel_width': -4063764978118475091,
                    'source_pixel_height': -2462162859364293299,
                    'rotation': -918976362704889755,
                    'virtual_nw_x_pixel': -154166919,
                    'virtual_nw_y_pixel': -136960622,
                    'virtual_width': -1634542410,
                    'virtual_height': 1071686534,
                },
                {
                    'source_monitor': 1302424,
                    'source_nw_x_pixel': -9001178398010455457,
                    'source_nw_y_pixel': -3378543083691982031,
                    'source_pixel_width': -9175815166822994427,
                    'source_pixel_height': -6818557433953469075,
                    'rotation': -2615088944531408813,
                    'virtual_nw_x_pixel': -626547293,
                    'virtual_nw_y_pixel': -1501064654,
                    'virtual_width': 752804372,
                    'virtual_height': 1986700735,
                },
                {
                    'source_monitor': 1730903,
                    'source_nw_x_pixel': -8097225458133661410,
                    'source_nw_y_pixel': -12588776306521910,
                    'source_pixel_width': -1333142163082411139,
                    'source_pixel_height': -1340990142841086061,
                    'rotation': -9149311735626847661,
                    'virtual_nw_x_pixel': 394613209,
                    'virtual_nw_y_pixel': 119635939,
                    'virtual_width': -1466878313,
                    'virtual_height': -850958948,
                },
                {
                    'source_monitor': -883234,
                    'source_nw_x_pixel': -5193918151597539294,
                    'source_nw_y_pixel': -5048358335314461062,
                    'source_pixel_width': -8114724545665469729,
                    'source_pixel_height': -3314835431358200505,
                    'rotation': -5298664273229868516,
                    'virtual_nw_x_pixel': 1854164371,
                    'virtual_nw_y_pixel': -1452252804,
                    'virtual_width': -215198131,
                    'virtual_height': 217142914,
                },
                {
                    'source_monitor': -256100,
                    'source_nw_x_pixel': -5511415601772479381,
                    'source_nw_y_pixel': -6211830304277544847,
                    'source_pixel_width': -144026072641750890,
                    'source_pixel_height': -4297939387331759253,
                    'rotation': -4183388434864512752,
                    'virtual_nw_x_pixel': 1517317962,
                    'virtual_nw_y_pixel': -597513137,
                    'virtual_width': 1316445806,
                    'virtual_height': -469464984,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
                {
                    'identifier': 1207136,
                    'width': 7862595858056230714,
                    'height': -3316553081482798565,
                },
            ],

            'screen': [
                {
                    'source_nw_x_pixel': -7163698806251200935,
                    'source_nw_y_pixel': -1215051189074591054,
                    'source_pixel_width': -2932683644412607341,
                    'source_pixel_height': -2520621402321173557,
                    'rotation': -1828524444519863164,
                    'virtual_nw_x_pixel': 57998559,
                    'virtual_nw_y_pixel': -897772515,
                    'virtual_width': -395335131,
                    'virtual_height': 123789676,
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
            'request_id': -228260,
            'mapped_screens_by_monitors': [
                {
                    'description': '˾Ȉ\x80ʡԂ\\˭ňĘҘѐӧò˚ЊƨȌЃ\x9cʗēϮôҡѠĒĈ˻à$',
                    'monitors': [
                            {
                                        'identifier': 6196742,
                                        'width': -2847347805163347344,
                                        'height': -2768572029463491599,
                                    },
                            {
                                        'identifier': 9452271,
                                        'width': 7812175584712981197,
                                        'height': -225435839496814034,
                                    },
                            {
                                        'identifier': 4649709,
                                        'width': 3258681252327859062,
                                        'height': -4441656379214113545,
                                    },
                            {
                                        'identifier': 3580297,
                                        'width': -8987223835471390466,
                                        'height': 4895310201172587593,
                                    },
                            {
                                        'identifier': 9158880,
                                        'width': 8574922697190003973,
                                        'height': 6101580004159210832,
                                    },
                            {
                                        'identifier': 3596914,
                                        'width': -6990812435652890530,
                                        'height': -7444037563941398576,
                                    },
                            {
                                        'identifier': 8500601,
                                        'width': -299912149127451318,
                                        'height': -8170965495056331720,
                                    },
                            {
                                        'identifier': 9013754,
                                        'width': -7471900282961638287,
                                        'height': 104938291922409800,
                                    },
                            {
                                        'identifier': 6137061,
                                        'width': -7669201319928113367,
                                        'height': -2870888570358255955,
                                    },
                            {
                                        'identifier': 6741242,
                                        'width': 3590906248516588610,
                                        'height': 3536231469802607755,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2847294,
                                        'source_nw_x_pixel': -1510907430972296422,
                                        'source_nw_y_pixel': -7777283482075518320,
                                        'source_pixel_width': -4977016562828050574,
                                        'source_pixel_height': -4287119609524025009,
                                        'rotation': -5572559851020873625,
                                        'virtual_nw_x_pixel': -131389108,
                                        'virtual_nw_y_pixel': 1217231677,
                                        'virtual_width': 1427510354,
                                        'virtual_height': -1841467122,
                                    },
                            {
                                        'source_monitor': 4213320,
                                        'source_nw_x_pixel': -259029258336523654,
                                        'source_nw_y_pixel': -1785353500202471196,
                                        'source_pixel_width': -1730679041076420248,
                                        'source_pixel_height': -1205854899621183014,
                                        'rotation': -436469036687822233,
                                        'virtual_nw_x_pixel': -576559460,
                                        'virtual_nw_y_pixel': 570200841,
                                        'virtual_width': -1887975256,
                                        'virtual_height': 995415821,
                                    },
                            {
                                        'source_monitor': 1550126,
                                        'source_nw_x_pixel': -5016458384078549649,
                                        'source_nw_y_pixel': -662207401848557141,
                                        'source_pixel_width': -8953451440175342674,
                                        'source_pixel_height': -6607142592446338442,
                                        'rotation': -4439347554023281889,
                                        'virtual_nw_x_pixel': -765082290,
                                        'virtual_nw_y_pixel': 1808018575,
                                        'virtual_width': 124651714,
                                        'virtual_height': 1724204886,
                                    },
                            {
                                        'source_monitor': 7295503,
                                        'source_nw_x_pixel': -4048943514629613426,
                                        'source_nw_y_pixel': -7759127799636312435,
                                        'source_pixel_width': -7399480641458990308,
                                        'source_pixel_height': -7342150786351519547,
                                        'rotation': -2167568675583867484,
                                        'virtual_nw_x_pixel': 1480539259,
                                        'virtual_nw_y_pixel': 1777081363,
                                        'virtual_width': -1319542678,
                                        'virtual_height': -722322434,
                                    },
                            {
                                        'source_monitor': 7388055,
                                        'source_nw_x_pixel': -8404996920607242339,
                                        'source_nw_y_pixel': -3441066818905909767,
                                        'source_pixel_width': -6201205656243199537,
                                        'source_pixel_height': -5990955689109375789,
                                        'rotation': -367019159195471618,
                                        'virtual_nw_x_pixel': 483937171,
                                        'virtual_nw_y_pixel': -1872806716,
                                        'virtual_width': -359492020,
                                        'virtual_height': -311844681,
                                    },
                            {
                                        'source_monitor': 1566290,
                                        'source_nw_x_pixel': -7801165811226909434,
                                        'source_nw_y_pixel': -4756168382732957157,
                                        'source_pixel_width': -681904307650590368,
                                        'source_pixel_height': -919155744076431812,
                                        'rotation': -1552379591029741942,
                                        'virtual_nw_x_pixel': 677589349,
                                        'virtual_nw_y_pixel': -1081284941,
                                        'virtual_width': -1432963425,
                                        'virtual_height': 1829296745,
                                    },
                            {
                                        'source_monitor': 9101342,
                                        'source_nw_x_pixel': -7034545272026891292,
                                        'source_nw_y_pixel': -5454169606421724761,
                                        'source_pixel_width': -344506172817086140,
                                        'source_pixel_height': -9182016066581630438,
                                        'rotation': -3213065387556567955,
                                        'virtual_nw_x_pixel': 1611243669,
                                        'virtual_nw_y_pixel': -1923024409,
                                        'virtual_width': -779032256,
                                        'virtual_height': 1440307971,
                                    },
                            {
                                        'source_monitor': 4309712,
                                        'source_nw_x_pixel': -8047894446594066000,
                                        'source_nw_y_pixel': -4467473998847531922,
                                        'source_pixel_width': -3484290057752208365,
                                        'source_pixel_height': -4839080937292843687,
                                        'rotation': -3315509265549185440,
                                        'virtual_nw_x_pixel': 1002507854,
                                        'virtual_nw_y_pixel': 1440310628,
                                        'virtual_width': 986085203,
                                        'virtual_height': 1918405378,
                                    },
                            {
                                        'source_monitor': 7790588,
                                        'source_nw_x_pixel': -2311218904082260870,
                                        'source_nw_y_pixel': -6497374809868390800,
                                        'source_pixel_width': -246116404628276781,
                                        'source_pixel_height': -2947773262735195192,
                                        'rotation': -1204516921098359956,
                                        'virtual_nw_x_pixel': -722227476,
                                        'virtual_nw_y_pixel': 237645576,
                                        'virtual_width': 384547355,
                                        'virtual_height': -1580928516,
                                    },
                            {
                                        'source_monitor': 4941447,
                                        'source_nw_x_pixel': -2831752754832823117,
                                        'source_nw_y_pixel': -2257208118591978360,
                                        'source_pixel_width': -7157337717942530797,
                                        'source_pixel_height': -2279323398383434654,
                                        'rotation': -4399854293782091255,
                                        'virtual_nw_x_pixel': 820454815,
                                        'virtual_nw_y_pixel': -162825632,
                                        'virtual_width': 1243424599,
                                        'virtual_height': -994655630,
                                    },
                        ],
                },
                {
                    'description': 'ԡϊʒȧƦΈғΒȾѷzƠʟùîɄθѱԅŅÛNǌ˼=ίʶ\u0379Ĩϗ',
                    'monitors': [
                            {
                                        'identifier': 4221296,
                                        'width': -2262147065084235895,
                                        'height': -1103669773543354724,
                                    },
                            {
                                        'identifier': 3504062,
                                        'width': -3848670823330739068,
                                        'height': 5618805032537442844,
                                    },
                            {
                                        'identifier': 7809301,
                                        'width': -1861595943075874871,
                                        'height': 2587457252327567716,
                                    },
                            {
                                        'identifier': 4692878,
                                        'width': -1403284518798596910,
                                        'height': 3787147307306947928,
                                    },
                            {
                                        'identifier': 1519581,
                                        'width': 7771275793135272768,
                                        'height': 8500448109681588578,
                                    },
                            {
                                        'identifier': 3733976,
                                        'width': 4477881922174515059,
                                        'height': 3290063758002042379,
                                    },
                            {
                                        'identifier': 4274198,
                                        'width': 4824544809845760660,
                                        'height': 5069456944634623337,
                                    },
                            {
                                        'identifier': 5192010,
                                        'width': -5709527453269927273,
                                        'height': -654718861502557398,
                                    },
                            {
                                        'identifier': 3949396,
                                        'width': -5041715997844438266,
                                        'height': 4744972962165107805,
                                    },
                            {
                                        'identifier': 4526004,
                                        'width': 8041322581876816507,
                                        'height': -8842188620516673356,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4322147,
                                        'source_nw_x_pixel': -5038358244533563025,
                                        'source_nw_y_pixel': -4058362497244608683,
                                        'source_pixel_width': -3834952378366253409,
                                        'source_pixel_height': -7188396925565024574,
                                        'rotation': -6051166062647074284,
                                        'virtual_nw_x_pixel': 282620192,
                                        'virtual_nw_y_pixel': 1714803225,
                                        'virtual_width': 1984909827,
                                        'virtual_height': -1746481407,
                                    },
                            {
                                        'source_monitor': 583087,
                                        'source_nw_x_pixel': -6587487617309641492,
                                        'source_nw_y_pixel': -1220923433640843218,
                                        'source_pixel_width': -3524432980548065661,
                                        'source_pixel_height': -1165597253517577318,
                                        'rotation': -6964996957837280873,
                                        'virtual_nw_x_pixel': 543323643,
                                        'virtual_nw_y_pixel': 215406227,
                                        'virtual_width': -391619617,
                                        'virtual_height': 583553398,
                                    },
                            {
                                        'source_monitor': 7140013,
                                        'source_nw_x_pixel': -8841386760597534382,
                                        'source_nw_y_pixel': -7988704663523183419,
                                        'source_pixel_width': -6397438754315650926,
                                        'source_pixel_height': -2972010224423984207,
                                        'rotation': -2593928437725224893,
                                        'virtual_nw_x_pixel': -62608065,
                                        'virtual_nw_y_pixel': -1378709734,
                                        'virtual_width': 1815760903,
                                        'virtual_height': 1060419739,
                                    },
                            {
                                        'source_monitor': 1381742,
                                        'source_nw_x_pixel': -4892102016765043844,
                                        'source_nw_y_pixel': -3312919964559845638,
                                        'source_pixel_width': -7923246161126623133,
                                        'source_pixel_height': -7143452488307269896,
                                        'rotation': -6706889769668619537,
                                        'virtual_nw_x_pixel': -1700374318,
                                        'virtual_nw_y_pixel': -1496025849,
                                        'virtual_width': 895794652,
                                        'virtual_height': 1160307807,
                                    },
                            {
                                        'source_monitor': 7111818,
                                        'source_nw_x_pixel': -1718746169723736293,
                                        'source_nw_y_pixel': -1789728166735340574,
                                        'source_pixel_width': -6982072176112574265,
                                        'source_pixel_height': -2619062816838068583,
                                        'rotation': -1287594116137345962,
                                        'virtual_nw_x_pixel': -446378919,
                                        'virtual_nw_y_pixel': -22901403,
                                        'virtual_width': -921203670,
                                        'virtual_height': 741213136,
                                    },
                            {
                                        'source_monitor': -179015,
                                        'source_nw_x_pixel': -5436993202007213581,
                                        'source_nw_y_pixel': -855683434942617068,
                                        'source_pixel_width': -8373208062367841134,
                                        'source_pixel_height': -8677887196276987937,
                                        'rotation': -1116658489333847517,
                                        'virtual_nw_x_pixel': -492549658,
                                        'virtual_nw_y_pixel': -1707135194,
                                        'virtual_width': -116684473,
                                        'virtual_height': 706489955,
                                    },
                            {
                                        'source_monitor': 101201,
                                        'source_nw_x_pixel': -7557319759895434729,
                                        'source_nw_y_pixel': -8728811582383168505,
                                        'source_pixel_width': -1212383171165436506,
                                        'source_pixel_height': -8675717244576519060,
                                        'rotation': -4021865171268641465,
                                        'virtual_nw_x_pixel': 1236694721,
                                        'virtual_nw_y_pixel': -127404783,
                                        'virtual_width': -783661264,
                                        'virtual_height': 1512541197,
                                    },
                            {
                                        'source_monitor': 9322279,
                                        'source_nw_x_pixel': -3407947439962230045,
                                        'source_nw_y_pixel': -3977621399315948693,
                                        'source_pixel_width': -5414399423184036830,
                                        'source_pixel_height': -4084779695889104989,
                                        'rotation': -4871549543404256311,
                                        'virtual_nw_x_pixel': -1619811764,
                                        'virtual_nw_y_pixel': -376944162,
                                        'virtual_width': 565038672,
                                        'virtual_height': -1276077931,
                                    },
                            {
                                        'source_monitor': 3377644,
                                        'source_nw_x_pixel': -1891708815506538250,
                                        'source_nw_y_pixel': -6735068499497017578,
                                        'source_pixel_width': -1651640534513769101,
                                        'source_pixel_height': -5565611961290611245,
                                        'rotation': -89035087462520181,
                                        'virtual_nw_x_pixel': -731695860,
                                        'virtual_nw_y_pixel': -1692398506,
                                        'virtual_width': -77467586,
                                        'virtual_height': 1034055899,
                                    },
                            {
                                        'source_monitor': -295713,
                                        'source_nw_x_pixel': -3554601263480589251,
                                        'source_nw_y_pixel': -9221762205631710510,
                                        'source_pixel_width': -6056273182191877531,
                                        'source_pixel_height': -8409923756967354689,
                                        'rotation': -2394413564872458656,
                                        'virtual_nw_x_pixel': 1589167806,
                                        'virtual_nw_y_pixel': -1800307050,
                                        'virtual_width': -596323585,
                                        'virtual_height': 350794940,
                                    },
                        ],
                },
                {
                    'description': 'ЬԣΜȩϝˡϡЃѲÓ\x95ɻǣҾ˞űĿŹȇϽˌȠʉºӂдӇŵȡǠ',
                    'monitors': [
                            {
                                        'identifier': -467176,
                                        'width': -6582559884573621909,
                                        'height': -3952853859071100692,
                                    },
                            {
                                        'identifier': 9461259,
                                        'width': 3730770087706272546,
                                        'height': 5270202997163911935,
                                    },
                            {
                                        'identifier': 5162372,
                                        'width': -1801866635073578950,
                                        'height': 5813414214109587480,
                                    },
                            {
                                        'identifier': -595319,
                                        'width': -1515547621716110341,
                                        'height': -3143394301294653025,
                                    },
                            {
                                        'identifier': 1695191,
                                        'width': -917430941166012988,
                                        'height': 2223112544671414989,
                                    },
                            {
                                        'identifier': -673286,
                                        'width': -6657836535099587996,
                                        'height': 1883604745743135643,
                                    },
                            {
                                        'identifier': 9114554,
                                        'width': 2701291634605924902,
                                        'height': -3492878882478878284,
                                    },
                            {
                                        'identifier': 9289713,
                                        'width': 3072345637214072728,
                                        'height': 1044693049693977858,
                                    },
                            {
                                        'identifier': 2821036,
                                        'width': -1291630952548784411,
                                        'height': 7035889853107773371,
                                    },
                            {
                                        'identifier': 296567,
                                        'width': -1485724317975873320,
                                        'height': 5224561058497972334,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8493407,
                                        'source_nw_x_pixel': -463754637023845450,
                                        'source_nw_y_pixel': -5228716026947641023,
                                        'source_pixel_width': -7641626959258577663,
                                        'source_pixel_height': -8301086759460938016,
                                        'rotation': -46459240510912723,
                                        'virtual_nw_x_pixel': 1048863085,
                                        'virtual_nw_y_pixel': 826387447,
                                        'virtual_width': -1171570969,
                                        'virtual_height': 1854827204,
                                    },
                            {
                                        'source_monitor': 1518019,
                                        'source_nw_x_pixel': -3306966637993244763,
                                        'source_nw_y_pixel': -1935751192382517624,
                                        'source_pixel_width': -3015051343617602531,
                                        'source_pixel_height': -3185978340580181799,
                                        'rotation': -6354302437627403415,
                                        'virtual_nw_x_pixel': 1892577404,
                                        'virtual_nw_y_pixel': -911989613,
                                        'virtual_width': -1540197030,
                                        'virtual_height': 1722134623,
                                    },
                            {
                                        'source_monitor': 8071864,
                                        'source_nw_x_pixel': -3823091149463460701,
                                        'source_nw_y_pixel': -4747542491276238740,
                                        'source_pixel_width': -3151110134595535630,
                                        'source_pixel_height': -6406020785835876661,
                                        'rotation': -3743874499942468282,
                                        'virtual_nw_x_pixel': -594433878,
                                        'virtual_nw_y_pixel': -611579833,
                                        'virtual_width': 1867371163,
                                        'virtual_height': 1770540937,
                                    },
                            {
                                        'source_monitor': -594713,
                                        'source_nw_x_pixel': -6979441357952508309,
                                        'source_nw_y_pixel': -6461098791713309274,
                                        'source_pixel_width': -2056480027869673170,
                                        'source_pixel_height': -1371599956992823613,
                                        'rotation': -6679616701486729587,
                                        'virtual_nw_x_pixel': 643842738,
                                        'virtual_nw_y_pixel': -201573213,
                                        'virtual_width': -192156014,
                                        'virtual_height': 1647097553,
                                    },
                            {
                                        'source_monitor': 716497,
                                        'source_nw_x_pixel': -2909195524985005046,
                                        'source_nw_y_pixel': -6244601474721496988,
                                        'source_pixel_width': -1498445705110810306,
                                        'source_pixel_height': -7675976632949084872,
                                        'rotation': -8574893243286302176,
                                        'virtual_nw_x_pixel': -884083809,
                                        'virtual_nw_y_pixel': 1187592593,
                                        'virtual_width': -1030745761,
                                        'virtual_height': 1651091484,
                                    },
                            {
                                        'source_monitor': -999216,
                                        'source_nw_x_pixel': -5998054998099567048,
                                        'source_nw_y_pixel': -2154262229595424188,
                                        'source_pixel_width': -5410468622245073780,
                                        'source_pixel_height': -770155130737612276,
                                        'rotation': -5848629081200745431,
                                        'virtual_nw_x_pixel': -655209422,
                                        'virtual_nw_y_pixel': -1181877050,
                                        'virtual_width': 23176446,
                                        'virtual_height': -1717327854,
                                    },
                            {
                                        'source_monitor': 7161053,
                                        'source_nw_x_pixel': -7409559226078826647,
                                        'source_nw_y_pixel': -1609865539953300266,
                                        'source_pixel_width': -7086398352268514222,
                                        'source_pixel_height': -337910588746182167,
                                        'rotation': -8274089167198463244,
                                        'virtual_nw_x_pixel': -1104088968,
                                        'virtual_nw_y_pixel': 802543733,
                                        'virtual_width': 828690537,
                                        'virtual_height': -848571791,
                                    },
                            {
                                        'source_monitor': 931187,
                                        'source_nw_x_pixel': -4138652010223998729,
                                        'source_nw_y_pixel': -5354368929544537206,
                                        'source_pixel_width': -4002103190425238699,
                                        'source_pixel_height': -7295388987722118442,
                                        'rotation': -7551444204084237167,
                                        'virtual_nw_x_pixel': 1624675268,
                                        'virtual_nw_y_pixel': -1844184884,
                                        'virtual_width': -226587058,
                                        'virtual_height': 241414592,
                                    },
                            {
                                        'source_monitor': 483796,
                                        'source_nw_x_pixel': -3384790171275834214,
                                        'source_nw_y_pixel': -2083185778198703872,
                                        'source_pixel_width': -7756060056224392760,
                                        'source_pixel_height': -3096417911563610015,
                                        'rotation': -8413307399603432594,
                                        'virtual_nw_x_pixel': 1074751467,
                                        'virtual_nw_y_pixel': -206733479,
                                        'virtual_width': 186388584,
                                        'virtual_height': -1205583925,
                                    },
                            {
                                        'source_monitor': 4647761,
                                        'source_nw_x_pixel': -8602157226827575227,
                                        'source_nw_y_pixel': -1013286501050957494,
                                        'source_pixel_width': -456994530253225878,
                                        'source_pixel_height': -5504805342495204537,
                                        'rotation': -2736920711702013658,
                                        'virtual_nw_x_pixel': -956928395,
                                        'virtual_nw_y_pixel': 1188265331,
                                        'virtual_width': 569181550,
                                        'virtual_height': -1345111817,
                                    },
                        ],
                },
                {
                    'description': 'ǥϩΒɴ;ǆĴĈц\u0382şȗѳңǱҳӏçŷĘΪʶðĄìҡóӌϹØ',
                    'monitors': [
                            {
                                        'identifier': 3798999,
                                        'width': 717859518128387081,
                                        'height': 2072392968593581082,
                                    },
                            {
                                        'identifier': 2681075,
                                        'width': -7125717986292422506,
                                        'height': -5333038877082792889,
                                    },
                            {
                                        'identifier': 103157,
                                        'width': 4415448313211832539,
                                        'height': 3566778388077125586,
                                    },
                            {
                                        'identifier': 9592862,
                                        'width': 5797473425735693749,
                                        'height': 59768859918856508,
                                    },
                            {
                                        'identifier': 5863130,
                                        'width': -7197081178034189076,
                                        'height': 3038835814040507243,
                                    },
                            {
                                        'identifier': 7705968,
                                        'width': -30397089473661798,
                                        'height': -1623059593880204453,
                                    },
                            {
                                        'identifier': -738415,
                                        'width': 7246443051569801971,
                                        'height': 5614197687911814518,
                                    },
                            {
                                        'identifier': 5480986,
                                        'width': -1618637446484408570,
                                        'height': 9187995888609795843,
                                    },
                            {
                                        'identifier': 9639483,
                                        'width': 6618776336020380139,
                                        'height': 6074542706479914651,
                                    },
                            {
                                        'identifier': 6613247,
                                        'width': -8163629715008069253,
                                        'height': 1445121376465348811,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8256598,
                                        'source_nw_x_pixel': -1411618876009112255,
                                        'source_nw_y_pixel': -2387821441125053709,
                                        'source_pixel_width': -6054867120935383775,
                                        'source_pixel_height': -1164023079902847204,
                                        'rotation': -3425511712010501538,
                                        'virtual_nw_x_pixel': 1337697465,
                                        'virtual_nw_y_pixel': -791394233,
                                        'virtual_width': 573609316,
                                        'virtual_height': -1016682532,
                                    },
                            {
                                        'source_monitor': 313015,
                                        'source_nw_x_pixel': -833992040353044535,
                                        'source_nw_y_pixel': -744001757953485350,
                                        'source_pixel_width': -6023495702978460101,
                                        'source_pixel_height': -2019793891759098419,
                                        'rotation': -2979094300574380380,
                                        'virtual_nw_x_pixel': -979228940,
                                        'virtual_nw_y_pixel': -1619478252,
                                        'virtual_width': 243044352,
                                        'virtual_height': -1821598211,
                                    },
                            {
                                        'source_monitor': 6107605,
                                        'source_nw_x_pixel': -3179276154332745720,
                                        'source_nw_y_pixel': -1717831732872142176,
                                        'source_pixel_width': -6661718990294787771,
                                        'source_pixel_height': -19985000365798690,
                                        'rotation': -7258343959871157139,
                                        'virtual_nw_x_pixel': -646139532,
                                        'virtual_nw_y_pixel': 1220874841,
                                        'virtual_width': -618345784,
                                        'virtual_height': -456043626,
                                    },
                            {
                                        'source_monitor': 884651,
                                        'source_nw_x_pixel': -4842351983671554697,
                                        'source_nw_y_pixel': -1799685785869148041,
                                        'source_pixel_width': -2269886163369532403,
                                        'source_pixel_height': -1212627935730238384,
                                        'rotation': -3868708312258887368,
                                        'virtual_nw_x_pixel': -1296719590,
                                        'virtual_nw_y_pixel': -1733153956,
                                        'virtual_width': 414544521,
                                        'virtual_height': -488336558,
                                    },
                            {
                                        'source_monitor': 3781507,
                                        'source_nw_x_pixel': -1812548311688272819,
                                        'source_nw_y_pixel': -6421537544208875505,
                                        'source_pixel_width': -8311906705942826321,
                                        'source_pixel_height': -6922077216060086908,
                                        'rotation': -9036912778914036717,
                                        'virtual_nw_x_pixel': -215559570,
                                        'virtual_nw_y_pixel': 920857434,
                                        'virtual_width': -1617703814,
                                        'virtual_height': -1011843102,
                                    },
                            {
                                        'source_monitor': 2316078,
                                        'source_nw_x_pixel': -1064636035276642677,
                                        'source_nw_y_pixel': -2918401773523823193,
                                        'source_pixel_width': -4466799227284669252,
                                        'source_pixel_height': -8970334356696398464,
                                        'rotation': -7597176214103409983,
                                        'virtual_nw_x_pixel': -629211647,
                                        'virtual_nw_y_pixel': -127614192,
                                        'virtual_width': 281898769,
                                        'virtual_height': -1270036573,
                                    },
                            {
                                        'source_monitor': 4781118,
                                        'source_nw_x_pixel': -8866074899699174633,
                                        'source_nw_y_pixel': -6718737326543111901,
                                        'source_pixel_width': -2477287347194811799,
                                        'source_pixel_height': -3597447757628177439,
                                        'rotation': -3556784965246208333,
                                        'virtual_nw_x_pixel': -888601596,
                                        'virtual_nw_y_pixel': -751536774,
                                        'virtual_width': 1955393711,
                                        'virtual_height': 502843529,
                                    },
                            {
                                        'source_monitor': 4188026,
                                        'source_nw_x_pixel': -6162283128338055743,
                                        'source_nw_y_pixel': -8211613713520052984,
                                        'source_pixel_width': -3147981615255282492,
                                        'source_pixel_height': -6125217885063322414,
                                        'rotation': -2385041784406373743,
                                        'virtual_nw_x_pixel': 1554049558,
                                        'virtual_nw_y_pixel': -1331461492,
                                        'virtual_width': 1093944332,
                                        'virtual_height': -967958368,
                                    },
                            {
                                        'source_monitor': 2993103,
                                        'source_nw_x_pixel': -4623332258455845709,
                                        'source_nw_y_pixel': -5926401072395218428,
                                        'source_pixel_width': -470787744933494288,
                                        'source_pixel_height': -2038036289603427810,
                                        'rotation': -9211620409722806757,
                                        'virtual_nw_x_pixel': -1252086338,
                                        'virtual_nw_y_pixel': -1164676086,
                                        'virtual_width': 530489573,
                                        'virtual_height': -332238696,
                                    },
                            {
                                        'source_monitor': 4889212,
                                        'source_nw_x_pixel': -1824203014868965043,
                                        'source_nw_y_pixel': -2160648121058298938,
                                        'source_pixel_width': -4529499847134205804,
                                        'source_pixel_height': -4888363220478530337,
                                        'rotation': -5309330104373386428,
                                        'virtual_nw_x_pixel': -1827225528,
                                        'virtual_nw_y_pixel': 442189714,
                                        'virtual_width': 659980763,
                                        'virtual_height': 1019549635,
                                    },
                        ],
                },
                {
                    'description': 'ϢfũùȦҠ[аΝʥλʭƆҰ4ʈĘΟѓςȩҫȾԫĘǿеɿʉþ',
                    'monitors': [
                            {
                                        'identifier': 8690307,
                                        'width': -3728183414087674475,
                                        'height': 8523808591111634482,
                                    },
                            {
                                        'identifier': -215280,
                                        'width': -6057518205187546817,
                                        'height': -9195494225443893054,
                                    },
                            {
                                        'identifier': 8965096,
                                        'width': -5897801554594878023,
                                        'height': 3116632068790092240,
                                    },
                            {
                                        'identifier': 2042255,
                                        'width': -7927975468670817604,
                                        'height': 8446309714405802849,
                                    },
                            {
                                        'identifier': 3685935,
                                        'width': -4462100714349574277,
                                        'height': -5856412741829523909,
                                    },
                            {
                                        'identifier': 8117772,
                                        'width': 8562268042530998473,
                                        'height': 4113777574886469493,
                                    },
                            {
                                        'identifier': 5579052,
                                        'width': 254330085281363289,
                                        'height': -4410215249949771778,
                                    },
                            {
                                        'identifier': 2188646,
                                        'width': -2521939545703971254,
                                        'height': -9056036216988634745,
                                    },
                            {
                                        'identifier': 8923083,
                                        'width': -3816269826093613025,
                                        'height': 3272640264075066137,
                                    },
                            {
                                        'identifier': 3896780,
                                        'width': 6570161957533792076,
                                        'height': -265091638270611892,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 9921867,
                                        'source_nw_x_pixel': -6496040072361241331,
                                        'source_nw_y_pixel': -4304139930302595814,
                                        'source_pixel_width': -273718991213125476,
                                        'source_pixel_height': -2410799616817327533,
                                        'rotation': -3799241028916651838,
                                        'virtual_nw_x_pixel': 1993537652,
                                        'virtual_nw_y_pixel': 1537530930,
                                        'virtual_width': 709965471,
                                        'virtual_height': -1299583863,
                                    },
                            {
                                        'source_monitor': 3666516,
                                        'source_nw_x_pixel': -5451055298495231346,
                                        'source_nw_y_pixel': -4955366832691641629,
                                        'source_pixel_width': -5158020904709655153,
                                        'source_pixel_height': -5727481258690128366,
                                        'rotation': -2695837778801554958,
                                        'virtual_nw_x_pixel': 9514732,
                                        'virtual_nw_y_pixel': -1256245516,
                                        'virtual_width': 529767993,
                                        'virtual_height': 1154213415,
                                    },
                            {
                                        'source_monitor': 8691800,
                                        'source_nw_x_pixel': -5970324750485474843,
                                        'source_nw_y_pixel': -7362567736740690605,
                                        'source_pixel_width': -4598260194562573278,
                                        'source_pixel_height': -7403001191917450708,
                                        'rotation': -5098786220465645938,
                                        'virtual_nw_x_pixel': -808610161,
                                        'virtual_nw_y_pixel': -1372606931,
                                        'virtual_width': 1060976298,
                                        'virtual_height': 1494741243,
                                    },
                            {
                                        'source_monitor': 6824118,
                                        'source_nw_x_pixel': -6821780795732536806,
                                        'source_nw_y_pixel': -3137443995217662802,
                                        'source_pixel_width': -4864384030823519766,
                                        'source_pixel_height': -7071209547940563779,
                                        'rotation': -7494977139211684065,
                                        'virtual_nw_x_pixel': -1715723180,
                                        'virtual_nw_y_pixel': -274941439,
                                        'virtual_width': 1360355450,
                                        'virtual_height': -464708569,
                                    },
                            {
                                        'source_monitor': -61862,
                                        'source_nw_x_pixel': -5113422396082303175,
                                        'source_nw_y_pixel': -5418224410112973768,
                                        'source_pixel_width': -2601117012723721924,
                                        'source_pixel_height': -850599865168336231,
                                        'rotation': -2904719176052307999,
                                        'virtual_nw_x_pixel': -1852495219,
                                        'virtual_nw_y_pixel': 1675410924,
                                        'virtual_width': 487268599,
                                        'virtual_height': -1323455788,
                                    },
                            {
                                        'source_monitor': 3456015,
                                        'source_nw_x_pixel': -6549457061162887919,
                                        'source_nw_y_pixel': -7606676677325983153,
                                        'source_pixel_width': -8444032751084829884,
                                        'source_pixel_height': -1946856114833065785,
                                        'rotation': -1184044228106607340,
                                        'virtual_nw_x_pixel': -1132952250,
                                        'virtual_nw_y_pixel': 1871834415,
                                        'virtual_width': 1325757657,
                                        'virtual_height': -1724923860,
                                    },
                            {
                                        'source_monitor': 809628,
                                        'source_nw_x_pixel': -5562594189513883526,
                                        'source_nw_y_pixel': -7746447323273022525,
                                        'source_pixel_width': -8648555154274357289,
                                        'source_pixel_height': -2887680544060855097,
                                        'rotation': -7074277704246099415,
                                        'virtual_nw_x_pixel': 1880127078,
                                        'virtual_nw_y_pixel': -957092646,
                                        'virtual_width': -1466471467,
                                        'virtual_height': -1304127240,
                                    },
                            {
                                        'source_monitor': 2067177,
                                        'source_nw_x_pixel': -4893361915571763977,
                                        'source_nw_y_pixel': -3324848023961833061,
                                        'source_pixel_width': -6340051212967702264,
                                        'source_pixel_height': -5548441865372958046,
                                        'rotation': -6049708886519689248,
                                        'virtual_nw_x_pixel': 1467788095,
                                        'virtual_nw_y_pixel': 1315016666,
                                        'virtual_width': -566540352,
                                        'virtual_height': -1393311098,
                                    },
                            {
                                        'source_monitor': 7371191,
                                        'source_nw_x_pixel': -7834987618830014763,
                                        'source_nw_y_pixel': -428938498496032664,
                                        'source_pixel_width': -624155842381010000,
                                        'source_pixel_height': -6798179726456152521,
                                        'rotation': -5682914092556764259,
                                        'virtual_nw_x_pixel': -597225061,
                                        'virtual_nw_y_pixel': -1534296687,
                                        'virtual_width': -396549768,
                                        'virtual_height': -596985354,
                                    },
                            {
                                        'source_monitor': 2194580,
                                        'source_nw_x_pixel': -2357258864724341413,
                                        'source_nw_y_pixel': -4299601273371063132,
                                        'source_pixel_width': -8388172530913781858,
                                        'source_pixel_height': -8333340220399045069,
                                        'rotation': -3894458734263511560,
                                        'virtual_nw_x_pixel': -1617957142,
                                        'virtual_nw_y_pixel': 187237960,
                                        'virtual_width': 1149513280,
                                        'virtual_height': -538293286,
                                    },
                        ],
                },
                {
                    'description': '˦ͳßŨʶђǀƝ\x8bԮĲ\x81-ƪ˒ǣʟCъ½ʫӮň˝¨ȤǠƿýɝ',
                    'monitors': [
                            {
                                        'identifier': -234994,
                                        'width': -5045272828813994196,
                                        'height': 7034998522569958271,
                                    },
                            {
                                        'identifier': -799652,
                                        'width': 677568208068018818,
                                        'height': -340240792859075295,
                                    },
                            {
                                        'identifier': 9142069,
                                        'width': -8408296706960528479,
                                        'height': -6124468309137352478,
                                    },
                            {
                                        'identifier': 9375034,
                                        'width': -6161004586468077612,
                                        'height': 2348335783369385240,
                                    },
                            {
                                        'identifier': -891242,
                                        'width': 128884096639127049,
                                        'height': 2239296543044263635,
                                    },
                            {
                                        'identifier': 6355923,
                                        'width': -5787108808434897977,
                                        'height': 8260094807981479778,
                                    },
                            {
                                        'identifier': 505093,
                                        'width': -4656619161631584384,
                                        'height': 177882996945189109,
                                    },
                            {
                                        'identifier': 4902000,
                                        'width': 7108360071097210788,
                                        'height': -4819656502570133691,
                                    },
                            {
                                        'identifier': 8275551,
                                        'width': 6348420891735781437,
                                        'height': 6741183570826649867,
                                    },
                            {
                                        'identifier': 9731937,
                                        'width': 37244054542040360,
                                        'height': -583449139948824570,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2980132,
                                        'source_nw_x_pixel': -2629831317974270568,
                                        'source_nw_y_pixel': -2448521985053834587,
                                        'source_pixel_width': -6757532842685243797,
                                        'source_pixel_height': -8578894445943257997,
                                        'rotation': -444305846154982754,
                                        'virtual_nw_x_pixel': 1415744373,
                                        'virtual_nw_y_pixel': -1099791342,
                                        'virtual_width': -352056527,
                                        'virtual_height': -1216834405,
                                    },
                            {
                                        'source_monitor': 6861381,
                                        'source_nw_x_pixel': -3941611749556197857,
                                        'source_nw_y_pixel': -333962448874060848,
                                        'source_pixel_width': -2457514613934443035,
                                        'source_pixel_height': -2575568119414756983,
                                        'rotation': -4192642449202807674,
                                        'virtual_nw_x_pixel': -1297946845,
                                        'virtual_nw_y_pixel': 311060540,
                                        'virtual_width': 1227357326,
                                        'virtual_height': 1461021087,
                                    },
                            {
                                        'source_monitor': 9135685,
                                        'source_nw_x_pixel': -6443400434397460311,
                                        'source_nw_y_pixel': -3778527264024102603,
                                        'source_pixel_width': -800935920839315736,
                                        'source_pixel_height': -8888730298339630292,
                                        'rotation': -9032351784831203195,
                                        'virtual_nw_x_pixel': 1864943383,
                                        'virtual_nw_y_pixel': 166334228,
                                        'virtual_width': -1503214295,
                                        'virtual_height': 21664334,
                                    },
                            {
                                        'source_monitor': 3241113,
                                        'source_nw_x_pixel': -1294412029158752433,
                                        'source_nw_y_pixel': -5501602088787142779,
                                        'source_pixel_width': -4235485028284808480,
                                        'source_pixel_height': -183078987954165339,
                                        'rotation': -7931952414107541939,
                                        'virtual_nw_x_pixel': 1763598623,
                                        'virtual_nw_y_pixel': 762106076,
                                        'virtual_width': 469203996,
                                        'virtual_height': 1518202518,
                                    },
                            {
                                        'source_monitor': 8197700,
                                        'source_nw_x_pixel': -8614903698978824013,
                                        'source_nw_y_pixel': -8302336629303414053,
                                        'source_pixel_width': -1412538889556687628,
                                        'source_pixel_height': -3235789504665983764,
                                        'rotation': -5783180271720304206,
                                        'virtual_nw_x_pixel': 1709822791,
                                        'virtual_nw_y_pixel': -1483293841,
                                        'virtual_width': -315635538,
                                        'virtual_height': 1519932503,
                                    },
                            {
                                        'source_monitor': 7920277,
                                        'source_nw_x_pixel': -6236485858595890550,
                                        'source_nw_y_pixel': -220558502263865158,
                                        'source_pixel_width': -2698979839718068905,
                                        'source_pixel_height': -7696544323393504646,
                                        'rotation': -5744283421301254037,
                                        'virtual_nw_x_pixel': 580066907,
                                        'virtual_nw_y_pixel': -1600416022,
                                        'virtual_width': 972187942,
                                        'virtual_height': 283663179,
                                    },
                            {
                                        'source_monitor': 5173874,
                                        'source_nw_x_pixel': -3335797719246510543,
                                        'source_nw_y_pixel': -2113196049646723098,
                                        'source_pixel_width': -7565203136598226825,
                                        'source_pixel_height': -4659034313689978103,
                                        'rotation': -2434326596718340820,
                                        'virtual_nw_x_pixel': 871861726,
                                        'virtual_nw_y_pixel': -1266466868,
                                        'virtual_width': 1785390187,
                                        'virtual_height': -1456778481,
                                    },
                            {
                                        'source_monitor': 1571180,
                                        'source_nw_x_pixel': -9142321014821245925,
                                        'source_nw_y_pixel': -886516224797803317,
                                        'source_pixel_width': -4089946407145998538,
                                        'source_pixel_height': -206541913760784754,
                                        'rotation': -3303172755982288747,
                                        'virtual_nw_x_pixel': 1836552170,
                                        'virtual_nw_y_pixel': -1306309377,
                                        'virtual_width': -1274902556,
                                        'virtual_height': -578473483,
                                    },
                            {
                                        'source_monitor': 8536629,
                                        'source_nw_x_pixel': -8253093773633646397,
                                        'source_nw_y_pixel': -668771430887251655,
                                        'source_pixel_width': -5398340104385193816,
                                        'source_pixel_height': -4878712880890610593,
                                        'rotation': -5323809031684140907,
                                        'virtual_nw_x_pixel': -1301106691,
                                        'virtual_nw_y_pixel': 821508865,
                                        'virtual_width': 87905189,
                                        'virtual_height': 462207208,
                                    },
                            {
                                        'source_monitor': 7805625,
                                        'source_nw_x_pixel': -2979271210947721634,
                                        'source_nw_y_pixel': -2056921869242606976,
                                        'source_pixel_width': -8806775507280875020,
                                        'source_pixel_height': -8805063202038174761,
                                        'rotation': -7562712653351430549,
                                        'virtual_nw_x_pixel': -480967989,
                                        'virtual_nw_y_pixel': 907827101,
                                        'virtual_width': 942891394,
                                        'virtual_height': 695255608,
                                    },
                        ],
                },
                {
                    'description': 'ɪʮԤͼÍǽʏâĔ.šӀт\u0381WėƂȆːП¨ŻѱğAΝϙѩÑħ',
                    'monitors': [
                            {
                                        'identifier': 3735044,
                                        'width': -6806125191303427289,
                                        'height': 7543300877568842637,
                                    },
                            {
                                        'identifier': -687858,
                                        'width': 1100940532517314604,
                                        'height': 7295836710790629373,
                                    },
                            {
                                        'identifier': -613928,
                                        'width': 766995998596830736,
                                        'height': -2541580342027538508,
                                    },
                            {
                                        'identifier': 5074356,
                                        'width': -8413301034065212383,
                                        'height': 3831072705410505289,
                                    },
                            {
                                        'identifier': 513017,
                                        'width': -5758542813732607848,
                                        'height': -966573965445532106,
                                    },
                            {
                                        'identifier': 3683201,
                                        'width': -3426884767512233226,
                                        'height': -2550128361874952391,
                                    },
                            {
                                        'identifier': 1335832,
                                        'width': 6597741334974097388,
                                        'height': -3389502147951505811,
                                    },
                            {
                                        'identifier': 8545871,
                                        'width': -5206416768657137654,
                                        'height': -4909973494782363814,
                                    },
                            {
                                        'identifier': 6378669,
                                        'width': 1858990250852418703,
                                        'height': -5136758319290706725,
                                    },
                            {
                                        'identifier': -773289,
                                        'width': 4390537710861294580,
                                        'height': 27426786118014792,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 799028,
                                        'source_nw_x_pixel': -5905444666187681613,
                                        'source_nw_y_pixel': -1782391619507317446,
                                        'source_pixel_width': -6147280366956102605,
                                        'source_pixel_height': -8315548361587233248,
                                        'rotation': -7545825420316825143,
                                        'virtual_nw_x_pixel': -1554517542,
                                        'virtual_nw_y_pixel': 139350326,
                                        'virtual_width': -623632007,
                                        'virtual_height': 841415957,
                                    },
                            {
                                        'source_monitor': 4707938,
                                        'source_nw_x_pixel': -3608540569749240435,
                                        'source_nw_y_pixel': -5543188875733441853,
                                        'source_pixel_width': -3692341282364141670,
                                        'source_pixel_height': -3018363936672521476,
                                        'rotation': -6855115290665344396,
                                        'virtual_nw_x_pixel': -1543328824,
                                        'virtual_nw_y_pixel': 1569514349,
                                        'virtual_width': -1454715589,
                                        'virtual_height': -74957628,
                                    },
                            {
                                        'source_monitor': 2388675,
                                        'source_nw_x_pixel': -2769925281035554885,
                                        'source_nw_y_pixel': -7412197752701027150,
                                        'source_pixel_width': -2735409617591280351,
                                        'source_pixel_height': -662565351926110053,
                                        'rotation': -94114354762550944,
                                        'virtual_nw_x_pixel': -1365537987,
                                        'virtual_nw_y_pixel': 903813611,
                                        'virtual_width': -86062470,
                                        'virtual_height': 1137061242,
                                    },
                            {
                                        'source_monitor': 5394447,
                                        'source_nw_x_pixel': -830694570966552359,
                                        'source_nw_y_pixel': -3068727907906432675,
                                        'source_pixel_width': -2206794598554917861,
                                        'source_pixel_height': -7728439672693345051,
                                        'rotation': -5766859323300787243,
                                        'virtual_nw_x_pixel': -228636279,
                                        'virtual_nw_y_pixel': -1355616627,
                                        'virtual_width': -1293648559,
                                        'virtual_height': 408238534,
                                    },
                            {
                                        'source_monitor': 8305436,
                                        'source_nw_x_pixel': -7960651539970497723,
                                        'source_nw_y_pixel': -5434081210089364704,
                                        'source_pixel_width': -589027051728705321,
                                        'source_pixel_height': -6427611294659874278,
                                        'rotation': -5208847413249066188,
                                        'virtual_nw_x_pixel': -260449346,
                                        'virtual_nw_y_pixel': -1429928394,
                                        'virtual_width': -1258713751,
                                        'virtual_height': 1236104088,
                                    },
                            {
                                        'source_monitor': 5801533,
                                        'source_nw_x_pixel': -5371402848995611365,
                                        'source_nw_y_pixel': -7908541226418172236,
                                        'source_pixel_width': -6011639882824153775,
                                        'source_pixel_height': -8488524341531905330,
                                        'rotation': -439454945491846382,
                                        'virtual_nw_x_pixel': 331436177,
                                        'virtual_nw_y_pixel': -655294908,
                                        'virtual_width': -325207383,
                                        'virtual_height': -795601270,
                                    },
                            {
                                        'source_monitor': 5781248,
                                        'source_nw_x_pixel': -725253875776875960,
                                        'source_nw_y_pixel': -2353484493194117981,
                                        'source_pixel_width': -3194052223939059599,
                                        'source_pixel_height': -2020375130746392043,
                                        'rotation': -1704726244232308703,
                                        'virtual_nw_x_pixel': 314893336,
                                        'virtual_nw_y_pixel': -354470745,
                                        'virtual_width': -1299377431,
                                        'virtual_height': -968155234,
                                    },
                            {
                                        'source_monitor': 8539428,
                                        'source_nw_x_pixel': -6846032733148984168,
                                        'source_nw_y_pixel': -5790927175236554306,
                                        'source_pixel_width': -5663234580188917499,
                                        'source_pixel_height': -5295616887682949600,
                                        'rotation': -1597867556087079386,
                                        'virtual_nw_x_pixel': 1142701366,
                                        'virtual_nw_y_pixel': 1062366597,
                                        'virtual_width': -1009296503,
                                        'virtual_height': 1317443951,
                                    },
                            {
                                        'source_monitor': 9698295,
                                        'source_nw_x_pixel': -1768617323662763746,
                                        'source_nw_y_pixel': -6817452720569179447,
                                        'source_pixel_width': -6220916425987322963,
                                        'source_pixel_height': -8414649343520942237,
                                        'rotation': -5811587089698277149,
                                        'virtual_nw_x_pixel': 414305936,
                                        'virtual_nw_y_pixel': -1697441070,
                                        'virtual_width': 1443903211,
                                        'virtual_height': -971067649,
                                    },
                            {
                                        'source_monitor': 6224601,
                                        'source_nw_x_pixel': -2445984426180996860,
                                        'source_nw_y_pixel': -8311782724853061344,
                                        'source_pixel_width': -3051749635105212653,
                                        'source_pixel_height': -5026672624123468810,
                                        'rotation': -1319602346492486724,
                                        'virtual_nw_x_pixel': -863741122,
                                        'virtual_nw_y_pixel': -1395294996,
                                        'virtual_width': -1730362617,
                                        'virtual_height': 1549158645,
                                    },
                        ],
                },
                {
                    'description': 'ЎM˥ʑkɌ¢iʨʡtʲУǝԄӣ\x8eӍӵϟSÏɓ\u0380βĨїӌʌҎ',
                    'monitors': [
                            {
                                        'identifier': 2196666,
                                        'width': -1711031518753158031,
                                        'height': 249389278787421711,
                                    },
                            {
                                        'identifier': 6102460,
                                        'width': -523766422684200813,
                                        'height': -483654279959005604,
                                    },
                            {
                                        'identifier': 1046623,
                                        'width': -3586806334537372904,
                                        'height': -6553014814867481883,
                                    },
                            {
                                        'identifier': 7608367,
                                        'width': 1159927821795859489,
                                        'height': -2622313115006066387,
                                    },
                            {
                                        'identifier': 8125840,
                                        'width': -8793734969371234901,
                                        'height': 6058433702385299633,
                                    },
                            {
                                        'identifier': 7274008,
                                        'width': 7901712502099821882,
                                        'height': -7145449109336136778,
                                    },
                            {
                                        'identifier': 36635,
                                        'width': 3819882058825525473,
                                        'height': 6485308844794612051,
                                    },
                            {
                                        'identifier': 2778994,
                                        'width': -1463546944453973585,
                                        'height': 2585692065130946279,
                                    },
                            {
                                        'identifier': 1085882,
                                        'width': 6653213816665013817,
                                        'height': 4016307210412440325,
                                    },
                            {
                                        'identifier': 8329768,
                                        'width': -8676458322155203436,
                                        'height': 1408956263221327702,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 438869,
                                        'source_nw_x_pixel': -2696560829290913708,
                                        'source_nw_y_pixel': -2161223852530517995,
                                        'source_pixel_width': -6320974224910229649,
                                        'source_pixel_height': -4696796123496681673,
                                        'rotation': -2603377342144316900,
                                        'virtual_nw_x_pixel': -873958529,
                                        'virtual_nw_y_pixel': 1904961091,
                                        'virtual_width': 1458645757,
                                        'virtual_height': 839474132,
                                    },
                            {
                                        'source_monitor': 579206,
                                        'source_nw_x_pixel': -4999649681136578083,
                                        'source_nw_y_pixel': -341354174394457322,
                                        'source_pixel_width': -3413649609411978710,
                                        'source_pixel_height': -1492301754781102882,
                                        'rotation': -5219804804901789920,
                                        'virtual_nw_x_pixel': -1797369922,
                                        'virtual_nw_y_pixel': -1595930200,
                                        'virtual_width': -1766474764,
                                        'virtual_height': -265939485,
                                    },
                            {
                                        'source_monitor': 2611022,
                                        'source_nw_x_pixel': -7430626882307145645,
                                        'source_nw_y_pixel': -6935156240587282743,
                                        'source_pixel_width': -2361366953262529225,
                                        'source_pixel_height': -7084352765916931639,
                                        'rotation': -5819542943917592491,
                                        'virtual_nw_x_pixel': -1754148442,
                                        'virtual_nw_y_pixel': -1203787764,
                                        'virtual_width': 687783469,
                                        'virtual_height': 1063431309,
                                    },
                            {
                                        'source_monitor': 574104,
                                        'source_nw_x_pixel': -6829999787851776252,
                                        'source_nw_y_pixel': -556913277503230893,
                                        'source_pixel_width': -7612176256332116193,
                                        'source_pixel_height': -361886695317730194,
                                        'rotation': -1452234114283815975,
                                        'virtual_nw_x_pixel': -1879945860,
                                        'virtual_nw_y_pixel': 523743540,
                                        'virtual_width': -47203783,
                                        'virtual_height': 206782697,
                                    },
                            {
                                        'source_monitor': 5339143,
                                        'source_nw_x_pixel': -6479198690500985937,
                                        'source_nw_y_pixel': -3023852096549308436,
                                        'source_pixel_width': -4270534522048344546,
                                        'source_pixel_height': -5514897010377777008,
                                        'rotation': -3519053389495512589,
                                        'virtual_nw_x_pixel': -1617929733,
                                        'virtual_nw_y_pixel': -1133801025,
                                        'virtual_width': 440007111,
                                        'virtual_height': -1923339160,
                                    },
                            {
                                        'source_monitor': 6512749,
                                        'source_nw_x_pixel': -6596760638948527428,
                                        'source_nw_y_pixel': -5063111188959580890,
                                        'source_pixel_width': -3500910535037966046,
                                        'source_pixel_height': -6811260488807513868,
                                        'rotation': -7266250943789293841,
                                        'virtual_nw_x_pixel': 1094454355,
                                        'virtual_nw_y_pixel': 1617582651,
                                        'virtual_width': -250561785,
                                        'virtual_height': 403110033,
                                    },
                            {
                                        'source_monitor': 392142,
                                        'source_nw_x_pixel': -6336558338100756825,
                                        'source_nw_y_pixel': -5906159621523498514,
                                        'source_pixel_width': -4701251984395647363,
                                        'source_pixel_height': -2308821710583254425,
                                        'rotation': -2497194963676841453,
                                        'virtual_nw_x_pixel': -361546059,
                                        'virtual_nw_y_pixel': 1451204154,
                                        'virtual_width': 1172928812,
                                        'virtual_height': 1128461488,
                                    },
                            {
                                        'source_monitor': 2385472,
                                        'source_nw_x_pixel': -4034825874243016815,
                                        'source_nw_y_pixel': -6063232459473718764,
                                        'source_pixel_width': -902725996239382601,
                                        'source_pixel_height': -1945247307574379254,
                                        'rotation': -2689567880229143756,
                                        'virtual_nw_x_pixel': -757457796,
                                        'virtual_nw_y_pixel': -222653610,
                                        'virtual_width': 1974295099,
                                        'virtual_height': -1910205413,
                                    },
                            {
                                        'source_monitor': 3245733,
                                        'source_nw_x_pixel': -5802001621528716102,
                                        'source_nw_y_pixel': -8902066736460624863,
                                        'source_pixel_width': -4053275840097425588,
                                        'source_pixel_height': -8961580427932331905,
                                        'rotation': -564938924857513530,
                                        'virtual_nw_x_pixel': -188396525,
                                        'virtual_nw_y_pixel': 23100225,
                                        'virtual_width': -595891068,
                                        'virtual_height': 1799933393,
                                    },
                            {
                                        'source_monitor': 9697280,
                                        'source_nw_x_pixel': -1125702105670767865,
                                        'source_nw_y_pixel': -9189367636224335797,
                                        'source_pixel_width': -1272557995108874304,
                                        'source_pixel_height': -1906811660916880560,
                                        'rotation': -47735239318418653,
                                        'virtual_nw_x_pixel': 707903860,
                                        'virtual_nw_y_pixel': 662365990,
                                        'virtual_width': 1574929530,
                                        'virtual_height': -1201251145,
                                    },
                        ],
                },
                {
                    'description': 'ƗхʼǃOm˧ҹ˚ɠǑȪɠÏгąƺԨŔăȜɰǊáӵ\x8b\x8fӉǠƺ',
                    'monitors': [
                            {
                                        'identifier': 4606843,
                                        'width': 4508479621595980072,
                                        'height': 6928669324199763682,
                                    },
                            {
                                        'identifier': 3889501,
                                        'width': -5828260627154069054,
                                        'height': 3844950547622575670,
                                    },
                            {
                                        'identifier': 6928150,
                                        'width': -5085157466708002794,
                                        'height': 8856641733010352463,
                                    },
                            {
                                        'identifier': 2809547,
                                        'width': 8972870229462302327,
                                        'height': 5808927983400992031,
                                    },
                            {
                                        'identifier': -279414,
                                        'width': -9173493407963079200,
                                        'height': -6776242821108011378,
                                    },
                            {
                                        'identifier': 2495179,
                                        'width': -2078070386887044626,
                                        'height': -2332469582567574708,
                                    },
                            {
                                        'identifier': 4130665,
                                        'width': -1383175726986797651,
                                        'height': -3878616560815014970,
                                    },
                            {
                                        'identifier': 3771019,
                                        'width': -3076685776431879916,
                                        'height': 1113499518237191529,
                                    },
                            {
                                        'identifier': 647511,
                                        'width': -8100995093504352177,
                                        'height': 1284504113898449477,
                                    },
                            {
                                        'identifier': -813904,
                                        'width': -7493754782300392009,
                                        'height': 6761546680672338992,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6449416,
                                        'source_nw_x_pixel': -8745777609803010808,
                                        'source_nw_y_pixel': -7371204785243823167,
                                        'source_pixel_width': -5822687406188729295,
                                        'source_pixel_height': -5358372825879432825,
                                        'rotation': -7670982237319211742,
                                        'virtual_nw_x_pixel': -1853973620,
                                        'virtual_nw_y_pixel': -1574695083,
                                        'virtual_width': 502730616,
                                        'virtual_height': -460380548,
                                    },
                            {
                                        'source_monitor': 1737821,
                                        'source_nw_x_pixel': -4418282846504101905,
                                        'source_nw_y_pixel': -2919871315158717359,
                                        'source_pixel_width': -4207450737302999800,
                                        'source_pixel_height': -2086124471780758305,
                                        'rotation': -1570324836793486682,
                                        'virtual_nw_x_pixel': 1931704119,
                                        'virtual_nw_y_pixel': 265782516,
                                        'virtual_width': 1282480656,
                                        'virtual_height': -1217755491,
                                    },
                            {
                                        'source_monitor': -215004,
                                        'source_nw_x_pixel': -7329335361591132367,
                                        'source_nw_y_pixel': -1547950979255741370,
                                        'source_pixel_width': -2374333774904199607,
                                        'source_pixel_height': -5590780207048698236,
                                        'rotation': -2166756070985652668,
                                        'virtual_nw_x_pixel': 1221090370,
                                        'virtual_nw_y_pixel': -1388460114,
                                        'virtual_width': 1733419647,
                                        'virtual_height': 1462056041,
                                    },
                            {
                                        'source_monitor': -9858,
                                        'source_nw_x_pixel': -525112410905776526,
                                        'source_nw_y_pixel': -6157162635277181990,
                                        'source_pixel_width': -1964958969157746175,
                                        'source_pixel_height': -7876930378584041358,
                                        'rotation': -2718641175270861116,
                                        'virtual_nw_x_pixel': -1846268433,
                                        'virtual_nw_y_pixel': -219145019,
                                        'virtual_width': -217251465,
                                        'virtual_height': -6248504,
                                    },
                            {
                                        'source_monitor': 5623749,
                                        'source_nw_x_pixel': -9074764883695222133,
                                        'source_nw_y_pixel': -3434458615261545150,
                                        'source_pixel_width': -4542070730079070212,
                                        'source_pixel_height': -1030967849801397351,
                                        'rotation': -6287911982064226075,
                                        'virtual_nw_x_pixel': -1130584271,
                                        'virtual_nw_y_pixel': -1884493847,
                                        'virtual_width': 1785775786,
                                        'virtual_height': -263256400,
                                    },
                            {
                                        'source_monitor': 1228221,
                                        'source_nw_x_pixel': -5864465414646784757,
                                        'source_nw_y_pixel': -3939256156229162193,
                                        'source_pixel_width': -5950281387990209164,
                                        'source_pixel_height': -7091477407027342566,
                                        'rotation': -8474736128408461530,
                                        'virtual_nw_x_pixel': 1039760735,
                                        'virtual_nw_y_pixel': 1786295072,
                                        'virtual_width': 199508984,
                                        'virtual_height': -629797237,
                                    },
                            {
                                        'source_monitor': 7746870,
                                        'source_nw_x_pixel': -5589640016255682031,
                                        'source_nw_y_pixel': -6618059602978584172,
                                        'source_pixel_width': -932263877648978540,
                                        'source_pixel_height': -7946228117479626718,
                                        'rotation': -8083257684916474794,
                                        'virtual_nw_x_pixel': 469959427,
                                        'virtual_nw_y_pixel': 254302838,
                                        'virtual_width': 517607710,
                                        'virtual_height': 771051807,
                                    },
                            {
                                        'source_monitor': 4549540,
                                        'source_nw_x_pixel': -5308165946883734854,
                                        'source_nw_y_pixel': -6216198826993024058,
                                        'source_pixel_width': -4807798352901931175,
                                        'source_pixel_height': -7436397210011961381,
                                        'rotation': -2114709690355197184,
                                        'virtual_nw_x_pixel': 1796712540,
                                        'virtual_nw_y_pixel': -73646103,
                                        'virtual_width': -1300284337,
                                        'virtual_height': 1912404584,
                                    },
                            {
                                        'source_monitor': 6494671,
                                        'source_nw_x_pixel': -2347489220003011074,
                                        'source_nw_y_pixel': -406055793093327486,
                                        'source_pixel_width': -7493648988353342059,
                                        'source_pixel_height': -4375499057732558382,
                                        'rotation': -7554112165316772284,
                                        'virtual_nw_x_pixel': -1377431853,
                                        'virtual_nw_y_pixel': 574442432,
                                        'virtual_width': -1448421768,
                                        'virtual_height': 1164406955,
                                    },
                            {
                                        'source_monitor': 5183842,
                                        'source_nw_x_pixel': -2940418144813995913,
                                        'source_nw_y_pixel': -465652062169365632,
                                        'source_pixel_width': -2486677432523524952,
                                        'source_pixel_height': -4022590098382639536,
                                        'rotation': -7426058891304952906,
                                        'virtual_nw_x_pixel': 1993863939,
                                        'virtual_nw_y_pixel': -940217747,
                                        'virtual_width': 1040945721,
                                        'virtual_height': -263903545,
                                    },
                        ],
                },
                {
                    'description': 'þĭʶ\x8e"ƍÂіªЛ×ǨΚДʮͽǹΡ¨üˏß£ЍŁɏъѧΞ˸',
                    'monitors': [
                            {
                                        'identifier': 3362797,
                                        'width': -1507881719448835262,
                                        'height': -7418270100032817508,
                                    },
                            {
                                        'identifier': 7146852,
                                        'width': 393235279055511118,
                                        'height': 2535327726428488847,
                                    },
                            {
                                        'identifier': 9830544,
                                        'width': -5178364603287271648,
                                        'height': -9095286863073861092,
                                    },
                            {
                                        'identifier': 6173373,
                                        'width': 7712280916288499499,
                                        'height': -4230494152828941783,
                                    },
                            {
                                        'identifier': 2419519,
                                        'width': 6228256765363658487,
                                        'height': -736491873479691002,
                                    },
                            {
                                        'identifier': 3379157,
                                        'width': -8242645614519711144,
                                        'height': -5402003397068862654,
                                    },
                            {
                                        'identifier': 7076196,
                                        'width': -7799625450257582274,
                                        'height': -6551648742942454560,
                                    },
                            {
                                        'identifier': -931506,
                                        'width': 1098006931310333,
                                        'height': -1831095429881880507,
                                    },
                            {
                                        'identifier': 2724490,
                                        'width': 8290762985597346393,
                                        'height': 4526554550588620090,
                                    },
                            {
                                        'identifier': 9335291,
                                        'width': -2985884443518864805,
                                        'height': 8795116562297072369,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2347798,
                                        'source_nw_x_pixel': -2746555942017531118,
                                        'source_nw_y_pixel': -6351216315708790216,
                                        'source_pixel_width': -7837931318510234109,
                                        'source_pixel_height': -6501807489561160668,
                                        'rotation': -6869529788074444092,
                                        'virtual_nw_x_pixel': 1597327561,
                                        'virtual_nw_y_pixel': 1162711085,
                                        'virtual_width': -293120494,
                                        'virtual_height': -1712553040,
                                    },
                            {
                                        'source_monitor': 4142013,
                                        'source_nw_x_pixel': -1365568714332443569,
                                        'source_nw_y_pixel': -3786077537965896794,
                                        'source_pixel_width': -4804188804110537445,
                                        'source_pixel_height': -5652986861045627904,
                                        'rotation': -5101323061998041509,
                                        'virtual_nw_x_pixel': 1310608123,
                                        'virtual_nw_y_pixel': 1411588150,
                                        'virtual_width': -1880730625,
                                        'virtual_height': -906381388,
                                    },
                            {
                                        'source_monitor': 8017518,
                                        'source_nw_x_pixel': -9021196796556348019,
                                        'source_nw_y_pixel': -7896755126822576794,
                                        'source_pixel_width': -6806617895463133959,
                                        'source_pixel_height': -3427509679288478673,
                                        'rotation': -7614765326115245095,
                                        'virtual_nw_x_pixel': 1200609406,
                                        'virtual_nw_y_pixel': -1671110815,
                                        'virtual_width': 713989238,
                                        'virtual_height': -296153745,
                                    },
                            {
                                        'source_monitor': 6326095,
                                        'source_nw_x_pixel': -753687003299289527,
                                        'source_nw_y_pixel': -5865272527524135295,
                                        'source_pixel_width': -620637775725544530,
                                        'source_pixel_height': -3110834111074281054,
                                        'rotation': -3905907703816567382,
                                        'virtual_nw_x_pixel': 1558129383,
                                        'virtual_nw_y_pixel': 774789446,
                                        'virtual_width': -937828814,
                                        'virtual_height': 1632046818,
                                    },
                            {
                                        'source_monitor': 129907,
                                        'source_nw_x_pixel': -513482137199877838,
                                        'source_nw_y_pixel': -1319110861434129509,
                                        'source_pixel_width': -5757328971873691261,
                                        'source_pixel_height': -8145268331236326951,
                                        'rotation': -3615273786191497824,
                                        'virtual_nw_x_pixel': -782713423,
                                        'virtual_nw_y_pixel': -524061636,
                                        'virtual_width': -1000456158,
                                        'virtual_height': 1027883913,
                                    },
                            {
                                        'source_monitor': 7598038,
                                        'source_nw_x_pixel': -2856444807521288552,
                                        'source_nw_y_pixel': -3002856245592281200,
                                        'source_pixel_width': -2800613527799546199,
                                        'source_pixel_height': -1265389307501648573,
                                        'rotation': -9156712339048849863,
                                        'virtual_nw_x_pixel': -214431940,
                                        'virtual_nw_y_pixel': -1206458197,
                                        'virtual_width': 1817348374,
                                        'virtual_height': 463744845,
                                    },
                            {
                                        'source_monitor': -144591,
                                        'source_nw_x_pixel': -5616729082478393556,
                                        'source_nw_y_pixel': -4948680391442977949,
                                        'source_pixel_width': -546982144478284905,
                                        'source_pixel_height': -629896193148427331,
                                        'rotation': -5121867960765895906,
                                        'virtual_nw_x_pixel': -1779832676,
                                        'virtual_nw_y_pixel': -1138842370,
                                        'virtual_width': -1686922050,
                                        'virtual_height': -593752514,
                                    },
                            {
                                        'source_monitor': -443186,
                                        'source_nw_x_pixel': -3549394947615347254,
                                        'source_nw_y_pixel': -1269015499273558459,
                                        'source_pixel_width': -3411754293863371381,
                                        'source_pixel_height': -3563405442017386513,
                                        'rotation': -5288781465595453337,
                                        'virtual_nw_x_pixel': 808037161,
                                        'virtual_nw_y_pixel': -728786190,
                                        'virtual_width': 843280649,
                                        'virtual_height': 1290941348,
                                    },
                            {
                                        'source_monitor': 7615148,
                                        'source_nw_x_pixel': -8895304410297412405,
                                        'source_nw_y_pixel': -2665043587726225690,
                                        'source_pixel_width': -4414872761594924020,
                                        'source_pixel_height': -389646240644138006,
                                        'rotation': -7724627743024128994,
                                        'virtual_nw_x_pixel': -588102796,
                                        'virtual_nw_y_pixel': 4083713,
                                        'virtual_width': 1476923277,
                                        'virtual_height': -1862767989,
                                    },
                            {
                                        'source_monitor': 4369705,
                                        'source_nw_x_pixel': -5564679788949447936,
                                        'source_nw_y_pixel': -7034230416950668395,
                                        'source_pixel_width': -721048204015669456,
                                        'source_pixel_height': -8397404828252054903,
                                        'rotation': -3183257978159631945,
                                        'virtual_nw_x_pixel': 95315027,
                                        'virtual_nw_y_pixel': -1282142217,
                                        'virtual_width': 1993321706,
                                        'virtual_height': 1311994691,
                                    },
                        ],
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': -801348,

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
            'request_id': 3842814,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'request_id': 9145580,

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
            '$': 'ƇèƅâǖƯǎϳҥˆзͷΔ˓˺ȞӴȧȹõŜɌϖǨƮƴÏˁўˬ',
        },
    ),

    (
        'int',
        {
            '^': 'int',
            '$': -878503593866608434,
        },
    ),

    (
        'float',
        {
            '^': 'float',
            '$': 608169.2513590067,
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
            '$': '20210327:032130.483955:+0000',
        },
    ),

    (
        'string_list',
        {
            '^': 'string_list',
            '$': [
                'ȬͼƉύƌϱÜFǂKɚӽ\x94ýҕɡϛȊͻ΄˒cѱʲľǿѦkĪɍ',
                'О˯ɨMȡоϰʺҰҳϴ˸ťëȬПǦȠԙʐʲBβӎˆ-ȩѷ\x9eΨ',
                '͵ʘӋТʗӅǧƓ/ΥϯҊҸβɸΫεɸ®˯ʏſ§ƞ\u0383YӁÎà҇',
                'ě¿ӎϟαϋҞЛұɰƝНʘȴÓΊùʥʽ:ȬцӞќ`ӧώ˽\x84ҥ',
                'ŹʫVѺМȽËĐϸЫŬӿĢüРӌƆˑGѤɲËКӣѴɿʫ\x9fύҩ',
                '˳ʍ˔ћϋωΌүɔ¿¼ϒҮ\x9bЈǫѰæÈ«\x96ӌǟ\u0380ΨΉÍÝˆϊ',
                '˸џŚѼϒ˘Έð͵[Ϭɂɂ¸ʤԧ˃ơ˖ϪϫӉҨ͵ƬBɹģŌʗ',
                'ѥʰʑʙǉý\x87ƟȳԕǼʣ҇ϹԄѳŽѽȈŉʛ˹ϋ҅Ïчʍn\u03a2Я',
                "ʶҜνǡɯ\x92ţΖ3ǢĦ͵Rӎɹǭœċ'ɁҝċĳȄǭȼЭǎƻɊ",
                'ȁȱøƬřʞНŴȥОƠљĎı\u038b˔\x8fȶΪȩԓŹʨƹƆVԑóϊɆ',
            ],
        },
    ),

    (
        'int_list',
        {
            '^': 'int_list',
            '$': [
                -3670495472970815394,
                -7160434025782185211,
                7197756374158450362,
                -8410275819871181321,
                -2695631278152991866,
                -7323933338146240331,
                4179473079040532361,
                3149130589977526841,
                -682159299931337045,
                6911991354054792156,
            ],
        },
    ),

    (
        'float_list',
        {
            '^': 'float_list',
            '$': [
                184995.03900377185,
                240609.05312189547,
                985782.3216511225,
                382143.5412595097,
                929124.0409158996,
                704153.9850084481,
                905497.5594908502,
                170156.52606057224,
                217336.78547246597,
                715070.4717017572,
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
            ],
        },
    ),

    (
        'datetime_list',
        {
            '^': 'datetime_list',
            '$': [
                '20210327:032131.419859:+0000',
                '20210327:032131.436865:+0000',
                '20210327:032131.455784:+0000',
                '20210327:032131.472987:+0000',
                '20210327:032131.490636:+0000',
                '20210327:032131.507587:+0000',
                '20210327:032131.524873:+0000',
                '20210327:032131.542126:+0000',
                '20210327:032131.559550:+0000',
                '20210327:032131.576694:+0000',
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
            'name': 'ҬˢʷÉӵѾӟűëEDԂɭѬ˙ӞĻʭϹҼ/AöЦə˞ŠÁӂâ',
            'value': {
                '^': 'datetime_list',
                '$': [
                    '20210327:032130.092175:+0000',
                    '20210327:032130.105318:+0000',
                    '20210327:032130.118390:+0000',
                    '20210327:032130.131367:+0000',
                    '20210327:032130.143807:+0000',
                    '20210327:032130.155952:+0000',
                    '20210327:032130.169426:+0000',
                    '20210327:032130.182746:+0000',
                    '20210327:032130.196001:+0000',
                    '20210327:032130.208692:+0000',
                ],
            },
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'name': 'ő',

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
            'catalog': 'ҊȥӠƅɅǛԗҺ΅ƱǴѼʉȇƘϼ˸\x89ˆΎȷЮʄʠǙpgƔʛȐ',
            'message': 'ӐʛʭǞΥ˧Ǣ!ɘ\x89ˏє®ßıɇқϤÉӊΔǮţгάҴѶԘ˼ē',
            'arguments': [
                {
                    'name': 'ˬñ˨ȴψƙ*ȰҪǶЋԐIФӎԒӂУ^¸˟αǅУúŒнд)ƅ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ʒó˸˞ïűǶÊ˚ӾȭƶԪϢŖϬЖ҅ĒȦɝɳýή˕ӓƻǅѵӐ',
                                        'ˁӰˌʭŹӆÊïѳʕ¾ʈǾл"нǅбΚН˝Ӏ҈ϩпεĂӎÄҶ',
                                        'ʚ˙ƛ˘ИǔˌʧѪ¤Őĥʩʬǘǔˎ\u0378ӝȶª˶ƧȸǝƋƯ¨Ӟǀ',
                                        'ԕ˷\x85ΈȲ˜șҲsӈʱɃʋѪΌò!\u0383З˯Ԟɷ˱¤Ȋ1ЏʞκĻ',
                                        'ԪͶȴǕɍͽȣɰҗŅʇԜħΙԉҵRӏʻÛԘʎ\x93ʼĕÇȜUӕʘ',
                                        '#ǽѷȸџƦāAǶαƖθĘŧˀÛpЖΉƖɴ\x83yp\x99ԃÆϟƁϸ',
                                        'ѕХª*Ơɩ˚\u0381Ѡҝł˃ɱƾ¸óԤrʅɹˉɢύĚѝӃӢ\u0379Ũф',
                                        'òüªȋ;\x9fɠϛ˪ϏΡƢПϥȿѠʗҨѴаŖɀż˝їìрǑ¡˚',
                                        'КĆȚÑε\u03a2ɽӹҰǫҒ\u038bÙҨУȴ;ҏʀ˺\x8eʹʃƠ˄мӾ\x86ͱʮ',
                                        'уħ¦ϡŌzɽ£Ưɳċr˛Ǩ˸ѯ\x87Ǔӣªϳê¸ϹʱЧϤҪæĤ',
                                    ],
                        },
                },
                {
                    'name': 'ҋҚR˺ӨѭΞñǅɖӲԊԒьÐʑÿƮrʌʤ˓ȞΞƑĴ˯',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:032128.325439:+0000',
                                        '20210327:032128.342750:+0000',
                                        '20210327:032128.360138:+0000',
                                        '20210327:032128.377660:+0000',
                                        '20210327:032128.395094:+0000',
                                        '20210327:032128.413201:+0000',
                                        '20210327:032128.430106:+0000',
                                        '20210327:032128.443655:+0000',
                                        '20210327:032128.458640:+0000',
                                        '20210327:032128.471203:+0000',
                                    ],
                        },
                },
                {
                    'name': "wñȩӏƒƩɩƉǀў˙EϏԊДñ'ѝΙÀЏӻǿц¦ŹԩӠԝȅ",
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:032128.548411:+0000',
                                        '20210327:032128.565280:+0000',
                                        '20210327:032128.581972:+0000',
                                        '20210327:032128.600327:+0000',
                                        '20210327:032128.617274:+0000',
                                        '20210327:032128.634275:+0000',
                                        '20210327:032128.651198:+0000',
                                        '20210327:032128.668309:+0000',
                                        '20210327:032128.686436:+0000',
                                        '20210327:032128.705868:+0000',
                                    ],
                        },
                },
                {
                    'name': '\x83сϦƔ\x9fȻȾǗǦcүҩ¤ΘóδďʁɓϲɅϞ˩\u03a2M3ƻƷ\x90ѷ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ӯʹŸŦʄΊԗӓzӒz҇@ͱΏ\x8eɷMσοӟOåĹϢκʴоμі',
                                        'ӭԡ|ǅȄњϧ÷ȰɐĹďÙƞĆʷźĦ²ĚәͱƄˬɋ\x8bϪΒҫϕ',
                                        'àțȸЄǑѳҗҧǆ¨£ԟѮ\x89ç\x7fԬʚΚ˪҈Óŧϸȩ=ϿÕèʵ',
                                        'ёЩϸ˔Ϣ˾ɌϰЕ˸ƒ҉ɷTɀǸƫϫȎџѠͱǗtòlχΞҾϽ',
                                        'ʹжшʎїƜӟǞȬ҃÷ƥʞѯn\x8eԪӻԂϗěțƪӊų˶µQĢľ',
                                        'ĭӉƫӫȔӑÅԚ˱жɔтч҂ƷȇǺʬƱǺ˯ĶΗ\xadөưɏº²ȋ',
                                        'ēuȠ¾ȭɉѼԪbŦļȕй>ø\x90ЇŰҷǇЈǪҁȆʷɈÅӳԀΜ',
                                        'ѶƁǌԑҌžŚYѾҟɰ9ëСКFÂ\xa0ӵ˻Ͳ˟ҷ\x90ŉƝ˼ĂЙˣ',
                                        'ͿӧДї1цǖιѶ\x90пäѮйfSˡčˏʺԎʱ˾Ҍ\x9eԘϒҮưӈ',
                                        'ɓIǁˑ˜ŐŊƂ˧ɚƭӞȩǿȱʇҡДя˄ãѷ΅ĉǊɘàĖɰč',
                                    ],
                        },
                },
                {
                    'name': 'ũΪѣԗŞ1ÝˡĜҸ?ŌҾΗϚӈћˈʎ',
                    'value': {
                            '^': 'string_list',
                            '$': [
                                        'ȗЅ¿\x9fLяː\x81вûÄӅι*ͰӨCφ˴Ĉγ҄ÈɥΐƾƥƨӎЖ',
                                        '˱ϖϳÃ˛ѤġˉНЌ\x86ă,Ŧ˖˟çǿɒɲԋȊЊ\x88ӇΤνšňΚ',
                                        'К»ԏþǴщҥȅ_ùÞ±дóƻÁȠҒǔɜ÷ζZŌ¹ҒбϪĘ:',
                                        'Ӱ',
                                        '˵ͻϴә¨˦\x8fδӉ\x9e\x84зÐʯǡǪǍĤþͷˁˈƁˎͳĽÏƚЯɉ',
                                        'jœÀǥUɘЊNӝȝԋƟѠǘĩȲ\u0381ӎtъʟʝhĬEѪƚϩλI',
                                        'œʪғӈȤǁԃ˦ǿ\x7fԏΤԁǦϻƑԍÕ\x99˗ɭƁ˓ȈΜʿƚϙĥơ',
                                        'Ϥʿ˰ƖъҎȸξɫŁӄş½ȩ#ǕrʊϔSͺʕėȞȵǳ\xa0¿хː',
                                        'ÇșМғϿǾ\x96ʷˌϯUƳǐшȈ7Ҡч\xad+ɤƪ8ӜЪθȐðŬΐ',
                                        '^ʃ_ɖ\x84Җ@ʖԆє\x8cƸȉˮΟğҧѝƙκ΅á?ŮǄıgO\x9b|',
                                    ],
                        },
                },
                {
                    'name': 'ϸˀѪȊԖҪΦĎќ2\x90ϫɾşϼЗ˒ȃλӳ\x8eƍΓŷҦİǩˎρҴ',
                    'value': {
                            '^': 'bool',
                            '$': True,
                        },
                },
                {
                    'name': 'ʊǁЩƖsɦϧѢ+ŶʼϲȣύǎВԩ',
                    'value': {
                            '^': 'datetime_list',
                            '$': [
                                        '20210327:032129.400604:+0000',
                                        '20210327:032129.422251:+0000',
                                        '20210327:032129.443694:+0000',
                                        '20210327:032129.463447:+0000',
                                        '20210327:032129.483990:+0000',
                                        '20210327:032129.505582:+0000',
                                        '20210327:032129.526751:+0000',
                                        '20210327:032129.548793:+0000',
                                    ],
                        },
                },
                {
                    'name': '˻ȯΥČǩ˄\x9eéƈƣѢɛǎıĪ\x81ʄɍϪìϰX\x8fΛɽϧӱǋdu',
                    'value': {
                            '^': 'float',
                            '$': 562030.3195415186,
                        },
                },
                {
                    'name': 'ҒˢψĠͲÉӗʬ?ŠƢӰȫI',
                    'value': {
                            '^': 'string',
                            '$': 'ʈȩPYĜ`ļљÑ҉ɑ>˓δҏǮʠҺʶΤЙόцgȀӋόЉщʬ',
                        },
                },
                {
                    'name': 'ћ?Ѱ҈ӋԇŋĹҌӏϲӽ',
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
                                        True,
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

            'catalog': 'ԁź',

            'message': 'č',

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
            'identifier': 'ǪЈҚƇ\x9bÁƷȁӛĻQƏ\x8côə~ɢ.Ɉđʹ¤ϱЇЪ҅"΄ŵԦ',
            'categories': [
                'network',
                'network',
                'access-restriction',
                'network',
                'os',
                'os',
                'os',
                'network',
                'configuration',
                'internal',
            ],
            'source': 'ʿԨȹԣˎƸϧß\x8eѦēөѓ\x9fхǅҥ7ńЦӤƿӽĕŭǼԡɶÂӣ',
            'messages': [
                {
                    'catalog': '%ĽʙЅ҆óыͳWĈșȰϐϥʙqʟùRz/έяȊāϞPȈġƍ',
                    'message': 'ҦёΗɅǨλƨ˕˭Ô¦ϱ˔ĿΏÚҚϡˆʺˋˍĒΩ\u0383ϰϬŴͿć',
                    'arguments': [
                            {
                                        'name': 'ƳΪŵȾåªǱĴΠƆԚԦCѬĚƏ¯ԩҝɪϸϝӫҭԮ\u03a2ϰԕǑɣ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ӛɎĈͱƐʿøŗ\x84Ĩ7ԒψǄҠʖ}óԨԟŖȑ\x82ű\u038dśγĢå+',
                                                    },
                                    },
                            {
                                        'name': 'ѣ˹ƫȿǈӼðЏÙΰȞшЗϫÑǮӆӦѩҷιvƫf˱Ψ҉ѓĶ¨',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032112.315941:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ÂǊñάŻӖȿӉƔӈȞù\x90ӠӽŒχҔфǧάǧҤØɘҼ˕Ӷɟǯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -42808.7810437925,
                                                    },
                                    },
                            {
                                        'name': 'Îӂ\x89',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5379828796788707896,
                                                    },
                                    },
                            {
                                        'name': 'Δ˺ǂƘ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ƚʇÍ°˵ҠTŔЍf˕ӐɣĢζс?ˎ±ė˄Ѻέԓ6ӎʃΌΘ˲',
                                                    },
                                    },
                            {
                                        'name': 'iƶǊėЈӛѰˀӰ˚ΓųĩƬӖӜġ\u0378ɎӴϻÏɌΨòƨ˹ψҢԠ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 232252.94742116402,
                                                    },
                                    },
                            {
                                        'name': '¥ɿϢ\x9cҢǦ¯ϒʼ\x9f҇ϬŊǍɗһǞÆɸҚТϋҍ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -732212139320680851,
                                                    },
                                    },
                            {
                                        'name': 'ӆɶɚSϑԮҊŒΜʛŠ\x95ԜҼӨӻȰä¤ӅŬ\x8eϟğóǻʁ\x9cҗ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -7834000917432028562,
                                                    },
                                    },
                            {
                                        'name': 'ʾɘȽрөÙ³#ϲҊ+ҁʍȲԦ»ÒlƶǘӮӸɨŝҤ\u0381òȑÃЍ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -2481540777920931607,
                                                                            1374959670855394687,
                                                                            3850665519932019928,
                                                                            -620787820268219863,
                                                                            1098371216997786520,
                                                                            -5039170481330533240,
                                                                            7875967510874503811,
                                                                            -3207505512244485708,
                                                                            -8702447429490633793,
                                                                            -3028090508602427256,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÁȸӘӦüҲœ˨о=ʈŷаȜrԨ`ĎӘƏΏÁ\x99ňіӃӸҙøǯ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Иɣӭ´ɰыǆūΌɽ˱ͲѨўҞɞíԌĚԮ2Ķ\u038b6ʳзγά˧Ϥ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ŬԚƛψɓү\u0383x\x9dŭļҕΧ˫ҁеͰǲƸ¸°ʧÆŻϭΌӨ_ӣƨ',
                    'message': 'ĔЬƘ҉Ӡ҃ˇƢу҆ҝβϐ˸ɞ\u03a2ªqʫПúđŮЬӴƘˬÀʎя',
                    'arguments': [
                            {
                                        'name': 'ȝƿɿѡЮˑƥųΊҀŪÍˋ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 588740.06910827,
                                                    },
                                    },
                            {
                                        'name': 'ԙːɃӺϺчˆɑтȤӏʩҝ1ȋӜȞӚϾŇƀƪHũьɲɵԕ¥Ĝ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032113.263825:+0000',
                                                                            '20210327:032113.280992:+0000',
                                                                            '20210327:032113.299419:+0000',
                                                                            '20210327:032113.317284:+0000',
                                                                            '20210327:032113.339126:+0000',
                                                                            '20210327:032113.361402:+0000',
                                                                            '20210327:032113.383796:+0000',
                                                                            '20210327:032113.407757:+0000',
                                                                            '20210327:032113.429150:+0000',
                                                                            '20210327:032113.448822:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ˤɘΞǒƽюʚɑǂǸƂƜơȩͶɮ˃9ȷ2ǣü˪ʵ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ĞϠˈ7(ƂƗǿqӝľɻѤȟˬÔ\x82÷ЋǹǒɒηϫΝh˰ʥʐɭ',
                                                    },
                                    },
                            {
                                        'name': '˖\x90ÿŷǸӊǣƗļbş\x7fđ@Ăӓ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            7757813763218029764,
                                                                            8156614991225447893,
                                                                            -9074658628417866657,
                                                                            3702781767530378346,
                                                                            7373829557986626542,
                                                                            -2405565526741629625,
                                                                            953491095415187377,
                                                                            6940484867696315652,
                                                                            -5088705135342645358,
                                                                            5912638329062357408,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '\xadԉёÑƧŦǚÛӾӤŊűƌΊààƈөIņԦņ§ŴӴ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032113.923321:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Rèɾ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 780035.62007163,
                                                    },
                                    },
                            {
                                        'name': 'ӤOǇμëʵͱӥΔƌɡȘɠѓϤ\x85ɳϟҖvÛӢА˖ɜ7X˧Ũć',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 120961.12257991219,
                                                    },
                                    },
                            {
                                        'name': 'уÿ\x88М˥їTҰѰ˔ҖϋˉèҲǷйЖϏѧǺƃʠЎԗ2ĕƤͺ8',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'Ўȣ҉ԝ\x91ҊҩƃɾϻЂͱH˷Ōωó',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'yɨűĝɀÌϓ°їÈƾċӷ©ɿҝмҩюȱϛϼԆǠű±˯ĚĒ1',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'łłӎЛʤȏåȿɛɌΡéjςԫҤ҅Ћ\x9aƪґѿґoƃĪʌΌ®ӫ',
                    'message': 'У¼Цдċԫʀʛſ{ӓѢԤҙƖĞŒҠΩþȣϊƥ˅UԞĪɊьþ',
                    'arguments': [
                            {
                                        'name': 'ʎsƪ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': -67302.2454215924,
                                                    },
                                    },
                            {
                                        'name': 'Ɂƽ\x9eєφå\u038dԭǀɯţԄǏǾ5ѷ\x8bė˪ѯӑǍӰËђ]ψÿǊӳ',
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
                                                                            False,
                                                                            False,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '˒ғƌ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -1962631697516841907,
                                                                            5393334285956599580,
                                                                            -1392331032735257163,
                                                                            1012911103621696937,
                                                                            -4753790142296422642,
                                                                            2991933170931802325,
                                                                            7080385051654471020,
                                                                            -5005203648062328112,
                                                                            7990541476426795426,
                                                                            -8099968129413176230,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӑ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6351423710455646449,
                                                                            8525237852804730629,
                                                                            -8739574847308891519,
                                                                            -5027471438831668641,
                                                                            553135943868685532,
                                                                            5256196130685393479,
                                                                            -7951288277061053132,
                                                                            8214668509165020355,
                                                                            1961999698347031725,
                                                                            6932306705886965599,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŰĺǪ\x98ѡ\x93ʱ\x86ϸćƇҟʿ˰ҟɤєΆ\x87ʝʣΝȽµӳ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                            {
                                        'name': 'ƻġ˳ɻбόͶ\x83ԓԪЫİȨοѝԕȫѬėϪ©ƍƆ҆Ȍ´ӆϣѬл',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 4717360514789267339,
                                                    },
                                    },
                            {
                                        'name': 'zÏǈˤ˲ƑˮА\u0380ϊӹˆ¬Ӭŧéɱϻҙï»ŴP',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 518941.7479316889,
                                                    },
                                    },
                            {
                                        'name': 'Ƅ¸¶ʋŭ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
                                                                            True,
                                                                            True,
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
                                        'name': 'Ť\x92ƛĒĹƹƅЫԃɬδʴԇèçҎǏǌBҺÎόĊѳȝČɷ˨ƴʐ',
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
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ʒ˅Ή\x80˫ƓΫÇĄ+',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': False,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': "Ēѡś³΄˙Ȟ'|ӱňҤɄЈӻˢѽ¾ƁɦԥĖȲҪĉɉǼ˃Ŝ\x93",
                    'message': 'Ӟ¾ŮӋеŤÔґˠʹӜƙǷЈΆqв˼ȓҞȩэ\x8eʋΎ˹ӐǩƋӇ',
                    'arguments': [
                            {
                                        'name': 'С\u0383ĈöɐĶǉƗǴǧɖȮŽ\x9eǀʐԑȾƼҫʏдујӰĶŐϋȯϖ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 5433624322379908899,
                                                    },
                                    },
                            {
                                        'name': 'ȰʱJӎ\x8a',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032116.064154:+0000',
                                                                            '20210327:032116.081990:+0000',
                                                                            '20210327:032116.099136:+0000',
                                                                            '20210327:032116.116618:+0000',
                                                                            '20210327:032116.135062:+0000',
                                                                            '20210327:032116.152373:+0000',
                                                                            '20210327:032116.169857:+0000',
                                                                            '20210327:032116.187094:+0000',
                                                                            '20210327:032116.204303:+0000',
                                                                            '20210327:032116.221535:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'қjÿϏ҃',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032116.315805:+0000',
                                                                            '20210327:032116.335220:+0000',
                                                                            '20210327:032116.352949:+0000',
                                                                            '20210327:032116.370629:+0000',
                                                                            '20210327:032116.387645:+0000',
                                                                            '20210327:032116.404694:+0000',
                                                                            '20210327:032116.421946:+0000',
                                                                            '20210327:032116.441135:+0000',
                                                                            '20210327:032116.458247:+0000',
                                                                            '20210327:032116.475527:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ǿ-\x8f\x7f+γ½Ӥч½ϸϾ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            852367.1484671879,
                                                                            407994.1704117104,
                                                                            195104.22695205337,
                                                                            765743.3882629694,
                                                                            381551.7468325678,
                                                                            709338.3918525659,
                                                                            351367.72985015286,
                                                                            977124.7457406316,
                                                                            660861.5619057094,
                                                                            406710.2546978176,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'жЁʧªϞӉь˽ӅͲҼȝɞёSʎӥԔєƃ\x86ĵΐͿ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032116.847642:+0000',
                                                                            '20210327:032116.867107:+0000',
                                                                            '20210327:032116.886571:+0000',
                                                                            '20210327:032116.903468:+0000',
                                                                            '20210327:032116.921260:+0000',
                                                                            '20210327:032116.941543:+0000',
                                                                            '20210327:032116.961310:+0000',
                                                                            '20210327:032116.980798:+0000',
                                                                            '20210327:032117.000369:+0000',
                                                                            '20210327:032117.020426:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ӯ3ɽО\x7fӾúΌϷԓ]ˏʭǯĐӅнϽԩˆËŶӻpԖɕҡfλϪ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': '˃ӛЬǺ\x82йЭӉȄԜ˂łԝǾƌͰȷХӾɠųňÒѵɩҤc˟ѓƭ',
                                                    },
                                    },
                            {
                                        'name': 'ӔѫЋϬ\xadłǥťҽҰΖԧxѨ¡ЙŸɌřy+КѽǥӤBɕԄԐȂ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            8118947548805638735,
                                                                            8477265826969935611,
                                                                            -5907519091929011782,
                                                                            -2054040784356330902,
                                                                            -2510569041743959706,
                                                                            5543646759752167250,
                                                                            4400683652979741080,
                                                                            -3017501720433240871,
                                                                            -6768553559874564906,
                                                                            1223867272282434348,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ҌĮŐʟ\u0382Ɂʹчˬ˚ʋͱԈŮԅɜΜΌκ\x88ʅşˌьÿΛí˜Ʋç',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            412472.34742737305,
                                                                            13103.374404131057,
                                                                            447920.8943604005,
                                                                            249220.22854949924,
                                                                            652871.0952053623,
                                                                            -50783.16215358824,
                                                                            893980.2475862263,
                                                                            552926.9897461779,
                                                                            371511.03617687436,
                                                                            815270.8667281631,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɿ¢ôӏǌǃŰ·ԇɨ˅ȑˡ&҂ԒțƄʟ\u0378',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Ӽ\u038b/=ƱԀғѤʤǝÀċ˳ĲԠԡŒɷκɪƯJҌѰȚĴɁʋȤʨ',
                                                    },
                                    },
                            {
                                        'name': 'ԣӑͱƜƜˆƐǕѨ[ǨŗǹʞȫϢɂǉϕĔɝӗҤЉɷѣЯĳŝl',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032117.737100:+0000',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ΞąеiӋHǤ\\Ýњ˱ɯ\x8fȕʙƴŌŇDĳԙИĔ}ȒǕȶʇʬð',
                    'message': 'ɨéMɱ΄ҍ˨Ͽѯ\x9bԉƛȩŒϿˈЈϐʹYҳƓWЀkȄÃѿȅй',
                    'arguments': [
                            {
                                        'name': 'ÐŤØѮɳϮԠ±ÑȰʪʷÍϽƨҝʪʛԨȍ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'căϩӋ˻ɭӃėɪЦ҃ʗԞΏДɟӠGԃΥǖǂTŅт=Ԕkƅ\x8c',
                                                                            'ѾȖʫÓɋм˭фƻǘǌǘҬϦҕПˍ_ˁ\x92őҪZпŁ\u0379ҏǳѨӉ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ªćΘжяш˵ԡǆŧȅǆΤҖɞήӷ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'ŒңҘɯ˰',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032118.036055:+0000',
                                                    },
                                    },
                            {
                                        'name': 'әĚӴцщңVʪɯϠǉԁҨʠtΰó˨Àҳ˸ŮĻʑ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            False,
                                                                            True,
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
                                        'name': 'ϙҭΉ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032118.422429:+0000',
                                                                            '20210327:032118.442349:+0000',
                                                                            '20210327:032118.463236:+0000',
                                                                            '20210327:032118.485109:+0000',
                                                                            '20210327:032118.502904:+0000',
                                                                            '20210327:032118.520400:+0000',
                                                                            '20210327:032118.543191:+0000',
                                                                            '20210327:032118.563423:+0000',
                                                                            '20210327:032118.583889:+0000',
                                                                            '20210327:032118.604887:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '#˙ċєźĒМʵ҂"θɆ˸mȐǗҭűŸ\'¨\x81ͻŷѥëȷę\x9bÓ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032118.703173:+0000',
                                                                            '20210327:032118.720415:+0000',
                                                                            '20210327:032118.739015:+0000',
                                                                            '20210327:032118.756304:+0000',
                                                                            '20210327:032118.774163:+0000',
                                                                            '20210327:032118.791418:+0000',
                                                                            '20210327:032118.810687:+0000',
                                                                            '20210327:032118.828193:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ό§Йʽ\x86Ʋȡ\x89ҸɺɭҕѵӘϟĿЌ˕ϘÔԅǽӝȄȓҿϗӐ˓ʊ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032118.904406:+0000',
                                                    },
                                    },
                            {
                                        'name': 'Җ½ŨȾìŻԨ\x9bҞѨȔΐ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 81491.8252386428,
                                                    },
                                    },
                            {
                                        'name': 'ˇǘvҔȱΑȠȇŇĳ\x9bϯƪƣƣȄǄӒfǄȜѧІėԞĀЍФҖѸ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ķȳҹQӒʄΡӇàІѦѴŞ×ˉЭzŐ\x9fȈӏҹҰŸҶȘñʈǎϐ',
                                                                            'ˑĐɔηĐӔӢӜıѝ5ͷǊȶ,\\Ĕ˰ȵʊΑ\xa0ƣŝȇҿϡáȊŝ',
                                                                            'ϗΝ®dЂѵçЋԞԫνǏԍЫ˳ľѫˢ\u0381ȃХϔɣĈĽĕ˽ϭфш',
                                                                            ';ӹǪɵζӘцδǳБťшЮˮŧǛϛ·ưčĮ·҇ȔԡưǮĹƱӗ',
                                                                            'Ȗ;ΐśԡa§õйȒҗЦęϔғƊκ¿ƎϕĨȥʨȺŎѺȅ^Ͽҭ',
                                                                            'Ԅ˦Һ¾(¢ǂPҐz˯πĿɐкҵÛΉЙũûό˪ǩӋϸv˫҄ʝ',
                                                                            'Ƨ¼Ь\x94\u0378ѮŜĮөŪԬÐĉӋҿӐɇŧҎԩƂƈОȲəzҘĸӀӆ',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɖӸyb×Ƹʲ˹ҙˏǲÅҞи+ʨΩÓč',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3871694813643612294,
                                                                            -5357901834581848266,
                                                                            7643813042437342726,
                                                                            -4734924103701765676,
                                                                            3812630443218120638,
                                                                            -4441451237993877335,
                                                                            6613324226734901860,
                                                                            -4559424591955076702,
                                                                            -8326494888281113783,
                                                                            7462729518884849032,
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǱЇ1ʹɰϡӢĜԎӞԣҫӷˇϤϗҟŌң·Ùűʾ°ЉӼ]ĶΠǹ',
                    'message': '\u0379ҍДĊұ\x96ρȽҩγ\x94źŔӻ˃ĉ\u0379ǂтǞЯÎˮ(ǩϽƥˈ ϟ',
                    'arguments': [
                            {
                                        'name': 'Ʉ\u0381ʲǆȹɾˑҟĔ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            1142075834859126596,
                                                                            -8329884423334563892,
                                                                            7287802195891221776,
                                                                            -5113325524434691147,
                                                                            4667103892418105593,
                                                                            -1269440789770668288,
                                                                            469563104669224143,
                                                                            -5582917705547190965,
                                                                            2324501735155096110,
                                                                            4605705652455283016,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ɗˠTîɴ/˹ƾȀeżҴͿ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            '˲ЭʡϔȉԨϴԮÉԘǔʱeγϪȡȸɵ`Ҕˌ¾?ɽѢǎҠåԬɊ',
                                                                            'όKΒ&ӲѥŖ˶ȭƄɴ§Лƅ˪ˤСӶԘȼ\x9c˰϶ϾıβàȥԔƗ',
                                                                            'ȦυɪғȮϓЃɢſԔɀԇοȼɅȉӃʘҍùηӸ\x9aǁԩˋǌÿʉȷ',
                                                                            'ŢѤƣˍʾŎѭ\u0381ѵêǹïсǚƥӮ\x88ʇHҎЃҰyԣɏǣ\u0378νƩҒ',
                                                                            'ȚВғѝэνΐĥəίтԦ¾ŹŉnџʪΊҚŖëџˡҡǎγů˂¾',
                                                                            'ġѲɫϔˬ˲×˒ʓǚӹ[ǟҫƵĻƿ3ʪ˅БȜȄԈГͶчҏҖ\x83',
                                                                            '1ȋzԁϞȼ¶8ÂŨƪƟξҴƥDʤԪÑŘЯӳϟMϗӚҭŢ\x84ˋ',
                                                                            'ĘԑǧЭӟǻƕǀԄɎǥȯˢɡčӊӿ×ҪĜöǶ/ұΩ˖ˊĖӤu',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʚĝaI˪ļΕɌјʶ~ҶΨϑ¹ɷƨŇƭӆђƳŁĬįԁɓɇŠϢ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ɎˢʙˋѸŢԒÄ@ԥɞʤ¤Ѷ'əˣҘɕƂǃͳҩϧŬӀµЕıI",
                                                    },
                                    },
                            {
                                        'name': 'ØȝЀę\x8aŞȌ˛Sǲč\x92ΧǑӻûͳȻŞʿŴ*НʆɨԏʇҘԈΡ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032120.111021:+0000',
                                                                            '20210327:032120.131114:+0000',
                                                                            '20210327:032120.152653:+0000',
                                                                            '20210327:032120.172440:+0000',
                                                                            '20210327:032120.192391:+0000',
                                                                            '20210327:032120.212126:+0000',
                                                                            '20210327:032120.232489:+0000',
                                                                            '20210327:032120.254793:+0000',
                                                                            '20210327:032120.269383:+0000',
                                                                            '20210327:032120.283944:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ψ',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ґǄĠňпеÄӘҘɢYϝɚˏɂ˦ƿ˾ЬɍʡӼƿÌɝƺɹͽăϯ',
                                                                            '\x7fΜҷˬ\x98ϒԅΫœχѲĝđ3ʬ҆ˈҕˈxˤ\x97ұȑI˶B\x9dʁԔ',
                                                                            'ɀ´˅ӵʴµγƇĺ«ӫȟúʼΞВӆ{\x9bȲȧΠƧƬɵƼaơƳ\x8d',
                                                                            'ǵμŖϒӼǵӈÊǟȹӝʂʜƮɤɠʇʩȑ\x9cԕĺŗкӵϋǕʼϼ)',
                                                                            '˜ӷѶėԉÀͺЧʹŷs\x96НҔʚҝϣʶŕÀԔ·ϲ,ѸBӽɜҗϰ',
                                                                            'Ē3ϑˀҗӬԤƛɾ³ϕʗȔʎΌѮҺWϯȺćɋзƞԎĸуǑȐў',
                                                                            'ǚƷϿƁϧҶÛʏ&аѷЮÓŭΌѪУSҎĹƣŬ˚ȆȆѹƈ6Ѽv',
                                                                            'ŔŇϾѰȥ,ɢψǺͱуˡԃȓɧʾĸȇӚxђʏɴɗ¯μȵģӜү',
                                                                            'ЉʄËҝ˩\x91ɰȂԁ˪ŤϯɊԠ҄7İϭβμОԢѱĴ\x82őԞƒÔӝ',
                                                                            'оΛȻdƙǴʝԉĠţ\x87ĐƛΰǔφǛсϯәȾ˹ȯċɃӓΈǐɋс',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'Ė',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032120.608776:+0000',
                                                    },
                                    },
                            {
                                        'name': 'εЛ\x8eƫɌ',
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
                                                                            True,
                                                                            True,
                                                                            True,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '_)őƎʥx¬Ӗŉ҂\x88Ε¨ϐԧȽҶ˱ҔңҙҰôXΙƯľ҅ҝˌ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032120.929782:+0000',
                                                                            '20210327:032120.947183:+0000',
                                                                            '20210327:032120.964768:+0000',
                                                                            '20210327:032120.981461:+0000',
                                                                            '20210327:032120.998679:+0000',
                                                                            '20210327:032121.016124:+0000',
                                                                            '20210327:032121.032876:+0000',
                                                                            '20210327:032121.049690:+0000',
                                                                            '20210327:032121.066564:+0000',
                                                                            '20210327:032121.083522:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȰȃĎľ˙\x9cż^ʐèPƉʥǳ\xa0ʙ¿ѸRϧ\u0380ÑИ&ӷǻҪΤԒ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'FRӧɞưŸ˧˓ȉǒȤǧ\u0383όïіǲϣԅ\x9e',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032121.237264:+0000',
                                                                            '20210327:032121.254324:+0000',
                                                                            '20210327:032121.272671:+0000',
                                                                            '20210327:032121.293163:+0000',
                                                                            '20210327:032121.315357:+0000',
                                                                            '20210327:032121.335723:+0000',
                                                                            '20210327:032121.354561:+0000',
                                                                            '20210327:032121.372771:+0000',
                                                                            '20210327:032121.393208:+0000',
                                                                            '20210327:032121.414145:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ǎųǿʐΤÃŁ6ͱĘɵ\x84ēɔ×]ÍϣɓûúГ˻ΰƨģҼ˼ʗԣ',
                    'message': '·Ǟ«Óňʁâ¥аУƁƀƠʾˊѮР˶ʍ˝ԮEϢ²ǞцǿО\xadԆ',
                    'arguments': [
                            {
                                        'name': 'ӜBōțh҂Ηθ³',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'Έ\x8fʙǹ˃ά˽ΪǶҗƝΠȏјΒП\x94ҤïïīѱЅȾѸCљԀ¸Ú',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '"ˣѓĺӤʄƤϿȤˁǽȎùïӑɸЉ˫҃ʣҟɯ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 762869.8712614771,
                                                    },
                                    },
                            {
                                        'name': '¦ϾhɌд',
                                        'value': {
                                                        '^': 'int',
                                                        '$': 7765277521048852707,
                                                    },
                                    },
                            {
                                        'name': 'ѣ©ČɈӇӽΰëǄÚʣČʂºԘуЀθɺԇȓȷҀβϓǣӜɋǯǼ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': '»ʒк˅ȐӈŖ\x8aыҷέϣ\u038dԏñЀsϕȗȕϊͿʘΗЏEƌӶ\x8fǸ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            338559.7197658577,
                                                                            132234.08340007172,
                                                                            979878.0788964424,
                                                                            544769.3056877078,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ŸɶҢ¿˙ĴʛȴȷҺƑͶԡƭēѠҠbɎȃδӝvɥлԁǤВǔʁ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Џˡù˵ґĵԗȘͺԊú˹њӫǔƀχɔȂѓ÷ԤĢͷ¿Ė®ɑȟт',
                                                    },
                                    },
                            {
                                        'name': 'ˈ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': "ΤǦŘӠWȯԜ˔ѐΡ*Ǔ'GӯɎ»Үʳ5ɊôќÿϤ[бÖɼǗ",
                                                    },
                                    },
                            {
                                        'name': '˓˅Ӻ/μOʅϨĢ΅ɨŀǆӞӯҁхѬĝɸɻʊԖԂѐˢąȋ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            966997.388329665,
                                                                            118617.12742277118,
                                                                            915259.7063900045,
                                                                            83892.02625172702,
                                                                            563998.1137463049,
                                                                            952003.1300354917,
                                                                            -5463.4947389540175,
                                                                            843454.752837929,
                                                                            159178.54517721056,
                                                                            65026.580797945935,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'нΨϔǝ˘ӂVúƿ\u0382҈ÜčģΚ˧Ҭѽ7ԊψЯɉԘʬʊɦЖԢӲ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            319398.8286573324,
                                                                            316767.72925985826,
                                                                            -63015.69318748158,
                                                                            10459.623835318343,
                                                                            455452.6289833796,
                                                                            650929.9157304367,
                                                                            -61606.92545458294,
                                                                            249207.79494298244,
                                                                            402547.8658468279,
                                                                            -88859.69048501586,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƹɤFqˑkлȿˡԆ һɜԭGČϧʀҲň`ӂ\u038d˴Ӑ\x9eɲƯƂÈ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 230193.53357463772,
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'эЇˈξɥå5ϷԈιƽҀǘƌ\x9cΊΙjԫǕȘƂ\u0381\x90ѓϒӢS҈Ϸ',
                    'message': 'ĜҕżˍʏԇȲƒлƄɊҊzțPȝ(ҟsǄ\u0380¦sԧҹƛӂɐɚҜ',
                    'arguments': [
                            {
                                        'name': 'óʔʏӀσ¬MʷĤȰѻwφѝΙɹŘϿŘ1ѮЈδτŚύǍӠlO',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            -79273.82321488297,
                                                                            -74257.19378108723,
                                                                            949821.2775814182,
                                                                            96922.67599094575,
                                                                            125597.02977368064,
                                                                            178071.2986305417,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'įȴдÄяĥҁſ\x87\x8cԟȠ҇ѦӉ˶Εʵйˊѳ˯ЂǄ ϞǮ¸Ǯʆ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ԋƼ¨ȇƪчºԒɵɻϽƵѾԌȠԈ.ŅΈƓǿͳ\x85\x8dƾTjġ҇Ý',
                                                    },
                                    },
                            {
                                        'name': 'ǍZ˩ςųćţӆǯɥǾӊÐȏҷ͵ЙȳǚʇѫЀпǇʐDʃűƇЫ',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'EӞɓЂʱ¯\x9dØ¼ɌϭӮŚϳэжƕ\x87ȂӅџ§д;ϢκЧЈÄӣ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            False,
                                                                            True,
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
                                        'name': '\x90ǓӷçǲҏҥʳѡωǞѩϯ˫ŝĞ3ZЙԨϺʑư˼ŭɵӈԕf',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            6511852305790447855,
                                                                            -3178685376663051253,
                                                                            -8771004547606775653,
                                                                            299622482002135885,
                                                                            2376955389178412257,
                                                                            -7762004033722823471,
                                                                            -8416516812466969074,
                                                                            1155758038167910791,
                                                                            894202015619219768,
                                                                            -1612387257330433315,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ÐџwɀȬɥǼæ',
                                        'value': {
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
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƮpҸ\x7fđ³ҙȹˈъӰйǕͲѩ҃ԫr6\x84©ҀȄĕƀΖњͻȦ˅',
                                        'value': {
                                                        '^': 'string_list',
                                                        '$': [
                                                                            'ҧЩđʶΩŷΞәѵʇϏɁñƆħƈ.åҦɧŮɑ|ЀӜǲƍǯʄЙ',
                                                                            'Җ¬¤ͶȬзȟцѵ%ʊԜΡȴ)ʓƳΘюϒ=АˍɅǄЄIӟї\x92',
                                                                            'ӔȡȱƦȹȼӳӋϑϐДēΖР\x8eɻҪЎɆˠҚ҈҈ʫҜ\u0378ɺǪɿÁ',
                                                                            'ĿǸƢϞȮӽĔȇ*ԍӘ\u0382ŬΆǙˈŮƓƺӵѻЧҚNԥ\x82чɄĂǍ',
                                                                            'ξӪƫΦȕЪ;EŁɷһv¸ʬχјˊWƿҹƒЫƞӦ3ɗ҇˼ʉϴ',
                                                                            'ԘҡÃɩеdŏƪȁĔʷ\x82τÚšÊ҈\x808ёƙ΅ѳ¯Ћѽ҉ýƶĘ',
                                                                            'ΟʙŕɜǗ͵ҹĞǕŬĆoѨԩJФŢ#°ȅƒůϕηοɒȇɆǒû',
                                                                            'ȊѶ˦ԅƭĢϭӝȓǡцҌœϧҵѮзĝρǛΆӱ˼ρԧ˯ƝǡȤ˲',
                                                                            'ñӀӕĕҹİʈɋŸ˘ɪˬљ!ʉ\x96Íѐʫхɝ\x9dϗƔѷŏӃǳӿй',
                                                                            'ӥǭѤɰâZėʔԧƲ˻ƉǎšǳѵϔˡŷѝɼԂöϞιԂӪɻ~â',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ʐǍԏ¬ˤԂǓϓŠЮ˂Ң\x96ҊЅԉӭѬԋӢӋȧԍɲ˄¤ĿPӣÓ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ʸŁƾɲßįϣˤɺƧèʨɗͻƏцҭɈ\x86˂ȇ\x82ȌǷԟǊϒĲѤʋ',
                                                    },
                                    },
                            {
                                        'name': 'ӕˈ\x83Ʋ£¹ű±ҕӉüԐ\xadğɹˬTҫǠє',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            371895.1479612281,
                                                                            516144.5919038758,
                                                                            413891.3296070294,
                                                                            -11507.27949608666,
                                                                            800686.667021635,
                                                                            148985.86522493375,
                                                                            952622.6019771555,
                                                                            76139.70749957196,
                                                                            924866.9196330179,
                                                                            290640.67026982765,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ԓāJ\xadΕǝƫӛӨęɹɒЍˊ',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'Þχħ+ѰʢцEļҽɲιȰԐҿζˠȕϤæ΄ԢƙŞȄѤ\x8a$ȗƗ',
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': '\x89џԬiςҏΨэүͶПƾЕƚŒȚƻƮ϶ùʔ҅ԕɷó\x9cǗy¾ѿ',
                    'message': 'ƸˀŴļťʴϫvǍƹűː\x90žė\x94Ӑưә;ɴǪќĈɚȓ]ƾψѠ',
                    'arguments': [
                            {
                                        'name': 'ͻÞԛʋǖѯϰҽЬȜƈΠɎԟ҃ыԧӦдĸϼτ>rͷέəϫɼ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4415632455601107545,
                                                    },
                                    },
                            {
                                        'name': 'ԤǡϖͿͺĬԭč',
                                        'value': {
                                                        '^': 'string',
                                                        '$': 'ɴǒǙƶӐϒӛǗҨEʪŏ΅ȍ\x89ԍ×SГҹӒԕɮц\x90ӪŌҚͲҥ',
                                                    },
                                    },
                            {
                                        'name': 'ћśяʭίƨʇřˍT˖ȚҲ$ҏÝ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032124.944189:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ĳÊҫʑӘǦʛʬʸ"ΐ΅šǝǕɼvѼʑΧĄԁ˫Ù҅Êɖűͷǧ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 227274.50290314486,
                                                    },
                                    },
                            {
                                        'name': 'ƸɕɢèфϥʴӦƚϴԏʌѶŐчēˬɼХÌ',
                                        'value': {
                                                        '^': 'bool_list',
                                                        '$': [
                                                                            True,
                                                                            True,
                                                                            False,
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
                                        'name': 'êNүıАȈĎʎҢǍƓʶӕλжϘҋЙ\x98Ǩцɛ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032125.335014:+0000',
                                                    },
                                    },
                            {
                                        'name': 'ǌВΫö+ĘѢӶ\u0379ǅ`ƺŞ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -1164961954411135775,
                                                    },
                                    },
                            {
                                        'name': 'ƵβʘЧӐаɇˀѶαтăȸǦ²ǋ',
                                        'value': {
                                                        '^': 'datetime',
                                                        '$': '20210327:032125.475954:+0000',
                                                    },
                                    },
                            {
                                        'name': '˴ȥZǯǹ\x9fԏЩ҈\x98ŲУѳуѵʊǆҰΆҧȶɛĹ˝{ʖɩӛϨҟ',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            3075803609379795337,
                                                                            -6257558775869600216,
                                                                            7672970690557100060,
                                                                            -7207759626056455050,
                                                                            -6648531255846213248,
                                                                            2466979878999239000,
                                                                            -6339684293490702522,
                                                                            2522821807895188794,
                                                                            -4943316428628652368,
                                                                            -6524515408298336010,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĭĤȱɛѷвѺćą҅ġԬƪǺǏȓχ\x9bǐʻӡl¢ʹӎŹmӖʬû',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032125.799142:+0000',
                                                                            '20210327:032125.816110:+0000',
                                                                            '20210327:032125.833722:+0000',
                                                                            '20210327:032125.850977:+0000',
                                                                            '20210327:032125.869684:+0000',
                                                                            '20210327:032125.889128:+0000',
                                                                            '20210327:032125.906464:+0000',
                                                                            '20210327:032125.924502:+0000',
                                                                            '20210327:032125.942524:+0000',
                                                                            '20210327:032125.959513:+0000',
                                                                        ],
                                                    },
                                    },
                        ],
                },
                {
                    'catalog': 'ѵŴԈëǱЮʎgʩΘɭˎҠѳȎeчmѵ\x93ҌŅȹъǚ˹ВѲʑƎ',
                    'message': 'έΚðˣʜ{ԭǚš¾,ɶaˋԄ҉ЎƴгԡˡƓЧ³å˽ʨeϾǜ',
                    'arguments': [
                            {
                                        'name': '˅òʏҎ¸ϻzОǔ˯ɾȁqˌŋ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032126.130735:+0000',
                                                                            '20210327:032126.148950:+0000',
                                                                            '20210327:032126.167737:+0000',
                                                                            '20210327:032126.186599:+0000',
                                                                            '20210327:032126.205500:+0000',
                                                                            '20210327:032126.224678:+0000',
                                                                            '20210327:032126.244825:+0000',
                                                                            '20210327:032126.263598:+0000',
                                                                            '20210327:032126.281800:+0000',
                                                                            '20210327:032126.300633:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': '£Ĳʉƚ\x8cÅԐҁԗī·ʶδɈӈԇӜӦЦϳƉŵїң˭ȠʴɢƼ\x9b',
                                        'value': {
                                                        '^': 'bool',
                                                        '$': True,
                                                    },
                                    },
                            {
                                        'name': 'Ǫ˭\x85ȥ',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032126.472999:+0000',
                                                                            '20210327:032126.493221:+0000',
                                                                            '20210327:032126.512309:+0000',
                                                                            '20210327:032126.532184:+0000',
                                                                            '20210327:032126.552109:+0000',
                                                                            '20210327:032126.573839:+0000',
                                                                            '20210327:032126.593557:+0000',
                                                                            '20210327:032126.611003:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȓĬǂɏς͵ǣУьӄӥ¥ΦŗΞҮ=ǎų¥ƅҴȌ8ЧɅыÐТǒ',
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
                                                                            False,
                                                                            True,
                                                                            False,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ªʡʴђʸė҃ȫҬsӄ˾ŋ΅ȜĻǚЙÃƪ\x81ԋГŰҝɂǘʃɉΉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 98864.1083204468,
                                                    },
                                    },
                            {
                                        'name': 'ʤɎђԃɑĸ\x90,\x9aˊ˵ĿΝ˖ļȔϢàΎԆĆˇІȓ\u03a2Ɇʋгƨч',
                                        'value': {
                                                        '^': 'datetime_list',
                                                        '$': [
                                                                            '20210327:032127.017518:+0000',
                                                                            '20210327:032127.034443:+0000',
                                                                            '20210327:032127.051608:+0000',
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ȿƕɊòҾƲŀѲűȌѿ˘\x83ÃƠǨ[Īïͽ',
                                        'value': {
                                                        '^': 'int',
                                                        '$': -4381985392008125927,
                                                    },
                                    },
                            {
                                        'name': '˄jäȢ:Ɵά·кҴԗɂɕѷСʈԐɿҽƎϚγѠԩ[jǿҔƳ',
                                        'value': {
                                                        '^': 'float_list',
                                                        '$': [
                                                                            679319.6177969576,
                                                                            340268.9892935905,
                                                                            641126.1375288019,
                                                                            757552.1183190625,
                                                                            323420.4488239675,
                                                                            190211.01458192623,
                                                                            765308.4197456074,
                                                                            461903.2351244078,
                                                                            99117.01725403071,
                                                                            74797.51062316881,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ĞʷǸшǽӼûÿģΡ&ҳʐПðәζxԃȵ³ħϙΣ˼ͻ½',
                                        'value': {
                                                        '^': 'int_list',
                                                        '$': [
                                                                            -797206319597075505,
                                                                            7368487675622960025,
                                                                            1544917664412341703,
                                                                            -341859061738225139,
                                                                            2842451123286847096,
                                                                            -593268203332537722,
                                                                            -7136578621367313195,
                                                                            3523198449078832641,
                                                                            -8219881871425944015,
                                                                            -3932811435094621701,
                                                                        ],
                                                    },
                                    },
                            {
                                        'name': 'ƙƠĝʿʚыƙԇńӍďÝ˹ԈЀ˩ʢԇԋĿ҉Ͷĉ',
                                        'value': {
                                                        '^': 'float',
                                                        '$': 145773.65893857492,
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

            'identifier': 'óƊÉӟɪ',

            'categories': [
                'invalid-user-action',
            ],

            'messages': [
                {
                    'catalog': 'Ɯӝ',
                    'message': 'ä',
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
            'request_id': 1176171,
            'error': {
                'identifier': 'ɓҀ˹ЭƢӲд˅ŋȒɅǶʀЩ˗ԧȃ\x8bǧϕȏ҉ǒȁҸјԠҩýѷ',
                'categories': [
                    'network',
                ],
                'source': '˅Ϯ4ǉŶщҭϝƍp˛ңUėНӔЬȢԭȨчŶԣхǊɍҦӼɭǫ',
                'messages': [
                    {
                            'catalog': '8ɜҽčȄǛ˞kͳΗӡӺѬНѷRӧȌUĿɍҡƃːʃϧŐӜВ\x96',
                            'message': '(ҋҔƄјΆΘǥöНËŬΏʲĚҗȸìĉ˔;ň Ɲ²ӡ±ӎvɐ',
                            'arguments': [
                                        {
                                                        'name': 'țɾҵɪƇĝ3ϴԄž\x81ɞ2ʚΌȾЂ˦ѦϠ\x92ŜȵέĶӷϗΒʅӶ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 642255.1558751388,
                                                                        },
                                                    },
                                        {
                                                        'name': 'иЂȫ˟:ǛӤϋǲҮƧ²˚ԪʣΤɘɃÉӛӳ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӻϮ\x85ȜЋΔЌĞƬüʗϩÏϒҺсҎĊƌ\x95Đԅ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ѫȿ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2217702252193783179,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҳ\x9bԫ˗¬\x98ȇϮÖҀǸ\x8aΑˀųˠ˛³\x91Я',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'çñÈǬwԅъËʜȤќǹčӓæˈƝ`ɭ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 497361.56298712955,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x94bˈŭő\x97ƖÞɁӍșɴӮГǾѰχӒΖÖłѼȁɷϥ\x94ԧŻȲ\x84',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': "ӱВ\x8a7΄шiӕǛчƚĝѠҖƼ§Ǆ;řȄ_˸ȘѥɨϬȺӲ'ͻ",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԖӬҦϽč˼ǴĘϣɭƃɔԬ\x80ԐʙɞĲʗƤɅʗôƬʔ˓ŒЫɾʜ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜХКЈȯмƨ§Ėňê©ʹƪΊȼ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'õ©Ԯ\x90πǼ\x87²ѭǜ\u038dηǸ˟ÆʌϛφӗʂҼʫŪÐĔŻҟ҈ҢΗ',
                            'message': 'ƼȌǅ\x97ԃďŔϐж¢җʜȦªöɑÞɕȀѥӒƞäƗ˅ƚʅÕϵ%',
                            'arguments': [
                                        {
                                                        'name': 'ÇΠǤ˕Źұ˜',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '2ΰɱͱ.ǏƵ҇Ƀџ·ǒÅ\u038bɈͲȘη˱ӫɡʶԧҔͳĚȠρǽΝ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԧ˪ɣТͷ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032105.071357:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '5δàȨɽώʙŤҼʤӗϢвν\x97<ƾTоЪкʥç',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӛӯȩΔ˭ɆӅɦØҙǞȀӃӽɁйıӀˡƾŁʸзҔɢӂéӺгΌ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʹʫ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɜϨ*ϵÐÓҩϯοǩζΛȞѯѣθ(ԉiҷ˭ҀӐ\x9aƂÖȄЊӰ¯',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4136684154565551433,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɯ˽щȹѺϹʴƔғԔүŦˀ<ȑЙƾҜ\x88ŒԍɍʈQΕ¯ȕ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'фǈɯԛӦŚύǢιȥŲϫ˫\x8cԉҚӾΓƾǪЍŖΖԑ\x95ϓӮ ԌΆ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɐϯәʧǄӮ.4οĆЩĨŌҿϡӋϔӊίČșȗȽМǽ7ařКw',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032105.520434:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʔǂ΅˸ʹΚΏ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'Ãǌ˞ÂҏǂͶ˙˽ȏϻ˭Ȱн¾įҧ,b\x82ɩʓŻɐΓ3Õȡнġ',
                            'message': '·Ґʇϋґ\x80İɈƤphĉʍõϛѶүƷáϤЉӹӹԊʇϼŊ@ʷɤ',
                            'arguments': [
                                        {
                                                        'name': 'ȁ2˲ÀϤZγЉʦ]˷Ŋń\u038d6҅ҿВˊƇєԥŏǔҊΘˏΪƸȦ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 2994550234633484651,
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϠΜķοԤēƴǽԨԀŮȽːϣӽнʊñϨʅԗǷͼ˅ɐҖƊȓɴԜ',
                            'message': 'ͻӠxѤҘĚǮ¬ĺ8Ӝ£ıћɛʔБžŤϝʇΦМЃιǗ\x94ÆbǺ',
                            'arguments': [
                                        {
                                                        'name': 'Ȟхˏΰџɝ˃ØʏρÂӏˆßԚώԚʼзʦѰœɃĲϠÒжѻιų',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɩȑƽӲάƕxϻʘ\x89ğʡɊɲÆЄǒϦʫ˥ѮÆϹӭĈȕщŋȮß',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ηж!{Υ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'қԥɱȫΐʫʇЏʠύԙɰʀˀǪɜπ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'cҷΞҶËǤĸȕ˳ăҪϠђ˚ƹɴѼɼˉԃ½',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'õǑþƍяҏφΖsκsÿĵŌ˞˖ԌҨҗ1Ӽw±ʒ²ϺԏƋĩҦ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'іǉæȒЯфɜƗҔNǥĬѕÁŶ-Ѣŀғ\x91ҺҰªΕùǼӓǜ˸ū',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҝоâҤѣɀԜrзȷ\\şƮғвɳʵ΄ˉԏŊЗőɦҹϵàɂʵǶ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'oҀǅƚӒƖԥѐˊ\x9bñ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ЂҺάǘǭ|Tž\x97õïʱŏ+ˡƚĶRȨ±ŶSπ\x93ķҀ0ɞŹ\x98',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԒʚӺ\xa0',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'đŪźʺʹ8ѩѡӳǊϼΐxԖ\x86ԞїŬҵҰ˂ɷ~ûŹ£ΖѪm˦',
                            'message': 'ɥ@ĴдΑfђң˸ԈʅїɹǰɡËǙĖæŭȉŚǶɅԊНƖ˄Ʈτ',
                            'arguments': [
                                        {
                                                        'name': 'ȬԘҡβǏāhdʕˇΠԝȼƺĲ˸Эϑ-Ԣ\xa0Ӣʹзɂüǭт-Ԝ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӲϊĀˑǂ;őкҒĢȇԔ˺ӦгŶ:ĜʤŠѯĚì˅ɱj҆ʵІϚ',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӹ˒ʄŅҳҫƲмOɩ/ѕʌŲӇǥξȗ\x83PτȠԇǬцĽӳӃΥ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -3633573360485448351,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ˋĊ#ĘӛƿɄűԘƼɡа˛ʣӺČ˚\x91ԣǻѬɹ5\x94ΛџʔșbӼ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӈ\u0383ŭɫlòʒԢРнÛ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -731839486919529920,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʣɆʌÓҴ6˸Јǃ˜mʤ<ɔґēǬɤϹӳǑǦ¿',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҼӄĜŚԨ˅ùϾЭĽüϜȦҾѲΡѿҤǨÉǣϸʹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɣ\x8eÏŸȭƱ˟җźɭѫˡԨʀǄ˲ϛȳˢQʒӅ@ĶłɺĶĪ҈ő',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƬˇҀԆ\x8b\x93´ʔѧƱԌ˦ɪİȻԊ*ԧ\u0382ɥкӱϡ·čƬŬȿˊδ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -4761456612952035164,
                                                                        },
                                                    },
                                        {
                                                        'name': "\x8dǿˏƱԆŮñv'ͶЃѽǼӘƗҸE",
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ͷĆ$ǁĉɿȰĿüΔʝͿ¢ZŢvvӓʉ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϾƳŮӊʟ˾μÕԆèŏü΅ȫȉďàÛȚţХŇϱжĭҝ\u0380ʺėͳ',
                            'message': 'ǤÂ˙ǋԢʆFцǬȃΎƛ˶Ɵʘ¹űҸХŧñ˱κх˗öω÷ӎ˰',
                            'arguments': [
                                        {
                                                        'name': 'Ӳа½Ҿ«Ŋ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԍ˥\u0378_ɧőʘƨǅhƔ˗Ĳ˨',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҽϿς˵ŨûÜƋѯŬ\x96ҿȩȤ˟ȽʻȯŨĝѭ6\x9a/ʹԇǷƶоԙ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȔҏSƠА',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɸѣʛ:ΕſͼǕ΅Ŭ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '˲Ӹʪ˩ǍơĜДњ\x88ŏ˶ϥϸřқ6Ǝɘ¹ԍɇȭ°чϽcȄăğ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032107.908168:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȴŤʪӅŷȘAʒϝ££ӖӸÞǄЧѕĂʐƤʣʷÛȁϦдƳƐƍȃ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': '\x8bњ¡ƛ*(?Z˘>ӛωúĻsßЫąїƵ\x91ČԣЯV˩ʖµƜç',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ҫǫкƯЛΔˢɰǱүtp\x92',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ĜϠȌÛņԅ˭ăƚ¢Ў',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032108.120247:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '«ԑɳøϝɻºԬéĊό\x9cɱǣϾǹФϞJ\x91µϝ˶üƧǸĂǘ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'EΥɆdŃлӽȢȷ\x83ΙΟϯȦԑž҇Ȩĥόϝȧǒ˧]ƗƦɻû',
                            'message': 'ĐѳǺƾϕрӳԢЊдŞʋˌʈҗǶΊҵǗ҉śɛӀΎТėʰ\x89ƅӫ',
                            'arguments': [
                                        {
                                                        'name': 'ЂŗѥλӨǑ˩{ƀȃɞ¶\x95ǁÁˢцϟÉиƸ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 356096.0570248916,
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ê*ϲ˾Ɵɉ˶ȰƥjϛȷƌӫҗϤͽԍòşѩΠǖȄРÍ˞Ҏȋʐ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '×CƵʤγÉƟ\x7fҬ˜ЙΧԮͳϷѕѡ˷θҦęԥУԅȮʘÿѲӶƴ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ЍʟъνӑѪƛϒҥΔŉÜΖԆЋԙĽʝ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\x97ӫɻ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ȁƈέ\x9aԉșʕПԑЃúɢųΈӈŽkƮ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ΰǍȺțŹпʿƦ_ƌǱњɪΟνӴԊZǱĪҞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03825ӹӷΞðÃѧϹ\x8dǂҢʈȋҠȹϚΡʺƪȣ\x88ήƖͻˠҾŇψÓ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': -5554309788827678205,
                                                                        },
                                                    },
                                        {
                                                        'name': 'γчʪ\x9d˦Ǫͽ\u0380ǳƒǇPЊѓɲǤȋнĳЄ?Ǚʑ',
                                                        'value': {
                                                                            '^': 'int',
                                                                            '$': 6816202960291138290,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӏԨƉѤƎ*ъέӕѦԔĊ˻ȩŏԐƷʥɺɉЪȸҸΤɥÒТCԄɯ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ϐ·;º¯йÐЊ÷МȮŇЛĬț҇ʚǄŪӡ·ϫϘąŔǾ˥Ђϝǂ',
                            'message': 'ĸӰѽ˝˒ǳʳſϱԄ®ϻϩШԗңФ˶Ҽҥȵżɺ6ȫѺƼ˻ɠí',
                            'arguments': [
                                        {
                                                        'name': '®ί˾;Ą',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'źøΫНǞÀ\x9eϡį\\ǵÊŢҀǏǄ҈˩ҽɓǊӦɐɒΦǽѱʚǢ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032109.308108:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'Đ9лтCӽАįɲřǾZˮŎÐ}Ļ\x93ошςԭӮͰԊˌƃˁѬǵ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': False,
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɳӱȱƵ±rΡʚ"ȪӏǡʹĶƢλñѠǚØ҂Ɨ·ȿȇшƥéǫΠ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ƯǧȦιƜȨ\x89ËǪхˠ\x8a\u038dϹĩԌѳјʣɽR/½Ż\x84Ǳ',
                                                        'value': {
                                                                            '^': 'float_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϧǤRӿƙњƿƥ4Є΄Ȅɟ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ćЀ҈дɾȺЕ\x92Ǭȉ˕ǎʇˊ;ÎːªɆ@\x97ÞVìƊӯ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϐ˨ӟϔ Үɶ˂҅\x85ν΅сͼɮŎ\u0381уӠԗΔűøʼˣӬǄхԓƹ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ƒ\x95Ϊøŏ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǂ\u0380ȴ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ǲ¿şǛËѨáĢȵʓΑȳ˽Я˴ʭʌʺˋɺыÄǐџƴʯ0ӉőΞ',
                            'message': 'ѢϛцƬ˩ͼɨXыƯҞԣя\x9a¨ʣǋ£ñѳ2ʵϑɬ\x8dʡɪҲ˸ȯ',
                            'arguments': [
                                        {
                                                        'name': '˓ȹrѷɗ]½ԒӭϧȜѨǇ¬ӈÒòzʝнʊɏ\x90ű',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾ°Ԅ',
                                                        'value': {
                                                                            '^': 'bool',
                                                                            '$': True,
                                                                        },
                                                    },
                                        {
                                                        'name': '\u03a2ВҝѾʔªǧҌȶ,\u038dɔƿĐʈʽԇǗèťΧΙĄ΅˃ȆǌɠĤǤ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'Ԧӻ\x98\x86țУ1kǀӮŒΦʉƝǎŘɁӶȒėҧƬƹȓ˰τть˵\x8a',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɾӃŦԫȐ',
                                                        'value': {
                                                                            '^': 'string',
                                                                            '$': 'ӃʍÐ˺ƬʑЙɧ˻ҤƪǜƏ<ŕǯһӶЁǴʮ×ӤԑΛûÏПӜ0',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ǎΑ\u03a2Ġɚȸ\x92ôΦбœҽПϟњĨ6zƷЩґ˃ь´ӕɓέҮƉO',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'Ɩ\xadҳǣԜϡS°΅\u0381ǦʽɅΟΞƈŬþ^ǢSʪäřϟȺƻNӧˇ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032110.402708:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': '˹˒ȳÃҺɣ',
                                                        'value': {
                                                                            '^': 'datetime',
                                                                            '$': '20210327:032110.485202:+0000',
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɚˡӤҷÀ҇ɽ\\к',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϲҧΓ\x83\x95ĆɥϚ\x9d˟ǽˋӐ˨ŤӎӘˑȌŗЏˢӼñʸΚÀɖȗè',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 627229.5709237932,
                                                                        },
                                                    },
                                        {
                                                        'name': '\x89ʔԪΠǔОʅσҹÅPҦbʡӈ\x94ЀEѪЪԘΎnπ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                    ],
                        },
                    {
                            'catalog': 'ÔʼˊĆǊʹìˊƖDӦӀϫɫӗһɻƟʫҁêȖȌԗ\x92!\xa0ŃΊѴ',
                            'message': ' F\u0378ҪȵԐçӾõȣ>«\x91ϼĚσƚͰȈ8ˢƴѭµ\u0380ǪϮƚʿƌ',
                            'arguments': [
                                        {
                                                        'name': '³Àɖаƙ£\u0379Ûɬ˟˅¿ǙǷȮ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ɊˬxӯȑίƣˣюǆПŌ/ԄʰFԅҧÞͳ\x8eæѯȶҶ\x8aʑӃȬɞ',
                                                        'value': {
                                                                            '^': 'int_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ŵƗʉǒԞԂĿ°dƫLſ¿щѳ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'χȪʂЅˀPȔǕμΈ!ƵφñƠδςȢʢx˗зZĠŰćԐ˟Хδ',
                                                        'value': {
                                                                            '^': 'float',
                                                                            '$': 225238.54527301627,
                                                                        },
                                                    },
                                        {
                                                        'name': 'эΗ8ʡΓíʧýûĉφŀȊЎүҬ\x80ǕȏӳǙУҀԋČϟìў/Ƈ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ӄКƆϩ¾Ɯ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': '¢ӏȇˌȱƧͳˌÂцɄӊĳǽȰ\x81ˉµǭʈτϣ˳Ʉšȹ',
                                                        'value': {
                                                                            '^': 'datetime_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ʐƓͺĆ',
                                                        'value': {
                                                                            '^': 'string_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ϹʽƯΦ˱řϝӌȆÁ',
                                                        'value': {
                                                                            '^': 'bool_list',
                                                                            '$': [
                                                                                                ],
                                                                        },
                                                    },
                                        {
                                                        'name': 'ԊϧʍĠӱЗˀȺȞ×ԡʦЗǻӄĔͶɣЯίʝͶ\u03798җҴÆɜžμ',
                                                        'value': {
                                                                            '^': 'int_list',
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

            'request_id': 6839066,

            'error': {
                'identifier': 'ɾĶ\u0378ϸҚ',
                'categories': [
                    'network',
                ],
                'messages': [
                    {
                            'catalog': '˛Ƙ',
                            'message': '˻',
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
            'nw_x_pixel': -1638959363,
            'nw_y_pixel': 1387199932,
            'width': -8172235842476816635,
            'height': -3981563995087287549,
            'ratio_x': -4424381987293565218,
            'ratio_y': 6787899458700880311,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'nw_x_pixel': 1175258716,

            'nw_y_pixel': 1337205421,

            'width': -3872266614331882328,

            'height': -2543554441224435503,

            'ratio_x': 6953790632133459657,

            'ratio_y': -74665789350506961,

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
                    'nw_x_pixel': 1573356103,
                    'nw_y_pixel': 1303680961,
                    'width': -520932189587471113,
                    'height': -9010138210722449427,
                    'ratio_x': -1609881402102063054,
                    'ratio_y': 654610942068876245,
                },
                {
                    'nw_x_pixel': 923154476,
                    'nw_y_pixel': -1276455577,
                    'width': -2684679381228458837,
                    'height': -7639836078453180,
                    'ratio_x': 4247635775127416410,
                    'ratio_y': -2441377582844063873,
                },
                {
                    'nw_x_pixel': -330626891,
                    'nw_y_pixel': -1959247951,
                    'width': -5456002940743995500,
                    'height': -2722201023762659622,
                    'ratio_x': 2055283469494302473,
                    'ratio_y': -8845995651219709364,
                },
                {
                    'nw_x_pixel': 1166540084,
                    'nw_y_pixel': 1397478395,
                    'width': -652022310682951512,
                    'height': -7260872019129977967,
                    'ratio_x': 2611189015820648799,
                    'ratio_y': 6701662002952772062,
                },
                {
                    'nw_x_pixel': -97770872,
                    'nw_y_pixel': 58345751,
                    'width': -672944995123081281,
                    'height': -832129182120981676,
                    'ratio_x': -2556784006501325259,
                    'ratio_y': 1945487777538187871,
                },
                {
                    'nw_x_pixel': -1919381847,
                    'nw_y_pixel': -1548547820,
                    'width': -5193434557914998996,
                    'height': -8178303808950020892,
                    'ratio_x': -8587384107730255528,
                    'ratio_y': 529893808469623050,
                },
                {
                    'nw_x_pixel': 486708652,
                    'nw_y_pixel': 1164159670,
                    'width': -5674396172271041667,
                    'height': -5026454036550830404,
                    'ratio_x': 2922303965452811042,
                    'ratio_y': -3766571274570634741,
                },
                {
                    'nw_x_pixel': 1606563900,
                    'nw_y_pixel': -658781235,
                    'width': -3295429205831107981,
                    'height': -8051462481511239642,
                    'ratio_x': -6689411771632878064,
                    'ratio_y': -3664504132612015944,
                },
                {
                    'nw_x_pixel': -488861614,
                    'nw_y_pixel': -1259499794,
                    'width': -2714230695403763736,
                    'height': -8419016809013795705,
                    'ratio_x': 4220421256358657799,
                    'ratio_y': -4718092547742459145,
                },
                {
                    'nw_x_pixel': 1943960080,
                    'nw_y_pixel': 226191031,
                    'width': -5466963946368283576,
                    'height': -911815853492600773,
                    'ratio_x': -6661004242368094419,
                    'ratio_y': 6292784179527782411,
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
                    'description': 'Ѽ§ŲШϤʠӈÊÈľįǥşȏѳŤɧƿеηņȿԈʭǬɱĈƇҜƗ',
                    'monitors': [
                            {
                                        'identifier': 7161195,
                                        'width': -579036355287488594,
                                        'height': 5455717065243117993,
                                    },
                            {
                                        'identifier': -515113,
                                        'width': -1725576124904507586,
                                        'height': -6505167604500864560,
                                    },
                            {
                                        'identifier': 2902236,
                                        'width': 2284304133594917280,
                                        'height': 4853016424405243358,
                                    },
                            {
                                        'identifier': 1429847,
                                        'width': -4117267796640369179,
                                        'height': -6823329781872487071,
                                    },
                            {
                                        'identifier': 4932672,
                                        'width': -7662383544249653050,
                                        'height': -7527092388162726671,
                                    },
                            {
                                        'identifier': 8782815,
                                        'width': 215581914326690733,
                                        'height': 1694925341128012299,
                                    },
                            {
                                        'identifier': 3265466,
                                        'width': 6584323993151708077,
                                        'height': -1852973455796591018,
                                    },
                            {
                                        'identifier': 2586755,
                                        'width': 1537272447360889130,
                                        'height': 6503229081902292036,
                                    },
                            {
                                        'identifier': 9772672,
                                        'width': -7305133057807594706,
                                        'height': 8151416475369522567,
                                    },
                            {
                                        'identifier': 9331513,
                                        'width': 5007387239257171466,
                                        'height': -7556567755306401801,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6189771,
                                        'source_nw_x_pixel': -8153111154865105075,
                                        'source_nw_y_pixel': -3270845936143967986,
                                        'source_pixel_width': -1230282644648030685,
                                        'source_pixel_height': -6059526760773419988,
                                        'rotation': -4652722104842500087,
                                        'virtual_nw_x_pixel': -1997530242,
                                        'virtual_nw_y_pixel': -952061192,
                                        'virtual_width': -829278424,
                                        'virtual_height': 1497189481,
                                    },
                            {
                                        'source_monitor': 3211999,
                                        'source_nw_x_pixel': -4756053056310129406,
                                        'source_nw_y_pixel': -429459289691824083,
                                        'source_pixel_width': -627120245498934303,
                                        'source_pixel_height': -1052069187891453176,
                                        'rotation': -4964331220227355058,
                                        'virtual_nw_x_pixel': -1676913375,
                                        'virtual_nw_y_pixel': -48680828,
                                        'virtual_width': -534975029,
                                        'virtual_height': -584659324,
                                    },
                            {
                                        'source_monitor': 9209633,
                                        'source_nw_x_pixel': -1358222914939467933,
                                        'source_nw_y_pixel': -6682674793777540178,
                                        'source_pixel_width': -7953300823026783848,
                                        'source_pixel_height': -3661829065659042249,
                                        'rotation': -811667554970922876,
                                        'virtual_nw_x_pixel': 717066181,
                                        'virtual_nw_y_pixel': -1425274371,
                                        'virtual_width': -1753337078,
                                        'virtual_height': -902503877,
                                    },
                            {
                                        'source_monitor': 2416548,
                                        'source_nw_x_pixel': -3237026735180710336,
                                        'source_nw_y_pixel': -1022884662226740280,
                                        'source_pixel_width': -1563121578764081905,
                                        'source_pixel_height': -5880964127353714095,
                                        'rotation': -5950209650872304863,
                                        'virtual_nw_x_pixel': -1611696704,
                                        'virtual_nw_y_pixel': 673063780,
                                        'virtual_width': -1679083975,
                                        'virtual_height': -904228205,
                                    },
                            {
                                        'source_monitor': 4082885,
                                        'source_nw_x_pixel': -3324942279200715745,
                                        'source_nw_y_pixel': -1058529893904374678,
                                        'source_pixel_width': -5045843504710516517,
                                        'source_pixel_height': -8638214090075139372,
                                        'rotation': -633476455087536810,
                                        'virtual_nw_x_pixel': 60594324,
                                        'virtual_nw_y_pixel': -608513405,
                                        'virtual_width': 1278102836,
                                        'virtual_height': -919088734,
                                    },
                            {
                                        'source_monitor': 5371315,
                                        'source_nw_x_pixel': -3380333115582342204,
                                        'source_nw_y_pixel': -4571844750214213202,
                                        'source_pixel_width': -8515980128943593988,
                                        'source_pixel_height': -531484501159132697,
                                        'rotation': -7434505449963445422,
                                        'virtual_nw_x_pixel': 396255022,
                                        'virtual_nw_y_pixel': -861650079,
                                        'virtual_width': -1019353142,
                                        'virtual_height': 229497719,
                                    },
                            {
                                        'source_monitor': -192332,
                                        'source_nw_x_pixel': -1878713328191623492,
                                        'source_nw_y_pixel': -2039916388022131041,
                                        'source_pixel_width': -6571588384339755868,
                                        'source_pixel_height': -7587669806558924820,
                                        'rotation': -4238651921999479378,
                                        'virtual_nw_x_pixel': -1771472235,
                                        'virtual_nw_y_pixel': -628077544,
                                        'virtual_width': 107545224,
                                        'virtual_height': 1453756617,
                                    },
                            {
                                        'source_monitor': 9158720,
                                        'source_nw_x_pixel': -4453756741618179428,
                                        'source_nw_y_pixel': -3863245030018541269,
                                        'source_pixel_width': -7486475257791623823,
                                        'source_pixel_height': -8888772527389863820,
                                        'rotation': -1482900589080928874,
                                        'virtual_nw_x_pixel': -898769211,
                                        'virtual_nw_y_pixel': 1286732034,
                                        'virtual_width': 170640769,
                                        'virtual_height': 1502178977,
                                    },
                            {
                                        'source_monitor': 9306210,
                                        'source_nw_x_pixel': -2253016986007249487,
                                        'source_nw_y_pixel': -1727151861672954208,
                                        'source_pixel_width': -6946761629080201729,
                                        'source_pixel_height': -6087805023253340647,
                                        'rotation': -8259771706199923357,
                                        'virtual_nw_x_pixel': -972312763,
                                        'virtual_nw_y_pixel': -1910215597,
                                        'virtual_width': -1369537864,
                                        'virtual_height': -811511064,
                                    },
                            {
                                        'source_monitor': 8088283,
                                        'source_nw_x_pixel': -7329615159081354159,
                                        'source_nw_y_pixel': -8018367854133756049,
                                        'source_pixel_width': -352893221648962398,
                                        'source_pixel_height': -8715884829228401320,
                                        'rotation': -5312220247881398203,
                                        'virtual_nw_x_pixel': -1373645722,
                                        'virtual_nw_y_pixel': 1167620764,
                                        'virtual_width': -773157399,
                                        'virtual_height': 964105714,
                                    },
                        ],
                },
                {
                    'description': "ȅ'ţsӴԇԔŪǳ±ϕÓҮƤ\x9bě˒\x91ԣģςɹɏȋǧǥuĂ~s",
                    'monitors': [
                            {
                                        'identifier': -675834,
                                        'width': -3525659257533089161,
                                        'height': -144575659318908401,
                                    },
                            {
                                        'identifier': 119018,
                                        'width': -6316423379514513410,
                                        'height': -8411909382204796085,
                                    },
                            {
                                        'identifier': 1498396,
                                        'width': 1424853131554790652,
                                        'height': -5938770786862718602,
                                    },
                            {
                                        'identifier': 5019879,
                                        'width': -3321926763970039167,
                                        'height': -912479038857982126,
                                    },
                            {
                                        'identifier': 740411,
                                        'width': 4160340140845110009,
                                        'height': 7571227811310238847,
                                    },
                            {
                                        'identifier': 5397585,
                                        'width': -2154538118825851991,
                                        'height': -5128532364254153233,
                                    },
                            {
                                        'identifier': 7648717,
                                        'width': -4788271106671134846,
                                        'height': -7360125579026610301,
                                    },
                            {
                                        'identifier': 3320555,
                                        'width': 865770656363368443,
                                        'height': 8597323797291704873,
                                    },
                            {
                                        'identifier': 4899407,
                                        'width': 1792122202336066424,
                                        'height': -2853278205851416355,
                                    },
                            {
                                        'identifier': -957139,
                                        'width': -2468851583218969152,
                                        'height': 7348224810158628722,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2169902,
                                        'source_nw_x_pixel': -589170874576353127,
                                        'source_nw_y_pixel': -2324508406517567735,
                                        'source_pixel_width': -64310897328876466,
                                        'source_pixel_height': -6365781100209937207,
                                        'rotation': -4292712421963957218,
                                        'virtual_nw_x_pixel': -148812555,
                                        'virtual_nw_y_pixel': -1584606167,
                                        'virtual_width': 148965931,
                                        'virtual_height': 1510922035,
                                    },
                            {
                                        'source_monitor': -739023,
                                        'source_nw_x_pixel': -7602228057396665448,
                                        'source_nw_y_pixel': -2235883863200207471,
                                        'source_pixel_width': -1749046614573664711,
                                        'source_pixel_height': -4455023564838550844,
                                        'rotation': -7282894349200127252,
                                        'virtual_nw_x_pixel': 288634603,
                                        'virtual_nw_y_pixel': -892448691,
                                        'virtual_width': 1051316946,
                                        'virtual_height': -1791996842,
                                    },
                            {
                                        'source_monitor': -727813,
                                        'source_nw_x_pixel': -2786198232302892263,
                                        'source_nw_y_pixel': -4708639969595030777,
                                        'source_pixel_width': -4070883337618063727,
                                        'source_pixel_height': -3193459708426362252,
                                        'rotation': -540872971418149208,
                                        'virtual_nw_x_pixel': -117133357,
                                        'virtual_nw_y_pixel': 373096496,
                                        'virtual_width': -1544123053,
                                        'virtual_height': -230581415,
                                    },
                            {
                                        'source_monitor': 5825526,
                                        'source_nw_x_pixel': -4422524269422577248,
                                        'source_nw_y_pixel': -5850482450663960576,
                                        'source_pixel_width': -928400315696743845,
                                        'source_pixel_height': -8126610219631780630,
                                        'rotation': -5912611492167702115,
                                        'virtual_nw_x_pixel': 1359780373,
                                        'virtual_nw_y_pixel': 494405803,
                                        'virtual_width': -735115457,
                                        'virtual_height': 1958363173,
                                    },
                            {
                                        'source_monitor': 4696375,
                                        'source_nw_x_pixel': -1392929804931178065,
                                        'source_nw_y_pixel': -8833845122282998669,
                                        'source_pixel_width': -9223138614498742048,
                                        'source_pixel_height': -5478827327846606610,
                                        'rotation': -7768600890054986872,
                                        'virtual_nw_x_pixel': -983290882,
                                        'virtual_nw_y_pixel': -1669684305,
                                        'virtual_width': -993148060,
                                        'virtual_height': -1243367129,
                                    },
                            {
                                        'source_monitor': -507449,
                                        'source_nw_x_pixel': -4450218048366716966,
                                        'source_nw_y_pixel': -2782061059104837891,
                                        'source_pixel_width': -1418500785431518888,
                                        'source_pixel_height': -966981628629211547,
                                        'rotation': -8126567736650013945,
                                        'virtual_nw_x_pixel': 673912630,
                                        'virtual_nw_y_pixel': -763371690,
                                        'virtual_width': 404024467,
                                        'virtual_height': -1411541566,
                                    },
                            {
                                        'source_monitor': 1183234,
                                        'source_nw_x_pixel': -8315168733593253626,
                                        'source_nw_y_pixel': -7019150693900284014,
                                        'source_pixel_width': -5766724225911572989,
                                        'source_pixel_height': -7509803444750964427,
                                        'rotation': -8384233852696206998,
                                        'virtual_nw_x_pixel': 50721459,
                                        'virtual_nw_y_pixel': 1242872598,
                                        'virtual_width': 1596368194,
                                        'virtual_height': -1827934429,
                                    },
                            {
                                        'source_monitor': -696612,
                                        'source_nw_x_pixel': -4918546777539141347,
                                        'source_nw_y_pixel': -73854717993803564,
                                        'source_pixel_width': -217831004043037483,
                                        'source_pixel_height': -3845108506378584967,
                                        'rotation': -2068010064972822523,
                                        'virtual_nw_x_pixel': 287624721,
                                        'virtual_nw_y_pixel': 96617704,
                                        'virtual_width': 1993658354,
                                        'virtual_height': -1670884461,
                                    },
                            {
                                        'source_monitor': 4157244,
                                        'source_nw_x_pixel': -4733102225831943935,
                                        'source_nw_y_pixel': -8751738046338362486,
                                        'source_pixel_width': -8708325219402347625,
                                        'source_pixel_height': -5966075264683591079,
                                        'rotation': -962031251442164168,
                                        'virtual_nw_x_pixel': -746719974,
                                        'virtual_nw_y_pixel': 1370193544,
                                        'virtual_width': -762973598,
                                        'virtual_height': -1940808415,
                                    },
                            {
                                        'source_monitor': 6432293,
                                        'source_nw_x_pixel': -1048138083937730525,
                                        'source_nw_y_pixel': -7778398877119934277,
                                        'source_pixel_width': -3359123244106242668,
                                        'source_pixel_height': -3335357716865576767,
                                        'rotation': -7142685399148830494,
                                        'virtual_nw_x_pixel': 1885249015,
                                        'virtual_nw_y_pixel': 1563041806,
                                        'virtual_width': 1331933355,
                                        'virtual_height': 939500745,
                                    },
                        ],
                },
                {
                    'description': 'ĊôɈӇYȽ¡Ǻϵǔѽȿǉĵ˖ǖˌ\u0379ūΰ3łȁɒʓeȟĉ˄Ҏ',
                    'monitors': [
                            {
                                        'identifier': 5818158,
                                        'width': -2074423859808707278,
                                        'height': 8102059876077648007,
                                    },
                            {
                                        'identifier': 3811494,
                                        'width': 4405628555729334053,
                                        'height': -1503494818851016614,
                                    },
                            {
                                        'identifier': 4537315,
                                        'width': 5015743703096675881,
                                        'height': 8351466142682992938,
                                    },
                            {
                                        'identifier': 4366407,
                                        'width': -4757365089277162106,
                                        'height': -1200073830450773610,
                                    },
                            {
                                        'identifier': 8252459,
                                        'width': -665461288079184930,
                                        'height': 6742963656642423983,
                                    },
                            {
                                        'identifier': 5666455,
                                        'width': 5665041737039412775,
                                        'height': 2384126365389926648,
                                    },
                            {
                                        'identifier': 6969014,
                                        'width': 6901308040736541238,
                                        'height': 1509231827652088619,
                                    },
                            {
                                        'identifier': 8065170,
                                        'width': 7101571961356804929,
                                        'height': -901725530678905559,
                                    },
                            {
                                        'identifier': 3703827,
                                        'width': -5385424773918334896,
                                        'height': 519660953604776364,
                                    },
                            {
                                        'identifier': 7743770,
                                        'width': 6356311557790059152,
                                        'height': 2106092261477400069,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 8379673,
                                        'source_nw_x_pixel': -5473322269080528732,
                                        'source_nw_y_pixel': -8038521903919477247,
                                        'source_pixel_width': -1851297510386984183,
                                        'source_pixel_height': -8813313276239205119,
                                        'rotation': -6717182337965827235,
                                        'virtual_nw_x_pixel': -1189603092,
                                        'virtual_nw_y_pixel': -755666590,
                                        'virtual_width': -755177377,
                                        'virtual_height': 277312757,
                                    },
                            {
                                        'source_monitor': 7801972,
                                        'source_nw_x_pixel': -766538368939749489,
                                        'source_nw_y_pixel': -155665022910556185,
                                        'source_pixel_width': -5204439221258220886,
                                        'source_pixel_height': -3646981078132513786,
                                        'rotation': -6842947821858546393,
                                        'virtual_nw_x_pixel': 1717365237,
                                        'virtual_nw_y_pixel': -1338120233,
                                        'virtual_width': 1662613124,
                                        'virtual_height': 82316792,
                                    },
                            {
                                        'source_monitor': 5698766,
                                        'source_nw_x_pixel': -5080492846469315119,
                                        'source_nw_y_pixel': -8188424034316585793,
                                        'source_pixel_width': -1469975957684647229,
                                        'source_pixel_height': -7641897663137825831,
                                        'rotation': -1169883386643206602,
                                        'virtual_nw_x_pixel': -1060718087,
                                        'virtual_nw_y_pixel': -286466637,
                                        'virtual_width': -904670024,
                                        'virtual_height': -1540833059,
                                    },
                            {
                                        'source_monitor': -434052,
                                        'source_nw_x_pixel': -3254736731564052944,
                                        'source_nw_y_pixel': -8381754218407781277,
                                        'source_pixel_width': -8387926970453896336,
                                        'source_pixel_height': -6830439655881238935,
                                        'rotation': -1272770062698331225,
                                        'virtual_nw_x_pixel': -404000266,
                                        'virtual_nw_y_pixel': -263812179,
                                        'virtual_width': -1059751264,
                                        'virtual_height': 127818420,
                                    },
                            {
                                        'source_monitor': 2682802,
                                        'source_nw_x_pixel': -7507037970682647350,
                                        'source_nw_y_pixel': -3167061281973369525,
                                        'source_pixel_width': -4503950073720859902,
                                        'source_pixel_height': -171387041976454734,
                                        'rotation': -5837669909514215143,
                                        'virtual_nw_x_pixel': -1489357271,
                                        'virtual_nw_y_pixel': -19601717,
                                        'virtual_width': -1473606945,
                                        'virtual_height': -1007007928,
                                    },
                            {
                                        'source_monitor': 4943844,
                                        'source_nw_x_pixel': -7279888110346502720,
                                        'source_nw_y_pixel': -1307092337410012421,
                                        'source_pixel_width': -443061356704489808,
                                        'source_pixel_height': -7737119382383351546,
                                        'rotation': -2107085230499187224,
                                        'virtual_nw_x_pixel': -1320072102,
                                        'virtual_nw_y_pixel': -316079648,
                                        'virtual_width': -1150305901,
                                        'virtual_height': 599506257,
                                    },
                            {
                                        'source_monitor': 1507862,
                                        'source_nw_x_pixel': -2293419621561383287,
                                        'source_nw_y_pixel': -3282797286966759469,
                                        'source_pixel_width': -8489636428649277085,
                                        'source_pixel_height': -3332120174626074642,
                                        'rotation': -579513858197606253,
                                        'virtual_nw_x_pixel': -442137202,
                                        'virtual_nw_y_pixel': 1615194993,
                                        'virtual_width': -1335481289,
                                        'virtual_height': 88855550,
                                    },
                            {
                                        'source_monitor': 1341885,
                                        'source_nw_x_pixel': -6936408139210716253,
                                        'source_nw_y_pixel': -5056580001076724889,
                                        'source_pixel_width': -4343690875235229559,
                                        'source_pixel_height': -4136550827063250763,
                                        'rotation': -9081140074643101268,
                                        'virtual_nw_x_pixel': -328755251,
                                        'virtual_nw_y_pixel': -546347341,
                                        'virtual_width': -467787528,
                                        'virtual_height': 736979197,
                                    },
                            {
                                        'source_monitor': 8642286,
                                        'source_nw_x_pixel': -4516266503002059712,
                                        'source_nw_y_pixel': -2711543380897920965,
                                        'source_pixel_width': -4366693797596392910,
                                        'source_pixel_height': -2900657470492999073,
                                        'rotation': -4413364929032905476,
                                        'virtual_nw_x_pixel': -788405396,
                                        'virtual_nw_y_pixel': 966458758,
                                        'virtual_width': 1126485067,
                                        'virtual_height': -865433697,
                                    },
                            {
                                        'source_monitor': 9062079,
                                        'source_nw_x_pixel': -3687724765611974224,
                                        'source_nw_y_pixel': -6790620910053092559,
                                        'source_pixel_width': -3396198636588658608,
                                        'source_pixel_height': -4396438377344907009,
                                        'rotation': -407147293049103729,
                                        'virtual_nw_x_pixel': -1510598497,
                                        'virtual_nw_y_pixel': 298018479,
                                        'virtual_width': -1535971631,
                                        'virtual_height': 574676259,
                                    },
                        ],
                },
                {
                    'description': 'ѕшԡWŌôηǐϡƏ˺ŬȺǭȟΘιέϾʈʔмĝͿĺţǘѴ#ź',
                    'monitors': [
                            {
                                        'identifier': 4827752,
                                        'width': 57300563986268429,
                                        'height': 6202801606197204061,
                                    },
                            {
                                        'identifier': 9108347,
                                        'width': 6138434716899589722,
                                        'height': 6741830383434715515,
                                    },
                            {
                                        'identifier': 2848386,
                                        'width': 587326568898061966,
                                        'height': 8244972639101552205,
                                    },
                            {
                                        'identifier': 5797191,
                                        'width': -7143235579464021961,
                                        'height': 5974784370287601889,
                                    },
                            {
                                        'identifier': 7236651,
                                        'width': -2433820440923701137,
                                        'height': -5495874956932623288,
                                    },
                            {
                                        'identifier': 4491012,
                                        'width': 1959343723866812775,
                                        'height': -3569216538477412294,
                                    },
                            {
                                        'identifier': 627609,
                                        'width': -9044388468411842310,
                                        'height': 1732645162466158513,
                                    },
                            {
                                        'identifier': 2498635,
                                        'width': 1398181358656251331,
                                        'height': 3135806368359867077,
                                    },
                            {
                                        'identifier': -14403,
                                        'width': 7754839258007212389,
                                        'height': -405187325380120389,
                                    },
                            {
                                        'identifier': 6001702,
                                        'width': -2941355853458978702,
                                        'height': 2748684165346816438,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 2322988,
                                        'source_nw_x_pixel': -1735557294689772700,
                                        'source_nw_y_pixel': -2298525032961694625,
                                        'source_pixel_width': -388192229280037658,
                                        'source_pixel_height': -3849050822577248247,
                                        'rotation': -8123795876591650104,
                                        'virtual_nw_x_pixel': -1364217974,
                                        'virtual_nw_y_pixel': -1208596400,
                                        'virtual_width': -322692357,
                                        'virtual_height': -1944884519,
                                    },
                            {
                                        'source_monitor': 5709129,
                                        'source_nw_x_pixel': -6585263224891002043,
                                        'source_nw_y_pixel': -2590265335639212733,
                                        'source_pixel_width': -3231807019896432043,
                                        'source_pixel_height': -1854141917582708680,
                                        'rotation': -8126992310582509742,
                                        'virtual_nw_x_pixel': 368269956,
                                        'virtual_nw_y_pixel': 575456453,
                                        'virtual_width': 554718714,
                                        'virtual_height': -126261525,
                                    },
                            {
                                        'source_monitor': 623578,
                                        'source_nw_x_pixel': -1519589035240185434,
                                        'source_nw_y_pixel': -5785784739600570499,
                                        'source_pixel_width': -629489879508331803,
                                        'source_pixel_height': -2617474012847774091,
                                        'rotation': -674281573386979760,
                                        'virtual_nw_x_pixel': -475713725,
                                        'virtual_nw_y_pixel': -978842499,
                                        'virtual_width': 1039250017,
                                        'virtual_height': -120639287,
                                    },
                            {
                                        'source_monitor': 3814287,
                                        'source_nw_x_pixel': -2529983263190037200,
                                        'source_nw_y_pixel': -4675493868810345291,
                                        'source_pixel_width': -5605288435140994227,
                                        'source_pixel_height': -8873274864602839035,
                                        'rotation': -4187940892119503742,
                                        'virtual_nw_x_pixel': -769429388,
                                        'virtual_nw_y_pixel': -1666183176,
                                        'virtual_width': 1205682848,
                                        'virtual_height': 1873740623,
                                    },
                            {
                                        'source_monitor': 5970301,
                                        'source_nw_x_pixel': -6260486629676915858,
                                        'source_nw_y_pixel': -856668826652155662,
                                        'source_pixel_width': -2893977887714635899,
                                        'source_pixel_height': -408226679915102847,
                                        'rotation': -6423401506851227044,
                                        'virtual_nw_x_pixel': 1088360106,
                                        'virtual_nw_y_pixel': -1964888051,
                                        'virtual_width': 207127204,
                                        'virtual_height': 1931914770,
                                    },
                            {
                                        'source_monitor': 5270520,
                                        'source_nw_x_pixel': -4242342419471087245,
                                        'source_nw_y_pixel': -2588143702577000644,
                                        'source_pixel_width': -7405132599499222901,
                                        'source_pixel_height': -37002608424567311,
                                        'rotation': -950809998452144469,
                                        'virtual_nw_x_pixel': -396744354,
                                        'virtual_nw_y_pixel': 1922018916,
                                        'virtual_width': -1220911081,
                                        'virtual_height': -200557357,
                                    },
                            {
                                        'source_monitor': 9225802,
                                        'source_nw_x_pixel': -3304848160669457185,
                                        'source_nw_y_pixel': -8056381758904823139,
                                        'source_pixel_width': -4063943432514284780,
                                        'source_pixel_height': -8429264384571461709,
                                        'rotation': -4965408352384075279,
                                        'virtual_nw_x_pixel': 612781827,
                                        'virtual_nw_y_pixel': 1821899326,
                                        'virtual_width': 1912315339,
                                        'virtual_height': -427192646,
                                    },
                            {
                                        'source_monitor': 236815,
                                        'source_nw_x_pixel': -4880963913526283778,
                                        'source_nw_y_pixel': -3602309911363485975,
                                        'source_pixel_width': -4317591171251371838,
                                        'source_pixel_height': -2648524467636474193,
                                        'rotation': -7856866387605338512,
                                        'virtual_nw_x_pixel': -1121030843,
                                        'virtual_nw_y_pixel': -1977375627,
                                        'virtual_width': -1680146909,
                                        'virtual_height': -1640772361,
                                    },
                            {
                                        'source_monitor': 2984361,
                                        'source_nw_x_pixel': -3016353112490623828,
                                        'source_nw_y_pixel': -8087715280009856060,
                                        'source_pixel_width': -4279406310901434763,
                                        'source_pixel_height': -7031838593575385169,
                                        'rotation': -7381172746742518693,
                                        'virtual_nw_x_pixel': -835966443,
                                        'virtual_nw_y_pixel': 22257417,
                                        'virtual_width': 1473786615,
                                        'virtual_height': -1234654359,
                                    },
                            {
                                        'source_monitor': 2158994,
                                        'source_nw_x_pixel': -6085317429564910771,
                                        'source_nw_y_pixel': -5311561622690672067,
                                        'source_pixel_width': -4057820941207640449,
                                        'source_pixel_height': -5070176006237481634,
                                        'rotation': -6863272304242950892,
                                        'virtual_nw_x_pixel': -288118284,
                                        'virtual_nw_y_pixel': 430042889,
                                        'virtual_width': 1516784679,
                                        'virtual_height': 920701464,
                                    },
                        ],
                },
                {
                    'description': 'ҶũνˌҎ˘nɨ®ÖЁˋΫi§ā;ϻЙNԛȷ«ȜΉ~ʛέɆͷ',
                    'monitors': [
                            {
                                        'identifier': -918111,
                                        'width': -1724252393689692576,
                                        'height': -4827235161986188573,
                                    },
                            {
                                        'identifier': 4223563,
                                        'width': 8928933498146754133,
                                        'height': 3868734432032133967,
                                    },
                            {
                                        'identifier': 8607566,
                                        'width': 6971638632412481438,
                                        'height': 8879415390849276167,
                                    },
                            {
                                        'identifier': 9703570,
                                        'width': 1406644051556906962,
                                        'height': 555560711496639904,
                                    },
                            {
                                        'identifier': 7273238,
                                        'width': 6446768284060922116,
                                        'height': -1252641907471192405,
                                    },
                            {
                                        'identifier': 4427882,
                                        'width': 5524863221280230116,
                                        'height': -9040655618642964215,
                                    },
                            {
                                        'identifier': 7086500,
                                        'width': 7268579134120203115,
                                        'height': -5835379131475838913,
                                    },
                            {
                                        'identifier': 1637600,
                                        'width': -1416677595362485632,
                                        'height': 5433366935542348610,
                                    },
                            {
                                        'identifier': 7244043,
                                        'width': 4502073604922651713,
                                        'height': -3877468710951499789,
                                    },
                            {
                                        'identifier': 9769103,
                                        'width': 370706703544513463,
                                        'height': 7351902074364130056,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 823880,
                                        'source_nw_x_pixel': -7451633657307493084,
                                        'source_nw_y_pixel': -4063733977920970090,
                                        'source_pixel_width': -7093544835277960908,
                                        'source_pixel_height': -8582479227012025787,
                                        'rotation': -7303610068272231109,
                                        'virtual_nw_x_pixel': 434061562,
                                        'virtual_nw_y_pixel': 507538556,
                                        'virtual_width': 1518427378,
                                        'virtual_height': 1022717252,
                                    },
                            {
                                        'source_monitor': 4832700,
                                        'source_nw_x_pixel': -8952917812007473232,
                                        'source_nw_y_pixel': -8539822755995283053,
                                        'source_pixel_width': -3315171865360755894,
                                        'source_pixel_height': -7148537735844318845,
                                        'rotation': -8084884763434856023,
                                        'virtual_nw_x_pixel': -46285731,
                                        'virtual_nw_y_pixel': 1537171149,
                                        'virtual_width': 1141767717,
                                        'virtual_height': 427921606,
                                    },
                            {
                                        'source_monitor': 7963749,
                                        'source_nw_x_pixel': -3134438710026211652,
                                        'source_nw_y_pixel': -3167608712697427873,
                                        'source_pixel_width': -5106148869017461295,
                                        'source_pixel_height': -771545502344612576,
                                        'rotation': -5900856639204819387,
                                        'virtual_nw_x_pixel': 1090798317,
                                        'virtual_nw_y_pixel': -1820240097,
                                        'virtual_width': -850525041,
                                        'virtual_height': 906811135,
                                    },
                            {
                                        'source_monitor': 1678514,
                                        'source_nw_x_pixel': -3374540516721882111,
                                        'source_nw_y_pixel': -4335235156392002903,
                                        'source_pixel_width': -4202186144933662093,
                                        'source_pixel_height': -213032059980607060,
                                        'rotation': -2707908744720261300,
                                        'virtual_nw_x_pixel': -51686735,
                                        'virtual_nw_y_pixel': -150964828,
                                        'virtual_width': 1300332007,
                                        'virtual_height': -1101408004,
                                    },
                            {
                                        'source_monitor': 799260,
                                        'source_nw_x_pixel': -2422741113422479303,
                                        'source_nw_y_pixel': -1017984916909823942,
                                        'source_pixel_width': -7150451706315679968,
                                        'source_pixel_height': -1563632056166515287,
                                        'rotation': -1205503467699103929,
                                        'virtual_nw_x_pixel': 1552537895,
                                        'virtual_nw_y_pixel': 1885375380,
                                        'virtual_width': 976655607,
                                        'virtual_height': -980694878,
                                    },
                            {
                                        'source_monitor': 4515107,
                                        'source_nw_x_pixel': -3379850131315461775,
                                        'source_nw_y_pixel': -3738086154387719878,
                                        'source_pixel_width': -8406599313828969855,
                                        'source_pixel_height': -5899356518243162373,
                                        'rotation': -3225520638695042116,
                                        'virtual_nw_x_pixel': 746147817,
                                        'virtual_nw_y_pixel': -1365288348,
                                        'virtual_width': 1357735854,
                                        'virtual_height': 282970761,
                                    },
                            {
                                        'source_monitor': 1467719,
                                        'source_nw_x_pixel': -1104278208793698900,
                                        'source_nw_y_pixel': -7579648272705458184,
                                        'source_pixel_width': -3962158163033585097,
                                        'source_pixel_height': -5464039371737913431,
                                        'rotation': -2261595424208184538,
                                        'virtual_nw_x_pixel': 1945750289,
                                        'virtual_nw_y_pixel': -1277452502,
                                        'virtual_width': -1324886936,
                                        'virtual_height': 1785335247,
                                    },
                            {
                                        'source_monitor': 6464715,
                                        'source_nw_x_pixel': -5926751014474320493,
                                        'source_nw_y_pixel': -2980445343791453818,
                                        'source_pixel_width': -5415376838281642449,
                                        'source_pixel_height': -1425293610422868321,
                                        'rotation': -3390447942234923380,
                                        'virtual_nw_x_pixel': -1020092032,
                                        'virtual_nw_y_pixel': 328903598,
                                        'virtual_width': -1541286568,
                                        'virtual_height': 1690736158,
                                    },
                            {
                                        'source_monitor': 4485478,
                                        'source_nw_x_pixel': -4130048881203262435,
                                        'source_nw_y_pixel': -614434632807629179,
                                        'source_pixel_width': -4375907403631760326,
                                        'source_pixel_height': -3221563731993367859,
                                        'rotation': -9070832681212011152,
                                        'virtual_nw_x_pixel': 42085365,
                                        'virtual_nw_y_pixel': 942966260,
                                        'virtual_width': 1479620045,
                                        'virtual_height': -272130815,
                                    },
                            {
                                        'source_monitor': 5851180,
                                        'source_nw_x_pixel': -7335549962774425212,
                                        'source_nw_y_pixel': -2212246105826058875,
                                        'source_pixel_width': -5442696584496338041,
                                        'source_pixel_height': -445682865799200281,
                                        'rotation': -4238760831902584929,
                                        'virtual_nw_x_pixel': -1485245518,
                                        'virtual_nw_y_pixel': -1926397415,
                                        'virtual_width': -1851973948,
                                        'virtual_height': -1920604233,
                                    },
                        ],
                },
                {
                    'description': 'ϳ#ǭlѬń9˔εǞͲŠҩМĸ/ĀȹȻʒƧǷӢQ2Øѓ\x9foҡ',
                    'monitors': [
                            {
                                        'identifier': -42117,
                                        'width': -5525244540941500478,
                                        'height': -480573764208052633,
                                    },
                            {
                                        'identifier': 9763275,
                                        'width': -5880782479058934370,
                                        'height': -8389463471403501527,
                                    },
                            {
                                        'identifier': 4434789,
                                        'width': -5439911030119523254,
                                        'height': -7064984939317202817,
                                    },
                            {
                                        'identifier': 2650439,
                                        'width': 8100032437059708549,
                                        'height': -8107920629255598087,
                                    },
                            {
                                        'identifier': 3342552,
                                        'width': -1054268938037946918,
                                        'height': -7949635965087386142,
                                    },
                            {
                                        'identifier': 771735,
                                        'width': -1811284927670742116,
                                        'height': -8420438069944740540,
                                    },
                            {
                                        'identifier': 1369440,
                                        'width': -6932004430428920613,
                                        'height': 7396592106604429080,
                                    },
                            {
                                        'identifier': 7743543,
                                        'width': -1214172929680964836,
                                        'height': -459360623602052095,
                                    },
                            {
                                        'identifier': 3958296,
                                        'width': -3345251742712229014,
                                        'height': 8958288085071315638,
                                    },
                            {
                                        'identifier': 4328101,
                                        'width': 6354437946456379285,
                                        'height': -5002061487978492056,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5294926,
                                        'source_nw_x_pixel': -6407413144089234009,
                                        'source_nw_y_pixel': -2763945567981894783,
                                        'source_pixel_width': -3126118243536915877,
                                        'source_pixel_height': -5175816533232873492,
                                        'rotation': -3300696712410036199,
                                        'virtual_nw_x_pixel': 902031217,
                                        'virtual_nw_y_pixel': -1283533017,
                                        'virtual_width': -247429024,
                                        'virtual_height': -556767735,
                                    },
                            {
                                        'source_monitor': 7768027,
                                        'source_nw_x_pixel': -2738117314255997130,
                                        'source_nw_y_pixel': -3935669461854120053,
                                        'source_pixel_width': -4777453881256518675,
                                        'source_pixel_height': -7479753919346476868,
                                        'rotation': -6184476386111921751,
                                        'virtual_nw_x_pixel': 959266528,
                                        'virtual_nw_y_pixel': -1519721927,
                                        'virtual_width': 1143493140,
                                        'virtual_height': 1056288283,
                                    },
                            {
                                        'source_monitor': 6531340,
                                        'source_nw_x_pixel': -2835630360627743616,
                                        'source_nw_y_pixel': -2451264353158682185,
                                        'source_pixel_width': -5128525797985499122,
                                        'source_pixel_height': -2025430536852684281,
                                        'rotation': -2949732662844162615,
                                        'virtual_nw_x_pixel': -1991441629,
                                        'virtual_nw_y_pixel': -607780092,
                                        'virtual_width': 1903513655,
                                        'virtual_height': 1124623747,
                                    },
                            {
                                        'source_monitor': 2037438,
                                        'source_nw_x_pixel': -4935354213698152316,
                                        'source_nw_y_pixel': -8298165168331141617,
                                        'source_pixel_width': -6869126796560317877,
                                        'source_pixel_height': -2129623347605534900,
                                        'rotation': -3782593229431204528,
                                        'virtual_nw_x_pixel': -1954952424,
                                        'virtual_nw_y_pixel': -867187843,
                                        'virtual_width': 941020200,
                                        'virtual_height': -1186330114,
                                    },
                            {
                                        'source_monitor': 7253842,
                                        'source_nw_x_pixel': -1886005092958355126,
                                        'source_nw_y_pixel': -7844384151308505830,
                                        'source_pixel_width': -2689889422983397189,
                                        'source_pixel_height': -9136152214798212628,
                                        'rotation': -3689673658473645844,
                                        'virtual_nw_x_pixel': 477079102,
                                        'virtual_nw_y_pixel': -944561335,
                                        'virtual_width': 1914138193,
                                        'virtual_height': 40226420,
                                    },
                            {
                                        'source_monitor': 2680396,
                                        'source_nw_x_pixel': -8950027919052898047,
                                        'source_nw_y_pixel': -9119392352409005002,
                                        'source_pixel_width': -1563858181886212676,
                                        'source_pixel_height': -3082420575726725003,
                                        'rotation': -7919756076425168950,
                                        'virtual_nw_x_pixel': -341292116,
                                        'virtual_nw_y_pixel': 1895200427,
                                        'virtual_width': -1021457115,
                                        'virtual_height': 1258397947,
                                    },
                            {
                                        'source_monitor': 2921383,
                                        'source_nw_x_pixel': -3093874547413513236,
                                        'source_nw_y_pixel': -269633158727775633,
                                        'source_pixel_width': -4816263778341377504,
                                        'source_pixel_height': -3036579423523707217,
                                        'rotation': -1401563359954068229,
                                        'virtual_nw_x_pixel': 49744122,
                                        'virtual_nw_y_pixel': -1490655031,
                                        'virtual_width': 1835714267,
                                        'virtual_height': 1718180872,
                                    },
                            {
                                        'source_monitor': 1506199,
                                        'source_nw_x_pixel': -4094763162648630405,
                                        'source_nw_y_pixel': -4731613570325509116,
                                        'source_pixel_width': -4045257293104744090,
                                        'source_pixel_height': -3929547589652283455,
                                        'rotation': -914766963952041534,
                                        'virtual_nw_x_pixel': 601232832,
                                        'virtual_nw_y_pixel': -1776675623,
                                        'virtual_width': -1051734729,
                                        'virtual_height': 1723705295,
                                    },
                            {
                                        'source_monitor': 8078137,
                                        'source_nw_x_pixel': -4588048285810468058,
                                        'source_nw_y_pixel': -8094468153798883899,
                                        'source_pixel_width': -6867308886011153339,
                                        'source_pixel_height': -461953898430933356,
                                        'rotation': -619999848311092375,
                                        'virtual_nw_x_pixel': 465022602,
                                        'virtual_nw_y_pixel': 342528321,
                                        'virtual_width': 1776933234,
                                        'virtual_height': 91150639,
                                    },
                            {
                                        'source_monitor': 8350290,
                                        'source_nw_x_pixel': -4948305518705606470,
                                        'source_nw_y_pixel': -1371362162014050040,
                                        'source_pixel_width': -6909926744110022151,
                                        'source_pixel_height': -3488076514212591384,
                                        'rotation': -6167594355846087079,
                                        'virtual_nw_x_pixel': 678925696,
                                        'virtual_nw_y_pixel': 623258160,
                                        'virtual_width': 753074111,
                                        'virtual_height': -38306649,
                                    },
                        ],
                },
                {
                    'description': 'ʪÏİЌԌȚȥѠǨ`ȉѐɊЉЫϡΑѸʚˈѱğРѱɦ\\ĕVѐ\x81',
                    'monitors': [
                            {
                                        'identifier': 6766569,
                                        'width': -1789176007618005249,
                                        'height': 5780255745747936000,
                                    },
                            {
                                        'identifier': 1623058,
                                        'width': -3409241728076265401,
                                        'height': 4009805571276816605,
                                    },
                            {
                                        'identifier': 7110536,
                                        'width': -8101925090118239337,
                                        'height': 7513709089607055917,
                                    },
                            {
                                        'identifier': 7175458,
                                        'width': 984218858968089108,
                                        'height': 8455765056854050365,
                                    },
                            {
                                        'identifier': -778126,
                                        'width': -2793480849304437433,
                                        'height': -5393862693777852758,
                                    },
                            {
                                        'identifier': 6698636,
                                        'width': 1858752906656438290,
                                        'height': -5497960240274017141,
                                    },
                            {
                                        'identifier': 4107419,
                                        'width': -7634091301870257036,
                                        'height': 26516426624969288,
                                    },
                            {
                                        'identifier': 7727659,
                                        'width': -6867735012027634762,
                                        'height': -5063867516462659005,
                                    },
                            {
                                        'identifier': 6305103,
                                        'width': 832521767863933420,
                                        'height': 6324372895779180106,
                                    },
                            {
                                        'identifier': 6849075,
                                        'width': 3759234885237293124,
                                        'height': 492948251316984578,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 6283436,
                                        'source_nw_x_pixel': -8777771210701229139,
                                        'source_nw_y_pixel': -285408687806487473,
                                        'source_pixel_width': -6382778752890475903,
                                        'source_pixel_height': -5788409774807493276,
                                        'rotation': -1515213559823656249,
                                        'virtual_nw_x_pixel': 1946347339,
                                        'virtual_nw_y_pixel': 1643349549,
                                        'virtual_width': 1734989720,
                                        'virtual_height': 213081331,
                                    },
                            {
                                        'source_monitor': 6745207,
                                        'source_nw_x_pixel': -1301737875926777840,
                                        'source_nw_y_pixel': -927513255954055375,
                                        'source_pixel_width': -4624486524976908615,
                                        'source_pixel_height': -815738611955831142,
                                        'rotation': -1899257613697025848,
                                        'virtual_nw_x_pixel': 1329596976,
                                        'virtual_nw_y_pixel': -1416916995,
                                        'virtual_width': -1388985479,
                                        'virtual_height': 1908639155,
                                    },
                            {
                                        'source_monitor': 4013710,
                                        'source_nw_x_pixel': -1194981455918574413,
                                        'source_nw_y_pixel': -3658889574043491806,
                                        'source_pixel_width': -1409078637424097749,
                                        'source_pixel_height': -8296293642600584524,
                                        'rotation': -6901368390538588824,
                                        'virtual_nw_x_pixel': 1620418065,
                                        'virtual_nw_y_pixel': 563039563,
                                        'virtual_width': 1021943525,
                                        'virtual_height': -623152163,
                                    },
                            {
                                        'source_monitor': -410092,
                                        'source_nw_x_pixel': -7795662084376686585,
                                        'source_nw_y_pixel': -2790452208449500835,
                                        'source_pixel_width': -2985036888163145888,
                                        'source_pixel_height': -6993196257841777624,
                                        'rotation': -4447273025815345466,
                                        'virtual_nw_x_pixel': 412277915,
                                        'virtual_nw_y_pixel': -1010928798,
                                        'virtual_width': -1941426806,
                                        'virtual_height': -702772830,
                                    },
                            {
                                        'source_monitor': 2633942,
                                        'source_nw_x_pixel': -2289302019119799991,
                                        'source_nw_y_pixel': -2305233834703109755,
                                        'source_pixel_width': -2112915209568424284,
                                        'source_pixel_height': -1749079069005450460,
                                        'rotation': -6874888313837561261,
                                        'virtual_nw_x_pixel': 1700497298,
                                        'virtual_nw_y_pixel': 637572792,
                                        'virtual_width': 765896013,
                                        'virtual_height': -456537917,
                                    },
                            {
                                        'source_monitor': 6041324,
                                        'source_nw_x_pixel': -9148002209130408402,
                                        'source_nw_y_pixel': -7321463284658036091,
                                        'source_pixel_width': -8545440983030130847,
                                        'source_pixel_height': -1972398274234819168,
                                        'rotation': -1362356139088276460,
                                        'virtual_nw_x_pixel': 85082819,
                                        'virtual_nw_y_pixel': -1996289286,
                                        'virtual_width': 235190701,
                                        'virtual_height': -964392401,
                                    },
                            {
                                        'source_monitor': 3440294,
                                        'source_nw_x_pixel': -49059325551539556,
                                        'source_nw_y_pixel': -6426355711026103780,
                                        'source_pixel_width': -8633995192759136186,
                                        'source_pixel_height': -4448091124999075481,
                                        'rotation': -1132161942843579435,
                                        'virtual_nw_x_pixel': -607894848,
                                        'virtual_nw_y_pixel': -1584640157,
                                        'virtual_width': 406928089,
                                        'virtual_height': -589933407,
                                    },
                            {
                                        'source_monitor': 8851820,
                                        'source_nw_x_pixel': -5409556522727527334,
                                        'source_nw_y_pixel': -7506999017266227605,
                                        'source_pixel_width': -7158970550412608615,
                                        'source_pixel_height': -3408137389310177750,
                                        'rotation': -8272393275463162286,
                                        'virtual_nw_x_pixel': -1192091952,
                                        'virtual_nw_y_pixel': 777608511,
                                        'virtual_width': 304260037,
                                        'virtual_height': -185745841,
                                    },
                            {
                                        'source_monitor': -195885,
                                        'source_nw_x_pixel': -2393734575266059099,
                                        'source_nw_y_pixel': -6140176010740357445,
                                        'source_pixel_width': -5138992293395501883,
                                        'source_pixel_height': -9146562178766614328,
                                        'rotation': -3590468725605013774,
                                        'virtual_nw_x_pixel': -1791910589,
                                        'virtual_nw_y_pixel': -1635456864,
                                        'virtual_width': 294968444,
                                        'virtual_height': 203332574,
                                    },
                            {
                                        'source_monitor': 8477629,
                                        'source_nw_x_pixel': -6370937455275129708,
                                        'source_nw_y_pixel': -8172164111431499492,
                                        'source_pixel_width': -4931993526826165074,
                                        'source_pixel_height': -7728026191820243796,
                                        'rotation': -3442669430505424283,
                                        'virtual_nw_x_pixel': 1907195374,
                                        'virtual_nw_y_pixel': 944354278,
                                        'virtual_width': -1014526540,
                                        'virtual_height': 1373063368,
                                    },
                        ],
                },
                {
                    'description': 'É¦rҜШʝƷǃ˸ŶϩÜɬԙƙΪū&ȡĔ-ԄkǓĭǲҤƾƋώ',
                    'monitors': [
                            {
                                        'identifier': 8573828,
                                        'width': -5612386897072639260,
                                        'height': 1554529331060727182,
                                    },
                            {
                                        'identifier': 4911394,
                                        'width': 4046430451649106284,
                                        'height': 6976486299726200296,
                                    },
                            {
                                        'identifier': 9478656,
                                        'width': 2108169561723174092,
                                        'height': -5336173456166750085,
                                    },
                            {
                                        'identifier': -42375,
                                        'width': 1579214058858406549,
                                        'height': -484064830705773495,
                                    },
                            {
                                        'identifier': 2760909,
                                        'width': 3398458963573885456,
                                        'height': -6837714924154029464,
                                    },
                            {
                                        'identifier': 5666736,
                                        'width': 421376211327642879,
                                        'height': 4866253865581791652,
                                    },
                            {
                                        'identifier': 3622698,
                                        'width': -6093335284456230904,
                                        'height': -1941085675057621444,
                                    },
                            {
                                        'identifier': 4593284,
                                        'width': -735116229371409537,
                                        'height': -5291828832801097168,
                                    },
                            {
                                        'identifier': 1719047,
                                        'width': 2777431411827307193,
                                        'height': 4953719290491436832,
                                    },
                            {
                                        'identifier': 603524,
                                        'width': -6487276343443028086,
                                        'height': 774921471320375045,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 5100157,
                                        'source_nw_x_pixel': -1368232116310500764,
                                        'source_nw_y_pixel': -8370730338486183933,
                                        'source_pixel_width': -8496072344314070708,
                                        'source_pixel_height': -4978224511257752741,
                                        'rotation': -701977456585420159,
                                        'virtual_nw_x_pixel': -50226265,
                                        'virtual_nw_y_pixel': -1895938701,
                                        'virtual_width': 550913654,
                                        'virtual_height': -704913269,
                                    },
                            {
                                        'source_monitor': 7194208,
                                        'source_nw_x_pixel': -7500274940791205634,
                                        'source_nw_y_pixel': -3447392160114313741,
                                        'source_pixel_width': -3508065432273197746,
                                        'source_pixel_height': -2439330565821980576,
                                        'rotation': -922744776523362699,
                                        'virtual_nw_x_pixel': 203288531,
                                        'virtual_nw_y_pixel': 573886796,
                                        'virtual_width': 360164601,
                                        'virtual_height': 1579714769,
                                    },
                            {
                                        'source_monitor': 2171578,
                                        'source_nw_x_pixel': -5158236455306042953,
                                        'source_nw_y_pixel': -8261491172892772610,
                                        'source_pixel_width': -8237295797447984948,
                                        'source_pixel_height': -5635999583395076569,
                                        'rotation': -1213374772944188128,
                                        'virtual_nw_x_pixel': 47788615,
                                        'virtual_nw_y_pixel': -1305850057,
                                        'virtual_width': -1475988451,
                                        'virtual_height': -1747863788,
                                    },
                            {
                                        'source_monitor': 3632352,
                                        'source_nw_x_pixel': -1144933305615627190,
                                        'source_nw_y_pixel': -2716453447979902187,
                                        'source_pixel_width': -6685071499238180451,
                                        'source_pixel_height': -6911796947732947724,
                                        'rotation': -3286859647104257727,
                                        'virtual_nw_x_pixel': -610318086,
                                        'virtual_nw_y_pixel': 1295967567,
                                        'virtual_width': 343976191,
                                        'virtual_height': -189763303,
                                    },
                            {
                                        'source_monitor': 8109511,
                                        'source_nw_x_pixel': -8260745293096313669,
                                        'source_nw_y_pixel': -2099037017927843643,
                                        'source_pixel_width': -5563221366753305883,
                                        'source_pixel_height': -8747046943901518234,
                                        'rotation': -4121344439013813405,
                                        'virtual_nw_x_pixel': 1578046902,
                                        'virtual_nw_y_pixel': 110084597,
                                        'virtual_width': 41187228,
                                        'virtual_height': -1396881336,
                                    },
                            {
                                        'source_monitor': 9931401,
                                        'source_nw_x_pixel': -7600037616769806635,
                                        'source_nw_y_pixel': -9054583517878329366,
                                        'source_pixel_width': -4841338202044190514,
                                        'source_pixel_height': -7326900832217242428,
                                        'rotation': -8864316051626765725,
                                        'virtual_nw_x_pixel': 848230893,
                                        'virtual_nw_y_pixel': -1441477448,
                                        'virtual_width': -1579712145,
                                        'virtual_height': 682676872,
                                    },
                            {
                                        'source_monitor': 3444327,
                                        'source_nw_x_pixel': -8755378426197304331,
                                        'source_nw_y_pixel': -3441524364281988260,
                                        'source_pixel_width': -3216842214299216422,
                                        'source_pixel_height': -8441194316993510787,
                                        'rotation': -2521081554001464064,
                                        'virtual_nw_x_pixel': -580716223,
                                        'virtual_nw_y_pixel': 1195396993,
                                        'virtual_width': -67501058,
                                        'virtual_height': -814224917,
                                    },
                            {
                                        'source_monitor': 7363598,
                                        'source_nw_x_pixel': -681868590808082298,
                                        'source_nw_y_pixel': -8739310575273339549,
                                        'source_pixel_width': -2070742902109833270,
                                        'source_pixel_height': -7883128332037998794,
                                        'rotation': -5761006906495360941,
                                        'virtual_nw_x_pixel': -58877599,
                                        'virtual_nw_y_pixel': 1824864344,
                                        'virtual_width': 621487694,
                                        'virtual_height': -1252051876,
                                    },
                            {
                                        'source_monitor': 9844106,
                                        'source_nw_x_pixel': -506642942935011064,
                                        'source_nw_y_pixel': -6217191273454028086,
                                        'source_pixel_width': -2363903927727981039,
                                        'source_pixel_height': -7501587103774434791,
                                        'rotation': -2607238035367813287,
                                        'virtual_nw_x_pixel': -234482605,
                                        'virtual_nw_y_pixel': -227814248,
                                        'virtual_width': -1812960225,
                                        'virtual_height': 656925250,
                                    },
                            {
                                        'source_monitor': -594505,
                                        'source_nw_x_pixel': -7767150965287499520,
                                        'source_nw_y_pixel': -7181198426763735313,
                                        'source_pixel_width': -2299857511793192788,
                                        'source_pixel_height': -1928740680189452196,
                                        'rotation': -611938902023902027,
                                        'virtual_nw_x_pixel': -1971330104,
                                        'virtual_nw_y_pixel': 141309295,
                                        'virtual_width': 189571744,
                                        'virtual_height': -1298725179,
                                    },
                        ],
                },
                {
                    'description': 'ҰǼӷӵįJƳ¨ѡX3ΤŁɂλЧɣŠΕӒξĴ>ȓÀƔϻǓˌ\u03a2',
                    'monitors': [
                            {
                                        'identifier': 3109969,
                                        'width': -4844760063251820480,
                                        'height': 8831971457499595107,
                                    },
                            {
                                        'identifier': 8046002,
                                        'width': -5248483226465476212,
                                        'height': -4180483715555093247,
                                    },
                            {
                                        'identifier': 7364701,
                                        'width': 5842598945778246631,
                                        'height': 5920805436609374650,
                                    },
                            {
                                        'identifier': 2291120,
                                        'width': 5459939380434995753,
                                        'height': -5755668494105672586,
                                    },
                            {
                                        'identifier': 2661913,
                                        'width': -2041646393973188401,
                                        'height': 643120282254901540,
                                    },
                            {
                                        'identifier': 1937004,
                                        'width': 1343726509512638280,
                                        'height': -5339218512790741852,
                                    },
                            {
                                        'identifier': -568676,
                                        'width': -3824890268499300015,
                                        'height': -1776029313726988470,
                                    },
                            {
                                        'identifier': 4251782,
                                        'width': -4537947421630275492,
                                        'height': 5793538690606014373,
                                    },
                            {
                                        'identifier': 6575266,
                                        'width': 4408972839137800990,
                                        'height': -2205895245709272879,
                                    },
                            {
                                        'identifier': 1575277,
                                        'width': 671147125611338242,
                                        'height': -5245662677854339201,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4597126,
                                        'source_nw_x_pixel': -4320894978900010965,
                                        'source_nw_y_pixel': -4268216651877914884,
                                        'source_pixel_width': -1666539960569743144,
                                        'source_pixel_height': -6662961389201773064,
                                        'rotation': -3316711901462384133,
                                        'virtual_nw_x_pixel': 285644779,
                                        'virtual_nw_y_pixel': 1188839763,
                                        'virtual_width': 1418717231,
                                        'virtual_height': -1818242411,
                                    },
                            {
                                        'source_monitor': -45910,
                                        'source_nw_x_pixel': -5827243525915078215,
                                        'source_nw_y_pixel': -3933433804418941827,
                                        'source_pixel_width': -5043401091406941855,
                                        'source_pixel_height': -1070380791001800699,
                                        'rotation': -7109289866759945683,
                                        'virtual_nw_x_pixel': 435149013,
                                        'virtual_nw_y_pixel': -679518431,
                                        'virtual_width': -1572234150,
                                        'virtual_height': 580900578,
                                    },
                            {
                                        'source_monitor': 4919272,
                                        'source_nw_x_pixel': -143012844917328522,
                                        'source_nw_y_pixel': -9174945255790142821,
                                        'source_pixel_width': -7590519189773256086,
                                        'source_pixel_height': -5397444344721051994,
                                        'rotation': -2236329762699825674,
                                        'virtual_nw_x_pixel': 1727055364,
                                        'virtual_nw_y_pixel': 1603109277,
                                        'virtual_width': 1802203851,
                                        'virtual_height': 303280659,
                                    },
                            {
                                        'source_monitor': 8300378,
                                        'source_nw_x_pixel': -8735905369416874138,
                                        'source_nw_y_pixel': -3188390616359681117,
                                        'source_pixel_width': -7761052630965549596,
                                        'source_pixel_height': -85382775888954650,
                                        'rotation': -33026591461223944,
                                        'virtual_nw_x_pixel': 599462811,
                                        'virtual_nw_y_pixel': 1959065865,
                                        'virtual_width': 1084591118,
                                        'virtual_height': 245859174,
                                    },
                            {
                                        'source_monitor': 8164868,
                                        'source_nw_x_pixel': -6739396982658548025,
                                        'source_nw_y_pixel': -4567166024556063067,
                                        'source_pixel_width': -1094647339124779234,
                                        'source_pixel_height': -629201145088924538,
                                        'rotation': -2511218566528730649,
                                        'virtual_nw_x_pixel': 1448025534,
                                        'virtual_nw_y_pixel': 1959426963,
                                        'virtual_width': -1119563154,
                                        'virtual_height': -1900743448,
                                    },
                            {
                                        'source_monitor': 7345233,
                                        'source_nw_x_pixel': -5613764795348327700,
                                        'source_nw_y_pixel': -4618970730946190432,
                                        'source_pixel_width': -3387446976266041280,
                                        'source_pixel_height': -5744246988293629131,
                                        'rotation': -2261780066013548297,
                                        'virtual_nw_x_pixel': 750244817,
                                        'virtual_nw_y_pixel': 1016783624,
                                        'virtual_width': -696723727,
                                        'virtual_height': -1550480557,
                                    },
                            {
                                        'source_monitor': 4702594,
                                        'source_nw_x_pixel': -8194276883803861661,
                                        'source_nw_y_pixel': -1603970331889062395,
                                        'source_pixel_width': -7854356625369318454,
                                        'source_pixel_height': -7521112640948144736,
                                        'rotation': -5738061307199320172,
                                        'virtual_nw_x_pixel': -376403132,
                                        'virtual_nw_y_pixel': 1144442110,
                                        'virtual_width': -903718326,
                                        'virtual_height': 1510365620,
                                    },
                            {
                                        'source_monitor': 6563818,
                                        'source_nw_x_pixel': -7021176860374457943,
                                        'source_nw_y_pixel': -3807326969371099346,
                                        'source_pixel_width': -7543880119582926594,
                                        'source_pixel_height': -5121660042763490593,
                                        'rotation': -8132004286366696640,
                                        'virtual_nw_x_pixel': 299189565,
                                        'virtual_nw_y_pixel': 8636384,
                                        'virtual_width': 1357194338,
                                        'virtual_height': 868590056,
                                    },
                            {
                                        'source_monitor': 2826134,
                                        'source_nw_x_pixel': -7475048751157237220,
                                        'source_nw_y_pixel': -1910722453251297654,
                                        'source_pixel_width': -807861780816524481,
                                        'source_pixel_height': -7812881249652316724,
                                        'rotation': -3073609292979593084,
                                        'virtual_nw_x_pixel': 1318811571,
                                        'virtual_nw_y_pixel': 571364691,
                                        'virtual_width': -37078715,
                                        'virtual_height': -108041883,
                                    },
                            {
                                        'source_monitor': 8944627,
                                        'source_nw_x_pixel': -2907583523998033686,
                                        'source_nw_y_pixel': -209527699747562112,
                                        'source_pixel_width': -3990187633219441616,
                                        'source_pixel_height': -3594040780931410242,
                                        'rotation': -691138049943605259,
                                        'virtual_nw_x_pixel': 149920417,
                                        'virtual_nw_y_pixel': 1291500048,
                                        'virtual_width': -301440254,
                                        'virtual_height': -1779733609,
                                    },
                        ],
                },
                {
                    'description': 'U\x83ǧǣ\x86ҵÀлԄʵӒҿŽ6=гϓӎн\u0380ǲÅӁÅҢѬ©ǀƲӢ',
                    'monitors': [
                            {
                                        'identifier': 9735018,
                                        'width': -3565288092635792762,
                                        'height': 8769802901693614793,
                                    },
                            {
                                        'identifier': 8680405,
                                        'width': 8242998828102262801,
                                        'height': 8925778119013308278,
                                    },
                            {
                                        'identifier': 9415910,
                                        'width': 1886466944863506475,
                                        'height': -8807299321156979255,
                                    },
                            {
                                        'identifier': 588292,
                                        'width': 4090943301802778457,
                                        'height': 805019632292211042,
                                    },
                            {
                                        'identifier': 9382500,
                                        'width': -8595275411927952960,
                                        'height': -2194112475498389523,
                                    },
                            {
                                        'identifier': 913696,
                                        'width': 2410589674728141962,
                                        'height': 6343364224780059293,
                                    },
                            {
                                        'identifier': 8493920,
                                        'width': -6320302316401240625,
                                        'height': -6785583601232630020,
                                    },
                            {
                                        'identifier': 3664897,
                                        'width': 5105967693731877515,
                                        'height': 6221750717634622856,
                                    },
                            {
                                        'identifier': 3245962,
                                        'width': -6243424524158734669,
                                        'height': 5857038763107010770,
                                    },
                            {
                                        'identifier': -260144,
                                        'width': 3878983085630512899,
                                        'height': 7386410840106775083,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_monitor': 4448322,
                                        'source_nw_x_pixel': -3989714574696679646,
                                        'source_nw_y_pixel': -4466680902873645622,
                                        'source_pixel_width': -6000718610476667002,
                                        'source_pixel_height': -8392927090145217038,
                                        'rotation': -6128446243441159258,
                                        'virtual_nw_x_pixel': -908740396,
                                        'virtual_nw_y_pixel': -1940320600,
                                        'virtual_width': 208558395,
                                        'virtual_height': 769677383,
                                    },
                            {
                                        'source_monitor': 1453714,
                                        'source_nw_x_pixel': -6836813780056055678,
                                        'source_nw_y_pixel': -5678254330289943806,
                                        'source_pixel_width': -5194569041806014698,
                                        'source_pixel_height': -8605632886561755822,
                                        'rotation': -6383258037168844955,
                                        'virtual_nw_x_pixel': -73008184,
                                        'virtual_nw_y_pixel': 1446795713,
                                        'virtual_width': -1132090651,
                                        'virtual_height': 363638674,
                                    },
                            {
                                        'source_monitor': 4227522,
                                        'source_nw_x_pixel': -521221986298074283,
                                        'source_nw_y_pixel': -4314425594897536405,
                                        'source_pixel_width': -8182793816456317078,
                                        'source_pixel_height': -4276859211617061965,
                                        'rotation': -1446921424040033872,
                                        'virtual_nw_x_pixel': 1982255293,
                                        'virtual_nw_y_pixel': 1752914412,
                                        'virtual_width': -91960417,
                                        'virtual_height': -390065865,
                                    },
                            {
                                        'source_monitor': 3657095,
                                        'source_nw_x_pixel': -178893654008260836,
                                        'source_nw_y_pixel': -5946935079073012036,
                                        'source_pixel_width': -1925473582015530967,
                                        'source_pixel_height': -9184937284741332892,
                                        'rotation': -7270975319197751477,
                                        'virtual_nw_x_pixel': -708682214,
                                        'virtual_nw_y_pixel': 1182191628,
                                        'virtual_width': -1660310571,
                                        'virtual_height': 882663797,
                                    },
                            {
                                        'source_monitor': 5998417,
                                        'source_nw_x_pixel': -7848617970165755400,
                                        'source_nw_y_pixel': -4264115606802902110,
                                        'source_pixel_width': -2137086015078005731,
                                        'source_pixel_height': -5550821443535242322,
                                        'rotation': -7070954814215093685,
                                        'virtual_nw_x_pixel': -1623100300,
                                        'virtual_nw_y_pixel': 208044879,
                                        'virtual_width': -1045863930,
                                        'virtual_height': 260392748,
                                    },
                            {
                                        'source_monitor': 9597063,
                                        'source_nw_x_pixel': -1873697721543321330,
                                        'source_nw_y_pixel': -1555960313916022599,
                                        'source_pixel_width': -7962176494591934484,
                                        'source_pixel_height': -3500503806557839932,
                                        'rotation': -9145185471438248672,
                                        'virtual_nw_x_pixel': -827551576,
                                        'virtual_nw_y_pixel': 638938197,
                                        'virtual_width': 1631739643,
                                        'virtual_height': -1618421383,
                                    },
                            {
                                        'source_monitor': 4806425,
                                        'source_nw_x_pixel': -6804492570435690155,
                                        'source_nw_y_pixel': -8150829867071049249,
                                        'source_pixel_width': -7538499629816706992,
                                        'source_pixel_height': -3031834988092092987,
                                        'rotation': -542256404212924416,
                                        'virtual_nw_x_pixel': -1512221399,
                                        'virtual_nw_y_pixel': 1926200948,
                                        'virtual_width': -1646575558,
                                        'virtual_height': -1229048682,
                                    },
                            {
                                        'source_monitor': 8520552,
                                        'source_nw_x_pixel': -7148504580071875728,
                                        'source_nw_y_pixel': -7806636161221411035,
                                        'source_pixel_width': -5987424172632653895,
                                        'source_pixel_height': -3751948082521292329,
                                        'rotation': -8886993867697241554,
                                        'virtual_nw_x_pixel': 1839358251,
                                        'virtual_nw_y_pixel': -787056834,
                                        'virtual_width': -708281283,
                                        'virtual_height': -582939158,
                                    },
                            {
                                        'source_monitor': 224828,
                                        'source_nw_x_pixel': -3996651304903140795,
                                        'source_nw_y_pixel': -8001244127520711451,
                                        'source_pixel_width': -1925666752794682205,
                                        'source_pixel_height': -2380782317103486537,
                                        'rotation': -2073553856544528696,
                                        'virtual_nw_x_pixel': 1414838766,
                                        'virtual_nw_y_pixel': -1685991025,
                                        'virtual_width': 852928679,
                                        'virtual_height': -1141228258,
                                    },
                            {
                                        'source_monitor': 9831094,
                                        'source_nw_x_pixel': -3083712964765962623,
                                        'source_nw_y_pixel': -961656804486800304,
                                        'source_pixel_width': -6344233009368051958,
                                        'source_pixel_height': -1443422103879040201,
                                        'rotation': -7735367752881302431,
                                        'virtual_nw_x_pixel': 10060704,
                                        'virtual_nw_y_pixel': 1684052358,
                                        'virtual_width': 757537655,
                                        'virtual_height': -305851155,
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
                                        'identifier': 1340775,
                                        'width': -8774088380018642479,
                                        'height': 2842112330821750734,
                                    },
                        ],
                    'screen': [
                            {
                                        'source_nw_x_pixel': -5174461496256983061,
                                        'source_nw_y_pixel': -5740141445273815972,
                                        'source_pixel_width': -5170580221774235075,
                                        'source_pixel_height': -6100606154419654553,
                                        'rotation': -8663507526909926056,
                                        'virtual_nw_x_pixel': 109840299,
                                        'virtual_nw_y_pixel': 834157792,
                                        'virtual_width': -740017653,
                                        'virtual_height': 445213676,
                                    },
                        ],
                },
            ],

        },
    ),
]
