# GENERATED CODE - DO NOT MODIFY

"""
Tests for the monitor module.
Extension petronia.core.api.native.monitor, Version 1.0.0
"""

# pylint: disable=too-many-lines,line-too-long,unused-import

import unittest
from typing import Sequence, Tuple, Dict, Any
from petronia_common.util import UserMessage, i18n, STANDARD_PETRONIA_CATALOG
from .. import monitor


class MonitorTest(unittest.TestCase):
    """
    Tests for Monitor
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in MONITOR_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitor.parse_data(test_data)
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
        for test_name, test_data in MONITOR_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.Monitor.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


MONITOR_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='identifier', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='description', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_width', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='real_pixel_height', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_x', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='dpi_y', name='Monitor'),
            ),
            (
                'Required field {field_name} in {name}',
                dict(field_name='supports_rotation', name='Monitor'),
            ),

        ),
    ),

]


MONITOR_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'identifier': 7022958,
            'description': 'ԨĭԅŅοуζȹӱϩ}ȑЛïʴéƴО\x88ϚĶ=υʜәNπΩ¸˚',
            'real_pixel_width': -8234285153921145772,
            'real_pixel_height': -3817316671629030142,
            'dpi_x': 445133478959219823,
            'dpi_y': 5586608861039386066,
            'supports_rotation': False,
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'identifier': 3059096,

            'description': '',

            'real_pixel_width': -7533255830084794680,

            'real_pixel_height': -7692690903976458626,

            'dpi_x': 181026334461624917,

            'dpi_y': 6297558693236480111,

            'supports_rotation': False,

        },
    ),
]


class ActiveMonitorsStateTest(unittest.TestCase):
    """
    Tests for ActiveMonitorsState
    """
    def test_parse_bad_data(self) -> None:
        """Data driven tests with validation problems."""
        self.maxDiff = None  # pylint: disable=C0103
        for test_name, test_data, messages in ACTIVE_MONITORS_STATE_BAD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.ActiveMonitorsState.parse_data(test_data)
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
        for test_name, test_data in ACTIVE_MONITORS_STATE_GOOD_PARSE_DATA_TESTS:
            with self.subTest(name=test_name):
                res = monitor.ActiveMonitorsState.parse_data(test_data)
                self.assertIsNone(res.error)
                self.assertEqual(test_data, res.result.export_data())


ACTIVE_MONITORS_STATE_BAD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any], Sequence[Tuple[str, Dict[str, Any]]]],
] = [

    (
        'all-fields-missing',
        {},
        (
            (
                'Required field {field_name} in {name}',
                dict(field_name='monitors', name='ActiveMonitorsState'),
            ),

        ),
    ),

]


ACTIVE_MONITORS_STATE_GOOD_PARSE_DATA_TESTS: Sequence[
    Tuple[str, Dict[str, Any]],
] = [
    (
        'all-fields-present',
        {
            'monitors': [
                {
                    'identifier': 5947748,
                    'description': 'bēѡΕɕԭŹɵҟӶѢӒͷʬ˸țрӕƮɸτŤòϬȁ˝хɭӹǷ',
                    'real_pixel_width': -8586474190156729421,
                    'real_pixel_height': -7912628184546893638,
                    'dpi_x': 8176465654671109753,
                    'dpi_y': 7791133640409086377,
                    'supports_rotation': True,
                },
                {
                    'identifier': 6068333,
                    'description': 'ɍɖƦӣźʴɳԜӞÅЋә˦БҾҴǴʂ¸UɥīȒʓѼɑϭȵɗǟ',
                    'real_pixel_width': -2586885383695493016,
                    'real_pixel_height': -180865606365543197,
                    'dpi_x': 5391634388240467591,
                    'dpi_y': 2462253475105887232,
                    'supports_rotation': True,
                },
                {
                    'identifier': 5206940,
                    'description': 'ȻëЖǹˠћΰӲҚӇώцĻɞʋ ϭѤΏ½}áɡqɺǅʚӒǏп',
                    'real_pixel_width': -3798061799763812809,
                    'real_pixel_height': -1027239965077889927,
                    'dpi_x': 7288677382877853537,
                    'dpi_y': 4335287414248352287,
                    'supports_rotation': True,
                },
                {
                    'identifier': 681270,
                    'description': 'Ф3\\\u0380ĿŝǂĉʀӴÑԘßОӤğbɏƁό˖ѝaϺКͽ϶\u0383ǌ҆',
                    'real_pixel_width': -784579361843011538,
                    'real_pixel_height': -5122352289544442696,
                    'dpi_x': 2359092310037798939,
                    'dpi_y': 1306813658626762012,
                    'supports_rotation': False,
                },
                {
                    'identifier': -980519,
                    'description': 'ƞƹεʬǭћOѥɧʉ\u0381ȖȐ˥ҀӉǞƧʨŁ˯Ə\x86ӨΥľЪӿђҐ',
                    'real_pixel_width': -4510646730779035776,
                    'real_pixel_height': -6260236081430131969,
                    'dpi_x': 4376847007754414200,
                    'dpi_y': 3024102725123439203,
                    'supports_rotation': True,
                },
                {
                    'identifier': 9886767,
                    'description': 'ɚķϊχҶ§ċªvЏɔʈҞǢÎӳåǕТˬԙɈBԁǕĝǤˀԈÏ',
                    'real_pixel_width': -4375151991980682429,
                    'real_pixel_height': -9019734289303856455,
                    'dpi_x': 5965032844809031851,
                    'dpi_y': 1529131660780228675,
                    'supports_rotation': True,
                },
                {
                    'identifier': 7929098,
                    'description': 'ΆǪЪȻƑ¼ԧӘѓҨȉAӉ1ƭŰԢӬѨFɞ·-âѝƄãƁɽ˕',
                    'real_pixel_width': -6250708013101830234,
                    'real_pixel_height': -6374239576726008446,
                    'dpi_x': 3282508584064884218,
                    'dpi_y': 6905141957501896605,
                    'supports_rotation': False,
                },
                {
                    'identifier': 9918864,
                    'description': 'ˈŕ_ďҚƝҕӳȀƟɿŻΑϫǊpƤ ΐĒҞǘј҈ϘǁýхǙŨ',
                    'real_pixel_width': -5245187520731901303,
                    'real_pixel_height': -5385555821861108911,
                    'dpi_x': 8190398657641981232,
                    'dpi_y': 7950080659401555003,
                    'supports_rotation': False,
                },
                {
                    'identifier': 3627868,
                    'description': 'ËŹѳqҼƃȍϴѷҹӃӼȷή¥ӷˑӷϖͶˑԛѪʱƀ\x96ȤƔłԔ',
                    'real_pixel_width': -948243982262023582,
                    'real_pixel_height': -5188560988853636237,
                    'dpi_x': 5473094507044733135,
                    'dpi_y': 8008102802541220257,
                    'supports_rotation': False,
                },
                {
                    'identifier': 2237979,
                    'description': 'ԙÕɹ/ŋʸ˟ʕɞ\x9e¸ʠčļыÁ\x84*ӿǞľͻ\x82²ǡɂ\x87Ҷœ˧',
                    'real_pixel_width': -6594128540674871696,
                    'real_pixel_height': -5990235232708265306,
                    'dpi_x': 999688895173051752,
                    'dpi_y': 5379415817344252391,
                    'supports_rotation': True,
                },
            ],
        },
    ),
    (
        'bare-minimum-fields-present',
        {

            'monitors': [
            ],

        },
    ),
]
